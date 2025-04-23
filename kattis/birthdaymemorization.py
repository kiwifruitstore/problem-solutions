#hi


inputlines = int(input())
print(inputlines)
inputlist = []
for i in range(inputlines):
    temp = str(input())
    listform = temp.split()
    inputlist.append(listform)
    

print(inputlist)

# input format : [name friendshipvalue XX/XX]