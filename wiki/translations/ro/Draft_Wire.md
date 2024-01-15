---
 GuiCommand:
   Name: Draft Wire
   Name/ro: Draft Wire
   MenuLocation: Draft , Wire
   Workbenches: Draft_Workbench/ro, Arch_Workbench/ro
   Shortcut: **P** **L**
   SeeAlso: Draft Line/ro, Draft BSpline/ro
---

# Draft Wire/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Unealta filament \"Wire\" creează o polilinie (o succesiune de segmente legate între ele) în [planul de lucru](Draft_SelectPlane/ro.md) curent. Preia valorile pentru [lăţimea și culoarea liniei](Draft_Linestyle/ro.md) setate în prealabil pe tab-ul \"Sarcini\" (Tasks). Unealta \"Wire\" se comportă ca şi unealta [linie din CIornă](Draft_Line/ro.md), cu deosebirea că va continua şi după trasarea între primele două puncte.


</div>

The corners of a Draft Wire can be filleted (rounded) or chamfered by changing its **Fillet Radius** or **Chamfer Size** respectively. It is also possible to subdivide the edges of a Draft Wire by changing its **Subdivisions** property.

<img alt="" src=images/Draft_Polyline_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Polyline_example.jpg  style="width:400px;">


</div>

## Create

### Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Cum se foloseşte 

1.  Apăsați tasta **<img src="images/Draft_Wire.png" width=16px> [Draft Wire](Draft_Wire/ro.md)
** button, or press **W** then **I** sau apăsați **W** apoi tastele **I**
2.  Faceți clic pe un prim punct din vizualizarea 3D sau tastați un coordinate
3.  Faceți clic pe un punct suplimentar în vizualizarea 3D sau tastați un coordinate
4.  Apăsați **F** sau **C** sau faceți dublu clic pe ultimul punct sau faceți clic pe primul punct pentru a termina sau a închide filamentul/polilinia. Dacă filamentul este închis, acesta va fi, de asemenea, o fațetă, chiar dacă acesta apare ca o rețea wireframe.


</div>

### Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts (for version 0.22).


<div class="mw-translate-fuzzy">

## Opțiuni

-   Dacă sunt selectate mai multe linii [Draft Lines](Draft_Line/ro.md) atunci când apăsați butonul **Draft Wire**, acestea vor fi transformate într-un fir și comanda va ieși. <small>(v0.17/ro)</small> 
-   Apăsați butonul **F** sau butonul **<img src="images/_Draft_FinishLine.png" width=12px> '''Finish'''** pentru a finalize firul și a-l lăsa deschis
-   Apăsați butonul **C** or the **<img src="images/Draft_CloseLine.png" width=12px> '''Close'''** terminați firul, dar închizându-l prin adăugarea unui ultim segment între ultimul punct și primul.
-   Apăsați **X**, **Y** sau **Z** după un punct pentru a restrânge următorul punct de pe axa dată.
-   Pentru a introduce manual coordonatele, pur și simplu introduceți numerele, apoi apăsați **ENTER** între fiecare componentă X, Y și Z.
-   Apăsați tasta **R** sau faceți clic pe caseta de selectare pentru a bifa/debifa butonul **'''Relativ'''**. Dacă modul relativ este activ, coordonatele punctului următor sunt relative la ultimul. Dacă nu, ele sunt absolute, luate din punctul de origine (0,0,0).
-   Apăsați tasta **T** sau faceți clic pe caseta de selectare pentru a bifa/debifa butonul **'''Continue'''**. Dacă funcția continuă este activată, instrumentul Wire se va reporni după ce terminați sau închideți-l, permițându-vă să desenați altul fără să apăsați din nou butonul Wire.
-   Apăsați **CTRL** în timp ce desenați pentru a forța ancorarea [snapping](Draft_Snap/ro.md) punctului dvs. către cea mai apropiată locație, independent de distanța.
-   Apăsați pe **SHIFT** în timp ce desenați [constrain](Draft_Constrain/ro.md) următorul punct pe orizontală sau pe verticală în raport cu ultimul.
-   Apăsați butonul **W** sau apăsați butonul **<img src="images/_Draft_Wipe.png" width=12px> '''Șterge'''** pentru a elimina segmentele existente și a porni firul de la ultima punct.
-   Apăsați tasta **CTRL** + **Z** sau apăsați pe **<img src="images/_Draft_UndoLine.png" width=12px> '''Undo'''** pentru a anula ultimul punct.
-   Apăsați butonul **I** sau butonul **'''Fillet'''** pentru a avea firul umplut cu o fațetă dacă este închis.
-   Apăsați butonul **ESC** sau butonul **'''Cancel'''** pentru a întrerupe comanda curentă.
-   Firele închise, atunci când sunt în modul de afișare \"Flat Lines\", pot afișa un model de hașură, prin setarea proprietății \"Pattern\" de mai jos.


</div>

## Join

### Usage 

1.  The end points of the [Draft Lines](Draft_Line.md) and/or Draft Wires to be joined must be exactly coincident. If required first adjust points to ensure that this is the case.
2.  Select two or more [Draft Lines](Draft_Line.md) and/or Draft Wires.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Wire.svg" width=16px> [Draft Wire](Draft_Wire.md)** button.
    -   Select the **Drafting → <img src="images/Draft_Wire.svg" width=16px> Polyline** option from the menu.
    -   Use the keyboard shortcut: **P** then **L**.

## Notes

-   A Draft Wire can be edited with the [Draft Edit](Draft_Edit.md) command.
-   A Draft Wire can be converted to a [Draft BSpline](Draft_BSpline.md) with the [Draft WireToBSpline](Draft_WireToBSpline.md) command.
-   [Draft Lines](Draft_Line.md) and Draft Wires can also be joined with the [Draft Join](Draft_Join.md) command or the [Draft Upgrade](Draft_Upgrade.md) command.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Wire object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the wire. The value will be {{value|0.0}} if **Make Face** is `False` or the face cannot be created.

-    **Base|Link**
    

-    **Chamfer Size|Length**: specifies the length of the chamfers at the corners of the wire.

-    **Closed|Bool**: specifies if the wire is closed or not. If the wire is initially open this value is `False`, setting it to `True` will draw a line segment to close the wire. If the wire is initially closed this value is `True`, setting it to `False` will remove the last line segment and make the wire open.

-    **End|VectorDistance**: specifies the end point of the wire.

-    **Fillet Radius|Length**: specifies the radius of the fillets at the corners of the wire.

-    **Length|Length**: (read-only) specifies the total length of the wire.

-    **Make Face|Bool**: specifies if the wire makes a face or not. If it is `True` a face is created, otherwise only the edges are considered part of the object. This property only works if **Closed** is `True` and if the wire does not self-intersect.

-    **Points|VectorList**: specifies the points of the wire in its local coordinate system.

-    **Start|VectorDistance**: specifies the start point of the wire.

-    **Subdivisions|Integer**: specifies the number of subdivisions for each edge of the wire. If it is {{value|1}} each edge will be divided into {{value|2}} equal segments. Subdivisions are applied before chamfers and fillets.

-    **Tool|Link**
    

### View


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifies the size of the symbol displayed at the end of the wire.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the end of the wire, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **End Arrow|Bool**: specifies whether to show a symbol at the end of the wire, so it can be used as an annotation line.

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the closed wire. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).



## Script-Programare 


<div class="mw-translate-fuzzy">

*A se vedea [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/ro.md) pentru mai multe informații*


</div>


<div class="mw-translate-fuzzy">

Instrumentul Wire tool poate fi utilizat în [macros](macros/ro.md) și de la consola Python utilizând următoarele funcții:


</div>


```python
wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
wire = make_wire(Part.Wire, closed=False, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Creează un obiect Wire din lista dată de vectori sau din lista de puncte date pointslist.
    -   Dacă închis este Adevărat sau dacă primele și ultimul puncte sunt identice, firul este închis.
-   Each point in the list is defined by its FreeCAD.Vector
    -   Alternatively, the input can be a Part.Wire, from which points are extracted
    -   Dacă closed este True (și firul este închis, (primul și ultimul punct sunt identice)), firul va forma o fațetă.
-   Se va folosi versiunea curentă de linie și culoare[Draft Linestyle](Draft_Linestyle.md).
-   Returnează obiectul nou creat.


</div>

Exempluː


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

wire1 = Draft.make_wire([p1, p2, p3], closed=True)
wire2 = Draft.make_wire([p1, 2*p3, 1.3*p2], closed=True)
wire3 = Draft.make_wire([1.3*p3, p1, -1.7*p2], closed=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Wire/ro
