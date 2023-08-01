---
- GuiCommand:
   Name: Draft Dimension
   Name/es: Draft Dimension
   MenuLocation: Croquis - Cotas
   Workbenches: [Croquis](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
   Shortcut: **D** **I**
   SeeAlso: [FlipDimension](Draft_FlipDimension/es.md)
---

# Draft Dimension/es


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

La herramienta cotas crea una cota en el documento actual con dos puntos definiendo la distancia a medir, y un tercer punto especificando por donde pasa la línea de cota.


</div>

Linear dimensions based on edges and radial dimensions are parametric. This means that they will update if the measured edge is modified. Measured edges can belong to Draft objects but also to solid bodies. Angular dimensions are not parametric.

Draft Dimensions can be displayed on a [TechDraw Workbench](TechDraw_Workbench.md) page using the [TechDraw DraftView](TechDraw_DraftView.md) or [TechDraw ArchView](TechDraw_ArchView.md) commands. Alternatively the [TechDraw Workbench](TechDraw_Workbench.md) offer its own dimension commands. But these create dimensions that are only displayed on the drawing page and not in the [3D view](3D_view.md).

<img alt="" src=images/Screenshot_Draft_Dimension.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Screenshot_Draft_Dimension.jpg  style="width:400px;">


</div>

## Create

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

### Usage linear dimension 


<div class="mw-translate-fuzzy">

## Utilización

1.  Presiona el botón **<img src="images/Draft_Dimension.png" width=16px> [cota](Draft_Dimension/es.md)
**, o presiona las teclas **D** y **I**
2.  Designa un punto en la vista 3D, o escribe unas coordenadas
3.  Designa un segundo punto en la vista 3D, o escribe unas coordenadas
4.  Designa un tercer punto en la vista 3D, o escribe unas coordenadas


</div>

### Usage radial dimension 

1.  Optionally select a circular edge in the [3D view](3D_view.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  The **Dimension** task panel opens. See [Options](#Options.md) for more information.
4.  If you have not yet selected an edge do one of the following:
    -   Press **E** or the **<img src="images/view-select.svg" width=16px> Select edge** button and select a circular edge in the [3D view](3D_view.md).
    -   Hold down the **Alt** key, select a circular edge in the [3D view](3D_view.md) and release the **Alt** key.
5.  To position the dimension line do one of the following:
    -   For a diameter dimension:
        -   Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
    -   For a radial dimension:
        -   Hold down the **Shift** key and pick a point in the [3D view](3D_view.md).

### Usage angular dimension 

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
2.  The **Dimension** task panel opens. See [Options](#Options.md) for more information.
3.  Do one of the following:
    -   Press **E** or the **<img src="images/view-select.svg" width=16px> Select edge** button and select a first straight edge in the [3D view](3D_view.md). Repeat this to select a second straight edge.
    -   Hold down the **Alt** key, select two straight edges in the [3D view](3D_view.md) and release the **Alt** key.
4.  To position the dimension arc pick a point in the [3D view](3D_view.md).
5.  The displayed angle depends on the edges and the picked point.

### Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opciones

-   Presiona **X**, **Y** o **Z** después de un punto para restringir el punto siguiente sobre el eje indicado.
-   Para introducir coordenadas manualmente, simplemente introduce los números y presiona **ENTER** entre cada componente X, Y y Z.
-   Presiona **CTRL** mientras dibujas para forzar el [ajuste](Draft_Snap/es.md) de tu punto a la ubicación de ajuste más cercana, independientemente de la distancia.
-   Presionando **SHIFT** se realizará una [restricción](Draft_Constrain/es.md) de la cota horizontal o verticalmente, o, cuando se trabaja con un segmento circular, conmuta entre los modos de radio y diámetro.
-   Presiona **R** o selecciona la casilla para activar/desactivar el botón **'''Relativas'''**. Si el modo relativas está activada, las coordenadas del siguiente punto son relativas al anterior. Si no, son absolutas, tomadas desde el origen de coordenadas (0,0,0).
-   Presiona **T** o selecciona la casilla para activar/desactivar el botón **'''Continuar'''**. Si el modo continuar está activado, podrás dibujar cotas continuas, una tras otra, que comparten la misma línea base.
-   Presiona **ESC** o el botón **'''Cancelar'''** para abortar el comando actual.
-   Seleccionando una arista existente con **ALT**, en lugar de introducir puntos de medición, la cota se convertirá en **paramétrica** y recordará a que arista está vinculada. Si los puntos finales de la arista se mueven posteriormente, la cota los seguirá.
-   Si se selecciona un borde antes de iniciar el comando Dimensión, la dimensión creada también será *\'paramétrica\'*.
-   La dirección de la dimensión se puede cambiar luego, modificando su propiedad \"Dirección\"


</div>

## Convert

### Usage

1.  Select one or more [Std MeasureDistance](Std_MeasureDistance.md) objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  Each selected object is replaced by a non-parametric linear Draft Dimension.

## Notes

-   Linear and radial Draft Dimensions can be edited with the [Draft Edit](Draft_Edit.md) command.
-   Draft Dimensions created or saved with [FreeCAD version 0.21](Release_notes_0.21.md) are not backward compatible.




<div class="mw-translate-fuzzy">

## Propiedades

-    {{PropertyData/es|Start}}: El punto inicial de la distancia a medir

-    {{PropertyData/es|End}}: El punto final de la distancia a medir

-    {{PropertyData/es|Dimline}}: Un punto por el cual debe pasar la línea de cota

-    {{PropertyView/es|Display Mode}}: Especifica si el texto está alineado con las líneas de cota o si siempre mira hacia la cámara

-    {{PropertyView/es|Font Size}}: El tamaño de las letras

-    {{PropertyView/es|Ext Lines}}: El tamaño de las líneas de extensión (entre los puntos de medición y la línea de cota)

-    {{PropertyView/es|Text Position}}: Puede utilizarse para forzar que el texto se muestre en determinada posición

-    {{PropertyView/es|Override}}: Especifica un texto a mostrar en lugar de la medición. Utiliza la palabra \"\$dim\", dentro del texto, para mostrar la medición

-    {{PropertyView/es|Font Name}}: La fuente a utilizar para dibujar el texto. Puede ser un nombre de fuente, como \"Arial\", un estilo por defecto como \"sans\", \"serif\" o \"mono\", o una familia como \"Arial,Helvetica,sans\" o un nombre con un estilo como \"Arial:Bold\". Si la fuente indicada no se encuentra en el sistema, se utilizará una genérica en su lugar.

-    {{PropertyView/es|Arrow Type}}: el tipo de flecha para usar

-    {{PropertyView/es|Arrow Size}}: el tamaño de las flechas

-    {{PropertyView/es|Decimals}}: la cantidad de lugares decimales que se mostrarán en la dimensión

-    {{PropertyView/es|Flip Arrows}}: invierte la orientación de las flechas

-    {{PropertyView/es|Unit Override}}: Expresa la distancia en la unidad dada (déjelo en blanco para usar la unidad del sistema) {{Version/es|0.17}}


</div>

See also: [Property editor](Property_editor.md).

A Draft Dimension object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated:

### Data linear and radial dimension 


{{TitleProperty|Dimension}}

-    **Dimline|VectorDistance**: specifies the point through which the dimension line passes.

-    **Linked Geometry|LinkSubList**: specifies the object and its subelement(s) the dimension is linked to.

-    **Normal|Vector**: specifies the normal of the plane of the text.

-    **Support|Link|hidden**: specifies the measured object.


{{TitleProperty|Linear/radial dimension}}

-    **Direction|Vector**: specifies the direction of the measurement.

-    **Distance|Length**: (read-only) specifies the value of the measurement.

-    **End|VectorDistance**: specifies the end point of the measurement.

-    **Start|VectorDistance**: specifies the start point of the measurement.


{{TitleProperty|Radial dimension}}

-    **Diameter|Bool**: specifies if a radial dimension is displayed as a diameter dimension. If it changed the symbol used in **Override** must be updated manually (from {{Value|Ø}} to {{Value|R}} or vice versa). Not used for linear dimensions.

### Data angular dimension 


{{TitleProperty|Angular dimension}}

-    **Angle|Angle**: (read-only) specifies the value of the measurement.

-    **Center|VectorDistance**: specifies the center of the measurement.

-    **First Angle|Angle**: specifies the start angle of the measurement.

-    **Last Angle|Angle**: specifies the end angle of the measurement.


{{TitleProperty|Dimension}}

-    **Dimline|VectorDistance**: specifies the point through which the dimension arc passes.

-    **Linked Geometry|LinkSubList|hidden**: not used.

-    **Normal|Vector|hidden**: specifies the normal of the plane of the dimension.

-    **Support|Link|hidden**: not used.

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the dimension. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the dimension.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|World}} the text will be displayed on a plane defined by the **Normal** of the measurement. If it is {{value|Screen}} the text will always face the screen. This is an inherited property. The mentioned options are the renamed options (<small>(v0.21)</small> ).


{{TitleProperty|Graphics}}

-    **Arrow Size|Length**: specifies the size of the symbols displayed at the ends of the dimension line or arc.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the ends of the dimension line or arc, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **Dim Overshoot|Distance**: specifies the additional length added to the dimension line. Not used for angular dimensions.

-    **Ext Lines|Distance**: specifies the length of the extension lines that go from the dimension line to the measured points. Use {{Value|0}} for full extension lines. A negative value defines the gap between the ends of the extension lines and the measured points. A positive value defines the maximum length of the extension lines. Only used for linear dimensions.

-    **Ext Overshoot|Distance**: specifies the additional length of the extension lines beyond the dimension line. Not used for angular dimensions.

-    **Flip Arrows|Bool**: specifies whether to flip the orientation of the symbols at the ends of the dimension line or arc. Only works if the symbols are arrows.

-    **Line Color|Color**: specifies the color of the dimension line or arc, and the arrows.

-    **Line Width|Float**: specifies the width of the lines or arc belonging to the dimension.

-    **Show Line|Bool**: specifies whether to display the dimension line. Does not affect the display of extension lines and overshoots. Not used for angular dimensions.


{{TitleProperty|Text}}

-    **Flip Text|Bool**: specifies whether to flip the orientation of the text.

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead.

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small.

-    **Override|String**: specifies a custom text to display instead of the actual measurement. Use the string {{value|$dim}} inside the text to include the measurement.

-    **Text Color|Color**: specifies the color of the text. <small>(v0.21)</small> 

-    **Text Position|VectorDistance**: specifies the position of the text in absolute coordinates. {{Value|[0, 0, 0]}} will display the text in its default position near the dimension line or arc.

-    **Text Spacing|Length**: specifies the space between the text and the dimension line or arc.


{{TitleProperty|Units}}

-    **Decimals|Integer**: specifies the number of decimal places to display for the measurement.

-    **Show Unit|Bool**: specifies whether to display the unit next to the numerical value of the measurement. Not used for angular dimensions.

-    **Unit Override|String**: specifies the unit in which to express the measurement, for example, {{value|km}}, {{value|m}}, {{value|cm}}, {{value|mm}}, {{value|mi}}, {{value|ft}}, {{value|in}} or {{value|arch}} for arch units. Leave this blank to use the default unit. Not used for angular dimensions.

## Scripting


<div class="mw-translate-fuzzy">

## Archivos de guión 

La herramienta cotas se puede utilizar en [macros](macros/es.md) y desde la consola de Python utilizando la siguientes funciones:


</div>

To create a Draft Dimension use the `make_dimension` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeDimension` method.


```python
dimension = make_dimension(p1, p2, p3=None, p4=None)```

There are various ways to invoke this method, depending on the arguments passed to it:


```python
dimension = make_dimension(p1, p2, p3=None)
dimension = make_dimension(object, i1, i2, p4=None)
dimension = make_dimension(object, i1, mode, p4=None)
```


<div class="mw-translate-fuzzy">

-   Crea un objeto cota con la línea de cota pasando por p3.
-   El objeto Dimension toma el [ Draft Linewidth and Color](Draft_Linestyle.md) establecido en la barra de comandos.
-   Existen varias formas de crear una cota, dependiendo de los argumentos que les pases:

1.  (p1,p2,p3): crea una cota estándar desde p1 hasta p2.
2.  (object,i1,i2,p3): crea una cota vinculada a los objetos dados, midiendo la distancia entre sus vértices indexados i1 e i2.
3.  (object,i1,mode,p3): crea una cota vinculada al objeto actual, i1 es el índice de la arista (curvada) a medir, y mode es tanto el \"radio\" como el \"diámetro\". Devuelve el objeto recién creado.


</div>

To create an angular dimension use the following method:


```python
dimension = make_angular_dimension(center, angles, p3, normal=None)
dimension = make_angular_dimension(center, [angle1, angle2], p3, normal=None)
```


<div class="mw-translate-fuzzy">

crea una cota angular desde el centro indicado, con la lista dada de ángulos, pasando por p3. Devuelve el objeto recién creado.


</div>

The view properties of `dimension` can be changed by overwriting its attributes; for example, overwrite `ViewObject.FontSize` with the new size in millimeters.

Ejemplo:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(-2500, 0, 0)
dimension1 = Draft.make_dimension(p1, p2, p3)
dimension1.ViewObject.FontSize = 200

polygon = Draft.make_polygon(3, radius=1000)
doc.recompute()

p4 = App.Vector(-2000, 1500, 0)
dimension2 = Draft.make_dimension(polygon, 1, 2, p4)
dimension2.ViewObject.FontSize = 200

center = App.Vector(2000, 0, 0)
p5 = App.Vector(3000, 1000, 0)
angle1 = 45
angle2 = 10
dimension3 = Draft.make_angular_dimension(center, [angle1, angle2], p5)
dimension3.ViewObject.FontSize = 200

dimension4 = Draft.make_angular_dimension(center, [angle2, angle1], p5*1.2)
dimension4.ViewObject.FontSize = 200

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Dimension/es
