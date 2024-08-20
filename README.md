# Репозиторий курса "Разработка интернет приложений" в бакалавриате ИУ5 МГТУ им. Баумана, 5 семестр

## Лабораторная работа №1 - Основные конструкции языка Python

Задание:
1. Программа должна быть разработана в виде консольного приложения на языке Python.
2. Программа осуществляет ввод с клавиатуры коэффициентов А, В, С, вычисляет дискриминант и корни уравнения (в зависимости от дискриминанта).
3. Если коэффициент А, В, С введен некорректно, то необходимо проигнорировать некорректное значение и ввести коэффициент повторно.
4. Первой строкой программа выводит ФИО разработчика и номер группы.
5. ДОПОЛНИТЕЛЬНОЕ ТРЕБОВАНИЕ. Коэффициенты А, В, С задаются в виде параметров командной строки. Если они не указаны, то вводятся с клавиатуры в соответствии с пунктом 2. Проверка из пункта 3 в этом случае производится для параметров командной строки без повторного ввода с клавиатуры.

## Лабораторная работа №2 - Объектно-ориентированные возможности языка Python

Задание::
1. Необходимо создать виртуальное окружение и установить в него хотя бы один внешний пакет с использованием pip.
2. Необходимо разработать программу, реализующую работу с классами. Программа должна быть разработана в виде консольного приложения на языке Python 3.
3. Все файлы проекта (кроме основного файла main.py) должны располагаться в пакете lab_python_oop.
4. Каждый из нижеперечисленных классов должен располагаться в отдельном файле пакета lab_python_oop.
5. Абстрактный класс «Геометрическая фигура» содержит абстрактный метод для вычисления площади фигуры. Подробнее про абстрактные классы и методы Вы можете прочитать здесь.
6. Класс «Цвет фигуры» содержит свойство для описания цвета геометрической фигуры. 
7. Класс «Прямоугольник» наследуется от класса «Геометрическая фигура». Класс должен содержать конструктор по параметрам «ширина», «высота» и «цвет». В конструкторе создается объект класса «Цвет фигуры» для хранения цвета. Класс должен переопределять метод, вычисляющий площадь фигуры.
8. Класс «Круг» создается аналогично классу «Прямоугольник», задается параметр «радиус». Для вычисления площади используется константа math.pi из модуля math.
9. Класс «Квадрат» наследуется от класса «Прямоугольник». Класс должен содержать конструктор по длине стороны. Для классов «Прямоугольник», «Квадрат», «Круг»:
    a. Определите метод "repr", который возвращает в виде строки основные параметры фигуры, ее цвет и площадь. Используйте метод format - https://pyformat.info/
    b. Название фигуры («Прямоугольник», «Квадрат», «Круг») должно 
задаваться в виде поля данных класса и возвращаться методом класса.
10. В корневом каталоге проекта создайте файл main.py для тестирования Ваших классов (используйте следующую конструкцию - https://docs.python.org/3/library/__main__.html). Создайте следующие объекты и выведите о них информацию в консоль (N - номер Вашего варианта по списку группы):
    a. Прямоугольник синего цвета шириной N и высотой N.
    b. Круг зеленого цвета радиусом N.
    c. Квадрат красного цвета со стороной N.
    d. Также вызовите один из методов внешнего пакета, установленного с использованием pip.



## Лабораторная работа №3 - Функциональные возможности языка Python

Задание лабораторной работы состоит из решения нескольких задач.
Файлы, содержащие решения отдельных задач, должны располагаться в пакете lab_python_fp. Решение каждой задачи должно располагаться в отдельном файле.
При запуске каждого файла выдаются тестовые результаты выполнения соответствующего задания.

### Задача 1 (файл field.py)
Необходимо реализовать генератор field. Генератор field последовательно выдает значения ключей словаря. Пример:
```
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]
```
`field(goods, 'title')` должен выдавать `'Ковер', 'Диван для отдыха'`

`field(goods, 'title', 'price')` должен выдавать `{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха'}`

* В качестве первого аргумента генератор принимает список словарей, дальше через *args генератор принимает неограниченное количествово аргументов.

* Если передан один аргумент, генератор последовательно выдает только значения полей, если значение поля равно None, то элемент пропускается.

* Если передано несколько аргументов, то последовательно выдаются словари, содержащие данные элементы. Если поле равно None, то оно пропускается. Если все поля содержат значения None, то пропускается элемент целиком.

Шаблон для реализации генератора:
```
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор 
```

### Задача 2 (файл gen_random.py)
Необходимо реализовать генератор `gen_random(количество, минимум, максимум)`, который последовательно выдает заданное количество случайных чисел в заданном диапазоне от минимума до максимума, включая границы диапазона. Пример:

`gen_random(5, 1, 3)` должен выдать 5 случайных чисел в диапазоне от 1 до 3, например `2, 2, 3, 2, 1`

Шаблон для реализации генератора:

```
# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки
def gen_random(num_count, begin, end):
    pass
    # Необходимо реализовать генератор
``` 

### Задача 3 (файл unique.py)
Необходимо реализовать итератор `Unique(данные)`, который принимает на вход массив или генератор и итерируется по элементам, пропуская дубликаты.

Конструктор итератора также принимает на вход именованный bool-параметр ignore_case, в зависимости от значения которого будут считаться одинаковыми строки в разном регистре. По умолчанию этот параметр равен False.

При реализации необходимо использовать конструкцию **kwargs.

Итератор должен поддерживать работу как со списками, так и с генераторами.

Итератор не должен модифицировать возвращаемые значения.

Пример:
``` 
data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
``` 

`Unique(data)` будет последовательно возвращать только 1 и 2.
```
data = gen_random(1, 3, 10)
```

`Unique(data)` будет последовательно возвращать только 1, 2 и 3.
```
data = [‘a’, ‘A’, ‘b’, ‘B’, ‘a’, ‘A’, ‘b’, ‘B’]
```

`Unique(data)` будет последовательно возвращать только a, A, b, B.

`Unique(data, ignore_case=True)` будет последовательно возвращать только a, b.

Шаблон для реализации класса-итератора:
```
# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        pass

    def __next__(self):
        # Нужно реализовать __next__    
        pass

    def __iter__(self):
        return self
```

### Задача 4 (файл sort.py)
Дан массив 1, содержащий положительные и отрицательные числа. Необходимо одной строкой кода вывести на экран массив 2, которые содержит значения массива 1, отсортированные по модулю в порядке убывания. Сортировку необходимо осуществлять с помощью функции sorted. Пример:
```
data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
Вывод: [123, 100, -100, -30, 30, 4, -4, 1, -1, 0]
```

Необходимо решить задачу двумя способами:

1. С использованием lambda-функции.
2. Без использования lambda-функции.

Шаблон реализации:

```
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = ...
    print(result)

    result_with_lambda = ...
    print(result_with_lambda)
```

### Задача 5 (файл print_result.py)
Необходимо реализовать декоратор print_result, который выводит на экран результат выполнения функции.

* Декоратор должен принимать на вход функцию, вызывать её, печатать в консоль имя функции и результат выполнения, после чего возвращать результат выполнения.
* Если функция вернула список (list), то значения элементов списка должны выводиться в столбик.
* Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равенства.
Шаблон реализации:
```
# Здесь должна быть реализация декоратора

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
```

Результат выполнения:

```
test_1
1
test_2
iu5
test_3
a = 1
b = 2
test_4
1
2
```

### Задача 6 (файл cm_timer.py)
Необходимо написать контекстные менеджеры cm_timer_1 и cm_timer_2, которые считают время работы блока кода и выводят его на экран. Пример:

```
with cm_timer_1():
    sleep(5.5)
```

После завершения блока кода в консоль должно вывестись `time: 5.5` (реальное время может несколько отличаться).

`cm_timer_1` и `cm_timer_2` реализуют одинаковую функциональность, но должны быть реализованы двумя различными способами (на основе класса и с использованием библиотеки contextlib).

### Задача 7 (файл process_data.py)

* В предыдущих задачах были написаны все требуемые инструменты для работы с данными. Применим их на реальном примере.

* В файле data_light.json содержится фрагмент списка вакансий.

* Структура данных представляет собой список словарей с множеством полей: название работы, место, уровень зарплаты и т.д.

* Необходимо реализовать 4 функции - f1, f2, f3, f4. Каждая функция вызывается, принимая на вход результат работы предыдущей. За счет декоратора @print_result печатается результат, а контекстный менеджер cm_timer_1 выводит время работы цепочки функций.

* Предполагается, что функции f1, f2, f3 будут реализованы в одну строку. В реализации функции f4 может быть до 3 строк.

* Функция f1 должна вывести отсортированный список профессий без повторений (строки в разном регистре считать равными). Сортировка должна игнорировать регистр. Используйте наработки из предыдущих задач.

* Функция f2 должна фильтровать входной массив и возвращать только те элементы, которые начинаются со слова “программист”. Для фильтрации используйте функцию filter.

* Функция f3 должна модифицировать каждый элемент массива, добавив строку “с опытом Python” (все программисты должны быть знакомы с Python). Пример: Программист C# с опытом Python. Для модификации используйте функцию map.

* Функция f4 должна сгенерировать для каждой специальности зарплату от 100 000 до 200 000 рублей и присоединить её к названию специальности. Пример: Программист C# с опытом Python, зарплата 137287 руб. Используйте zip для обработки пары специальность — зарплата.

Шаблон реализации:

```
import json
import sys
# Сделаем другие необходимые импорты

path = None

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    raise NotImplemented


@print_result
def f2(arg):
    raise NotImplemented


@print_result
def f3(arg):
    raise NotImplemented


@print_result
def f4(arg):
    raise NotImplemented


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
```


## Лабораторная работа №4 - Шаблоны проектирования и модульное тестирование в Python.

1.1	Необходимо для произвольной предметной области реализовать три шаблона проектирования: один порождающий, один структурный и один поведенческий. В качестве справочника шаблонов можно использовать следующий каталог.
* Порождающий паттерн проектирования - abstract_factory.py
* Структурный паттерн проектирования - wrapper.py
* Поведенческий паттерн проектирования - observer.py

1.2	Для каждой реализации шаблона необходимо написать модульный тест. В модульных тестах необходимо применить следующие технологии:
* TDD – фреймворк
* BDD – фреймворк
* Создание Mock-объектов




## Лабораторная работа №5 - Создание HTML сайта

Разработать макет сайта на языке разметки HTML, состоящий из нескольких связанных HTML-документов. Макет сайта должен включать следующие элементы:
1. Списки.
2. Изображения.
3. Таблицы.
4. Фреймы, для создания меню используются гиперссылки.
5. Плавающие фреймы.
6. Элементы семантической разметки.



## Лабораторная работа №6 - Разработка веб-форм

Разработать HTML-форму, содержащую следующие элементы:
1. Текстовое однострочное поле ввода
2. Набор элементов checkbox
3. Набор радиокнопок
4. Текстовое поле ввода из нескольких строк
5. Список
6. Выпадающий список
7. Список на основе текстового поля
8. Кнопку с изображением
9. Кнопку отправки формы


## Лабораторная работа №7 - Разработка макета веб-приложения

Разработать макет сайта.
Макет сайта должен включать следующие элементы:
1. Таблицы
2. Элементы HTML-форм
3. Панель навигации (в верхней части страницы)
4. Выпадающие списки кнопок (могут быть использованы в 
панели навигации)
5. Индикаторы прогресса

## Лабораторная работа №8 - Создание веб-приложения на Django

Создайте прототип веб-приложения с использованием фреймворка Django:
* Создайте виртуальное окружение
* Установите в него Django
* Создайте проект и приложение Django
2. Создайте представление и шаблоны (по желанию можно использовать модели), реализующие концепцию master/detail со следующей функциональностью:
* На странице master в виде списка HTML выводится информация 
о трех объектах. Каждая строка списка представляет собой гиперссылку, при нажатии на которую происходит переход к странице detail.
* Страница detail содержит детальное описание объекта, фотографию, гиперссылку на master-страницу
* Фотография относится к статическому содержимому сайта
* Страница detail должна выводить данные с использованием таблицы HTML
* Шаблон страницы detail получает от представления данные о детальном объекте с использованием контекста
* ПО желанию можно использовать верстку с применением Bootstrap (или аналогичного фреймворка), а также представление на основе классов (class-based views)

## Рубежный контроль №1 

Вариант Д7 Микропроцессор - Компьютер

1. «Компьютер» и «Микропроцессор» связаны соотношением один-комногим. Выведите список всех микропроцессоров, у которых модель заканчивается на «en», и название их компьютеров.
2. «Компьютер» и «Микропроцессор» связаны соотношением один-комногим. Выведите список компьютеров со средней стоимостью микропроцессора в каждом компьютере, отсортированный по средней стоимости
3. «Компьютер» и «Микропроцессор» связаны соотношением многие-комногим. Выведете список компьютеров, у которых название начинается с «L», и список установленных в нем микропроцессоров. 

## Рубежный контроль №2 

_Запрос Д_

1. Данные класса 1 должны выводиться в виде таблицы с отступами от внутренних границ (cellpadding)
2. Данные класса 2 должны выводиться в виде нумерованного списка, используется нумерация римскими цифрами
3. С использованием технологии CSS реализуйте чересстрочное форматирование ("зебру") для данных таблицы

_Предметная область 7: Микропроцессор - Компьютер_

## Домашняя работа

Создайте прототип веб-приложения с использованием фреймворка 
Django на основе базы данных, реализующий концепцию master/detail. 
Прототип должен содержать:
* Две модели, связанные отношением один-ко-многим
* Стандартное средство администрирования Django позволяет редактировать данные моделей. Желательно настроить русификацию ввода и редактирования данных.
* Веб0приложение формирует отчет в виде отдельного view/template, отчет выводит HTML-страницу, содержащую связанные данные из двух моделей.
* Для верстки шаблонов используется фреймворк Bootstrap, или аналогичный фреймворк по желанию студента
Расширенное задание:
* Реализация в отчете (пункт 3 стандартного задания) графика на основе данных отчета с использованием библиотек JavaScript (например, c3js) и развертывание приложения на облачном 
сервисе (например, heroku)

