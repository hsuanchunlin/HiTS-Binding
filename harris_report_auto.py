##################################################
# Hsuan-Chun Lin
# 10/25/2014
# Recode harris report in Python
# Techinique include: dictionary, file IO
# and argument files
#Usage:
#python harris_report.py EQB_ATC_1.fq_p.fastq EQB_2_1.tab 26 6 1
#Remember number starts from 0
#"Usage is: python harris_report_auto.py <inputfile> <start> <howmany> <summary=1 other = summary+2nt>"
###################################################

#!/usr/bin/python

import sys, string

      
def twoNt():
    nT = ["A","C","G","T"]
    twoNtName = ""
    k = 0
    dT =  ["" for x in range(16)]
    for i in range(4):
        for j in range(4):
            twoNtName = nT[i]+nT[j]
            dT[k] = twoNtName
            k = k+1
    return dT
def sixNt():
    nT = ["A","C","G","T"]
    sixnt = ["" for x in range(4096)]
    q = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        for n in range(4):
                            sixnt[q] = nT[i]+ nT[j]+ nT[k]+ nT[l]+ nT[m]+ nT[n]
                            q = q + 1
    return sixnt



# Create a function to create an hashtable (dictionary)
    

    
if __name__ == '__main__':
    print("The length of argv is ", len(sys.argv))
    if len(sys.argv) == 6:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]+".tab"
        number = int(sys.argv[3])
        howmany = int(sys.argv[4])
        decision = int(sys.argv[5])
        phantom = 0
    #open a reading file
        fi = open(inputFile, "r+") #for file input
        fo = open(outputFile, "w") #for file output

    #create the two and six nucleotide
        sixN = sixNt()
        twoN = twoNt()

    #create an empty dictionary
        dictP = {}
        if decision == 1: # for summary only
            for i in sixN:
                dictP[i] = 0

            print("Dictionary generated!!")
            while(True): #Unlimited loop
                head = fi.readline()
                if not head:
                      break
                seqRead = fi.readline() #each time read one line
                plus = fi.readline()
                quality = fi.readline()
                seqChop = seqRead.strip() #each time chomp the string from  the right
                try:
                    dictP[seqChop[number:number+howmany]] += 1
                    phantom = phantom + 1
                except:
                    phantom = phantom

            #export the hashtable
            print("Exporting tab file!!")
            for i in sixN:
                writeSeq = i + "\t" + str(dictP[i]) + "\n"
                fo.write(writeSeq)
    #for multiple mer
        else:
            #fill the hashtag into the dictionary
            for i in sixN:
                for j in twoN:
                    dictP[i,j] = 0
            print("Dictionary generated!!")
            while(True): #unlimited loop
                head = fi.readline()
                if not head:
                    break
                seqRead = fi.readline() #each time read one line
                plus = fi.readline()
                quality = fi.readline()
                seqChop = seqRead.strip() #each time chomp the string from  the right
                try:
                    dictP[seqChop[number:number+howmany], seqChop[0:0+2]] += 1
                    phantom = phantom + 1
                except:
                    phantom = phantom
            #export the hashtable
            print("Exporting tab file!!")
            for i in sixN:
                for j in twoN:
                    writeSeq = i + "\t" + j + "\t" + str(dictP[i,j]) + "\n"
                    fo.write(writeSeq)
        fi.close()
        fo.close()
        print("Total sequence number = ", phantom)
    
    else:
        print("Usage is: python harris_report_py.py <inputfile> <outputfile> <start> <howmany> <summary=1 other = summary+2nt>")

  
