---
 GuiCommand:
   Name: PartDesign Revolution
   Name/de: PartDesign Drehteil
   MenuLocation: Part Design , Objekte hinzufügen , Drehteil
   Workbenches: PartDesign_Workbench/de
   SeeAlso: PartDesign_Groove/de
---

# PartDesign Revolution/de



## Beschreibung

Das Werkzeug **Drehkörper** erstellt einenVolumenkörper durch Rotation einer Skizze oder eines 2D-Objekts um eine gegebene Achse.

![](images/PartDesign_Revolution_example.svg )



*Oben: Skizze (A) wird um 270 Grad gegen den Uhrzeigersinn um die Achse (B) gedreht; der resultierende Volumenkörper (C) ist rechts dargestellt.*



## Anwendung

1.  Eine einzelne Skizze oder eine oder mehrere Flächen des Körpers auswählen.
2.  Die Schaltfläche **<img src="images/PartDesign_Revolution.svg" width=16px> [Drehteil](PartDesign_Revolution/de.md)** drücken.
3.  Parameter des Drehteils einstellen, siehe [Optionen](#Optionen.md) unten.
4.  Die Schaltfläche **OK** drücken.



## Optionen

Während der Erstellung des Drehteils oder nach einem Doppelklick auf ein bestehendes Drehteils in der [Baumansicht](Tree_view/de.md) wird der Aufgaben-Dialog **Drehteil-Parameter** angezeigt. Er ermöglicht folgende Einstellungen:

![](images/partdesign_revolution_parameters.png )



### Typ


{{Version/de|1.0}}

Typ bietet fünf verschiedene Möglichkeiten zum Festlegen des Winkels des Drehteils:

#### Dimension

Enter a numeric value for the **Angle** of the revolution. With the option **Symmetric to plane** the revolution will extend half the given angle to either side of the sketch or face.

#### To last 

The revolution will extend up to the last face of the support it encounters in its direction. If there is no support, an error message will appear.

#### To first 

The revolution will extend up to the first face of the support it encounters in its direction. If there is no support, an error message will appear.

#### Up to face 

The revolution will extend up to a face. Press the **Face** button and select a face or a [datum plane](PartDesign_Plane.md) from the Body.

#### Two dimensions 

This allows to enter a second angle in which the revolution should extend in the opposite direction. The directions can be switched by checking the **Reversed** option.



### Achse

Specifies the axis of the revolution:

-   **Vertikale Skizzenachse**: Wählt die vertikale Achse der Skizze aus.
-   **Horizontale Skizzenachse**: Wählt die horizontale Achse der Skizze aus.
-   **Konstruktionslinie**: wählt eine Hilfslinie der Skizze aus, die für das Drehteil verwendet wird. Die Aufklappliste enthält einen Eintrag für jede Hilfslinie. Die erste Hilfslinie, die in der Skizze erstellt wurde, wird mit *Konstruktionslinie 1* bezeichnet.
-   **Basis (X-/Y-/Z-)Achse**: wählt die X-, Y- oder Z-Achse des Urspungs des Körpers (Body) aus.
-   **Referenz auswählen\...**: ermöglicht die Auswahl einer geraden Kante oder einer [Bezugslinie](PartDesign_Line/de.md) am Körper.

Note that when changing the axis, the **Reversed** option may be (un)checked automatically.



### Winkel

Legt den Winkel des Drehteils fest. Diese Option steht nur zur Verfügung, wenn für **Typ** **Abmessung** oder **Zwei Längen** ausgewählt wurde. Winkel größer als 360° sind nicht möglich, auch keine negativen Werte; stattdessen verwendet man dafür die Option **Umgekehrt**.



### Symmetrisch zur Ebene 

Diese Option auswählen, wenn jeweils die Hälfte des angegeben Winkels zu beiden Seiten der Skizzenebene oder Fläche ausgeführt werden soll. Diese Option steht nur zur Verfügung, wenn für **Typ** **Abmessung** ausgewählt wurde



### Umgekehrt

Kehrt die Richtung des Drehteils um.

### 2nd angle 


{{Version/de|1.0}}

Defines the angle of the revolution in the opposite direction. This option is only available if **Type** is **Two dimensions** and **Angle** is smaller than 360°.



## Eigenschaften

### Data


{{TitleProperty|Part Design}}

-    **Refine|Bool**
    


{{TitleProperty|Revolution}}

-    **Type|Enumeration**
    

-    **Base|Vector**: (read-only)

-    **Axis|Vector**: (read-only)

-    **Angle|Angle**
    

-    **Up To Face|LinkSub**
    

-    **Angle2|Angle**
    

-    **Reference Axis|LinkSub**
    


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    

## Notes

-   A <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [ShapeBinder](PartDesign_ShapeBinder.md) cannot be used for the profile.
-   When using a <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [SubShapeBinder](PartDesign_SubShapeBinder.md) for the profile, selecting the binder in the [Tree view](Tree_view.md) will fail, instead the binder\'s face has to be selected in the [3D view](3D_view.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/de
