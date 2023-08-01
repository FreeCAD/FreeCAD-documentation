---
- GuiCommand:
   Name: Std MeasureDistance
   Name/de: Std AbstandMessen
   MenuLocation: Werkzeuge - Abstand messen
   Workbenches: Alle
   SeeAlso: [Part LinearMessen](Part_Measure_Linear/de.md), [Draft Maß](Draft_Dimension/de.md)
---

# Std MeasureDistance/de

## Beschreibung

Das Werkzeug **Std AbstendMessen** erstellt ein Distance-Objekt, das den Abstand zwischen zwei Punkten misst und anzeigt.

## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Std_MeasureDistance.svg" width=16px> [Std Abstand messen](Std_MeasureDistance/de.md)** drücken.
    -   Den Menüeintrag **Werkzeuge → <img src="images/Std_MeasureDistance.svg" width=16px> Abstand messen** auswählen.
2.  Den ersten Messpunkt irgendwo auf einem Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
3.  Den zweiten Messpunkt irgendwo auf einem Objekt in der3D-Ansicht auswählen.
4.  Die Auswahlreihenfolge der Punkte kann die Lage der Maßlinie beeinflussen.
5.  Wahlweise kann die Lage der Maßlinie umgekehrt werden, indem die {{PropertyView/de|Mirror}} des Distance-Objekts geändert wird.

## Hinweise

-   Das Fangwerkzeug des Arbeitsbereichs [Draft](Draft_Workbench/de.md) kann nicht mit diesem Werkzeug zusammen verwendet werden.
-   Um einer Zeichnung Maße hinzuzufügen, werden die Bemaßungswerkzeuge des Arbeitsbereichs [TechDraw](TechDraw_Workbench/de.md) verwendet.
-   Für umfangreichere Messwerkzeuge kann der [externe Arbeitsbereich](External_workbenches/de.md) <img alt="" src=images/Manipulator_workbench_icon.svg  style="width:24px;"> [Manipulatorverwendet](Manipulator_Workbench/de.md) werden.

## Eigenschaften

### Daten


{{TitleProperty|Basis}}

-    {{PropertyData/de|Label}}: Standardmäßig enthält das Label den gemessenen Abstand, aber dieser Abstand wird nicht aktualisiert, wenn P1 oder P2 später geändert wird.


{{TitleProperty|Measurement}}

-    {{PropertyData/de|P1}}: Der erste Punkt der Messung.

-    {{PropertyData/de|P2}}: Der zweite Punkt der Messung.

-    {{PropertyData/de|Distance}}: Der gemessene Abstand zwischen P1 und P2 (schreibgeschützt) .

### Ansicht


{{TitleProperty|Basis}}

-    {{PropertyView/de|Dist Factor}}: Dieser Faktor, mit dem gemessenen Abstand multipliziert, bestimmt den Abstand der Maßlinie.

-    {{PropertyView/de|Font Size}}: Die Schrifthöhe (Zeilenabstand in Pixeln).

-    {{PropertyView/de|Mirror}}: Wenn auf `True` gesetzt, wird die Lage der Maßlinie relativ zu P1 and P2 umgedreht.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std MeasureDistance/de
