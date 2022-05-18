from graph import load_graph, export_graph

examples = [
    ('Москва', 'Владимир'),
    ('Саранск', 'Воронеж'),
    ('Чебоксары', 'Иваново'),
    ('Иваново', 'Чебоксары'),
]


def run_example(graph, a, b):
    path, value = graph.find_minimal_path(a, b)
    print(f'Минимальный путь от города "{a}" до города "{b}":')
    print(' -> '.join(path), '=', value)


def main():
    graph = load_graph('data/graph_big.txt')
    for example in examples:
        run_example(graph, *example)


if __name__ == '__main__':
    main()