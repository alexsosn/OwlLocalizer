OwlLocalizer
============

Application allows you to search for strings that may need localisation in iOS project. Uses natural language processing and heuristics to exclude urls, dates, autolayouts, predicates etc. Have several modes of search and allows to find strings in code sources, plists and UI files (.xib, .storyboards).

## Usage

```sh
 python loc_finder.py 

 -i -- ifile <inputfile> 

 -o --ofile <outputfile> 

 -s --localizable_strings [Generate Localizable.strings or just create list of strings?]

 -N --use_nltk [Should I use natural language processing to extract all lines which may require localization? (Slower)]
```

## Version
0.0.1

## Todo

* Add handling for localizedStringForKey:
* Context awareness
* Tests
* Multi-line strings
* ...
