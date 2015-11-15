DSL Task Repository
====

This is the official repository for the Disciminating between Similar Language (DSL) Shared Task 2015. Discriminating between similar languages and language varieties is one of the bottlenecks of language identification systems.

The results of the DSL-2015 Shared Task can be found on https://goo.gl/dCaxAV 

This repo contains the following:
 - DSL Corpus Collection (DSLCC) version 2.0 (training, dev, test and gold data included)
 - DSL Shared Task submissions from participating teams
 - The script to blind Named Entities (NEs) for the Test Set B in DSL-2015 (`blindNE.py`)
 - The evaluation script to evaluate your outputs (`evaluate.py`)
 - The evaluation script to evaluate all submitted systems (`evaluate_submissions.py`)

To Evalute Your Output
====

Here's an example to evaluate your system output:

```
$ git clone https://github.com/Simdiva/DSL-Task.git
$ cd DSL-Task
$ python3 evaluate.py submissions/mms/mms-tfidf-close-run1.txt data/DSLCC-v2.0/gold/test-gold.txt
```

To blind Named Entities in the training data
====
```
$ python3 blindNE.py data/DSLCC-v2.0/train-dev/train.txt
$ python3 blindNE.py data/DSLCC-v2.0/train-dev/train.txt > train-noNE.txt
```


Previous Workshops
====
 
 - [VarDial 2014](http://corporavm.uni-koeln.de/vardial/sharedtask.html) - First DSL Shared Task was held @ COLING 2014 (https://bitbucket.org/alvations/dslsharedtask2014)
 - [LT4VarDial 2015](http://ttg.uni-saarland.de/lt4vardial2015/index.html) - 2nd Edition DSL Shared Task is going to be held @ RANLP 2015 (https://github.com/Simdiva/DSL-Task)
