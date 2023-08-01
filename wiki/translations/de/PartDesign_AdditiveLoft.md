---
- GuiCommand:
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

1.  Die Schaltfläche (additive) **[<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Ausformung](PartDesign_AdditiveLoft/de.md)** drücken.
2.  Im Dialogfeld **Element auswählen** eine Skizze auswählen, die als Basisprofilobjekt verwendet werden soll, und auf **OK** klicken.
    -   Alternativ kann entweder eine einzelne Skizze oder die Fläche eines 3D-Objekts ({{Version/de|0.20}}) ausgewählt werden, bevor auf die Schaltfläche Ausformung geklickt wird.
3.  Unter **Ausformungsparameter** die Schaltfläche **Schnitt hinzufügen** drücken.
4.  Die nächste Skizze in der [3D-Ansicht](3D_view/de.md) auswählen. Diesen Vorgang wiederholen, um weitere Skizzen in der Reihenfolge auszuwählen, in der sie eingefügt werden sollen. (Die Schnittreihenfolge kann irgendwann später im Dialogfeld der Ausformung geändert werden, indem die Schnitte in der Liste an die gewünschte Position gezogen werden.)
5.  Wenn nötig Optionen festlegen und auf **OK** klicken.



### Auswahlbasierter Arbeitsablauf 

1.  Mehrere Skizzen auswählen. Dabei ist es wichtig, in welcher Reihenfolge sie ausgewählt werden:
    -   Die zuerst ausgewählte Skizze wird im nächsten Schritt zum Basis-Profilobjekt.
    -   Die nach der ersten ausgewählten Skizzen werden zu den Ausformungs(quer)schnitten. Auch hier ist die Reihenfolge der Auswahl wichtig: Die als zweite ausgewählte Skizze wird zum ersten Ausformungsschnitt, die als dritte ausgewählte zum zweiten Schnitt und so weiter. (Die Schnittreihenfolge kann irgendwann später im Dialogfeld der Ausformung geändert werden, indem die Schnitte in der Liste an die gewünschte Position gezogen werden.)
    -   Der erste oder der letzte Schnitt kann auch eine Fläche eines 3D-Objekts sein. ({{Version/de|0.20}})
2.  Die Schaltfläche **[<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Ausformung](PartDesign_AdditiveLoft/de.md)** drücken.
3.  Wenn nötig Optionen festlegen und auf die Schaltfläche **OK** klicken.



## Optionen

-   **Regelfläche**: erstellt gerade Übergänge zwischen Querschnitten. Wird nicht auf eine Ausformung mit zwei Querschnitten angewendet. Wenn nicht angekreuzt, werden die Übergänge glatt sein.
-   **Geschlossen**: erstellt einen Übergang vom letzten zum ersten Querschnitt, wodurch ein Ring entsteht. {{Version/de|0.21}}



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



## Hinweise

-   Um die Form der Ausformung besser kontrollieren zu können, wird empfohlen, dass alle Querschnitte die gleiche Anzahl von Segmenten haben. Zum Beispiel kann für eine Ausformung zwischen einem Rechteck und einem Kreis der Kreis in 4 zusammenhängende Bögen aufgeteilt werden.
-   Die Ausformung kann mit einem einzelnen Knotenpunkt ([vertex](Glossary#V.md)) einer Skizze oder eines Körpers beginnen oder enden. {{Version/de|0.20}}
-   Ein Knotenpunkt kann nur entweder Start- oder Endpunkt einer Ausformung sein. Andernfalls würde der Ausformungskörper aus zwei an der spitze verbundenen Festkörpern bestehen. Dies würde gegen die Definition eines 3D-Objekts des CAD-Kernels verstoßen.
-   Ein Querschnitt kann nicht auf derselben Ebene liegen wie der unmittelbar vorhergehende.
-   Wenn die Skizze eine innere Geometrie hat, d. h. die Ausformung soll Löcher haben, dann sollte die Reihenfolge, in der die Skizzengeometrie erstellt wird, für alle Schnitte gleich sein: Entweder beginnen alle Schnitte mit der inneren Geometrie oder sie beginnen alle mit der äußeren. Andernfalls kann ein ungültiger Ausformung erzeugt werden, bei dem sich Innen- und Außenwände kreuzen.
-   Es ist nicht möglich, unzusammenhängende oder sich kreuzende Konturen zu verwenden.
-   Einige Fehler-Modi färben das Bauteil schwarz.



## Verweise

-   [Part Ausformung Technische Details](Part_Loft_Technical_Details/de.md) erläutert wie eine [Part Ausformung](Part_Loft/de.md) erstellt wird; der größte Teil des Inhalts gilt auch für die (additive) PartDesign Ausformung.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveLoft/de
