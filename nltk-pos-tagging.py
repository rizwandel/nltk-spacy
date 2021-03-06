import nltk

str = "Pythons live near the equator, in Asia and Africa, where it is hot and wet and their huge bodies can stay warm.  They make their homes in caves or in trees and have become used to living in cities and towns since people have been moving in on their territory."

tokens = nltk.word_tokenize(str)
nltk.pos_tag(tokens)


# Out[4]:
# [('Pythons', 'NNS'),
#  ('live', 'VBP'),
#  ('near', 'IN'),
#  ('the', 'DT'),
#  ('equator', 'NN'),
#  (',', ','),
#  ('in', 'IN'),
#  ('Asia', 'NNP'),
#  ('and', 'CC'),
#  ('Africa', 'NNP'),
#  (',', ','),
#  ('where', 'WRB'),
#  ('it', 'PRP'),
#  ('is', 'VBZ'),
#  ('hot', 'JJ'),
#  ('and', 'CC'),
#  ('wet', 'JJ'),
#  ('and', 'CC'),
#  ('their', 'PRP$'),
#  ('huge', 'JJ'),
#  ('bodies', 'NNS'),
#  ('can', 'MD'),
#  ('stay', 'VB'),
#  ('warm', 'JJ'),
#  ('.', '.'),
#  ('They', 'PRP'),
#  ('make', 'VBP'),
#  ('their', 'PRP$'),
#  ('homes', 'NNS'),
#  ('in', 'IN'),
#  ('caves', 'NNS'),
#  ('or', 'CC'),
#  ('in', 'IN'),
#  ('trees', 'NNS'),
#  ('and', 'CC'),
#  ('have', 'VBP'),
#  ('become', 'VBN'),
#  ('used', 'VBN'),
#  ('to', 'TO'),
#  ('living', 'VBG'),
#  ('in', 'IN'),
#  ('cities', 'NNS'),
#  ('and', 'CC'),
#  ('towns', 'NNS'),
#  ('since', 'IN'),
#  ('people', 'NNS'),
#  ('have', 'VBP'),
#  ('been', 'VBN'),
#  ('moving', 'VBG'),
#  ('in', 'IN'),
#  ('on', 'IN'),
#  ('their', 'PRP$'),
#  ('territory', 'NN'),
#  ('.', '.')]
