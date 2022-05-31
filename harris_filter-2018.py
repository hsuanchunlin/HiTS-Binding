# -*- coding: utf-8 -*-
"""
Created on Fri May 18 15:04:35 2018
@author: Hsuan-chun Lin for recode in python
Name:		harris_filter.py
adapted from: 	Neil Molyneaux written in perl
Purpose:	Filters a Fastq file to only include sequences that contain a particular 21-mer.
Usage:	harris_filter.py <fastq file> <export file>

"""
import sys
import os

# function to calculate the mismatch
def quality_check(sequence, reference):
    seq_len = len(sequence)
    ref_len = len(reference)
    n = 0
    for i in range(ref_len):
        if sequence[i] != reference[i]:
            n += 1
    return n


# Here the code starts
if not sys.argv[1]:
    print(
        """
          Please check the command usage as
          python harris_filter.py <fastq file> <modified fastq file>
          """
    )

fileIn = sys.argv[1]
fileOut = sys.argv[2]
test_seq = "ATGTCGAAGTCATCC"
len_test = len(test_seq)

sequence_start = 2
output = open(sys.argv[2], "a")

with open(sys.argv[1], "r") as f:
    while True:
        header = f.readline().strip()
        seq = f.readline().strip()
        plus = f.readline().strip()
        quality = f.readline().strip()
        if not header:
            break
        try:
            comp_target = seq[sequence_start : (sequence_start + len_test)]
            # Start to check the sequence, if mismatch <=2, then print the sequence into the file
            mismatch = quality_check(comp_target, test_seq)
            if mismatch <= 2:
                output.writelines(header + "\n")
                output.writelines(seq + "\n")
                output.writelines(plus + "\n")
                output.writelines(quality + "\n")

        except:
            pass
            # print("String_error, length does not match!")

output.close()
