#!/usr/bin/python3.2
import re

"""Very simply compare the given string to a second given string."""

#test_string = input("Please input a test string to compare: ")
#file = open('temp.pym', 'w')
#file.write(test_string)
#file.close()
file = open('temp.pym', 'r')

file_string = file.read()
print(file_string)
# Matches every word and leading/trailing punctuation
#test_string = re.findall('[\w!?",\'.\(\)]+', file_string)

# Matches every word and every relavant punctuation mark
test_string = re.findall('\w+|[!?",\'.\(\)]', file_string)

print(test_string)
compare_string = input("Please input string for comparison: ")
compare_string = re.findall('\w+|[!?",\'.\(\)]', compare_string)
print(compare_string)
for i in range(0,len(test_string)):
	if re.match(re.compile(compare_string[i]), test_string[i]):
		print('1')
else:
	print('0')


#print(x)
file.close()
	
