import xlwt
import matplotlib.pyplot as plt
#add weight n to a line
def multiplyn(line,n):
    line = line.split(",")
    #print(line)
    actual = line[1][0]
    dist1 = line[4].replace("*","")
    dist1 = float(dist1)*float(n)
    dist2 = line[5].replace("*","").replace("\n","")
    dist2 = float(dist2)
    if dist1 < dist2:
        predict = "2"
    else:
        predict = "1"
    if actual == "1" and predict == "1":
        return "TP"
    elif actual == "1" and predict == "2":
        return "FN"
    elif actual == "2" and predict == "1":
        return "FP"
    elif actual == "2" and predict == "2":
        return "TN"
    else:
        return False
#main function of adding weight
def weight(lines,n):
    #filex = open(r"C:\Users\surface\Desktop\Georgina\3007\pwm_aac.txt","r")        
    correct = 0
    TP = FP = TN = FN =0
    total = 0
    loop = True
    for line in lines:
        #line = filex.readline()
        if len(line) == 0:
            loop = False
        else: 
            total += 1
            result = multiplyn(line,n)
            if result == "TP":
                correct += 1
                TP += 1
            elif result == "TN":
                correct += 1
                TN += 1
            elif result == "FP":
                FP += 1
            elif result == "FN":
                FN += 1
            else:
                pass            
    
    return correct,total,TP,FP,FN,TN

def main(filex):
    #roc =[]
    roc = [[],[]]
    weightlist = [j/10.0 for j in range(1,101)]  
    lines = filex.readlines()
    for w in weightlist:
        rst = weight(lines,w)
        correct = rst[0]
        total = rst[1]
        accuracy = correct/total        
        sn = rst[2]/(rst[2]+rst[4])
        sp = rst[5]/(rst[5]+rst[3])
        #print(w,accuracy,sn,sp,sn*sp)
        roc.append([1-sp,sn])   
        roc[0].append(1-sp)
        roc[1].append(sn)     
    return roc

file1 = open(r"C:\Users\surface\Desktop\Georgina\3007\pwm_aac.txt","r")
file2 = open(r"C:\Users\surface\Desktop\Georgina\3007\pwm2.txt","r")
roc1 = main(file1)
roc2 = main(file2)
plt.plot(roc1[0],roc1[1],label='PWM+AAC')
plt.plot(roc2[0],roc2[1],label='PWM')
plt.legend()
plt.show()
file1.close()
file2.close()

#path = r"C:\Users\surface\Desktop\lab\lab-2.xls"
'''
rb = xlwt.Workbook()
sheet = rb.add_sheet('sheet1',cell_overwrite_ok=True)

roc = main()

count = 1
for i in roc:        
    sheet.write(0,count,i[0])        
    sheet.write(1,count,i[1])            
    count += 1
rb.save(path)'''
