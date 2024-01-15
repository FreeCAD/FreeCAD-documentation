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



## Anwendung

1.  Den Befeh <img alt="" src=images/SheetMetal_BaseShape.svg  style="width:16px;"> **SheetMetal BaseShape** aktivieren durch:
    -   Die Schaltfläche **<img src="images/SheetMetal_BaseShape.svg" width=16px> [Add base shape](SheetMetal_BaseShape/de.md)**.
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_BaseShape.svg" width=16px> Add base shape**.
    -   Das Tastaturkürzel **H**.

2.  Der Aufgaben-Bereich **Unfold sheet metal object** wird geöffnet.

3.  Die gewünschte Form aus den Optionen von **Base shape type** auswählen.

4.  Die Parameter anpassen.

5.  
    **OK**drücken, um den Befehl abzuschließen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-BaseShape-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|fill Gaps|Bool}}: Erweitert die Seite und die Kanten (Flansche), um alle Lücken zu schließen. Standardwert: `True`.

-    {{PropertyData/de|flangeWidth|Length}}: Breite der oberen Kante (Flansch). Standardwert: {{Value|5,00 mm}}.

-    {{PropertyData/de|height|Length}}: Höhe der Form. Standardwert: {{Value|10,00 mm}}.

-    {{PropertyData/de|length|Length}}: Länge der Form. Standardwert: {{Value|30,00 mm}}.

-    {{PropertyData/de|radius|Length}}: Biegeradius. Standardwert: {{Value|1,00 mm}}.

-    {{PropertyData/de|shape Type|Enumeration}}: Art der Grundform. {{Value|L-Shape}} (standard), {{Value|U-Shape}}, {{Value|Tub}}, {{Value|Hat}}, {{Value|Box}}.

-    {{PropertyData/de|thickness|Length}}: Blechstärke. Standardwert: {{Value|1,00 mm}}.

-    {{PropertyData/de|width|Length}}: Breite der Form. Standardwert: {{Value|20,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal BaseShape/de
