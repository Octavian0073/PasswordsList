import io
import sys

def readList(filename="nums8.txt"):
	try:
		with open(filename, "r") as file: 
			words = file.read().splitlines()
		return words
	except FileNotFoundError:
		return []

def writeToList(words, filename="nums8.txt"):
	with open(filename, "w") as file:
		for word in words:
			file.write(word + "\n") 

def numberSeq(num):
	nums = []
	max_num = 0
	max_num_str = str(max_num)
	i = 0
	while len(max_num_str) != num:
		max_num += (10**i) * 9
		max_num_str = str(max_num)
		i += 1
	for j in range(max_num + 1):
		num_str = str(j)
		while len(num_str) != num:
			num_str = "0" + num_str
		nums.append(num_str)
	return nums

def wordList(*words):
	new_comb = readList()
	for i in range(9):
		for j in range(1, 10):
			num_str1 = str(i)
			num_str2 = str(j)
			num =  num_str1 + num_str2
			while len(num) != 8:
				num = num_str1 + num_str2 + num
			new_comb.append(num)
			while len(num) != 10:
                                num = num_str1 + num_str2 + num
			new_comb.append(num)
	writeToList(new_comb)

if __name__ == "__main__":
	wordsList = sys.argv[1:]
	wordList(*wordsList)

