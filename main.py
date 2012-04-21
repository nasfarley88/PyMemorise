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
			#print('No Match') temp_test_word = re.findall('\w+[\'-,]?\w*',test_string[i])
			#print(temp_test_word)
			temp_compare_word = re.findall('\w+[\'-]?\w*',compare_string[i])
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


def check_string_2(test_string,compare_string,test_string_punc):
	"""Check if the string is correct -- BibleMemorizer technique."""
	# I'm thinking, we make this function, the one that checks the method we need to use.
	min_length = min(len(test_string),len(compare_string))
	i_user_offset = 0
	wrong_counter = 0
	i_real_offset = 0
	for i_real in range(0,min_length):
		match_is_true = False
		i = i_real + i_real_offset
		print()
		print('i loop entered, where i =', i, 'i_user_offset =', i_user_offset, "i_real_offset =", i_real_offset)
		# Compare the compare_string to see if it matches the test_string and vice versa
		print('I want to compare', test_string[i], 'and', compare_string[i+i_user_offset])
		if re.match(re.compile(test_string[i]), compare_string[i+i_user_offset]) \
				and re.match(re.compile(compare_string[i+i_user_offset]), test_string[i]):
			print()
			print("MATCH")
			# Print any missing words
			if wrong_counter > 0:
				for j in range (i-wrong_counter,i):
					cprint(test_string[j], 'blue', end='')
				
				# Reset the counter, it's done it's job
				wrong_counter = 0
			#if matches, print the test string equivalent (saying it's good.)
			cprint(test_string[i], 'yellow', end='')
		else:
			for j in range(i,min_length):
				#print()
				print('j loop entered, j =', j, ' i =', i)
				if re.match(re.compile(test_string[j]), compare_string[i+i_user_offset]) \
						and re.match(re.compile(compare_string[i+i_user_offset]), test_string[j]):
					for k in range(i,j):
						#print()
						print('k loop entered, k =', k, ' j =', j, ' i =', i)
						# Print the words in between, and the one's counted by wrong_counter
						cprint(test_string[k], 'blue', end='')
						# Because it's output them now.
						wrong_counter = 0
					#i_user_offset = i_user_offset + i_real + i_real_offset - j
					i_user_offset = i_user_offset + i - j
					print('i_user_offset =', i_user_offset)
					#i_real_offset = j - i_real
					i_real_offset = i_real_offset + j - i
					print('i_real_offset =', i_real_offset)
					#print('Before the change j =', j, 'and i =', i)
					# Act as if it is the right one.
					cprint(test_string[i_real+i_real_offset], 'yellow', end='')
					#print()
					print('Changed j to', j, 'i to', i, 'i_user_offset to', i_user_offset)
					match_is_true = True
					break # break the loop, we've found what we're looking for.

			if match_is_true == False:
				cprint(compare_string[i+i_user_offset], 'red', end='')
				print('I couldn\'t find the word you\'re looking for...')
				i_real_offset = i_real_offset - 1
				i_user_offset = i_user_offset + 1
				# Can't find a word? Count how many here.
				#wrong_counter = wrong_counter + 1


		if i + i_user_offset > min_length or i + i_real_offset > min_length:
			print("OH MY GOSH IT'S ALL GOING TO--")
			print('len(test_string) =', len(test_string), "i+i_user_offset =", i+i_user_offset)
			print('len(compare_string) =', len(compare_string), 'i+i_real_offset =', i+i_real_offset)
			if i + i_user_offset >= len(test_string):
				for j in range(i + i_real_offset, len(test_string)):
					cprint(test_string[j], 'blue', end=' ')
			if i + i_real_offset > len(compare_string):
				for j in range(i + i_real_offset+1, len(compare_string)):
					cprint(compare_string[j], 'red', end=' ')
			break # break, because the user string has come to an end before i loop is ready to give up.

def no_of_punc(x):
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
test_string_unchanging = test_string # remove this variable later, restructure the programe to have only one unchangeable variable
test_string_punc = test_string # this will be formatted later
#print(file_string)
print(test_string)

# New plan: catalog phrases, not words. Let's match phrases
#test_string = re.findall('([\w\s\'-,]+)[\W\s\'-]+', test_string)
test_string = re.findall('([\w\'-,]+)[\W\'-]+', test_string)
print(test_string)

# I need to extract the punctuation
test_string_punc = re.findall('[,.;:]', test_string_punc)
print(test_string_punc)

print('\n\n###Time for comparison###\n\n')

#compare_string = input("Please input string for comparison: ")
file_compare = open('temp_compare.pym', 'r')
compare_string = file_compare.read()

#compare_string = re.findall('([\w\s\'-,]+)[\W\s\'-]+', compare_string)
compare_string = re.findall('([\w\'-,]+)[\W\'-]+', compare_string)
print(compare_string)
print()



################### everyting after this needs to be functioned out. ###############

# Time to show the user what's happened to their string
#test_string_watchman = [0] * len(test_string)
#compare_string_watchman = [0] * len(compare_string)
# TODO this will be reinstaed when I have done the BibleMemoriser technique
#check_string(test_string,compare_string,test_string_punc)
check_string_2(test_string,compare_string,test_string_punc)

no_of_punc(test_string_unchanging)



# just a print to get the next line.
print()
