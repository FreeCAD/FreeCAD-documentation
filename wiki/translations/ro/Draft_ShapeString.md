---
 GuiCommand:
   Name: Draft ShapeString
   Name/ro: Draft ShapeString
   MenuLocation: Draft , Shape from text ...
   Workbenches: Draft_Workbench/ro, Arch_Workbench/ro
   Shortcut: **S** **S**
   SeeAlso: Draft Text/ro, Part Extrude/ro
---

# Draft ShapeString/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

Instrumentul ShapeString introduce o formă compusă care reprezintă un șir de caractere(text) într-un punct dat în documentul curent. Pot fi definite atribute ca: Înălțimea textului, tipul fontul, etc. The resulting shape can be used with the [Part Extrude](Part_Extrude/ro.md) tool to create 3D letters.


</div>


<div class="mw-translate-fuzzy">

Cele [Draft Text](Draft_Text/ro.md) instrumentul este o alternativă mai simplă, care nu produce o formă închisă.


</div>

![](images/Draft_ShapeString_Example400.png )


<div class="mw-translate-fuzzy">

![](images/Draft_ShapeString_Example400.png )


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

For Windows users: please read the [Font file selection on Windows](#Font_file_selection_on_Windows.md) paragraph first.

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_ShapeString.svg" width=16px> [Shape from text](Draft_ShapeString.md)** button.
    -   Select the **Drafting → <img src="images/Draft_ShapeString.svg" width=16px> Shape from text** option from the menu.
2.  The **ShapeString** task panel opens.
3.  Click a point in the [3D view](3D_view.md), or type coordinates.
4.  Optionally press the **Reset Point** button to reset the point to the origin.
5.  Enter a **String**.
6.  Specify the **Height**.
7.  To select a font do one of the following:
    -   Enter a file path in the **Font file** input box.
    -   Press the **...** button and select a file.
8.  Press the **OK** button to finish the command.
9.  Optionally change the **Justification** of the ShapeString. See [Properties](#Properties.md).



## Opţiuni


<div class="mw-translate-fuzzy">

-   Pentru a introduce coordonatele manual, pur și simplu introduceți numerele, apoi apăsați **ENTER** între fiecare componenetă pe X, Y și Z.
-   Apăsați tasta **ESC**pentru a abandona operațiunea.
-   Puteți defini un fișier de font implicit în Draft/Prefences.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Limitations

-   Acest instrumente nu este disponibil pentru versiunile anterioarea lui FreeCAD 0.14
-   Sunt suportatea următoareal tipuri de fișiere pentru fonturi: TrueType(\*.ttf), OpenType(\*.otf) și Type1(\*.pfb).
-   Înălțimile foarte mici ale textului pot cauza distorsionarea glifelor de caractere din cauza pierderii detaliilor la scalare.
-   Versiunea actuală este limitată la scrierile de la stânga la dreapta pe o linie de bază orizontală.
-   Pentru a crea texte de formă curbă puteți utiliza [Macro FCCircularText](Macro_FCCircularText/ro.md).


</div>

## Font file selection on Windows 

On Windows access to the default font folder is restricted. This affects the font file selection for ShapeStrings. There are three cases in FreeCAD where a font file for ShapeStrings can be specified: in the ShapeString task panel, when changing the **Font File** property of a ShapeString, and when specifying the default font file in the [Draft Preferences](Draft_Preferences#Texts_and_dimensions.md).

Pressing the **...** button and then selecting a file from the default Windows font folder is not possible when using the native file dialog. There are a number of workarounds:

-   Make sure **DontUseNativeFontDialog** is set to {{True}}, which is the default value for this preference. This will only call a different, non-native, file dialog when pressing the **...** button in the ShapeString task panel. With this file dialog the default Windows font folder can be accessed.
-   Change **DontUseNativeDialog** to {{True}}. This instructs FreeCAD to always use the non-native file dialog.
-   Specify the font file in the input box. You can of course type the full path or copy-paste the path from the Windows File Explorer. But there is also another way to enter the path. If you enter {{Value|C:\}} a dropdown list will appear. Select {{Value|Windows}} from that list and add {{Value|\F}}. Select {{Value|Fonts}} from the new dropdown list. Finally add {{Value|\}} and the first letter(s) of the font file, and then select it from the dropdown list.
-   Create a custom folder for your font files.

See the [Preferences](#Preferences.md) paragraph below for the location of the mentioned preferences.




<div class="mw-translate-fuzzy">

## Tutorials

-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial/ro.md)


</div>

-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md): extrude a ShapeString, position it in 3D space, and create an engraving in another body.
-   [How to use ShapeStrings in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623)

## Preferences

See also: [Preferences Editor](Preferences_Editor.md), [Draft Preferences](Draft_Preferences.md) and [Std DlgParameter](Std_DlgParameter.md).

-   The default font file can be changed in the preferences: **Edit → Preferences... → Draft → Texts and dimensions → Default ShapeString font file**.
-   For Windows users:
    -   Set **Tools → Edit parameters... → BaseApp → Preferences → Dialog → DontUseNativeFontDialog** to {{True}} to use the non-native file dialog when selecting a font file from the ShapeString task panel.
    -   Alternatively, set **Tools → Edit parameters... → BaseApp → Preferences → Dialog → DontUseNativeDialog** to {{True}} to always use the non-native file dialog.



## Proprietăți

See also: [Property editor](Property_editor.md).

A Draft ShapeString object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/ro|Position}}: Punctul de bază a formei compuse

-    {{PropertyData/ro|String}}: Conținutul șirului tip text

-    {{PropertyData/ro|Size}}: Înălțimea literelor exprimată în unități FC

-    {{PropertyData/ro|Tracking}}: Spațierea dintre caractere exprimată în unități FC

-    {{PropertyData/ro|Font File}}: Definirea fișierului fontului utilizat pentru a desena șirul de caractere


</div>

<img alt="" src=images/Draft_ShapeString_Justification.png  style="width:200px;"> 
*The height of the red rectangle (solid line) is equal to the cap height.<br>
The height of the green rectangle (dashed line) is equal to the shape height.<br>
The corners, the midpoints of the edges, and the center of the rectangles<br>
match the 9 justification options: Top-Left to Bottom-Right.*

## Scripting


<div class="mw-translate-fuzzy">

## Scripturi


</div>


<div class="mw-translate-fuzzy">

Instrumentul ShapeString poate fi utilizat în [macros](macros/ro.md) și de la consola Python folosind următoarele funcții:


</div>


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```


<div class="mw-translate-fuzzy">

-   Transformați un șir tip text într-o Compound Shape utilizând fontul specificat.
-   Creează o formă compusă ShapeString utilizând codul String specificat

  +

-   FontFile este obligatorie și trebuie să fie calea completă a unui fișier de fonturi acceptat

  +

-   Size este înălțimea textului rezultat în milimetri

  +

-   Tracking este distanța inter-caracter suplimentară în milimetri


</div>

The placement of the ShapeString can be changed by overwriting its `Placement` attribute, or by individually overwriting its `Placement.Base` and `Placement.Rotation` attributes.

Exempluː


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



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ShapeString/ro
