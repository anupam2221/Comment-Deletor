#(C)- Anupam Kumar
import os
import time
with open("initial.py/c/cpp") as f:
    lines = f.readlines()
    lines = [l for l in lines if "ROW" in l]
    with open("out.txt", "w") as f1:
        f1.writelines(str(lines))
with open('current.txt','w')as f:
	for line in f.readline():
		f=0
		for word in line.split(' '):
			for letter in word.split(''):
				if letter=='#':
					f=1
					for fix in range(letter,'\0'):
						fix=''
				if f==1:
					break
			if f==1:
				break
os.rename('current','initial')
