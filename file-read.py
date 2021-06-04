# file-read.py

def main():
    s = 0  # 합 계산
    c = 0  # 입력 데이터 수
    data = []
    
    infile = open("data2.txt", "r") # 파일 열기
    temp = infile.read()
    inList = temp.split(',')

    for i in inList:
        data.append(int(i))  # 리스트 추가
        s = s + int(i)  # 데이터 합
        c = c + 1
        
    infile.close()  #파일 닫기
    
    print(">> data: ", data)
    print(">> n:{0:2}, avg : {1:5.2f}".format(c, s / c))
     
main()

