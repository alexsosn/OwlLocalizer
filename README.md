<p align="center">
<img src="owl.png" alt="OwlLocalizer: Smart Localization Tool for iOS Developers" />
<br><font color="gray" size="-3">source: <a href="https://upload.wikimedia.org/wikipedia/commons/4/4d/Tetradrachm_Athens_450_reverse_CdM_Paris-transparent.png">wikimedia</a></font>
</p>


OwlLocalizer: Smart Localization Tool for iOS Developers
============

### Problem
You need to add localization support to the iOS project which was developed with assumption that only english-speaking users will use it. Or even worse - someone started implementing localization and gave up halfway.

### Solution
The tool allows you to search for strings that *may need* localisation in iOS project. Uses natural language processing and heuristics to exclude urls, dates, autolayouts, predicates etc. It has several modes of search and allows to find strings in code sources, plists and UI files.

## The goal of the project
* **Unrealistic goal:** Find all strings in iOS project, which requires localization regardless of the place in the project.
* **More realistic:** Suggest strings, which may require localization.

## Features
- [x] Objective-C, Objective-C++, Swift support.
- [x] .xib, .storyboards support.
- [x] parses .plist and .string files.
- [x] excludes CocoaPods, .git and Build folders from search.
- [x] 'Heuristic mode': looks for predefined patterns like names of UI elements in storyboards or ```NSLocalizedString()``` in objective-c sources. 
- [x] 'AI mode': looks for all strings which are similar to natural language.
- [x] Output formats:
    - [x] plain text lists of suspicious strings
    - [x] CSV table
    - [x] localizable.strings
- [x] Easy configuration: just add your own regular expressions, file types and folders to the ```config.py```.

## Usage


 >python loc_finder.py 

> -i -- ifile <inputfile> 

> -o --ofile <outputfile> 

> -s --localizable_strings [Generate Localizable.strings or just create list of strings?]

> -N --use_nltk [AI mode enabled: use natural language processing to extract all lines which may require localization? (Slower)]

> -c --csv set output format to csv. Only [NLTK] parsing will be used with this option. Output format: [Description,What,Where]. Duplicates will not be removed.

> **Examples:** 
>> python loc_finder.py -i my-ios-project-folder -o local.csv -Nc
>
>> python loc_finder.py -i my-ios-project-folder -o localizable.strings -s

> To add your own regular expressions or folders to ignore or change settings of file formats see config.py.

## NLTK dependencies installation

If after running the script you've got the following error

```bash
Unexpected error:(<class 'LookupError'>, LookupError("\n**********************************************************************\n  Resource 'tokenizers/punkt/PY3/english.pickle' not found.\n  Please use the NLTK Downloader to obtain the resource:  >>>\n  nltk.download()\n  Searched in:\n    - '/Users/gigaset/nltk_data'\n    - '/usr/share/nltk_data'\n    - '/usr/local/share/nltk_data'\n    - '/usr/lib/nltk_data'\n    - '/usr/local/lib/nltk_data'\n    - ''\n**********************************************************************",), <traceback object at 0x1084fc408>)
```
you probably don't have some [NLTK] packages installed. Script will try to start **NLTK package downloader**. Do the following:

* When NLTK package downloader started go to 'Corpora' tab and select 'wordnet' from under the 'Identifier' column (WordNet).
* Click Download and it will install the necessary files.
* Go to the 'Models' tab and select 'punkt' from under the 'Identifier' column.
* Then click Download and it will install the necessary files.
* Close NLTK package downloader.
* Restart script. 

## Version
0.0.2

## Requirements

* [Python 3.4]
* [NLTK]
* [Pandas] 0.16.0

## Known bugs

* [ ] No support for multi-line strings.
* [ ] Escaped symbols can be escaped twice (``` \n -> \\n ```). 

## Todo

* [ ] Add mode to find only non-localized content, which is not present in localizable.strings yet. 
* [ ] Add handling for ```localizedStringForKey:```.
* [ ] Context awareness / Abstract Syntactic Tree awareness.
* [ ] Add mode to exclude NSErrors.
* [ ] Add mode with context included.
* [ ] Exclude unit tests from search by default.

[NLTK]: http://www.nltk.org/
[Python 3.4]: https://www.python.org/download/releases/3.4.0/
[Pandas]: https://pypi.python.org/pypi/pandas