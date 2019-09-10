# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

#output : Numbers: 4 5 6

print("{0}{1}{0}".format("abra", "cad"))

a = "{x}, {y}".format(x=5, y=12)
print(a) # 5,12

str="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)