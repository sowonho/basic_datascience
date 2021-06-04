# key-input.py

def main():
    s = 0  # 합 계산
    c = 0  # 입력 데이터 수
    data = []
    
    i = input("data(Enter to Quit!)= ")
    while i != "":
        data.append(int(i))  # 리스트 추가
        s = s + int(i)  # 데이터 합
        c = c + 1
        i = input("data(Enter to Quit!)= ")
        
    print(">> data: ", data)
    print(">> avg : ", s / c)
     
main()
