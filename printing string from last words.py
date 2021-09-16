
my_str =input()
newstr = my_str.split()
print(newstr)
output = newstr[-1::-1]
op = ' '.join(output)
print(f"'{op}'")
