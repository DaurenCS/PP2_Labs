import random
x = random.randrange(0, 20, 1)


n = input('Hello! What is your name?\n')
print(f'Well, {n}, I am thinking of a number between 1 and 20.')
cont = 0
while True:
	a = int(input('Take a guess.\n'))
	if x == a :
		cont += 1
		print(f'Good job,{n} You guessed my number in {cont} guesses!')
		break
	elif x > a:
		cont += 1
		print('Your guess is too low.')
	elif x < a:
		cont += 1
		print('Your guess is too big.')


	