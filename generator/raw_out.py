import re
from typing import Dict, List, Pattern, Generator

import requests


class TechTerms:
    TERM_URL = 'https://raw.githubusercontent.com/togakangaroo/tech-terms/master/terms.org'

    def __init__(self):
        self.terms = self.parse_ank_raw_from_source()

    def _parse_ank_raw_from_source(self) -> Dict[str, list]:
        two_col_org_row: Pattern[str] = self.compile_regex_from_parts()

        content = self.grab_data_from_github()

        lines: List[str] = content.splitlines()

        return {x['term']: x['definition'] for x in self.filter_matches(lines, two_col_org_row)}

    def _grab_data_from_github(self) -> str:
        r = requests.get(self.TERM_URL)
        return r.content.decode('utf-8')

    def _compile_regex_from_parts(self) -> Pattern[str]:
        n_spaces_pipe_n_spaces = '\\s*\\|\\s*'
        non_greedy_group_of_chars = '.*?'
        regex_string = f'^{n_spaces_pipe_n_spaces}(?P<term>{non_greedy_group_of_chars})' \
                       f'{n_spaces_pipe_n_spaces}(?P<definition>{non_greedy_group_of_chars}){n_spaces_pipe_n_spaces}$'

        return re.compile(regex_string)

    def _filter_matches(self, lines: List[str], two_col_org_row: Pattern[str]) -> Generator[dict, None, None]:
        for line in lines:
            match = two_col_org_row.match(line).groupdict()
            if match.get('term') and match.get('definition'):
                yield match


if __name__ == '__main__':
    print(TechTerms().terms)
