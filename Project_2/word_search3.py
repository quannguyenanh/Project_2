file_name = raw_input("Enter input file name: >")
print ("You want to search file: %s \n") % file_name
word_list = []
for i, line in enumerate (open(file_name)):
	line = (line.strip()).split(" ") #first strip for "\n" character then split line into words
	line_count = str(i+1)
	for word in line:
		for elm in word_list:
			if elm[0] == word: #first appear in word list
				elm[1] += 1
				if line_count not in elm[2]:
					elm[2].append(line_count)
				break
		else:
			word_list.append( [ word.lower(), 1, [line_count] ] )
for key, value, index in sorted(word_list, key=lambda (k,v,i):(v,k,i), reverse=True):
	print "%s %s" %(value, key),
	for i in index:
		print i,
	print "\n"		
