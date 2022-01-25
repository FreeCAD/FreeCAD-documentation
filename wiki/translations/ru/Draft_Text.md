---
- GuiCommand:/ru
   Name/ru:Текст
   Name:Draft_Text
   MenuLocation:Annotation → Текст
   Workbenches:[Draft](Draft_Workbench/ru.md), [Arch](Arch_Workbench/ru.md)
   Shortcut:**T** **E**
   Version:0.7
   SeeAlso:[Метка](Draft_Label/ru.md), [Фигура из текста](Draft_ShapeString/ru.md)
---

# Draft Text/ru

## Описание


<div class="mw-translate-fuzzy">

Инструмент **<img src="images/Draft_Text.svg" width=16px> [Текст](Draft_Text.md)** позволяет добавить в документ многострочную текстовую область в указанную точку. Он использует предварительно выбранный [Draft Linestyle](Draft_Linestyle/ru.md), установленный в [Draft Tray](Draft_Tray/ru.md).


</div>

To create a text element with an arrow use the [Draft Label](Draft_Label.md) command instead.


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Text_example.png  style="width:400px;"> 
*Для размещения текстового поля требуется одна точка*


</div>

## Использование

See also: [Draft Tray](Draft_Tray.md) and [Draft Snap](Draft_Snap.md).


<div class="mw-translate-fuzzy">

1.  Нажмите кнопку **<img src="images/Draft_Text.svg" width=16px> [Текст](Draft_Text/ru.md)
**, или нажмите клавишу **T**, а затем**E**
2.  Укажите точку на трёхмерном виде или задайте координаты и нажмите кнопку **<img src="images/Draft_AddPoint.svg" width=16px> add point**.
3.  Введите желаемый текст нажимая **Enter** между каждыми строками
4.  Дважды нажмите **Enter** для завершения.


</div>

## Опции

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Для указания координат вручную, введите число и нажимайте **ENTER** для перехода между координатами X, Y и Z. Вы можете нажать кнопку **<img src="images/Draft_AddPoint.svg" width=16px> добавить точку**, когда у вас есть нужные значения для вставки точки.
-   Удерживайте **Ctrl** при размещении текста, чтобы принудительно установить [привязку](Draft_Snap/ru.md) вашей точки в ближайшее место привязки, независимо от расстояния.
-   Нажмите **Enter** или **↓ Стрелка вниз**, чтобы ввести новую строку текста.
-   Нажмите **↑ Стрелка вверх**, чтобы отредактировать предыдущую строку текста.
-   Дважды нажмите **Enter** или **↓ Стрелка вниз**, чтобы завершить редактирование текста.
-   Нажмите **Esc** или кнопку **Close**, чтобы прервать выполнение текущей команды.


</div>

## Примечания

-   A Draft Text can be edited by double-clicking it in the [Tree view](Tree_view.md). <small>(v0.20)</small> 
-   Draft Texts created with [FreeCAD version 0.18](Release_notes_0.18.md) are not backward compatible.

## Свойства

See also: [Property editor](Property_editor.md).

A Draft Text object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated.

### Данные


{{TitleProperty|Основные}}


<div class="mw-translate-fuzzy">

-    **Положение**: указывает базовую точку первой линии текстового блока.

-    **Текст**: указывает содержимое текстового блока как список строк, каждый элемент списка, разделённый запятыми, показывает новую строку


</div>

### Вид


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the text. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the text.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|3D text}} the text will be displayed in a plane defined by its **Placement**. If it is {{value|2D text}} the text will always face the camera. This is an inherited property.


{{TitleProperty|Graphics}}

-    **Line Color|Color**: not used.

-    **Line Width|Float**: not used.


{{TitleProperty|Text}}


<div class="mw-translate-fuzzy">

-    **Режим отображения**: если это «3D текст», текст будет выровнен по осям сцены, изначально лежащим в плоскости XY; если это «2D-текст», текст всегда будет смотреть в камеру.

-    **Шрифт**: указывает шрифт для отображения текста. Может быть название шрифта, например \"Arial\", название стиля, например, \"sans\", \"serif\" или \"mono\", название семейства, например, \"Arial,Helvetica,sans\", или название со стилем, например \"Arial:Bold\". Если указанный шрифт не найден в системе, то будет использован основной.

-    **Размер шрифта**: указывает размер символов текста. Если текстовый объект создается в древе проекта, но текст не отображается, увеличивайте размер текста, пока он не станет видим.

-    **Выравнивание**: указывает выравнивание текста налево, направо или по центру от базовой точки.

-    **Межстрочное расстояние**: указывает расстояние между строк текста.


</div>

## Программирование


**См. так же:**

[Draft API](Draft_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Инструмент Текст может быть использован в [макросах](macros/ru.md) и из консоли [Python](Python/ru.md) следующими функциями:


</div>


```python
text = make_text(string, placement=None, screen=False)
```


<div class="mw-translate-fuzzy">

-   Создать объект `Text` в `point`, определённой как `FreeCAD.Vector`.

-    `stringlist`это строка, или список строк, если это список, каждый элемент показывается в отдельной строке.

-   Если `screen` равен `True`, текст всегда ориентируется в направлении просмотра камеры, иначе выравнивается по осям сцены и лежит в плоскости XY.


</div>

The view properties of `text` can be changed by overwriting its attributes; for example, overwrite `ViewObject.FontSize` with the new size in millimeters.

Пример:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

t1 = "This is a sample text"
p1 = App.Vector(0, 0, 0)

t2 = ["First line", "second line"]
p2 = App.Vector(1000, 1000, 0)

text1 = Draft.make_text(t1, p1)
text2 = Draft.make_text(t2, p2)
text1.ViewObject.FontSize = 200
text2.ViewObject.FontSize = 200

zaxis = App.Vector(0, 0, 1)

t3 = ["Upside", "down"]
p3 = App.Vector(-1000, -500, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 180))
text3 = Draft.make_text(t3, place3)
text3.ViewObject.FontSize = 200

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Text/ru
