# Manual:Parametric objects/ru
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC}}


<div class="mw-translate-fuzzy">

FreeCAD спроектирован для параметрического моделирования. Это значит, что создаваемая Вами геометрия не свободно лепится, а производится правилами и параметрами. Например, цилиндр должен создаваться по радиусу и высоте. С этими двумя параметрами программа имеет достаточно информации для построения цилиндра.


</div>


<div class="mw-translate-fuzzy">

Параметрические объекты в FreeCAD это фактически небольшие куски программ, запускаемые при изменении параметров. Объекты могут иметь множество различных типов параметров: числа (целые вроде 1, 2, 3 или действительные с плавающей точкой вроде 3.1416), реальные размеры (1mm, 2.4m, 4.5ft), координаты (x,y,z), текстовые строки (\"Привет!\") и другие.


</div>


<div class="mw-translate-fuzzy">

В примере ниже твердотельный кубический объект (Pad) базируется на плоской прямоугольной форме (Sketch) и имеет дальность вытягивания. С этими двумя параметрами он производит твёрдое тело вытягиванием базовой формы на данное расстояние. Мы можете затем использовать этот объект как базу для дальнейших операций, таких как рисование новых двумерных форм на его грани (Sketch001) и затем выреза (Pocket), вплоть до получения финального объекта.


</div>

![](images/FreeCAD_022_PArametricDesignPlate.png )

On the top face of the plate you sketch a circle of a given diameter d. You then use this circle to create a pocket (remove material) from the original plate.

![](images/FreeCAD_022_ParametricDesignPocket.png )

If you decide to change either of the dimensions of the plate, or of the circle, the final object would be also modified. Thanks to the use of a parametric design approach, there is no need to redo the object from the beginning.


<div class="mw-translate-fuzzy">

1.  Рекомпиляция не всегда автоматическая. Тяжёлые операции, которые должны модифицировать большую часть вашего документа и должны занять много времени, не производятся автоматически. Вместо этого объекты (и все зависимые от них объекты) отмечаются как нуждающиеся в рекомпиляции (в древе проекта рядом с ними появляется маленькая голубая иконка). После этого Вы должны нажать кнопку рекомпиляции (или **Правка->Обновить**), чтобы перекомпилировать все отмеченные объекты.
2.  Древо зависимости должно всегда идти в том же направлении. Петли недопустимы (см. [DAG](Glossary/ru#Directed_Acyclic_Graph.md), и [DAG view](DAG_view/ru.md)). Вы можете иметь объект, зависящий от объекта Б, который зависим от объекта В, но Вы не можете иметь объект А, который зависит от объекта Б, зависимого от объекта А. Это будет круговая зависимость. Однако Вы можете иметь множество объектов зависимых от одного объекта, например, объект Б и В может зависеть от объекта А. Меню **Инструменты -> Граф зависимостей** покажет Вам диаграмму зависимостей вроде картинки выше. Это может быть полезно для определения проблем.


</div>

In FreeCAD\'s parametric modeling process, examining the dependency tree of an object provides a clear insight into the sequential build and relationships within a model. At the foundation of the structure in the above example is the \'Plate Sketch,\' which serves as the base for the initial form of the model. A \'Pad\' operation is then applied, which adds material to this foundational sketch, effectively creating a three-dimensional structure from the two-dimensional base.

Following this, a \'Circle Sketch\' is drafted on the newly formed surface. This circle forms the basis for the subsequent \'Pocket\' operation. The pocket operation strategically removes material from the structure, essentially carving out a portion based on the circle sketch. This process of adding and then subtracting material allows for complex geometries and features to be integrated into the basic model seamlessly.

Through this sequence of operations---starting from the base sketch, adding volume with a pad, and creating detailed features with additional sketches and pockets---the final object takes shape. Each step in this chain depends on its predecessor, illustrating the interconnected nature of parametric design in FreeCAD.

![](images/FreeCAD_022_ParametricDesignDependGraph.png )


<div class="mw-translate-fuzzy">

Не все объекты в FreeCAD параметрические. Зачастую импортируемая из других файлов геометрия не содержит параметров, и будет простой, не параметрической. Тем не менее, они обычно могут использоваться как база или стартовая точка для новых параметрических объектов, разумеется, в зависимости от их требований и качества импортируемой геометрии.


</div>

Все объекты, параметрические или нет, будут иметь множество базовых параметров, таких как Имя, уникальное в документе и не редактируемое, Метку, представляющую собой редактируемое пользовательское имя, и [размещение](placement/ru.md), устанавливающее позицию в трёхмерном пространстве.


<div class="mw-translate-fuzzy">

В конце стоит отметить, что пользовательские параметрические объекты [легко программировать на python](Scripted_objects/ru.md).


</div>

**Читать далее**


<div class="mw-translate-fuzzy">

-   [Редактор параметров](Property_editor/ru.md)
-   [Как программировать параметрические объекты](Scripted_objects/ru.md)
-   [Расположение объектов в FreeCAD](Placement/ru.md)
-   [Включение графа зависимостей](Std_ExportGraphviz/ru.md)


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Parametric objects/ru
