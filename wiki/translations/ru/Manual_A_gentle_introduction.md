# Manual:A gentle introduction/ru
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

[Python](https://ru.wikipedia.org/wiki/Python) - популярный язык программирования с открытыми исходниками, часто встраиваемый в приложения как скриптовый язык, как в случае FreeCAD. У него так же много возможностей, интересных для пользователей FreeCAD: он лёгок в изучении, особенно для людей, ранее не программировавших, и встроен во множество других приложений. Это делает его очень ценным для изучения, поскольку Вы сможете использовать его во множестве других приложений, таких как [Blender](http://www.blender.org), [Inkscape](http://www.inkscape.org) или [GRASS](http://grass.osgeo.org/).


</div>


<div class="mw-translate-fuzzy">

FreeCAD широко использует Python. С его помощью Вы можете иметь доступ и управлять практически любой возможностью FreeCAD. Например, Вы можете создавать новые объекты, модифицировать его геометрию, анализировать содержимое, или даже создавать новые элементы управления, инструменты и панели. Некоторые верстаки FreeCAD и большинство дополнительных верстаков запрограммированы полностью на Python. У FreeCAD есть совершенная консоль Python, доступная из меню **Вид-\>Панели-\>Консоль Python**. Она часто полезна для выполнения операций, для которых пока нет кнопок инструментальных панелей, или проверки фигур на ошибки, или выполнения повторяющихся задач:


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_python_01.jpg )


</div>

In FreeCAD, Python scripting enables you to:

-   Automate repetitive tasks to save time and reduce errors.
-   Create custom parametric objects that dynamically adapt to changes.
-   Develop personalized macros and tools tailored to specific workflows.
-   Interact with FreeCAD's Application Programming Interface (API) to access and manipulate geometry, scenes, and user interface elements programmatically.

By leveraging Python, FreeCAD users can unlock the full potential of the software, transforming it into a powerful and flexible tool tailored to their unique needs.


<div class="mw-translate-fuzzy">

Но консоль Python можно использовать и по-другому: каждый раз как Вы нажмёте на кнопку в панели инструментов или выполните в FreeCAD другую операцию, в консоли появляется и выполняется код Python. Оставляя консоль Python открытой, Вы можете точно видеть как разворачивается код Python в процессе работы, и довольно быстро, почти не замечая, Вы сможете выучить что-то из языка Python.


</div>


<div class="mw-translate-fuzzy">

У FreeCAD так же есть [система макросов](Macros/ru.md), позволяющая записывать действия для последующего воспроизведения. Эта система так же использует консоль Python, просто записывая всё, что им сделано.


</div>

В этой главе мы покажем общие основы языка Python. Если Вы хотите изучать дальше, wiki-документация FreeCAD содержит обширный раздел насчёт [программирования на Python](Power_users_hub.md).



### Написание кода на Python 


<div class="mw-translate-fuzzy">

Есть два простых способа написания кода Python в FreeCAD: из консоли Python (меню **Вид -\> Панели -\> Консоль Python**), или из редактора макросов (меню **Tools -\> Macros -\> New**). В консоли Вы пишете команды Python одну за одной, и они выполняются после нажатия кнопки Return, в то время как макросы могут содержать сложный скрипт из нескольких линий, исполняемый лишь когда макрос запущен из того же окна макросов.


</div>

Если Вы впервые используете Python, перед продолжением сначала подумайте о знакомстве с [введением в программирование на Python](Introduction_to_Python/ru.md), которое сделает Ваши основные понятия о Python яснее.



### Манипуляция объектами FreeCAD 

Начнём с создания нового пустого документа:


```python
doc = FreeCAD.newDocument()
```


<div class="mw-translate-fuzzy">

Если Вы вводили это в консоли Python FreeCADа, то заметили, что как только Вы ввели \"FreeCAD.\" (слово FreeCAD с последующей точкой), появилось окно, позволяющее быстро автозаполнить продолжение строки. Даже лучше, каждый ввод в списке автодополнения содержит подсказку. Это облегчает раскрытие имеющейся функциональности. Перед выбором \"newDocument\", взгляните на другие доступные опции.


</div>


<div class="mw-translate-fuzzy">

![](images/Exercise_python_02.jpg )


</div>


<div class="mw-translate-fuzzy">

Как только Вы нажмёте **Enter**, будет создан новый документ. Это то же, что нажать на панели инструментов кнопку \"Создать\". В Python кнопка используется, чтобы показать нечто, что содержится в чём-то другом (функция newDocument содержится внутри модуля FreeCAD). Окно с вариантами, которое появляется, соответственно показывает всё, что содержится в \"FreeCAD\". Если Вы вместо скобок добавите точку после newDocument, Вам будет показано всё содержимое функции newDocument. Скобки обязательны, когда Вы вызываете функцию Python, такую как эта. Мы покажем это яснее внизу.


</div>


<div class="mw-translate-fuzzy">

Теперь вернёмся назад в документ. Посмотрим, что мы можем с ним сделать. Введите следующее и изучите доступные варианты:


</div>

Now let\'s get back to our document. Let\'s see what we can do with it. Type the following and explore the available options:


```python
doc.
```


<div class="mw-translate-fuzzy">

Обычно имена, начинающиеся с заглавной буквы, это атрибуты, они содержат значения. Имена с маленькой буквы являются функциями (называемые так же методами), они \"что-то делают\". Имена, начинающиеся с подчёркиваний, обычно используются для внутренних нужд модуля, и Вам лучше игнорировать их. Используем один из методов для добавления в документ нового объекта:


</div>

-   Names that begin with an upper-case letter are typically attributes, which store values or data, such as properties of an object.
-   Names that begin with a lower-case letter are usually functions (also called methods), which perform actions or operations, such as creating or modifying objects.
-   Names that begin with an underscore (\_) are generally intended for internal use within the module and can usually be ignored.

This distinction helps you navigate FreeCAD's API and select the appropriate command for your needs. For example, you might use a method to add a new object to a document. The method performs the action of creating and adding the object, while attributes store the object\'s properties. Understanding this structure makes it easier to explore the functionality available, especially when using the autocomplete feature or reading tooltips. Let\'s add a box.


```python
box = doc.addObject("Part::Box", "myBox")
```


<div class="mw-translate-fuzzy">

Наш куб уже добавлен в древо проекта, но ничего не возникло в окне трёхмерного вида, поскольку при работе из Python документ не пересчитывается автоматически. Нам надо сделать это вручную, когда нужно:


</div>

-   **doc.addObject**: This tells FreeCAD to add a new object to the document.
-   **Part::Box**: This specifies the type of object to create, in this case, a 3D box.
-   **myBox**: This assigns a name to the new object, making it easier to identify and reference later.

The result of this command is that a box appears in the active document, and the variable box stores a reference to it so you can modify or interact with it later. Our box is added in the tree view, but nothing happens in the 3D view yet, because when working from Python, the document is never recomputed automatically. We must do that manually, whenever required:


```python
doc.recompute()
```


<div class="mw-translate-fuzzy">

Теперь наш куб появился в окне трёхмерного вида. Большинство кнопок панелей инструментов фактически делают две вещи: добавляют объект и выполняют рекомпиляцию. Если Вы включите в настройках опцию \"Показывать команды скриптов в консоли Python\" и попробуете добавить сферу с соответствующей кнопкой в верстаке Part, Вы увидите две линии кода Python, выполняемые одна за другой.


</div>


<div class="mw-translate-fuzzy">

Вы можете получить список всех возможных объектов, подобных Part::Box:


</div>


<div class="mw-translate-fuzzy">

doc.supportedTypes()


</div>


```python
doc.supportedTypes()
```


<div class="mw-translate-fuzzy">

box.


</div>


```python
box.
```


<div class="mw-translate-fuzzy">

box.Height


</div>


```python
box.Height
```


<div class="mw-translate-fuzzy">

box.Height = 5


</div>


```python
box.Height = 5
```


<div class="mw-translate-fuzzy">

box.Length


</div>


```python
box.Length
```


<div class="mw-translate-fuzzy">

Попробуйте следующий пример для доступа к цвету линии нашего куба:


</div>


<div class="mw-translate-fuzzy">

box.ViewObject.LineColor


</div>


```python
box.ViewObject.LineColor
```




<div class="mw-translate-fuzzy">

Вектора это фундаментальная концепция в любом приложении трёхмерного моделирования. Это список из 3 чисел (x, y и z), указывающих точку или позицию в трёхмерном пространстве. С векторами могут быть выполнены множество вещей, сложение, вычитание, проекции и многое другое. В FreeCAD векторы работают так:


</div>


<div class="mw-translate-fuzzy">

myvec = FreeCAD.Vector(2,0,0)

print(myvec)
print(myvec.x)
print(myvec.y)
othervec = FreeCAD.Vector(0,3,0)
sumvec = myvec.add(othervec)


</div>


<div class="mw-translate-fuzzy">

Другое общее свойство объектов FreeCAD это их размещение **Placement**. Как мы видели в предыдущих главах, у каждого объекта есть параметр Placement, содержащий его позицию (Base) и ориентацию (Rotation). Ими легко манипулировать через Python, например, для перемещения нашего объекта:


</div>


<div class="mw-translate-fuzzy">

print(box.Placement)

print(box.Placement.Base)
box.Placement.Base = sumvec
otherpla = FreeCAD.Placement()
otherpla.Base = FreeCAD.Vector(5,5,0)
box.Placement = otherpla


</div>


<div class="mw-translate-fuzzy">

**Читать далее**


</div>


```python
myvec = FreeCAD.Vector(2, 0, 0)
print(myvec)
print(myvec.x)
print(myvec.y)
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```


<div class="mw-translate-fuzzy">





</div>


<div class="mw-translate-fuzzy">





</div>


```python
print(box.Placement)
print(box.Placement.Base)
box.Placement.Base = sumvec
otherpla = FreeCAD.Placement()
otherpla.Base = FreeCAD.Vector(5, 5, 0)
box.Placement = otherpla
```

Here is a short breakdown of the above commands:

-   **print(box.Placement)**: Prints the placement of the box, which includes its position, rotation, and orientation in 3D space.
-   **print(box.Placement.Base)**: Prints the position (Base) of the box, which is a vector representing its location in 3D space.
-   **box.Placement.Base = sumvec**: Sets the base position (location) of the box to the vector sumvec, effectively moving the box to this new position.
-   **otherpla = FreeCAD.Placement()**: Creates a new placement object named otherpla.
-   **otherpla.Base = FreeCAD.Vector(5,5,0)**: Sets the base position of otherpla to a vector at coordinates (5, 5, 0).
-   **box.Placement = otherpla**: Applies otherpla to the box, updating its placement to the new position and orientation defined by otherpla.

**Read more**

-   [Python](https://www.python.org)
-   [Macros](Macros.md)
-   [Introduction to Python](Introduction_to_Python.md)
-   [Python scripting tutorial](Python_scripting_tutorial.md)
-   [Power users hub](Power_users_hub.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:A gentle introduction/ru
