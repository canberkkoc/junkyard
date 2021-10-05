with open("FILE_PATH_1") as f:
    dnslist = f.readlines()

with open("FILE_PATH_2") as f:
    changelist = f.readlines()


# Find different records of files and add them to a tuple
indexlist = []
for index,line in enumerate(dnslist):
    templine = line.split(" ")
    for l in changelist:
        templ = l.split(" ")
        if f'ap-{templ[1].rstrip()}' == templine[-1].rstrip():
            indexlist.append((index,f"# {line}",f'{templ[0]} ap-{templ[1]}'))

# Unpack tuple and iterate list reversely to protect indexes
for index,old,new in indexlist[-1::-1]:
    dnslist[index] = old
    dnslist.insert(index+1, new)


with open("FILE_TO_WRITE","w") as f:
   f.writelines(dnslist)
