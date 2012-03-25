#!/usr/bin/python3.2
import re

"""Very simply compare the given string to a second given string."""

#test_string = input("Please input a test string to compare: ")
#file = open('temp.pym', 'w')
#file.write(test_string)
#file.close()
file = open('temp.pym', 'r')

#file_string = file.read()
test_string = file.read()
#print(file_string)
print(test_string)

# Matches every word and leading/trailing punctuation
#test_string = re.findall('[\w!?",\'.\(\)]+', file_string)

# Matches every word and every relavant punctuation mark
#test_string = re.findall('\w+|[!?",\'.\(\)]', file_string)

# Matches only words.
#test_string = re.findall('\w+', file_string)
#print(test_string)

# New plan: catalog phrases, not words. Let's match phrases
#test_string = re.findall('(?<=[,.;:\(\)^]).*?(?=[,\.;:\(\)$])', test_string)
test_string = re.findall('([\w\s\'-]+)[\W\s\'-]+', test_string)
#test_string = re.findall('^.*;', test_string)
print(test_string)

###########################################################################################################
#after this, it should be used ater like
###########################################################################################################
#compare_string = input("Please input string for comparison: ")
file_compare = open('temp_compare', 'r')
compare_string = file_compare.read()

# This comparison includes punctuation, I'll handle that separately.
#compare_string = re.findall('\w+|[!?",\'.\(\)]', compare_string)

# Setting up the 'true' counters.
# These should match the i in the for loop for a perfect run.
i_test_string = 0
i_compare_string = 0



compare_string = re.findall('([\w\s\'-]+)[\W\s\'-]+', compare_string)
print(compare_string)

# Reference string, to say which words are right about each string.
test_string_watchman = [0] * len(test_string)
compare_string_watchman = [0] * len(compare_string)

"""
# Loop over the max_length
# a break should catch it if it starts to go over either len().
if len(test_string) > len(compare_string):
	max_length = len(test_string)
else:
	max_length = len(compare_string)
"""
max_length = len(test_string)-2
# main loop
for i in range(0,max_length):
	if re.match(re.compile(compare_string[i_compare_string]), test_string[i_test_string]):

		# Mark the word as correct in both strings.
		test_string_watchman[i_test_string] = 1
		compare_string_watchman[i_compare_string] = 1
		
		# prepare the number for the next iteration.
		i_compare_string = i_compare_string + 1

	else:
		# assume that if we ignore the watchmen, they'll still 0.
		# Loop over the rest, check if it's valid.

		# true counters for the else
		j_test_string = i_test_string
		j_compare_string = i_compare_string

		# pin the start
		j_start = i
		
		# This range is the maximum range we could need.
		for j in range(j_start,max_length):

			a = b = c = 0

			# DEBUG
			print()
			print('in the loop...')
			print('i_test_string:', i_test_string)
			print('i_compare_string:', i_compare_string)
			print('j_test_string:',j_test_string)
			print('j_compare_string:', j_compare_string)
			print('Try to match', compare_string[j_compare_string], 'and', test_string[j_test_string])
			print('Try to match', compare_string[j_compare_string+1], 'and', test_string[j_test_string+1])
			print('Try to match', compare_string[j_compare_string+2], 'and', test_string[j_test_string+2])
			#print(re.match(re.compile(compare_string[j_compare_string]), test_string[j_test_string]))
			#print(re.match(re.compile(compare_string[j_compare_string+1]), test_string[j_test_string+1]))
			#print(re.match(re.compile(compare_string[j_compare_string+2]), test_string[j_test_string+2]))
			print()

			# To improve readability, I'll put these here instead of in the if.
			a = bool(re.match(re.compile(compare_string[j_compare_string]), test_string[j_test_string]))
			b = bool(re.match(re.compile(compare_string[j_compare_string+1]), test_string[j_test_string+1]))
			c = bool(re.match(re.compile(compare_string[j_compare_string+2]), test_string[j_test_string+2]))
			print('The result of comparisons...', a, b, c)

			if a and b and c:
				print('There is a match!')
				
				# Still not working...something about the string going too far. Need to trace all the iteration ints.
				test_string_watchman[j_test_string] = 1
				compare_string_watchman[j_compare_string] = 1
				break
			else:
				#j_test_string = j_test_string + 1 # of course I don't want to loop this.
				j_compare_string = j_compare_string + 1

				# Check it's not going to collide and overreach the end of the string
				test_variable = j_compare_string + 2
				if test_variable == len(compare_string)-1:
					print('DONT\' PANIC')

	# Try the next word for a match
	i_test_string = i_test_string + 1

	print('-'*10,'Successful iteration','-'*10)
	print('test_string_watchman:', test_string_watchman)
	print('compare_string_watchman:', compare_string_watchman)

print('i_test_string =', i_test_string)
print('i_compare_string =', i_compare_string)
print('test_string_watchman =', test_string_watchman) 
print('compare_string_watchman =', compare_string_watchman) 
file.close()
file_compare.close()
	
