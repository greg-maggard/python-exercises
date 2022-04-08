#!/usr/bin/env python
# coding: utf-8

# 1. You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

# In[5]:


rental_lengths = [3, 5, 1]

rental_cost = 0 

for i in rental_lengths:
    rental_cost += (3 * i)

rental_cost


# 2. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

# In[6]:


def timesheet_calculation(google, amazon, facebook):
    total_pay = (google * 400) + (amazon * 380) + (facebook * 350)
    return total_pay
    
timesheet_calculation(6, 4, 10)


# 3. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

# In[15]:


class_not_full = True
no_schedule_conflict = True

enrollment_possible = class_not_full and no_schedule_conflict

print(enrollment_possible)


# 4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

# In[19]:


premium_member = False
amount_purchased = 3
offer_not_expired = True

offer_applied = premium_member or ((amount_purchased > 2) and offer_not_expired)

print(offer_applied)


# Continue working in your data_types_and_variables.py file. Use the following code to follow the instructions below:
# 
# username = 'codeup'
# password = 'notastrongpassword'

# In[27]:


username = 'codeup'
password = 'notastrongpassword'

pw_at_least_5 = (len(password) >= 5)
un_at_most_20 = (len(username) <= 20)
do_not_match = (password != username)
no_white_space = ((password[0] != ' ' and password[-1] != ' ') and (username[0] != ' ' and username[-1] != ' '))

print(pw_at_least_5)
print(un_at_most_20)
print(do_not_match)
print(no_white_space)

