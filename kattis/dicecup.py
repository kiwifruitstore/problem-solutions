# probability boooooooooooo

"""
6 6:

grid thing, but it's 7 as expv(6) = 3.5

can't do this solely on expected value though

how to find all solutions
for loops? messed up
should be some prettier math
one way: 
for i in first dice:
    for n in second dice:
        n + i = output
etc etc
this will run max 400 times :skull:


whatever
"""


inputline = input()
first_dice = int(inputline.split(" ")[0])
second_dice = int(inputline.split(" ")[1])

possible_values = []
for x in range(1, first_dice + 1):
    for y in range(1, second_dice + 1):
        possible_values.append(int(x+y))
#print(possible_values)
frequency_list = []
max_frequency = 0
for thing in range(2, first_dice + second_dice):
    if possible_values.count(thing) > max_frequency:
        max_frequency = possible_values.count(thing)
    frequency_list.append([thing, possible_values.count(thing)])
#print(frequency_list)
#print(max_frequency)
# item, frequency
output = []
for item in frequency_list:
    if item[1] == max_frequency:
        output.append(item[0])
print(*output, sep='\n')