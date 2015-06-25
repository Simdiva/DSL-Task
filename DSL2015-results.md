Results of DSL Shared Task 2015
====

We are happy to report that 23 teams registered for the shared task and 10 teams submitted systems.


Evaluation
=====

The evaluation is based on overall accuracy for every language/variety .

The best performing system(s) are decided by the overall accuracy across all languages/varieties for the various types of submission:
 - **Close submission** trained on only DSLCC v2.0 and tested on normal news text (`test.txt`, aka. Test Set A)
 - **Close submission** trained on only DSLCC v2.0 and tested on news text with **blinded Named Entities** (`test-none.txt`, aka. Test Set B)
 - **Open submission** trained on any resources and tested on normal news text (`test.txt`)
 - **Open submission** traned on any resources and tested on news text with **blinded NEs** (`test-none.txt`)
  
The overall accuracy is caluclated as such: 

      overall accuracy = sum(TP) / #sents

where:

     TP = True Positive for all languages/varieties 
     #sents = total number of documents in evaluation dataset 



Rankings
====

Team | Close (Normal) | Close (No NEs) | Open (Normal)  | Open (No NEs)
-----|----------------|----------------|----------------|---------------
BOICEV | 4 | 5 | - | -
BRUNIBP | 5 | - | - | -
INRIA | 7 | - | - | -
MAC | 1 | 1 | - | -
MMS | 2 | 4 | - | -
NLEL | 8 | 7 | 2 | 2
NRC | 2 | 3 | 1 | 1
OSEVAL | - | - | 3 | 3
PRHLT | 6 | 6 | - | -
SUKI | 3 | 2 | - | -

