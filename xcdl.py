#!/usr/bin/env/python
#
# A script to download bird sound files from the www.xeno-canto.org archives without metadata
#
# Usage: python scr/data/xcdl.py searchTerm1 searchTerm2 ... searchTermN
#
# The program downloads all the files found with the search terms into
# subdirectory data/xeno-canto-dataset.
#
# Karoliina Oksanen, 2014
# Updated to python 3.7.4, Agnieszka Mikolajczyk, 2019

import urllib.request
import sys
import re
import os

# returns the Xeno Canto catalogue numbers for the given search terms.
# @param searchTerms: list of search terms
# http://www.xeno-canto.org/explore?query=common+snipe
def read_numbers(searchTerms):
    i = 1 # page number
    numbers = []
    while True:
        page = urllib.request.urlopen('https://xeno-canto.org/explore?pg={0}&query={1}'.format(i,
            '+'.join(searchTerms)))
        newResults = re.findall(r"/(\d+)/download", page.read().decode('utf-8'))
        print(newResults)
        if(len(newResults) > 0):
            numbers.extend(newResults)
        # check if there are more than 1 page of results (30 results per page)
        if(len(newResults) < 30):
            break
        else:
            i += 1 # move onto next page

    return numbers

# returns the filenames for all Xeno Canto bird sound files found with the given
# search terms.
# @param searchTerms: list of search terms
def read_filenames(searchTerms):
    i = 1 # page number
    filenames = []
    while True:
        page = urllib.request.urlopen('https://xeno-canto.org/explore?pg={0}&query={1}'.format(i,
            '+'.join(searchTerms)))
        newResults = re.findall(r"data-xc-filepath=\'(\S+)\'", page.read().decode('utf-8'))
        if(len(newResults) > 0):
            filenames.extend(newResults)
        # check if there are more than 1 page of results (30 results per page)
        if(len(newResults) < 30):
            break
        else:
            i += 1 # move onto next page

    return filenames

# creates the subdirectory data/xeno-canto-dataset if necessary, and downloads all sound files
# found with the search terms into that directory. inserts the XC catalogue
# number in front of the file name, otherwise preserving original file names.
def download(searchTerms):
    # create data/xeno-canto-dataset directory
    if not os.path.exists("data/xeno-canto-dataset"):
        print("Creating subdirectory \"data/xeno-canto-dataset\" for downloaded files...")
        os.makedirs("data/xeno-canto-dataset")
    filenames = read_filenames(searchTerms)
    if len(filenames) == 0:
        print("No search results.")
        sys.exit()
    numbers = read_numbers(searchTerms)
    # regex for extracting the filename from the file URL
    fnFinder = re.compile('\S+/+(\S+)')
    print("A total of {0} files will be downloaded.".format(len(filenames)))
    for i in range(0, len(filenames)):
        print("Name: " + filenames[i])

        localFilename = numbers[i] + "_" + fnFinder.findall(filenames[i])[0]
        # some filenames in XC are in cyrillic characters, which causes them to
        # be too long in unicode values. in these cases, just use the ID number
        # as the filename.
        if(len("data/xeno-canto-dataset/" + localFilename) > 255):
            localFilename = numbers[i]
            print("Downloading " + localFilename)
        urllib.request.urlretrieve('https:'+filenames[i], "data/xeno-canto-dataset/" + localFilename)

def main(argv):
    if(len(sys.argv) < 2):
        print("Usage: scr/data/python xcdl.py searchTerm1 searchTerm2 ... searchTermN")
        print("Example: scr/data/python xcdl.py common snipe")
        return
    else:
        download(argv[1:len(argv)])

if __name__ == "__main__":
    main(sys.argv)
