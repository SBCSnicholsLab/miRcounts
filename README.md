## miRcounts

This will take raw small RNA reads in fastq format and output counts of
the known miRNA. 
This script requires Python V2, Biopython, and Blast+.
 
usage: ./raw_to_counts_fast.py known_miRNA.fasta RAWREADS.fastq output.txt 

### Test files:

######-- known_miRNA.fasta
A set of known *Brassica napus* miRNA from the publication: (identical miRNA sequences were removed)
 
     Shen, Enhui et al. "Identification, Evolution, And Expression Partitioning Of miRNAs In 
     Allopolyploid Brassica napus". EXBOTJ 66.22 (2015): 7241-7253.
 
######-- RawSeq.fastq
*Brassica napus* reads taken directly from sequencing on a MiSeq. 
