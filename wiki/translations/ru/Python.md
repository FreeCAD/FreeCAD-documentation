# Python/ru
<div class="mw-translate-fuzzy">


**(Январь 2020) FreeCAD изначально был разработан для работы с Python 2. Поскольку срок службы Python 2 истек в 2020 году, дальнейшая разработка FreeCAD будет осуществляться исключительно с использованием Python 3, и обратная совместимость поддерживаться не будет.**


</div>

## Описание


{{TOCright}}

[Python](https   *//www.python.org) - это язык программирования высокого уровня, общего назначения, который очень часто используется в больших приложениях для автоматизации некоторых задач путем создания скриптов или [макросов](macros.md).

В FreeCAD код Python можно использовать для создания различных элементов программно, без необходимости нажимать на графический пользовательский интерфейс. Кроме того, многие инструменты и верстаки FreeCAD запрограммированы на Python.

Смотрите [Введение в Python](Introduction_to_Python.md), чтобы узнать об основах языка программирования Python, затем [Руководство по написанию сценариев на Python](Python_scripting_tutorial.md) и [Основы написания скриптов для FreeCAD](FreeCAD_Scripting_Basics.md), чтобы начать писать скрипты для FreeCAD.

## Удобочитаемость

Читабельность кода Python является одним из наиболее важных аспектов этого языка. Использование четкого и последовательного стиля в сообществе Python облегчает вклад различных разработчиков, поскольку большинство опытных программистов на Python ожидают, что код будет отформатирован определенным образом и будет следовать определенным правилам. При написании кода на Python рекомендуется следовать [PEP8   * Руководство по стилю написания кода Python](https   *//www.python.org/dev/peps/pep-0008/) и [PEP257   * Соглашения о строках документов](https   *//www.python.org/dev/peps/pep-0257/).

Эти документы представляют пояснения в более удобной для пользователя форме   *

-   [Как написать Красивый код на Python с помощью PEP 8](https   *//realpython.com/python-pep8/)
-   [Документирование Кода Python   * Полное Руководство](https   *//realpython.com/documenting-python-code/).

## Соглашения

В этой документации следует соблюдать некоторые соглашения для примеров Python.

Это типичная сигнатура функции


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
```

-   Аргументы с парами ключ-значение являются необязательными, значение по умолчанию указано в подписи. Это означает, что следующие вызовы эквивалентны   *


```python
Wire = make_wire(pointslist, False, None, None, None)
Wire = make_wire(pointslist, False, None, None)
Wire = make_wire(pointslist, False, None)
Wire = make_wire(pointslist, False)
Wire = make_wire(pointslist)
```


   *   В этом примере первый аргумент не имеет значения по умолчанию, поэтому его всегда следует включать.

-   Если аргументы заданы с явным ключом, необязательные аргументы могут быть заданы в любом порядке. Это означает, что следующие вызовы эквивалентны   *


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None)
Wire = make_wire(pointslist, closed=False, face=None, placement=None)
Wire = make_wire(pointslist, placement=None, closed=False, face=None)
Wire = make_wire(pointslist, support=None, closed=False, placement=None, face=None)
```

-   В рекомендациях Python подчеркивается удобочитаемость кода; в частности, круглые скобки должны сразу следовать за именем функции, а пробел должен следовать за запятой.


```python
p1 = Vector(0, 0, 0)
p2 = Vector(1, 1, 0)
p3 = Vector(2, 0, 0)
Wire = make_wire([p1, p2, p3], closed=True)
```

-   Если код необходимо разбить на несколько строк, это следует делать через запятую внутри скобок или круглых скобок; вторая строка должна быть выровнена с предыдущей.


```python
a_list = [1, 2, 3,
          2, 4, 5]

Wire = make_wire(pointslist,
                False, None,
                None, None)
```

-   Функции могут возвращать объект, который может быть использован в качестве основы для другой функции рисования.


```python
Wire = make_wire(pointslist, closed=True, face=True)
Window = make_window(Wire, name="Big window")
```

## Применение \"Import\" 

Функции Python хранятся в файлах, называемых модулями. Перед использованием любой функции вызываемой из модуля, модуль должен быть включен в код инструкцией `import`.

Это создает префиксы к функциям, то есть `module.function()`. Эта система предотвращает колизии имен между функциями, которые имеют одинаковые имена, но находятся в разных модулях. Например, две функции `Arch.make_window()` и `MyModule.make_window()` могут сосуществовать без проблем.

Полные примеры должны включать необходимый импорт и функции с префиксами.


```python
import FreeCAD as App
import Draft

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1, 1, 0)
p3 = App.Vector(2, 0, 0)
Wire = Draft.make_wire([p1, p2, p3], closed=True)
```


```python
import FreeCAD as App
import Draft
import Arch

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1, 0, 0)
p3 = App.Vector(1, 1, 0)
p4 = App.Vector(0, 2, 0)
pointslist = [p1, p2, p3, p4]

Wire = Draft.make_wire(pointslist, closed=True, face=True)
Structure = Arch.make_structure(Wire, name="Big pillar")
```




[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *API](Category_API.md) [Category   *Python Code](Category_Python_Code.md) [Category   *Glossary](Category_Glossary.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [API](Category_API.md) > [Python Code](Category_Python Code.md) > [Glossary](Category_Glossary.md) > Python/ru
