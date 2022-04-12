# b_test 함수 정의
def b_test(eggs):
    eggs.append(1)
    eggs = [2,3]
    print("1.",eggs)
    
ham = [0,1] 
b_test(ham)
print("2.",ham)