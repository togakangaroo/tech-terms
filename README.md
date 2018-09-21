<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Technical Terms Flashcard Deck</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

# Tech Terms

[See the current list of tech terms](https://github.com/togakangaroo/tech-terms/blob/master/terms.org)

[See the current shared Anki flashcard deck](https://ankiweb.net/shared/info/40916824)

## Background

Throughout most of my life I've been very negative on the role of memorization in education, considering it a bad way to learn a topic and frankly, beneath me. Still, when I found about [Anki](http://ankiweb.net/) in late 2017 I - after browsing some of the shared decks - decided to try it to do something I've always wanted to do: memorize all the Chinese provinces and their capitals. 

Shocked at how effective this was, I continued with geography; memorizing all the countries, capitals, flags, water bodies, and states of several more countries. I also shifted to history, memorizing important dates and events. As I did this, I was surprised to realize an additional benefit - by having geography and the broad outline of history at my beck and call, powering through dense history books became far easier. I no longer had to struggle to establish context or cross reference maps, everything just made sense. I began reconsidering the role of memorization in the learning process. 

I am a software developer and [a manager](https://www.surgeforward.com/our-team/). As part of my job, I act as support to sales and recruiters who frequently refer to me to orient them with one piece of tech or another. More importantly, I do a great deal of mentoring, spending a lot of time helping novices with organizations like [Operation Code](http://operationcode.org) and [Operation Spark](https://operationspark.org/) (no relation to each other). I have seen over and over again people get completely overwhelmed and disoriented with the amount of information, areas of competency, and just flat out terminology out there. It is my contention that the same memorization techniques can help get people grounded in the field.

So this is a project to create a list of terms that might be helpful for familiarizing someone with the industry and in general how developers speak. Each term is accompanied by a short, [flash-card-able](https://ankiweb.net/shared/info/40916824) definition. The goal is not to be comprehensive or even very precise, just to give users enough of a head start to make the rest of their journey easier.

## Plan

- [x] Put together big, unsorted list of terms to define (aim for a few hundred terms)
- [x] Denormalize and flatten list
- [x] Define terms
- [x] Create transformer to transform into [Anki](http://ankiweb.net/)
- [ ] Create and administer a poll to figure out the most important terms
- [ ] Create several sets of flashcards of increasing granularity

## Contribute

Terms are written in org mode in the `terms.org` file. To add or edit terms, open the file in the Github or any text editor (one with [org-mode support](https://en.wikipedia.org/wiki/Org-mode#Integration) is encouraged but not necessary for this), make edits, and give me a pull request. Remember, the goal is not to be comprehensive, so much as memorizeable. Therefore, please limit term and defintion lengths to the somewhat arbitrarily (and because it worked for me) current width of the table:

* 52 character maximum for terms
* 220 character maximum for definitions

### Python Script To Build Anki apkg file

While there is no problem with just using the table directly to study, I very much prefer using the free Anki program. An Anki deck is therefore provided and can be built from the `terms.org` file.

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

