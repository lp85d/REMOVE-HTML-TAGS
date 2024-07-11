# Открываем файл 1.html для чтения
with open('1.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Удаляем HTML теги, оставляя только текст
clean_text = ''
tag = False
for char in html_content:
    if char == '<':
        tag = True
    elif char == '>':
        tag = False
    elif not tag:
        clean_text += char

# Записываем очищенный текст в файл 0.html
with open('0.html', 'w', encoding='utf-8') as file:
    file.write(clean_text)
