import json

def main():
    my_dict = {
        'name': 'Joker',
        'age': 18,
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280}
        ]
    }

    try:
        with open('../file/data.json', 'w', encoding='utf-8') as fs:
            json.dump(my_dict, fs)
    except IOError as e:
        print(e)
    print('保存成功！')

if __name__ == "__main__":
    main()