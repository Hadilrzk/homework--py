word = input('enter a word:').lower().replace(" ","")
cout=0
for x in word:
     cout += 1
print(f" the number of letters in the word{word} is:{cout}")    