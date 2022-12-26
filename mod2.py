# mod2.py

def sum(a, b):
    return a + b

def safe_sum(a, b):
    # type이 다를 경우 발생하는 문제를 처리하고 싶을 때
    if type(a) != type(b):
        print("자료형이 일치하지 않습니다.")
        return # 제어권을 넘겨준다
    else:
        result = sum(a, b)
    
    return result