import slate3k as slate
# suitably reads tables and written text
import re

with open('pdf_folder/CSE 3 YEAR.pdf', 'rb') as f:
    doc = slate.PDF(f)

print(doc)

print(len(doc))

# strings=[]
# for x in doc:
#     for y in re.split(',|.|\n|:',x):
#         strings.append(y)
s="\n" # for splitting as sentence based on '.'
# s=" " # splitting of word based on " "

strings=re.split(s,doc[0])

print("After splitting based on '.'",strings)
print("Total lines extracted ",len(strings))

#prints the full document as a list of strings
#each element of the list is a page in the document

print(doc[0])
#prints the first p
print("Printing line by line")
for x in strings:
    print("line: ",x)

# create as function
# create a function to match similarity!!


