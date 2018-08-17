import re

def filter_punc(raw_string):
    filted = re.sub('''[\s+\.\!\/_,$%^*(+\"\']+|[+——！，
    。？?~、～@#￥%……&*【】ฅ>ω<ฅ)ノ｀Д)ノ（）『』≧≦)]+''',
    "",raw_string)
    return filted

def main():
    example = "Various punctutaions  \' . &*%R84dsfafhsd中文、。、234】"
    print(filter_punc(example))

if __name__ == '__main__':
    main()