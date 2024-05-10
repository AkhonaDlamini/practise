#Use a lambda function to sort a list of tuples based on the second element.
list = [(1,'Mon'),(2,'Tues'),(3,'Wed'),(4,'Thurs'),(5,'Frid'),(6,'Surt'),(7,'Sun')]

new_list = sorted(list, key = lambda x : x[1])
print(new_list)

