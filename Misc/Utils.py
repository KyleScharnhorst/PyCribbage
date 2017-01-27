
# This module contains all utility functions

# Recreation of ANSII C's atoi function.
# Will create an int from a string even if there are is alpha characters in the string.
# E.g.:
# asd -> 0
# 10c -> 10
# 10c1 -> 10
# 765 -> 765
def atoi(a_str):
	result = ""
	for i in range(len(a_str)):
		a_char = a_str[i]
		if a_char >= '0' and a_char <= '9':
			result = result + a_char
		else:
			break;
	if len(result) > 0:
		return int(result)
	else:
		return 0	 

class Debug(object):
    _Debugging = False
    
    @classmethod
    def Print(class_info, *args):
        if Debug._Debugging:
            print(*args)