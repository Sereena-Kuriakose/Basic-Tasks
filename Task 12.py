def copy(txt,n):
    flen = 2
    if flen >len(txt):
        flen =len(txt)
    sbter = txt[:flen]
    result = ""
    for i in range (n):
        result = result + sbter
    return result
print(copy("abcd",3))

