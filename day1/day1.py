with open('input.txt') as f:
  input = f.read()

inputArray = input.split("\n\n")

max = 0

for elf in inputArray:
  cal = 0
  calos = elf.split("\n")
  for calo in calos:
    if calo != '':
      cal += int(calo)
  #print("elf has : " + str(cal))
  if cal > max:
    max = cal

print("max is : " + str(max))

max1 = 0
max2 = 0
max3 = 0

for elf in inputArray:
  cal = 0
  calos = elf.split("\n")
  for calo in calos:
    if calo != '':
      cal += int(calo)
  #print("elf has : " + str(cal))
  if cal > max1:
    max1 = cal
  elif cal > max2 or cal == max1:
    max2 = cal
  elif cal > max3 or cal == max2:
    max3 = cal

print("max1 is : " + str(max1))
print("max2 is : " + str(max2))
print("max3 is : " + str(max3))

print("top 3 max is : " + str(max1 + max2 + max3))
