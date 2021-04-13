def counter(txt):
    line_list = list()
    for file in txt:
        with open(file, encoding='utf-8') as f:
            lines = f.readlines()
            line_dict = {'lines': len(lines), 'file': file}
            line_list.append(line_dict)
    low_high_list = sorted(line_list, key=lambda i: i['lines'])
    return low_high_list


def resulting():
    with open('result.txt', 'w') as fw:
        low_high_list = counter(documents)
        for doc in low_high_list:
            file_str = f'{doc["file"]}\n'
            fw.write(file_str)
            line_str = f'{doc["lines"]}\n'
            fw.write(line_str)
            fw.write('\n')
    return


if __name__ == '__main__':
    documents = ['1.txt', '2.txt', '3.txt']
    print(counter(documents))
    print(resulting())
