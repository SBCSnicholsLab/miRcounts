#! /usr/bin/env python

'''
This will take raw small RNA reads in fastq format and output counts of
the known miRNA. 
This script requires Python V2 and Biopython.

usage: ./miRcounts_simple.py known_miRNA.fasta RawSeq.fastq output.txt
'''

import sys as sys
import time
import Bio
from Bio import SeqIO
from StringIO import StringIO

start_time = time.time()
DBknown=SeqIO.to_dict(SeqIO.parse(sys.argv[1],'fasta'))
fastaDB=SeqIO.index(sys.argv[2],'fastq')
output=open(sys.argv[3], 'w')

print "*This may take a while*"

counts = {}
for record in DBknown:
    counts[record] = 0
	
for mirna in DBknown.itervalues():
    mirna.seq = mirna.seq.back_transcribe()
	
for record in fastaDB.itervalues():
    for mirna in DBknown.itervalues():
        if str(record.seq).find(str(mirna.seq)) > -1:
            counts[mirna.name] += 1 
				
for key, value in counts.items():
    output.write("%s\t%s\n" %(key,value))
	
	
print("--- RUNTIME: %s minutes ---" % ((time.time() - start_time)/60))	
print "*** Counting complete, check out the output file! ***"	
