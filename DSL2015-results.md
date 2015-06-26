Results of DSL Shared Task 2015
====

We are happy to report that 23 teams registered for the shared task and 10 teams submitted systems to the [DSL Shared Task 2015](http://ttg.uni-saarland.de/lt4vardial2015/dsl.html)


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

The participating systems are ranked according to their best performing runs for the various submission types.

Team | Close (Normal) | Close (No NEs) | Open (Normal)  | Open (No NEs)
-----|:----------------:|:----------------:|:----------------:|:---------------:
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

Overall Accuracy
====

The best accuracy achieved by the systems for the various submission types.

Team | Close (Normal) | Close (No NEs) | Open (Normal)  | Open (No NEs)
-----|:----------------:|:----------------:|:----------------:|:---------------:
BOBICEV | 94.14 | 92.22 | - | -
BRUNIBP | 93.66 | - | - | -
INRIA | 83.91 | - | - | -
MAC | **95.54** | **94.01** | - | -
MMS | 95.24 | 92.78 | - | -
NLEL | 64.04 | 62.78 | 91.84 | 89.56
NRC | 95.24 | 93.01 | **95.65** | **93.41**
OSEVAL | - | - | 76.17 | 75.3
PRHLT | 92.74 | 90.8 | - | -
SUKI | 94.67 | 93.02 | - | -

Closed Submission (Normal)
====

Team | Overall Accuracy | Submission File |
-----|:----------------|:---------------| 
MAC | 0.9553571429 | submissions/mac/mac-lad-close-run3.txt | 
MAC | 0.9544285714 | submissions/mac/mac-lad-close-run2.txt | 
MAC | 0.9531428571 | submissions/mac/mac-lad-close-run1.txt | 
MMS | 0.9524285714 | submissions/mms/mms-tfidf-close-run2.txt | 
NRC | 0.9524285714 | submissions/nrc/nrc-catego-close-run2.txt | 
NRC | 0.9482142857 | submissions/nrc/nrc-catego-close-run1.txt | 
SUKI | 0.9467142857 | submissions/suki/suki-suki-close-run3.txt | 
SUKI | 0.9435714286 | submissions/suki/suki-suki-close-run2.txt | 
BOBICEV | 0.9413571429 | submissions/bobicev/Bobicev-PPM5-close-run1.txt | 
MMS | 0.9409285714 | submissions/mms/mms-tfidf-close-run1.txt | 
MMS | 0.9407142857 | submissions/mms/mms-tfidf-close-run3.txt | 
SUKI | 0.9372857143 | submissions/suki/suki-suki-close-run1.txt | 
BRUNIBP | 0.9366428571 | submissions/brunibp/brunibp-brunibp-close-run2.txt | 
BRUNIBP | 0.9348571429 | submissions/brunibp/brunibp-brunibp-close-run3.txt | 
BRUNIBP | 0.9331428571 | submissions/brunibp/brunibp-brunibp-close-run1.txt | 
PRHLT** | 0.9273571429 | submissions/prhlt/PRHLT_UPV_AUTORITAS-skipGr-close-run3.txt | 
PRHLT | 0.9267142857 | submissions/prhlt/PRHLT_UPV_AUTORITAS-skipGr-close-run2.txt | 
PRHLT | 0.9211428571 | submissions/prhlt/PRHLT_UPV_AUTORITAS-skipGr-close-run1.txt | 
INRIA | 0.8390714286 | submissions/inria/inria-triwords-closed-run1.txt | 
INRIA | 0.8390714286 | submissions/inria/inria-triwords-closed-run2.txt | 
INRIA | 0.6439285714 | submissions/inria/inria-triwords-closed-run3.txt | 
NLEL | 0.6403571429 | submissions/nlel/NLEL_UPV_Autoritas-probfwk-close-run2.txt | 

Close Submission (Blinded NE)
====

Team | Overall Accuracy | Submission File |
-----|:----------------|:---------------| 
MAC | 0.9400714286 | submissions/mac/mac-lad-close-none-run3.txt | 
MAC | 0.9387857143 | submissions/mac/mac-lad-close-none-run1.txt | 
MAC | 0.9372857143 | submissions/mac/mac-lad-close-none-run2.txt | 
SUKI | 0.9302142857 | submissions/suki/suki-suki-close-none-run3.txt | 
NRC | 0.9300714286 | submissions/nrc/nrc-catego-close-none-run1.txt | 
MMS | 0.9277857143 | submissions/mms/mms-tfidf-close-none-run1.txt | 
MMS | 0.9277857143 | submissions/mms/mms-tfidf-close-none-run2.txt | 
SUKI | 0.9272142857 | submissions/suki/suki-suki-close-none-run2.txt | 
MMS | 0.9247142857 | submissions/mms/mms-tfidf-close-none-run3.txt | 
NRC | 0.923 | submissions/nrc/nrc-catego-close-none-run2.txt | 
BOBICEV | 0.9222142857 | submissions/bobicev/Bobicev-PPM5-close-none-run1.txt | 
PRHLT | 0.908 | submissions/prhlt/PRHLT_UPV_AUTORITAS-skipGr-close-none-run2.txt | 
PRHLT | 0.9047857143 | submissions/prhlt/PRHLT_UPV_AUTORITAS-skipGr-close-none-run1.txt | 
PRHLT** | 0.885 | submissions/prhlt/PRHLT_UPV_AUTORITAS-skipGr-close-none-run3.txt | 
NLEL | 0.6277857143 | submissions/nlel/NLEL_UPV_Autoritas-probfwk-close-none-run2.txt | 
SUKI | 0.07107142857 | submissions/suki/suki-suki-close-none-run1.txt | 

Open Submission (Normal)
====

Team | Overall Accuracy | Submission File |
-----|:----------------|:---------------| 
NRC | 0.9565 | submissions/nrc/nrc-catego-open-run2.txt
NRC | 0.9542857143 | submissions/nrc/nrc-catego-open-run1.txt
NLEL | 0.9183571429 | submissions/nlel/NLEL_UPV_Autoritas-probfwk-open-run1.txt
OSEVAL | 0.7617142857 | submissions/oseval/langmodel-oseval-open-run1.txt

Open Submission (Blinded NE)
====

Team | Overall Accuracy | Submission File |
-----|:----------------|:---------------| 
NRC | 0.9341428571 | submissions/nrc/nrc-catego-open-none-run1.txt
NRC | 0.9289285714 | submissions/nrc/nrc-catego-open-none-run2.txt
NLEL | 0.8956428571 | submissions/nlel/NLEL_UPV_Autoritas-probfwk-open-none-run1.txt
OSEVAL | 0.753 | submissions/oseval/langmodel-oseval-open-none-run1.txt
