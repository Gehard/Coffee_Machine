row = abs(int(input()))
column = abs(int(input()))
if row in (1, 8) and column in (1, 8):
    print("3")
elif row in range(2, 8) and column in range(2, 8):
    print("8")
else:
    print("5")
