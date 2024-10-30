import nltk

grammar_1 = nltk.CFG.fromstring("""
  S -> NP VP
  NP -> Det N
  VP -> V NP
  Det -> 'the' | 'a'
  N -> 'cat' | 'dog'
  V -> 'chased' | 'saw'
""")

parser = nltk.ChartParser(grammar_1)
sentence = ['the', 'cat', 'chased', 'a', 'dog']

for tree in parser.parse(sentence):
    tree.pretty_print()

for tree in parser.parse(sentence):
    print(tree)


grammar_2 = nltk.CFG.fromstring("""
  S -> NP VP
  NP -> Det Adj N | Det N | 'I'
  VP -> V NP | V Adv NP
  Det -> 'the' | 'a'
  Adj -> 'big' | 'small' | 'furry'
  N -> 'dog' | 'cat' | 'man' | 'woman'
  V -> 'chased' | 'saw' | 'found'
  Adv -> 'quickly' | 'slowly'
""")

# Parser tanımı
parser = nltk.ChartParser(grammar_2)

# Örnek bir cümlesentence 

['the', 'big', 'dog', 'quickly', 'chased', 'a', 'small', 'cat']


try:
  # Parse işlemi ve sonuçların yazdırılması
  for tree in parser.parse(sentence):
      tree.pretty_print()
  for tree in parser.parse(sentence):
    print(tree)

except Exception as e:
   print(e)
