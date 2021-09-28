# SinglishERG

A branch of the English Resource Grammar (ERG) that is used for Singlish.

These are the files that have been changed since they have been cloned from the ERG trunk.
Refer to config and singlish.tdl to see which files are in use.

To compile this grammar using LKB most conveniently:
* clone this whole directory (rename it as singlish) into the erg_trunk folder 
* move the contents of lkb in this repository into the trunk's lkb folder
* Under Lkb Top's Advanced menu, select 'Evaluate Lisp expression' and type in '(push :singlish \*features\*)'
* Select the script file that was copied from here into trunk's lkb folder to load complete grammar
