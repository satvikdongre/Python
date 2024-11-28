#lab 8 Count no. of lowercase words in file
count = 0
f = open("Demo.txt", "r")
for line in f:
	word = line.split(" ")
	b=" "
	for x in word:
		if x.islower():
			b+=x
			count += 1

print("Total Number of Words: " + str(count))
f.close()
