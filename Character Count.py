


#Character Count - this program will count the appearances of each character in a given string!

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
b = {}

for a in message:
	b.setdefault(a,0)
	b[a] = b[a]+1
	
print(b)
