def remove_repeated(s):
	last, ans = ' ', ""
	for c in s:
		if(last != c):
			ans += c
		last = c
	return ans
	
def round_number(arr):
	max_val, max_idx = 0, -1
	for i in range(len(arr)):
		if(arr[i] % 10 == 0 and arr[i] > max_val):
			max_val, max_idx = arr[i], i
	return max_idx
	

print remove_repeated("aaaaa")
print remove_repeated("abccaaab")
print round_number([0,	5,	10,	15])
print round_number([1,	2,	3,	4,	5])
print round_number([10,	5,	30,	18]) 
