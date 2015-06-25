# -*- coding: utf-8 -*-

import io
import sys
from collections import Counter

red = '\033[01;31m'
native = '\033[m'

def err_msg(txt):
    return red + txt + native

def language_groups(version=2.0):
    varieties = {'Portugese': ['pt-BR', 'pt-PT'],
                 'Spanish': ['es-ES', 'es-AR'],
                 'English':['en-UK', 'en-US']}
    
    similar_languages = {'Malay, Indo':['my', 'id'],
                         'Czech, Slovak':['cz', 'sk'],
                         'Bosnian, Croatian, Serbian':['bs', 'hr', 'sr'],
                         'Bulgarian, Macedonian':['bg','mk'],
                         'Others':['xx']}
    
    if version == 1:
        similar_languages.pop('Bulgarian, Macedonian')
        similar_languages.pop('Others')
    elif version == 2:
        varieties.pop('English')
    
    groups = varieties; groups.update(similar_languages)
    return groups
    

def breakdown_evaluation(results, goldtags, version=2.0, human_readable=True,
                         overall_only=False):    
    positives = Counter([y for x,y in zip(results,goldtags) if x.lower().replace('_', '-')==y.lower()])
    golds = Counter(goldtags)    
    
    groups = language_groups(version)

    sum_positives = sum(positives.values())
    sum_gold = sum(golds.values())
    accuracy = sum_positives / float(sum_gold)
    
    if overall_only:
        output_line = map(str, ['Overall', 'Accuracy', 
                                    sum_positives, sum_gold, accuracy])
        return accuracy
    
    bygroup_output = [] 
    
    if human_readable:
        print "=== Results === "
        for g in groups:
            print
            print g
            for l in groups[g]:
                p = positives[l]
                gl = golds[l]
                print "{}: {} / {} = {}".format(l, p, gl, p/float(gl))
        print 
        print "Overall:", "{} / {} = {}".format(sum_positives, sum_gold, accuracy)
        print
    else:
        for g in groups:
            for l in groups[g]:
                p, gl = positives[l], golds[l]
                if not overall_only:
                    result_line = '\t'.join(map(str,[g, l, p, gl, p/float(gl)]))
                    bygroup_output.append(result_line)
        # print '\t'.join(output_line)
        return bygroup_output
        

def main(system_output, goldfile):
    results = [i.strip().split('\t')[-1] for i in io.open(system_output, 'r')]
    goldtags = [i.strip().split('\t')[-1] for i in io.open(goldfile, 'r')]
    breakdown_evaluation(results, goldtags, version=2.0, human_readable=True)
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage_msg = err_msg('Usage: python3 %s system_output goldfile\n'
                            % sys.argv[0])
        example_msg = err_msg('Example: python3 %s ~/usaar-dislang-run1-test.txt '
                              '~/DSLCC-v2.0/gold/test-gold.txt \n' % sys.argv[0])
        sys.stderr.write(usage_msg)
        sys.stderr.write(example_msg)
        sys.exit(1)

    main(*sys.argv[1:])