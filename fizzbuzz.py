#loop starts
for x in range(1,101):
#checks if number isn't equal to 3 or 5 first
  if(x % 3 != 0 and x % 5 != 0):
    print(str(x), end=", ")
#checks if number is divisible by 3 and if it's also divisible by 5
  if(x % 3 == 0):
    if(x % 5 == 0):
      print("fizz buzz", end=", ")
      continue
    else:
      print("fizz", end=", ")
 #only checks if it's divisible by 5 bc the second if statement would catch if a number's divisible by 3. 
  if(x % 5 == 0):
      print("buzz", end=", ")
