#!/home/user/miniconda3/bin/python

## Finding The square of prime numbers between 1&100

Prime_numbers=range(1,100)
[i**2 for i in range(1,100) if i%3==0]


## Finding the reverse complement of 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'

template = "AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"
print(template)

rev_template=list(template)
rev_template.reverse()
rev_template

d = { 'T' : 'A', 'A' :'T', 'C' : 'G', 'G': 'C'}
Reverse=[d[i] for i in template]
print(Reverse)
"".join(Reverse)

