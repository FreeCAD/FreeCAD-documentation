---
- GuiCommand:/de
   Name:PartDesign SubtractivePipe
   Name/de:PartDesign Subtraktives Rohr 
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   MenuLocation:Part Design → Abziehbares Rohr
   Version:0.17
   SeeAlso:[Additives Rohr](PartDesign_AdditivePipe/de.md), [Subtraktive Ausformung](PartDesign_SubtractiveLoft/de.md)
---


</div>

## Beschreibung

**Subtraktives Rohr** erzeugt einen subtraktiven Volumenkörper im aktiven Bauteil, indem eine oder mehrere Skizzen (auch als Querschnitte bezeichnet) entlang eines offenen oder geschlossenen Pfades ausgetragen werden. Seine Form wird dann von dem vorhandenen Körper subtrahiert. Subtraktives Rohr wird häufig zusammen mit [Part Helix](Part_Helix/de.md) und [PartDesign ShapeBinder](PartDesign_ShapeBinder/de.md) verwendet, um ein Gewinde zu erzeugen; siehe das [Schraubengewinde Tutorium](Thread_for_Screw_Tutorial/de.md) für Einzelheiten.

## Anwendung


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src="images/PartDesign_SubtractivePipe.svg" width=24px> '''Subtraktives Rohr'''** Schaltfläche.
2.  Im **Element auswählen** Dialog, wähle eine Skizze, die als erster Querschnitt verwendet werden soll, und klicke**OK**.
    -   Alternativ kann eine einzelne Skizze ausgewählt werden, bevor die Schaltfläche Subtraktives Rohr gedrückt wird.
3.  Im **Rohrparameter** unter **Profil**, drücke die **Objekt** Schaltfläche.
4.  Wähle die Skizze aus, die als Pfad in der 3D Ansicht verwendet werden soll:
    -   Alternativ können Kanten des Körpers ausgewählt werden, durch drücken von **Add Edge** und auswählen von Kanten in der 3D Ansicht
5.  Um mehr als einen Querschnitt zu verwenden, setze unter **Schnitttransformation** den Umwandlungsmodus auf *\'Mehrfachschnitt*; drücke **Add Section** und wähle dann eine Skizze in der 3D Ansicht aus. Wiederhole diesen Vorgang für jeden weiteren Querschnitt.
6.  Lege bei Bedarf Optionen fest und klicke auf **OK**.


</div>

## Optionen

**Section Transformation**:

-   Select **Constant** to use a single profile
-   Select **Multisection** to use multiple profiles

**Section Orientation**:

-   Standard
    -   This keeps the cross section shape perpendicular to the path. This is the default setting.
-   Fixed
    -   Orientation set by first profile and constant throughout. This deactivates the alignment to the path normal vector. That means that the cross-section shape will not rotate with the path. Sweep along a circle to see the effect.
-   Frenet
    -   Create minimum possible twisting of profile. For more info, see [Frenet-Serret Formulas](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas)
-   Auxiliary
    -   Specify secondary path to guide pipe.
    -   For each point **P** along the sweep path, there will be a corresponding point **Q** on the auxiliary path.
    -   As the profile is swept, it will be transformed such that the **PQ** line is the normal of the sweep path.
    -   If **Curvelinear equivalence** is set, then the **Q** points are scaled proportionally along the sweep path, regardless of is length.
-   Binormal
    -   Specify binormal vector in X, Y and Z

**Corner Transition**

-   Transformed
-   Right
-   Rounded

## Eigenschaften

-    **Label**: Name, der der Vorgang erhalten hat, dieser Name kann nach Belieben geändert werden.

-    **Verfeinern**: true oder false. Wenn auf true gesetzt, wird der Volumenkörper von Restkanten gereinigt, die von den Formelementen hinterlassen wurden. Siehe [Part FormVerfeinern](Part_RefineShape/de.md) für weitere Einzelheiten.

-    **Abschnitte**: listet die verwendeten Abschnitte auf.

-    **Rücken Tangente**: true oder false (Standard). True erweitert den Pfad um tangentiale Kanten.

-    **Hilfs Rücken Tangente**: true oder false (Standard). True erweitert den Hilfspfad um tangentiale Kanten.

-    **Hilfs Kurvelinear**: true oder false (Standard). True berechnet die Normale zwischen äquidistanten Punkten auf beiden Rücken.

-    **Modus**: Profilmodus. Siehe [Options](#Options.md).

-    **Binormal**: Binormalvektor für den entsprechenden Ausrichtungsmodus.

-    **Übergang**: Übergangsmodus. Die Optionen sind *umgewandelt*, *Rechte Ecke* oder *Runde Ecke*.

-    **Transformation**: *Konstante* verwendet einen einzigen Querschnitt. *Mehrfachschnitt* verwendet zwei oder mehr Querschnitte. *Linear*, *S-förmig* und *Interpolation* sind derzeit nicht funktionsfähig.

## Begrenzungen

-   Skizzen, die für Querschnitte verwendet werden, müssen geschlossene Profile bilden.
-   Es ist nicht möglich, einen Knotenpunkt als Querschnitt zu verwenden.
-   Ein Querschnitt kann nicht auf der gleichen Ebene liegen wie die unmittelbar vorausgehende.
-   Um die Form des Rohres besser kontrollieren zu können, wird empfohlen, dass alle Querschnitte die gleiche Anzahl von Segmenten haben. Beispielsweise kann bei einem Rohr zwischen einem Rechteck und einem Kreis der Kreis in 4 zusammenhängende Bögen aufgeteilt werden.





{{PartDesign Tools navi

}} 
