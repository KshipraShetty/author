import pandas as pd
import numpy as np
import re
import random
filen="author.csv"
#randomly pick 5000 authors 
n=sum(1 for line in open(filen))-1
s=5000
skip=sorted(random.sample(xrange(1,1+n),n-s))
fl=pd.io.parsers.read_csv(filen,skiprows=skip)
print fl.Name
#remove the blank records
fl=fl[fl.Name.notnull()]
fl=fl.reset_index()
#select the names
names=fl.Name
#select the ids
id=fl.Id
#new dataframe to store the suspects
df=pd.DataFrame(columns=list('AB'))
for i in range(0,len(names)):
	nam=names[i].split(" ")
	na=""
	#to check if strating letter of each word matches and in order
	for k in range(0,len(nam)):
		na=na+"(.*)"
		na=na+nam[k][0]
	for j in range(i+1,len(names)):
		if (re.match(na,names[j])):
			#find the common alphabets
			a=set(names[i]).intersection(names[j])
			a.discard(' ') 
			a.discard('.')
			a.discard(nam[0][0])
			#a.discard(nam[1][0])
			#not much difference between the number of words
			if len(a)>6 and abs(len(names[i].split(" "))-len(names[j].split(" ")))<2:
				df2=pd.DataFrame([[id[i],id[j]]],columns=list('AB'))
				df=df.append(df2,ignore_index=True)
			else:
				continue

print df
#write the suspects into a new file
df.to_csv("new.csv",index=False,cols=('A','B'))

