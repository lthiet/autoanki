"""
The goal of this script to clean up the data before putting it
through a model that will generate clozes

The task list are :
- Remove unecessary sections
- Clean encoding
- Remove ambiguity
- Split big paragraph into list of sentences
- Break down long sentences
"""

import json
import os
from pathlib import Path
from os import listdir
from os.path import isfile, join


def preprocess_page(data):
    """
    Self explanatory
    """

    # Step 1: Remove unecessary sections
    # NOTE: for now, section with less than a certain number of characters gets removed.
    # this is rather arbitrary, there are probably better ways to deal with useless
    # sections such as citations, links, etc.
    to_be_removed = []
    for i in range(len(data['headers'])):
        if len(data['content'][i]) < 1000:
            to_be_removed.append(i)

    for i in sorted(to_be_removed, reverse=True):
        del data['content'][i]
        del data['headers'][i]

    # TODO: Remove unicode

    # TODO: Remove Ambiguity

    # TODO: Breakdown Long sentences

    return data


if __name__ == '__main__':
    p_in = str(Path(os.getcwd()).parent.parent) + '/data/pages/raw/'
    p_out = str(Path(os.getcwd()).parent.parent) + '/data/pages/preprocessed/'

    for p in listdir(p_in):
        with open(p_in + p, 'r') as f:
            data = json.load(f)
            data = preprocess_page(data)

        with open(p_out + 'preprocessed_' + p, 'w') as f:
            json.dump(data, f, indent=4)
