from collections import defaultdict


dictionary_names = [
  "MM.adj",
  "MM.adv",
  "MM.int",
  "MM.nom",
  "MM.tanc",
  "MM.vaux",
  "MM.verb",
]

def get_file(n):
  with open('../data/' + n) as f:
    return f.readlines()

def add_entry(entries, form, lemma):
  if form not in entries:
    entries[form] = lemma

def parse_entry(entry, lookup_tables):
  [form, lemma, tag] = entry.strip().split(" ")
  if tag.startswith('D'): # determiner
    add_entry(lookup_tables["DET"], form, lemma)
  if tag.startswith('A'): # adjective
    add_entry(lookup_tables["ADJ"], form, lemma)
  if tag.startswith('N'): # noun
    add_entry(lookup_tables["NOUN"], form, lemma)
  if tag.startswith('V'): # verb
    add_entry(lookup_tables["VERB"], form, lemma)
  if tag.startswith('R'): # adverb
    add_entry(lookup_tables["ADV"], form, lemma)
  if tag.startswith('S'): # adposition
    add_entry(lookup_tables["ADP"], form, lemma)
  if tag.startswith('C'): # conjuntion
    add_entry(lookup_tables["CONJ"], form, lemma)
  if tag.startswith('P'): # pronoun
    add_entry(lookup_tables["PRON"], form, lemma)
  if tag.startswith('I'): # interjection
    add_entry(lookup_tables["INTJ"], form, lemma)


def process_file(n, lookup_tables):
  entries = get_file(n)
  print("{} entries...".format(len(entries)))
  for entry in entries:
    parse_entry(entry, lookup_tables)

def load_lookup_tables():
  lookup_tables = defaultdict(dict)
  for name in dictionary_names:
    process_file(name)
  return lookup_tables
