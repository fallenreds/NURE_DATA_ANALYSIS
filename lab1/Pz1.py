def csv_to_list(data: str):
    data = data.split(',')
    data[-1] = data[-1].replace('\n', '')
    return data


def list_to_csv(data: list):
    data[-1] = f'{data[-1]}\n'
    return ','.join(data)


def append_element(line, element):
    if not isinstance(line, list):
        line = csv_to_list(line)
    line.append(element)
    return list_to_csv(line)


def get_wine_cost(wine_data):
    data = csv_to_list(wine_data)
    w1, w2, w3, w4 = 0.35, 0.1, 0.15, 0.4

    wine = {
        'alcohol': float(data[3]),
        'density': float(data[4]),
        'ph': float(data[6]),
        'sugar': float(data[7]),
    }
    cost = w1 * wine['alcohol'] + w2 * wine['density'] + w3 * wine['ph'] + w4 * wine['sugar']
    data = append_element(data, cost)

    return data


with open('data_wine.csv', 'r') as data_wine, open('data_wine_copy.csv', 'w') as copy:
    headers = data_wine.readline()
    copy.writelines(append_element(csv_to_list(headers), 'Cost'))
    row_with_costs = (get_wine_cost(line) for line in data_wine)
    [copy.writelines(line) for line in row_with_costs]

with open('data_wine_copy.csv', 'r') as data_wine:
    data_wine.readline()
    wine = [csv_to_list(line) for line in data_wine]
    correct_cost = (float(line[-1]) for line in wine if line[1] == '6' and line[2] == 'white_wine')
    red_wine = (line[3] for line in wine if line[2] == 'red_wine' and float(line[3]) < 8)
    print(sum(correct_cost))
    print(list(set(red_wine)))
