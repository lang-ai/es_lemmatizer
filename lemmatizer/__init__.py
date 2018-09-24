from data_loader import load_lookup_tables

lookup_tables = load_lookup_tables()

def update_lemma(token):
  pos = token.pos_
  form = token.lower_
  if form in lookup_tables[pos]:
    token.lemma_ = lookup_tables[pos][form]
  return token

def lemmatize(doc):
  return list(map(update_lemma, doc))