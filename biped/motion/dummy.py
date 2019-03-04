text_file = open("stand.txt", "r")
mot= []
for val in text_file.read().split(','):
    mot.append(int(val))

for x in mot:
    print(x)

# print(lines)
# text_file.close()
# text_file = open("stand.txt", "r")
# time = text_file.read().split('|')
# print(time)
