with open('quotes.txt', 'r', encoding = 'utf-8') as file:
    for data in file:
        print(data)
autor = input('Введите автора:')

with open('quotes.txt', 'a', encoding = 'utf-8') as file:
    file.write('\n(' + autor + ')')

with open('quotes.txt', 'r', encoding = 'utf-8') as file:
    for data in file:
        print(data)

while input('Хотите добавить ещё автора?') != 'нет':
    quote = input('Введите цитату:')
    autor = input('Введите автора:')
    with open('quotes.txt', 'a', encoding = 'utf-8') as file:
        file.write('\n' + quote)
        file.write('\n(' + autor + ')\n')
    
    with open('quotes.txt', 'r', encoding = 'utf-8') as file:
        data = file.read()
        print(data)
