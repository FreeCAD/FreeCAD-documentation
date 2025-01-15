# Manual:Creating and manipulating geometry/ro
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

În capitolele anterioare, am aflat despre diferitele ateliere de lucru ale FreeCAD și despre modul în care fiecare dintre ele implementează propriile instrumente și tipuri de geometrii. Același concept se aplică atunci când lucrați din codul Python.


</div>


<div class="mw-translate-fuzzy">

De asemenea, am văzut că marea majoritate a atelierelor de lucru FreeCAD depind de una foarte fundamentală: [Part Workbench](Part_Workbench.md). De fapt, multe alte ateliere de lucru, cum ar fi [Draft](Draft_Workbench.md) și [Arch](Arch_Workbench.md), fac exact ceea ce vom face în acest capitol: utilizează codul Python pentru a crea și manipula geometria pieselor.


</div>


<div class="mw-translate-fuzzy">

Deci, primul lucru pe care trebuie să-l facem pentru a lucra cu geometria pieselor, este de a face Python echivalentă cu comutarea la Workbench Part: import modulul Part:


</div>


```python
import Part 
```

import Part


<div class="mw-translate-fuzzy">

Luați un minut pentru a explora conținutul Atelierului Part (Workbench), tastând Part și navigând prin diferitele metode propuse aici. Atelierul Piese (Part) oferă mai multe funcții de comode, cum ar fi makeBox, makeCircle, etc \... care vor construi instantaneu un obiect pentru tine. Încercați aceasta, de exemplu:


</div>


```python
Part.makeBox(3,5,7) 
```


<div class="mw-translate-fuzzy">

Când apăsați Enter după introducerea liniei de mai sus, în vizualizarea 3D nu va apărea nimic, dar ceva similar va fi tipărit pe consolă Python:


</div>


```python
<Solid object at 0x5f43600> 
```


<div class="mw-translate-fuzzy">

Aici intră în scenă un concept important. Ceea ce am creat aici este o Formă de Piesă Acesta nu este un document obiect al FreeCAD (nu încă). În FreeCAD, obiectele și geometria lor sunt independente. Gândiți-vă la un document obiect al FreeCAD ca la un container, care va găzdui o formă. Obiectele parametrice vor avea de asemenea proprietăți precum Lungime și Lățime și vor **recalculate** forma lor din zbor, ori de câte ori se schimbă una dintre proprietăți. Ceea ce am făcut aici este de a calcula manual o formă.


</div>


<div class="mw-translate-fuzzy">

Acum putem crea cu ușurință un document obiect \"generic\" în documentul curent (asigurați-vă că aveți cel puțin un nou document deschis) și dați-i o formă de cutie așa cum am și făcut-o:


</div>

boxShape = Part.makeBox(3,5,7)

myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
myObj.Shape = boxShape
FreeCAD.ActiveDocument.recompute()


<div class="mw-translate-fuzzy">

Notați cum am tratat myObj.Shape, vedeți că acest lucru se face exact așa cum am făcut în capitolul anterior, când am schimbat alte proprietăți ale unui obiect, cum ar fi box.Height = 5. În realitate, **Shape** este de asemenea o proprietate, la fel ca **Height**. Doar aveți nevoie de o formă de Piesă, nu de un număr. În capitolul următor, vom examina mai detaliat modul în care sunt construite aceste obiecte parametrice.


</div>

We can now easily create a \"generic\" document object in the current document (make sure you have at least one new document open), and give it a box shape like the one we just made:


```python
boxShape = Part.makeBox(3,5,7)
myObj = FreeCAD.ActiveDocument.addObject("Part::Feature","MyNewBox")
myObj.Shape = boxShape
FreeCAD.ActiveDocument.recompute()
```

Here is a breakdown of the previous commands:

-   **boxShape = Part.makeBox(3,5,7)**: Creates a 3D box with dimensions 3x5x7 (length, width, and height) and stores it as a Part Shape in the variable boxShape. This shape exists only in memory and is not yet part of the FreeCAD document.

-   **myObj = FreeCAD.ActiveDocument.addObject(\"Part::Feature\", \"MyNewBox\")**: Adds a new Part::Feature object named \"MyNewBox\" to the active FreeCAD document and assigns it to the variable myObj. The new object will appear in the FreeCAD document tree.

-   **myObj.Shape = boxShape**: Links the boxShape geometry to the Shape property of myObj, integrating the geometry into the FreeCAD document.

-   **FreeCAD.ActiveDocument.recompute()**: Updates the document to reflect the changes, ensuring that the new object and its geometry appear in the graphical interface.

print(boxShape.Vertexes)

print(boxShape.Edges)
print(boxShape.Wires)
print(boxShape.Faces)
print(boxShape.Shells)
print(boxShape.Solids)


<div class="mw-translate-fuzzy">

De exemplu, hai să găsim zona de mai sus a fiecărei fațete a formei noastre de cutie de mai sus:


</div>

-   **Vertexes**: Points in 3D space that define the corners or endpoints of geometry.
-   **Edges**: Straight or curved lines connecting two vertexes.
-   **Wires**: Closed or open loops formed by one or more connected edges.
-   **Faces**: Surfaces enclosed by one or more wires.
-   **Shells**: Groups of connected faces, forming a continuous surface.
-   **Solids**: 3D volumes enclosed by one or more shells.

for f in boxShape.Faces:

  print(f.Area)


```python
print(boxShape.Vertexes)
print(boxShape.Edges)
print(boxShape.Wires)
print(boxShape.Faces)
print(boxShape.Shells)
print(boxShape.Solids)
```


<div class="mw-translate-fuzzy">

Pentru fiecare margine, există un punct de început și un punct final:


</div>


```python
for f in boxShape.Faces:
   print(f.Area)
```

for e in boxShape.Edges:

  print("New edge")
  print("Start point:")
  print(e.Vertexes[0].Point)
  print("End point:")
  print(e.Vertexes[1].Point)


```python
for e in boxShape.Edges:
   print("New edge")
   print("Start point:")
   print(e.Vertexes[0].Point)
   print("End point:")
   print(e.Vertexes[1].Point)
```


<div class="mw-translate-fuzzy">

După cum vedeți, dacă boxShape are un atribut \"Vertexes\", fiecare Edge al boxShape are și un atribut \"Vertexes\". Așa cum ne putem aștepta, boxShape va avea 8 vârfuri, în timp ce marginea va avea doar 2, care fac parte din lista celor 8.


</div>

Noi putem verifica întodeauna care este tipul formei :


```python
print(boxShape.ShapeType)
print(boxShape.Faces[0].ShapeType)
print(boxShape.Vertexes[2].ShapeType)
```

print(boxShape.ShapeType)

print(boxShape.Faces[0].ShapeType)
print(boxShape.Vertexes[2].ShapeType)

-   **print(boxShape.Faces\[0\].ShapeType)**: Accesses the first face in the **Faces** list of **boxShape** (index 0) and prints its shape type. For a box, each face is a flat surface, so the output will be \"Face\".

-   **print(boxShape.Vertexes\[2\].ShapeType)**: Accesses the third vertex in the **Vertexes** list of **boxShape** (index 2) and prints its shape type. Since this is a specific point in 3D space, the output will be \"Vertex\".


<div class="mw-translate-fuzzy">

Deci, pentru a relua tema Formele piesei (Part Shape): Totul începe cu Vertex. Cu unul sau două vârfuri, formați o margine (un cerc complet are doar un vertex). Cu una sau mai multe muchii, formați un fir(polilinie). Cu unul sau mai multe cabluri închise, formați o față (firele suplimentare devin \"găuri\" în fața). Cu una sau mai multe fire, formați un o cochilie(Shell). Atunci când un Shell este complet închis (etanș), puteți forma un Solid din acesta. Și, în final, puteți să alăturați oricâte forme(Shape) de orice tip, împreună, formând ceea ce se numește un compus(Compound).


</div>

Acum putem încerca să creăm forme complexe de la zero, prin construirea tuturor componentelor lor una câte una. De exemplu, să încercăm să creăm un volum ca acesta:

![](images/Exercise_python_03.jpg )

Vom începe prin a crea o formă plană în felul următor:

![](images/Wire.png )

În primul rând, să formăm cele patru puncte de bază:


```python
V1 = FreeCAD.Vector(0,10,0)
V2 = FreeCAD.Vector(30,10,0)
V3 = FreeCAD.Vector(30,-10,0)
V4 = FreeCAD.Vector(0,-10,0)
```

Apoi creăm două segmente liniare:

![](images/Line.png )


```python
L1 = Part.LineSegment(V1,V2)
L2 = Part.LineSegment(V4,V3)
```


<div class="mw-translate-fuzzy">

Notați că nu era nevoie să creăm Vertices? Am putea crea imediat Parts.Lines de la FreeCAD Vectors. Asta pentru că nu am creat Edges încă. O Part.Line (precum și Part.Circle, Part.Arc, Part.Ellipse sau Part.BSpline) nu creează o Edge, ci mai degrabă o geometrie de bază pe care va fi creată o Edge. Muchiile (Edges) sunt întotdeauna făcute dintr-o astfel de geometrie de bază, care se numește atributul Curve. Deci, dacă aveți o margine, faceți:


</div>


```python
print(Edge.Curve) 
```


<div class="mw-translate-fuzzy">

vă va arăta ce fel de margine este, adică dacă se bazează pe o linie, pe un arc etc. Dar să ne întoarcem la exercițiul nostru și să construim segmentele arcului. Pentru aceasta, vom avea nevoie de un al treilea punct, astfel încât să putem folosi convenabil Part.Arc, care are 3 puncte:


</div>

![](images/Circel.png )


```python
VC1 = FreeCAD.Vector(-10,0,0)
C1 = Part.Arc(V1,VC1,V4)
VC2 = FreeCAD.Vector(40,0,0)
C2 = Part.Arc(V2,VC2,V3)
```

Acum avem 2 linii (L1 and L2) și 2 arcuri (C1 and C2). trebuei să le transformăm în muchii(edges):


```python
E1 = Part.Edge(L1)
E2 = Part.Edge(L2)
E3 = Part.Edge(C1)
E4 = Part.Edge(C2)
```


<div class="mw-translate-fuzzy">

Alternativ, geometrii de bază au, de asemenea, o funcție toShape () care face exact același lucru:


</div>


```python
E1 = L1.toShape()
E2 = L2.toShape()
 ...
```


<div class="mw-translate-fuzzy">

Odată ce avem o serie de margini, putem acum să formăm o polilinie, oferindu-i o listă de muchii. Trebuie să avem grijă de ordinea lor.


</div>


```python
W = Part.Wire([E1,E4,E2,E3]) 
```


<div class="mw-translate-fuzzy">

Și putem verifica dacă polilinia dvs. a fost corect înțeleasă și că contrul este corect închis:


</div>


```python
print( W.isClosed() ) 
```


<div class="mw-translate-fuzzy">

Care va imprima \"Adevărat\" sau \"Fals\". Pentru a face o fațetă, avem nevoie de polilinii închise, deci este întotdeauna o idee bună să verificați faptul acesta înainte de a crea fațetă. Acum putem crea o fațetă, oferindu-i o singură polilinie (sau o listă de polilinii dacă vrem și găuri în fațetă):


</div>


```python
F = Part.Face(W) 
```

Then we extrude it:


```python
P = F.extrude(FreeCAD.Vector(0,0,10)) 
```


<div class="mw-translate-fuzzy">

Note that P is already a Solid:


</div>


```python
print(P.ShapeType) 
```


<div class="mw-translate-fuzzy">

Acest lucru se datorează faptului că atunci când extrudăm o singură față, întotdeauna obținem un Solid. Acest lucru nu ar fi cazul, de exemplu, dacă am fi extrudat o poliline(Wire) în schimb:


</div>


```python
S = W.extrude(FreeCAD.Vector(0,0,10))
print(S.ShapeType)
```

Care, desigur, ne va da o cochilie goală, cu fațetele de sus și de jos lipsă.

Acum că avem Forma noastră finală, suntem nerăbdători să o vedem pe ecran! Deci, să creăm un obiect generic și să-l atribuim noului nostru Solid :


```python
myObj2 = FreeCAD.ActiveDocument.addObject("Part::Feature","My_Strange_Solid")
myObj2.Shape = P
FreeCAD.ActiveDocument.recompute()
```

În mod alternativ, modulul Part oferă, de asemenea, o scurtătură care face operația de mai sus mai rapidă (dar nu puteți alege numele obiectului):


```python
Part.show(P) 
```

Toate cele de mai sus, și multe altele, sunt explicate în detaliu pe pagina [ Part Scripting](Topological_data_scripting.md), împreună cu exemple.

**De citit în plus**

-   [The Part Workbench](Part_Workbench.md)
-   [Part scripting](Topological_data_scripting.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Manual:Creating and manipulating geometry/ro
