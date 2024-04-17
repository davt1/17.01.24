str1, str2, str3 = input(), input(), input()
#str1, str2, str3 = "SANTACLAUS", "DEDMOROZ", "SANTAMOROZDEDCLAUS"

def dct(s):
    d = dict()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

answ = "YES"
# if dct(str1) | dct(str2) == dct(str3):
#    answ = "YES"
dct1 = dct(str1)
dct2 = dct(str2)
dct3 = dct(str3)
def correct_update (dct1, dct2):
    dct = {} #{key: dct1[key] + dct2[key] for key in dct1 | dct2}
    for key in dct1 | dct2:
        val1 = dct1.get(key) if dct1.get(key) else 0
        val2 = dct2.get(key) if dct2.get(key) else 0
        dct[key] = val1 + val2
    return dct 

dct1 = correct_update(dct1, dct2)
max_dict = dct3 if len(dct1) < len(dct3) else dct1
for l in max_dict:
    if not (dct1.get(l) and dct3.get(l)):
        answ='NO'
        break
    if dct1[l] != dct3[l]:
        answ='NO'
        break
print(answ)