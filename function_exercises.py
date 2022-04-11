def is_two(number):
    if number == 2 or number == 'Two':
        return(True)
    else: 
        return(False)

print(is_two(3))

# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(letter):
    if letter in ('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False

print(is_vowel('p'))