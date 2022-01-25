---
- GuiCommand:/es
   Name:Draft_Text
   Name/es:Draft_Text
   MenuLocation:Croquis → Texto
   Workbenches:[Croquis](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
   Shortcut:**T** **E**
---

# Draft Text/es


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

La herramienta Texto inserta una parte de un texto en un punto dado en el documento actual. Toma el [tamaño de texto y color](Draft_Linestyle/es.md) previamente establecidos en la pestaña de tareas.


</div>

To create a text element with an arrow use the [Draft Label](Draft_Label.md) command instead.


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Text_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md) and [Draft Snap](Draft_Snap.md).


<div class="mw-translate-fuzzy">

## Utilización

1.  Presiona el botón **<img src="images/Draft_Text.png" width=16px> [Texto](Draft_Text/es.md)
**, o presiona las teclas **T** y **E**
2.  Designa un punto en la vista 3D, o escribe unas coordenadas
3.  Introduce el texto deseado, presionando **ENTER** entre cada línea
4.  Presiona **ENTER** dos veces para terminar la operación.


</div>

## Opciones

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Presionando **CTRL** se realizará un [ajuste](Draft_Snap/es.md) del punto a las ubicaciones de ajuste disponibles.
-   Para introducir coordenadas manualmente, simplemente introduce los números, presiona **ENTER** entre cada componente X, Y y Z.
-   Presionando **ESC** se cancela la operación.
-   Cuando editando el texto, se presiona **ENTER** o **DOWN ARROW** permite introducir o editar una nueva línea de texto.
-   Presionando **UP ARROW** permite editar una línea de texto previa.
-   Presionando **ENTER** **dos veces** (hasta dejar la última línea vacía) se añade el texto al documento y se cierra el editor.


</div>

## Notes

-   A Draft Text can be edited by double-clicking it in the [Tree view](Tree_view.md). <small>(v0.20)</small> 
-   Draft Texts created with [FreeCAD version 0.18](Release_notes_0.18.md) are not backward compatible.


<div class="mw-translate-fuzzy">

## Propiedades

-    **Position**: El punto base del bloque de texto

-    **Label Text**: El contenido del bloque de texto

-    **Display Mode**: Especifica si el texto está alineado con los ejes de la escena o si siempre mira hacia la cámara

-    **Font Size**: El tamaño de las letras

-    **Justification**: Especifica si el texto está alineado a la izquierda, derecha o centrado del punto base.

-    **Line Spacing**: Especifica el espacio entre líneas de texto

-    **Rotation**: Especifica una rotación a ser aplicada al texto

-    **Rotation Axis**: Especifica el eje a utilizar para la rotación

-    **Font Name**: La fuente a utilizar para dibujar el texto. Puede ser un nombre de una fuente, como \"Arial\", un estilo por defecto como \"sans\", \"serif\" o \"mono\", o una familia como \"Arial,Helvetica,sans\" o un nombre con un estilo como \"Arial:Bold\". Si la fuente indicada no se encuentra en el sistema, se utilizará en su lugar una genérica.


</div>

See also: [Property editor](Property_editor.md).

A Draft Text object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated.

### Data


{{TitleProperty|Base}}

-    **Placement|Placement**: specifies the position of the text in the [3D view](3D_view.md). See [Placement](Placement.md).

-    **Text|StringList**: specifies the contents of the text. Each item in the list represents a new text line.

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the text. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the text.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|3D text}} the text will be displayed in a plane defined by its **Placement**. If it is {{value|2D text}} the text will always face the camera. This is an inherited property.


{{TitleProperty|Graphics}}

-    **Line Color|Color**: not used.

-    **Line Width|Float**: not used.


{{TitleProperty|Text}}

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead.

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small.

-    **Justification|Enumeration**: specifies if the alignment of the text: {{value|Left}}, {{value|Center}} or {{value|Right}}.

-    **Line Spacing|Float**: specifies the factor applied to the default line height of the text.

-    **Text Color|Color**: specifies the color of the text.

## Scripting


<div class="mw-translate-fuzzy">

## Archivos de guión 

La herramienta Texto puede utilizarse en [macros](macros/es.md) y desde la consola de Python utilizando la siguiente función:


</div>

To create a Draft Text use the `make_text` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeText` method.


```python
text = make_text(string, placement=None, screen=False)
```


<div class="mw-translate-fuzzy">

-   Crea un objeto texto, en el punto indicado si se proporciona un vector, conteniendo la cadena de texto o las cadenas dadas en la lista, una cadena de texto por línea.
-   Se utilizan el color, altura de texto y fuente actuales de Boceto. Si screenmode es True, el texto siempre mira en la dirección de la vista, en otro casi permanece en el plano XY.
-   Devuelve el objeto recién creado.


</div>

The view properties of `text` can be changed by overwriting its attributes; for example, overwrite `ViewObject.FontSize` with the new size in millimeters.

Ejemplo:


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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Text/es
