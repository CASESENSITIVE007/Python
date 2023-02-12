
import random
man=[  
'''
         -------|
            |   |
                |
                |
                |
                |
            ---------''',
 '''
    -------|
       |   |
       o   |
           |
           |
           |
       ---------''',
    '''
         -------|
          |     |
          o     |
           \    |
                |
                |
            ---------''',
    '''
         -------|
          |     |
          o     |
         / \    |
                |
                |
            ---------''',
    '''
         -------|
          |     |
          o     |
         / \    |
          |     |
                |
            ---------''',
    '''
         -------|
          |     |
          o     |
         / \    |
          |     |
         / \    |
            ---------''']
stages=0
print("WELCOME TO HANGMAN YOU HAVE 6 lives LIVES\nLETS GOO!!!!")
words=["mouse","elephant","tiger","buffalloo","btslover"]
random_word=random.choice(words)
#abcprint(random_word)
list_underscore=[]
for i in range(len(random_word)):
    a="_"
    list_underscore.append(a)
print(list_underscore)
for i in range(len(random_word)+10):
    if a in list_underscore:
        letter=input("enter the letter: ").lower()
        for position in range(len(random_word)):
            i=random_word[position]
            if i==letter:
                list_underscore[position]=i
        print(list_underscore)
    if letter not  in random_word:
            print(man[stages])
            stages+=1    
    if stages==6:    
        print("you loose")
        break  
              
if a not in list_underscore:
    print("you win")



