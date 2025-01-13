---
 GuiCommand:
   Name: PartDesign Groove
   Name/de: PartDesign Nut
   MenuLocation: Part Design , Objekte abziehen , Nut
   Workbenches: PartDesign_Workbench/de
   SeeAlso: PartDesign_Revolution/de
---

# PartDesign Groove/de



## Beschreibung

Das Werkzeug **Nut** dreht eine ausgewählte Skizze oder ein Profil um eine gegebene Achse und entfernt Material aus dem aktiven Körper.

![](images/PartDesign_Groove_example.svg )



*Oben: Skizze (A) ist um die Achse (B) gedreht; die resultierende Nut auf dem Volumenkörper (C) ist rechts dargestellt.*



## Anwendung

1.  Eine einzelne Skizze oder eine oder mehrere Flächen des Körpers auswählen.
2.  Die Schaltfläche **<img src="images/PartDesign_Groove.svg" width=16px> [Nut](PartDesign_Groove/de.md)** drücken.
3.  Parameter der Nut einstellen, siehe [Optionen](#Optionen.md) unten.
4.  Die Schaltfläche **OK** drücken.



## Optionen

Während der Erstellung der Tasche oder nach einem Doppelklick auf eine bestehende Tasche in der [Baumansicht](Tree_view/de.md) wird der Aufgaben-Dialog **Nut-Parameter** angezeigt. Er ermöglicht folgende Einstellungen:

![](images/partdesign_groove_parameters.png )



### Typ


{{Version/de|1.0}}

Typ bietet fünf verschiedene Möglichkeiten zum Festlegen des Winkels der Nut:

#### Dimension

Enter a numeric value for the **Angle** of the groove. With the option **Symmetric to plane** the groove will extend half the given angle to either side of the sketch or face.

#### Through all 

The groove will extend up to the last face of the support it encounters in its direction. With the option **Symmetric to plane** the groove will cut through all material in both directions.

#### To first 

The groove will extend up to the first face of the support it encounters in its direction.

#### Up to face 

The groove will extend up to a face. Press the **Face** button and select a face or a [datum plane](PartDesign_Plane.md) from the Body.

#### Two dimensions 

This allows to enter a second angle in which the groove should extend in the opposite direction. The directions can be switched by checking the **Reversed** option.

### Axis

Specifies the axis of the groove:

-   **Vertikale Skizzenachse**: Wählt die vertikale Achse der Skizze aus.
-   **Horizontale Skizzenachse**: Wählt die horizontale Achse der Skizze aus.
-   **Konstruktionslinie**: wählt eine Hilfslinie der Skizze aus, die für die Nut verwendet wird. Die Aufklappliste enthält einen Eintrag für jede Hilfslinie. Die erste Hilfslinie, die in der Skizze erstellt wurde, wird mit *Konstruktionslinie 1* bezeichnet.
-   **Basis (X-/Y-/Z-)Achse**: wählt die X-, Y- oder Z-Achse des Urspungs des Körpers (Body) aus.
-   **Referenz auswählen\...**: ermöglicht die Auswahl einer geraden Kante oder einer [Bezugslinie](PartDesign_Line/de.md) am Körper.

Note that when changing the axis, the **Reversed** option may be (un)checked automatically.



### Winkel

Legt den Winkel der Nut fest. Diese Option steht nur zur Verfügung, wenn für **Typ** **Abmessung** oder **Zwei Längen** ausgewählt wurde. Winkel größer als 360° sind nicht möglich, auch keine negativen Werte; stattdessen verwendet man dafür die Option **Umgekehrt**.



### Symmetrisch zur Ebene 

Diese Option aktivieren, um jeweils die Hälfte des angegebenen Winkels zu beiden Seiten der Skizze oder Fläche auszuführen, wenn für **Typ** entweder **Abmessung**, oder **Durch alles** ausgewählt wurde.



### Umgekehrt

Kehrt die Richtung der Nut um.



### Zweiter Winkel 


{{Version/de|1.0}}

Defines the angle of the groove in the opposite direction. This option is only available if **Type** is **Two dimensions** and **Angle** is smaller than 360°.



## Eigenschaften

### Data


{{TitleProperty|Groove}}

-    **Type|Enumeration**
    

-    **Base|Vector**: (read-only)

-    **Axis|Vector**: (read-only)

-    **Angle|Angle**
    

-    **Angle2|Angle**
    

-    **Up To Face|LinkSub**
    

-    **Reference Axis|LinkSub**
    


{{TitleProperty|Part Design}}

-    **Refine|Bool**
    


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    

## Notes

-   A <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [ShapeBinder](PartDesign_ShapeBinder.md) cannot be used for the profile.
-   When using a <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [SubShapeBinder](PartDesign_SubShapeBinder.md) for the profile, selecting the binder in the [Tree view](Tree_view.md) will fail, instead the binder\'s face has to selected in the [3D view](3D_view.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Groove/de
