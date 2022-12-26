stu_Info = {} # 딕셔너리 선언
class Student:
    
    def __init__(self):
        self.kor = ''
        self.eng = ''
        self.math = ''
    
    def val_Id(self): # 학번 예외처리 + 유효성 검사 ## 완료 시 val_name()으로 넘어감 ### 완료
        while True:
            self._id = input("학번 = ")
            print()
            if self._id != '':  # 학번이 공백일 경우 예외처리
                if self._id not in stu_Info.keys(): # 유효성 검사
                    self.val_Name()
                    break
                else:
                    print('중복된 학번입니다.\n')
            else:
                print('학번란은 비워둘 수 없습니다.\n')
    
    def val_Name(self): # 이름 예외처리 ## 완료 시 val_sub()로 넘어감 ### 완료
        while True:
            self.name = input("이름 = ")
            print()
            if self.name != '':
                self.val_Sub()
                break
            else:
                print('이름은 비워둘 수 없습니다.\n')
    
    def val_Sub(self): # 과목 예외처리 함수 ## 완료 시 compute(self.kor, self.eng, self.math)로 넘어감 ### 완료
        while True:
            if self.kor != '' and self.eng != '' and self.math != '': # 3가지 과목 성적이 모두 채워질 경우
                    print('성적 입력이 끝났습니다.\n')
                    self.compute()
                    break
            else:
                self.sub = input("입력할 과목(kor, eng, math) = ")
                print()
                if self.sub != '': # 유효성 검사
                    if self.sub == 'kor': # self.sub 에 'kor'을 입력받으면
                        self.val_Kor() # 국어성적 예외처리 함수

                    elif self.sub == 'eng':
                        self.val_Eng() # 영어성적 예외처리 함수

                    elif self.sub == 'math':
                        self.val_Math() # 수학성적 예외처리 함수

                    else:
                        print('과목명을 제대로 입력해 주세요.\n')
                else:
                    print('과목명은 비워둘 수 없습니다.\n')
                
    def val_Kor(self): # 국어 성적 예외처리 ## 완료
        while True:
            if self.kor == '': # 유효성 검사 # self.kor 이 비어있을경우
                self.kor = input("국어 성적 = ") # 공백을 입력받으면 int(input())은 오류가 발생하기 때문에 밑에서 처리
                print()
                if 0 <= int(self.kor) <= 100: # 예외처리 ## 정수를 안받는 경우도 생각해서 try 함수를 써보려 했지만
                    # 잠깐 봐서는 이해가 안되서 포기
                    self.kor = int(self.kor)
                    break
                else:
                    self.kor = ''
                    print('성적은 0 ~ 100 사이로 입력해야 합니다.\n')
            else:
                print('국어 성적은 이미 입력되어 있습니다.\n')
                break
    
    def val_Eng(self): # 영어 성적 예외처리 ## 완료
        while True:
            if self.eng == '': # 유효성 검사
                self.eng = input("영어 성적 = ") # 공백을 입력받으면 int(input())은 오류가 발생하기 때문에 밑에서 처리
                print()
                if 0 <= int(self.eng) <= 100: # 예외처리
                    self.eng = int(self.eng)
                    break
                else:
                    self.eng = ''
                    print('성적은 0 ~ 100 사이로 입력해야 합니다.\n')
            else:
                print('영어 성적은 이미 입력되어 있습니다.\n')
                break
                            
    def val_Math(self): # 수학 성적 예외처리 ## 완료
        while True:
            if self.math == '': # 유효성 검사
                self.math = input("수학 성적 = ") # 공백을 입력받으면 int(input())은 오류가 발생하기 때문에 밑에서 처리
                print()
                if 0 <= int(self.math) <= 100: # 예외처리
                    self.math = int(self.math)
                    break
                else:
                    self.math = ''
                    print('성적은 0 ~ 100 사이로 입력해야 합니다.\n')
            else:
                print('수학 성적칸은 이미 입력되어 있습니다.\n')
                break
            
    def compute(self): # 국어 영어 수학 성적을 토대로 총점, 평균, 학점을 추출 ## 완료시 add_Stu()로 넘어감 ## 완료
        self.tot = self.kor + self.eng + self.math
        self.avg = self.tot / 3
        if self.avg >= 90:
            self.grade = "A"
        elif self.avg >= 80:
            self.grade = "B"
        elif self.avg >= 70:
            self.grade = "C"
        elif self.avg >= 60:
            self.grade = "D"
        else:
            self.grade = "F"
            
    def add_Stu(self): # 받은 학생정보를 학번을 키로 딕셔너리에 저장 ## 완료
        stu_Info[self._id] = [self.name, self.kor, self.eng, self.math, self.tot, self.avg, self.grade]
        print('등록이 완료되었습니다.\n')
        
    def stu_Insert(self): # 1. 학생등록 ## 완료
        self.val_Id() # val_id > val_name > val_sub > compute
        self.add_Stu() # 딕셔너리에 저장

    def search_Id(self): # 2. 학번 검색 ## 완료
        while True:
            if stu_Info == {}:
                print('학생이 없습니다.\n')
                break
            self._id = input("학번 = ")
            print()
            if self._id != '':  # 학번이 공백일 경우 예외처리
                if self._id not in stu_Info.keys(): # 유효성 검사
                    print('존재하지않는 학번입니다.\n')
                else:
                    self.one_Info()
                    break
            else:
                print('학번란은 비워둘 수 없습니다.\n')

    def one_Info(self): # 완료 # 학번검색에 사용
        print('\n학번이 {}인 학생의 이름 : {}, 국어 : {}점, 영어 : {}점, 수학 : {}점, 총점 : {}, 평균 {:.2f}, 학점 : {}\n'.format(self._id, stu_Info[self._id][0], stu_Info[self._id][1], stu_Info[self._id][2], stu_Info[self._id][3], stu_Info[self._id][4], stu_Info[self._id][5], stu_Info[self._id][6]))

    def update_Id(self): # 3. 학번수정 + 예외처리 ## 완료
        while True:
            if stu_Info == {}:
                print('학생이 없습니다.\n')
                break
            self._id = input("변경할 학번 : ")
            print()
            if self._id != '':  # 학번이 공백일 경우 예외처리
                if self._id not in stu_Info.keys(): # 유효성 검사
                    print('수정하려는 학번은 존재하지 않는 학번입니다.\n')
                else: # 학번이 딕셔너리의 키중에 있으면
                    self.new_id = input('변경된 학번 입력 : ')
                    print()
                    if self.new_id != '':
                        if self.new_id in stu_Info.keys():
                            print('변경하려는 학번이 이미 존재합니다\n')
                        else: # 문자열은 글자가 없으면 False, 있으면 True
                            stu_Info[self.new_id] = stu_Info[self._id] # 키를 _id 에서 self.new_id 로 변경
                            del stu_Info[self._id] # 변경하고 남은 _id 를 삭제
                            break
                    else:
                        print('변경할 학번란은 비워둘 수 없습니다.\n')
            else: # 학번이 공백이면
                print('학번란은 비워둘 수 없습니다.\n')

    def same_Info(self): # 4. 중복된 이름을 가진 학생의 정보 출력 ## 예외처리 완료
        while True:
            if stu_Info == {}:
                print('학생이 없습니다.\n')
                break
            self.name = input('같은 이름을 찾을 이름입력 : \n') # 같은 이름을 찾을 이름 name 에 받기
            print()
            count = 0   # switching 변수 0: 해당 이름이 존재하지 않음
            if self.name == '':
                print('이름란은 비워둘 수 없습니다.\n')
            else:
                for i in stu_Info:
                    if self.name in stu_Info[i][0]: # s를 키로 갖는 stu_Info의 값중 0 번째(이름)안에 name이 있으면
                        count += 1
                if count > 1:
                    for i in stu_Info:
                        if self.name == stu_Info[i][0]:
                            print('학번 : {}, 이름 : {}, 국어 : {}점, 영어 : {}점, 수학 : {}점, 총점 : {}, 평균 {:.2f}, 학점 : {}\n'.format(i, stu_Info[i][0], stu_Info[i][1], stu_Info[i][2], stu_Info[i][3], stu_Info[i][4], stu_Info[i][5], stu_Info[i][6]))
                    break
                else:
                    print('\n같은 이름을 가진 학생이 없습니다.\n')
                    break
        
    def all_Info(self): # 5. 전체 출력 # 완료
        if stu_Info == {}:
            print('학생이 없습니다.\n')
        else:
            sort_stu = sorted(stu_Info.items()) # sort_stu[s] = 키
            for s in range(len(sort_stu)): # sort_stu 리스트의 갯수만큼 반복
                print('학번 : {}, 이름 : {}, 국어 : {}점, 영어 : {}점, 수학 : {}점, 총점 : {}, 평균 : {:.2f} 학점 : {}\n'.format(sort_stu[s][0], sort_stu[s][1][0], sort_stu[s][1][1], sort_stu[s][1][2], sort_stu[s][1][3], sort_stu[s][1][4], sort_stu[s][1][5], sort_stu[s][1][6]))

    def menu(self):
        while True:
            self.kor = ''
            self.eng = ''
            self.math = ''
            print('====== 학생 관리 ======')
            print('1. 학생 등록')
            print('2. 학번 검색')
            print('3. 학번 수정')
            print('4. 같은 이름 학생 확인')
            print('5. 전체 출력')
            print('6. 프로그램 종료')
            print('=' * 23 + '\n')
            menu = input('번호 입력 : ')
            if menu == '1':
                print('\n====== 학생 등록 ======\n')
                s1.stu_Insert()
            elif menu == '2':
                print('\n====== 학번 검색 ======\n')
                s1.search_Id()
            elif menu == '3':
                print('\n====== 학번 수정 ======\n')
                s1.update_Id()
            elif menu == '4':
                print('\n== 같은이름 학생확인 ==\n')
                s1.same_Info()
            elif menu == '5':
                print('\n====== 전체 출력 ======\n')
                s1.all_Info()
            elif menu == '6':
                print('\n프로그램을 종료합니다.')
                break
            else:
                print('\n잘못된 번호를 입력하셨습니다.\n')
                
if __name__ == "__main__":
    s1 = Student()
    s1.menu()