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

e = train(fileString)
a = generate(e, "Barry" ,10)
print(a)
        
