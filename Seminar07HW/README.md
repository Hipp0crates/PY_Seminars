# **Чат-бот-словарь**  
## **Файлы**  
1. `dictionaries.py` - стартовые словари  
2. `functions.py` - набор функций  
3. `main.py` - по-умолчанию главный модуль  

## **Алгоритм**
1. При первичном запуске или отсутствии файла `words.json` грузится словарь из `dictionaries.py`.
2. При выходе или сохранении создаётся/перезаписывается файл `words.json`.
3. Есть возможность добавлять, удалять, сохранять и проверять свои познания путём перевода рандомного слова из созданного словаря.
4. Команды ввиде одного символа, при вводе непонятно чего в качестве команды ничего не происходит, просто показывет список доступных кнопок.
5. Также можно залипнуть на *"Магию Нехогвардс"*, выход из *магии* `CTRL+C`.