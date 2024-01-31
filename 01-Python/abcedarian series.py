str1="ABCDEF"
str2="ate"
str3=''.join(sorted(str1))
strnew=""
for i in str3:
    print(i+str2,end=" ")
