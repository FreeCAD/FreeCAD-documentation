---
- GuiCommand:
   Name: PartDesign Revolution
   Name/de: PartDesign Drehteil
   MenuLocation: Part Design - Objekte hinzufügen - Drehteil
   Workbenches: [PartDesign](PartDesign_Workbench/de.md)
   SeeAlso: [PartDesign Nut](PartDesign_Groove/de.md)
---

# PartDesign Revolution/de



## Beschreibung

Das Werkzeug **Drehkörper** erstellt einenVolumenkörper durch Rotation einer Skizze oder eines 2D-Objekts um eine gegebene Achse.

![](images/PartDesign_Revolution_example.svg ) 
*Oben: Skizze (A) wird um 270 Grad gegen den Uhrzeigersinn um die Achse (B) gedreht; der resultierende Volumenkörper (C) ist rechts dargestellt.*



## Anwendung

1.  Die Skizze auswählen, die rotiert werden soll. Alternativ kann eine Fläche des vorhandenen Festkörpers verwendet werden.

2.  Die Schaltfläche **<img src="images/_PartDesign_Revolution.svg" width=24px> '''Drehteil'''** drücken.

3.  Drehparameter festlegen (siehe nächster Abschnitt).

4.  
    **OK**drücken.



## Optionen

Bei der Erstellung eines Drehteils bietet der Dialog **Parameter der Rotation** einige Parameter an, die angeben, wie die Skizze gedreht werden soll.

  
  ![](images/partdesign_revolution_parameters.png )
  



### Achse

Diese Option gibt die Achse an, um die die Skizze rotieren soll.

-   **Vertikale Skizzenachse**: Wählt die vertikale Achse der Skizze aus.
-   **Horizontale Skizzenachse**: Wählt die horizontale Achse der Skizze aus.
-   **Konstruktionslinie**: wählt eine Konstruktionslinie der Skizze aus, die für die Drehung verwendet wird. Die Aufklappliste enthält einen Eintrag für jede Konstruktionslinie. Die erste Konstruktionslinie, die in der Skizze erstellt wurde, wird mit *Konstruktionslinie 1* bezeichnet.
-   **Basis (X-/Y-/Z-)Achse**: wählt die X-, Y- oder Z-Achse des Urspungs des Körpers (Body) aus.
-   **Referenz auswählen\...**: ermöglicht die Auswahl einer Kante des Körpers oder einer [Bezugslinie](PartDesign_Line/de.md) in der 3D-Ansicht.



### Winkel

Dies steuert den Winkel, über den die Rotation zu bilden ist. 360 ° wäre z.B. eine vollständige, zusammenhängende Rotation. Die Bilder im Abschnitt [ Beispiele](#Examples.md) zeigen einige der Möglichkeiten bei der Angabe verschiedener Winkel. Es ist nicht möglich, negative Winkel anzugeben (verwenden Sie stattdessen die Option *\'Umgekehrt\'*) oder Winkel größer als 360 °.



### Symmetrisch zur Ebene 

Wenn ausgewählt, wird die Rotation um die Hälfte des angegeben Winkels erweiterte in beide Richtungen der Skizzenebene.



### Umgekehrt

Wenn ausgewählt, ist die Rotationsrichtung umgekehrt zur vorgegebenen Richtung im Uhrzeigersinn.



## Eigenschaften

Unterhalb wird beschrieben, welche Eigenschaften im Nachhinein änderbar sind. *Basis* und *Achse* sind nicht änderbar.

-    {{PropertyData/de|Winkel}}: Drehwinkel der Rotation. Siehe [Winkel](#Winkel.md).

-    {{PropertyData/de|Label}}: Frei wählbare Bezeichnung des Drehkörpers.

-    {{PropertyData/de|Midplane}}: true oder false. Siehe [Symmetrisch zur Ebene](#Symmetrisch_zur_Ebene.md).

-    {{PropertyData/de|Umkekehrt}}: true oder false. Siehe [Umgekehrt](#Umgekehrt.md).

-    {{PropertyData/de|Verfeinern}}: true oder false. Wenn auf true gesetzt, wird der Festkörper von übriggebliebenen Restkanten der Formelemente bereingt . Siehe [Part Form aufbereiten](Part_RefineShape/de.md) für weitere Details.



## Beispiele

![Beispiel Rotation mit einer Konstruktionslinie als Rotationsachse: In diesem Bild ist der Winkel 75 °, die Rotation ist um die Konstruktionslinie (Skizzenachse 0)](images/PartDesign_Revolution_axis_fromconstructionlines1.jpg )



## Hilfreiche Verweise 

Ein [ausführliches Anwendungsbeispiel](http://forum.freecadweb.org/viewtopic.php?f=3&t=3674) im Forum.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/de
