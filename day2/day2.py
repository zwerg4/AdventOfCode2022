with open('input.txt') as f:
  input = f.read()

inputArray = input.split("\n")


points = 0
for steps in inputArray:
  step = steps.split(" ")
  if step[1] == "X":
    points += 1
  elif step[1] == "Y":
    points += 2
  elif step[1] == "Z":
    points += 3

  if (step[0] == "A" and step[1] == "X") or (step[0] == "B" and step[1] == "Y") or (step[0] == "C" and step[1] == "Z"):
    points += 3
  elif (step[0] == "A" and step[1] == "Y") or (step[0] == "B" and step[1] == "Z") or (step[0] == "C" and step[1] == "X"):
    points += 6
  else:
    points += 0

print("1) Points all: " + str(points))

points = 0
for steps in inputArray:
  step = steps.split(" ")
  if step[1] == "X": #loose
    points += 0
    if step[0] == "A":
      points += 3 
    elif step[0] == "B":
      points += 1  
    elif step[0] == "C":
      points += 2  
  elif step[1] == "Y": #draw
    points += 3
    if step[0] == "A":
      points += 1 
    elif step[0] == "B":
      points += 2  
    elif step[0] == "C":
      points += 3  
  elif step[1] == "Z": #win
    points += 6
    if step[0] == "A":
      points += 2 
    elif step[0] == "B":
      points += 3  
    elif step[0] == "C":
      points += 1  

print("2) Points all: " + str(points))