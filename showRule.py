import pickle

dataset = 'C_P_OS'
split = 'cv3-0'

name = dataset + '_' + split

def showRule(name):
    with open('obj/bio_' + name + '.pkl','rb') as f:
        bioList = pickle.load(f) #[[(0, 5, 0.5, True)],[(0, 2, 0.5, False)]]
        i = 0
        while i < len(bioList):
            if len(bioList[i]) == 1: printSingleRule(bioList[i], i) 
            else: extractRule(bioList[i], i)
            i += 1

def extractRule(item, c):
    i = 0
    string = 'R' + str(c) +': '
    while i < len(item):
        if (item[i][3] == True): op = '>'
        else: op = '<='
        string = string + 'feature:' + str(item[i][1]) + ' ' + op + ' ' + str(item[i][2])
        if (i != len(item) - 1): string = string + ' and '
        i += 1
    string = string + ' => 1'
    print(string)

def printSingleRule(item, c):
    if (item[0][3] == True): op = '>'
    else: op = '<='
    print('R', c,':')
    print('if Neuron:', str(item[0][1]), op, str(item[0][2]) ,' => 1')

def showRuleBnn(list):
    bnnList = list #[[(0, 5, 0.5, True)],[(0, 2, 0.5, False)]]
    i = 0
    while i < len(bnnList):
        if len(bnnList[i]) == 1: printSingleRuleBnn(bnnList[i], i) 
        else: extractRuleBnn(bnnList[i], i)
        i += 1

def showBNN(name):
    with open('obj/BNN_' + name + '.pkl','rb') as f:
        bnnDict = pickle.load(f)
        #bnnDict = {(4, 1, 0.5, True): [[(3, 0, -0.27577212452888, False)]], (3, 0, -0.27577212452888, False): [[(2, 2, -0.27173203229904, False)]], (2, 2, -0.27173203229904, False): False}
        for x, y in bnnDict.items():
            print('for Neuron',x[1],'in Layer', x[0])
            if showRuleBnn(y) == None: print('')
            else: print(showRuleBnn(y))
            print('')

def printSingleRuleBnn(item, c):
    if (item[0][3] == True): op = '>'
    else: op = '<='
    print('R', c,':')
    print('if Neuron:', str(item[0][1]), op, str(item[0][2]))

def extractRuleBnn(item, c):
    i = 0
    string = 'R' + str(c) +': '
    while i < len(item):
        if (item[i][3] == True): op = '>'
        else: op = '<='
        string = string + 'f:' + str(item[i][1]) + ' ' + op + ' ' + str(item[i][2])
        if (i != len(item) - 1): string = string + ' and '
        i += 1
    print(string)


#showRule(name)
print('')
print('BNN intermediate rules:')
print('')
showBNN(name)
