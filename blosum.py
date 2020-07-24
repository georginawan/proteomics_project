import xlrd
file = "C:\\Users\\surface\\Documents\\WeChat Files\\Georginanananana\\Files\\blusom62.xlsx"
def read_excel(file):
    blosum_dict = {}
    wb = xlrd.open_workbook(filename=file)
    sheet1 = wb.sheet_by_index(0)
    row_num = 0
    while True:
        row_num += 1
        try:
            rows = sheet1.row_values(row_num)
            #if len(rows) > 0:                
            label = rows[0]
            if len(label) > 0:
                blosum_dict[label]=rows[1:]              
        except:
            break
    return blosum_dict

def lineToVector(blosum,peptide):
    vector = []
    for aa in peptide:
        data = blosum[aa]
        for i in data:
            vector.append(i)
    return vector
    
filep = open(r"C:\Users\surface\Desktop\Georgina\3007\final\positive_testing.txt","r")
filen = open(r"C:\Users\surface\Desktop\Georgina\3007\final\negative_testing.txt","r")
filenew = open(r"C:\Users\surface\Desktop\Georgina\3007\final\blosum_testing_libsvm.txt","w")
def main_1(filex,x,blosum):
    loop = True    
    while loop:
        name = filex.readline()
        if len(name) > 0:
            peptide = filex.readline()
            peptide = peptide.replace("\n","")            
            vector = lineToVector(blosum,peptide)
            newline = ""
            for i in range(1,len(vector)+1):
                newline = newline + str(i) + ":" + str(vector[i-1]) + " "           
            filenew.write(x+" "+newline+"\n")
        else:
            loop = False

blosum = read_excel(file)            
main_1(filep,"1",blosum)
main_1(filen,"2",blosum)
