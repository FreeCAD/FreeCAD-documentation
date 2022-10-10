---
- GuiCommand   */de
   Name   *Std MeasureDistance
   Name/de   *Std AbstandMessen
   MenuLocation   *Werkzeuge → Abstand messen
   Workbenches   *All
   SeeAlso   *[Part Linear messen](Part_Measure_Linear/de.md), [Draft Maß](Draft_Dimension/de.md), [Arch Vermessung](Arch_Survey/de.md)
---

# Std MeasureDistance/de


</div>

## Beschreibung

Das Werkzeug **Std AbstendMessen** erstellt ein Distance-Objekt, das den Abstand zwischen zwei Punkten misst und anzeigt.

## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen   *
    -   Die Schaltfläche **<img src="images/Std_MeasureDistance.svg" width=16px> [Std Abstand messen](Std_MeasureDistance/de.md)** drücken.
    -   Den Menüeintrag **Werkzeuge → <img src="images/Std_MeasureDistance.svg" width=16px> Abstand messen** auswählen.
2.  Den ersten Messpunkt irgendwo auf einem Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
3.  Den zweiten Messpunkt irgendwo auf einem Objekt in der3D-Ansicht auswählen.
4.  Die Auswahlreihenfolge der Punkte kann die Lage der Maßlinie beeinflussen.
5.  Wahlweise kann die Lage der Maßlinie umgekehrt werden, indem die {{PropertyView/de|Mirror}} des Distance-Objekts geändert wird.

## Hinweise

-   You cannot use the [Draft](Draft_Workbench.md) snap tools with this command.
-   To add dimensions to drawings use the dimension tools from the [TechDraw Workbench](TechDraw_Workbench.md).
-   For more comprehensive measuring tools, install the <img alt="" src=images/Manipulator_workbench_icon.svg  style="width   *24px;"> [Manipulator Workbench](Manipulator_Workbench.md) (an [external workbench](External_workbenches.md)).

## Eigenschaften

### Daten


{{TitleProperty|Basis}}

-    **Label**   * by default the label contains the measured distance, but this distance is not updated when P1 or P2 are later changed.


{{TitleProperty|Measurement}}

-    **P1**   * the first dimension point.

-    **P2**   * the second dimension point.

-    **Distance**   * (read-only) the measured distance between P1 and P2.

### Ansicht


{{TitleProperty|Basis}}

-    **Dist Factor**   * this factor, multiplied by the measured distance, determines the dimension line offset.

-    **Font Size**   * the height of the letters (line height in pixels).

-    **Mirror**   * if set to `True` the position of the dimension line relative to P1 and P2 is flipped.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std MeasureDistance/de
