## Data Directory
This directory contains 3 main folders: wikidata, trees and skeletons

### wikidata
This directory contains the following:
* `get_examples.py`: the python file used to extract the example sentences from `singlish-wiktionary.json`
* `singlish-wiktionary.json`: a json file containing the extracted wiktionary extries associated with Singlish
* `wikiexamples.txt`: the examples extracted through get_examples.py
* `wikiexamples_*`: the sentences from `wikiexamples.txt` where each sentence is given a new line. In sentences containing direct speech, only the direct speech is used.
* `wikiparsing_results` contains the results of parsing the `wikiexamples_*` sentences. The files are named according to the grammar used (`en` for standard English or `sg` for Singlish) and
whether they only take sentences with 10 or less words, or 20 or less words, or if there is no restriction. The number at the top of the file represents
the number of sentences that parsed / the number of sentences that did not parse given the restriction in length.
### trees
The `trees` directory contains treebanked results for 30 sentences from wikidata. 
* `30sent_blank` contains the untreebanked versions of the 30 sentences for a fresh slate to be used if treebanking needs to be done again
* `UWH` in the folder names refer to whether the Unknown Word Handling feature was used. The feature, if used, assigns parts of speech to unknown words so that they can also be parsed
* `lex` indicates whether additional lexicon was added for the previously unknown words within the 30 sentences
* `_en` or `_sg` refers to the grammar used
* In each folder, the directory `result` contains the correctly parsed sentences that were treebanked and `tree` contains comments made during treebanking

### skeletons
This directory contains the synthetic sentences used to test for different phenomena in the grammar.
