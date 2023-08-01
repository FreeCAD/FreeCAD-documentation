---
- GuiCommand:/ro
   Name:Draft Label
   Name/ro:Draft Label
   MenuLocation:Draft → Label
   Workbenches:[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   Shortcut:**D** **L**
---

# Draft Label/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

Acest instrument introduce o etichetă, care este o fragment de text cu o linie de 2 segmente și o săgeată, în documentul activ. Dacă se selectează un obiect sau un sub-element (față, muchie sau vârf) la pornirea comenzii, eticheta poate fi făcută să afișeze automat un anumit atribut al elementului selectat.


</div>

If an object or a sub-element (face, edge or vertex) is selected when starting the command, the text can be made to display one or two attributes of the selected element, including position, length, area, volume and material. The text will then be linked to the attributes and will update if their values change.

To insert a text element without an arrow use the [Draft Text](Draft_Text.md) command instead.

<img alt="" src=images/Draft_Label_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Label_example.jpg  style="width:400px;">


</div>



## How to use 

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Opțional, selectați un obiect sau un subelement al unui obiect (Vertex, margine sau fațetă)
2.  Apăsați butonul {{KEY | <img src="images/_Draft_Label.svg_" width= 16px> [Etichetă de proiectare](Draft_Label/ro.md)}} sau apăsați {{KEY | D}} apoi tastele 
**L**
3.  Faceți clic pe un prim punct al vizualizării 3D sau introduceți un coordinate pentru a indica punctul țintă (poziția săgeții). Acest lucru poate fi oriunde, nu trebuie să fie exact pe elementul selectat
4.  Faceți clic pe un al doilea punct din vizualizarea 3D sau tastați un coordinate pentru a indica punctul intermediar care reprezintă începutul segmentului drept.
5.  Faceți clic pe un al treilea punct din vizualizarea 3D sau tastați un coordinate pentru a indica poziția textului.


</div>



## Opţiuni

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Apăsând pe {{KEY | CTRL}}, [ snap](Draft_Snap.md) punctul dvs. de locații disponibile snap.
-   Pentru a introduce manual coordonatele, pur și simplu introduceți numerele, apoi apăsați {{KEY | ENTER}} între fiecare componentă X, Y și Z.
-   Apăsând {{KEY | ESC}} se va anula operația.
-   Direcția segmentului drept (dreapta sau stânga) va justifica automat textul stânga sau dreapta.


</div>




<div class="mw-translate-fuzzy">

## Tipuri de etichete 


</div>

The following label types are available:


<div class="mw-translate-fuzzy">

-   **Custom**: Afișează conținutul proprietății text personalizat
-   **Name**: Afișează numele obiectului țintă
-   **Label**: Afișează eticheta obiectului țintă
-   **Poziția**: Afișează coordonatele obiectului țintă (punctul de bază al amplasamentului) sau coordonatele vârfului țintă, dacă este cazul, sau coordonatele centrului subelementului țintă (centrul de masă)
-   **Length**: Afișează lungimea subelementului țintă, dacă este posibil
-   **Area**: Arată suprafața subelementului țintă, dacă este posibil
-   **Volume**: Afișează volumul obiectului țintă, dacă este posibil
-   **Tag**: Afișează valoarea etichetei obiectului țintă, dacă obiectul țintă are o astfel de proprietate (ceea ce este cazul tuturor obiectelor Arch)
-   **Material**: Afișează eticheta materialului obiectului țintă, dacă obiectul țintă are o astfel de proprietate


</div>

## Notes

-   The direction of the second segment of the leader determines the alignment of the text. If the segment is horizontal and pointing to the right the text is aligned to the left and vice versa. If the second segment goes vertically up, the text is aligned to the left. If it goes vertically down, the text is aligned to the right.
-   Draft Labels created or saved with [FreeCAD version 0.21](Release_notes_0.21.md) are not backward compatible.



## Proprietăți

See also: [Property editor](Property_editor.md).

A Draft Label object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated:

### Data


{{TitleProperty|Label}}


<div class="mw-translate-fuzzy">

-    {{PropertyData | Tip de etichetă}}: tipul de informații afișate de această etichetă (vedeți mai jos)

-    {{PropertyData | Text personalizat}}: Textul care se afișează când tipul de etichetă este setat la personalizat

-    {{PropertyData | Placement}}: Indică rotația și poziția textului

-    {{PropertyData | Straight Distance}}: Lungimea segmentului drept

-    {{PropertyData | Direcție dreaptă}}: Direcția segmentului drept Orizontală sau verticală

-    {{PropertyData | Target Point}}: Punctul indicat de această etichetă

-    {{PropertyView | Text Size}}: Dimensiunea textului

-    {{PropertyView | Text Font}}: fontul folosit pentru text

-    {{PropertyView | Text Alignment}}: Alinierea verticală a textului: Sus, mijlocul sau partea de jos

-    {{PropertyView | Text Color}}: Culoarea textului

-    {{PropertyView | Lățime linie}}: Lățimea liniei

-    {{PropertyView | Line Color}}: culoarea liniei

-    {{PropertyView | Arrow Type}}: Tipul săgeții: Dot, cerc, săgeată sau bifați.

-    {{PropertyView | Dimensiunea săgeții}}: mărimea săgeții

-    {{PropertyView | Frame}}: Desenează un cadru în jurul textului


</div>


{{TitleProperty|Leader}}

-    **Points|VectorList**: specifies the points of the leader.

-    **Straight Direction|Enumeration**: specifies the direction of the first leader segment: {{Value|Custom}}, {{Value|Horizontal}} or {{Value|Vertical}}.

-    **Straight Distance|Distance**: specifies the length of the first leader segment. Only used if **Straight Direction** is {{Value|Horizontal}} or {{Value|Vertical}}. If the distance is positive, the leader starts from the right side of the text and the text aligns to the right. Otherwise the leader starts from the left side of the text and the text aligns to the left.


{{TitleProperty|Target}}

-    **Target|LinkSub**: specifies the object and optional subelement the label is linked to.

-    **Target Point|Vector**: specifies the position of the tip of the leader, which is where the arrow is attached.

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the label. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the label.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|World}} the text will be displayed on a plane defined by the **Placement** of the label. If it is {{value|Screen}} the text will always face the screen. This is an inherited property. The mentioned options are the renamed options (<small>(v0.21)</small> ).


{{TitleProperty|Graphics}}

-    **Arrow Size|Length**: specifies the size of the symbol displayed at the tip of the leader.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the tip of the leader, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **Frame|Enumeration**: specifies what type of frame is drawn around the text. The current options are {{Value|None}} or {{Value|Rectangle}}.

-    **Line|Bool**: specifies whether to display the leader line. If it is `False` only the arrow and the text are displayed.

-    **Line Color|Color**: specifies the color of the leader and the arrow. This is also used for the frame (<small>(v0.20)</small> ).

-    **Line Width|Float**: specifies the width of the leader. This is also used for the frame (<small>(v0.20)</small> ).


{{TitleProperty|Text}}

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead. <small>(v0.21)</small> 

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small. <small>(v0.21)</small> 

-    **Justification|Enumeration**: specifies the horizontal alignment of the text: {{value|Left}}, {{value|Center}} or {{value|Right}}. Only used if **Straight Direction** is {{Value|Custom}}. Otherwise the horizontal alignment is based on the sign (positive or negative) of **Straight Distance**.

-    **Line Spacing|Float**: specifies the factor applied to the default line height of the text.

-    **Max Chars|Integer**: specifies the maximum number of characters on each line of the text.

-    **Text Alignment|Enumeration**: specifies the vertical alignment of the text: {{value|Top}}, {{value|Middle}} or {{value|Bottom}}.

-    **Text Color|Color**: specifies the color of the text.

## Scripting


<div class="mw-translate-fuzzy">

## Script-Programare 

Instrumentul Text poate fi utilizat în [macros](macros.md) și din consola python utilizând următoarea funcție:


</div>

To create a Draft Label use the `make_label` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeLabel` method.


```python
label = make_label(target_point=App.Vector(0, 0, 0),
                   placement=App.Vector(30, 30, 0),
                   target_object=None, subelements=None,
                   label_type="Custom", custom_text="Label",
                   direction="Horizontal", distance=-10,
                   points=None)
```

Exempluː


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(4000, 1000)
doc.recompute()

p1 = App.Vector(-200, 1000, 0)
place1 = App.Placement(App.Vector(-1000, 1300, 0), App.Rotation())

label1 = Draft.make_label(p1, place1, target_object=rectangle, distance=500, label_type="Label")
label1.ViewObject.TextSize = 200

p2 = App.Vector(-200, 0, 0)
place2 = App.Placement(App.Vector(-1000, -300, 0), App.Rotation())

label2 = Draft.make_label(p2, place2, target_object=rectangle, distance=500, label_type="Custom",
                          custom_text="Beware of the sharp edges")
label2.ViewObject.TextSize = 200

p3 = App.Vector(1000, 1200, 0)
place3 = App.Placement(App.Vector(2000, 1800, 0), App.Rotation())

label3 = Draft.make_label(p3, place3, target_object=rectangle, distance=-500, label_type="Area")
label3.ViewObject.TextSize = 200

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Label/ro
