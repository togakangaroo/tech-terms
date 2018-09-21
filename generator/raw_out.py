import re
from collections import defaultdict
from typing import DefaultDict
from typing import List

import requests

TERM_URL = 'https://raw.githubusercontent.com/togakangaroo/tech-terms/master/terms.org'


def convert_to_dict_list(items: List[dict]) -> DefaultDict[str, list]:
    terms: DefaultDict[str, list] = defaultdict(list)

    for item in items:
        terms[item['term']].append(item['definition'])

    return terms


def parse_ank_raw_from_source() -> DefaultDict[str, list]:
    r = requests.get(TERM_URL)
    content = r.content

    # this regex matches 
    two_col_org_row = re.compile('^\\s*\\|\\s*(?P<term>.*?)\\s*\\|\\s*(?P<definition>.*?)\\s*\\|\\s*$')
    lines = content.splitlines()
    extracted_cells = (two_col_org_row.match(l.decode("utf-8")).groupdict() for l in lines)

    return convert_to_dict_list(list(extracted_cells))


if __name__ == '__main__':
    parse_ank_raw_from_source()
