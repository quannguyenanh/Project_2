import string
file_name = raw_input("Enter input file name: >")
print ("You want to search file: %s \n") % file_name

line_count = 1
word_pattern = []
word_dict_1 = {}
word_dict_2 = {}

for line in open(file_name):
	line = (line.strip()).split(" ")
	for word in line:
		word = string.lower(word)
		word_pattern.append([word, line_count])
		word_dict_1[word] = word_dict_1.get(word,0)+1
	line_count += 1
	
for key, value in sorted(word_pattern, key=lambda (k,v): (v,k), reverse=True):
	if (word_dict_1.get(value,0)):
		word_dict_1[value] = list([]).append(key)	
		print "%s: %s" % (key, value)