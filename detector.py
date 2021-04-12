from difflib import SequenceMatcher, Differ
import difflib

with open('C:/Users/Lenovo/Desktop/Jagjit_BTES.pdf', errors='ignore') as file1, open('C:/Users/Lenovo/Desktop/Jagjit_BTES.pdf',errors='ignore') as file2:
	file_1_data=file1.read().split()
	file_2_data=file2.read().split()
	print(list(file_1_data))
	print(list(file_2_data))
	a=list(file_1_data)
	b=list(file_2_data)
	'''dif=Differ()
	df= list(dif.compare(a,b))
	print(df)'''
	Similarity = SequenceMatcher(None, file_1_data, file_2_data).ratio()
	print(Similarity*100)

	a='MY name is Jagjit'
	b='abc adgvs'
	seq=difflib.SequenceMatcher(None,a.lower(),b.lower()).ratio()
	print(seq*100)