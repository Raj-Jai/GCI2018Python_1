Google = "GCI is great"
x = 0
    
print()
print("TO PRINT GCI is great for 10 times")
print()
for loop in Google:
    print(Google)
    x = x + 1
    if x == 10:
      break
    
print()
print("TO PRINT USER NAME")
print()
print("Please Enter Your Name: ")
name = input()

reverse = name[::-1]

print()
print("Hello {},please to meet you! Did you know that your name backwards is" .format (name),(reverse))
print()
print("Meet you again!")
   
