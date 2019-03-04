def read_file(filename): 
    text_file = open("motion/" + filename + ".txt", "r")
    mot= []
    for val in text_file.read().split('\n'):
        inpos=[]
        for num in val.split(' '):
            inpos.append(int(num))
        mot.append(inpos)
    text_file.close()
    return mot



