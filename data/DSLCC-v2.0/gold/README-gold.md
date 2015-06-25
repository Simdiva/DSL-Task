DSL Shared Task 2015
====

**Website**: http://ttg.uni-saarland.de/lt4vardial2015/dsl.html

**Contact**:  dsl.sharedtask@gmail.com or https://groups.google.com/forum/?hl=en#!forum/dsl-shared-task

**Test data Release**: 22 Jun 2015

These DSL Gold Sets are part of the DSLCC v2.0, it comprises news data from various corpora to emulate the diverse news content across different languages and varieties.

Format Description
====

The gold data contains 4 files (including this README).
 1. `test-gold.txt` (Test Set A with gold labels)
 2. `test-none-gold.txt` (Test Set B with gold labels)
 3. `test-ne.txt` (Test Set B with NEs but w/o labels)
 4. `README-gold.md` 

**Note**:

 - The `test-gold.txt` contains 14,000 sentences for 13 languages/varieties and others (bg, bs, cz, es-AR, es-ES, hr, id, mk, my, pt-BR, pt-PT, sk, sr, xx)

 - The `test-none-gold.txt` contains 14,000 sentences with documents that have blinded Named Entities; they are different documents from test.txt.

 - The `test-ne.txt` contains 14,000 sentences with documents, they are the unblinded version of `test-none.txt` from the test set.
 
 - All sentences are encoding in UTF-8.

 - The test data only contain sentences without their language/variety labels.


Organizers
====

Marcos Zampieri, Saarland University, Germany

Liling Tan, Saarland University, Germany

Nikola Ljubešić, University of Zagreb, Croatian

Jörg Tiedemann, Uppsala University, Sweden

Preslav Nakov, Qatar Computing Research Institute, Qatar

