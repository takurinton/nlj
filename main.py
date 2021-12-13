def nlj():
    table1 = [
        {
            'username': 'takurinton',
            'status': 1,
        },
        {
            'username': 'hoge',
            'status': 2,
        },
        {
            'username': 'fuga',
            'status': 2,
        },
        {
            'username': 'piyo',
            'status': 3,
        }
    ]

    table2 = [
        {
            'status': 1,
            'name': 'die',
        },
        {
            'status': 2,
            'name': 'fine',
        },
        {
            'status': 3,
            'name': 'tired',
        }
    ]

    result = []
    for t1 in table1:
        for t2 in table2:
            if t1['status'] == t2['status']:
                result.append({
                    'username': t1['username'],
                    'status': t1['status'],
                    'status_name': t2['name'],
                })

    print(result)

if __name__ == '__main__':
    nlj()
