import re 
import csv

def llen(gen):
    return sum(1 for _ in gen)

two_col_org_row = re.compile('^\\s*\\|\\s*(.*?)\\s*\\|\\s*(.*?)\\s*\\|\\s*$')
with open(f'../terms.org', 'r') as file:
    lines = file.read().splitlines()
    extracted_cells = (two_col_org_row.match(l).groups() for l in lines)
    term_definitions = (g for g in extracted_cells if len(g) == 2)

    with open(f'./test.csv', 'w') as csv_file:
        wr = csv.writer(csv_file)
        for (term, definition) in term_definitions:
            wr.writerow([term, definition])
