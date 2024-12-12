from multiprocessing import Pool
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break

filenames = [f'./file {number}.txt' for number in range(1, 5)]

#Линейный
#start = datetime.now()
#for i in filenames:
    #read_info(i)
#end = datetime.now()
#res = end - start
#print(res)

#Многопроцессный
if __name__ == '__main__':
    start = datetime.now()
    with Pool(4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    res = end - start
    print(res)