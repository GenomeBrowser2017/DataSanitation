#!/bin/env python
import re
from sys import argv

filename = argv

def generateNewLineEntry(lineArray):
    return "\t".join(map(str, lineArray))

def convertStartAndEndPoints(line):
    #strip out leading and trailing whitespace
    line = line.strip()

    #skip comments
    if( not line.startswith("#")):
        lineSplitByTabs = re.split(r'\t+', line)

        #only process if there are 9 fields
        if(9 == len(lineSplitByTabs)):
            rem = re.search('([a-zA-Z0-9_]+)\.([0-9]+)\.([0-9]+)-([0-9]+)', lineSplitByTabs[0])
            try:
                geneStart = int(rem.group(3))
                featureStart_gene = int(lineSplitByTabs[3])
                featureEnd_gene = int(lineSplitByTabs[4])
                if(fileName[1].startswith("TMHMM")):
                    featureStart_gene = 3 * featureStart_gene
                    featureEnd_gene = 3 * featureEnd_gene
                featureStart_global = geneStart + featureStart_gene
                featureEnd_global = geneStart + featureEnd_gene;
                newSequenceName = "{}:{}".format(rem.group(1), rem.group(2));
                newLineSplitByTabs = [newSequenceName, lineSplitByTabs[1], lineSplitByTabs[2], featureStart_global, featureEnd_global, lineSplitByTabs[5], lineSplitByTabs[6], lineSplitByTabs[7], lineSplitByTabs[8]]
                print generateNewLineEntry(newLineSplitByTabs)
            except:
                print "#e:{0}".format(line)
                pass

        else:
            print "#9:{0}".format(line)
    else:
        print "#c{0}".format(line)

def main(fileName):
    targetFile = open(fileName[1])
    for line in targetFile:
        convertStartAndEndPoints(line)

main(filename)
