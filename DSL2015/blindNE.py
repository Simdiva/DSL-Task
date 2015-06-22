import io
import re
import sys


red = '\033[01;31m'
native = '\033[m'

def err_msg(txt):
    return red + txt + native

def blind_ne(text):
	return re.sub(r'[A-Z]\S+\s*', ' #NE# ', text)

def blind_ne_without_first(text):
	# Keep the first word unchanged.
	first_word, _, the_rest = text.partition(' ')
	blinded_text = first_word + ' ' + blind_ne(text)	
	# Removes extra whitespaces.
	blinded_text = " ".join(blinded_text.split(' '))
	return blinded_text

def main(textfile):
	with io.open(textfile, 'r', encoding='utf8') as fin:
		for line in fin:
			doc = line.split('\t')[0].strip()
			print(blind_ne_without_first(doc))
	
if __name__ == '__main__':
	if len(sys.argv) is not 2:
		usage_msg = err_msg('Usage: python3 %s test-ne.txt\n'
				        % sys.argv[0])
		sys.stderr.write(usage_msg)
		sys.exit(1)
	main(*sys.argv[1:])

