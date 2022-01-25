---
- GuiCommand:/ro
   Icon:PartDesign InternalExternalGear.svg
   Name:PartDesign InvoluteGear
   Name/ro:PartDesign: Angrenaj cilindric cu dinți drepți în evolventă
   MenuLocation:Part Design → Involute gear...
   Workbenches:[PartDesign](PartDesign_Workbench.md)
---

# PartDesign InvoluteGear/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Acest instrument vă permite să creați un profil 2D al unei roți dințate în evolventă. Acest profil 2D este complet parametric și poate fi extrudat cu funcția [PartDesign Pad](PartDesign_Pad.md).

Pentru a face un profil elicoidală, acesta trebuie extrudat cu ajutorul instrumentului Sweep folosind o elice ca traiectorie


</div>

For more detailed information see Wikipedia\'s entries for: [Gear](https://en.wikipedia.org/wiki/Gear) and [Involute Gear](https://en.wikipedia.org/wiki/Involute_gear)

![](images/PartDesign_Involute_Gear_01.png )

## Usage

### Create the profile 


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Go to the **Part Design → <img alt="" src=images/PartDesign_InvoluteGear.png  style="width:16px;"> Involute gear\...** menu.
2.  Set the Involute parameters.
3.  Click OK.
4.  Profilul în evolventă este creat în afara corpului activ. Trageți-l și plasați-l într-un corp pentru a aplica alte funcții, cum ar fi extrudarea.


</div>

### Create a spur gear 

1.  Select the gear profile in the tree.
2.  Press the **<img src="images/PartDesign_Pad.svg" width=16px> PartDesign Pad** button.
3.  Set the pad\'s **Length** to the desired face width of the gear.
4.  Click **OK**

### Create a helical gear 


<small>(v0.19)</small> 

1.  Select the gear profile in the tree.
2.  Press the **<img src="images/PartDesign_AdditiveHelix.svg" width=16px> [PartDesign AdditiveHelix](PartDesign_AdditiveHelix.md)** button.
3.  Choose as Axis the normal of the gear profile, that is **Normal sketch axis** <small>(v0.20)</small> . (In earlier versions the **Base Z axis** can be used as long as the profile\'s plane has not been altered.)
4.  Choose a **Height-Turns** mode.
5.  Set the **Height** to the desired face width of the gear.
6.  To set the desired helical angle an [Expressions](Expressions.md) for the **Turns** is required.
    1.  Click the blue <img alt="" src=images/Bound-expression.svg  style="width:16px;"> icon at the right of the input field.
    2.  Enter the following formula: `Height * tan(25°) / (InvoluteGear.NumberOfTeeth * InvoluteGear.Modules * pi)`, where `25°` is an example for the desired helical angle (also known as beta-value) and `InvoluteGear` is the **Name** of the profile.
    3.  Click **OK** to close the formula editor.
7.  Click **OK** to close the task panel.

Hint: To make the helical angle an accessible parameter, use a *dynamic property*:

1.  Select the profile.
2.  In the [Property editor](Property_editor.md) activate the **Show all** option in the context menu.
3.  Again in the context menu, select **Add Property**. Note: this entry is only available when **Show all** is active.
4.  In the **Add Property** dialog:
    1.  Choose `App::PropertyAngle` as Type.
    2.  Set `Gear` as Group.
    3.  Set `HelicalAngle` as Name (without a space).
    4.  Click **OK**
5.  Now a new property **Helical Angle** (space added automatically), with an initial value of `0.0°`, becomes available.
6.  Assign the desired helical angle to the new property.
7.  In the formula of the **Turns** property of the AdditiveHelix, you can now reference `InvoluteGear.HelicalAngle` instead of the hard coded value of e.g. `25°`; again assuming `InvoluteGear` is the **Name** of the profile.

## Properties


<div class="mw-translate-fuzzy">

-   Angrenaj Extern: True or false


</div>


<div class="mw-translate-fuzzy">

-   Precizie ridicată: True or false


</div>


<div class="mw-translate-fuzzy">

-   Modulul:

Diametrul primitiv împărțit la numărul de dinți. Sau: Modulul X Numărul de dinți = Diametrul Primitiv (acestea sunt diametrele tangente într-o pereche de roți).

Acestea depind de distanța centrală a arborilor suport și de raportul de reducere a vitezei dintre cei doi arbori.


</div>


<div class="mw-translate-fuzzy">

-   Număr de dinți: Definește numărul de dinți.


</div>


<div class="mw-translate-fuzzy">

-   Unghiul de presiune: Unghiul ascuțit între linia de acțiune (tracțiune) și o linie normală la linia care leagă centrele de angrenaje (tangentă la cercurile primitive).

Valoarea implicită este de 20 de grade. ([More info](http://en.wikipedia.org/wiki/Involute_gear))


</div>

## Tutorials

[How to make gears in FreeCAD](https://www.youtube.com/watch?v=8VNhTrnFMfE)

## Related

-   [FCGear Workbench](FCGear_Workbench.md)


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign InvoluteGear/ro
