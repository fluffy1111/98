sample1="I love sandwichis"
sample2="and cats"
def swapFileData():
    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'r') as a:
        data_a = a.read()
    with open(file2, 'w') as a:
        a.write(data_b)