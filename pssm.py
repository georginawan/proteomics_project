import os
def aadict():
    aadict = dict()
    aa = "ARNDCQEGHILKMFPSTWYV"
    for i in aa:
        aadict[i] = list()
    return aadict

#lst should be a list, numstr should be a string
def strToList(numstr):
    lst = list()
    string = ""
    for i in numstr:
        if i == ",":
            if string == "":
                pass
            else:
                lst.append(int(string))
                string = ""
        else:
            string += i
    return lst

def combineList(listo,listn):
    newlist = list()
    for i in range(len(listo)):
        num = listo[i] + listn[i]
        newlist.append(num)
    return newlist

def nElementList(n):
    lst = list()
    for i in range(n):
        lst.append(0)
    return lst

def fileToDict(path):
    hd = open(path,"r")
    lines = hd.readlines()
    aadict_ = aadict()
    for i in lines[3:]:
        if i == "\n":
            break
        else:
            aa = i[6] #amino acid name
            listo = aadict_[aa]
            i = i[7:70]
            i = i.replace(" ",",")
            lst = strToList(i)
            if listo == []:
                aadict_[aa] = lst
            else:
                aadict_[aa] = combineList(listo,lst)
    hd.close()
    return aadict_   

def dictToList(dct):
    lst = list()
    for aa in dct.keys():
        if dct[aa] == []:
            for i in nElementList(20):
                lst.append(i)
        else:
            for i in dct[aa]:
                lst.append(i)
    return lst

def listToLine(lst):
    count = 1
    line = ""
    for i in lst:
        line += str(count) + ":" + str(i) + " "
        count += 1
    return line

#rootdir是文件夹路径，x是1（positive）/2（negative）,hd是要写入的libsvm文件
def writeIn(rootdir,x,hd):
    filelist = os.listdir(rootdir)
    for filename in range(len(filelist)):
        path = os.path.join(rootdir,filelist[filename])
        if os.path.isfile(path):
            dct = fileToDict(path)
            lst = dictToList(dct)
            line = listToLine(lst)
            hd.write(x + " " + line + "\n")
        else:
            print("False")

def main():
    hd1 = open("C:\\Users\\surface\\Desktop\\lab\\pssm_testing_n1.txt","w")
    hd2 = open("C:\\Users\\surface\\Desktop\\lab\\pssm_testing_n2.txt","w")
    rootdirp = "C:\\Users\\surface\\Desktop\\lab\\pssm_testing\\pssm_p"
    rootdirn1 = "C:\\Users\\surface\\Desktop\\lab\\pssm_testing\\pssm_n1"
    rootdirn2 = "C:\\Users\\surface\\Desktop\\lab\\pssm_testing\\pssm_n2"
    writeIn(rootdirp,"1",hd1)
    writeIn(rootdirn1,"2",hd1)
    writeIn(rootdirp,"1",hd2)
    writeIn(rootdirn2,"2",hd2)
    hd1.close()
    hd2.close()

main()