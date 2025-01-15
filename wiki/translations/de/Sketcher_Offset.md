---
 GuiCommand:
   Name: Sketcher Offset
   Name/de: Sketcher Versatzkontur
   MenuLocation: Skizze , Sketcher-Werkzeuge , Versatzkontur
   Workbenches: Sketcher_Workbench/de
   Shortcut: **Z** **T**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Offset/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_Offset.svg  style="width:24px;"> [Sketcher Versatzkontur](Sketcher_Offset/de.md) erstellt eine equidistante Kante (Versatzkontur) um ausgewählte Kanten herum.

<img alt="" src=images/Sketcher_OffsetExample.png‎  style="width:400px;"> 
*Equidistante Kanten um eine geschlossene (O) und eine offene (U) Hilfs-Polylinie*



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

Dim-OVP = Dimensional [On-View-Parameters](Sketcher_Preferences/de#Allgemein.md) (In-Ansicht-Parameter zur maßlichen Festlegung).

1.  Eine oder mehrere Linien, Kreise und/oder Kreisbögen auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_Offset.svg" width=16px> [Versatzkontur](Sketcher_Offset/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher Werkzeuge → <img src="images/Sketcher_Offset.svg" width=16px> Versatzkontur** auswählen.
    -   Ein Rechtsklick in der [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_Offset.svg" width=16px> Versatzkontur** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **Z** then **T**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Der Abschnitt **Versatzparameter** wird im oberen Bereich des [Sketcher-Dialogs](Sketcher_Dialog/de.md) hinzugefügt.
5.  Wahlweise die **U**-Taste drücken oder die CheckBox **Originalgeometrien löschen** aktivieren, um nur den neuen Umriss zu behalten.
6.  Wahlweise die **J**-Taste drücken oder die CheckBox **Offset-Randbedingung hinzufügen** aktivieren, um eine maßliche Randbedingung zwischen dem versetzten Umriss und der originalen Geometrie hinzuzufügen.
7.  Wahlweise die **M**-Taste drücken oder in der Ausklappliste des Abschnitts Versatzparameter den Werkzeugmodus auswählen:
    -   <img alt="" src=images/Sketcher_OffsetArc.svg  style="width:16px;"> 
**Kreisbogen**
    -   <img alt="" src=images/Sketcher_OffsetIntersection.svg  style="width:16px;"> 
**Schnitt**
8.  Einen Punkt auswählen, um den Versatzabstand festzulegen. Oder mit Dim-OVP: diesen Abstand eingeben.
9.  Die Geometrie wird erstellt und wenn **Offset-Randbedingung hinzufügen** aktiviert ist, wird eine maßliche Randbedingung hinzugefügt.


<div lang="en" dir="ltr" class="mw-content-ltr">

## Limitations


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

This tool has certain limitations, mainly due to [OCC](OpenCASCADE.md) issues:

-   The following types of geometry are currently unsupported: ellipses, B-splines, hyperbolas and parabolas.
-   Offsetting a single line can yield unexpected results.
-   Open profiles are offset on both sides, creating a closed contour.
-   External geometry can\'t be offset directly.


</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Offset/de
