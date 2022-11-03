# Задача 2. В первой строке файла находится информация об ассортименте мороженого,
# во второй - информация о том, какое мороженное есть на складе.
# Выведите название того товара, который закончился.
def readFile(nameFile):
    data = open(nameFile, encoding = 'utf-8')
    iceCream = data.read()
    data.close()
    return iceCream
def comparisonString():
    list = readFile('iceCream.txt')[0:-1].split('\n')
    range = list[0].split()
    range = set(range)
    stock = list[1].split()
    stock = set(stock)
    print('Мороженое в ассортименте: ', range)
    print('Мороженое на складе: ', stock)
    print('Закончилось мороженое: ', range.difference(stock))

comparisonString()
