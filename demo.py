from __future__ import print_function
from __future__ import division
import os
import re
from spacy.en import English, LOCAL_DATA_DIR

data_dir = os.environ.get('SPACY_DATA', LOCAL_DATA_DIR)
nlp = English(data_dir=data_dir)


def annonymizer(input_line):

	tokens = nlp(input_line)
	tags = [tok.tag_ for tok in tokens]
	for tok,tag in zip(tokens, tags):
		if tag == 'CD':
			input_line = re.sub(str(tok),'XXXX', input_line)

	return input_line


some_email = open('sample_email.txt','r').read().splitlines()
some_email = map(lambda line: unicode(line, errors='ignore'), some_email)
for sent in some_email:
	anon_sent = annonymizer(sent)
	print(anon_sent)
