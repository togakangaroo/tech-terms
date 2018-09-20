import re 
import genanki
import os

file_name = 'tech_terms.apkg'

term_model = genanki.Model(
  505739646,
  'Tech Term Card Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])
terms_deck = genanki.Deck(1824707089, 'Tech Terms')

two_col_org_row = re.compile('^\\s*\\|\\s*(.*?)\\s*\\|\\s*(.*?)\\s*\\|\\s*$')
with open(f'../terms.org', 'r') as file:
    lines = file.read().splitlines()
    extracted_cells = (two_col_org_row.match(l).groups() for l in lines)
    term_definitions = (g for g in extracted_cells if len(g) == 2)

    notes = (genanki.Note(model=term_model, fields=[term, definition]) for (term, definition) in term_definitions)
    for note in notes:
        terms_deck.add_note(note)

genanki.Package(terms_deck).write_to_file(file_name)

print(f'Wrote {os.path.getsize(file_name)} bytes to {file_name}')
