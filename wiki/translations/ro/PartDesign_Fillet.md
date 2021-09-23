# PartDesign Fillet/ro
---
- GuiCommand:   Name:PartDesign Fillet   Workbenches:[MenuLocation:PartDesign → Fillet   SeeAlso:[[Part Fillet|Part Fillet](PartDesign_Workbench___PartDesign]],_Complete.md)---


</div>

## Descriere


<div class="mw-translate-fuzzy">

Acest instrument creează racordări/rotunjiri pe muchiile selectate al unui obiect. O nouă separată intrare Fillet (urmată de un număr secvențial dacă sunt deja racordări/rotunjiri existent în document) este creată în arborescența Project.


</div>

## Cum se folosește 


<div class="mw-translate-fuzzy">

-   Select a single or multiple edges or a face on an object, then start the tool either by clicking its icon or going into the menu. In case you selected a face all its edges are respected for filleting.
-   In Fillet parameters in the TaskPanel, set the fillet radius either by entering the value, or by clicking on the up/down arrows. The applied fillet is shown in real time.
-   If you want to add more edges or faces click first the **Add ref** button and then select the edge or the face.
-   If you want to remove edges or faces click the **Remove ref** button. All edges and faces being previously selected are highlighted in purple. Select the edge or the face to be removed.
-   Click pe OK pentru validare.
-   Pentru un lanț de muchii tangențial una cu celălaltă, poate fi selectată o singură margine; rotunjirea se va propaga de-a lungul lanțului.
-   Pentru a edita rotunjirea după validarea funcției, fie faceți dublu clic pe eticheta Fillet din arborescența Project, fie faceți clic dreapta pe el și selectați **Edit Fillet**.


</div>


<div class="mw-translate-fuzzy">

#### PartDesign Fillet VS. Part Fillet 

**PartDesign Fillet nu trebuie confundat cu contrapartida sa [Part workbench counterpart](Part_Fillet.md)**. Deși împărt aceeași pictogramă, ele nu sunt aceleași și nu sunt utilizate în același mod. Iată cum diferă acestea unul de celălalt:

-   The PartDesign Fillet is *parametric*. After a fillet has been applied, its radius can be edited; this is not possible with the Part Fillet.
-   Edges must be selected on an object before activating the PartDesign Fillet. WIth the Part Fillet, the tool can be started, then a solid is selected, then edges.
-   The PartDesign Fillet creates a separate Fillet entry (followed by a sequential number if there are already existing fillets) in the Project tree. The Part Fillet becomes the parent of the object it was applied to.
-   The PartDesign Fillet offers a live preview of the fillet applied to the object before validating the function.
-   The Part Fillet supports variable radii (with a start radius and an end radius). The PartDesign fillet doesn\'t.





</div>

<img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> [PartDesign Fillet](PartDesign_Fillet.md) is not to be confused with **<img alt="" src=images/Part_Fillet.svg  style="width:24px;"> [Part Fillet](Part_Fillet.md)** of the [Part Workbench](Part_Workbench.md). Although they share the same name, they are not the same, and are not used the same way.

Here is how they differ from each other:

-   The PartDesign Fillet is *Parametric*. After a fillet has been applied, its radius can be edited; this is not possible with the Part Fillet.
-   The PartDesign Fillet creates a separate Fillet entry (followed by a sequential number if there are already existing fillets) in the Project tree. The Part Fillet becomes the parent of the object it was applied to.
-   The PartDesign Fillet offers a live preview of the fillet applied to the object before validating the function.
-   The Part Fillet supports variable radii (with a start radius and an end radius). The PartDesign fillet doesn\'t.

## Probleme cunoscute 


<div class="mw-translate-fuzzy">

-   Rotunjirile care nu reușesc cu raze implicite de 1 mm pot provoca căderea programului, salvați-vă piesa înainte de a utiliza rontjirea pentru a fi siguri
    -   This is due to issue in OCC kernel
-   Edge numbers are not stable so you should finish all design work before filleting your part otherwise filleted edges will change and likely become invalid
    -   This is due to topological naming issues


</div>


<div class="mw-translate-fuzzy">

If run from the terminal, FreeCAD may output a log like this one after the crash: {{code|code=
#1  0x7fff63d660ba in BRep_Tool::Curve(TopoDS_Edge const&, TopLoc_Location&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x2a
#2  0x7fff63d69546 in BRep_Tool::Curve(TopoDS_Edge const&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x46
#3  0x7fff71f4fef5 in ChFi3d_Builder::PerformIntersectionAtEnd(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x3b05
#4  0x7fff71f58307 in ChFi3d_Builder::PerformOneCorner(int, bool) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x1097
#5  0x7fff71ef6218 in ChFi3d_Builder::PerformFilletOnVertex(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x4e8
#6  0x7fff71ef71d1 in ChFi3d_Builder::Compute() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0xe31
#7  0x7fff720ad7c3 in BRepFilletAPI_MakeChamfer::Build() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x33
#8  0x7fff723be48e in PartDesign::Chamfer::execute() from /usr/lib/freecad-daily/lib/_PartDesign.so+0x60e
...
}}


</div>


{{code|code=
#1  0x7fff63d660ba in BRep_Tool::Curve(TopoDS_Edge const&, TopLoc_Location&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x2a
#2  0x7fff63d69546 in BRep_Tool::Curve(TopoDS_Edge const&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x46
#3  0x7fff71f4fef5 in ChFi3d_Builder::PerformIntersectionAtEnd(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x3b05
#4  0x7fff71f58307 in ChFi3d_Builder::PerformOneCorner(int, bool) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x1097
#5  0x7fff71ef6218 in ChFi3d_Builder::PerformFilletOnVertex(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x4e8
#6  0x7fff71ef71d1 in ChFi3d_Builder::Compute() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0xe31
#7  0x7fff720ad7c3 in BRepFilletAPI_MakeChamfer::Build() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x33
#8  0x7fff723be48e in PartDesign::Chamfer::execute() from /usr/lib/freecad-daily/lib/_PartDesign.so+0x60e
...
}}


<div class="mw-translate-fuzzy">

This output references functions located in `libTKBRep.so`, `libTKFillet.so`, etc., which are OCC libraries. If these type of crashes occur, the problem may need to be reported and solved in OCC rather than in FreeCAD.


</div>


<div class="mw-translate-fuzzy">

See the forum threads for more information:

-   [Bug Chamfer bigger than 2mm crashes freecad](https://forum.freecadweb.org/viewtopic.php?p=263818#p263818)
-   [Segfault when using part desgin fillet](https://forum.freecadweb.org/viewtopic.php?p=264827#p264827)


</div>

Utilizatorul este, de asemenea, responsabil pentru integritatea propriului model. În funcție de model, ar putea fi imposibil să efectuați o racordare sau o șanfrenare dacă corpul nu este suficient de mare pentru a susține acea operație. De exemplu, nu ar fi posibil să creați o racordare de 10 mm dacă o margine este separată la numai 5 mm de suprafața următoare. În acest caz, raza maximă pentru un filet ar fi de 5 mm; încercarea de a utiliza o valoare mai mare poate avea ca rezultat o formă care nu calculează sau chiar un crash/accident. Dacă utilizarea limitei exacte de 5 mm nu funcționează, este posibil să se utilizeze o apropiere foarte apropiată, ca de exemplu 4,9999 mm, pentru a produce același rezultat vizibil.

### Topological naming 


<div class="mw-translate-fuzzy">

### Topological naming 

Numerele de margine nu sunt complet stabile, prin urmare este recomandat să finalizați lucrarea principală de proiectare a corpului dvs solid înainte de a aplica funcții cum ar fi racordări și șanfren, în caz contrar arginile ar putea schimba numele și margini racordate ar deveni probabil nevalabile.


</div>

Read more in [topological naming problem](topological_naming_problem.md).

## Programare-Script 


<div class="mw-translate-fuzzy">

Instrumentul **[16px|text-top=Fillet|link=PartDesign_Fillet](File:PartDesign_Fillet.png.md) [Fillet](_PartDesign_Fillet.md)** poate fi utilizat într-o macrocomandă, și, din consola Pythonutilizând următaorea funcție :


</div>


```python
Box = Box.makeFillet(3,[Box.Edges[0]]) # 1 Fillet
Box = Box.makeFillet(3,[Box.Edges[1],Box.Edges[2],Box.Edges[3],Box.Edges[4]]) # for several Fillets
```

-   3 = radius
-   Box.Edges\[2\] = Edge with its number


<div class="mw-translate-fuzzy">

Exemple :


</div>


```python
import PartDesign
from FreeCAD import Base

Box = Part.makeBox(10,10,10)
Box = Box.makeFillet(3,[Box.Edges[0]]) # pour 1 Fillet
Box = Box.makeFillet(3,[Box.Edges[1],Box.Edges[2],Box.Edges[3],Box.Edges[4]]) # for several Fillets
Part.show(Box)
```





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Fillet/ro
