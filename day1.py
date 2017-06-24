""" 1 """

# answer = 0

# for i in range(1, 1000):
# 	if i % 3 == 0 or i % 5 == 0:
# 		answer += i

# print(answer)



""" 2 """

# a, b = 1, 2
# answer = 0
# limit = 4000000

# while a < limit and b < limit:
# 	if a < limit and a % 2 == 0: 
# 		answer += a
# 	if b < limit and b % 2 == 0: 
# 		answer += b
# 	print(a, b)
# 	a += b
# 	b += a 

# print("\n", answer)


""" 3 """

# biggestFactor = tar = 600851475143

# def isPrime(num):
# 	if num % 2 == 0:
# 		return False
# 	for i in range(3, int(num**0.5)+1, 2):
# 		if num % i == 0:
# 			return False	
# 	return True


# for i in range(1, int(tar**0.5)+1):
# 	if tar % i == 0: 
# 		if isPrime(i):
# 			biggestFactor = i

# print(biggestFactor) 

""" 4 """

# answer = 0

# for bigCircle in range(100, 1000):
# 	for smallCircle in range(100, 1000):
# 		n = bigCircle*smallCircle
# 		if len(str(n)) % 2 == 0:
# 			half = len(str(n)) / 2
# 			if str(n)[:half] == str(n)[:half-1:-1]:
# 				answer = n if answer < n else answer
# 		else:
# 			half = (len(str(n))-1) / 2
# 			if str(n)[:half] == str(n)[half-1:-1]:
# 				answer = n if answer < n else answer

# print(answer)


""" 5 """

# def nok(a, b):
# 	def nod(a, b):
# 		while a != 0 and b != 0:
# 		    if a > b: a = a % b
# 		    else: b = b % a
# 		return(a + b)
# 	return (a * b) / nod(a, b)

# result = nok(1, 2)

# for i in range(2, 21):
# 	result = nok(result, i)
# 	print(result)


""" 6 """

# sumOfSquares = squaredSum = 0

# for i in range(1, 101):
# 	sumOfSquares += i ** 2
# 	squaredSum += i

# print(squaredSum**2 - sumOfSquares)


""" 7 """

# primes = []
# x = 1

# def isPrime(num):
# 	if num % 2 == 0:
# 		return False
# 	for i in range(3, int(num**0.5)+1, 2):
# 		if num % i == 0:
# 			return False	
# 	return True		

# while len(primes) != 10001:
# 	if isPrime(x):
# 		primes.append(x)
# 	x += 1

# print(primes)


""" 8 """

# num =  "73167176531330624919225119674426574742355349194934\
# 96983520312774506326239578318016984801869478851843\
# 85861560789112949495459501737958331952853208805511\
# 12540698747158523863050715693290963295227443043557\
# 66896648950445244523161731856403098711121722383113\
# 62229893423380308135336276614282806444486645238749\
# 30358907296290491560440772390713810515859307960866\
# 70172427121883998797908792274921901699720888093776\
# 65727333001053367881220235421809751254540594752243\
# 52584907711670556013604839586446706324415722155397\
# 53697817977846174064955149290862569321978468622482\
# 83972241375657056057490261407972968652414535100474\
# 82166370484403199890008895243450658541227588666881\
# 16427171479924442928230863465674813919123162824586\
# 17866458359124566529476545682848912883142607690042\
# 24219022671055626321111109370544217506941658960408\
# 07198403850962455444362981230987879927244284909188\
# 84580156166097919133875499200524063689912560717606\
# 05886116467109405077541002256983155200055935729725\
# 71636269561882670428252483600823257530420752963450"

# result = 1
# lastResult = result
# maximum = result

# for i in range(1, 988):
# 	for j in range(i, i+13):
# 		result *= int(num[j])
# 		if result > maximum:
# 			maximum = result
# 	lastResult = result
# 	result = 1

# print("\n" + str(maximum))


""" 9 """

# for c in range(2, 1000):
# 	for b in range(1, c):
# 		for a in range(0, b):
# 			if ((a ** 2 + b ** 2) == c ** 2) and (a + b + c) == 1000:
# 				print(a * b * c)
# 				exit()	


""" 10 """

# primes = []

# def isPrime(num):
# 	if num % 2 == 0 and num != 2:
# 		return False
# 	for i in range(3, int(num**0.5)+1, 2):
# 		if num % i == 0:
# 			return False	
# 	return True	

# for num in range(2, 2000000):
# 	result = isPrime(num)
# 	if result: primes.append(num)

# print(sum(primes))