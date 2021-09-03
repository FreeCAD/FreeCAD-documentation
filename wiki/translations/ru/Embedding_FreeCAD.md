


{{TOCright}}

## Introduction

FreeCAD может импортироваться как модуль [Python](Python/ru.md) в другие программы или в автономную консоль python, вместе со всеми модулями и компонентами. Можно даже импортировать пользовательский интерфейс FreeCAD как модуль python, но с [некоторыми ограничениями](Embedding_FreeCAD/ru#Caveats.md).

## Использование FreeCAD без GUI 


<div class="mw-translate-fuzzy">

Одно из первых, простых, прямой и полезных приложений , вы можете создать чтобы импортировать FreeCAD документы в ващу программу. В следующем примере, мы импортируем Part геометрию FreeCAD документа в [blender](http://www.blender.org). Это готовый сценарий. Я надеюсь вы будете поражены его простотой:


</div>


{{Code|lang=python|code=
<nowiki>
FREECADPATH = '/opt/FreeCAD/lib' # path to your FreeCAD.so or FreeCAD.dll file
import Blender, sys
sys.path.append(FREECADPATH)
 
def import_fcstd(filename):
   try:
       import FreeCAD
   except ValueError:
       Blender.Draw.PupMenu('Error%t|FreeCAD library not found. Please check the FREECADPATH variable in the import script is correct')
   else:
       scene = Blender.Scene.GetCurrent()
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()

def main():
   Blender.Window.FileSelector(import_fcstd, 'IMPORT FCSTD', 
                        Blender.sys.makename(ext='.fcstd'))    
 
# This lets you import the script without running it
if __name__=='__main__':
   main()
</nowiki>
}}


<div class="mw-translate-fuzzy">

Сперва, вожно убедится что python найдет ваши FreeCAD библиотеки. как только он их найдет, все модули FreeCAD такие как Part, которые мы также будем использовать, будут доступны автоматически. Так что мы просто берес значение переменной sys.path, где описано где python ищет модули, и мы добавляем буть к библиотекам FreeCAD. Это изменение носит временный характер, и будет потеряно когдв мы закроем наш python интепритатор. Другой способ которым вы можете создать ссылку на вашу FreeCAD библиотеку в одном посковых путей python. Я держал путь в константе (FREECADPATH) так что бы было легче другому пользователю сценария настроить его под свою систему.


</div>


{{Code|lang=python|code=
FREECADPATH = '/opt/FreeCAD/lib' # path to your FreeCAD.so or FreeCAD.dll file
import Blender, sys
sys.path.append(FREECADPATH)
}}


<div class="mw-translate-fuzzy">

После того как мы проверили что библиотеки загружены (повторите/исключите последовательность), теперь мы можем работать с FreeCAD, так же как если бы мы были внутри FreeCADовского python интерпритатора. Мы открываем FreeCAD документ который передается нам с помощью функции main() , и мы создаем список список своих объектов. Затем, так как мы решаем заботиться только о геометрии детали «Part», мы проверяем, содержит ли свойство Type каждого объекта «Part», и затем тесселяем ее.


</div>


{{Code|lang=python|code=
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
}}

Трансляция(tesselation- преобразование в сетку) произвела список вершин и список граней, заданных индексами вершин.Это идеальный вариант, так как он точно аналогично блендеру задает сетки. Таким образом, наша задача до смешного проста, мы просто добавим оба списка содержащих вершины и грани в блендере сетку. Когда все будет сделано, мы просто перерисуем экран, и вот оно!


{{Code|lang=python|code=
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()
}}


<div class="mw-translate-fuzzy">

Конечно этот сценарий очень прост (в действительности я создал более продвинутый [здесь](http://yorik.orgfree.com/scripts/import_freecad.py)), вы можете продолжить его, например импортирвав также полигиональные объекты, или импортировав Part геометрию которая не обладает гранями, или импортировав другие файловые форматы которые может читать FreeCAD. Вы также можете экспортировать геометрию в FreeCAD документ, что можно сделать схожим образом. Вы также можете создать диолог, где пользователь может выбрать что импортировать и.т.д\... Красота всего этого заключается в том, что вы позволяете FreeCAD делать фоновую работу вто время как его результаты представляются в программе по вашему выбору.


</div>


**Note:**

checkout [Headless FreeCAD](Headless_FreeCAD.md) for running FreeCAD without the GUI.

## Использование FreeCAD с GUI 

Начиная с версии 4.2, Qt обладает интегрирующей способностью встраивать Qt-GUI-зависящие плагины в не-Qt главные приложения и распространять как привязки к главному приложению.

В особенности, для FreeCAD это означает что он может быть импортирован из другого приложения со всем его интерфейсом где головное приложение имеет полный контроль над FreeCAD, тогда.

Весь python код , для достижения этого, укладывается всего в две строчки


```python
import FreeCADGui 
FreeCADGui.showMainWindow()
```

Если головное приложение основывается на Qt, то это решение должно работать на всех платформах поддерживаемых Qt. Однако, головное приложение должно ссылаться на туже версию Qt что и FreeCAD потому что иначе мы може столкнуться с неожиданными ошибками во время выполнения.

Однако,Для не-Qt преложений, имеется несколько ограничений , вы должны знать об этом. Это решение , вероятно не сработает вместе с остальными инструментальными средствами. Для Windows это работает до тех пор пока головное приложение напрямую основано на Win32 или любом другом инструментальном средстве который внутренне использует Win32 API такие как wxWidgets, MFC или WinForms. Для того чтобы заставить его работать под X11, головное предложение необходимо связать с библиотекой \"glib\".

Обратите внимание, для любого консольного приложения это решение, конечно, не работает, потому что не существует запущенного цикла обработки событий.

## Caveats

Although it is possible to import FreeCAD to an external Python interpreter, this is not a common usage scenario and requires some care. Generally, it is better to use the Python included with FreeCAD, run FreeCAD via command line, or as a subprocess. See [Start up and Configuration](Start_up_and_Configuration.md) for more on the last two options.

Since the FreeCAD Python module is compiled from C++ (rather than being a pure Python module), it can only be imported from a compatible Python interpreter. Generally this means that the Python interpreter must be compiled with the same C compiler as was used to build FreeCAD. Information about the compiler used to build a Python interpreter (including the one built with FreeCAD) can be found as follows: 
```python
>>> import sys
>>> sys.version
'2.7.13 (default, Dec 17 2016, 23:03:43) \n[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]'
```

## Related

-   [Headless FreeCAD](Headless_FreeCAD.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
