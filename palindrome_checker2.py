word1 = input("What word would you like to check? ")

def reverse(x):
	return x[::-1]

if (reverse(word1) == word1):
	print("This is a palindrome!")
else:
	print("This is not a palindrome.")
