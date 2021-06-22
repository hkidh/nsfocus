
# read file
data = []
with open('tp.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
print('Policy 共有' + str(len(data)) + '行資料')

# write file
with open('tp.csv', 'w') as f:
    for line in data:
        if line == '!':
            continue
        if len(line) != 0:
            if 'protect zone' in line:
                    f.write(line + '\n')

# filter Policy
csv = []
one = []
with open('tp.csv', 'r') as f:
    for line in f:
        csv.append(line.split(' '))
    for line in csv:
        one.append(line[2])
    x = sorted(set(one))
    for line in x:
        print(line)

with open('tp.csv', 'r') as f:
    print('---------------------')
    gn = input('請輸入 Group_name: ')
    for line in f:
        if gn in line:
            if '-group_ip' in line:
                continue
            print(line.strip())
        


