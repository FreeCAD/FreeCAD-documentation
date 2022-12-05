# Manual:Creating parametric objects/ru
{{Manual:TOC/ru}}

В [предыдущей главе](Manual:Creating_and_manipulating_geometry/ru.md) мы видели создание геометрии Part, и как показать её на экране присоединением её к \"пустому\" (непараметрическому) объекту документа. Это муторно, когда мы хотим изменить форму объекта. Нам нужно создать новую форму, затем снова приписать её к нашему объекту.

Однако мы видели в предыдущих главах этого руководства, как велики возможности параметрических объектов. Мы можем изменить один параметр, и форма пересчитывается на лету.

Внутри параметрические объекты не делают ничего иного кроме того, что мы делали: они пересчитывают содержимое параметра Shape, раз за разом когда другие параметры изменяются.

FreeCAD обеспечивает очень удобную систему для построения таких параметрических объектов полностью в Python. Они состоят из простых классов Python, которые определяют все нужные объекту параметры, и что случится если один из этих параметров изменится. Структура этих параметрических объектов так проста, как это:


```python
class myParametricObject:

    def __init__(self, obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "MyLength")
        ...

    def execute(self,obj):
        print ("Recalculating the shape...")
        print ("The value of MyLength is:")
        print (obj.MyLength)
        ...
```

Все классы Python обычно имеют метод \_\_init\_\_. Всё, что внутри этого метода, исполняется когда создаётся экземпляр этого класса (что знает, на программистском сленге, что объект Python создаётся из этого класса. Представляйте класс как \"шаблон\" для создания живых копий). В наших функциях \_\_init\_\_ мы здесь делаем две важные вещи: 1- сохраняем наш класс в атрибут \"Proxy\" объекта нашего документа FreeCAD, то есть документ FreeCAD будет носить этот код в себе, и 2- создает все параметры, которые нужны нашему объекту. Доступны множество типов параметров, Вы можете получить полный список, набрав следующий код:


```python
FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "dummy").supportedProperties()
```

Следующая важная часть это исполняемый метод. Любой код в этом методе исполняется когда объект маркирован для пересчёта, что происходит когда объект изменяется. Это всё, что есть. Внутри исполнения требуется сделать всё, что надо, то есть вычисление новой формы, и приписывания объекту чего-то вроде obj.Shape = myNewShape. Вот почему исполняемый метод принимает аргумент \"obj\", которых будет самим документом FreeCAD, так что мы можем манипулировать им внутри нашего кода python.

Последняя вещь, которую важно запомнить: когда Вы создаёте такой параметрический объект в документе FreeCAD, когда Вы сохраняете файл, вышеуказанный код python не сохраняется в файле. Это происходит из соображений безопасности, если бы файлы FreeCAD содержали код, у злоумышленников была бы возможность распространять файлы FreeCAD с вредоносным кодом, который мог бы повреждать чужие компьютеры. Так что если Вы распространяете файл, который содержит объекты, сделанные с помощью вышеуказанного года, этот код должен так же находиться на компьютерах, которые откроют файл. Простейший путь достичь этого - сохранить код в макросе, и распространять макрос вместе с файлом, или делиться своим макросом на [репозитории макросов FreeCAD](Macros_recipes/ru.md), где каждый сможет загрузить его.

Ниже мы выполним маленькое упражнение, создав параметрический объект - простейшая параметрическая прямоугольная грань. Более сложные примеры доступны в [примере параметрического объекта](Scripted_objects/ru.md) и в [коде самого FreeCAD](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py).

Мы придадим нашему объекту два параметра: Length и Width, которые мы будем использовать для создания прямоугольника. Затем, поскольку наш объект уже имеет встроенный параметр Placement (все геометрические объекты имеют его по умолчанию, их не надо добавлять самостоятельно), мы поместим наш прямоугольник в положение/наклон, установленные в Placement, так что пользователь сможет перемещать прямоугольник редактированием параметра Placement.


```python
class ParametricRectangle:

    def __init__(self,obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "Length")
        obj.addProperty("App::PropertyFloat", "Width")

    def execute(self, obj):
        # We need to import the FreeCAD module here too, because we might be running out of the Console
        # (in a macro, for example) where the FreeCAD module has not been imported automatically:
        import FreeCAD
        import Part

        # First we need to make sure the values of Length and Width are not 0
        # otherwise Part.LineSegment will complain that both points are equal:
        if (obj.Length == 0) or (obj.Width == 0):
            # If yes, exit this method without doing anything:
            return

        # We create 4 points for the 4 corners:
        v1 = FreeCAD.Vector(0, 0, 0)
        v2 = FreeCAD.Vector(obj.Length, 0, 0)
        v3 = FreeCAD.Vector(obj.Length,obj.Width, 0)
        v4 = FreeCAD.Vector(0, obj.Width, 0)

        # We create 4 edges:
        e1 = Part.LineSegment(v1, v2).toShape()
        e2 = Part.LineSegment(v2, v3).toShape()
        e3 = Part.LineSegment(v3, v4).toShape()
        e4 = Part.LineSegment(v4, v1).toShape()

        # We create a wire:
        w = Part.Wire([e1, e2, e3, e4])

        # We create a face:
        f = Part.Face(w)

        # All shapes have a Placement too. We give our shape the value of the placement
        # set by the user. This will move/rotate the face automatically.
        f.Placement = obj.Placement

        # All done, we can attribute our shape to the object!
        obj.Shape = f
```

Вместо того чтобы вставить вышеуказанный код в консоль Python, лучше сохраним его где-нибудь, чтобы мы могли повторно использовать и модифицировать его позднее. Например, в макросе (меню Tools -\> Macros -\> Create). Назовём его, например, \"ParamRectangle\". Тем не менее, макрос FreeCAD сохраняется с расширением .FCMacro, который Python не разспознаёт при импорте. Поэтому перед использованием этого кода нам надо переименовать ParamRectangle.FCMacro в ParamRectangle.py. Это легко делается в вашем менеджере файлов, найдя папку Macros, показанную в меню Tools -\> Macros.

Когда это сделано, мы можем сделать это в консоли Python:


```python
import ParamRectangle
```

Открывая содержимое ParamRectangle, мы убедимся, что он содержит лишь наш класс ParametricRectangle.

Для создания нового параметрического объекта с использованием нашего класса ParametricRectangle мы будем использовать следующий код. Заметьте, что мы используем Part::FeaturePython вместо Part::Feature, который мы использовали в предыдущих главах (версия Python позволяет определить наш собственное параметрическое поведение):


```python
myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "Rectangle")
ParamRectangle.ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0 # This is mandatory unless we code the ViewProvider too.
FreeCAD.ActiveDocument.recompute()
```

Пока ничего на экране не появилось, поскольку параметры Length и Width равны 0, что включает наше правило \"do-nothing\" внутри execute. Нам надо просто изменить значения Length и Width, и наш объект волшебно появится и будет пересчитан на лету.

Разумеется, было бы утомительно вводить эти 4 строки кода Python каждый раз, когда нам нужно создать новый параметрический прямоугольник. Простой путь решить это - поместить эти 4 строки в наш файл ParamRectangle.py в конце, после класса ParametricRectange (Мы можем делать это в редакторе макросов).

Теперь, когда мы напишем import ParamRectangle , новый параметрический прямоугольник создастся автоматически. Даже лучше, мы можем добавить кнопку панели инструментов, которая сделает это:

-   Открыть меню **Tools -\> Customize**
-   На вкладке \"Macros\" выберите наш ParamRectangle.py, заполните детали по желанию и нажмите \"Add\":

![](images/Exercise_python_04.jpg )

-   На вкладке Toolbars создайте новую панель инструментов в каком хотите верстаке (или глобально), выделите ваш макрос и добавьте его в панель инструментов:

![](images/Exercise_python_05.jpg )

-   Это всё, мы уже имеем новую кнопку панели инструментов, которая при клике создаст параметрический прямоугольник.

Запомните, если Вы хотите распространять файлы, созданные с помощью этого нового инструмента среди других людей, они должны так же иметь установленный на своём компьютере макрос ParamRectangle.py.

**Читать далее**

-   [Репозиторий макросов FreeCAD](Macros_recipes/ru.md)
-   [Пример параметрического объекта](Scripted_objects/ru.md)
-   [Дополнительные примеры в коде FreeCAD](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating parametric objects/ru
