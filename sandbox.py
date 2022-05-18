import json
import random
import sys

def printd(d):
    print(json.dumps(d, indent=4))

_matrix = [
    [0, 156, 0, 0, 246, 0, 184, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 462, 0, 0, 171, 0, 157, 0, 363],
    [156, 0, 323, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 323, 0, 151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 151, 0, 0, 545, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [246, 0, 0, 0, 0, 174, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 545, 174, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [184, 0, 0, 0, 0, 0, 0, 83, 224, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 192, 0, 0, 0],
    [0, 0, 0, 0, 100, 0, 83, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 224, 0, 0, 209, 0, 0, 0, 0, 217, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 209, 0, 116, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 116, 0, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 180, 0, 157, 251, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 157, 0, 342, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 251, 342, 0, 111, 208, 0, 0, 0, 0, 0, 382, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 217, 0, 0, 0, 0, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 208, 0, 0, 335, 462, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 335, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [462, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 462, 0, 0, 212, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 212, 0, 135, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 135, 0, 174, 0, 0, 0, 0],
    [171, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 174, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 192, 0, 0, 0, 0, 0, 0, 382, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [157, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 171, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 171, 0, 0],
    [363, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

_vertices = [
    'Москва',
    'Тверь',
    'Великий Новогород',
    'Санкт-Петербург',
    'Ярославль',
    'Вологда',
    'Владимир',
    'Иваново',
    'Нижний Новгород',
    'Чебоксары',
    'Казань',
    'Ульяновск',
    'Самара',
    'Пенза',
    'Саранск',
    'Саратов',
    'Волгоград',
    'Воронеж',
    'Курск',
    'Орёл',
    'Тула',
    'Резань',
    'Калуга',
    'Брянск',
    'Смоленск',
]


def gen_value(a=0, b=200, default=0, default_probability=50):
    value = random.randint(a, b)
    dp = random.randint(0, 100)
    return value if dp < default_probability else default


def randomize_matrix(m):
    for row, row_v in enumerate(m):
        for col, col_v in enumerate(row_v):
            if random.randint(0, 100) < 2:
                m[row][col] = random.randint(0, 200)
    return m


def gen_matrix(vertices):
    matrix = []
    for row in range(len(vertices)):
        matrix_row = []
        for col in range(len(vertices)):
            new_value = gen_value(15) if row != col else 0
            matrix_row.append(new_value)
        matrix.append(matrix_row)
    return matrix


def make_graph_data(matrix, vertices):
    data = ''
    for row, row_v in enumerate(vertices):
        for col, col_v in enumerate(vertices):
            fwd_value = matrix[row][col]
            bwd_value = matrix[col][row]
            if fwd_value == 0 and bwd_value == 0:
                continue
            fwd_value, bwd_value = fwd_value or 'N/A', bwd_value or 'N/A'
            data += f'{row_v};{col_v};{fwd_value};{bwd_value}\n'
    return data

def write_graph_data(data: str, data_file: str):
    with open(data_file, 'w') as f:
        f.write(data)


def main():
    if len(sys.argv) > 1:
        save_file = sys.argv[1]
    else:
        save_file = 'graph.txt'
    
    v = _vertices
    matrix = randomize_matrix(_matrix)
    data = make_graph_data(matrix, v)
    write_graph_data(data, save_file)
    print(f'Generated graph with {len(v)} vertices and saved it to {save_file}')
    

if __name__ == '__main__':
    main()
