#!/usr/bin/python3.2
import re
from termcolor import colored, cprint

#TODO: known bugs
# - allowed punctuation does not spark wrong word at the beggining of the word.
#   i.e. 'word will match word but not w'ord will not match word.
# 
# This program needs a big debug. A proper, awake, work through to test the logic
# It's too twisted to change now.

"""Very simply compare the given string to a second given string.

The termcolor package is required for this python script to run."""

def check_string(test_string,compare_string,test_string_punc):
	"""Check if the string is correct."""
	# I'm thinking, we make this function, the one that checks the method we need to use.
	min_length = min(len(test_string),len(compare_string))
	for i in range(0,min_length):
		# Compare the compare_string to see if it matches the test_string and vice versa
		if re.match(re.compile(test_string[i]), compare_string[i]) \
				and re.match(re.compile(compare_string[i]), test_string[i]):
			#if matches, print the test string equivalent
			#cprint(test_string[i], 'yellow', end='')
			printsp(test_string[i], 'yellow')
		else:
			#else, check each word.
			#print('No Match') temp_test_word = re.findall('\w+[\'-,]?\w*',test_string[i])
			#print(temp_test_word)
			temp_compare_word = re.findall('\w+[\'-]?\w*',compare_string[i])
			#print(temp_compare_word)
			temp_min_length = min(len(temp_test_word),len(temp_compare_word))
			temp_max_length = max(len(temp_test_word),len(temp_compare_word))

			for j in range(0,temp_min_length):
				if re.match(re.compile(temp_test_word[j]), temp_compare_word[j]):
					#if match, print test word.
					#cprint(temp_test_word[j], 'yellow', end='')
					printsp(temp_test_word[j], 'yellow')
				else:
					#else, print **wrong word**<right word>
					#cprint(temp_compare_word[j], 'red', end='')
					printsp(temp_compare_word[j], 'red')
					#cprint("[" + temp_test_word[j] + "]", 'blue', end='')
					printsp("[" + temp_test_word[j] + "]", 'blue')
				# put a space at the end of the word, but not before [.,;:]
				if j != temp_max_length-1: print(' ', end='')

			# This part of the function should probably do the same for compare_string too.
			# Loop for continuing temp_test_word
			if temp_min_length<len(temp_test_word):
				
				cprint("[", 'blue', end='')
				for k in range(temp_min_length,len(temp_test_word)):
					cprint(temp_test_word[k], 'blue', end='')
					if k != len(temp_test_word)-1:
						print(' ', end='')
				cprint("]", 'blue', end='')

			# This doesn't work, but probably because it doesn't detect anything wrong.
			if temp_min_length<len(temp_compare_word):
				for k in range(temp_min_length,len(temp_compare_word)):
					cprint(temp_compare_word[k], 'red', end='')
					if k != len(temp_compare_word)-1:
						print(' ', end='')

		cprint(test_string_punc[i], 'yellow', end=' ')

def printsp(x,color):
	"""Print a string with a preceding space if not a punctuation character"""
	if re.match('[.,;:]', x): 
		cprint(x, color, end='')
	else:
		print(end=' ')
		cprint(x, color, end='')


def check_string_2(test_string,compare_string):
	"""Check if the string is correct -- BibleMemorizer technique."""

	# Split the strings for processing
	test_string = re.findall('\w+|[;:,.]', test_string)
	compare_string = re.findall('\w+|[,.;:]', compare_string)
	
	# Some debug output
	print('The test_string is: ', test_string, '\n')
	print('The compare_string is:', compare_string, '\n')

	# find the minimum length, for the loop to iterate over.
	min_length = min(len(test_string),len(compare_string))

	# Various variable to change which strings are compared.
	i_user_offset = 0
	missing_counter = 0
	i_real_offset = 0

	# This loop goes across the string lists until one runs out.
	for i_real in range(0,min_length):

		# match_is_true allows the loop to know if a match has happened.
		match_is_true = False

		# variable to control the 'real' or test string.
		ir = i_real + i_real_offset
		
		# variable to control the 'user' or compare string
		iu = i_real + i_user_offset
		
		# TODO here the re.compile matches '.' as DOTALL. Hrmf
		if re.match(re.compile(test_string[ir]), compare_string[iu]) \
				and re.match(re.compile(compare_string[iu]), test_string[ir]):
			
			# If there are missing words from something before, print them before printing the match.
			if missing_counter > 0:
				for j in range (ir-missing_counter,ir):
					#cprint(test_string[j], 'blue', end='')
					printsp(test_string[j], 'blue')
				
				# Reset the counter, it's done it's job
				missing_counter = 0
			# Print the match.
			#cprint(test_string[ir], 'yellow', end='')
			printsp(test_string[ir], 'yellow')
		else:
			print('or maybe...')
			# If it doesn't match, then loop over the rest of the compare_string 
			for j in range(ir,min_length):
				if re.match(re.compile(test_string[j]), compare_string[iu]) \
						and re.match(re.compile(compare_string[iu]), test_string[j]):
					# If it matches, print the missing words (in blue), reset the wroung_counter and change... variables?!
					for k in range(ir,j):
						print('this one')
						# Print the words in between, and the one's counted by missing_counter
						#cprint(test_string[k], 'blue', end='')
						printsp(test_string[k], 'blue')
						# Because it's output them now.
						missing_counter = 0
					
					# Setting the offsets to reflect the new values.
					i_user_offset = i_user_offset + i_real - j
					i_real_offset = i_real_offset + j - i_real

					# A change in i_user_offset and i_real_offset implies that...
					ir = i_real + i_real_offset
					iu = i_real + i_user_offset
					# should be reset

					# Act as if it is the right one.
					#cprint(test_string[ir], 'yellow', end='')
					printsp(test_string[ir], 'yellow')
					print('matched with' + compare_string[iu])
					match_is_true = True
					break # break the loop, we've found what we're looking for.
				
			# If the previous for loop didn't find anything then print the word as wrong
			if match_is_true == False:
				#cprint(compare_string[i_real+i_user_offset], 'red', end='')
				printsp(compare_string[i_real+i_user_offset], 'red')

				# This makes sure the test string does not move on (it hasn't been found yet).
				i_real_offset = i_real_offset - 1

				# And, just so I don't forget to set this later
				ir = i_real + i_real_offset

		# This if is supposed to print the rest of the string in the event it's not already printed by the end of the testing.
		# In order to fix this, I *need* to understand how my variables work. I'll draw a diagram tomorrow. (Sunday 27th May)
		"""if i + i_user_offset > min_length or i + i_real_offset > min_length:
			print("OH MY GOSH IT'S ALL GOING TO--")
			print('len(test_string) =', len(test_string), "i+i_user_offset =", i+i_user_offset)
			print('len(compare_string) =', len(compare_string), 'i+i_real_offset =', i+i_real_offset)
			if i + i_user_offset >= len(test_string):
				for j in range(i + i_real_offset, len(test_string)):
					cprint(test_string[j], 'blue', end=' ')
			if i + i_real_offset > len(compare_string):
				for j in range(i + i_real_offset+1, len(compare_string)):
					cprint(compare_string[j], 'red', end=' ')
			# TODO I'm unclear as to why this break is here. But it does 'fix' stuff.
			# Maybe rewrite the if loop, with a proper understanding of the variables.
			break # break, because the user string has come to an end before i loop is ready to give up. """

def no_of_punc(x):
	""" I may not need this function anymore... using different methods for punctuation."""
	#TODO possible error when there is a newline in the quote (i.e. a '\n')
	y = "no_of_punc didn't work."
	#y = re.findall('([\w\s\'-,]+)[\W\s\'-]+', x)
	y = re.findall('[\w\s\-\']+', x)
	z = [0]*(len(y))
	for i in range(0,len(y)-1):
		y[i] = re.findall('\w+', y[i])
		z[i] = len(y[i])
	print("y =",y)
	print("z =",z)
	return z



# Some intro stuff
cprint('################################################################################', 'red')
cprint('##########                                                            ##########', 'red')
cprint('##########  PyMemorise: Helping you memorise everything you want to!  ##########', 'red')
cprint('##########                                   Author: Nathanael Farley ##########', 'red')
cprint('################################################################################', 'red')

#test_string = input("Please input a test string to compare: ")
#file = open('temp.pym', 'w')
#file.write(test_string)
#file.close()
file = open('temp_test.pym', 'r')

#file_string = file.read()
test_string = file.read()
test_string_unchanging = test_string # TODO remove this variable later, restructure the programe to have only one unchangeable variable
test_string_punc = test_string # this will be formatted later
#print(file_string)
print(test_string)


print('\n\n###Time for comparison###\n\n')

#compare_string = input("Please input string for comparison: ")
file_compare = open('temp_compare.pym', 'r')
compare_string = file_compare.read()

# Time to show the user what's happened to their string
check_string_2(test_string,compare_string)
