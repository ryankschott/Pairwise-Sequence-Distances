# Pairwise-Sequence-Distances

An updated set of scripts to calculate pairwise sequences distances from the following paper:

Targeted capture of complete coding regions across divergent species

Ryan K Schott, Bhawandeep Panesar, Daren C Card, Matthew Preston, Todd A Castoe, Belinda SW Chang
Genome Biol. Evol. 9(2):398–414.


# Decsriptopm

These set of scripts take a folder of fasta files each containing two sequences for comparison. The sequences will be aligned either using MUSCLE or PRANK and pairwise sequence distance calculated using USEARCH.
Optionally gaps can be removed using TRIMAL prior to calcular sequences distances, which will decrease the distances for gappy alingments.


# Usage Example

python distance_PRANK.py <folder path> <outputfile>


# Prerquisites

These programs should be available in the PATH:

Python
PRANK (http://wasabiapp.org/download/prank/)
MUSCLE (https://www.drive5.com/muscle/downloads.htm)
USEARCH (https://www.drive5.com/usearch/download.html)
TRIMAL (http://trimal.cgenomics.org/downloads)
