
class finder():
    
    
    
    def __init__(self,src_loc):
        self.list = open(src_loc+"/list.txt").read().replace(" ","").split("\n")
        self.puzzle = open(src_loc + "/puzzle.txt").read().split("\n")
        self.height = len(self.puzzle)
        self.width = len(self.puzzle[0])
        self.found = []
        self.solve()
        
    def rotate90(self):
        vlines = []
        for i in range(0,len(self.puzzle[0])):
            vline = ""
            for hline in self.puzzle:
                vline+=hline[i]
            vlines.append(vline)
        self.puzzleVert = vlines
        
    def rotate45(self):
        fwd = ["" for i in range(0,self.height+self.width)]
        bck = ["" for i in range(0,self.height+self.width)]
        for i in range(0,self.height):
            for j in range(0,self.width):
                fwd[i+j]+=self.puzzle[j][i]
                bck[i+j]+=self.puzzle[self.height-i-1][j]
        self.puzzleFwd = fwd
        self.puzzleBck = bck

    def check(self,word,puzzle,which):
        found=False
        for i,line in enumerate(puzzle):
            if word in line:
                self.solutions.append([word,i,f"{which}+",line.index(word)])
                found=True
            elif word[::-1] in line:
                self.solutions.append([word,i,f"{which}-",line.index(word[::-1])])
                found=True 
        return(found)

    def solve(self):
        self.solutions = []
        self.rotate45()
        self.rotate90()
            
        for word in self.list:
            found = False
            found = self.check(word,self.puzzle,"h")
            if not found:
                found = self.check(word,self.puzzleVert,"v")
            if not found:
                found = self.check(word,self.puzzleFwd,"f")
            if not found:
                found = self.check(word,self.puzzleBck,"b")
            if not found:
                print(f"unable to locate {word}")
    
    def showAnswers(self):
        for sol in self.solutions:
            print(sol)
            
        for sol in self.solutions:
            found = [["." for j in range(0,self.width)] for i in range(0,self.height)]
            
            y = sol[1]
            x = sol[3]
            
            if "h" in sol[2]:
                if "+" in sol[2]:
                    for i,letter in enumerate(sol[0]):
                        found[y][x+i] = letter
                else:
                   for i,letter in enumerate(sol[0][::-1]):
                        found[y][x+i] = letter
                        
            if "v" in sol[2]:
                if "+" in sol[2]:
                    for i,letter in enumerate(sol[0]):
                        found[x+i][y] = letter
                else:
                   for i,letter in enumerate(sol[0][::-1]):
                        found[x+i][y] = letter 
                        
            if "f" in sol[2]:
                if y>self.height-1:
                    _y = self.height-1
                    _x = y-(self.height-1)
                else:
                    _y = y
                    _x = 0
                _x+=x
                _y-=x
                
                if "+" in sol[2]:
                    for i,letter in enumerate(sol[0]):
                        found[_y-i][_x+i] = letter
                else:
                   for i,letter in enumerate(sol[0][::-1]):
                        found[_y-i][_x+i] = letter 
                        
            if "b" in sol[2]:
                if y>self.width-1:
                    _y = (self.height-1)*2 - y
                    _x = self.height-1
                else:
                    _x = y
                    _y = self.height-1
                _x-=x
                _y-=x
                
                if "+" in sol[2]:
                    for i,letter in enumerate(sol[0]):
                        found[_y-i][_x-i] = letter
                else:
                   for i,letter in enumerate(sol[0][::-1]):
                        found[_y-i][_x-i] = letter 
            
            newGrid = [" "+"_"*self.width+" "]
            for line in found:
                newString = "|"
                for letter in line:
                    newString+=letter
                newString+="|"
                newGrid.append(newString)
                #print(line,newString)
            newGrid.append(newGrid[0])
            newGrid[-1] = "|"+newGrid[-1][1:-1]+"|"
            
            for line in newGrid:
                print(line)
            x = input("Press any key to continue...")
            

