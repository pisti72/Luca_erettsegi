txt = ""
for i in range(1,5+1):
    delimiter = ", "
    if i==5:
        delimiter = ""
    txt += str(i) + delimiter
print(txt)