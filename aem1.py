

input_file = []
data = []
with open("kroA100.txt", 'r') as instance:
    infile_tasks = instance.readlines()
    infile_tasks = [line[:].replace('\n',"").split(' ') for line in infile_tasks][1:]




print(infile_tasks)
