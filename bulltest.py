str = 'Snow,John,21\nLincoln,Abraham,31\nGates,Bill,29'

 #Split the original string to lines/records by newline character
for man in (str.split("\n")): 
     #Split every record for attribute 
     name, given_name, age = man.split(",")
     print("Name: " + name + "| Given Name: " + given_name + "| Age: " + age)
     
