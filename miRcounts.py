#! /usr/bin/env python

'''
This will take raw small RNA reads in fastq format and output counts of
the known miRNA. 
This script requires Python V2, Biopython, and Blast+.
 
usage: ./miRcounts_fast.py known_miRNA RAWREADS.fastq output.txt 
'''

import sys as sys
import time
import tempfile
from Bio import SeqIO
from StringIO import StringIO
import subprocess as SP


start_time = time.time()
knownMiRNA=open(sys.argv[1],'r')
fileinput=open(sys.argv[2],'r')
fileoutput=open(sys.argv[3],'w')
fastaDB = tempfile.NamedTemporaryFile()
knownMiRNAlen = tempfile.NamedTemporaryFile()

##############################################################################
# First add the length of each known miRNA sequence to the name because
# blast wont check for exact length match, so later we have to check 
# against this 'real' length. 

miRNA = []
for line in knownMiRNA:
    miRNA.append(line)
	
names = miRNA[::2] 
seqs = miRNA[1::2]
 
numPrefix = []
for line in seqs:
    numPrefix.append(str(len(line)-1) + '~')    

justNames = []
for line in names:
    justNames.append(line.split('>')[1])

###### new WIP
# for this part:
namesNums = []  # The new miRNA names with length prefix attached
namesDB = []  # will need this list of names for the counter in the last part
for x in range(len(names)):
    namesDB.append(numPrefix[x] + justNames[x].rstrip())
    namesNums.append('>' + numPrefix[x] + justNames[x])
######    

final = []
for x in range(len(names)):
    final.append(namesNums[x])
    final.append(seqs[x])

# put the miRNA DB with number prefix into a temporary file
for part in range(len(final)):
    knownMiRNAlen.write(final[part])

# Convert the raw fastq file into a fasta file 
print "*** First we convert the fastq file into a fasta file ***"
num_reads = SeqIO.convert(fileinput, "fastq", fastaDB, "fasta")

##############################################################################
# Run BLAST 
# To make the fasta file into a blast database
print "*** Making fasta file into Blast database. ***"
makedb = SP.Popen(['makeblastdb', '-in', fastaDB.name, 
                 '-dbtype', 'nucl'])
makedb.wait()

# Running the blast (this is a special blast with parameters optimised
# for short reads):
print "*** blast database is ready, now the blast starts ***"
blastseqs = SP.Popen(['blastn', '-query', knownMiRNAlen.name, '-db', 
					fastaDB.name, '-evalue', '0.01', '-task', 'blastn-short',
					'-perc_identity', '100', '-strand', 'plus', 
					'-max_target_seqs', '1000000', '-outfmt', 
					"6 qseqid evalue length sseqid nident"], stdout=SP.PIPE) 

# Since used PIPE to store the blastn output, retrieve it with .communicate()
blastOutput = blastseqs.communicate()
outlist = blastOutput[0].split('\n')
# because the above separating makes the last item in the list, '', 
# we remove it:
outlist.pop()


##############################################################################
# Count up the miRNA found with the blast (only keeping identical lengths):

# make a dictionary to hold the miRNA names and counts:
counts = {}
for name in namesDB:
    name = name.rsplit('~')[1]
    counts[name] = 0

for line in outlist:
    seq = line.rsplit('\t')
    name = seq[0].rsplit('~')[1]
    expect_length = int(seq[0].rsplit('~')[0])
    if expect_length == int(seq[2]):
        counts[name] += 1


# write my count dictionary into the output file 
sumCounts = 0
for key, value in counts.items():
    fileoutput.write("%s\t%s\n" %(key,value)) 
    sumCounts += value
   
print("--- RUNTIME: %s minutes ---" % ((time.time() - start_time)/60))
print "*** Counting complete, check out the output file! ***"
print("Total known miRNA found: %s" % sumCounts)

knownMiRNAlen.close()
fastaDB.close()
