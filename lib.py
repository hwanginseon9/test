class BookList:
    def __init__(self,num,name,author):# 고유번호, 책 이름, 저자
            self.num=num
            self.name=name
            self.author= author

    def showList(self):
        books=[[1,'나미야 잡화점의 기적','하가시노 게이고'],
               [2,'      7년 후      ','  기욤 뭐소   '],
               [3,'      긴긴밤      ','     루리     '],
               [4,'     부의 변곡점   ','    정윤진    '],
               [5,'     책의 부엌     ','    김지혜    '],
               [6,'     천사의 부름   ','   기욤 뭐소   '],
               [7, '  지구 끝의 온실  ','      김초엽   '],
               [8, '   미움 받을 용기 ','  가시미 이치로 '],
               [9,'    메이즈 러너    ','  제임스 대시너 '],
               [10,'해리포너와 마법사의 돌',' J.K롤린  ']]
        #print('고유번호      책제목             저자')
        #for x in books:
        #    print(x)

    def rental(self):
        while True:
            print("-" * 40 + "\n")
            print('1. 장바구니에 담긴 리스트 보기 \n2. 대여하기 \n3.종료')
            print("-" * 40 + "\n")
            menu = int(input("메뉴 선택>>>"))  # int형이 아닐 시 오류나면서 종료.

            # 1을 눌렀을때: 도서 정보 입력
            if menu == 1:
                self.showList()
                while True:
                    slt = input('장바구니에 취소할 도서가 있습니까? (y/n)')
                    if slt == 'y' or slt == 'Y':
                        num = int(input('취소할 도서 고유 번호 입력>>'))
                        for list in self.showList():
                            print(list)

                            '''if list==num:
                                del books[num]
                                print("정상적으로 삭제 되었습니다.\n")'''
                    elif slt == 'n' or slt == 'N':
                        print("취소할 도서가 없습니다.\n")
                    else:
                        print("마지막")
            else:
                print("잘못입력함\n")

a=BookList(1,'대한민국','황인선')
i=0
for list in a.showList:
    print(list)
    i+=1
    print(i)
#우왕테스트한당