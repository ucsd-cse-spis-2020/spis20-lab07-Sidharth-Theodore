from _collections import defaultdict
import random
trainingData = "Yeah baby I like it like that You gotta believe me when I tell you I said I like it like that"

def train(string):
    string = string.split()
    newDict = defaultdict(list)
    for word in range(len(string)-1):
        newDict[string[word]].append(string[word+1])
    '''
    for key in newDict:
        print(str(key)+ " " + str(newDict[key]))
        pass
    '''
    return dict(newDict)



def generate(model,firstWord,numWords):
    #model = dictionary
    #the key
    #numwords number of total words
    if numWords == 0:
        return ""
    else:
        vals = model[firstWord]
        #print(vals)
        valsLength = len(vals)
        ind = random.randint(0,valsLength-1)
        word = vals[ind]
        #print(word)
        return firstWord +' '+ generate(model,word,numWords-1)+' '


e = train(trainingData)
a = generate(e, "I", 8)
print(a)
        
