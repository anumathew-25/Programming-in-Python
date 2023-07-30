data="myprogram.exe"
print(len(data))
print(data[1:10:2])
print(data[::-1])
print(data[:-1:2])
print(data[5:9])
print(data[-4:])
print(data[len(data)//2])
for ch in range(len(data)-1,-1,-1):
    print(data[ch])
