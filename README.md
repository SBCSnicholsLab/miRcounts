# miRcounts

There are two versions of this script. I highly recommend the 'fast' version, as it is exponentially faster than the 'simple' version, but requires a local download of Blast.


# miRcounts_simple:

This will take raw small RNA reads in fastq format and output counts of
the known miRNA. 
This script requires Python V2 and Biopython.

usage: ./raw_to_counts_simple.py known_miRNA.fasta RawSeq.fastq output.txt



# miRcounts_fast:

This will take raw small RNA reads in fastq format and output counts of
the known miRNA. 
This script requires Python V2, Biopython, and Blast+.
 
usage: ./raw_to_counts_fast.py known_miRNA.fasta RAWREADS.fastq output.txt 
