>From the book: Automate the Boring Stuff with Python. Writer: Al Sweigart

# Character Count

It's a practice project for python beginners.

***👉 No.1 Write a short program `characterCount.py` that counts the number of occurrences of each letter in a given string `message = 'It was a bright cold day in April, and the clocks were striking thirteen.'`.***

*HINT: The program should loop over each character in the `message` variable’s string, counting how often each character appears.*
 
The `setdefault()` method call ensures that the `key` is in the `count dictionary` (with a default `value` of `0`), so the program doesn’t throw a `KeyError` error.

**When you run your program, the output should look like this:**
```
{' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5, 'd': 3, 'g': 2, 'i': 6, 'h': 3, 
'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p': 1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1}
```

From your output, you should be able to see that the lowercase letter `c` appears `3 times`, the `space` character appears `13` times, and the uppercase letter `A` appears `1` time. This program should work with no matter what string is inside the message variable, even if the string is `millions of characters long`!


