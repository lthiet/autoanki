"""
This script will read a wikipedia page into a collection of text and meta data to be processed.
As an example, we will use Napoleon Bonaparte wiki page:
https://en.wikipedia.org/wiki/Napoleon
"""

import wikipediaapi
import json
import sys
import os
from pathlib import Path
wiki = wikipediaapi.Wikipedia('en')


def get_data(export, headers, section):
    """
    Will fill inplace the export data structure with nested headers
    and their respective text
    """
    for unit in section:

        # We use a temporary variable so as to not update it for all
        # iteration
        temp_header = headers + [unit.title]

        # Get the text
        text = unit.text

        # Ignore sections with empty texts
        # NOTE: this is probably dirty, could use classes instead?
        if len(text) != 0:
            export['headers'].append(temp_header)
            export['content'].append(unit.text)

        get_data(export, temp_header, unit.sections)


if __name__ == '__main__':
    # Read input
    target = sys.argv[1]
    page_py = wiki.page(target)

    # Check for page existence
    if not page_py.exists():
        print("ERROR: Page doesn't exist.")
        exit(1)

    # Create data
    export = {
        'headers': [],
        'content': []
    }

    # Fetch data
    get_data(export, [], page_py.sections)

    # Save data
    p = str(Path(os.getcwd()).parent.parent) + '/data/pages/'

    with open(p + page_py.title + '.json', 'w') as f:
        json.dump(export, f, indent=2)
