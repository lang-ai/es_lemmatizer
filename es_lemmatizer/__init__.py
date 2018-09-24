from .data_loader import load_lookup_tables

lookup_tables = load_lookup_tables()

def update_lemma(token):
  pos = token.pos_
  form = token.lower_
  if form in lookup_tables[pos]:
    token.lemma_ = lookup_tables[pos][form]
  else:
    token.lemma_ = form
  return token

def lemmatize(doc):
  for tk in doc:
    update_lemma(tk)
  return doc