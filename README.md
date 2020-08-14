# AutoAnki

This project aims to automate the process of creating cloze notes using a combination of existing research and new findings in the field of
Natural Language Processing. It will at first aims to work alongside Anki as an addon.

The target language currently is English.

# Pipeline

In this section we shall discuss about the different modules that makes up the process. To put it shortly the pipeline is designed as such:

- Parsing from a Source & Preprocessing
- Learn key information from the text and generate clozes
- Postprocessing 
- Export to Anki

## Parsing from a Source & Preprocessing 

The scope of this project limits itself to text based content. For example, we will not attempt to automatically generate clozes for :

- Schematics
- Mathemathical Equations
- Anatomy
- etc.

At first, we will get content from verified Wikipedia articles. The parsing should be relatively straightforward, we simply want to extract the text,
clean it if possible: remove hyperlinks, superscripts, etc. anything that brings no value to learning key information from a text
or that is too hard or exotic for models to process.

Some preprocessing can also be done. A model could actually be used here as well. The idea is to remove ambiguity, like replacing
pronouns with the actual nouns they represent, or shortening long sentences into a collection of shorter ones.

