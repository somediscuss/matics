
import math
try:
    import func1
except:
    print("$ ./install.sh")
    exit()

import ctypes as c 
so = c.CDLL("./step.so")

class Constant:
    
    
    """
    >>> j=Constant()
    >>> j.pi()
    3.14159265358979323846
    >>> j=Constant(num=5)
    >>> j.pi()
    3.14159
    >>> j.tau()
    
    """
     
    def __init__(self, num=20):
        self.num = num
        self.float_pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
        
    def pi(self):
        
        """返回pi的一定位数,精度可选"""
        
        return round(self.float_pi, self.num)
        
    def tau(self):
        
        """返回tau的一定位数,精度可选"""
        
        return round(self.float_pi * 2, self.num)
        
class Calculate:    

    """方便计算,所以开发"""
    
    def __init__(self,number):
        if isinstance(number,str):
            raise TypeError("Type must be int or float!")

        elif isinstance(number,float):
            number = int(number)
        
        self.number = number

    def __int__(self):
        return int(self.number)
    
    def __repr__(self):
        return f"Calculate({self.number})"

    def __str__(self):
        return f"{self.number}"

    def __eq__(self,other):
        return self.number == other.number 

    def __ne__(self,other):
        return self.number != other.number 

    def __lt__(self,other):
        return self.number < other.number 

    def __gt__(self,other):
        return self.number > other.number 

    def __add__(self,other):
        return self.number + other.number 

    def __sub__(self,other):
        return self.number - other.number 

    def __mul__(self,other):
        return self.number * other.number 

    def __div__(self,other):
        return self.number / other.number 
    
    def __mod__(self,other):
        return self.number % other.number 

    def __iadd__(self,other):
        self.number += other.number 
        return self.number
    
    def factor(self):
        
        """用列表推导式找因数"""
        
        return factor.factor(self.number)
        
    def primer_number(self):
        
        """找一定范围的素数"""
        
        return [i for i in primer(self.number)]

    def composite_number(self):
        
        """找一定范围的合数"""
        
        return [i for i in func1.composite(self.number)]

    def acfactor(self,number2):

        # all common factor 

        if isinstance(number2,Calculate):
            number2 = number2.number
        result = math.gcd(int(self.number),int(number2))
        return func1.factor(result)

    def step_add(self):
        if isinstance(self.number,int):                                                     
            print('Type must be int ')                                            
            exit()                                                             
        result = self.number + (self.number + 1) // 2 if self.number > 65535 else so.step_add(self.number)             
        return result

    def primef(self):
        # Prime factorization
        return func1.pf(self.number)

    def least_cm(self,num):
        # least common multiple
        return (self.number * num)  // math.gcd(self.number,num)

class Equation:
    """开发中的解方程类"""

    def __init__(self,x):
        self.x = x
        
    def solution(self, string, number):
        self.string = string
        self.number = number

        for i in range(self.number+1):
            string =  self.string.replace(self.x,str(i))
            if int(eval(string)) == self.number:
                return i

            string.replace(str(i),self.x)
