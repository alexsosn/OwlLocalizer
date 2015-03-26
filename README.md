
OwlLocalizer
============

Application allows you to search for strings that may need localisation in iOS project. Uses natural language processing and heuristics to exclude urls, dates, autolayouts, predicates etc. Have several modes of search and allows to find strings in code sources, plists and UI files (.xib, .storyboards).

## Ultimate goal of project
> Find all strings in iOS project, which requires localization regardless of whether they are marked using NSLocalizedString(...) or not.

## Usage


 >python loc_finder.py 

> -i -- ifile <inputfile> 

> -o --ofile <outputfile> 

> -s --localizable_strings [Generate Localizable.strings or just create list of strings?]

> -N --use_nltk [Should I use natural language processing to extract all lines which may require localization? (Slower)]

> -c --csv set output format to csv. Only NLTK parsing will be used with this option. Output format: [Description,What,Where]. Duplicates will not be removed.

> **Examples:** 
>> python loc_finder.py -i my-ios-project-folder -o local.csv -Nc
>
>> python loc_finder.py -i my-ios-project-folder -o localizable.strings -s

>To add your own regular expressions or folders to ignore or change settings of file formats see config.py.

## Version
0.0.2

## Requirements

* Python 3.4
* NLTK
* Pandas 0.16.0

## Todo

* Add handling for localizedStringForKey:
* Context awareness / AST awareness
* Multi-line strings.
* Do not include unit tests in search.
