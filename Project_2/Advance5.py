import difflib

s1 = "ptslddf"
s2 = "tsgldds"

print 's1 = %s, s2 = %s' %(s1, s2)

print 's1 == s2: \n', s1==s2

def str_2_list(str):
	ltmp = list(str)	
	return ltmp
	
def list_2_str(list_str):
	str = ''.join(list_str)
	return str
	
l1 = str_2_list(s1)
l2 = str_2_list(s2)

f = open('OUTPUT.TXT','a')

matcher = difflib.SequenceMatcher(None, l1, l2)

if matcher != []:
	f.write("Bien doi ngon lanh canh dao\n")

for tag, i1, i2, j1, j2 in matcher.get_opcodes():#reversed(matcher.get_opcodes()):

	if tag == 'delete':
		f.write('%s - xoa %s/%d -> ' % (list_2_str(l1), list_2_str(l1[i1:i2]), i2)),
		del l1[i1:i2]
		s1 = list_2_str(l1)
		f.write("%s\n" %s1)		

	elif tag == 'equal':
		pass
		
	elif tag == 'insert':
		f.write('%s - them %s/%d -> ' % (list_2_str(l1), list_2_str(l2[j1:j2]), i1)),
		l1[i1:i2] = l2[j1:j2]
		s1 = list_2_str(l1)
		s2 = list_2_str(l2)
		f.write("%s\n" %s1)
		
	elif tag == 'replace':
		f.write('%s - thay %s/%d/%s -> ' % (list_2_str(l1), list_2_str(l1[i1:i2]), i2, list_2_str(l2[j1:j2]))),
		l1[i1:i2] = l2[j1:j2]
		s1 = list_2_str(l1)
		s2 = list_2_str(l2)
		f.write("%s\n" %s1)
f.close()

print 's1 = %s, s2 = %s' %(s1, s2)

print 's1 == s2:', s1==s2