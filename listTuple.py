#Generate a list of tuples where each tuple contains a number and its square, for numbers from 1 to 10.

list = [ (x, x * x) for x,y in enumerate(range(1, 11))]
print(list)