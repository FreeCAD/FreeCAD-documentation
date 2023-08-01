---
- GuiCommand:
   Name:Arch Rebar
   Name/ro:Arch Rebar
   Workbenches:[Arch](Arch_Workbench/ro.md)
   MenuLocation:Arch → Rebar
   Shortcut:R B
   SeeAlso:[Arch Structure](Arch_Structure/ro.md)
---

# Arch Rebar/ro


</div>


<div class="mw-translate-fuzzy">

---
- GuiCommand:
   Name:Arch Rebar
   Name/ro:Arch Rebar
   Workbenches:[Arch](Arch_Workbench/ro.md)
   MenuLocation:Arch → Rebar
   Shortcut:R B
   SeeAlso:[Arch Structure](Arch_Structure/ro.md)
---

# Arch Rebar/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

Instrumentul Rebar vă permite să plasați barele de armătură [1](http://en.wikipedia.org/wiki/Rebar) în interiorul obiectelor [Arch Structure](Arch_Structure.md). Obiectele bare de armătură sunt bazate pe profilele 2D, cum ar fi [sketches](Sketcher_Workbench.md) sau [draft objects](Draft_Workbench.md), care trebuie să fie desenate pe o față a unui obiect de structură. Puteți apoi să reglați configurația armăturilor, cum ar fi numărul și diametrul barelor sau distanța de decalaj dintre cele două capete ale elementului structural.


</div>

The [Arch Rebar](Arch_Rebar.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

Rebar objects are based on 2D profiles such as [Draft objects](Draft_Workbench.md) and [Sketches](Sketcher_Workbench.md), that must be drawn on a face of the structural object. After creation you can adjust the properties of the rebar, including the number and diameter of the bars, and the offset distance between them and the faces of the structural element.

<img alt="" src=images/Arch_Rebar_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

Imaginea de mai sus prezintă un obiect structural, în care sunt desenate două schițe, care definesc două diagrame de bare. Aceste două schițe sunt apoi transformate în obiecte de armătură.


</div>



## Extensii disponibile 


<div class="mw-translate-fuzzy">

Instrumentul Rebar a fost mult îmbunătățit în timpul ediției din 2017 a [Google Summer of Code](Google_Summer_of_Code.md) . Rezultatul acestei lucrări este o serie de noi presetări și vrăjitori/asistenți pentru cele mai comune tipuri de bare. Acestea sunt ambalate sub un modul independent numit **Reinforcement**, pe care îl puteți instala prin meniul Tools -\> Addons Manager. Odată ce aplicația Addon Reinforcement este instalată, la următoarea rulare, FreeCAD o va detecta și va adăuga o serie de instrumente noi sub butonul Rebar din bara de instrumente Arch și meniul:


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Creați un elemente de [structure](Arch_Structure.md)
2.  Switch to the [Sketcher Workbench](Sketcher_Workbench.md)
3.  Select one face of the structural element
4.  Press the **<img src="images/Sketcher_NewSketch.png" width=16px> [New Sketch](Sketcher_NewSketch.md)** button to start a new sketch on the selected face
5.  Draw the diagram of your bar
6.  Press the **<img src="images/Sketcher_LeaveSketch.png" width=16px> [Leave Sketch](Sketcher_LeaveSketch.md)** button to finish
7.  Switch back to the [Arch Workbench](Arch_Workbench.md)
8.  Select the sketch you just drew
9.  Press the **<img src="images/Arch_Rebar.png" width=16px> [[Arch Rebar]]** button, or press **R** then **B** keys
10. Reglați proprietățile dorite (armăturae dvs. ar putea să nu apară imediat dacă unele dintre proprietăți creează o situație imposibilă, cum ar fi diametrul barei fiind 0 sau distanțele dispuse mai mari decât lungimea elementului structural)


</div>

Although normally a rebar is used inside an Arch Structure, since FreeCAD 0.19 the rebar can be created outside of any host object. To host a rebar inside an object, you just need to set its **Host**.



## Opţiuni

-   Barele partajează proprietățile și comportamentele comune ale tuturor [Arch Components](Arch_Component.md)
-   The rounding value is expressed in times the diameter. If your bar has a diameter of 5mm, a rounding value of 3 will create rounding at angles with a radius of 15mm.
-   Default values for new rebars can be set in the Arch preferences settings.
-   If a direction vector is not specified, the direction and distance along which the bars will spread is calculated automatically from the host structural object, by taking the normal direction of the base sketch, and taking its intersection with the structural object. If you specify a direction vector, the length of that vector will also be taken into account.
-   Valoarea distanței este calculată din cantitatea curentă de bare și reprezintă distanța dintre axele fiecărei bare. Prin urmare, trebuie să scădeți diametrul barei pentru a obține dimensiunea spațiului liber dintre bare.



## Proprietăți

-    **Amount**: Cantitatea de bare.

-    **Diameter**: The diameter of the bars.

-    **Direction**: The direction (and length) along which the bars must spread. If the value is (0,0,0), the direction is calculated automatically from the host structural object.

-    **Offset Start**: The offset distance between the border of the structural object and the first bar.

-    **Offset End**: The offset distance between the border of the structural object and the last bar.

-    **Rounding**: A rounding value to be applied to the corners of the bars, expressed in times the diameter.

-    **Spacing**: Distanța dintre axele fiecărei bare.




<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Instrumentul Rebar poate fi folosit în [macros](macros.md) și din consola python utilizând următoarea funcție:


</div>


```python
Rebar = makeRebar(baseobj=None, sketch=None, diameter=None, amount=1, offset=None, name="Rebar")
```


<div class="mw-translate-fuzzy">

-   Adăugă un obiect Bar armare la obiectul structural dat, utilizând schița dată ca profil.
-   Dacă nu este indicat niciun diametru, valoare sau valoare de compensare, se aplică valorile implicite din setările preferințelor Arch.
-   Returnează noul obiect Rebar.


</div>

Exempluː


```python
import FreeCAD, Arch, Part

Structure = Arch.makeStructure(None, length=1000, width=1000, height=3000)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

p1 = FreeCAD.Vector(-400, 400, 0)
p2 = FreeCAD.Vector(400, 400, 0)
Sketch = FreeCAD.ActiveDocument.addObject('Sketcher::SketchObject', 'Sketch')
Sketch.MapMode = "FlatFace"
Sketch.Support = [(Structure, "Face6")]
Sketch.addGeometry(Part.LineSegment(p1, p2))
FreeCAD.ActiveDocument.recompute()

Rebar = Arch.makeRebar(Structure, Sketch, diameter=80, amount=7, offset=50)
Rebar.OffsetStart = 100
Rebar.OffsetEnd = 100
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar/ro
