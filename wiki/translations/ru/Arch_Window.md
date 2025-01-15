---
 GuiCommand:
   Name: Arch_Window
   Name/ru: Окно
   MenuLocation: Архитектура , Окно
   Workbenches: Arch_Workbench/ru
   Shortcut: **W** **I**
   SeeAlso: Arch_Wall/ru, Arch_Add/ru
---

# Arch Window/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

[Arch Window](Arch_Window/ru.md) (окно) это базовый объект для всех типов \"внедряемых\" объектов, таких как окна, двери и т.д\... Он спроектирован так, что может быть и независим, и \"базироваться\" на другом компоненте вроде [стены](Arch_Wall/ru.md), [структуры](Arch_Structure/ru.md), или [крыши](Arch_Roof/ru.md). У него своя собственная геометрия, которая может быть сделана из нескольких твердотельных компонентов (обычно оконная рама и внутренняя панель), и определяет объём, которые будет вычитаться из базового объекта, чтобы сделать проём.


</div>

Объекты Window базируются на замкнутых двумерных объектах, вроде [прямоугольников](Draft_Rectangle/ru.md) или [эскизов](Sketcher_Workbench.md), которые используются для определения их внутренних компонентов. Базовые двумерные объекты должны, следовательно, содержать несколько замкнутых многоугольников, которые могут быть скомбинированы для создания заполненных панелей (один многоугольник) или рамок (несколько многоугольников).


<div class="mw-translate-fuzzy">

Инструмент Window предлагает несколько **предустановок**, это позволяют пользователю создать общие типы окон и дверей с некоторыми редактируемыми параметрами, без необходимости создавать вручную двумерные объекты и компоненты.


</div>


<div class="mw-translate-fuzzy">

Вся информация, применимая к [Arch Window](Arch_Window/ru.md), также относится к [Arch Door](Arch_Door/ru.md), поскольку это один и тот же базовый объект. Основное различие между окном и дверью состоит в том, что у двери есть внутренняя панель, которая показана непрозрачной (сама дверь), в то время как окно имеет частично прозрачную панель (стекло).


</div>

<img alt="" src=images/Arch_Window_example2.jpg  style="width:600px;"> 
*Более сложное окно, созданное на базе [эскиза](Sketcher_Workbench.md). При входе в режим редактирования окна, Вы можете создать различные компоненты, установить их толщину, и выделить и назначить многоугольники из эскиза для них.*



## Применение



### Применение предустановок 


<div class="mw-translate-fuzzy">

1.  Нажмите кнопку **<img src="images/Arch_Window.svg" width=16px> [Окно](Arch_Window/ru.md)
**, или нажмите клавиши **W**, затем **I**
2.  Выберите предустановку из списка
3.  Заполните желаемые параметры
4.  В [трёхмерном просмотре](3D_view/ru.md) переместите окно в то место, где вы хотите его разместить. Если вы наведете указатель на [Arch Wall](Arch_Wall/ru.md), контур окна должен выровняться относительно лицевой стороны этого объекта.
5.  Щелкните мышью на [трёхмерном просмотре](3D_view/ru.md) или трижды нажмите клавишу **Enter**, чтобы подтвердить координаты X, Y, Z места размещения.


</div>

#### Additional presets 

If you install the [Parts Library](Parts_Library_Workbench.md) from the [Addon Manager](Std_AddonMgr.md), the window tool will search this library for additional presets. These presets are FreeCAD files containing a single window based on a parametric sketch that has named constrains. You may place additional presets in the **parts_library** directory so that they are found by the window tool.


**$ROOT_DIR/Mod/parts_library/Architectural Parts/Doors/Custom/**

**$ROOT_DIR/Mod/parts_library/Architectural Parts/Windows/Custom/**

-   The **$ROOT_DIR** is the user directory where FreeCAD configuration files, macros, and external workbenches are stored. It can be found be entering `FreeCAD.getUserAppDataDir()` in the [Python console](Python_console.md).
    -   On Linux it is usually **/home/username/.local/share/FreeCAD/** (<small>(v0.20)</small> ) or **/home/username/.FreeCAD/** ({{VersionMinus|0.19}})
    -   On Windows it is usually **C:\Users\username\Application Data\FreeCAD\**
    -   On Mac OSX it is usually **/Users/username/Library/Preferences/FreeCAD/**
-   The subdirectory name **Custom** is just a suggestion, any name can be used. But the files must be placed in one or more subdirectories inside the **Doors** or **Windows** directories.




<div class="mw-translate-fuzzy">

### Создание с нуля 


</div>


<div class="mw-translate-fuzzy">

1.  По желанию, выделите грань объекта, где Вы хотите вставить окно
2.  Переключитесь на [верстак Sketcher](Sketcher_Workbench/ru.md)
3.  Создайте новый эскиз
4.  Нарисуйте одну или более замкнутых ломаных (петель)
5.  Закройте эскиз
6.  Переключитесь обратно на [верстак Arch](Arch_Workbench/ru.md)
7.  Нажмите кнопку **<img src="images/Arch_Window.svg" width=16px> [Arch Window](Arch_Window/ru.md)
**, или нажмите клавиши **W**, затем **I**
8.  Чтобы настроить компоненты окна и различные свойства, войдите в окно [панели задач](task_panel/ru.md), дважды щелкнув созданный объект в [древе проекта](tree_view/ru.md).


</div>



## Предустановки

Доступны следующие предустановки:


<div class="mw-translate-fuzzy">

Image:ParametersDoorGlass.svg\|Glass door (стеклянная дверь) Image:ParametersDoorSimple.svg\|Simple door (простая дверь) Image:ParametersWindowDouble.svg\|Double-opening window (двустворчатое окно) Image:ParametersWindowFixed.svg\|Fixed window (глухое окно) Image:ParametersWindowSimple.svg\|Single-opening window (одностворчатое окно) Image:ParametersWindowStash.svg\|Sash-opening window (сдвижное окно)


</div>



## Создание компонентов 


<div class="mw-translate-fuzzy">

Окна могут включать 3 типа компонентов: панели, рамы и жалюзи. Панели и жалюзи делаются из замкнутых ломаных, которые выдавливаются, в то время как рамы делаются из двух и более замкнутых ломаных, где каждый выдавливается, затем меньший вычитается из большего. Вы можете иметь доступ, создавать, модифицировать и удалять компоненты в окне в режиме редактирования (дважды кликнув по окну в древе проекта). У компонента имеются следующие параметры:


</div>

-   **Name**: имя компонента
-   **Type**: тип компонента. Может быть \"Frame\", \"Glass panel\", \"Solid panel\" или \"Louvres\"
-   **Wires**: разделяемый запятыми список ломаных, на которых базируется компонент
-   **Thickness**: толщина выдавливания компонента
-   **Z Offset**: расстояние между компонентом и его базовой ломанной
-   **Hinge**: позволяет выбрать край базового 2D-объекта, а затем установить этот край в качестве места для петель этого компонента и следующих в списке.
-   **Opening mode**: если вы определили край для петель в этом компоненте или любом другом ранее в списке, установка режима открытия позволит окну казаться открытым или отображать 2D-символы открытия в плане или на фасаде.

<img alt="" src=images/Arch_Window_options.jpg  style="width:600px;">



## Опции


<div class="mw-translate-fuzzy">

-   Оборудование обладает такими же общими свойствами и моделью поведения, как и все остальные [компоненты верстака Arch](Arch_Component/ru.md)
-   Если метка **Auto-include** на панели задач создания окна не снята, окно не будет вмонтировано ни в один несущий объект при его создании.
-   Добавить выделенное окно в [стену](Arch_Wall/ru.md), выделив оба и нажатием кнопки **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add/ru.md)**.
-   Убрать выбранное окно из [стены](Arch_Wall/ru.md) выделив окно, затем нажав кнопку **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove/ru.md)**.
-   При использовании предустановок часто полезно включить [привязку](Draft_Snap/ru.md) \"Near\", чтобы Вы смогли привязать окно к существующей грани.
-   Отверстие, создаваемое окном в базовом объекте, определяется двумя параметрами: **Hole Depth** и **Hole Wire** ({{Version/ru|0.17}}). Число Hole Wire может быть получено в трёхмерном окне из панели задач окна, доступной при двойном клике на окне в древе проектов
-   Окна могут использовать [Multi-Materials](Arch_MultiMaterial/ru.md). Окно ищет в присоединённом Multi-Material слои материала с теми же именами для каждого компонента окна, и используют их при нахождении. Например, компонент под названием \"OuterFrame\" ищет в приложеннном Multi-Material материальный слой под именем \"OuterFrame\". Если этот слой найден, его материал будет назначен компоненту OuterFrame. Значение толщины слоя материала отбрасывается.


</div>



## Условное обозначение направления открывания окон 


**Смотрите также:**

[Руководство по обозначению направления открытия окон и дверей](Tutorial_for_open_windows/ru.md)


<div class="mw-translate-fuzzy">

Двери и окна могут отображаться частично или полностью открытыми в 3D-модели или могут отображать открывающие символы как в плане, так и в области высоты. Следовательно, они также появятся в извлеченных 2D-представлениях, сгенерированных [Draft Shape2DView](Draft_Shape2DView/ru.md) или [TechDraw Workbench](TechDraw_Workbench/ru.md) или [Drawing Workbench](Drawing_Workbench/ru.md). Чтобы получить это, по крайней мере один из компонентов окна должен иметь шарнир и режим открытия (см. [Создание компонентов](#Создание_компонентов.md) выше). Затем вы можете настроить внешний вид окна, используя свойства **Opening**, **Symbol Plan** или **Symbol Plan**:


</div>

<img alt="" src=images/Arch_window_openings.png  style="width:600px;"> 
*A door showing the symbol plan, symbol elevation and opening properties at work*

## Defining window types 

Windows can also take advantage of other tools, specifically [PartDesign](PartDesign_Workbench.md) workflows, to define a type. A type is an object that defines the shape of the window. This is specially well suited to work with [App Parts](App_Part.md):

<img alt="" src=images/Arch_window_type_example.png  style="width:800px;">

[Download the example file shown above](https://github.com/FreeCAD/Examples/raw/master/Arch_Example_Files/Window_Type.FCStd)

### Example workflow 

-   Create a window frame object, a glass panel, and any other window component you need, using [Part Workbench](Part_Workbench.md) or [PartDesign](PartDesign_Workbench.md) tools.
-   For example, create a base rectangular sketch for your window, then a profile sketch for the frame, and create a [Part Sweep](Part_Sweep.md) to sweep the profile around the base sketch. Create a [Part Offset2D](Part_Offset2D.md) from the base sketch, then a [Part Extrude](Part_Extrude.md) to create the glass panel
-   Make sure all these pieces have a unique, meaningful name (for example, \"Frame\" or \"Glass Panel\")
-   Create an [App Part](App_Part.md), and place all your subcomponents in it
-   Create a volume to be subtracted from the wall, for example by extruding the base sketch. Add this volume to the App Part. Make sure the volume is turned off
-   If using FreeCAD version 0.19 or later, you can add 3 properties to your App Part, by right-clicking its properties view, and check \"Show All\". Add the following properties (all of them are optional, the group doesn\'t matter):
    -   **Height** as a PropertyLength and link it, for example, to a vertical constraint of your base sketch
    -   **Width** as a PropertyLength and link it, for example, to a horizontal constraint of your base sketch
    -   **Subvolume** as a PropertyLink and link it to the volume to be subtracted that we created above
    -   **Tag** as a PropertyString

Our window type is now ready. We can create window objects from it, simply by selecting the App Part and pressing the window button. The \"Height\", \"Width\", \"Subvolume\" and \"Tag\" properties of the window will be linked to the corresponding property of the App Part, if existing.

### Materials

To build a material for type-based windows:

-   Create a [multi-material](Arch_MultiMaterial.md)
-   Create one entry in the multi-material for each component of your App Part. For example, one \"Frame\", one \"Glass panel\" as we used above. Make sure to use the exact same name.
-   Attribute that multi-material to each of the windows derived from the same type

You can use any other kind of workflow than the one described above, the important points to remember are:

-   The type object must be one object, no matter the type (App Part, PartDesign Body, Part Compound, or even another Arch Window)
-   The type object must have a \"Subvolume\" property (linked to the window\'s Subvolume property) for openings in host objects to work
-   The type object must have a \"Group\" property with different children with same names as multi-material items for multi-materials to work



## Свойства

### Data


{{TitleProperty|Window}}


<div class="mw-translate-fuzzy">

-    **Height**: Высота окна

-    **Width**: Ширина окна

-    **Hole Depth**: Глубина углубления, созданного окном в базовом объекте

-    **Hole Wire**: Номер многоугольника, используемого для создания проёма окна. Значение может быть установлено графически двойным кликом на окне в древе проекта. Если установить значение в ноль, для проёма будет автоматически браться наибольший многоугольник.

-    **Window Parts**: Список струн (5 струн на компонент, установка опций компонента выше)

-    **Louvre Width**: Если какой-либо из компонентов установлен в \"Louvres (жалюзи)\", этот параметр определяет размер элементов жалюзи

-    **Louvre Spacing**: Если какой-либо из компонентов установлен в \"Louvres (жалюзи)\", этот параметр определяет пробел между элементами жалюзи

-    **Opening**: все компоненты, для которых установлен режим открытия, и при условии, что в них или в более раннем компоненте в списке определен шарнир, будут отображаться открытыми в процентах, определяемых этим значением.

-    **Symbol Plan**: отображение двумерного символа проема на виде сверху

-    **Symbol Elevation**: показывает двумерный символ проема на фасаде


</div>



## Программирование


**См. так же:**

[Arch API](Arch_API/ru.md) и [Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


<div class="mw-translate-fuzzy">

Инструмент создания окон может использоваться в [макросах](Macros/ru.md) и их консоли [Python](Python/ru.md), с использованием следующих функций:


</div>


```python
Window = makeWindow(baseobj=None, width=None, height=None, parts=None, name="Window")
```


<div class="mw-translate-fuzzy">

-   Создает объект `Window` на основе `baseobj`, который должен быть правильно сформированной замкнутой [ломанной](Draft_Wire/ru.md) или [эскизом Sketcher](Sketcher_Workbench/ru.md).
-   Если доступно, устанавливает `width`, `height` и `name` (метку) окна.
-   Если `baseobj` не является замкнутой формой, инструмент может не создать правильную сплошную фигуру.


</div>

Пример:


```python
import FreeCAD, Draft, Arch

Rect1 = Draft.makeRectangle(length=900, height=3000)
Window = Arch.makeWindow(Rect1)
FreeCAD.ActiveDocument.recompute()
```

Вы можете так же создать окно из предустановок.


```python
Window = makeWindowPreset(windowtype, width, height, h1, h2, h3, w1, w2, o1, o2, placement=None)
```


<div class="mw-translate-fuzzy">

-   Создает объект `Window` на основе `windowtype`, который должен быть одним из имен, определенных в `Arch.WindowPresets`
    -   Некоторые из этих предустановок: `"Fixed"`, `"Open 1-pane"`, `"Open 2-pane"`, `"Sash 2-pane"`, `"Sliding 2-pane"`, `"Simple door"`, `"Glass door"`, `"Sliding 4-pane"`.

-    `width`и `height` определяют общий размер объекта в миллиметрах.

-   Параметры `h1`, `h2`, `h3` (вертикальные смещения), `w1`, `w2` (ширина), `o1` и `o2` (горизонтальные смещения) определяют разные расстояния в миллиметрах и зависят от типа создаваемой предустановки.

-   Если задано `placement`, используется оно.


</div>

Пример:


```python
import FreeCAD, Arch

base = FreeCAD.Vector(2000, 0, 0)
Axis = FreeCAD.Vector(1, 0, 0)
place=FreeCAD.Placement(base, FreeCAD.Rotation(Axis, 90))

Door = Arch.makeWindowPreset("Simple door",
                             width=900, height=2000,
                             h1=100, h2=100, h3=100, w1=200, w2=100, o1=0, o2=100,
                             placement=place)
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Arch Window/ru
