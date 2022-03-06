class wordle:
    
    libraryRaw = open("./sgb-words.txt")
    library = libraryRaw.read()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    
    def __init__(self,found="*****",invalid="",partial=""):
        self.found = found
        self.validWords = []
        self.partial=[]
        self.update(invalid=invalid,partial=partial)
    
    def validate(self,word):
        for param in self.partial:
            if param[0] == word[param[1]] or param[0] not in word:
                #print(f"Failed on param,{word}.")
                return(False)
        if word in wordle.library:
            #print(f"Pass, {word}.")
            self.validWords.append(word)
            return(True)
        else:
            #print(f"Not in library, {word}.")
            return(False)
        
        
    def generateGuess(self,found=""):
        if found == "":
            found = self.found
        if "*" in found:
            for letter in self.alphabet:
                self.generateGuess(found=found.replace("*",letter,1))
        else:
            self.validate(found)
            
    def rankGuess(self,showProcess=False):
        if showProcess:
            print("Begin recursive word finder.")
        self.generateGuess(self.found)
        if showProcess:
            print("Word search done.  Ranking letters by frequency.")
            print(self.validWords)
        letterCount = {}
        ranking = {}
        for word in self.validWords:
            for i,letter in enumerate(word):
                if letter != self.found[i]:
                    try:
                        letterCount[letter]+=1
                    except:
                        letterCount[letter]=1
        if showProcess:
            print("Letter ranking complete. Beginning word ranking.")
            print(letterCount)
        for word in self.validWords:
            tmpValue = 0
            for i,letter in enumerate(word):
                if letter != self.found[i]:
                    tmpValue += letterCount[letter]
            ranking[word] = tmpValue
        print(sorted(ranking.items(),key=lambda item: item[1]))
    
            
    def update(self,found="",invalid="",partial=""):
        if found!="":
            self.found=found
        if invalid != "":
            for letter in invalid:
                self.alphabet = self.alphabet.replace(letter,"")
        if partial != "":
            for i,letter in enumerate(partial):
                if letter != "*":
                    self.partial.append([letter,i])
        self.validWords=[]
