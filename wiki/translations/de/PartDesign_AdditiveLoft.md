---
- GuiCommand:/de
   Name:PartDesign AdditiveLoft
   Name/de:PartDesign AusformungHinzufügen
   MenuLocation:Part Design → Objekte hinzufügen → Ausformung
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[PartDesign RohrHinzufügen](PartDesign_AdditivePipe/de.md), [PartDesign AusformungAbziehen](PartDesign_SubtractiveLoft/de.md)
---

# PartDesign AdditiveLoft/de

## Beschreibung

**Additive Ausformung** erzeugt einen Festkörper im aktiven Körper, indem er einen Übergang zwischen zwei oder mehreren Skizzen (auch Querschnitte genannt) herstellt. Wenn der Körper bereits Elemente enthält, wird die additive Ausformung mit diesen zusammengeführt.

![](images/PartDesign_AddLoft_example.png ) 
*Links: Querschnitte (A), (B) und (C). Rechts: Die erstellte Ausformung*

## Anwendung

### Dialogbasierter Arbeitsablauf 


<div class="mw-translate-fuzzy">

1.  Drücke die **[<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Additive Ausformung](PartDesign_AdditiveLoft/de.md)** Schaltfläche
2.  Wähle im **Funktion auswählen** Dialogfeld eine Skizze, die als Basisprofilobjekt verwendet werden soll, und klicke auf **OK**.
    -   Alternativ kann eine einzelne Skizze ausgewählt werden, bevor auf die Schaltfläche Additive Ausformung geklickt wird.
3.  Drücke in den **Ausformungsparametern** die **Abschnitt hinzufügen** Schaltfläche.
4.  Wähle die nächste Skizze in der [3D Ansicht](3D_view/de.md). Wiederhole diesen Vorgang, um weitere Skizzen in der Reihenfolge auszuwählen, in der sie eingefügt werden sollen. (Du kannst die Schnittreihenfolge jederzeit später im Ausformungs Dialogfeld ändern, indem du die Schnitte in der Liste an die gewünschte Position ziehst. {{Version/de|0.19}})
5.  Lege Optionen wenn notwendig fest und klicke auf **OK**.


</div>

### Auswahlbasierter Arbeitsablauf 


<div class="mw-translate-fuzzy">


<small>(v0.19)</small> 

1.  Wähle mehrere Skizzen aus. Dabei ist es wichtig, in welcher Reihenfolge du sie auswählst:
    -   Die zuerst ausgewählte Skizze wird im nächsten Schritt zum Basis Profilobjekt.
    -   Die nach der ersten ausgewählten Skizzen werden zu den Ausformungsabschnitten. Auch hier ist die Reihenfolge der Auswahl wichtig: Die als zweite ausgewählte Skizze wird zum ersten Ausformungsabschnitt, die als dritte ausgewählte zum zweiten Abschnitt und so weiter. (Du kannst die Reihenfolge der Abschnitte jederzeit später im Ausformungsdialog ändern, indem du die Abschnitte in der Liste an die gewünschte Position ziehst.<small>(v0.19)</small> )
2.  Drücke die **[<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Additive loft](PartDesign_AdditiveLoft.md)** Schaltfläche.
3.  Lege Optionen wenn notwendig fest und klicke auf die **OK** Schaltfläche.


</div>

## Optionen

-   **Regelfläche**: erstellt gerade Übergänge zwischen Querschnitten. Wird nicht auf eine Ausformung mit zwei Querschnitten angewendet. Wenn nicht angekreuzt, werden die Übergänge glatt sein.
-   **Geschlossen**: macht einen Übergang vom letzten zum ersten Querschnitt, wodurch ein Ring entsteht.

## Eigenschaften

-    {{PropertyData/de|Label}}: Bezeichnung, die der Operation gegeben wurde, diese Benennung kann nach Belieben geändert werden.

-    {{PropertyData/de|Sections}}: Listet die verwendeten Profilschnitte auf.

-    {{PropertyData/de|Ruled}}: siehe [Optionen](#Optionen.md).

-    {{PropertyData/de|Geschlossen}}: siehe [Optionen](#Optionen.md).

-    {{PropertyData/de|Refine}}: true oder false. Wenn auf true gesetzt, befreit den Festkörper von übriggebliebenen Kanten, die von den Formelementen hinterlassen wurden. Siehe [Part FormAufbereiten](Part_RefineShape/de.md) für weitere Einzelheiten.

-    **Profile**: das Basis-Profilobjekt der Ausformung.

-    {{PropertyData/de|Midplane}}: nicht anwendbar.

-    {{PropertyData/de|Reversed}}: nicht anwendbar.

-    **Up To Face**: nicht anwendbar.

-    **Allow Multi Face**: nicht anwendbar.

## Notes


<div class="mw-translate-fuzzy">

-   Skizzen müssen geschlossene Profile bilden.
-   Es ist nicht möglich, einen Knoten auszuformen.
-   Ein Querschnitt kann nicht auf der gleichen Ebene liegen wie die unmittelbar vorhergehende Ebene.
-   Um die Form der Ausformung besser kontrollieren zu können, wird empfohlen, dass alle Querschnitte die gleiche Anzahl von Segmenten haben. Zum Beispiel kann eine Ausformung zwischen einem Rechteck und einem Kreis in 4 zusammenhängende Bögen zerlegt werden.
-   Die Ausformung wird in der Reihenfolge erzeugt, in der die Querschnitte hinzugefügt wurden.
-   Wenn die Skizze eine innere Geometrie hat, d. h. die Ausformung soll Löcher haben, dann sollte die Reihenfolge, in der die Skizzengeometrie erstellt wird, für alle Schnitte gleich sein: Entweder beginnen alle Schnitte mit der inneren Geometrie oder sie beginnen alle mit der äußeren. Andernfalls kann ein ungültiger Ausformung erzeugt werden, bei dem sich Innen- und Außenwände kreuzen.


</div>

## Verweise


<div class="mw-translate-fuzzy">

-   [Part Ausformung Technische Details](Part_Loft_Technical_Details/de.md) erläutert wie ein [\|Part Ausformung](Part_Loft/de.md) erstellt wird. Der größte Teil des Inhalts ist auch für den PartDesign Additive Ausformung relevant.


</div>





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveLoft/de
