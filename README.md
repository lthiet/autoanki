# AutoAnki

This project aims to automate the process of creating cloze notes using a combination of existing research and new findings in the field of
Natural Language Processing. It will at first aims to work alongside Anki as an addon.

# Pipeline

In this section we shall discuss about the different modules that makes up the process. To put it shortly the pipeline is designed as such:

- Parsing from a Source
- Preprocessing
- Generate meta-data
- Learn key information from the text and generate clozes
- Postprocessing 
- Export to Anki

## Parsing from a Source

The scope of this project limits itself to text based content. For example, we will not attempt to automatically generate clozes for :

- Schematics
- Mathemathical Equations
- Anatomy
- etc.

At first, we will get content from verified Wikipedia articles.


