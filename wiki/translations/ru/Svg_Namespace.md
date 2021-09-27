# Svg Namespace/ru
**Development of the [[Drawing Workbench]] stopped in FreeCAD 0.16, and the new [[TechDraw Workbench]] aiming to replace it was introduced in v0.17. Both workbenches are still provided in v0.17, but the Drawing Workbench may be removed in future releases.**


{{TOCright}}


<div class="mw-translate-fuzzy">

В _ и используемые в качестве страницы [шаблонов](Drawing_templates/ru.md), несколько пользовательских [атрибутов](http://www.w3schools.com/xml/xml_attributes.asp) могут использоваться первоначально для собственного внутреннего использования FreeCAD, но в будущем могут также использоваться другими приложениями, поддерживающими FreeCAD. Все эти атрибуты начинаются с префикса [пространства имен](http://www.w3schools.com/xml/xml_namespaces.asp) \"freecad:\". URL-адрес пространства имен, определенный в этих документах SVG, относится к этой странице.


</div>

## Применение

Один пиксель = один миллиметр.

Вы должны вставить где-нибудь внутри вашего svg-кода, где вы хотите, чтобы отображалось содержимое чертежа (например, в конце файла, непосредственно перед последним тегом \'\'\'


</svg>

\'\'\'), следующую строку :

 {.xml}



 {.xml}
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
    xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"


Чтобы включить печать в масштабе, реальный размер текста должен быть указан в атрибутах ширины и высоты SVG-тега. Размер документа в пользовательских единицах (px) должен быть указан в атрибуте viewBox.

Следующее должно быть отформатировано, как в примере ниже, где:

-   xxx = ширина в пикселях
-   yyy = высота пикселях

 {.xml}
width="xxxmm"
height="yyymm"
viewBox="0 0 xxx yyy"


Дополнительная информация для рабочего пространства и блока заголовка может быть добавлена и определена на странице [стандартных шаблонов чертежей](Drawing_templates/ru.md).

## Атрибуты

### _

To use any of the **freecad:** attributes in your SVG documents, you must first define the freecad namespace as an attribute of the opening


<svg>

tag:

Defines a text in a template that can be edited by FreeCAD.

Пример:

 {.xml}
<text freecad:EditableText="MyTitleText">
    <tspan>This is a title</tspan>
</text>


### freecad:basepoint1

Defines the first point of a [Draft Dimension](Draft_Dimension.md) object (represented as a group in a SVG document). This attribute is used when importing the SVG fragment in FreeCAD, in order to recreate the dimension object. The group contains paths and other graphical items to correctly render the dimension object in other SVG applications.

Пример:

 {.xml}
<g freecad:basepoint1="0.5 4.34" freecad:basepoint2="2.4 5.8" dimpoint="3.2 7.76">
    <path d="...">
</g>


### freecad:basepoint2

Defines the second point of a [Draft Dimension](Draft_Dimension.md) object (represented as a group in a SVG document). This attribute is used when importing the SVG fragment in FreeCAD, in order to recreate the dimension object. The group contains paths and other graphical items to correctly render the dimension object in other SVG applications.

Example: see _

### freecad:dimpoint

Defines the point of a [Draft Dimension](Draft_Dimension.md) object through which the dimension line passes. This attribute is used when importing the SVG fragment in FreeCAD, in order to recreate the dimension object. The group contains paths and other graphical items to correctly render the dimension object in other SVG applications.

Example: see _

### Example of code freecad:EditableText 

This example is taken from a cartridge to a sheet [A3\_Landscape](Misc_templates#A3_Landscape_US_Text_Complet_With_Convention_US.md)

#### 1 : Title without textedit 

<img alt="" src=images/Svg_Namespace_01.png  style="width:300px;">

 {.xml}
  <g
     id="g3587">
    <text
       sodipodi:linespacing="119.00001%"
       id="text3482"
       y="229.10912"
       x="220.8476"
       style="font-size:1.97555566px;font-style:normal;font-weight:normal;line-height:119.00000572%;letter-spacing:0.01975556px;word-spacing:0.00846667px;writing-mode:lr-tb;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"
       xml:space="preserve"><tspan
         y="229.10912"
         x="220.8476"
         id="tspan3484"
         sodipodi:role="line">AUTHOR NAME :</tspan></text>


#### 2 : Title with textedit 

<img alt="" src=images/Svg_Namespace_02.png  style="width:300px;">

 {.xml}
  <g
     style="fill:none;stroke:#000000;stroke-width:0.13;stroke-linecap:butt;stroke-linejoin:miter"
     id="g578-7"
     transform="translate(0,4)">
    <text
       xml:space="preserve"
       style="font-size:4px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:sans;-inkscape-font-specification:sans"
       x="220.9935"
       y="228.95425"
       id="text3331"
       sodipodi:linespacing="125%"
       freecad:editable="AuthorName"><tspan
         sodipodi:role="line"
         id="tspan3333"
         x="220.9935"
         y="228.95425">AUTHOR NAME</tspan></text>
    <text
    ...
    ...
    ...
    ... </text>
  
  </g>


#### Explanations

 {.xml}
  <g


Beginning of the framework

 {.xml}
     style="fill:none;stroke:#000000;stroke-width:0.13;stroke-linecap:butt;stroke-linejoin:miter"
     id="g578-7"
     transform="translate(0,4)">


Data on the framework

 {.xml}
    <text


Beginning of the text block

 {.xml}
       xml:space="preserve"
       style="font-size:4px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:sans;-inkscape-font-specification:sans"


All the information about the text that will be displayed

 {.xml}
       x="220.9935"
       y="228.95425"
       id="text3331"
       sodipodi:linespacing="125%"


Coordinates and identity where the text will appear

 {.xml}
       freecad:editable="AuthorName"><tspan


Here **AuthorName** is the var managed by **freecad:editable** who saves the string to change that will be displayed

 {.xml}
         sodipodi:role="line"
         id="tspan3333"
         x="220.9935"
         y="228.95425">AUTHOR NAME</tspan></text>


Coordinates and identity of the text that is displayed by default and **** means the end of the block text

 {.xml}
    <text
    ...
    ...
    ...
    ... </text>
  </g>


Other blocks texts and end **** the framework grouping text blocks

It is possible after having worked the Inkscape SVG file as the file no longer works, it is possible that information has gone missing.

Then check that the edit text is not modified

Example :

-   **editable** = \"AuthorName\"
-   replace by **freecad:editable** = \"AuthorName\"

## Other attributes availlables 

See [Drawing templates](Drawing_templates.md)


{{Drawing Tools navi

}}

_ _ _ _

---
[documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > Svg Namespace/ru
