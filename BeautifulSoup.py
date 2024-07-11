from bs4 import BeautifulSoup

# Открываем файл 1.html для чтения
with open('1.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Используем метод get_text для извлечения текста без тегов
clean_text = soup.get_text()

# Записываем очищенный текст в файл 0.html
with open('0.html', 'w', encoding='utf-8') as file:
    file.write(clean_text)
