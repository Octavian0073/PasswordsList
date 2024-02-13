import io
import sys

def readList(filename="psswd.txt"):
	try:
		with open(filename, "r") as file: 
			words = file.read().splitlines()
		return words
	except FileNotFoundError:
		return []

def writeToList(words, filename="psswd.txt"):
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
	new_words = []
	for word in words:
		new_words.append(word)
		new_words.append(word.title())
		i = 1
		while i < 6:
			nums = numberSeq(i)
			for num in nums:
				new_words.append(word+num)
				new_words.append(word.title()+num)
			i += 1
	writeToList(new_words)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python3 psswdList.py <name1> [name2 name3...]")
	else:
		wordsList = sys.argv[1:]
		wordList(*wordsList)
