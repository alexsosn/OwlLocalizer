<h5 align="center">
<img src="owl.png" alt="OwlLocalizer: Smart Localization Tool for iOS Developers" />
<font color="gray">source: <a href="https://upload.wikimedia.org/wikipedia/commons/4/4d/Tetradrachm_Athens_450_reverse_CdM_Paris-transparent.png">wikimedia</a></font>
</h5>


OwlLocalizer: Smart Localization Tool for iOS Developers
============

The tool allows you to search for strings that may need localisation in iOS project. Uses natural language processing and heuristics to exclude urls, dates, autolayouts, predicates etc. It has several modes of search and allows to find strings in code sources (Objective-C, Objective-C++, Swift), plists and UI files (.xib, .storyboards).

## The goal of the project
* **Unrealistic goal:** Find all strings in iOS project, which requires localization regardless of the place in the project.
* **More realistic:** Suggest strings, which may require localization.

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

> To add your own regular expressions or folders to ignore or change settings of file formats see config.py.

## NLTK dependencies installation

If you got an error

```bash
Unexpected error:(<class 'LookupError'>, LookupError("\n**********************************************************************\n  Resource 'tokenizers/punkt/PY3/english.pickle' not found.\n  Please use the NLTK Downloader to obtain the resource:  >>>\n  nltk.download()\n  Searched in:\n    - '/Users/gigaset/nltk_data'\n    - '/usr/share/nltk_data'\n    - '/usr/local/share/nltk_data'\n    - '/usr/lib/nltk_data'\n    - '/usr/local/lib/nltk_data'\n    - ''\n**********************************************************************",), <traceback object at 0x1084fc408>)
```
you probably don't have some NLTK packages installed. Script will try to start **NLTK package downloader**. Do following:
* Go to 'Corpora' tab and select 'wordnet' from under the 'Identifier' column (WordNet).
* Click Download and it will install the necessary files.
* Go to the 'Models' tab and select 'punkt' from under the 'Identifier' column.
* Then click Download and it will install the necessary files.
* Restart script. 

## Version
0.0.2

## Requirements

* Python 3.4
* NLTK
* Pandas 0.16.0

## Known bugs

* No support for multi-line strings.
* Escaped symbols can be escaped twice (``` \n -> \\n ```). 

## Todo

* Swift support.
* Add mode to find only non-localized content, which is not present in localizable.strings yet. 
* Add handling for ```localizedStringForKey:```.
* Context awareness / Abstract Syntactic Tree awareness.
* Add mode to exclude NSErrors.
* Add mode with context included.
* Multi-line strings.
* Exclude unit tests from search.
