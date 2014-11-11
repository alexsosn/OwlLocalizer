OwlLocalizer
============

<a title="By Pearson Scott Foresman [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File%3AScreech_owl_1_(PSF).png"><img width="256" alt="Screech owl 1 (PSF)" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/45/Screech_owl_1_%28PSF%29.png/256px-Screech_owl_1_%28PSF%29.png"/></a>

Application allows you to search for strings that may need localisation in iOS project. Uses natural language processing and heuristics to exclude urls, dates, autolayouts, predicates etc. Have several modes of search and allows to find strings in code sources, plists and UI files (.xib, .storyboards).

## Usage

```sh
 python loc_finder.py 

 -i -- ifile <inputfile> 

 -o --ofile <outputfile> 

 -s --localizable_strings [Generate Localizable.strings or just create list of strings?]

 -N --use_nltk [Should I use natural language processing to extract all lines which may require localization? (Slower)]
```