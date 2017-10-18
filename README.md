## miRcounts

This script will take raw small RNA reads in fastq format and output counts of
the known miRNA. 
This script requires Python V2, Biopython, and Blast+.
 
usage: ./raw_to_counts.py known_miRNA.fasta RawReads.fastq output.txt 

### Test files:
##### known_miRNA.fasta
A set of known *Brassica napus* miRNA from the publication: (identical miRNA sequences were removed)

    Shen, Enhui et al. "Identification, Evolution, And Expression Partitioning Of miRNAs In 
    Allopolyploid Brassica napus". EXBOTJ 66.22 (2015): 7241-7253.

##### RawReads.fastq
Sequence reads in fastq format from a *Brassica napus* sample, taken directly from a MiSeq. No pre-processing required -- just be sure to unzip them first, can be done in the command line with this command:
    gunzip filename.fastq.gz




_________
_This project is licensed under the terms of the MIT license._
