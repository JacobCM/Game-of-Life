import subprocess
import time
import sys
    
def nextGen(grid):
    n=len(grid)
    newGrid=[[0 for x in range(n)] for y in range(n)]

    for x in range(n):
        for y in range(n):
            liveFriends=countFriends(grid,x,y)
            if grid[x][y]==1:
                if liveFriends<2 or liveFriends>3:
                    newGrid[x][y]=0
                else:
                    newGrid[x][y]=1

            if grid[x][y]==0:
                if liveFriends==3:
                    newGrid[x][y]=1
                else:
                    newGrid[x][y]=0

    return newGrid

def countFriends(grid,x,y):
    n=len(grid)
    liveFriends=0
    if x>0 and y>0 and grid[x-1][y-1]==1:
        liveFriends+=1
    if x>0 and grid[x-1][y]==1:
        liveFriends+=1
    if x>0 and y<n-1 and grid[x-1][y+1]==1:
        liveFriends+=1
    if y>0 and grid[x][y-1]==1:
        liveFriends+=1
    if y<n-1 and grid[x][y+1]==1:
        liveFriends+=1
    if x<n-1 and y>0 and grid[x+1][y-1]==1:
        liveFriends+=1
    if x<n-1 and grid[x+1][y]==1:
        liveFriends+=1
    if x<n-1 and y<n-1 and grid[x+1][y+1]==1:
        liveFriends+=1
        
    return liveFriends

def readFile():
    file=open("/Users/jacobcm/Desktop/Xcode Projects/GoL/in.txt",'r')
    generations=int(file.readline())

    line=file.readline()
    grid=[]
    
    grid=[[0 for x in range(len(line)-1)] for y in range(len(line)-1)]
    
    i=0
    while len(line)!=0:
        for j in range(len(line)-1):
            grid[i][j]=int(line[j])
        i+=1
        line=file.readline()

    return (generations,grid)

def printToTerm(string):
    subprocess.call(["echo", string]) #Print out game to terminal

    #CHANGE VALUE BELOW TO CHANGE SPEED
    time.sleep(0.1) #Sleep for a bit

def printOut(gens): #prints to file
    out=open("/Users/jacobcm/Desktop/Xcode Projects/GoL/out.txt",'w')
    n=len(gens[0])
    line=""

    for i in range(len(gens)):
        out.write("Generation "+str(i+1)+'\n')
        for x in range(n):
                for y in range(n):
                    line+=str(gens[i][x][y])
                out.write(line+'\n')
                line=""

def main():
    terminalLines = subprocess.Popen(["tput", "cols"], stdout=subprocess.PIPE)
    terminalRows = subprocess.Popen(["tput", "lines"], stdout=subprocess.PIPE)
    columns = int(terminalLines.communicate()[0])
    rows = int(terminalRows.communicate()[0]) - 1

    (generations,grid)=readFile() #Get num of generations and intial stae from file
    gens=[]
    string=""
    
    for i in range(generations):
        string="Generation "+str(i+1)+'\n'
        for x in range(rows-1):
            for y in range(columns):
                if x>=len(grid) or y>=len(grid):
                    string+=" "
                elif grid[x][y]==0:
                    string+=" "
                else:
                    string += "\xE2\x96\x89"

        printToTerm(string)
        gens+=[grid]
        grid=nextGen(grid)
        
    printOut(gens)

def backupMain():
    (generations,grid)=readFile() #Get num of generations and intial stae from file
    gens=[]
    n=len(grid)
    
    for i in range(generations):
        gens+=[grid]
        grid=nextGen(grid)
        
    printOut(gens)

main()
