#!/usr/bin/python3.2
import re

"""Very simply compare the given string to a second given string."""

def check_string(test_string,compare_string):
	"""Check if the string is correct."""
	# I'm thinking, we make this function, the one that checks the method we need to use.
	min_length = min(len(test_string),len(compare_string))
	for i in range(0,min_length):
		# Compare the compare_string to see if it matches the test_string
		if re.match(re.compile(test_string[i]), compare_string[i]):
			#print('Match')
			print(test_string[i], end='')
		else:
			#print('No Match')
			temp_test_word = re.findall('\w+[\'-]?\w+',test_string[i])
			#print(temp_test_word)
			temp_compare_word = re.findall('\w+[\'-]?\w+',compare_string[i])
			#print(temp_compare_word)
			temp_min_length = min(len(temp_test_word),len(temp_compare_word))

			# TODO the min length restricts the output to the length of the guess.
			# This needs to work so that if the guesser didn't guess enough words
			# in that phrase it continues to 'not match' the words.
			#
			# The problem is, bad attempts will not match the same number of phrases
			# probably not even close. The questions to ask is, what would a 
			# human do to tell you it was wrong?
			# - Tell the person it's wrong, and not continue reviewing
			# - check for similar words?
			#
			# Do I need to use a different method for mis-phrased attempts?
			for j in range(0,temp_min_length):
				if re.match(re.compile(temp_test_word[j]), temp_compare_word[j]):
					#print('\tMatch word')
					print(temp_test_word[j], end='')
				else:
					#print('\tNot Match word')
					print("**" + temp_test_word[j] + "**<" + temp_compare_word[j] + ">" , end='')
				# put a space at the end of the word, but not before [.,;:]
				if j != temp_min_length-1: print(' ', end='')
	# TODO This is supposed to be the loop that prints the rest of the test string. 
	# it's not working yet.
	if min_length < len(temp_test_word): 
		for j in range(min_length+1,len(temp_test_word)):
			print(temp_test_word[j], end=' ')
		print(test_string_punc[i], end=' ')
	# end of not working bit.

# Some intro stuff
print('################################################################################')
print('##########                                                            ##########')
print('##########  PyMemorise: Helping you memorise everything you want to!  ##########')
print('##########                                   Author: Nathanael Farley ##########')
print('################################################################################')

#test_string = input("Please input a test string to compare: ")
#file = open('temp.pym', 'w')
#file.write(test_string)
#file.close()
file = open('temp.pym', 'r')

#file_string = file.read()
test_string = file.read()
test_string_punc = test_string # this will be formatted later
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

# I need to extract the punctuation
test_string_punc = re.findall('[.,;:]', test_string_punc)
print(test_string_punc)

print('\n\n###Time for comparison###\n\n')

#compare_string = input("Please input string for comparison: ")
file_compare = open('temp_compare.pym', 'r')
compare_string = file_compare.read()

compare_string = re.findall('([\w\s\'-]+)[\W\s\'-]+', compare_string)
print(compare_string)
print()


################### everyting after this needs to be functioned out. ###############

# Time to show the user what's happened to their string
#test_string_watchman = [0] * len(test_string)
#compare_string_watchman = [0] * len(compare_string)
check_string(test_string,compare_string)
"""
min_length = min(len(test_string),len(compare_string))

print('Prepare to be CORRECTED')

for i in range(0,min_length):
	# Compare the compare_string to see if it matches the test_string
	if re.match(re.compile(test_string[i]), compare_string[i]):
		#print('Match')
		print(test_string[i], end='')
	else:
		#print('No Match')
		temp_test_word = re.findall('\w+[\'-]?\w+',test_string[i])
		#print(temp_test_word)
		temp_compare_word = re.findall('\w+[\'-]?\w+',compare_string[i])
		#print(temp_compare_word)
		temp_min_length = min(len(temp_test_word),len(temp_compare_word))

		# TODO the min length restricts the output to the length of the guess.
		# This needs to work so that if the guesser didn't guess enough words
		# in that phrase it continues to 'not match' the words.
		#
		# The problem is, bad attempts will not match the same number of phrases
		# probably not even close. The questions to ask is, what would a 
		# human do to tell you it was wrong?
		# - Tell the person it's wrong, and not continue reviewing
		# - check for similar words?
		#
		# Do I need to use a different method for mis-phrased attempts?
		for j in range(0,temp_min_length):
			if re.match(re.compile(temp_test_word[j]), temp_compare_word[j]):
				#print('\tMatch word')
				print(temp_test_word[j], end='')
			else:
				#print('\tNot Match word')
				print("**" + temp_test_word[j] + "**<" + temp_compare_word[j] + ">" , end='')
			# put a space at the end of the word, but not before [.,;:]
			if j != temp_min_length-1: print(' ', end='')
	print(test_string_punc[i], end=' ')
"""

# just a print to get the next line.
print()























# Next, to get each phrase to check it's word content. But only if it's a 
# Not Match




# This comparison includes punctuation, I'll handle that separately.
#compare_string = re.findall('\w+|[!?",\'.\(\)]', compare_string)

## Setting up the 'true' counters.
## These should match the i in the for loop for a perfect run.
#i_test_string = 0
#i_compare_string = 0
#
#
#
#compare_string = re.findall('([\w\s\'-]+)[\W\s\'-]+', compare_string)
#print(compare_string)
#
## Reference string, to say which words are right about each string.
#test_string_watchman = [0] * len(test_string)
#compare_string_watchman = [0] * len(compare_string)
#
#"""
## Loop over the max_length
## a break should catch it if it starts to go over either len().
#if len(test_string) > len(compare_string):
#	max_length = len(test_string)
#else:
#	max_length = len(compare_string)
#"""
#max_length = len(test_string)-2
## main loop
#for i in range(0,max_length):
#	if re.match(re.compile(compare_string[i_compare_string]), test_string[i_test_string]):
#
#		# Mark the word as correct in both strings.
#		test_string_watchman[i_test_string] = 1
#		compare_string_watchman[i_compare_string] = 1
#		
#		# prepare the number for the next iteration.
#		i_compare_string = i_compare_string + 1
#
#	else:
#		# assume that if we ignore the watchmen, they'll still 0.
#		# Loop over the rest, check if it's valid.
#
#		# true counters for the else
#		j_test_string = i_test_string
#		j_compare_string = i_compare_string
#
#		# pin the start
#		j_start = i
#		
#		# This range is the maximum range we could need.
#		for j in range(j_start,max_length):
#
#			a = b = c = 0
#
#			# DEBUG
#			print()
#			print('in the loop...')
#			print('i_test_string:', i_test_string)
#			print('i_compare_string:', i_compare_string)
#			print('j_test_string:',j_test_string)
#			print('j_compare_string:', j_compare_string)
#			print('Try to match', compare_string[j_compare_string], 'and', test_string[j_test_string])
#			print('Try to match', compare_string[j_compare_string+1], 'and', test_string[j_test_string+1])
#			print('Try to match', compare_string[j_compare_string+2], 'and', test_string[j_test_string+2])
#			#print(re.match(re.compile(compare_string[j_compare_string]), test_string[j_test_string]))
#			#print(re.match(re.compile(compare_string[j_compare_string+1]), test_string[j_test_string+1]))
#			#print(re.match(re.compile(compare_string[j_compare_string+2]), test_string[j_test_string+2]))
#			print()
#
#			# To improve readability, I'll put these here instead of in the if.
#			a = bool(re.match(re.compile(compare_string[j_compare_string]), test_string[j_test_string]))
#			b = bool(re.match(re.compile(compare_string[j_compare_string+1]), test_string[j_test_string+1]))
#			c = bool(re.match(re.compile(compare_string[j_compare_string+2]), test_string[j_test_string+2]))
#			print('The result of comparisons...', a, b, c)
#
#			if a and b and c:
#				print('There is a match!')
#				
#				# Still not working...something about the string going too far. Need to trace all the iteration ints.
#				test_string_watchman[j_test_string] = 1
#				compare_string_watchman[j_compare_string] = 1
#				break
#			else:
#				#j_test_string = j_test_string + 1 # of course I don't want to loop this.
#				j_compare_string = j_compare_string + 1
#
#				# Check it's not going to collide and overreach the end of the string
#				test_variable = j_compare_string + 2
#				if test_variable == len(compare_string)-1:
#					print('DONT\' PANIC')
#
#	# Try the next word for a match
#	i_test_string = i_test_string + 1
#
#	print('-'*10,'Successful iteration','-'*10)
#	print('test_string_watchman:', test_string_watchman)
#	print('compare_string_watchman:', compare_string_watchman)
#
#print('i_test_string =', i_test_string)
#print('i_compare_string =', i_compare_string)
#print('test_string_watchman =', test_string_watchman) 
#print('compare_string_watchman =', compare_string_watchman) 
file.close()
file_compare.close()
	
