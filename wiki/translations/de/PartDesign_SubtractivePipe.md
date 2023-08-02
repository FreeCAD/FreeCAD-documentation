---
- GuiCommand:
   Name: PartDesign SubtractivePipe
   Name/de: PartDesign Subtraktives Rohr
   MenuLocation: Part Design -> Create a substractive feature -> Subtractive pipe
   Workbenches: PartDesign_Workbench/de
   Version: 0.17
   SeeAlso: PartDesign_AdditivePipe/de, PartDesign_SubtractiveLoft/de
---

# PartDesign SubtractivePipe/de



## Beschreibung

**Subtraktives Rohr** erzeugt einen subtraktiven Volumenkörper im aktiven Bauteil, indem eine oder mehrere Skizzen (auch als Querschnitte bezeichnet) entlang eines offenen oder geschlossenen Pfades ausgetragen werden. Seine Form wird dann von dem vorhandenen Körper subtrahiert. Subtraktives Rohr wird häufig zusammen mit [Part Helix](Part_Helix/de.md) und [PartDesign ShapeBinder](PartDesign_ShapeBinder/de.md) verwendet, um ein Gewinde zu erzeugen; siehe das [Schraubengewinde Tutorium](Thread_for_Screw_Tutorial/de.md) für Einzelheiten.



## Anwendung

1.  Die Schaltfläche **<img src="images/PartDesign_SubtractivePipe.svg" width=24px> '''Subtraktives Rohr'''** drücken.
2.  Im Dialog **Element auswählen** eine Skizze auswählen, die als erster Querschnitt verwendet werden soll, und **OK** klicken.
    -   Alternativ kann eine einzelne Skizze ausgewählt werden oder eine Fläche eines 3D-Objekts ({{Version/de|0.20}}), bevor die Schaltfläche (subtraktives) Rohr gedrückt wird.
3.  Im Dialogbereich **Rohr-Parameter** unter **Profil** die Schaltfläche **Objekt** drücken.
4.  Die Skizze auswählen, die in der 3D-Ansicht als Pfad verwendet werden soll:
    -   Alternativ können Kanten des Körpers ausgewählt werden, indem **Kante hinzufügen** gedrückt wird und die Kanten in der 3D-Ansicht ausgewählt werden.
5.  Um mehr als einen Querschnitt zu verwenden, wird unter **Abschnitt Transformation** der Transformationsmodus auf **Mehrere Abschnitte** gesetzt, die Schaltfläche **Schnitt hinzufügen** drücken und dann eine Skizze in der 3D-Ansicht auswählen. Diesen Vorgang für jeden weiteren Querschnitt wiederholen.
6.  Bei Bedarf Optionen festlegen und auf **OK** klicken.



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



## Hinweise

-   Um die Form des Rohres besser steuern zu können, wird empfohlen, dass alle Querschnitte mit derselben Anzahl von Abschnitten erstellt werden. Beispielsweise sollte für ein Rohr zwischen einem Rechteck und einem Kreis der Kreis in vier verbundene Bögen aufgebrochen werden.
-   Das Rohr kann in einem einzelnen Knotenpunkt ([Vertex](Glossary/de#Vertex.md)) einer Skizze oder eines Körpers beginnen oder enden. {{Version/de|0.20}}
-   Wird ein [Knotenpunkt](Glossary#Vertex.md) verwendet, muss er in den meisten Fällen als letzter Querschnitt des Rohres verwendet werden. Die Reihenfolge der Querschnitte kann geändert werden, indem sie in der Liste verschoben werden.
-   Der Pfad kann nur aus einer einzelnen Skizze, einem Formelement oder einem Formbinder erstellt werden. Falls er entlang mehrerer Kanten verschiedener Skizzen ausgetragen werden soll, kann ein **[<img src=images/PartDesign_SubShapeBinder.svg style="width:16px"> [Teilformbinder](PartDesign_SubShapeBinder.md)** verwendet werden.
-   Der Pfad darf keine Verzweigungen oder T-Verbindungen usw. enthalten; (nur) geschlossene Konturen sind erlaubt.
-   Es kann zu Problemen führen, wenn ein Querschnitt in 3D nicht senkrecht auf dem Pfad steht.
-   Ein Querschnitt kann nicht mit dem unmittelbar vorhergehenden Querschnitt auf derselben Ebene liegen.
-   Ein Querschnitt darf keine aufgetrennten oder sich kreuzende Schlaufen enthalten.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePipe/de
