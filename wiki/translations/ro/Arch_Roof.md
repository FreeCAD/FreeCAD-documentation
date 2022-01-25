---
- GuiCommand:/ro
   Name:Arch Roof
   Name/ro:Arch Roof
   MenuLocation:Arch → Roof
   Workbenches:[Arch](Arch_Workbench/ro.md)
   Shortcut:R F
   SeeAlso:[[Arch Structure]], [[Arch Wall]]
---

# Arch Roof/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul Acoperiș vă permite să creați un acoperiș înclinat de la o linie selctată. Obiectul de acoperiș creat este parametric, menținându-și relația cu obiectul de bază. Rețineți că acest instrument este în curs de dezvoltare și ar putea să nu reușească cu forme foarte complexe. Principiul este acela că fiecare margine este văzută alocând un profil de acoperiș (panta, lățimea, lungimea, grosimea \...).


</div>

**Note:** This tool is still in development, and might fail with very complex shapes.

<img alt="" src=images/RoofExample.png  style="width:600px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/RoofExample.png  style="width:600px;">


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Create a wire with following the counterclockwise direction and select it.
    -   <img alt="" src=images/CounterclockwiseWire.png  style="width:600px;">
2.  Press the **<img src="images/Arch_Roof.png" width=16px> [[Arch Roof]]** button, or press **R** then **F** keys
3.  The default roof object could have a strange shape, it\'s because the tool have not all the needed informations.
4.  After creating the default roof, double click on the object in the tree view to access and edit all the properties. Angle must be between 0 and 90.
    -   ![](images/RoofTable.png )
5.  Each line correspond to a roof pane. So you can set properties you want for each roof pane.
6.  To help you, you can set Angle or Run to 0 and defined a Relative Id, this make automatic calculs to find the data relative to the relative Id.
7.  It work like this :
    1.  If Angle = 0 and Run = 0 then profile is identical to the relative profile.
    2.  If Angle = 0 then angle is calculated so that the height is the same one as the relative profile.
    3.  If Run = 0 then Run is calculated so that the height is the same one as the relative profile.
8.  At the end, set an angle to 90° to make a gable.
    -   <img alt="" src=images/RoofProfil.png  style="width:600px;">
9.  **Also you can check this video** : <https://www.youtube.com/watch?v=4Urwru71dVk>


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

-   Roofs share the common properties and behaviours of all [Arch Components](Arch_Component.md)


</div>

## Proprietăți


<div class="mw-translate-fuzzy">

-    **Angles**: Valorea unghiurilor apei/versantului acoperișului (un unghi pentru fiecare margine filamentului).

-    **Runs**: Proiecția orizontală a lungimii apei/versantului acoperișului (o apă/versant pentru fiecare margine a filamentului inițial).

-    **IdRel**: Relația/raportul Id între unghiul și panta acoperișului

-    **Thickness**: List of thickness of the roof pane. (a thickness for each edge in the wire).

-    **Overhang**: Proiecția orizontală a streașinei fiecărei ape/versat al acoperișului (o sreașină pentru fiecare margine a filamentului original).

-    **Face**: Indexul fațetei obiectului de bază de utilizat \#Nu este deocamdaă utilizat


</div>


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul Acoperiș poate fi folosit în [macros](macros.md) și din consola python utilizând următoarea funcție:


</div>


```python
Roof = makeRoof(baseobj=None, facenr=0, angles=[45.,], run=[], idrel=[0,], thickness=[50.,], overhang=[100.,], name="Roof")
```


<div class="mw-translate-fuzzy">


:   Face un acoperiș pe baza unui filament închis. Puteți furniza o listă de unghiuri, run, idrel, grosime, consola pentru fiecare margine a firului pentru a defini forma acoperișului. Valoarea implicită pentru unghi este de 45 și lista este completată automat pentru a se potrivi cu numărul de muchii din fir.


</div>

Exempluː


```python
import FreeCAD as App
import Arch, Draft

doc = App.newDocument()

rect = Draft.makeRectangle(3000, 4000)
doc.recompute()

roof = Arch.makeRoof(rect, angles=[30.,])

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(0, 2000, 0)

wire = Draft.make_wire([p1, p2, p3], closed=True)
doc.recompute()

roof1 = Arch.makeRoof(wire)

doc.recompute()
```


<div class="mw-translate-fuzzy">


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Roof/ro
