import random
import copy
import string
directions = {
	0:[1,0],
	1:[1,-1],
	2:[0,-1],
	3:[-1,-1],
	4:[-1,0],
	5:[-1,1],
	6:[0,1],
	7:[1,1]

}
F = open('template.txt', 'r')
contents = F.read()
F.close()
contents  = contents.split("\n")

sizex = int(contents[1])
sizey = int(contents[0])
words = contents[2:len(contents)]

def addlists(a,b):
	newlist = []
	for x in range(0,len(a)):
		newlist.append(a[x] + b[x])
	return newlist

def generateempty(y,x):
	empty = []
	for a in range(0,x):
		empty.append([])
		for b in range(0,y):
			empty[a].append("/")
	return empty
def reorder(lis):
	counter = 0
	while counter < 31:
		for item in lis:
			if len(item) > counter:
				lis.insert(0, lis.pop(lis.index(item)))
		counter +=1
	return lis
def writeword(cs, word, pos, dirt):
	testlist = copy.deepcopy(cs)
	checker = True
	for x in range(0,len(word)):
		scaleddir = [n*x for n in dirt]
		cpos = addlists(pos, scaleddir)
		#testlist.append(cpos)
		if cs[cpos[0]][cpos[1]] == "/" or cs[cpos[0]][cpos[1]] == word[x]:
			testlist[cpos[0]][cpos[1]] = word[x]
		else:
			checker = False
			break
	if checker:
		thingtoreturn = testlist
	else:
		thingtoreturn = "no"
	return (thingtoreturn)





def fitword(cs, word, xcheck, ycheck):
	
	while True:
		counter = 0
		indexthing = random.randint(0,7)
		direction = directions[indexthing]
		if xcheck:
			direction[0] = 0
		if ycheck:
			direction[1] = 0

		if direction[0] == -1:
			x = random.randint(len(word)-1, len(cs)-1)
		elif direction[0] == 1:
			x = random.randint(0, (len(cs) - len(word)))
		else:
			x = random.randint(0, len(cs)-1)
		if direction[1] == -1:
			y = random.randint(len(word)-1, len(cs[0])-1)
		elif direction[1] == 1:
			y = random.randint(0, (len(cs[0]) - len(word)))
		else:
			y = random.randint(0, len(cs[0])-1)
		startloc = [x,y]
		newsearch = writeword(cs, word, startloc, direction)
		if newsearch != "no":
			break
		counter += 1
		if counter >= 1000:
			print("COUNTER")
			return False
	return newsearch
blank = generateempty(sizey,sizex)
prevtest = copy.deepcopy(blank)

words2 = reorder(words)
amount = 0
for item in words2:
	for letter in item:
		amount += 1
if amount >= sizex*sizey:
	test = "not possible"
else:
	for item in words2:
		checkx = False
		checky = False
		if len(item) > sizex:
			print(item, "to long for x")
			checkx = True
		elif len(item) > sizey:
			print(item, "too long for y")
			checky = True
		if len(item) > sizex and len(item) > sizey:
			print("not possible")
			test = "not possible"
			break
		test = fitword(prevtest, item, checkx, checky)
		if not test:
			break
	prevtest = copy.deepcopy(test)
if test == "not possible":
	print("that is literally impossible")
else:
	for item in test:
		for item2 in item:
			if item2 == "/":
				print (random.choice(string.ascii_lowercase) + " ", end = "")
			else:
				print (item2 + " ", end = "")
		print("")

