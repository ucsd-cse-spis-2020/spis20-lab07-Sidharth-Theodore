from _collections import defaultdict
import random
trainingData = "Yeah baby I like it like that You gotta believe me when I tell you I said I like it like that"


filepath = 'BEEMOVIE.txt'
file = open(filepath,'r')
fileString = file.read()
fileString.replace(" ","")
#print(fileString)




def train(string):
    '''takes in string of text, returns dictionary. Each key is a word from the string, value is a list of words that possibly follow each key in original string'''
    #splits string into list of words
    string_list = string.split()
    newDict = defaultdict(list)
    #iterates through string_list, adds each word as a key and adds word+1 as value
    for word in range(len(string_list)-1):
        newDict[string_list[word]].append(string_list[word+1])
    '''
    for key in newDict:
        print(str(key)+ " " + str(newDict[key]))
    '''
    
    return dict(newDict)

'''
def generate(model, firstWords, sens):
    generates specified number of sentences by drawing from random values of each key, starting with the firstWord as the first key.

    # model = dictionary
    # the key
    # numwords number of total words
    if sens == -1:
        return "."
    else:
        vals = model[firstWords[sens-1]]  # a list of values (possible continuing words) based on firstWord
        valsLength = len(vals)  # length of vals in order to find random index
        if valsLength > 1:
            ind = random.randint(0, valsLength - 1)  # using random method to find a random index
        elif valsLength == 1:
            ind = 0
        word = vals[ind]
        if valsLength == 0:
            word = '.'
        # print(word)
        return word + ' ' + generate(model, word,sens-1) + ' '
        
        elif ind == -1:
            # firstWords.remove(firstWords[0])
            return word + '.'+ generate(model, word, sens-1)
        
'''

def generateWords(model,firstWord,numWords):
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
        return firstWord +' '+ generateWords(model,word,numWords-1)+' '

def generateSen(model, firstWords, result = ""):
    #model = dictionary
    #firstWords = the words that start each sentence, user input
    #result = the final string that is a sum of all the words we add to it. The product we return
    resultList = result.split() #list of words in result

    
    if len(resultList) == 0:
        result += firstWords[0] + " "
        firstWords.pop(0)
        return generateSen(model,firstWords,result)

        #vals = model[firstWords[0]] #list of possible next words depending on the first word (Case: first iteration)
                
    '''if len(firstWords) == -1: #base case, when we are out of sentence starters
        result += '\n done \n'
        return result #return the result because function is over

    else:'''

       
    lastWord = resultList[len(resultList)-1]
    vals = model[lastWord] #list of possible next words depending on the first word (Case: not first iteration)
    valsLength = len(vals) # number of values we have to work with
    
    if valsLength > 1: #if multiple value possibilities, pick a random one
        ind = random.randint(0, valsLength - 1)  # using random method to find a random index
        word = vals[ind] #random word depending on random index
        
    elif valsLength == 1: # if there is only one word in vals
        word = vals[0] #setting word to the only word in the list

    if '.' in word:
        result+= ". \nending sentence...\n"
        try:
            word = firstWords[0]
            firstWords.pop(0)        
        except:
            result += '\n done \n'
            return result
    #print("added " + word)
    result += (word + " ")  
    return generateSen(model,firstWords,result)


e = train(fileString)
a = generateSen(e, ["Barry","Bee"])
print(a)
        
