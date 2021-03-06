##Оглавление##
1. Типизация и система типов языка Python.

2. Основные управляющие конструкции.

3. Подмножество языка для функционального программирования:

    * способы обеспечить иммутабельность данных там, где это необходимо
    * функции как объекты 1-го класса
    * функции высших порядков 
    * встроенные функции высших порядков для работы с последовательностями.

4. Важнейшие функции для работы:
    * с потоками ввода/вывода
    * строками
    * регулярными выражениями
<br/><br/>

##1. Типизация и система типов.

В python **типизация динамическая, неявная и сильная**:

	>>> a = 5 
	>>> a
	5
	>>> a = float(a)
	>>> a
	5.0


###Встроенные типы данных Python

К стандартным типам данных в Python относят:

* Числа (Numbers)
* Список (List)
* Строка (String)
* Кортеж (Tuple)
* Словарь (Dictionary)
* Сет (Set)


####Числа

В Python поддерживаются **3 разных числовых типа**:

* целые числа со знаком (int);
* значения с плавающей запятой (float);
* комплексные числа (complex).

Не существует ограничения на размер памяти для хранения одного числа - память добавляется при надобности

type() и  isinstance() - функции, позволяющие узнать тип численной переменной

	>>> a = 5
	>>> print(a, "is of type", type(a))
	5 is of type <class 'int'>
	>>> a = 2.0
	>>> print(a, "is of type", type(a))
	2.0 is of type <class 'float'>
	>>> a = 1+2j
	>>> print(a, "is complex number?", isinstance(1+2j, complex))
	(1+2j) is complex number? True

####Списки
В Python есть **списки** - упорядоченные последовательности элементов (не обязательно одного типа).

	>>> a = [1, 2.2, 'python']
	>>> a
	[1, 2.2, 'python']

Список представляет массив указателей на значения его элементов в памяти.

####Строки 
**Строка** - просто последовательность символов между кавычками (одинарными или двойными).
 
    >>> s1 = "abra cadabra"
    >>> s1
    'abra cadabra'
    >>> s2 = 'abra cadabra'
    >>> s2
    'abra cadabra'

####Кортежи
**Кортеж** - тот же список, но без возможности изменения его элементов.

    >>> t = (1, 2, 3) 
    >>> t
    (1, 2, 3)

####Словари
**Словарь** - неупорядоченные коллекции произвольных объектов с доступом по ключу. 
Их иногда ещё называют ассоциативными массивами или хеш-таблицами.

    >>> d = {'a':1, 'b':2, 'c':3}
    >>> d
    {'a': 1, 'b': 2, 'c': 3}

####Сеты
**Сеты** - неупорядоченные и непроиндексированные множества элементов. <br/>
Сет не  содержит дубликатов.

    >>> s = {2, 1, 3, 3, 4}
    >>> s
    {1, 2, 3, 4}
                                                 
##2. Основные управляющие конструкции.
####Операторы условия 
    if a>b:
        print(a)
---
    if a>b:
        print(a)
    else: 
        print(b)
---         
    if a>b:
        print(a)
    elif a<b: 
        print(b)
    else:
        print("a equals b")

####Циклы с условием
    a = 1
    while a < 10:
        a+=1
    print(a)
    
####Цикл с параметром
    for i in range(1, 10):
        print(i)

<br/>

##3. Подмножество языка для функционального программирования

####Cпособы обеспечить иммутабельность данных там, где это необходимо
Функция id() возвращает адрес переменной в памяти

    >>> a = 5
    >>> id(a)
    140062400325888
    >>> a+=2
    >>> id(a)
    140062400325952
    
При изменении переменной её адрес тоже изменился. 
Это значит, что интерпретатор не перезаписал значение по адресу, 
а выделил место в памяти под новый объект,
который вернула операция '+='. 
Значит, в Python int - иммутабельный.

Вот табличка мутабельности некоторых встроенных типов:

|Класс|Мутабелен?|
|---|:---:|
|bool|-
|int|-
|float|-
|complex|-
|list|+
|tuple|-
|str|-
|set|+
|dict|+

Если создать новый класс, то он будет мутабельным.

<br/>

####Функции как объекты 1-го класса
>Объектами первого класса в контексте конкретного языка программирования 
>называются элементы, которые могут быть переданы как параметр, 
>возвращены из функции, присвоены переменной. 

    def shout(text):
        return text.upper()
        
    print(shout('Hello'))   #передали функцию как параметр
    yell = shout            #присвоили функцию переменной
    print yell('Hello')
    
    def returnf(f):
        return f
    yell2 = returnf(shout)  #вернули функцию из функции
    print yell2('Hello')
    
В результате выполнения этого кода на экран 3 раза выведется HELLO

####Функции высших порядков 
Так как в Python функции – это объекты первого класса, 
то они являются функциями высшего порядка, что демонстрирует предыдущий пример.
####Встроенные функции высших порядков для работы с последовательностями.
К встроенным функциям высшего порядка относятся *map* и *filter*.
<br/>

Функция **map** принимает функцию и последовательность, возвращает последовательность, 
элементами которого являются результаты применения функции к элементам 
входной последовательности.

    >>> a = [1, 2, 3]
    >>> def f(x):
    ...     return x+2
    >>> list(map(f,a))
    [3, 4, 5]

Функция **filter** принимает функцию предикат и последовательность, 
возвращает последовательность, элементами которой являются данные из исходной, 
для которых предикат возвращает True.

    >>> list(filter(lambda x: x > 0, [-1, 1, -2, 2, 0]))
    [1, 2]
    
<br/>    
    
##Важнейшие функции в Python
###Потоки ввода/вывода
Функции **print()** и **input** предназначены для работы со стандартными потоками -
консолью и клавиатурой. <br/>
 
####Чтение из файла
Для открытия файла используется функция **open()**, которая возвращает файловый объект. 
Наиболее часто используемый вид данной функции выглядит так: 
        
    open(имя_файла, режим_доступа). 
    
Для указания режима доступа используется следующие символы:

* ‘r’ – открыть файл для чтения;

* ‘w’ – открыть файл для записи;

* ‘x’ – открыть файл с целью создания, если файл существует, то вызов функции open завершится с ошибкой;

* ‘a’ – открыть файл для записи, при этом новые данные будут добавлены в конец файла, без удаления существующих;

* ‘b’ – бинарный режим;

* ‘t’ – текстовый режим;

*  ‘+’ – открывает файл для обновления.

По умолчанию файл открывается на чтение в текстовом режиме. 
<br/>
У файлового объекта есть следующие атрибуты.

* file.closed – возвращает true если файл закрыт и false в противном случае;

* file.mode – возвращает режим доступа к файлу, при этом файл должен быть открыт;

* file.name – имя файла.

Для закрытия файла используется метод close().

####Запись в файл
Для записи данных файл используется метод **write(строка)**, 
при успешной записи он вернет количество записанных символов.

<br/>

###Строки
    >>> a = "aaaa"
    >>> b = "bbbb"
    >>> a+b
    'aaaabbbb'
    >>> a*4
    'aaaaaaaaaaaaaaaa'
    >>> len(a)
    4
    >>> c = "abc"
    >>> c[1]
    'b'
    >>> c[1:3]
    'bc'
    >>> d = "ab\ncd"
    >>> print(d)
    ab
    cd


###Регулярные выражения

**re.search(pattern, string, flags[optional])** используется для 
нахождения первого вхождения заданного шаблона в строку.


**findall(pattern, string, flags=0[optional])** возвращает список, 
в котором в виде строк содержатся все искомые вхождения по порядку. 
Если вхождений нет, то эта функция возвратит пустой список.


<br/>
**Основные шаблоны для регулярных выражений:**

|Символ |Описание|
|---|---|
|.| 	любой символ, за исключением новой строки
|\w| 	любой буквенный, цифровой символ, а также нижнее подчеркивание
|\W| 	любые не буквенные и не цифровые символы и не нижнее подчеркивание
|\d |	любая одиночная цифра
|\D| 	любой одиночный символ, кроме цифры
|\s| 	любой пробельный символ, как например \n, \t, а также сам пробел
|\S| 	любой не пробельный одиночный символ
|[abc] |	любой одиночный символ в данном множестве, то есть в этом примере это либо  a, либо b, либо c
|[^abc] |	любой одиночный символ, отличный от a, b и c
|[a-z] 	|любой одиночный символ в диапазоне от a до z
|[a-zA-Z] |	любой одиночный символ в диапазоне a-z или A-Z
|[0-9] 	|любой одиночный символ в диапазоне 0—9
|^ |	сравнение начинается с начала строки
|$ |	сравнение начинается с конца строки
|+ |	один или больше символов (жадное соответствие).
|* |	ноль или больше символов (жадное соответствие).
