##### write
print('# write')
with open('./python_file_IO.txt', 'w') as f:
    f.write('hello world!\n')
    f.write('This is Python File IO Test!\n')
    f.write('Make python_file_IO.txt!')
#####

print('==========')

##### read1
print('# read1')
f = open('./python_file_IO.txt', 'r')

i = 0
while True:
    i += 1
    line = f.readline()
    if not line:
        break
    print(f'This is {i}th line : {line}')
    
f.close()
#####

print('==========')

##### read2
print('# read2')
f = open('./python_file_IO.txt', 'r')

lines = f.readlines()
print(f'This is readlines : {lines}')
print(f'Type : type(lines)')
i = 0
for line in lines:
    i += 1
    print(f'line{i} : {line}')
f.close()
#####

print('==========')

##### read3
print('# read3')
f = open('./python_file_IO.txt', 'r')

descript = f.read()
print()
print(descript)
f.close()
#####

print('==========')

##### add
print('# add')
with open('./python_file_IO.txt', 'a') as f:
    f.write('This is additional contents!')
