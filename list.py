'''Write a simple quiz game that has a list of ten questions and a list of answers to those questions.
The game should give the player four randomly selected questions to answer. It should
ask the questions one-by-one, and tell the player whether they got the question right or
wrong. At the end it should print out how many out of four they got right.'''
from random import *
questions= \
    [
    'What is the capital of the United States of America? ',
    'Who is the current president of the United States of America? ',
    'What is the capital of Nigeria? ',
    'Muhammadu Buhari is the president of which country? ',
    'Uhuru Kenyatta is the president of which country? ',
    'What is the capital of France? ',
    'Which state has only one neighbor? ',
    'Where is Amsterdam located? ',
    'Emmanuel Macron is the president of which country?  ',
    'Sir Alex Ferguson until his retirement coached which team? ',
    ]

answers=[ 'Washington DC',
          'Donald Trump',
          'Abuja',
          'Nigeria',
          'Kenya',
          'Paris',
          'Maine',
          'Netherland',
          'France',
          'Manchester United'
        ]
s= sample(questions,4)

num_right= 0
ai = 0 
for i in range(len(s)):
    answer= input(s[i])
	#get corresponding index 
    ai = questions.index(s[i])#chai, no semi colon, useless lang, oh well, what's my own :)
    if answer.lower()== answers[ai].lower():
        print('Correct!!!')
        num_right+=1
    else:
        print('Not correct ')
        print(answers[ai])










