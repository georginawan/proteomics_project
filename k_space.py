import matplotlib.pyplot as plt
import xlwt
#to find pairs
def find_pairs(peptide,k):
    peptide = peptide.replace("\n","")
    if len(peptide) < k+2:
        pairs = {}        
    else:
        count = 0
        pairs = dict()
        for i in peptide:
            count+=1
            if count+k >=len(peptide):
                break
            else:
                pair = peptide[count-1]+"X"*k+peptide[count+k]
                if pair in pairs.keys():
                    pairs[pair]+=1
                else:
                    pairs[pair]=1
        for i,j in pairs.items():
            pairs[i] = j/(len(peptide)-k-1)
    return pairs

#prepare empty dicts
def ksdict(k):
    aalist = "GAVLIPFYWSTCMNQDEKRH"
    ksdict = dict()
    for i in aalist:
        for j in aalist:
            if i+"X"*k+j in ksdict.keys():
                pass
            else:
                ksdict[i+"X"*k+j] = 0
    return ksdict

#to combine dicts together, x for new dict, y for total
def combine_dict(x,y):
    for u,v in x.items():
        if u in y.keys():
            y[u] += v
        else:
            y[u] = v
    return y
# y-x
def minus_dict(x,y):
    new = dict()
    for u,v in x.items():
        if u in y.keys():
            new[u] = y[u] - v
        else:
            new[u] = 0 - v
    return new

def k_space(peptide,k):
    ks = ksdict(k)    
    pairs = find_pairs(peptide,k)
    total = combine_dict(pairs,ks)
    return total

#filep = open(r"C:\Users\surface\Desktop\lab\finalfinal\positive_training.txt","r")
#filen = open(r"C:\Users\surface\Desktop\lab\finalfinal\negative1_training.txt","r")
#filenew = open(r"C:\Users\surface\Desktop\lab\kspace1_2_libsvm.txt","w")
def main_1(filex,x):
    loop = True
    while loop:
        name = filex.readline()
        if len(name) > 0:
            peptide = filex.readline()
            peptide = peptide.replace("\n","")            
            ks0 = k_space(peptide,2)   #这里要修改
            ks0 = list(ks0.values())
            newline = ""
            for i in range(1,401):
                newline = newline + str(i) + ":" + str(ks0[i-1]) + " "           
            filenew.write(x+" "+newline+"\n")
        else:
            loop = False
            
#main_1(filep,"1")
#main_1(filen,"2")
#filep.close()
#filen.close()
#filenew.close()

def sort_by_value(Dict,topx):
    items = Dict.items()
    pairs=[[j[1],j[0]] for j in items]
    pairs.sort(reverse=True)
    return [pairs[i][1] for i in range(topx)]

filep = r"C:\Users\47696\Documents\lab\positive_training.txt"
filen1 = r"C:\Users\47696\Documents\lab\negative1_training.txt"
filen2 = r"C:\Users\47696\Documents\lab\negative2_training.txt"

def main(filename):
    k = 0
    total = dict()
    while k<=5:
        with open(filename,"r") as hd:
            peptides = hd.readlines()
            for i in peptides[1::2]:
                ktotal = k_space(i,k)
                combine_dict(ktotal,total)
            k+=1
    return total

total_p = main(filep)
total_n1 = main(filen1)
total_n2 = main(filen2)

total_p_n1 = minus_dict(total_n1,total_p)
total_p_n2 = minus_dict(total_n2,total_p)

top20_1 = sort_by_value(total_p_n1,20)
top20_2 = sort_by_value(total_p_n2,20)

num_list_1 = []
num_list_2 = []

for i in top20_1:
    num_list_1.append(total_p_n1[i])
for i in top20_2:
    num_list_2.append(total_p_n2[i])

f = xlwt.Workbook()
sheet1 = f.add_sheet("1")
for i in range(20):
    sheet1.write(i,0,top20_1[i])
    sheet1.write(i,1,num_list_1[i])
    sheet1.write(i,2,top20_2[i])
    sheet1.write(i,3,num_list_2[i])
f.save('kspace.xls')
