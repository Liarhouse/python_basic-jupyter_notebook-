stuDic = dict()


class Students:

    def __init__(self, pin, name, pw, score, avg):
        self.pin = pin
        self.name = name
        self.pw = pw
        self.score = score
        self.avg = avg

    def update(self, name, pw):  # 관리자용
        self.name = name
        self.pw = pw

    def getPin(self):
        return self.pin

    def getName(self):
        return self.name

    def getPw(self):
        return self.pw

    def getScore(self):
        return self.score

    def compute(self):
        tot = 0
        for i in range(len(self.score)):
            tot += self.score[i]
        if tot != 0:
            self.avg = round(tot / len(self.score), 2)

    def show(self):
        return "%s %s %s %.2f" % (self.pin, self.name, self.score, self.avg)

#     def change(self, pw): #학생용
#         self.pw = pw
#         stuDic[self] = (self.name, self.pw)

class StuMan(Students):
    def __init__(self):
        self.stuList = []

    def oneName(self):  # 관리자용
        handle = self
        if len(self.stuList) != 0:
            name = input("이름 = ")
            check = 0
            for alp in self.stuList:
                if name == alp.getName():
                    alp.compute()
                    print(alp.show())
                    check = 1
            if check == 0:
                print("해당 이름의 학생은 시스템에 등록되어 있지 않습니다.")
            while True:
                print("=" * 20)
                print("[1] 다른 이름 조회")
                print("[2] 조회 메뉴로 돌아가기")
                print("[3] 메인 메뉴로 돌아가기")
                print("[4] 로그아웃")
                print("[5] 프로그램 종료")
                menu = input("메뉴 = ")
                if menu == "1":
                    print("다른 이름을 조회합니다.")
                    self.oneName()
                elif menu == "2":
                    searchStu(handle)
                elif menu == "3":
                    teacherMenu(handle)
                elif menu == "4":
                    print("로그아웃 됐습니다.")
                    mainMenu()
                elif menu == "5":
                    escape()
                #                     print("프로그램을 종료합니다.")
                #                     exit("프로그램이 정상적으로 종료됐습니다.")
                else:
                    print("잘못된 접근입니다")
        else:
            print("시스템에 등록된 학생이 없습니다.")
            searchStu(handle)

    def allStudents(self):  # 관리자용
        handle = self
        if len(self.stuList) != 0:
            for alp in self.stuList:
                alp.compute()
                print(alp.show())
            print("전체 학생정보 조회가 완료됐습니다.")
            searchStu(handle)
        else:
            print("시스템에 등록된 학생이 없습니다.")
            teacherMenu(handle)

    def addStudent(self):  # 관리자용
        handle = self
        pin = ('s' + str(len(self.stuList) + 1))
        #        for i in stuDic.keys():
        #             if pin == i:
        name = input("이름 = ")
        pw = name
        stuDic[pin] = (name, pw)
        pin = Students(pin, name, pw, [], 0)  # (학번, 학생이름, 비밀번호, 성적리스트, 평균)
        self.stuList.append(pin)
        print("학생 등록이 완료됐습니다.")
        searchStu(handle)

    #         pin = input("학번 = ")
    #         if pin in stuDic.keys():
    #             print("이미 존재하는 학번입니다.")
    #             searchStu()
    #         else:
    #             name = input("이름 = ")
    #             pw = name
    #             stuDic[pin] = (name, pw)
    #             stu = Students(pin, name, pw, [], 0) #(학번, 학생이름, 비밀번호, 성적리스트, 평균)
    #             self.stuList.append(stu)
    #             print("학생 등록이 완료됐습니다.")
    #             searchStu()

    def showMyAvg(self, pin):
        for stu in self.stuList:
            if pin == stu.pin:
                stu.compute()
                print("=" * 20)
                print("%s님은 총 %d회 퀴즈를 풀었고, 평균은 %.2f입니다." % (
                    stu.name, len(stu.score), stu.avg))
                self.myScoreMenu(pin, stu)

    def myScoreMenu(self, pin, stu):
        handle = self
        print("\n1. 전체 회차별 점수 조회")
        print("2. 특정 회차 점수 조회")
        print("3. 메인 메뉴로 나가기")
        print("4. 로그아웃")
        print("5. 프로그램 종료")
        print("=" * 20)
        menu = input("메뉴 = ")
        if menu == "1":
            self.showMyAllScore(pin, stu)
        elif menu == "2":
            self.showMyScore(pin, stu)
        elif menu == "3":
            studentMenu(pin, handle)
        elif menu == "4":
            print("로그아웃 됐습니다.")
            mainMenu()
        elif menu == "5":
            escape()
        #             print("프로그램을 종료합니다.")
        #             exit("프로그램이 정상적으로 종료됐습니다.")
        else:
            print("잘못된 접근입니다.")

    def showMyAllScore(self, pin, stu):
        for i, r in enumerate(stu.score):
            print("%s님의 %d회차 점수는 %d입니다." % (stu.name, (i + 1), r))
        self.afterAllScore(pin, stu)

    def afterAllScore(self, pin, stu):
        handle = self
        print("=" * 20)
        print("1. 조회 메뉴로 나가기")
        print("2. 메인 메뉴로 나가기")
        print("3. 로그아웃")
        print("4. 프로그램 종료")
        menu = input("메뉴 = ")
        if menu == '1':
            self.myScoreMenu(pin, stu)
        elif menu == '2':
            studentMenu(pin, handle)
        elif menu == '3':
            print("로그아웃 됐습니다.")
            mainMenu()
        elif menu == '4':
            escape()
        #             print("프로그램을 종료합니다.")
        #             exit("프로그램이 정상적으로 종료됐습니다.")
        else:
            print("잘못된 접근입니다.")
            self.afterAllScore(pin, stu)

    def showMyScore(self, pin, stu):
        try:
            no = int(input("조회하고 싶은 회차를 입력해주세요. = "))
        except:
            print("숫자를 입력해주세요.")
            self.showMyScore(pin, stu)
        else:
            if no > len(stu.score):
                print("아직 %d회차까지만 퀴즈를 풀었습니다." % len(stu.score))
                self.showMyScore(pin, stu)
            else:
                print("=" * 20)
                print("%s님의 %d회차 점수는 %d입니다." % (
                    stu.name, no, stu.score[no - 1]))
                self.afterMyScore(pin, stu)

    def afterMyScore(self, pin, stu):
        handle = self
        print("=" * 20)
        print("1. 다른 회차 조회하기")
        print("2. 메인 메뉴로 나가기")
        print("3. 로그아웃")
        print("4. 프로그램 종료")
        menu = input("menu = ")
        if menu == '1':
            self.showMyScore(pin, stu)
        elif menu == '2':
            studentMenu(pin, handle)
        elif menu == '3':
            print("로그아웃 됐습니다.")
            mainMenu()
        elif menu == '4':
            escape()
        #             print("프로그램을 종료합니다.")
        #             exit("프로그램이 정상적으로 종료됐습니다.")
        else:
            print("잘못된 접근입니다.")
            self.afterMyScore(pin, stu)

    def cal(self, pin, count):
        for stu in self.stuList:
            if pin == stu.pin:
                stu.score.append(count)

    def change(self, pin):  # 학생용
        handle = self
        for alp in handle.stuList:
            if pin == alp.pin:
                pw = input("변경할 비밀번호를 입력하세요 = ")
                alp.pw = pw
                stuDic[pin] = (alp.name, alp.pw)
                print("비밀번호 변경이 완료됐습니다.")
                studentMenu(pin, handle)

    def onePin(self):  # 관리자용
        handle = self
        if len(self.stuList) != 0:
            print()
            pin = input("학번 = ")
            check = 0
            for alp in self.stuList:
                if pin == alp.getPin():
                    alp.compute()
                    print(alp.show())
                    check = 1
                    while True:
                        print("=" * 20)
                        print("[1] 다른 학번 조회")
                        print("[2] 조회 메뉴로 돌아가기")
                        print("[3] 메인 메뉴로 돌아가기")
                        print("[4] 로그아웃")
                        print("[5] 프로그램 종료")
                        menu = input("메뉴 = ")
                        if menu == "1":
                            print("다른 학번을 조회합니다.")
                            self.onePin()
                        elif menu == "2":
                            searchStu(handle)
                        elif menu == "3":
                            teacherMenu(handle)
                        elif menu == "4":
                            print("로그아웃 됐습니다.")
                            mainMenu()
                        elif menu == "5":
                            escape()
                        #                             print("프로그램을 종료합니다.")
                        #                             exit("프로그램이 정상적으로 종료됐습니다.")
                        else:
                            print("잘못된 접근입니다.")
            if check == 0:
                print("해당 학번의 학생은 시스템에 등록되어 있지 않습니다.")
                searchStu(handle)
        else:
            print("시스템에 등록된 학생이 없습니다.")
            searchStu(handle)


# 퀴즈 풀기

def quiz(pin, handle):  # pin은 점수 기입을 위해 활용, handle은 핸들러용
    import random
    import time  # 모듈 호출

    count = 0
    start_time = time.time()  # 시작 시간 저장
    quz = {}
    quz_finish = []  # 메인 변수 저장

    with open("sensequs.txt", "r") as f:
        for line in f:
            data = line.split(":")
            sensequz, senseans = data[0], data[1]
            sensequz = sensequz.strip()
            senseans = senseans.strip()
            quz[sensequz] = senseans  # 텍스트 파일 추출하여 변수에 저장

    while len(quz_finish) != 5:  # 문제 5개까지 출력
        keys = list(quz.keys())
        index = random.randint(0, len(keys) - 1)
        if index in quz_finish: continue  # 중복된 문제 출력 안되게 하는 제어문
        quz_finish.append(index)
        sensequz = keys[index]
        senseans = quz[sensequz]

        guess = input("{} = ".format(sensequz)).strip()  # 난수, 인덱스, 딕셔너리 활용하여 랜덤으로 문제 추출

        if guess == senseans:  # 입력된 값과 문제 정답 확인
            print("정답")
            count += 1
        else:
            print("오답")

    handle.cal(pin, count)  # 클래스 메서드 활용하여 점수 기입

    end_time = time.time()  # 끝나는 시간 기록
    print("퀴즈가 끝났습니다.")
    print("당신의 점수는 {0}점만점에 {1}점입니다.".format(len(quz_finish), count))  # 점수 출력
    print("총 소요시간: {0:.1f} 초".format(end_time - start_time))  # 소요 시간 출력
    quizMenu(pin, handle)


def quizMenu(pin, handle):  # 퀴즈 푼 후
    import time
    print("*" * 20)
    print("1. 문제 다시 풀기")
    print("2. 메인 메뉴로 돌아가기")
    print("3. 로그아웃")
    print("4. 프로그램 종료")
    menu = input("메뉴 = ")
    if menu == "1":
        print("재도전 합니다.")
        print("3초 후 문제가 출력됩니다.")
        time.sleep(3)
        quiz(pin, handle)
    elif menu == "2":
        studentMenu(pin, handle)
    elif menu == "3":
        print("로그아웃 됐습니다.")
        mainMenu()
    elif menu == "4":
        escape()
    #         print("프로그램을 종료합니다.")
    #         exit("프로그램이 정상적으로 종료됐습니다.")
    else:
        print("잘못된 접근입니다.")
        quizMenu(pin, handle)


# 문제 추가

def addQuiz(handle):
    f = open("sensequs.txt", "a")
    print("종료를 입력하면 문제 추가를 취소합니다")
    q = input("문제 기입 = ")
    if q == "종료":
        f.close()
        teacherMenu(handle)
    else:
        print("종료를 입력하면 문제 추가를 취소합니다")
        a = input("정답 기입 = ")
        if a == "종료":
            f.close()
            teacherMenu(handle)
        else:
            f.write(f"{q} : {a}\n")
            print("문제 추가가 완료됐습니다.")
            f.close()
            teacherMenu(handle)


# 문제 수정

def updateQuiz(handle):
    foo = open('sensequs.txt', 'r+')  # 텍스트 파일 열람용 함수 설정
    data = foo.readlines()  # 텍스트 내용 리스트로 저장
    try:
        pos = int(input("수정할 문제 번호를 입력해주세요. = ")) - 1  # 파이썬에서는 0부터 데이터 처리하기에 -1 처리
    except:
        print("문제 번호를 정확히 입력해주세요.")  # 만약 숫자를 입력하지 않았을 시 예외 처리
        foo.close()
        updateQuiz(handle)
    else:
        if pos > len(data):  # 만약 입력한 숫자에 해당하는 문제가 없을 경우를 대비한 제어문
            print("해당 문제 번호가 존재하지 않습니다.")
            foo.close()
            updateQuiz(handle)
        else:
            print("종료를 입력하면 문제 수정을 취소합니다")
            que = input("문제를 입력해주세요. = ")  # 문제 입력
            que = que.strip()
            if que == "종료":
                foo.close()
                teacherMenu(handle)
            else:
                print("종료를 입력하면 문제 수정을 취소합니다")  # 정답 입력
                ans = input("정답을 입력해주세요. = ")
                ans = ans.strip()
                if ans == "종료":
                    foo.close()
                    teacherMenu(handle)
                else:
                    data.insert(pos, que + ":" + ans + "\n")  # 리스트에 입력된 값 insert 함수 활용하여 원하는 줄에 삽입
                    x = data[pos + 1]
                    data.remove(x)  # remove 함수 활용하여 원하는 줄 삭제
                    foo.truncate(0)  # text파일 초기화
                    foo.seek(0)  # 커서 0으로 옮기기
                    for i in data:
                        foo.write(str(i))  # write 함수로 텍스트 파일에 기입
                    print("문제 수정이 완료됐습니다.")
                    foo.close()
                    teacherMenu(handle)


# 문제 삭제

def removeQuiz(handle):
    foo = open('sensequs.txt', 'r+')
    data = foo.readlines()  # reads file as list
    count = len(data)
    print("종료를 입력하면 문제 삭제를 취소합니다")
    poss = input("삭제할 문제 번호를 입력해주세요. = ")  # list position to edit
    if poss == "종료":
        foo.close()
        teacherMenu(handle)
    else:
        try:
            pos = int(poss) - 1
        except:
            print("문제 번호를 정확히 입력해주세요.")
            foo.close()
            removeQuiz(handle)
        else:
            if pos > len(data):
                print("해당 문제 번호가 존재하지 않습니다.")
                foo.close()
                removeQuiz(handle)
            else:
                x = data[pos]
                data.remove(x)  # removes item to edit
                foo.truncate(0)
                foo.seek(0)
                for i in data:  # strips "\n" from list items
                    i.strip()
                    foo.write(i)
                print("문제 삭제가 완료됐습니다.")
                foo.close()
                teacherMenu(handle)


# 문제 조회(확인)
def showQuiz(handle):
    f = open("sensequs.txt", "r")
    a = f.readlines()
    for i in a:
        print(i, end="")
    print("메인메뉴로 돌아가시겠습니까?")
    menu = input("y or n = ")
    if menu == 'y':
        f.close()
        teacherMenu(handle)
    elif menu == 'n':
        f.close()
        showQuiz(handle)
    else:
        f.close()
        print("y나 n을 입력해주세요.")
        showQuiz(handle)


def mainMenu():
    print("=" * 20)
    print("====상식 퀴즈 월드====")
    print("====로그인  하세요====")
    print("입력창에 exit를 입력하면 종료됩니다.")
    pin = input("아이디를 입력해주세요 = ")
    if pin == "123teacher":
        teacherLogin(handle)

    elif pin in stuDic.keys():
        pw = input("비밀번호 = ")
        if pw == stuDic[pin][1]:
            print("로그인 됐습니다.")
            studentMenu(pin, handle)
        else:
            print("잘못된 비밀번호 입니다.")
            mainMenu()
    elif pin == "exit":
        escape()
    #         print("프로그램을 종료합니다.")
    #         exit("프로그램이 정상적으로 종료됐습니다.")
    elif pin not in stuDic.keys():
        print("\n존재하지 않는 pin입니다.")
        mainMenu()


#     def make_account(self): # 길이 2이상, 숫자와 영문자로만 구성.
#         make_pin = input("생성할 아이디를 입력하세요.")


# def studentLogin():
#     pw = input("비밀번호 = ")
#     if pw == stuDic[all_pin][1]:
#         print("로그인 됐습니다.")
#         studentMenu()
#     else:
#         print("잘못된 비밀번호 입니다.")
#         studentLogin()

def studentMenu(pin, handle):
    print("\n\n\n\n\n안녕하세요, %s님. 상식 퀴즈 월드에 오신 걸 환영합니다." % stuDic[pin][0])
    print("=" * 20)
    print("======퀴즈 메뉴======")
    print("1. 문제 풀기")
    print("2. 성적 조회")
    print("3. 비밀번호 변경")
    print("4. 로그아웃")
    print("5. 프로그램 종료")
    menu = input("메뉴 = ")
    if menu == "1":
        quiz(pin, handle)  ### 문제 풀기 프로그램으로 들어가기
    elif menu == "2":
        handle.showMyAvg(pin)
    elif menu == "3":
        handle.change(pin)
    elif menu == "4":
        print("로그아웃 됐습니다.")
        mainMenu()
    elif menu == "5":
        escape()
    else:
        print("잘못된 접근입니다.")
        studentMenu(pin, handle)


def teacherLogin(handle):
    teacher_pw = input("비밀번호 = ")
    if teacher_pw == "123@tt":
        print("로그인 됐습니다.")
        teacherMenu(handle)

    else:
        print("비밀번호가 틀렸습니다.")
        teacherLogin(handle)


def teacherMenu(handle):
    print("=" * 20)
    print("=====관리자  메뉴=====")
    print("[1] 문제 추가")
    print("[2] 문제 삭제")
    print("[3] 문제 조회")
    print("[4] 문제 수정")
    print("[5] 학생 관리")
    print("[6] 로그아웃")
    print("[7] 프로그램 종료")
    menu = input("메뉴 = ")
    if menu == "1":
        addQuiz(handle)
    elif menu == "2":
        removeQuiz(handle)
    elif menu == "3":
        showQuiz(handle)
    elif menu == "4":
        updateQuiz(handle)
    elif menu == "5":
        searchStu(handle)
    elif menu == "6":
        print("로그아웃 됐습니다.")
        mainMenu()
    elif menu == "7":
        escape()
    #         print("프로그램을 종료합니다.")
    #         exit("프로그램이 정상적으로 종료됐습니다.")
    else:
        print("잘못된 접근입니다.")
        teacherMenu(handle)


def searchStu(handle):
    print("=" * 20)
    print("=====학생 관리=====")
    print("[1] 이름으로 조회")
    print("[2] 학번으로 조회")
    print("[3] 전체 조회")
    print("[4] 학생 추가")
    print("[5] 메인 메뉴로")
    print("[6] 로그아웃")
    print("[7] 프로그램 종료")
    print("[*] 기본값 부여")
    menu = input("메뉴 = ")
    if menu == "1":
        handle.oneName()
    elif menu == "2":
        handle.onePin()
    elif menu == "3":
        handle.allStudents()
    elif menu == "4":
        handle.addStudent()
    elif menu == "5":
        teacherMenu(handle)
    elif menu == "6":
        print("로그아웃 됐습니다.")
        mainMenu()
    elif menu == "7":
        escape()
    #         print("프로그램을 종료합니다.")
    #         exit("프로그램이 정상적으로 종료됐습니다.")
    elif menu == "*":
        default(handle)
        print("기본값을 부여했습니다.")
        searchStu(handle)
    else:
        print("잘못된 접근입니다.")
        teacherMenu(handle)


def default(handle):
    first = Students("s1", "강보원", "강보원", [4, 5, 4], 4.33)
    second = Students("s2", "박희현", "park002", [4, 5, 4], 4.33)
    third = Students("s3", "정동환", "qwertypython", [3, 4], 3.50)
    stuDic[first.pin] = (first.name, first.pw)
    stuDic[second.pin] = (second.name, second.pw)
    stuDic[third.pin] = (third.name, third.pw)
    handle.stuList.append(first)
    handle.stuList.append(second)
    handle.stuList.append(third)


def escape():
    from sys import exit
    try:
        exit(0)
    except:
        print("프로그램을 종료합니다.")

