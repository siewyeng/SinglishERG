# SinglishERG

A branch of the English Resource Grammar (ERG) that is used for Singlish. Created as a Master's Research project.

These are the files that have been changed since they have been cloned from the ERG trunk.
Refer to config and singlish.tdl to see which files are in use.

To compile this grammar using LKB most conveniently:
* download this whole directory (rename it as singlish) into the erg_trunk folder 
* move the contents of lkb in this repository into the trunk's lkb folder
* Under Lkb Top's Advanced menu, select 'Evaluate Lisp expression' and type in '(push :singlish \*features\*)'
* Select the script file that was copied from here into trunk's lkb folder to load complete grammar

To compile this grammar using ace:
* download this whole directory (rename it as singlish) into the erg_trunk folder
* move 'singlish.tdl' out to the trunk level
* with the terminal at trunk directory, use the config file from singlish and compile grammar
* * eg. 'ace -G singlish.dat -g singlish/config.tdl'

To check the semantics:
* echo "sentence" | ace -g [grammar].dat -Tfq

And to generate in another grammar:
* echo "sentence" | ace -g [grammar1].dat -Tfq | ace -g [grammar2].dat -e
* cat [mrs] | ace -g [grammar2].dat -e
* to change the generation root, add "-r [root]" to the command
* and add "--disable-subsumption-test" for easier generation
### Data
Data was extracted from examples on Wiktionary pages with words that were marked to be Singlish. It includes also the other non-Singlish definitions and usages of the words. The example sentences include some that are offensive and racist but they not taken out as it reflects how this variety is used.

To parse the data using ace (parts in brackets are optional)
* To parse with only top tree: cat wikiexamples_next300.txt | ace (--max-words=20) -g singlish.dat -Tf1(> output.txt)
* To remove lines starting with "#": grep -vP "^#" wikiexamples_next300.txt | ace...

