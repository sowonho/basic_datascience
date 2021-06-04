# printfile.py

import matplotlib.pyplot as plt

def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    temp = infile.readline()
    print(temp)
    mpg = []
    hp = []
    
    for line in infile.readlines():
        line.strip()
        i = line.find('"',1)
        print(i, end= ":")  # " 위치 찾기
        line = line[i+1:] # 자동차 이름 제거
        a = line.split()
        mpg.append(eval(a[0]))
        hp.append(eval(a[3]))
        
        print(a)
       
    infile.close()

    plt.scatter(mpg, hp)
    plt.show()
main()
