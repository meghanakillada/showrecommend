#PLAYGROUND

#Strings and Numbers
print("hello world") #strings are between quotes
print(int(5))
print(float(5))

#Variables and Assignments
red = "\033[1;31;40m"
print(red, "hello world!!!!!")

#Lists, Arrays, 2D
example_list = [1, 2, 3, 4]
print(example_list[-1])

#Iteration
ship1_L = ["   /|   ", "   \|   ", "\___|__/", " \____/ "]
ship1_R = [" |\ ", " |/ ", "\___|__/", " \____/ "]

for variable in ship1_L:
    print(variable)

print(ship1_L[0])
print(ship1_L[1])
print(ship1_L[2])
print(ship1_L[3])

#Procedures, Function, Classes/Objects
def funcy():
    import funcy
    funcy.snake()
#funcy()
