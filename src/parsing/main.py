"""
This script will read a wikipedia page into a collection of text and meta data to be processed.
As an example, we will use Napoleon Bonaparte wiki page:
https://en.wikipedia.org/wiki/Napoleon
"""

import wikipediaapi
import json
import sys
import os
import multiprocessing as mp,os
import time
from pathlib import Path
import sys
#wikipediaapi.log.setLevel(level=wikipediaapi.logging.DEBUG)

# Set handler if you use Python in interactive mode
#out_hdlr = wikipediaapi.logging.StreamHandler(sys.stderr)
#out_hdlr.setFormatter(wikipediaapi.logging.Formatter('%(asctime)s %(message)s'))
#out_hdlr.setLevel(wikipediaapi.logging.DEBUG)
#wikipediaapi.log.addHandler(out_hdlr)

wiki = wikipediaapi.Wikipedia('en')



# TODO add flags for language

# splitting file into chunks(pointers)
# creating each thread for each chunk
#fix shit


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

        # NOTE: this is probably dirty, could use classes instead?
        export['headers'].append(temp_header)
        export['content'].append(unit.text)

        get_data(export, temp_header, unit.sections)

def check_path():
    p = Path(os.getcwd()).parent.parent / 'data';
    
    if not os.path.exists(p):
        os.mkdir(p);
    p = p / 'pages'
    if not os.path.exists(p):
        os.mkdir(p);
    p = p / 'raw'
    if not os.path.exists(p):
        os.mkdir(p)
    return p

'''def listIt(filepath):
    #Mode can be f for files and i for input that can be single  string or array separated by space
    
'''
def normalFetch(data,path):
    successful= 0;
    failure =0 ;
    for target in data:
        try:
            
            
            #page_py = wiki.page(target)
            page_py = wiki.page(target)
            print(page_py)
        
            # Check for page existence
            if not page_py.exists():
                print(f"ERROR: Page {target} doesn't exist.")    
                failure +=1                    
                # Create data
            else :
                export = {
                    'headers': [],
                    'content': []
                }

                # Fetch data
                get_data(export, [], page_py.sections)

                # Save data
                # NOTE: this could be done a litte better
                
                with open(path / (page_py.title.replace(' ', '_') + '.json'), 'w') as f:
                    json.dump(export, f, indent=2)
                print(f"SUCCESS : Fetched data for : {target}")
                successful +=1
            
        except Exception as e:
            print(f"ERROR while fetching data for : {e}")
            failure +=1

    print(f"Successeful : {successful}\nFailiure : {failure}")
#function for -i flag
def arrayFetch(inputPath,path):
    successful= 0;
    failure =0 ;
    try:
        with open(inputPath,'rb') as fh:
            for targets in fh:
                try:                      
                    #convert to str     
                    target = targets.rstrip(b'\n')
                    page_py = wiki.page(target)

                    # Check for page existence
                    if not page_py.exists():
                        print(f"ERROR: Page {target} doesn't exist.")    
                        failure +=1                    
                        # Create data
                    else :
                        export = {
                            'headers': [],
                            'content': []
                        }

                        # Fetch data
                        get_data(export, [], page_py.sections)

                        # Save data
                        # NOTE: this could be done a litte better
                        
                        with open(path / (page_py.title.replace(' ', '_') + '.json'), 'w') as f:
                            json.dump(export, f, indent=2)
                        print(f"SUCCESS : Fetched data for : {target}")
                        successful +=1
                except:
                    print(f"ERROR while fetching data for : {target}")
                    failure +=1
    except Exception as e:
        print(e)
    return (f'S : {successful}\nF : {failure}')

#function for -f flag <=50MB
def smallFileDataParser(inputPath,outputPath):

    arrayFetch(inputPath,outputPath)
    

#function for -f flag >50MB
def bigFileDataParser(path):
    pass

if __name__ == '__main__':
    # Read input
    start = time.time()
    targets = sys.argv[1:]
    #Empty data array
    data = []
    #Checking if output exits and if it doesn't it creates one
    path = check_path()
    
    if(targets[0] == '-f'):
        filePath = Path(os.getcwd()).parent.parent / 'input'
        if(os.path.exists(filePath)):
            filePath = filePath / targets[1]
            if(os.path.getsize(filePath)):
                smallFileDataParser(filePath,path)
            else:
                bigFileDataParser(path)
        else:
            print('File not found!')
    elif(targets[0] == '-i'):
        if(len(targets)<50):
            data = targets[1:]    
            normalFetch(data,path)
        else:
            print("Max arguments with -i flag is 50 for more use txt file with -f flag!"); 
    else:
        print('Invalid aruguments given. For more information run --help');
    end = time.time();

    print(end-start)

    
    
    
