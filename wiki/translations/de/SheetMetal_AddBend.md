---
 GuiCommand:
   Name: SheetMetal AddBend
   Name/de: SheetMetal BiegungHinzufügen
   MenuLocation: SheetMetal , Make Bend
   Workbenches: SheetMetal_Workbench/de
   Shortcut: **S** **B**
   SeeAlso: SheetMetal_AddRelief/de, SheetMetal_AddJunction/de
---

# SheetMetal AddBend/de



## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddBend.svg  style="width:24px;"> [Biegung hinzufügen](SheetMetal_AddBend/de.md) tauscht scharfe Kanten zwischen zwei Abschnitten (Grundplatte/Kanten/Falze) eines SheetMetal-Objekts gegen runde Biegungen aus. Ohne diese Bögen wären das Objekt nicht abwickelbar.

Dieser Befehl ist der dritte von drei Schritten, um ein Schalenobjekt, das mit dem Arbeitsbereich [Part](Part_Workbench/de.md) oder [PartDesign](PartDesign_Workbench/de.md) erzeugt wurde, in ein abwickelbares SheetMetal-Objekt umzuwandeln:

1.  [SheetMetal Entlastungsausschnitt hizufügen](SheetMetal_AddRelief/de.md)
2.  [SheetMetal Stoß hinzufügen](SheetMetal_AddJunction/de.md)
3.  [SheetMetal Biegung hinzufügen](SheetMetal_AddBend/de.md)

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:200px;"> 
*Biegung hinzufügen - Scharfe Kanten durch Bögen ersetzen*



## Anwendung

1.  Eine oder mehrere Kanten auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/SheetMetal_AddBend.svg" width=16px> [Bogen einfügen](SheetMetal_AddBend/de.md)** drücken.
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_AddBend.svg" width=16px> Bogen einfügen** auswählen.
    -   Ein Rechtsklick in die [Baumansicht](Tree_view/de.md) oder die [3D-Ansicht](3D_view/de.md) und die Menüoption **SheetMetal → <img src="images/SheetMetal_AddBend.svg" width=16px> Bogen einfügen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **S** dann **B**.
3.  Das [Aufgaben-Fenster](Task_panel/de.md) **Bend sharp corners Parameters** wird geöffnet (eingeführt in Version 0.5.00).
4.  Wahlweise die Schaltfläche **Auswahl** drücken, um weitere Kanten auszuwählen.
    -   Die Schaltfläche **Vorschau** drücken, um die Auswahl abzuschließen und die Änderungen anzuzeigen.
5.  Wahlweise die Parameter im Aufgaben-Fenster anpassen.
6.  Die Schaltfläche **OK** rücken, um den Befehl abzuschließen und das Aufgaben-Fenster zu schließen.
7.  Ein **SolidBend**-Objekt wird erstellt und enthält einen neuen Bogen an jeder ausgewählten Kante.
8.  Wahlweise die Parameter im [Eigenschafteneditor](Property_editor/de.md) anpassen.

<img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-08.png  style="width:200px;">



## Hinweise

Die Befehle <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[Stoß hinzufügen](SheetMetal_AddJunction/de.md)** und <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[Biegung hinzufügen](SheetMetal_AddBend/de.md)** funktionieren am besten mit hohlen Quadern, d.h. Schalenobjekten mit einer konstanten Wandstärke und nur 90° Winkeln zwischen den Flächen.

Siehe [SheetMetal Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de#Hinweise.md) für Hinweise zur Erstellung von Schalenobjekten aus Quadern.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-SolidBend-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet oder, wenn es sich in einem [PartDesign-Körper](PartDesign_Body/de.md) befindet, von einem [PartDesign Formelement](PartDesign_Feature/de.md) und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|base Object|LinkSub}}: \"Base object\". Verknüpfungen zu den Kanten, die gebogen werden sollen.

-    {{PropertyData/de|radius|Length}}: \"Bend Radius\". Standardwert: {{value|1,00 mm}}.

-    {{PropertyData/de|thickness|Length}}: \"Thickness of sheetmetal\". Standardwert: {{value|1,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddBend/de
