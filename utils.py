def open_html(file):
    with open(file, 'r', encoding='UTF-8') as f:
        result = f.read()
        return result
