#!/bin/env python
import re
from sys import argv

filename = argv

def generateNewLineEntry(lineArray):
    return "\t".join(map(str, lineArray))

def convertStartAndEndPoints(line):
    global filename
    #print "{}".format(filename[1])
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
                #do we need to convert AA coordinates to DNA coordinates
                if((filename[1].find("TMHMM.gff") != -1) or (filename[1].find("InterProScan.gff") != -1)):
                    featureStart_gene = 3 * featureStart_gene
                    featureEnd_gene = 3 * featureEnd_gene

                #Do we need to convert gene based coordinates into genome based coordinates
                if(geneStart > featureEnd_gene):
                    featureStart_global = geneStart + featureStart_gene
                    featureEnd_global = geneStart + featureEnd_gene;
                else:
                    featureStart_global = featureStart_gene
                    featureEnd_global = featureEnd_gene;
                newSequenceName = "{}:{}".format(rem.group(1), rem.group(2));
                newLineSplitByTabs = [newSequenceName, lineSplitByTabs[1], lineSplitByTabs[2], featureStart_global, featureEnd_global, lineSplitByTabs[5], lineSplitByTabs[6], lineSplitByTabs[7], lineSplitByTabs[8]]
                print generateNewLineEntry(newLineSplitByTabs)
            except:
                print "#e:{0}".format(line)
                pass

        else:
            print "{0}".format(line)
    else:
        print "#c{0}".format(line)

def main(fileName):
    targetFile = open(fileName[1])
    for line in targetFile:
        convertStartAndEndPoints(line)
    targetFile.close()

main(filename)
