---
- GuiCommand:/de
   Name:PartDesign SubtractiveLoft
   Name/de:PartDesign Subtraktive Ausformung
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   MenuLocation:Part Design → Subtraktive Ausformung
   Version:0.17
   SeeAlso:[Additive Ausformung](PartDesign_AdditiveLoft/de.md), [Abziehbares Rohr](PartDesign_SubtractivePipe/de.md)
---

# PartDesign SubtractiveLoft/de


</div>

## Beschreibung

**Abziehbare Ausformung** erstellt einen abziehbaren Volumenkörper in dem aktiven Körper indem ein Übergang zwischen zwei oder mehreren Skizzen (auch als Querschnitte bezeichnet) erzeugt wird. Seine geometrische Form wird dann von der bestehenden Form abgezogen.

## Anwendung

### Dialog-basierter Arbeitsablauf 


<div class="mw-translate-fuzzy">

1.  Drücke die **[<img src=images/PartDesign_SubtractiveLoft.svg style="width:24px"> [Subtractive loft](PartDesign_SubtractiveLoft.md)** Schaltfläche.
2.  Wähle im Dialog **Formelement auswählen** eine Skizze, die als Basisprofilobjekt verwendet werden soll, und klicke auf **OK**.
    -   Alternativ kann eine einzelne Skizze ausgewählt werden, bevor die Schaltfläche Subtraktive Ausformung gedrückt wird.
3.  Drücke in den **Ausformungsparametern** die Schaltfläche **Abschnitt hinzufügen**.
4.  Wähle die nächste Skizze in der [3D Ansicht](3D_view/de.md). Wiederhole diesen Vorgang, um weitere Skizzen in der Reihenfolge auszuwählen, in der sie ausgeformt werden sollen. (Du kannst die Abschnittsreihenfolge jederzeit später im Ausformungsdialog ändern, indem du Abschnitte in der Liste an die gewünschte Position ziehst.<small>(v0.19)</small> )
5.  Stelle bei Bedarf Optionen ein und klicke auf **OK**.


</div>

### Auswahlbasierter Arbeitsablauf 


<small>(v0.19)</small> 

1.  Select several sketches. It is hereby important in what order you select them:
    -   The sketch selected at first will become the base profile object in the next step
    -   The sketches selected after the first one will become the loft sections. Also here the selection order is important: The sketch selected as second will become the first loft section, the one selected as third becomes the second section and so on. (You can change the section order any time later in the loft dialog by dragging sections in the list to the desired position.<small>(v0.19)</small> )
    -   The first or last selection can also be a face of a 3D object (<small>(v0.20)</small> )
2.  Press the **[<img src=images/PartDesign_SubtractiveLoft.svg style="width:24px"> [Subtractive loft](PartDesign_SubtractiveLoft.md)** button.
3.  Set options if needed and click **OK**.

## Optionen


<div class="mw-translate-fuzzy">

-   **Geregelte Oberfläche**: generiert gerade Übergänge zwischen den Querschnitten. Gilt nicht für eine Ausformung mit zwei Querschnitten. Wenn nicht angehakt, werden die Übergänge glatt sein.
-   **Geschlossen** macht einen Übergang vom letzten Querschnitt zum ersten, wodurch ein Umlauf entsteht.


</div>

## Eigenschaften

-    **Kennzeichnung**: Ein Name für die Operation, kann bei Bedarf geändert werden.

-    **Schnitte**: listet die verwendeten Abschnitte auf.

-    **Geregelt**: siehe [Optionen](#Options.md).

-    **Geschlossen**: siehe [Optionen](#Options.md).

-    **Mittelebene**: N/A

-    **Umgekehrt**: N/A

-    **Verfeinern**: \"true\" oder \"false\". Wenn auf \"true\" gesetzt, wird der Festkörper von Restkanten gereinigt, die durch Formelemente hinterlassen wurden. Siehe [Part FormVerfeinern](Part_RefineShape/de.md) für weitere Einzelheiten.

## Notes


<div class="mw-translate-fuzzy">

-   Skizzen müssen geschlossene Konturen bilden.
-   Es ist nicht möglich, an einen Knoten auszuformen.
-   Ein Querschnitt kann nicht auf der gleichen Ebene liegen wie die unmittelbar vorausgehende.
-   Um die Form des Ausformung besser kontrollieren zu können, wird empfohlen, dass alle Querschnitte die gleiche Anzahl von Segmenten haben. Zum Beispiel kann bei einer Ausformung zwischen einem Rechteck und einem Kreis der Kreis in 4 zusammenhängende Bögen zerlegt werden.


</div>

## Verweise

-   [Part Ausformung Technische Details](Part_Loft_Technical_Details/de.md) erläutert wie eine [Part Ausformung](Part_Loft/de.md) erstellt wird. Der größte Teil des Inhalts ist auch für den PartDesign Subtraktive Ausformung relevant.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveLoft/de
