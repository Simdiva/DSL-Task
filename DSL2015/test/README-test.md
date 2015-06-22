DSL Shared Task 2015
====

**Website**: http://ttg.uni-saarland.de/lt4vardial2015/dsl.html

**Contact**:  dsl.sharedtask@gmail.com or https://groups.google.com/forum/?hl=en#!forum/dsl-shared-task

**Test data Release**: 22 Jun 2015

These DSL Test Sets are part of the DSLCC v2.0, it comprises news data from various corpora to emulate the diverse news content across different languages and varieties.

Format Description
====

The test data contains 3 files (including this README).
 1. `test.txt` (Test Set A)
 2. `test-none.txt` (Test Set B)
 3. `README-test.md` 

**Note**:

 - The `test.txt` contains 14,000 sentences for 13 languages/varieties and others (bg, bs, cz, es-AR, es-ES, hr, id, mk, my, pt-BR, pt-PT, sk, sr, xx)

 - The `test-none.txt` contains 14,000 sentences with documents that have blinded Named Entities; they are different documents from test.txt.

 - All sentences are encoding in UTF-8.

 - The test data only contain sentences without their language/variety labels.

IMPORTANT
====

IMPORTANT!!! Please note the following to facilitate the evaluation:

**(i)** provide the system output as how the training and development data was 
formatted, without changing the order of the test sentences:

	sentence<tab>language

**(ii)** Please name your submission files with the following convention,
all in lowercase:

	<team_name>-<system_name>-<open_or_close>-<run#>.txt

For example, if your team_name is "USAAR" , system_name is "DisLang" and it's an
open submission and it's the 1st run that you want to submit, the submission
file should be as such:

	usaar-dislang-open-run1.txt

**(iii)** For Test Set B (train-none.txt) evaluation, please name your submission 
files with the following convention, all in lowercase:

	<team_name>-<system_name>-<open_or_close>-none-<run#>.txt

For example, if your team_name is "USAAR" , system_name is "DisLang" and it's an
open submission and it's the 1st run that you want to submit, the submission
file should be as such:

	usaar-dislang-open-none-run1.txt

**(iv)** Along with the systems runs, **please submit a short description of your system**.
This is to facilitate the description of the systems in the summary/finding 
paper for the shared task. The short description should include:

 - General description of system (at least 3-5 sentences)
 - System's machine learning technique (e.g. classifier, clustering, rule-based, etc.)
 - Choice of alogrithm (e.g. Naive Bayes, SVM, KNN, etc.
 - Primary feature set (give a list or a short 2-3 sentence description, if necessary longer is okay)
 - Authors of your task description paper (It'll be good if the order is the same as your system description paper)
 - Any other special/interesting information about the system.
 - (If you submitted to the open submission), please also specify the resources used to train your system
 - (If you're using off the shelf tools), please give a url reference to the paper or the software.

**(v)** Please also compress ALL run submissions into a single file and send it to
dsl.sharedtask@gmail.com before the submission deadline (23 Apr), please name
compressed file in the following format: (team_name-system-name.zip)
For example:

	usaar-dislang.zip

**(vi)** Do specify in the email title when sending the compression submission file,
e.g. (team_name DSL2015 submission)

	Title: USAAR DSL2015 submission

**(vii)** Each team is ONLY allowed to submit 3 runs for closed and/or 3 runs for 
open task for both Test Set A and Test Set B (so that 12 files in total for 
teams participating in both open and close submission for both test sets).

DSL schedule
====

**Training set release**: May 20th, 2015

**Test set release**: June 22nd, 2015

**System submissions due**: June 24th, 2016 (23:59 EST) !!!

**Results announced**: June 26th, 2016

**Short papers deadline**: TBA (tentatively,  July 20th, 2015)

**Feedback**: TBA (tentatively, August 1st, 2015)

**Camera-ready versions**: TBA (tentatively, August 9th, 2015)

Organizers
====

Marcos Zampieri, Saarland University, Germany

Liling Tan, Saarland University, Germany

Nikola Ljubešić, University of Zagreb, Croatian

Jörg Tiedemann, Uppsala University, Sweden

Preslav Nakov, Qatar Computing Research Institute, Qatar

