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


