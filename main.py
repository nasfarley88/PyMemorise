#!/usr/bin/python3.2
import re
from termcolor import colored, cprint

#TODO: known bugs
# - allowed punctuation does not spark wrong word at the beggining of the word.
#   i.e. 'word will match word but not w'ord will not match word.

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
			cprint(test_string[i], 'yellow', end='')
		else:
			#else, check each word.
			#print('No Match')
			temp_test_word = re.findall('\w+[\'-,]?\w*',test_string[i])
			#print(temp_test_word)
			temp_compare_word = re.findall('\w+[\'-,]?\w*',compare_string[i])
			#print(temp_compare_word)
			temp_min_length = min(len(temp_test_word),len(temp_compare_word))
			temp_max_length = max(len(temp_test_word),len(temp_compare_word))

			for j in range(0,temp_min_length):
				if re.match(re.compile(temp_test_word[j]), temp_compare_word[j]):
					#if match, print test word.
					cprint(temp_test_word[j], 'yellow', end='')
				else:
					#else, print **wrong word**<right word>
					cprint(temp_compare_word[j], 'red', end='')
					cprint("[" + temp_test_word[j] + "]", 'blue', end='')
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
	# TODO This is supposed to be the loop that prints the rest of the test string. 
	# it's not working yet.
#	if min_length < len(temp_test_word): 
#		for j in range(min_length+1,len(temp_test_word)):
#			print(temp_test_word[j], end=' ')
#		print(test_string_punc[i], end=' ')
	# end of not working bit.

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
test_string_punc = test_string # this will be formatted later
#print(file_string)
print(test_string)

# New plan: catalog phrases, not words. Let's match phrases
test_string = re.findall('([\w\s\'-,]+)[\W\s\'-]+', test_string)
print(test_string)

# I need to extract the punctuation
test_string_punc = re.findall('[.;:]', test_string_punc)
print(test_string_punc)

print('\n\n###Time for comparison###\n\n')

#compare_string = input("Please input string for comparison: ")
file_compare = open('temp_compare.pym', 'r')
compare_string = file_compare.read()

compare_string = re.findall('([\w\s\'-,]+)[\W\s\'-]+', compare_string)
print(compare_string)
print()


################### everyting after this needs to be functioned out. ###############

# Time to show the user what's happened to their string
#test_string_watchman = [0] * len(test_string)
#compare_string_watchman = [0] * len(compare_string)
check_string(test_string,compare_string,test_string_punc)

# just a print to get the next line.
print()
