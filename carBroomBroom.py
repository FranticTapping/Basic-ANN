filee = open("world.txt")

worldData = filee.readlines()
filee.close()


for i in range(0,len(worldData)):
    worldData[i] = list(worldData[i])


pos = [0,1]

display = ""
for column in range(0,len(worldData)):
    for row in range(0,len(worldData[column])):
        if column == pos[1] and row == pos[0]:
            display += "@"
        else:    
            display += worldData[column][row]

print(display)