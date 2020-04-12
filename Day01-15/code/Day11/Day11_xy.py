import time
import json
import requests

def main_readtxt():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())

    except FileNotFoundError:
        print('File not found')
    except LookupError:
        print('Unknown encode')
    except UnicodeDecodeError:
        print('Decoding error')
    finally:  # 总是执行代码块
        if f:
            f.close()


def main_readlines():
    """
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()
    """

    with open('致橡树.txt', encoding='utf-8') as f:
        lines = f.readlines()
        lines2 = [line.split('\n')[0] for line in lines if line!='\n']
    print(lines)
    print(lines2)


def main_json():
    mydict = {
        'name': 'XU Yun',
        'age': 28,
        'email': 'xuyun921017@163.com',
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('Data saved')

# dump-将Python对象按照JSON格式序列化到文件中
# dumps-将Python对象处理成JSON格式的字符串
# load-将文件中的JSON数据反序列化成对象
# loads-将字符串的内容反序列化成Python对象


def main_request():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    print(data_model)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main_request()
