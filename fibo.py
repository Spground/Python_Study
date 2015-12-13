#Fibonacci numbers module
if __name__ == "__main__":
        print("fibo module自身在运行")
else:
        print("fibo module在另一模块中运行")
        
def fib(n):#write Fibonacci series up to n
        a, b = 0, 1;
        while  b < n:
                print(b, end=" ");
                a, b = b, a+b;
        print();
        return;

def fib2(n):#return Fibonacci series up to n
        result = [];
        a, b = 0, 1;
        while b < n:
                result.append(b);
                a, b = b, a+b;
        return result;

