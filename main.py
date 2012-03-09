#!/usr/bin/python3.2
import re

"""Very simply compare the given string to a second given string."""

test_string = input("Please input a test string to compare: ")
file = open('temp.pym', 'w')
file.write(test_string)
file.close()
file = open('temp.pym', 'r')

file_string = file.read()
print(file_string)
# Matches every word and leading/trailing punctuation
#test_string = re.findall('[\w!?",\'.\(\)]+', file_string)

# Matches every word and every relavant punctuation mark
#test_string = re.findall('\w+|[!?",\'.\(\)]', file_string)

# Matches only words.
test_string = re.findall('\w+', file_string)

"""Here's the plan:
	if the word doesn't match, loop over the whole phrase to see if you find it.
	If it does, check if the next two words are the same as expected.
	If they are not, reject it. If they are, continue the counter from there (assume extra phrase).

	Also, cut the loop short if it reaches the end of either string.
	GO.
	
	That was the plan. I need to review my logic carefully. It's not working atm."""

print(test_string)
compare_string = input("Please input string for comparison: ")

# This comparison includes punctuation, I'll handle that separately.
#compare_string = re.findall('\w+|[!?",\'.\(\)]', compare_string)

# Setting up the 'true' counters.
# These should match the i in the for loop for a perfect run.
i_test_string = 0
i_compare_string = 0


compare_string = re.findall('\w+', compare_string)
print(compare_string)

# Reference string, to say which words are right about each string.
test_string_watchman = [0] * len(test_string)
compare_string_watchman = [0] * len(compare_string)

# Loop over the max_length
# a break should catch it if it starts to go over either len().
if len(test_string) > len(compare_string):
	max_length = len(test_string)
else:
	max_length = len(compare_string)

# main loop
for i in range(0,max_length):

	# Stop the loop if either end of string is reached.
	# Note to self, this works because it's before any evalutaions,
	# so it doesn't try to use any invalid indicies.
	if i_test_string>=len(test_string) or i_compare_string>=len(compare_string):
		break

	# DEBUG
	#print(i_compare_string)
	#print(i_test_string)

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
			# check if things are going to break at THE START OF THE looop.
			print('TOTALLY TRYING TO COMPARE', j_compare_string+2, 'AND', len(compare_string))
			if (j_compare_string+2)>len(compare_string):
				print('not found')
				break

			a = b = c = 0

			# DEBUG
			print()
			print('in the loop...')
			print('j_test_string:',j_test_string)
			print('j_compare_string:', j_compare_string)
			print('Try to match', compare_string[j_compare_string], 'and', test_string[j_test_string])
			print('Try to match', compare_string[j_compare_string+1], 'and', test_string[j_test_string+1])
			print(j_compare_string+2, '>', len(compare_string), 'or', j_test_string+2, '>', len(test_string))
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
				print('SUCCESSSSSS')
				
				# Still not working...something about the string going too far. Need to trace all the iteration ints.
				test_string_watchman[j_test_string] = 1
				compare_string_watchman[j_compare_string] = 1
				break

			#j_test_string = j_test_string + 1 # of course I don't want to loop this.
			j_compare_string = j_compare_string + 1

	# the compare doesn't do much, because I've iterated over compare_string enough
	i_test_string = i_test_string + 1

	# test if we're at the end of either string 
	print('Successful iteration----------------------------------')

print('i_test_string =', i_test_string)
print('i_compare_string =', i_compare_string)
print('test_string_watchman =', test_string_watchman) 
print('compare_string_watchman =', compare_string_watchman) 
file.close()
	
