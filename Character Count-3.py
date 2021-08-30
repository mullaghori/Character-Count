

#Character Count - this program will count the appearances of each character in a given string!

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
b = {}

for a in message:
	if a not in b:
		b[a] = 1
	else:
		b[a] += 1

print(b)