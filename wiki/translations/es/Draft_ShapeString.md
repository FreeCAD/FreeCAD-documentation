---
- GuiCommand:/es
   Name:Draft ShapeString
   Name/es:Bosquejar forma de cadena
   MenuLocation:Borrador -> Bosquejar forma de cadena
   Workbenches:[Borrador](Draft_Workbench/es.md), [Arquitectura](Arch_Workbench/es.md)
   Shortcut:**S** **S**
   SeeAlso:[Draft Text](Draft_Text/es.md), [Part Extrude](Part_Extrude/es.md)
---


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta forma de cadena, inserta una forma compuesta representando una cadena de texto a un punto dado en el actual documento. Altura, trayectoria y fuente pueden ser definidas.


</div>

The Draft ShapeString command is not intended for standard text annotations. The [Draft Text](Draft_Text.md) command or the [Draft Label](Draft_Label.md) command should be used for that purpose.

![](images/Draft_ShapeString_Example400.png )


<div class="mw-translate-fuzzy">

![](images/Draft_ShapeString_Example400.png )


</div>


<div class="mw-translate-fuzzy">

## Como utilizar 


</div>

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_ShapeString.svg" width=16px> [Draft ShapeString](Draft_ShapeString.md)** button.
    -   Select the **Drafting → <img src="images/Draft_ShapeString.svg" width=16px> Shape from text** option from the menu.
    -   Use the keyboard shortcut: **S** then **S**.
2.  The **ShapeString** task panel opens.
3.  Click a point in the [3D view](3D_view.md), or type coordinates.
4.  Optionally press the **Reset Point** button to reset the point to the origin.
5.  Enter a **String**.
6.  Specify the **Height**.
7.  To select a font do one of the following:
    -   Enter a file path in the **Font file** input box.
    -   Press the **...** button and select a file.
8.  Press the **OK** button to finish the command.

## Opciones


<div class="mw-translate-fuzzy">

-   Para ingresar coordenadas manualmente, simplemente ingresa los numeros, luego **ENTER** entre cada componente X,Y y Z.
-   Presionando **ESC** cancelará la operación.
-   Puedes ajustar un archivo fuente predeterminado en Draft/Preferencias.


</div>

## Notes

-   Supported fonts include TrueType ({{FileName|.ttf}}), OpenType ({{FileName|.otf}}) and Type 1 ({{FileName|.pfb}}).
-   The command is restricted to LTR (left-to-right) text. Therefore at the moment RTL (right-to-left + top-to-bottom) text isn\'t supported.
-   Very small text heights may result in deformed character shapes due to loss of detail in scaling.
-   Many fonts will generate problematic geometry. This is because font contours are allowed to overlap, have small gaps, and have varying directions within a glyph. These conditions are considered errors in wires used to define faces.
-   Draft ShapeStrings can also be created with the [Macro Fonts Win10 PYMP](Macro_Fonts_Win10_PYMP.md).
-   To create Draft ShapeStrings arranged in a circular fashion use the [Macro FCCircularText](Macro_FCCircularText.md).

## Tutorials

-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md): extrude a ShapeString, position it in 3D space, and create an engraving in another body.
-   [How to use ShapeStrings in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623)

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The default font file can be changed in the preferences: **Edit → Preferences... → Draft → Texts and dimensions → Default ShapeString font file**. See [Draft Preferences](Draft_Preferences.md).

## Propiedades

See also: [Property editor](Property_editor.md).

A Draft ShapeString object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **Position**: El punto base del compuesto

-    **String**: Los contenidos del texto

-    **Size**: La altura de las letras en unidades de FreeCAD

-    **Tracking**: El espacio adicional entre los caracteres en unidades de FreeCAD

-    **Font File**: El archivo fuente utilizado para dibujar el texto


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the faces of the text. This property only works if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

Esta herramienta se puede utilizar en [macros](macros/es.md) y desde la consola de Python mediante las siguientes funciones:


</div>


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```


<div class="mw-translate-fuzzy">

-   Convierte un texto en un compuesto usando la fuente especificada.


</div>

The placement of the ShapeString can be changed by overwriting its `Placement` attribute, or by individually overwriting its `Placement.Base` and `Placement.Rotation` attributes.

Ejemplo:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

font1 = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
font2 = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
font3 = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

S1 = Draft.make_shapestring("This is a sample text", font1, 200)

S2 = Draft.make_shapestring("Inclined text", font2, 200, 10)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(-1000, 500, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 45))
S2.Placement = place2

S3 = Draft.make_shapestring("Upside-down text", font3, 200, 10)
S3.Placement.Base = App.Vector(0, -1000, 0)
S3.Placement.Rotation = App.Rotation(zaxis, 180)

doc.recompute()
```





 
