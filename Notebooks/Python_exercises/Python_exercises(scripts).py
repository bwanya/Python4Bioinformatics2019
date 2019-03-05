#!/home/user/miniconda3/bin/python

## Exercise 1_Calculating GC & AT content
trna=("AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA")
len(trna)
A_total=trna.count("A")
C_total=trna.count("C")
G_total=trna.count("G")
T_total=trna.count("T")
GC_total=trna.count("C")+trna.count("G")
AT_total=trna.count("A")+trna.count("T")
Total_nucleotides=len(trna)
print(GC_total)
print(AT_total)
print(Total_nucleotides)
GC_content=(GC_total/Total_nucleotides)*(100)
AT_content=(AT_total/Total_nucleotides)*(100)
print(GC_content)
print(AT_content)


## Exercise 2 The square of prime numbers between 1&100

Prime_numbers=range(1,100)
[i**2 for i in range(1,100) if i%3==0]




