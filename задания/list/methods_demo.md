## Методы списков
---
В первой строке вводятся элементы списка (числа).
Во второй - параметры *a*, *b*, *c*, *d*.
Выполните следующую последовательность действий с помощью методов списков и в качестве ответа выведите получившийся список.  
Порядок действий:  
1. Добавте в конец списка элемент *a*
2. С помощью срезов добавте в конец списка первую половину текущего списка
3. Удалите последний элемент
4. Удалите элемент с позиции *b*
5. На позицию *c* поставьте элемент *d*
6. Добавьте в конец списка индекс первого элемента в списке, который равен *a*

### Пример
---
Ввод
```
3 6 2 1 7 2 1 4
3 6 2 4
```
Вывод
```
3 6 4 2 1 7 2 4 3 3 6 2 0
```
Пояснение
```python
результат выполнения для каждого этапа
[3, 6, 2, 1, 7, 2, 1, 4, 3]
[3, 6, 2, 1, 7, 2, 1, 4, 3, 3, 6, 2, 1]
[3, 6, 2, 1, 7, 2, 1, 4, 3, 3, 6, 2]
[3, 6, 2, 1, 7, 2, 4, 3, 3, 6, 2]
[3, 6, 4, 2, 1, 7, 2, 4, 3, 3, 6, 2]
[3, 6, 4, 2, 1, 7, 2, 4, 3, 3, 6, 2, 0]
```