# PySide/ru
{{TOCright}}

## Введение


<div class="mw-translate-fuzzy">

[PySide](PySide/ru.md) - это библиотека, дающая доступ к инструментарий кроссплатформенного графического интерфейса пользователя Qt. Qt представляет собой набор библиотек C++, но с помощью PySide можно использовать те же компоненты из [Python](Python/ru.md). Любой сложный графический интерфейс, который может быть создан в C++, может быть так же создан и изменен в Python. Преимущество использования Python заключается в том, что интерфейсы Qt можно разрабатывать и тестировать вживую, без нужды компилировать исходные файлы.


</div>

When you install FreeCAD, you should get both Qt and PySide as part of the package. If you are [compiling](Compiling.md) yourself then you must verify that these two libraries are installed in order for FreeCAD to run correctly. Of course, PySide will only work if Qt is present.

In the past, FreeCAD used PyQt, another Qt binding for Python, but in 2013 ([commit 1dc122dc9a](https://github.com/FreeCAD/FreeCAD/commit/1dc122dc9a)) the project migrated to PySide because it has a more permissible [license](licence.md).

For more information see:

-   [Wikipedia:PySide](https://en.wikipedia.org/wiki/PySide)
-   [Differences Between PySide and PyQt](https://wiki.qt.io/Differences_Between_PySide_and_PyQt)

![](images/PySideScreenSnapshot1.jpg ) ![](images/PySideScreenSnapshot2.jpg ) 
*Examples created with PySide. Left: a simple dialog. Right: a more complex dialog with graphs.*

## PySide в FreeCAD с Qt5 

FreeCAD был разработан для использования с Python 2 и Qt4. Поскольку эти две библиотеки устарели, FreeCAD перешёл на Python 3 и Qt5. В большинстве случаев этот переход произошёл без отказа от обратной совместимости.


<div class="mw-translate-fuzzy">

Модуль `PySide` даёт поддержку Qt4, а `PySide2` - Qt5. Однако в FreeCAD нет необходимости использовать `PySide2` напрямую, благодаря специальному модулю `PySide` для поддержки Qt5.


</div>

Модуль `PySide` располагается в каталоге `Ext/` установки FreeCAD, скомпилированной для Qt5. 
```python
/usr/share/freecad/Ext/PySide
```


<div class="mw-translate-fuzzy">

Этот модуль просто импортирует необходимые классы из `PySide2`, но размещает их в пространстве имён `PySide`. Это значит, что в большинстве случаев тот же самый код может быть использован как с Qt4, так и с Qt5, когда тот импортирует единый модуль `PySide`.


</div>


```python
PySide2.QtCore -> PySide.QtCore
PySide2.QtGui -> PySide.QtGui
PySide2.QtSvg -> PySide.QtSvg
PySide2.QtUiTools -> PySide.QtUiTools
```

Единственный необычный аспект это то, что классы `PySide2.QtWidgets` помещены в пространстве имён `PySide.QtGui`. 
```python
PySide2.QtWidgets.QCheckBox -> PySide.QtGui.QCheckBox
``` {{Top}}

## Примеры использования PySide 


<div class="mw-translate-fuzzy">

-   [Примеры PySide для начинающих](PySide_Beginner_Examples/ru.md), Hello World, анонсы, ввод текста, ввод чисел.
-   [Примеры PySide среднего уровня](PySide_Intermediate_Examples/ru.md), изменение размеров окон, сокрытие виджетов, всплывающие меню, позиционирование мыши, события мыши
-   [Сложные примеры PySide](PySide_Advanced_Examples/ru.md), много виджетов.


</div>

Примеры PySide разделены на 3 части, дифференцированные по уровню воздействия PySide, Python и внутренних компонентов FreeCAD. На первой странице представлен обзор PySide, а на второй и третьей страницах приведены примеры кода на разных уровнях.

Ожидается, что эти примеры полезны для начала, и после этого пользователь может обратиться к другим ресурсам онлайн или официальной документации. {{Top}}

## Документация

There are some differences in handling of widgets in Qt4 (PySide) and Qt5 (PySide2). The programmer should be aware of these incompatibilities, and should consult the official documentation if something doesn\'t seem to work as expected on a given platform. Nevertheless, Qt4 is considered obsolete, so most development should target Qt5 and Python 3.

The PySide documentation refers to the Python-style classes; however, since Qt is originally a C++ library, the same information should be available in the corresponding C++ reference.

-   [Qt Modules](https://doc.qt.io/qtforpython/modules.html) available from PySide2 (Qt5).
-   [All Qt classes by module](https://doc.qt.io/qt-5/modules-cpp.html) in Qt5 for C++.
-   [Qt Modules](https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/index.html) available from PySide (Qt4).


{{Top}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > PySide/ru
