with open('1.py', 'w') as file:
    file.write('exam is done')

# Відкриття файлу для читання
with open('2.py', 'r') as file:
    content = file.read()
    print(content)