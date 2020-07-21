def composite(s):
	list_a = []
	for i in range(2, s + 1):
		for j in range(2, i):
			if i % j == 0 :
				list_a.append(i)
				break
	return list_a
def primer(se):
	primes = [2, 3, 5, 7]
	r = primes[:]
	for a in range(8, int(se) + 1):
		if any(a % k == 0 for k in primes):
			continue
		r.append(a)
	return r
try:
    from functools import reduce
    from ctypes import CDLL
    so = CDLL("./step.so")
    #程序员:苏晨果
    #1.1.2版
    #来源:未知
    def stepadd(m):
        if type(m) != int:
            print('类型必须为整数')
            exit()
        result = m + (m + 1) // 2 if m > 65535 else so.step_add(m)
        return result

except:
    print("Please look at README.md!")
    exit()

def factor(m):

	return [i for i in range(1, m + 1) if not m % i]

def pf(number):

	i = (i for i in range(number) if len(factor(i)) == 2)
	u = []
	
	for num in i:
		while number % num == 0:
			number /= num
			u.append(num)
			
	return u
