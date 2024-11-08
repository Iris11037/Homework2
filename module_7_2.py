def custom_write(file_name, strings):
    f = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    num = 0
    byte = f.seek(0)
    for string_ in strings:
        f.write(string_ + '\n')
        num += 1
        key = (num, byte)
        strings_positions[key] = string_
        byte = f.tell()
    f.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
