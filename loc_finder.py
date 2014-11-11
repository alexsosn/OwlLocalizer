#!/usr/bin/python

__author__ = 'asos'
import sys, getopt, os, re
import nltk, webbrowser
from nltk.corpus import wordnet as wn
from config import Config

global_word_pull = set()

def main(argv):
    inputfile = ''
    outputfile = ''
    generate_localizable_strings = False
    func_to_search = [search_for_loc]
    try:
        opts, args = getopt.getopt(argv,"hi:o:sN",["ifile=","ofile=","localizable_strings", "use_nltk"])
    except getopt.GetoptError:
        print (hlp_str())
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print (hlp_str())
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-s", "--localizable_strings"):
            generate_localizable_strings = True
        elif opt in ("-N", "--use_nltk"):
            func_to_search.append(search_for_all_strings)

    out = []
    for function in func_to_search:
        out.append({'=============================================================================================':
                        "..."})
        out.append(recursively_check (inputfile, function))
    for item in out:
        output(outputfile, item, generate_localizable_strings)

def hlp_str():
    '''Help string'''
    return 'USAGE: \nloc_finder.py \n-i <inputfile> \n-o <outputfile> \n-s [generate Localizable.strings?] \
    \n-N [should I use natural language processing to extract all lines which may require localization? (Much slower)]'

def recursively_check(project_folder, func_to_search):
    '''Recursively scan through folders structure'''
    result = {}

    for root, subdirs, files in os.walk(project_folder, topdown=True):
        subdirs[:] = [d for d in subdirs if d not in set(Config.excluded_folders)]

        for filename in files:
            if "-Info.plist" in filename: continue

            file_path = os.path.join(root, filename)

            file_name_no_ext, file_ext = os.path.splitext(filename)
            if file_ext in Config.allowed_formats:
                with open(file_path, 'rb') as f:
                    for line in f:
                        for match in func_to_search(str(line), file_ext):
                            if not match in result:
                                result[match] = []
                            result[match].append(filename)

    return result

def output(output_file, result, generate):
    '''Generate output file'''
    if generate:
        with open(output_file, 'a') as f:
            for key, value in result.items():
                f.write('"{0}" = "{1}";\n'.format(key, key))

    else:
        rev_index = {}
        for key, value in result.items():
            for item in value:
                if not item in rev_index:
                    rev_index[item] = []
                rev_index[item].append(key)
        already_remembered = set()
        with open(output_file, 'a', encoding='utf-8') as f:
            for key, value in rev_index.items():
                f.write('\n======= %s =======\n' % str(key))
                for item in value:
                    if not item in already_remembered:
                        f.write('%s\n' % item)
                        already_remembered.add(item)


def contains_forbidden_patterns(string):
    for regexp in Config.excluded_patterns:
        for match in re.finditer(regexp, string):
            if match :
                return True
    return False

def search_for_all_strings(line, file_format):
    '''Search for all strings with NLTK'''
    result = []
    for regexp in Config.excluded_lines:
        for match in re.finditer(regexp, line):
            if match:
                return([])

    for regexp in Config.strings_patterns[file_format]:
        for match in re.finditer(regexp, line):
            if match :
                group = match.group(1)
                if len(group) > 0:
                    try:
                        if not contains_forbidden_patterns(group):
                            tokens = nltk.word_tokenize(group)
                            if len(tokens) > 0:
                                for word in tokens:
                                    morf = wn.morphy(word)
                                    if morf and len(str(morf))>1:
                                        if group not in global_word_pull:
                                            result.append(group)
                                            global_word_pull.add(group)
                                        break
                    except:
                        url = os.path.join(os.path.split(os.path.realpath(__file__))[0] + "/nltk_info.html")
                        print("See here for installation instructions:\n" + url)
                        webbrowser.open_new(url)

                        nltk.download()
                        sys.exit(2)

    return result

def search_for_loc(line, file_format):
    '''Search with specific regular expressions for occurences of localized strings in line'''
    result = []
    for regexp in Config.evristics[file_format]:
        for match in re.finditer(regexp, line):
            if match :
                group = match.group(1)
                if len(group) > 0:
                    if group not in global_word_pull:
                        result.append(group)
                        global_word_pull.add(group)

    return result

if __name__ == "__main__":
    main(sys.argv[1:])