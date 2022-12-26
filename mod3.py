# mod3.py

PI = 3.141592

class Math:

    def solv(self, r):
        return (r ** 2) * PI
    
    def sum(a, b):
        return a + b
    
print("Math 모듈이 로딩되었습니다.")

if __name__ == "__main__":
    print(PI)
    ap = Math()
    print(ap.solv(2))
    print(sum(PI, 4.4))