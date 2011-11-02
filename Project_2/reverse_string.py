import string
#jeans VT 159-161 HHT
s = raw_input("Input string:> ")

#C1
def reverse_str_1(str):
	new_str = ""
	list_tmp = []
	for i in range(0,len(str)):
		list_tmp.append(str[len(str) - i-1])
	new_str = ''.join(list_tmp)
	return new_str
#C2
def reverse_str_2(str):	
	list_tmp = list(str)
	list_tmp.reverse()
	s = ''.join(list_tmp)
	return s
	
# Reverse
new_s_1 = reverse_str_1(s)
print new_s_1
new_s_2 = reverse_str_2(s)
print new_s_2

