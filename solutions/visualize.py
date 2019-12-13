from math import ceil

OFFSET = 1000
TASK_COUNT = 1150
COLUMNS = 25
ROWS = ceil(TASK_COUNT/COLUMNS)

def generate_html(pids_set):
    tab = '\t'
    rows = []
    for r in range(ROWS):
        columns = []
        for c in range(COLUMNS):
            pid = (OFFSET + r*COLUMNS + c)
            exist = pid in pids_set
            color = 'green' if exist else 'lightgray'
            column = f'{tab*2}<td style="color:{color}">{pid}</td>'
            columns.append(column)
        row = '\n'.join(columns)
        row = f'{tab}<tr>\n{row}\n{tab}</tr>'
        rows.append(row)
    html = '\n'.join(rows)
    html = f'<table>\n{html}\n</table>'
    html = f'<p>Got: {len(pids_set)}</p>\n{html}'
    return html

def write(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

def visualize(pids_set):
    write('out.html', generate_html(pids_set))
