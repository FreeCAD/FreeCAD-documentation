# Manual:Creating parametric objects/ru
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC}}


<div class="mw-translate-fuzzy">

В [предыдущей главе](Manual:Creating_and_manipulating_geometry/ru.md) мы видели создание геометрии Part, и как показать её на экране присоединением её к \"пустому\" (непараметрическому) объекту документа. Это муторно, когда мы хотим изменить форму объекта. Нам нужно создать новую форму, затем снова приписать её к нашему объекту.


</div>


<div class="mw-translate-fuzzy">

Однако мы видели в предыдущих главах этого руководства, как велики возможности параметрических объектов. Мы можем изменить один параметр, и форма пересчитывается на лету.


</div>


<div class="mw-translate-fuzzy">

Внутри параметрические объекты не делают ничего иного кроме того, что мы делали: они пересчитывают содержимое параметра Shape, раз за разом когда другие параметры изменяются.


</div>

-   Declares the necessary properties for the object.
-   Defines the behavior when any of these properties are modified.

The structure of such a parametric object is as simple as this:


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


<div class="mw-translate-fuzzy">

FreeCAD обеспечивает очень удобную систему для построения таких параметрических объектов полностью в Python. Они состоят из простых классов Python, которые определяют все нужные объекту параметры, и что случится если один из этих параметров изменится. Структура этих параметрических объектов так проста, как это:


</div>

-   Store the class itself in the **Proxy** attribute of the FreeCAD document object:

By assigning **self** to the **Proxy** attribute of the FreeCAD document object, we link the logic of our Python class to the FreeCAD object. This means the document object will \"carry\" the Python class code inside itself, allowing it to behave according to the logic defined in the class. This connection enables FreeCAD to know how to interact with and recalculate the parametric object.

-   Create all the properties the object needs:

Using the **addProperty** method, we define the custom properties required by the object. Properties act as parameters or variables for the object and can be accessed, modified, and displayed in FreeCAD\'s property editor. In the example, we add a floating-point property named **MyLength**. This property will later influence the shape or behavior of the object.

There are many types of properties available in FreeCAD, ranging from floating-point numbers to strings and even specialized types for geometry and materials. To explore the full list of available property types, you can type the following code in the Python console:


```python
FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "dummy").supportedProperties()
```


<div class="mw-translate-fuzzy">

Все классы Python обычно имеют метод \_\_init\_\_. Всё, что внутри этого метода, исполняется когда создаётся экземпляр этого класса (что знает, на программистском сленге, что объект Python создаётся из этого класса. Представляйте класс как \"шаблон\" для создания живых копий). В наших функциях \_\_init\_\_ мы здесь делаем две важные вещи: 1- сохраняем наш класс в атрибут \"Proxy\" объекта нашего документа FreeCAD, то есть документ FreeCAD будет носить этот код в себе, и 2- создает все параметры, которые нужны нашему объекту. Доступны множество типов параметров, Вы можете получить полный список, набрав следующий код:


</div>

In summary:

-   The **execute** method is called whenever the object needs to be updated.
-   It is responsible for recalculating the shape and assigning it to the object\'s **Shape** attribute.
-   The **obj** argument gives access to the FreeCAD document object, enabling you to make changes programmatically.

With this system, FreeCAD handles the rest---ensuring that the object is properly updated in the document and displayed correctly in the graphical interface.


<div class="mw-translate-fuzzy">

Следующая важная часть это исполняемый метод. Любой код в этом методе исполняется когда объект маркирован для пересчёта, что происходит когда объект изменяется. Это всё, что есть. Внутри исполнения требуется сделать всё, что надо, то есть вычисление новой формы, и приписывания объекту чего-то вроде obj.Shape = myNewShape. Вот почему исполняемый метод принимает аргумент \"obj\", которых будет самим документом FreeCAD, так что мы можем манипулировать им внутри нашего кода python.


</div>


<div class="mw-translate-fuzzy">

Последняя вещь, которую важно запомнить: когда Вы создаёте такой параметрический объект в документе FreeCAD, когда Вы сохраняете файл, вышеуказанный код python не сохраняется в файле. Это происходит из соображений безопасности, если бы файлы FreeCAD содержали код, у злоумышленников была бы возможность распространять файлы FreeCAD с вредоносным кодом, который мог бы повреждать чужие компьютеры. Так что если Вы распространяете файл, который содержит объекты, сделанные с помощью вышеуказанного года, этот код должен так же находиться на компьютерах, которые откроют файл. Простейший путь достичь этого - сохранить код в макросе, и распространять макрос вместе с файлом, или делиться своим макросом на [репозитории макросов FreeCAD](Macros_recipes/ru.md), где каждый сможет загрузить его.


</div>

Ниже мы выполним маленькое упражнение, создав параметрический объект - простейшая параметрическая прямоугольная грань. Более сложные примеры доступны в [примере параметрического объекта](Scripted_objects/ru.md) и в [коде самого FreeCAD](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py).


<div class="mw-translate-fuzzy">

Мы придадим нашему объекту два параметра: Length и Width, которые мы будем использовать для создания прямоугольника. Затем, поскольку наш объект уже имеет встроенный параметр Placement (все геометрические объекты имеют его по умолчанию, их не надо добавлять самостоятельно), мы поместим наш прямоугольник в положение/наклон, установленные в Placement, так что пользователь сможет перемещать прямоугольник редактированием параметра Placement.


</div>


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


<div class="mw-translate-fuzzy">

Вместо того чтобы вставить вышеуказанный код в консоль Python, лучше сохраним его где-нибудь, чтобы мы могли повторно использовать и модифицировать его позднее. Например, в макросе (меню Tools -\> Macros -\> Create). Назовём его, например, \"ParamRectangle\". Тем не менее, макрос FreeCAD сохраняется с расширением .FCMacro, который Python не разспознаёт при импорте. Поэтому перед использованием этого кода нам надо переименовать ParamRectangle.FCMacro в ParamRectangle.py. Это легко делается в вашем менеджере файлов, найдя папку Macros, показанную в меню Tools -\> Macros.


</div>

Когда это сделано, мы можем сделать это в консоли Python:


```python
import ParamRectangle
```

Открывая содержимое ParamRectangle, мы убедимся, что он содержит лишь наш класс ParametricRectangle.


<div class="mw-translate-fuzzy">

Для создания нового параметрического объекта с использованием нашего класса ParametricRectangle мы будем использовать следующий код. Заметьте, что мы используем Part::FeaturePython вместо Part::Feature, который мы использовали в предыдущих главах (версия Python позволяет определить наш собственное параметрическое поведение):


</div>


```python
myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "Rectangle")
ParamRectangle.ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0 # This is mandatory unless we code the ViewProvider too.
FreeCAD.ActiveDocument.recompute()
```

Here is a quick breakdown of the previous commands:

-   **myObj = FreeCAD.ActiveDocument.addObject(\"Part::FeaturePython\", \"Rectangle\")**: Creates a new **Part::FeaturePython** object named **Rectangle** in the active FreeCAD document. This object is specifically designed for custom parametric behavior, allowing Python-defined logic to manage its properties and behavior.

-   **ParamRectangle.ParametricRectangle(myObj)**: Initializes the object by associating it with the **ParametricRectangle** class from the **ParamRectangle** module or script. This links the custom Python-defined logic to the object, enabling it to act as a parametric object.

-   **myObj.ViewObject.Proxy = 0**: Resets the **ViewObject.Proxy** attribute to 0, ensuring that the object uses FreeCAD's default view handling. This step is required unless you define a custom ViewProvider to manage the visual representation of the object.

-   **FreeCAD.ActiveDocument.recompute()**: Recomputes the document to update the geometry and reflect changes in the FreeCAD graphical interface, making the new object fully visible and functional


<div class="mw-translate-fuzzy">

Пока ничего на экране не появилось, поскольку параметры Length и Width равны 0, что включает наше правило \"do-nothing\" внутри execute. Нам надо просто изменить значения Length и Width, и наш объект волшебно появится и будет пересчитан на лету.


</div>


<div class="mw-translate-fuzzy">

Разумеется, было бы утомительно вводить эти 4 строки кода Python каждый раз, когда нам нужно создать новый параметрический прямоугольник. Простой путь решить это - поместить эти 4 строки в наш файл ParamRectangle.py в конце, после класса ParametricRectange (Мы можем делать это в редакторе макросов).


</div>


<div class="mw-translate-fuzzy">

Теперь, когда мы напишем import ParamRectangle , новый параметрический прямоугольник создастся автоматически. Даже лучше, мы можем добавить кнопку панели инструментов, которая сделает это:


</div>


<div class="mw-translate-fuzzy">

-   Открыть меню **Tools -\> Customize**
-   На вкладке \"Macros\" выберите наш ParamRectangle.py, заполните детали по желанию и нажмите \"Add\":

![](images/Exercise_python_04.jpg )


</div>

![](images/FreeCAD_python_macroRec.png )

-   На вкладке Toolbars создайте новую панель инструментов в каком хотите верстаке (или глобально), выделите ваш макрос и добавьте его в панель инструментов:

![](images/FreeCAD_python_toolbarCus.png )

-   Это всё, мы уже имеем новую кнопку панели инструментов, которая при клике создаст параметрический прямоугольник.


<div class="mw-translate-fuzzy">

Запомните, если Вы хотите распространять файлы, созданные с помощью этого нового инструмента среди других людей, они должны так же иметь установленный на своём компьютере макрос ParamRectangle.py.


</div>

**Читать далее**

-   [Репозиторий макросов FreeCAD](Macros_recipes/ru.md)
-   [Пример параметрического объекта](Scripted_objects/ru.md)
-   [Дополнительные примеры в коде FreeCAD](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py)


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Manual:Creating parametric objects/ru
