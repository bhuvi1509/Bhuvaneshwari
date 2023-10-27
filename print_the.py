'''Problem 1:
Read a passage from a file. (If you don't know how to handle files in Python, you can hardcode a long passage)
Count the number of times the word 'the' followed by another 'the' without 'a' in between.

Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.

answer is 4 (The king, the forest, The King the next).'''


s = "The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day."
target = "the" 
words = s.split()
for i,w in enumerate(words):
    if w == target:
        # next word
        print (target + words[i+1]) 
        
        # previous word
        '''if i>0:
            print( target + words[i-1]) '''
