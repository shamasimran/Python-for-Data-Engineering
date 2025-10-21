
# while loop does not automatically create or update a counter.
# You have to declare i yourself and manually update it (i += 1).

i = 1
while i <= 5: #while i in range(5):
  print(i)
  if i == 3:
    print("loop is going to break due to break statement")
    break
  else:
    print("loop is continuing")
  i += 1
else:
  print("loop is completed, as i is no longer less than or equal to 5")
# Note: The else block after while loop executes only if the loop is not terminated by a break statement.


fruits = ["apple", "banana", "cherry", "mango"]
for x in fruits:
    print(x)
    if "cherr" in x:
        print("loop is going to break as we found cherry")
        break
    else:
        print("loop is continuing")

# if you have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass
