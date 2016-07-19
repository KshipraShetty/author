import pandas as pd
import random
fn=pd.read_csv("new.csv")
"""n=sum(1 for line in open("PaperAuthor.csv"))-1
s=15000
skip=sorted(random.sample(xrange(1,1+n),n-s))
fpa=pd.io.parsers.read_csv("PaperAuthor.csv",skiprows=skip)
"""
#PaperAutho.csv has 20000 papers
fpa=pd.io.parsers.read_csv("PaperAutho.csv")
a=[]
for index,row in fn.iterrows():
	#check if authorid is present in the paperauthor
	if (fpa['AuthorId']==row[0]).any() and (fpa['AuthorId']==row[1]).any():
		for ind,rows in fpa.iterrows():
			#find the corresponding paper ids
			if row[0]==rows[1]:
				id=rows[0]
				ro=fpa.loc[fpa['PaperId']==id]
				s=set(ro['Name'])
		#finding paperid for suspected duplicate author
		for i,rows in fpa.iterrows():	
			if row[1]==rows[1]:
				id=rows[0]
                        	ro=fpa.loc[fpa['PaperId']==id]
                        	sa=set(ro['Name'])
				#check if they have same co authors
				si=set(s)&(sa)
		#		print sa,s
				print "\n\n"
				#if they have same co authors then remove them from suspect list
				if si:
				#	print si
					si={}
					sa={}
					s={}
					a.append(index)
			else:
				continue
	else: 
		continue	
fn.drop(fn.index[a], inplace=True)			
					
					
		


