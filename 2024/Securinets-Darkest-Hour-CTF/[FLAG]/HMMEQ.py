flag=b"Securinets{REDIRECT}"
flag1=bytes_to_long(flag[0: 11])
flag2=bytes_to_long(flag[11:22])
flag3=bytes_to_long(flag[22:33])
flag4=bytes_to_long(flag[33:44])

assert flag1+flag2+3*flag3==583601198217999802821640273 
assert 3*flag1+2*flag2+2*flag3==787432535105101541361772353 
assert -flag2-2*flag3+2*flag4== -119883660368948934388465829 
assert -flag1+flag3-flag4==-102047525517112400806626497
