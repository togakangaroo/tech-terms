# Tech Terms

A repository of technical terms and definitions. Eventually to be converted to flashcards or...whatever.

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

## Plan

The idea is that this list is optimized for rote memorization - so each definition is short and presentable in flash-card format. The theory is that by memorizing this terminology, a beginner will get immediately situated within the terminology of the world of develoment.

- [x] Put together big, unsorted list of terms to define (aim for a few hundred terms)
- [x] Denormalize and flatten list
- [x] Define terms
- [x] Create transformer to transform into [Anki](http://ankiweb.net/)
- [ ] Create and administer a poll to figure out the most important terms
- [ ] Create several sets of flashcards of increasing granularity

## Contribute

Terms are written in org mode. For now just give a regular pull request. I'll take care of merging for now.

### Python Script To Build Anki apkg file

You can generate an apkg file from terms.org by running `parse_terms.py` from the `generator/` directory. For this you will need a version of Python 3 and [Pipenv](https://pipenv.readthedocs.io/en/latest/). Nothing will be installed globally.

    > cd generator
    generator> pipenv install
    generator> pipenv run python ./parse_terms.py
    
This will generate a `tech_terms.apkg` file in that directory. This file can now be opened with Anki.

### Jupyter Notebook

There is the `generator/playground.ipynb` for playing around with the script. To run it you must first [set up the pipenv environment as a Jupyter kernel target](https://stackoverflow.com/questions/47295871/is-there-a-way-to-use-pipenv-with-jupyter-notebook).

To run it

    > cd generator
    generator> pipenv install --dev
    generator> pipenv run python -m ipykernel install --user --name=tech-terms-generator
    
You may then run `jupyter notebook` as normal an select this kernel

## Future Work

Look at [Glossary Tech](https://glossarytech.com/terms/software_architecture/page2), maybe scrape it

