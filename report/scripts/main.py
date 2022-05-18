import helpers
import latex


def get_complexity_table():
    methods = ['find_minimal_path', 'add_vertex']
    table = latex.LatexTable(
        2, caption='Оценка временной сложности методов класса Graph',
        caption_pos='bottom', label='complexity'
    )
    table.set_header('Метод', 'Оценка временной сложности')
    for method in methods:
        table.add_row(f'\\verb|{method}|', '$ O(n^2) $')
    return table.render()


neighbors_example = latex.LatexPicture(
    'neighbors_example',
    'Пример отображения соседей вершины графа',
)

sample_graph = latex.LatexPicture(
    'big_graph.dot',
    'Граф, использующийся в примерах',
    'sample_graph'
)


def make_example(num, src, tgt):
    pic = latex.LatexPicture(
        f'example_{num}',
        f'Пример выполнения при поиске пути {src} -> {tgt}'
    )
    s = (
        f'\\subsection*{{Пример {num}}}\n\n'
        f'Стартовый город: {src}\n\n'
        f'Конечный город: {tgt}\n\n'
        f'Пример выполнения представлен на рис. \\ref{{{pic.label}}}\n\n'
        f'{pic.render()}\n\n'
    )
    return s


def make_examples(*examples):
    s = ''
    for num, (src, tgt) in enumerate(examples, start=1):
        s += make_example(num, src, tgt)
    return s



def main():
    print(make_examples(
        ('Москва', 'Владимир'),
        ('Саранск', 'Воронеж'),
        ('Чебоксары', 'Иваново'),
        ('Иваново', 'Чебоксары'),
    ))


if __name__ == '__main__':
    main()
