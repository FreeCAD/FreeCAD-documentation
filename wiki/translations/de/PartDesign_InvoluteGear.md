---
- GuiCommand   */de
   Name   *PartDesign InvoluteGear
   Name/de   *PartDesign Evolventenzahnrad
   MenuLocation   *Part Design → Evolventenzahnrad...
   Workbenches   *[PartDesign](PartDesign_Workbench/de.md)
---

# PartDesign InvoluteGear/de

## Beschreibung

Dieses Werkzeug erlaubt es ein 2D-Profil eines Evolventenzahnrades zu erstellen. Dieses 2D-Profil ist vollständig parametrisch und kann mit den Formelementen [PartDesign Aufpolsterung](PartDesign_Pad/de.md) oder [PartDesign Wendel](PartDesign_AdditiveHelix/de.md) extrudiert werden.

Für detailliertere Informationen siehe Wikipedia   * [Gear](https   *//en.wikipedia.org/wiki/Gear) und [Involute Gear](https   *//en.wikipedia.org/wiki/Involute_gear) (engl.).

![](images/PartDesign_Involute_Gear_01.png )

## Anwendung

### Profil erstellen 

1.  Wahlweise den richtigen Körper aktivieren.

2.  Zum Menü **Part Design → [<img src=images/PartDesign_InternalExternalGear.svg style="width   *16px"> Involute gear...** wechseln.

3.  Die Evolventenparameter anpassen.

4.  
    **OK**klicken.

5.  Wurde noch kein Körper aktiviert   * Das Zahnrad auf einen Körper ziehen und ablegen, um es mit weiteren Formelementen zu verwenden.

### Ein geradverzahntes Stirnrad erstellen 

1.  Das Zahnradprofil in der [Baumansicht](Tree_view/de.md) Auswählen.

2.  Die Schaltfläche **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Aufpolsterung](PartDesign_Pad/de.md)** drücken.

3.  Die {{PropertyData/de|Length}} des Blocks auf die gewünschte Zahnradbreite einstellen.

4.  
    **OK**klicken.

### Ein schrägverzahntes Stirnrad erstellen 


{{Version/de|0.19}}

1.  Select the gear profile in the [Tree view](Tree_view.md).
2.  Press the **<img src="images/PartDesign_AdditiveHelix.svg" width=16px> [PartDesign AdditiveHelix](PartDesign_AdditiveHelix.md)** button.
3.  Choose as Axis the normal of the gear profile, that is **Normal sketch axis** <small>(v0.20)</small> . (In earlier versions the **Base Z axis** can be used as long as the profile\'s plane has not been altered.)
4.  Choose a **Height-Turns** mode.
5.  Set the **Height** to the desired face width of the gear.
6.  To set the desired helical angle an [Expression](Expressions.md) for the **Turns** is required.
    1.  Click the blue <img alt="" src=images/Bound-expression.svg  style="width   *16px;"> icon at the right of the input field.
    2.  Enter the following formula   * `Height * tan(25°) / (InvoluteGear.NumberOfTeeth * InvoluteGear.Modules * pi)`, where `25°` is an example for the desired helical angle (also known as beta-value) and `InvoluteGear` is the **Name** of the profile.
    3.  Click **OK** to close the formula editor.
7.  Click **OK** to close the task panel.

Hint   * To make the helical angle an accessible parameter, use a *dynamic property*   *

1.  Select the profile.
2.  In the [Property editor](Property_editor.md) activate the **Show all** option in the context menu.
3.  Again in the context menu, select **Add Property**. Note   * this entry is only available when **Show all** is active.
4.  In the **Add Property** dialog   *
    1.  Choose `App   *   *PropertyAngle` as Type.
    2.  Set `Gear` as Group.
    3.  Set `HelicalAngle` as Name (without a space).
    4.  Click **OK**
5.  Now a new property **Helical Angle** (space added automatically), with an initial value of `0.0°`, becomes available.
6.  Assign the desired helical angle to the new property.
7.  In the formula of the **Turns** property of the AdditiveHelix, you can now reference `InvoluteGear.HelicalAngle` instead of the hard coded value of e.g. `25°`; again assuming `InvoluteGear` is the **Name** of the profile.

## Eigenschaften

-    {{PropertyData/de|External Gear}}(Stirnrad)   * Wahr oder Falsch

-    {{PropertyData/de|High Precision}}(Hohe Präzision)   * Wahr oder Falsch

-    {{PropertyData/de|Modules}}(der Modul)   * Teilkreisdurchmesser geteilt durch die Anzahl der Zähne.

-    {{PropertyData/de|Number Of Teeth}}   * Legt die Anzahl der Zähne fest.

-    {{PropertyData/de|Pressure Angle}}(Eingriffswinkel)   * Winkel zwischen der Wirkungslinie und einer Normalen zu der Linie, die die Zahnradmitten verbindet. Standard ist 20 Grad. ([Weitere Informationen](https   *//de.wikipedia.org/wiki/Evolventenverzahnung))

## Limitations

-   It is currently not possible to adjust the tooth thickness. Tooth and tooth space are distributed equally on the pitch circle. Thus the only way to control backlash is to adjust the center distance in a gear paring.
-   There is currently no [undercut](https   *//www.tec-science.com/mechanical-power-transmission/involute-gear/undercut/) in the generated gear profile. That means gears with a low number of teeth can interfere with the teeth of the mating gear. The lower limit depends on the **Pressure Angle** and is around 17 teeth for 20° and 32 for 14.5°. Most practical applications tolerate a missing undercut for gears a little smaller than this theoretical limit though.

## Tutorien

[How to make gears in FreeCAD](https   *//www.youtube.com/watch?v=8VNhTrnFMfE)

## Verwandt

-   Arbeitsbereich [FCGear](FCGear_Workbench/de.md)





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign InvoluteGear/de
