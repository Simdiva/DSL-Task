
import io

from evaluate import breakdown_evaluation, main

open_submissions = {'nrc': ['submissions/nrc/nrc-catego-open-run1.txt',
                            'submissions/nrc/nrc-catego-open-run2.txt'],

                    'oseval':['submissions/oseval/langmodel-oseval-open-run1.txt'],
                    
                    'nlel':['submissions/nlel/NLEL_UPV_Autoritas-probfwk-open-run1.txt'],
                    }


open_none_submissions = {'nrc':['submissions/nrc/nrc-catego-open-none-run1.txt',  
                                'submissions/nrc/nrc-catego-open-none-run2.txt'],
                         'oseval':['submissions/oseval/langmodel-oseval-open-none-run1.txt'],
                         
                         'nlel':['submissions/nlel/NLEL_UPV_Autoritas-probfwk-open-none-run1.txt'],
                         }


close_submissions = {'inria':['submissions/inria/inria-triwords-closed-run1.txt',  
                            'submissions/inria/inria-triwords-closed-run2.txt',  
                            'submissions/inria/inria-triwords-closed-run3.txt'],
                     
                     'bobicev':['submissions/bobicev/Bobicev-PPM5-close-run1.txt'],
                     
                     
                    'mac':['submissions/mac/mac-lad-close-run1.txt',  
                           'submissions/mac/mac-lad-close-run2.txt',  
                           'submissions/mac/mac-lad-close-run3.txt'],
                     
                                         
                    'nrc':['submissions/nrc/nrc-catego-close-run1.txt',  
                    'submissions/nrc/nrc-catego-close-run2.txt'],
                     
                     'suki':['submissions/suki/suki-suki-close-run1.txt',
                                'submissions/suki/suki-suki-close-run2.txt',
                                'submissions/suki/suki-suki-close-run3.txt'],
                     
                     'prhlt':['submissions/prhlt/PRHLT_UPV_AUTORITAS-skipGr-close-run1.txt',
                              'submissions/prhlt/PRHLT_UPV_AUTORITAS-skipGr-close-run2.txt',
                              'submissions/prhlt/PRHLT_UPV_AUTORITAS-skipGr-close-run3.txt'],
                     
                     'mms':['submissions/mms/mms-tfidf-close-run1.txt',
                            'submissions/mms/mms-tfidf-close-run2.txt',
                            'submissions/mms/mms-tfidf-close-run3.txt'],
                     
                     'brunibp':['submissions/brunibp/brunibp-brunibp-close-run1.txt',
                            'submissions/brunibp/brunibp-brunibp-close-run2.txt',
                            'submissions/brunibp/brunibp-brunibp-close-run3.txt'],
                     
                     'nlel':['submissions/nlel/NLEL_UPV_Autoritas-probfwk-close-run2.txt']

                    }


close_none_submissions = {'bobicev':['submissions/bobicev/Bobicev-PPM5-close-none-run1.txt'],
                          
                          'mac':['submissions/mac/mac-lad-close-none-run1.txt',  
                                'submissions/mac/mac-lad-close-none-run2.txt',  
                                'submissions/mac/mac-lad-close-none-run3.txt'],
                          
                          'nrc':['submissions/nrc/nrc-catego-close-none-run1.txt',  
                                 'submissions/nrc/nrc-catego-close-none-run2.txt'],  
                          
                        'suki':['submissions/suki/suki-suki-close-none-run1.txt',  
                                'submissions/suki/suki-suki-close-none-run2.txt',  
                                'submissions/suki/suki-suki-close-none-run3.txt'],
                          
                          'prhlt':['submissions/prhlt/PRHLT_UPV_AUTORITAS-skipGr-close-none-run1.txt',  
                                    'submissions/prhlt/PRHLT_UPV_AUTORITAS-skipGr-close-none-run2.txt',
                                    'submissions/prhlt/PRHLT_UPV_AUTORITAS-skipGr-close-none-run3.txt'],  
                          
                          'mms':['submissions/mms/mms-tfidf-close-none-run1.txt',  
                                    'submissions/mms/mms-tfidf-close-none-run2.txt',  
                                    'submissions/mms/mms-tfidf-close-none-run3.txt'],
                          
                          'nlel':['submissions/nlel/NLEL_UPV_Autoritas-probfwk-close-none-run2.txt']
                          
                          }

gold_file = 'data/DSLCC-v2.0/gold/test-gold.txt'
gold_none_file = 'data/DSLCC-v2.0/gold/test-none-gold.txt'

print "Close Submission\n========="
for team in close_submissions:
    for s in close_submissions[team]:
        results = [i.strip().split('\t')[-1] for i in io.open(s, 'r')]
        goldtags = [i.strip().split('\t')[-1] for i in io.open(gold_file, 'r')]
        results = breakdown_evaluation(results, goldtags, version=2.0, overall_only=True)
        print s + '\t' + str(results)
print

print "Close Blinded NE Submission\n========="
for team in close_none_submissions:
    for s in close_none_submissions[team]:
        results = [i.strip().split('\t')[-1] for i in io.open(s, 'r')]
        goldtags = [i.strip().split('\t')[-1] for i in io.open(gold_none_file, 'r')]
        results = breakdown_evaluation(results, goldtags, version=2.0, overall_only=True)
        print s + '\t' + str(results)
print 

print "Open Submission\n========="
for team in open_submissions:
    for s in open_submissions[team]:
        results = [i.strip().split('\t')[-1] for i in io.open(s, 'r')]
        goldtags = [i.strip().split('\t')[-1] for i in io.open(gold_file, 'r')]
        results = breakdown_evaluation(results, goldtags, version=2.0, overall_only=True)
        print s + '\t' + str(results)
print 

print "Open Blinded NE Submission\n========="
for team in open_none_submissions:
    for s in open_none_submissions[team]:
        results = [i.strip().split('\t')[-1] for i in io.open(s, 'r')]
        goldtags = [i.strip().split('\t')[-1] for i in io.open(gold_none_file, 'r')]
        results = breakdown_evaluation(results, goldtags, version=2.0, overall_only=True)
        print s + '\t' + str(results)
print

print "Close Submission by group\n========="
for team in close_submissions:
    for s in close_submissions[team]:
        results = [i.strip().split('\t')[-1] for i in io.open(s, 'r')]
        goldtags = [i.strip().split('\t')[-1] for i in io.open(gold_file, 'r')]
        results = breakdown_evaluation(results, goldtags, version=2.0, human_readable=False)
        for line in results:
            print s + '\t' + str(line)
print

print "Close Blinded NE by group\n========="
for team in close_none_submissions:
    for s in close_none_submissions[team]:
        results = [i.strip().split('\t')[-1] for i in io.open(s, 'r')]
        goldtags = [i.strip().split('\t')[-1] for i in io.open(gold_none_file, 'r')]
        results = breakdown_evaluation(results, goldtags, version=2.0, human_readable=False)
        for line in results:
            print s + '\t' + str(line)
print
