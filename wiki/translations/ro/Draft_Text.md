---
- GuiCommand:/ro
   Name:Draft Text
   Name/ro:Draft Text
   Workbenches:[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   MenuLocation:Draft → Text
   Shortcut:**T** **E**
   SeeAlso:[Draft Label](Draft_Label.md), [Draft ShapeString](Draft_ShapeString.md)
---

# Draft Text/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Unealta Text inserează o porţiune de text într-un punct dat din documentul curent. În prealabil, seta\'i în meniul **Editare**, opţiunea **Preferinţe**, [mărimea şi culoarea textului](Draft_Linestyle/ro.md) în tab-ul **Sarcini** (Draft Tray toolbar.).


</div>


<div class="mw-translate-fuzzy">

Pentru a crea forme de text solide, utilizați [Draft ShapeString](Draft_ShapeString/ro.md) cu [Part Extrude](Part_Extrude/ro.md).


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Text_example.jpg  style="width:400px;">


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md) and [Draft Snap](Draft_Snap.md).


<div class="mw-translate-fuzzy">

## Mod de utilizare 

1.  Apăsaţi butonul **<img src="images/Draft_Text.png" width=16px> [Draft Text](Draft_Text/ro.md)** ori apăsaţi tasta **T**, apoi tasta **E**.
2.  Daţi clic în fereastra de vizualizare 3D sau introduceţi coordonatele.
3.  Introduceţi textul dorit, apăsând tasta **ENTER** treceți la linie nouă.
4.  Apăsaţi DE DOUĂ ORI **ENTER** ca să terminaţi operaţia.


</div>

## Opţiuni

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

Apăsând pe **CTRL**, [snap](Draft_Snap/ro.md) punctul dvs. va fi ancorat la locațiile disponibile.

-   Pentru a introduce manual coordonatele, pur și simplu introduceți numerele, apoi apăsați **ENTER** între fiecare componentă X, Y și Z.
-   Apăsând **ESC** se va anula operația.
-   Când editați textul, apăsând **ENTER** sau **DOWN ARROW** vă permite să introduceți sau să editați un rând următor de text.
-   Apăsarea tastei **UP ARROW** vă permite să editați o linie anterioară de text.
-   Apăsând **ENTER** **de două ori**(lăsând astfel ultima linie goală) adaugă textul în document și închide editorul.


</div>

## Notes

-   A Draft Text can be edited by double-clicking it in the [Tree view](Tree_view.md). <small>(v0.20)</small> 
-   Draft Texts created with [FreeCAD version 0.18](Release_notes_0.18.md) are not backward compatible.


<div class="mw-translate-fuzzy">

## Proprietăți

-    {{PropertyData/ro|Position}}: Punctul de bază al blocului de text

-    {{PropertyData/ro|Label Text}}: conținutul blocului de text

-    {{PropertyView/ro|Mod afișare}}: Specifică dacă textul este aliniat la axele de scenă sau întotdeauna se confruntă cu camera

-    {{PropertyView/ro|Dimensiune font}}: Dimensiunea literelor

-    {{PropertyView/ro|Justification}}: Specifică dacă textul este aliniat la stânga, la dreapta sau la centrul punctului de bază.

-    {{PropertyView/ro|Line Spacing}}: Specifică spațiul dintre liniile de text

-    {{PropertyView/ro|Rotation}}: Specifică o rotație care trebuie aplicată textului

-    {{PropertyView/ro|Axa de rotație}}: Specifică axa de utilizat pentru rotație

-    {{PropertyView/ro|Font Name}}: fontul folosit pentru a desena textul. Poate fi un nume de font, cum ar fi \"Arial\", un stil implicit, cum ar fi \"sans\", \"serif\" sau \"mono\", sau o familie ca \"Arial, Helvetica, sans\" \"Arial: Bold\". În cazul în care fontul dat nu este găsit pe sistem, în locul acestuia se utilizează unul generic.


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

## Script-Programre 

Instrumentul Text poate fi folosit în [macro-uri](macros/ro.md) şi de la consola Python cu ajutorul funcţiei următoare:


</div>

To create a Draft Text use the `make_text` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeText` method.


```python
text = make_text(string, placement=None, screen=False)
```


<div class="mw-translate-fuzzy">

-   Creează un obiect Text , într-un punct dat, dacă este furnizat un FreeCAD.Vector , care conține șirul sau șirurile dintr-o listă, câte un șir pe rând.
-   stringlist este un șir sau o listă de șiruri de caractere; dacă este o listă, fiecare element este afișat într-o singură linie
-   Se utilizează actualul [Draft Linestyle](Draft_Linestyle/ro.md) specificat în preferințe.
-   Dacă screen este True, textul se află întotdeauna în direcția de vizualizare a camerei, altfel se află pe planul XY


</div>

The view properties of `text` can be changed by overwriting its attributes; for example, overwrite `ViewObject.FontSize` with the new size in millimeters.

Exempluː


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Text/ro
