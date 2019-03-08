#!/home/user/miniconda3/bin/python

## Exercise 1_Calculating GC & AT percent content

trna=("AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA")
len(trna)
A_total=trna.count("A")
C_total=trna.count("C")
G_total=trna.count("G")
T_total=trna.count("T")

GC_total=trna.count("C")+trna.count("G")
AT_total=trna.count("A")+trna.count("T")
print(GC_total)
print(AT_total)

GC_content=(GC_total/len(trna))*(100)
AT_content=(AT_total/len(trna))*(100)
print( "GC percent content is %d"%GC_content)
print( "AT percent content is %d"%AT_content)






