import math

word = input("What word would you like to check: ")

isPalindrome = 0

mid = (math.floor(len(word)/2))

for i in range(0, mid):
	if (word[i] != word[(len(word) - 1 - i)]):
		isPalindrome = 1

if isPalindrome == 1:
	print("This is not a palindrome")
else:
	print("This is a palindrome!")
