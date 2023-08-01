---
- GuiCommand:
   Name: PartDesign SubtractiveLoft
   Name/de: PartDesign Ausformung
   MenuLocation: Part Design - Objekte abziehen - Ausformung
   Workbenches: [PartDesign](PartDesign_Workbench/de.md)
   Version: 0.17
   SeeAlso: [PartDesign AdditiveAusformung](PartDesign_AdditiveLoft/de.md), [PartDesign SubtraktivesRohr](PartDesign_SubtractivePipe/de.md)
---

# PartDesign SubtractiveLoft/de



## Beschreibung

**Abziehbare Ausformung** erstellt einen abziehbaren Volumenkörper in dem aktiven Körper indem ein Übergang zwischen zwei oder mehreren Skizzen (auch als Querschnitte bezeichnet) erzeugt wird. Seine geometrische Form wird dann von der bestehenden Form abgezogen.



## Anwendung



### Dialog-basierter Arbeitsablauf 

1.  Die Schaltfläche (subtraktive) **[<img src=images/PartDesign_SubtractiveLoft.svg style="width:24px"> [Ausformung](PartDesign_SubtractiveLoft/de.md)** drücken.
2.  Im Dialogfeld **Element auswählen** eine Skizze auswählen, die als Basisprofilobjekt verwendet werden soll, und auf **OK** klicken.
    -   Alternativ kann entweder eine einzelne Skizze oder die Fläche eines 3D-Objekts ({{Version/de|0.20}}) ausgewählt werden, bevor die Schaltfläche Ausformung gedrückt wird.
3.  In den **Ausformungsparametern** die Schaltfläche **Schnitt hinzufügen**.
4.  Die nächste Skizze in der [3D-Ansicht](3D_view/de.md) auswählen. Diesen Vorgang wiederholen, um weitere Skizzen in der Reihenfolge auszuwählen, in der sie eingefügt werden sollen. (Die Schnittreihenfolge kann irgendwann später im Dialogfeld der Ausformung geändert werden, indem die Schnitte in der Liste an die gewünschte Position gezogen werden.
5.  Wenn nötig Optionen festlegen und auf **OK** klicken.



### Auswahlbasierter Arbeitsablauf 

1.  Mehrere Skizzen auswählen. Dabei ist die Reihenfolge wichtig, in der sie ausgewählt werden:
    -   Die zuerst ausgewählte Skizze wird im nächsten Schritt das Basisprofil (-Objekt).
    -   Mit den danach ausgewählten Skizzen werden die Ausformungsabschnitte (loft sections) erstellt. Auch hier ist die Auswahlreihenfolge wichtig: Der erste Ausformungsabschnitt endet an der zweiten Skizze, der zweite Abschnitt an der dritten Skizze und so weiter. (Die Reihenfolge der Querschnitte kann später im Dialog Ausformung geändert werden, indem die Querschnitte in der Liste an die gewünschten Positionen gezogen werden.)
    -   Die erste oder die letzte Auswahl kann auch eine Fläche eines 3D-Objekts sein. ({{Version/de|0.20}})
2.  Die Schaltflache (abzuziehende) **[<img src=images/PartDesign_SubtractiveLoft.svg style="width:24px"> [Ausformung](PartDesign_SubtractiveLoft/de.md)** drücken.
3.  Bei Bedarf Optionen anpassen und **OK** klicken.



## Optionen

-   **Regelfläche**: erstellt gerade Übergänge zwischen Querschnitten. Wird nicht auf eine Ausformung mit zwei Querschnitten angewendet. Wenn nicht angekreuzt, werden die Übergänge glatt sein.
-   **Geschlossen**: erstellt einen Übergang vom letzten zum ersten Querschnitt, wodurch ein Ring entsteht. {{Version/de|0.21}}



## Eigenschaften

-    **Label**: Eine Benennung für die Operation, kann bei Bedarf geändert werden.

-    **Sections**(Schnitte): listet die verwendeten Querschnitte auf.

-    **Ruled**(Regelfläche): siehe [Optionen](#Optionen.md).

-    **Closed**(Geschlossen): siehe [Optionen](#Optionen.md).

-    **Midplane**: nicht verwendet.

-    **Reversed**: nicht verwendet.

-    **Refine**(Aufbereiten): \"true\" oder \"false\". Wenn auf \"true\" gesetzt, wird der Festkörper von Restkanten bereinigt, die durch Formelemente hinterlassen wurden. Siehe [Part FormAufbereiten](Part_RefineShape/de.md) für weitere Einzelheiten.



## Hinweise

-   Um die Form der Ausformung besser steuern zu können, wird empfohlen, dass alle Querschnitte mit derselben Anzahl von Abschnitten erstellt werden. Beispielsweise sollte für eine Ausformung zwischen einem Rechteck und einem Kreis der Kreis in vier verbundene Bögen aufgebrochen werden.
-   Die Ausformung kann in einem Knotenpunkt ([Vertex](Glossary/de#Vertex.md)) einer Skizze oder eines Körpers beginnen oder enden. {{Version/de|0.20}}
-   [Knotenpunkte](Glossary/de#Vertices.md) können in den meisten Fällen nur (entweder) der Anfang oder das Ende der Ausformung sein.
-   Ein Querschnitt kann nicht mit dem unmittelbar vorhergehenden Querschnitt auf derselben Ebene liegen.
-   Hat eine Skizze innere Geometrien, d.h. die Ausformung soll Löcher enthalten, dann sollte die Reihenfolge, in der die Skizzengeometrie erstellt wird, für alle Querschnitte dieselbe sein: Entweder startet man alle Querschnitte mit den inneren Geometrien oder mit den äußeren. Andernfalls kann eine ungültige Ausformung entstehen, bei der sich innere und äußere Wände überschneiden.
-   Es ist nicht möglich aufgetrennte oder sich kreuzende Schlaufen auszuformen.



## Verweise

-   [Part Ausformung Technische Details](Part_Loft_Technical_Details/de.md) erläutert wie eine [Part Ausformung](Part_Loft/de.md) erstellt wird. Der größte Teil des Inhalts ist auch für den PartDesign Subtraktive Ausformung relevant.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveLoft/de
