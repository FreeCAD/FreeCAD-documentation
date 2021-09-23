---
- GuiCommand:/de
   Name:PartDesign AdditiveLoft
   Name/de:PartDesign AdditiveAusformung
   MenuLocation:Part Design → Additive Ausformung
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign AdditivesRohr](PartDesign_AdditivePipe/de.md), [PartDesign SubtraktiveAusformung](PartDesign_SubtractiveLoft/de.md)
---


</div>

## Beschreibung

**Additive Ausformung** erzeugt einen Festkörper im aktiven Körper, indem er einen Übergang zwischen zwei oder mehreren Skizzen (auch Querschnitte genannt) herstellt. Wenn der Körper bereits Elemente enthält, wird die additive Ausformung mit diesen zusammengeführt.

![](images/PartDesign_AddLoft_example.png )


<div class="mw-translate-fuzzy">

*Zur Linken: Querschnitte (A), (B) und (C); erstellte Additive Ausformung rechts.*


</div>

## Anwendung

### Dialogbasierter Arbeitsablauf 

1.  Drücke die **<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Additive Ausformung](PartDesign_AdditiveLoft/de.md)** Schaltfläche
2.  Wähle im **Funktion auswählen** Dialogfeld eine Skizze, die als Basisprofilobjekt verwendet werden soll, und klicke auf {{Schaltfläche|OK}}.
    -   Alternativ kann eine einzelne Skizze ausgewählt werden, bevor auf die Schaltfläche Additive Ausformung geklickt wird.
3.  Drücke in den **Ausformungsparametern** die **Abschnitt hinzufügen** Schaltfläche.
4.  Wähle die nächste Skizze in der [3D Ansicht](3D_view/de.md). Wiederhole diesen Vorgang, um weitere Skizzen in der Reihenfolge auszuwählen, in der sie eingefügt werden sollen. (Du kannst die Schnittreihenfolge jederzeit später im Ausformungs Dialogfeld ändern, indem du die Schnitte in der Liste an die gewünschte Position ziehst.<small>(v0.19)</small> )
5.  Lege Optionen wenn notwendig fest und klicke auf **OK**.

### Auswahlbasierter Arbeitsablauf 


<small>(v0.19)</small> 

1.  Wähle mehrere Skizzen aus. Dabei ist es wichtig, in welcher Reihenfolge du sie auswählst:
    -   Die zuerst ausgewählte Skizze wird im nächsten Schritt zum Basis Profilobjekt.
    -   Die nach der ersten ausgewählten Skizzen werden zu den Ausformungsabschnitten. Auch hier ist die Reihenfolge der Auswahl wichtig: Die als zweite ausgewählte Skizze wird zum ersten Ausformungsabschnitt, die als dritte ausgewählte zum zweiten Abschnitt und so weiter. (Du kannst die Reihenfolge der Abschnitte jederzeit später im Ausformungsdialog ändern, indem du die Abschnitte in der Liste an die gewünschte Position ziehst.<small>(v0.19)</small> )
2.  Drücke die **<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Additive loft](PartDesign_AdditiveLoft.md)** Schaltfläche.
3.  Lege Optionen wenn notwendig fest und klicke auf die **OK** Schaltfläche.

## Optionen


<div class="mw-translate-fuzzy">

-   **Geregelte Oberfläche**: macht gerade Übergänge zwischen Querschnitten. Gilt nicht für eine Ausformung mit zwei Querschnitten. Wenn nicht angekreuzt, werden die Übergänge glatt sein.
-   **Geschlossen**: macht einen Übergang vom letzten zum ersten Querschnitt, wodurch eine Schleife entsteht.


</div>

## Eigenschaften


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Label}}: Name, der der Operation gegeben wurde, dieser Name kann nach Belieben geändert werden.

-    {{PropertyData/de|Sections}}: listet die verwendeten Abschnitte auf.

-    {{PropertyData/de|Ruled}}: siehe [Optionen](#Options.md).

-    {{PropertyData/de|Geschlossen}}: siehe [Optionen](#Options.md).

-    {{PropertyData/de|Refine}}: true oder false. Wenn auf true gesetzt, reinigt den Festkörper von den Restkanten, die von den Funktionen hinterlassen wurden. Siehe [Part FormVerfeinern](Part_RefineShape/de.md) für weitere Einzelheiten.

-    **Profile**: das siehe Basisprofil Objekt der Ausformung.

-    {{PropertyData/de|Midplane}}: nicht anwendbar.

-    {{PropertyData/de|Reversed}}: nicht anwendbar.

-    **Up To Face**: nicht anwendbar.

-    **Allow Multi Face**: nicht anwendbar.


</div>

## Begrenzungen

-   Skizzen müssen geschlossene Profile bilden.
-   Es ist nicht möglich, einen Knoten auszuformen.
-   Ein Querschnitt kann nicht auf der gleichen Ebene liegen wie die unmittelbar vorhergehende Ebene.
-   Um die Form der Ausformung besser kontrollieren zu können, wird empfohlen, dass alle Querschnitte die gleiche Anzahl von Segmenten haben. Zum Beispiel kann eine Ausformung zwischen einem Rechteck und einem Kreis in 4 zusammenhängende Bögen zerlegt werden.
-   Die Ausformung wird in der Reihenfolge erzeugt, in der die Querschnitte hinzugefügt wurden.
-   Wenn die Skizze eine innere Geometrie hat, d. h. die Ausformung soll Löcher haben, dann sollte die Reihenfolge, in der die Skizzengeometrie erstellt wird, für alle Schnitte gleich sein: Entweder beginnen alle Schnitte mit der inneren Geometrie oder sie beginnen alle mit der äußeren. Andernfalls kann ein ungültiger Ausformung erzeugt werden, bei dem sich Innen- und Außenwände kreuzen.

## Known Issues 


<div class="mw-translate-fuzzy">

## Bekannte Probleme 

-   Einige Fehlersituationen lassen das Teil schwarz werden


</div>

## Verweise


<div class="mw-translate-fuzzy">

-   [Part Ausformung Technische Details](Part_Loft_Technical_Details/de.md) erläutert wie ein [\|Part Ausformung](Part_Loft/de.md) erstellt wird. Der größte Teil des Inhalts ist auch für den PartDesign Additive Ausformung relevant.


</div>





{{PartDesign Tools navi

}} 
