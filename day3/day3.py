with open('input.txt') as f:
  input = f.read()

inputArray = input.split("\n")
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

sum = 0
for rucks in inputArray:
  rucks = rucks.strip()
  left = rucks[:int(len(rucks)/2)]
  right = rucks[int(len(rucks)/2):]
  duplicates = []
  for letter in letters:
    if letter in left and letter in right:
      duplicates.append(letter)
  for dup in duplicates:
    sum += letters.index(dup)+1

print("Sum of priorities: " + str(sum))

sum = 0
for group in range(0,len(inputArray),3):
  usr1 = inputArray[group]
  usr2 = inputArray[group + 1]
  usr3 = inputArray[group + 2]
  for letter in letters:
    if letter in usr1 and letter in usr2 and letter in usr3:
      sum += letters.index(letter)+1

print("Sum of group priorities: " + str(sum))