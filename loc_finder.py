#!/usr/bin/python

__author__ = 'asos'
import sys
import getopt
import os
import re
import webbrowser
import traceback

import nltk
from nltk.corpus import wordnet as wn
import pandas as pd

from config import Config


global_word_pull = set()
output_format = "txt"

def main(argv):
    inputfile = ''
    outputfile = ''
    generate_localizable_strings = False
    func_to_search = [search_for_loc]
    global output_format

    try:
        opts, args = getopt.getopt(argv, "hi:o:sNc", ["ifile=", "ofile=", "localizable_strings", "use_nltk", "csv"])
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
        elif opt in ("-c", "--csv"):
            output_format = "csv"

    if (output_format == "csv"):
        csv_result_dict = recursively_check(inputfile, search_for_loc, output_format)
        result_df = pd.DataFrame.from_dict(csv_result_dict)
        result_df.to_csv(outputfile)

    elif (output_format == "txt"):
        out = []
        for function in func_to_search:
            out.append({'=============================================================================================':
                            "..."})
            out.append(recursively_check(inputfile, function))
        for item in out:
            output(outputfile, item, generate_localizable_strings)

def hlp_str():
    '''Help string'''
    return 'USAGE: \nloc_finder.py \n-i <inputfile> \n-o <outputfile> \n-s [generate Localizable.strings?] \
    \n-N [should I use natural language processing to extract all lines which may require localization? (Much slower)]'


def recursively_check(project_folder, func_to_search, output_format="txt"):
    '''Recursively scan through folders structure'''
    result = {}

    if (output_format == 'csv'):
        result = {"Where": [], "What": [], "Description": []}

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
                            if (output_format == 'csv'):
                                result["Where"].append(filename)
                                result["What"].append(match)
                                result["Description"].append(file_path)
                            elif (output_format == 'txt'):
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
            if not match:
                continue
            group = match.group(1)
            if len(group) > 0 and not contains_forbidden_patterns(group):
                try:
                    tokens = nltk.word_tokenize(group)
                    if len(tokens) > 0:
                        for word in tokens:
                            morf = wn.morphy(word)
                            if morf and len(str(morf)) > 1:
                                if (output_format == "csv") | (group not in global_word_pull):
                                    result.append(group)
                                    global_word_pull.add(group)
                                break
                except:
                    print ("Unexpected error:{0}".format(sys.exc_info()))
                    traceback.print_tb(sys.exc_info()[2])
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
                    if (output_format == "csv") | (group not in global_word_pull):
                        result.append(group)
                        global_word_pull.add(group)

    return result

if __name__ == "__main__":
    main(sys.argv[1:])