import string
file_name = raw_input("Enter input file name: >")
print ("You want to search file: %s \n") % file_name
f = open (file_name)
line = f.read()
word_dict_1 = {}

#C1
for words in line.split():
	words = string.lower(words)
	word_dict_1[words] = word_dict_1.get(words,0)+1

for key, value in sorted(word_dict_1.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "%s: %s" % (key, value)
#C2	
line_count = 1
word_list = []
word_dict = {}
for line in open(file_name):
	line = (line.strip()).split(" ") #first strip for "\n" character then split line into words
	for word in line:
		word_list.append([string.lower(word), line_count])
	line_count += 1
word_list.sort()	
list_word = []
for i in range (0, len(word_list)):
	count = 1
	list_tmp = []
	list_tmp.append(word_list[i][1])
	for j in range (i+1, len(word_list)):		
		if word_list[j][0] == word_list[i][0]:
			count += 1	
			if word_list[j][1] != word_list[i][1]:
				list_tmp.append(word_list[j][1])			
	list_word.append([word_list[i][0], count, set(list_tmp)])
list_word.sort()
	
for word in list_word:
	t = set(word[2])
	list_tmp = [word[1], t]
	word_dict[word[0]] = list_tmp

new_list =[]
for i in word_dict:
	new_list.append([i, word_dict[i]])
	
new_list.sort()
sorted(new_list, key=lambda (k,v): (v,k), reverse=True)
for i in new_list:
	print "\n"
	print "%s %s" %(i[1][0], i[0]),
	for j in i[1][1]:
		print "%s" %j,