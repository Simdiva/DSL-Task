VarDial - DSL Shared Task 2015 (DSL Corpus Collection v2.0)

Website: http://corporavm.uni-koeln.de/vardial/sharedtask.html
Contact: Liling Tan <dsl.sharedtask@gmail.com>

Training and Development data: 

The DSLCC comprises news data from various corpora to emulate the diverse news 
content across different languages.


== Format Description ==

The training and development data contains 3 files (including this README).
i. 		devel.txt
ii. 	train.txt
iii.	README.md

The train.txt contains 18,000 sentences for each language. 
The devel.txt contains 2,000 sentences for each language.
All sentences are encoding in latin script UTF-8.

Each line in the .txt files are tab-delimited in the format:
sentence<tab>language-label

==Langauges==

- **South-Eastern Slavic**
 - Bulgarian (bg)
 - Macedonian (mk)
- **South-Western Slavic**
 - Bosnian (bs)
 - Croatian (hr)
 - Serbian (sr)
- **West Slavic**
 - Czech (cz)
 - Slovak (sk)
- **Spanish**
 - Argentine Spanish (es_AR)
 - Peninsular Spanish (es_ES)
- **Portuguese**
 - Brazilian Portuguese (pt-BR)
 - European Portuguese (pt-PT)
- **Austronesian**
 - Indonesian (id)
 - Malay (my)
 
To emulate a realistic language identification setup additional texts from 
various languages are added to the data set. They are labelled with the language
code (xx)


== Evaluation ==

The test data realeased on June 2015, it will only contain sentences without
its language/variety label.

!!! IMPORTANT, please note the following to facilitate the evaluation !!!

(1) provide the system output as how the training and development data was 
formatted, without changing the order of the test sentences:
sentence<tab>language-label

(2) Please name your submission files with the following convention,
all in lowercase:

	<team_name>-<system_name>-<open_or_close>-<run#>.txt

For example, if your team_name is "USAAR" , system_name is "DisLang" and it's an
open submission and it's the 1st run that you want to submit, the submission
file should be as such:
	
	usaar-dislang-open-normal-run1.txt


(3) Please also compress ALL run submissions into a single file and send it to
dsl.sharedtask@gmail.com before the submission deadline (23 Apr), please name
compressed file in the following format: (team_name-system-name.zip)
For example:

	usaar-dislang.zip

(4) Do specify in the email title when sending the compression submission file,
e.g. (team_name DSL2015 submission)
Title: USAAR DSL2015 submission

(5) Each team is ONLY allowed to submit 3 runs for closed and/or 3 runs for 
open task, (6 runs in total for teams participating in both)

(6) Along with the systems runs, submit a short description of your system.
This is to facilitate the description of the systems in the summary/finding 
paper for the shared task. You can put it as a plaintext file into the 
compressed zip or just write it in the email as you send the submissions.


== DSL schedule ==

Training set release: 
Test set release: 
System submissions due:  (23:59 EST)
Results announced: 
Short papers deadline: 
Feedback:
Camera-ready versions: 

== LT4VarDial and DSL Task Organizers ==

Preslav Nakov, Qatar Computing Research Institute, Qatar
Marcos Zampieri, Saarland University, Germany
Petya Osenova, Bulgarian Academy of Sciences, Bulgaria
Cristina Vertan, University of Hamburg, Germany
Nikola Ljubešić, University of Zagreb, Croatian
Jörg Tiedemann, Uppsala University, Sweden
Liling Tan, Saarland University, Germany

