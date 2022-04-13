#!/usr/bin/env python
# coding: utf-8

# ### 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[75]:


def is_two(number):
    if number == 2 or number == '2':
        return(True)
    else: 
        return(False)
    
    
#Adam's solution:
def is_two(n):
    return n == 2 or n == '2'

## This ^ will return the boolean value, without having to write 'if' statements to specifically call for them. 

#print(is_two(3))


# ### 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
# 

# In[78]:


def is_vowel(letter):
    if letter in ('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False

# Adam's solution: 

def is_vowel2(somestring):
    if type(somestring) == str: #This line intended to verify first that the input is a string.
        result = somestring.lower() in ['a', 'e', 'i', 'o', 'u']
        return result
    else:
        return False
    
#print(is_vowel('a'))
#print(is_vowel2('a'))

# I could rewrite mine as (note that in my original, I did not write in a check to verify that the input is a string.)

def is_vowel3(string):
    return string in ('a', 'e', 'i', 'o', 'u')

#print(is_vowel3('a'))

#A key thing I want to remember is that Python is *already* evaluating expressions, before I ever include an 'if' statement.
#This means that if I'm wanting to return a boolean value, I should think about whether the extra lines will make any difference. 


# ### 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
#     

# In[79]:


def is_consonant(letter):
    if letter in ('a', 'e', 'i', 'o', 'u'):
        return False
    else:
        return True
    
#print(is_consonant('b'))
    
#Adam's solution
def is_consonant2(somestring):
    if type(somestring) == str: #This line validates the string type (I'd like to practice including these more)
        only_letters = somestring.isalpha() #This line verifies that the characters are alphabetical
        return only_letters and not is_vowel(somestring) # This line runs it through the is_vowel function and negates the return. Since consonants and vowels are dichotomous.
    return False

# print(is_consonant2('b'))


# ### 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
# 

# In[6]:


def capital_word(word):
    first_letter = word[0]
    if word[0] not in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']:
        print(word[0])
        return str(word).title()
    else:
        return "Please enter a word starting with a consonant."

#print(capital_word('Axolotl'))


# ### 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[22]:


def calculate_tip(percentage, total):
    if percentage > 1 or percentage < 0:
        return str('Please use a percentage value in decimal form, between 0 and 1.')
    else:
        return str('Your total bill, including tip, is: $' + str((round(float(((total * percentage) + total)),2))))
    
#print(calculate_tip(.25, 12.12))


# ### 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[30]:


def apply_discount(original_price, discount_percent):
    if discount_percent > 1 or discount_percent < 0:
        return str('Please use a discount percentage value in decimal form, between 0 and 1.')
    else:
        return str('Your total bill, minus discount, is: $' + str((round(float(((original_price - (original_price * discount_percent)))),2))))
                                                                  
#print(apply_discount(12.12, .15))                                                                


# ### 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[32]:


def handle_commas(str):
    return str.replace(',','')

#print(handle_commas('37,000'))

#Adam's Solution:
def handle_commas2(somestring):
    if type(somestring) != str:
        return 'input must be a string'
    somestring = somestring.replace(',','')
    if somestring.isdigit():
        return float(somestring)
    else: 'Please enter a value that is a string.'


# ### 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[36]:


def get_letter_grade(grade):
    if type(grade) in [float, int]:
        if grade >= 90:
            letter = 'A'
        elif grade >= 80 and grade < 90:
            letter = 'B'
        elif grade >= 70 and grade < 80:
            letter = 'C'
        elif grade < 70:
            letter = 'F'
        return str('Your letter grade is: ' + str(letter))
    return "Please enter a value as a float or integer."

#print(get_letter_grade(92))


# ### 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[47]:


def remove_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    letter_list = []
    for letter in str:
        if letter not in vowels:
            letter_list.append(letter)
    vowels_removed = tuple(letter_list)
    return ''.join(vowels_removed)
    
# print(remove_vowels('soliloquy'))


# ### 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# 
# #### - anything that is not a valid python identifier should be removed
# #### - leading and trailing whitespace should be removed
# #### - everything should be lowercase
# #### - spaces should be replaced with underscores
# #### - for example:
#     - Name will become name
#     - First Name will become first_name
#     - % Completed will become completed

# In[64]:


def normalize_name(string):
    return string.strip((' 0123456789!@#$%^&*')).replace(' ', '_').lower()

#print(normalize_name('Name'))

#the string method .isidentifier() could take some of the guesswork out of what is allowed.


# ### 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[71]:


def cumulative_sum(number_list):
    sum_list = []
    sum_value = 0
    for number in number_list:
        sum_value += number
        sum_list.append(sum_value)
    return sum_list

#print(cumulative_sum([1, 2, 3, 4]))

#Come back and look into the "enumerate" tool for this exercise. 


# # BONUS

# ### 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# In[ ]:





# ### 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column. 

# In[ ]:




