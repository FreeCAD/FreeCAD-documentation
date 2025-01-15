# Pivy/ru
## Введение


<div class="mw-translate-fuzzy">

[Pivy](Pivy/ru.md) - это библиотека привязок [Python](Python/ru.md) для [Coin3D](https://github.com/coin3d), библиотеки 3D-рендеринга, используемой в FreeCAD для отображения вещей в [трёхмерный вид](3D_view/ru.md). При импорте в работающий интерпретатор Python Pivy позволяет напрямую взаимодействовать с любым работающим [графом сцен](Scenegraph/ru.md) Coin, таким, как [трёхмерный вид](3D_view/ru.md) FreeCAD, или даже создавать новые. Pivy не требуется для компиляции FreeCAD, но требуется во время выполнения при запуске основанных на Python верстаков, которые создают фигуры на экране, такие как [Draft](Draft_Workbench/ru.md) и [Arch](Arch_Workbench/ru.md). Из-за этого Pivy обычно устанавливается при установке дистрибутива FreeCAD.


</div>

When imported in a running Python interpreter, Pivy allows us to communicate directly with any running Coin [scenegraph](Scenegraph.md), such as the [3D view](3D_view.md), or even to create new ones. Pivy is not required to compile FreeCAD, but it is required at runtime when running Python-based workbenches that create shapes on screen, like [Draft](Draft_Workbench.md) and [BIM](BIM_Workbench.md). Because of this, Pivy is normally installed when installing a distribution of FreeCAD.

Библиотека Coin разделена на несколько частей, собственно Coin, для управления графами сцен и привязки к различным GUI системам, таким как Windows или Qt. Если эти модули присутствуют в системе, они также доступны для Pivy. Модуль Coin всегда присутствует, и это то что мы будем использовать в любом случае, поэтому мы не должны заботится о привязках нашего трёхмерного отображения к различным интерфейсам, что уже сделано в FreeCAD. Все что вам нужно, так это сделать это:


```python
from pivy import coin
```



## Древо сцены 

Мы видели на странице [Scenegraph](Scenegraph/ru.md), как организована типичная сцена Coin. Все что появляется в [трехмерный вид](3D_view.md) - это граф сцен Coin, организованный так же. У нас есть один корневой узел, и все объекты на экране его потомки.

FreeCAD обладает простым способом получит доступ к корневому узлу(вершине) древа сцена 3D вида:


```python
sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
print(sg)
```

Это вернет корневой узел:


```python
<pivy.coin.SoSelection; proxy of <Swig Object of type 'SoSelection *' at 0x360cb60> >
```

Мы сразу же можем просмотреть потомков, нашей сцены:


```python
for node in sg.getChildren():
    print(node)
```

Некоторые из этих узлов, такие как ноды `SoSeparator` или `SoGroup`, также могут обладать потомками. Полный список доступных объектов Сoin можно найти в официальной документации Сoin.

Давайте, сейчас, попробуем добавить что-нибудь в наше древо сцены. Мы добавим милейший красный куб:


```python
col = coin.SoBaseColor()
col.rgb = (1, 0, 0)
cub = coin.SoCube()
myCustomNode = coin.SoSeparator()
myCustomNode.addChild(col)
myCustomNode.addChild(cub)
sg.addChild(myCustomNode)
```

Теперь попробуем следующее:


```python
col.rgb = (1, 1, 0)
```

Как видите, все по прежнему доступно и изменяемо на лету. Не нужно что-нибудь пересчитывать или перересовывать, Coin позаботится обо всем. Вы можете что-то в ваше древо сцен, изменить свойства, скрыть этот объект, показать временный объект, что угодно. Конечно это касается только отображения трехмерного вида. Это отображение получается при считывании FreeCAD-ом файла при открытии, и когда объект нужно перечитать. Так что, если вы изменили какой-нибудь аспект в существующем FreeCAD объекте,эти изменения будут потеряны, если объект перечитают, или же повторно откроют.

Как уже упоминалось, в графе сцен openInventor важен порядок. Каждый узел влияет на то, что будет дальше. Например, если мы хотим иметь возможность переместить наш куб, нам нужно добавить узел `SoTranslation` **перед** кубом:


```python
col = coin.SoBaseColor()
col.rgb = (1, 0, 0)
trans = coin.SoTranslation()
trans.translation.setValue([0, 0, 0])
cub = coin.SoCube()
myCustomNode = coin.SoSeparator()
myCustomNode.addChild(col)
myCustomNode.addChild(trans)
myCustomNode.addChild(cub)
sg.addChild(myCustomNode)
```

Чтобы переместить наш куб, мы можем теперь сделать:


```python
trans.translation.setValue([2, 0, 0])
```

Наконец удалим что-нибудь, введя:


```python
sg.removeChild(myCustomNode)
```


{{Top}}



## Обратные вызовы 

[Функция обратного вызова](http://ru.wikipedia.org/wiki/Callback_(программирование)) это система, позволяет библиотекам вроде нашей библиотеки Coin , возвращать вызов, то есть возможность вызова определенных функций с вашего запущенного объекта Python. Таким образом Coin может сообщить вам, что на сцене произошло конкретное событие. Coin может наблюдать за множеством различных вещей, таких как положение курсора, нажатия клавиши мыши, нажатые клавиши клавиатуры, и многое другое.

FreeCAD способен легко использовать такие функции обратного вызова:


```python
from pivy import coin

class ButtonTest:
    def __init__(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.callback = self.view.addEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.getMouseClick) 

    def getMouseClick(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == coin.SoMouseButtonEvent.DOWN:
            print("Alert!!! A mouse button has been improperly clicked!!!")
            self.view.removeEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.callback)

ButtonTest()
```


<div class="mw-translate-fuzzy">

Функция обратного вызова, должна быть инициализирована объектом, потому что объект должен по прежнему работать, когда случатся обратные вызовы. Смотри также [полный список](Code_snippets#Observing_mouse_events_in_the_3D_viewer_via_Python.md) возможных событий и их параметров, или официальную документацию Coin.


</div>


{{Top}}



## Документация

К сожалению, Pivy не обладает собственной документацией. Однако, так как это оболочка библиотекиCoin, вы можете читать справку по C++. В этом случает Вам нужно лишь переводить стиль наименования классов C++ в стиль Python.

В C++:


```python
SoFile::getClassTypeId()
```

В Pivy:


```python
SoFile.getClassId()
```

-   [Coin3D](https://github.com/coin3d) homepage.
-   [Pivy](https://github.com/coin3d/pivy) homepage.
-   [Coin3D wiki](https://github.com/coin3d/coin/wiki), at GitHub.
-   [Coin3D wiki documentation](https://github.com/coin3d/coin/wiki/Documentation), at GitHub.
-   [Coin3D Documentation](https://coin3d.github.io/Coin/html/), latest automatically generated Doxygen documentation.
-   [(Open)Inventor Mentor](https://webdocs.cs.ualberta.ca/~graphics/books/mentor.pdf) - recommended.

### Older

These links provide reference documentation for Coin v3.x. The differences with v4.x are minimal, so they may still be useful.

-   [Coin3D Documentation](https://coin3d.bitbucket.io/Coin/index.html), at BitBucket.
-   [Coin3D Documentation](https://grey.colorado.edu/coin3d/index.html), at University of Colorado.
-   [Open Inventor Reference Documentation](https://mevislabdownloads.mevis.de/docs/current/MeVis/ThirdParty/Documentation/Publish/OpenInventorReference/index.html), by MeVisLab.


{{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Pivy/ru
