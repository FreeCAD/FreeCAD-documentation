---
 GuiCommand:
   Name: SheetMetal BaseShape
   Name/de: SheetMetal Grundform
   MenuLocation: SheetMetal , Add base shape
   Workbenches: SheetMetal_Workbench/de
   Version: 0.3.10
   Shortcut: **H**
---

# SheetMetal BaseShape/de



## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_BaseShape.svg  style="width:24px;"> **SheetMetal Grundform** erzeugt ein SheetMetal-Basisobjekt (BaseShape-Objekt) aus Parametern.

<img alt="" src=images/SheetMetal_BaseShape-01.png  style="width:400px;">



*Die fünf möglichen Grundformen: L-Form, U-Form, Wanne, Hut, und Kasten*

Eine rechteckige sechste Form, Platine genannt (Flat), wurde eingeführt mit Version 0.4.10.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/SheetMetal_BaseShape.svg" width=16px> [Add base shape](SheetMetal_BaseShape/de.md)** drücken.
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_BaseShape.svg" width=16px> Add base shape** auswählen.
    -   Ein Rechtsklick in die [Baumansicht](Tree_view/de.md) oder die [3D-Ansicht](3D_view/de.md) und die Menüoption **SheetMetal → <img src="images/SheetMetal_BaseShape.svg" width=16px> Add base shape** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **H**.
2.  Das [Aufgaben-Fenster](Task_panel/de.md) **Blech-Grundform erstellen** wird geöffnet.
3.  Die gewünschte Form aus den Optionen von **Art der Grundform** auswählen.
4.  Die Position des Ursprungs im Widget **Lage des Bauteilursprungs** auswählen.
5.  Wahlweise die Parameter im Aufgaben-Fenster anpassen.
6.  Die Schaltfläche **OK** drücken, um den Befehl abzuschließen und das Aufgaben-Fenster zu schließen.
7.  Ein **BaseShape**-Objekt wird erstellt.
8.  Wahlweise die Parameter im [Eigenschafteneditor](Property_editor/de.md) anpassen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-BaseShape-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet oder, wenn es sich in einem [PartDesign-Körper](PartDesign_Body/de.md) befindet, von einem [PartDesign Formelement](PartDesign_Feature/de.md) und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|fill Gaps|Bool}}: Erweitert die Seite und die Kanten (Flansche), um alle Lücken zu schließen. Standardwert: `True`.

-    {{PropertyData/de|flangeWidth|Length}}: Breite der oberen Kante (Flansch). Standardwert: {{Value|5,00 mm}}.

-    {{PropertyData/de|height|Length}}: Höhe der Form. Standardwert: {{Value|10,00 mm}}.

-    {{PropertyData/de|length|Length}}: Länge der Form. Standardwert: {{Value|30,00 mm}}.

-    **origin Loc|Enumeration**: Lage des Ursprungs.

    :   
        {{Value|-X,-Y}}
        
        , {{Value|-X,0}}, {{Value|-X,+Y}}, {{Value|0,-Y}}, {{Value|0,0}} (default), {{Value|0,+Y}}, {{Value|+X,-Y}}, {{Value|+X,0}}, and {{Value|+X,+Y}}

-    {{PropertyData/de|radius|Length}}: Biegeradius. Standardwert: {{Value|1,00 mm}}.

-    {{PropertyData/de|shape Type|Enumeration}}: Art der Grundform.

    :   
        {{Value|Flat}}
        
        (eingeführt in Version 0.4.10), {{Value|L-Shape}} (standard), {{Value|U-Shape}}, {{Value|Tub}}, {{Value|Hat}}, {{Value|Box}}.

-    {{PropertyData/de|thickness|Length}}: Blechstärke. Standardwert: {{Value|1,00 mm}}.

-    {{PropertyData/de|width|Length}}: Breite der Form. Standardwert: {{Value|20,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal BaseShape/de
