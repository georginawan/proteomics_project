#find N5C5 for a given peptide
def N5C5(peptide):
    N5C5 = peptide[:5] + peptide[:-6:-1]
    return N5C5

#build an empty dict following specific sequence
def aalist():
    aalist = dict()
    for i in "GAVLIPFYWSTCMNQDEKRH":
        aalist[i] = 0
    return aalist

#find AAC for every N5C5 fragment
def AAC(peptide):
    AAC = aalist()
    for i in peptide:
        AAC[i] += 1/len(peptide)
    return AAC

#main part_1
filep = open(r"C:\Users\surface\Desktop\lab\finalfinal\positive_training.txt","r")
filen1 = open(r"C:\Users\surface\Desktop\lab\finalfinal\negative1_training.txt","r")
filen2 = open(r"C:\Users\surface\Desktop\lab\finalfinal\negative2_training.txt","r")
filenew = open(r"C:\Users\surface\Desktop\lab\finalfinal\N5C52libsvm.txt","w")
def main_1(filex,x):
    loop = True
    while loop:
        name = filex.readline()
        if len(name) > 0:
            peptide = filex.readline()
            peptide = peptide.replace("\n","")
            n5c5 = N5C5(peptide)
            aac = AAC(n5c5)
            aac = list(aac.values())
            newline = ""
            for i in range(1,21):
                newline = newline + str(i) + ":" + str(aac[i-1]) + " "            
            filenew.write(x+" "+newline+"\n")
        else:
            loop = False
#main_1(filep,"1")
#main_1(filen,"2")


def dictinlist(n):
    lista = list()
    for i in range(n):
        lista.append(aalist())
    return lista

#main part 2
def main_2(filex):
    total = dictinlist(10)
    loop = True
    while loop:
        name = filex.readline()
        if len(name) > 0:
            peptide = filex.readline()
            peptide = peptide.replace("\n","")
            n5c5 = N5C5(peptide)
            for i in range(10):
                total[i][n5c5[i]] += 1
        else:
            loop = False
    return total


import xlwt
path = r"C:\Users\surface\Desktop\lab\lab-2.xls"
total = main_2(filep)
rb = xlwt.Workbook()
sheet = rb.add_sheet('sheet1',cell_overwrite_ok=True)
for i in range(10):
    dict_ = total[i]
    count = 1
    for j in dict_.values():       
        sheet.write(i+1,count,j/463)              
        count += 1
total = main_2(filen1)
for i in range(10):
    dict_ = total[i]
    count = 1
    for j in dict_.values():       
        sheet.write(i+12,count,j/463)              
        count += 1
total = main_2(filen2)
for i in range(10):
    dict_ = total[i]
    count = 1
    for j in dict_.values():       
        sheet.write(i+23,count,j/463)              
        count += 1


rb.save(path)

filep.close()
filen1.close()
filen2.close()
filenew.close()