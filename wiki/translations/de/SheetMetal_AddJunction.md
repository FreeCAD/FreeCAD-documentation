---
 GuiCommand:
   Name: SheetMetal AddJunction
   Name/de: SheetMetal StoßHinzufügen
   MenuLocation: SheetMetal , Make Junction
   Workbenches: SheetMetal_Workbench/de
   Shortcut: **S** **J**
   SeeAlso: SheetMetal_AddRelief/de, SheetMetal_AddBend/de
---

# SheetMetal AddJunction/de



## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:24px;"> [Stoß hinzufügen](SheetMetal_AddJunction/de.md) erzeugt einen offenen Stoß zwischen zwei Abschnitten (Kanten/Falze) eines SheetMetal-Objekts. Ohne diese Stöße wären (zusammenhängende) Abschnitte, die mit derselben Grundplatte verbunden sind, nicht abwickelbar.

Dieser Befehl ist der zweite von drei Schritten, um ein Schalenobjekt, das mit dem Arbeitsbereich [Part](Part_Workbench/de.md) oder [PartDesign](PartDesign_Workbench/de.md) erzeugt wurde, in ein abwickelbares SheetMetal-Objekt umzuwandeln:

1.  [SheetMetal Entlastungsausschnitt hizufügen](SheetMetal_AddRelief/de.md)
2.  [SheetMetal Stoß hinzufügen](SheetMetal_AddJunction/de.md)
3.  [SheetMetal Biegung hinzufügen](SheetMetal_AddBend/de.md)

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;"> 
*Stoß hinzufügen - Kanten aufschneiden*



## Anwendung

1.  Eine oder mehrere Kanten auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/_SheetMetal_AddJunction.svg_" width=16px> [Stoß hinzufügen](SheetMetal_AddJunction/de.md)** drücken.
    -   Den Menüeintrag **SheetMetal → <img src="images/_SheetMetal_AddJunction.svg_" width=16px> Stoß hinzufügen** auswählen.
    -   Ein Rechtsklick in die [Baumansicht](Tree_view/de.md) oder die [3D-Ansicht](3D_view/de.md) und die Menüoption **SheetMetal → <img src="images/_SheetMetal_AddJunction.svg_" width=16px> Stoß hinzufügen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **S** dann **J**.
3.  Das [Aufgaben-Fenster](Task_panel/de.md) **Add Junction Parameters** wird geöffnet (eingeführt in Version 0.5.00).
4.  Wahlweise die Schaltfläche **Auswahl** drücken, um weitere Kanten auszuwählen.
    -   Die Schaltfläche **Vorschau** drücken, um die Auswahl abzuschließen und die Änderungen anzuzeigen.
5.  Wahlweise die Parameter im Aufgaben-Fenster anpassen.
6.  Die Schaltfläche **OK** rücken, um den Befehl abzuschließen und das Aufgaben-Fenster zu schließen.
7.  Ein **Junction**-Objekt wird erstellt und ergibt einen Stoß an jeder ausgewählten Kante.
8.  Wahlweise die Parameter im [Eigenschafteneditor](Property_editor/de.md) anpassen.

<img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;">



## Hinweise

-   Die Befehle <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[Stoß hinzufügen](SheetMetal_AddJunction/de.md)** und <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[Biegung hinzufügen](SheetMetal_AddBend/de.md)** funktionieren am besten mit hohlen Quadern, d.h. Schalenobjekten mit einer konstanten Wandstärke und nur 90° Winkeln zwischen den Flächen.
-   Siehe [SheetMetal Entlastungsausschnitt hinzufügen](SheetMetal_AddRelief/de#Hinweise.md) für Hinweise zur Erstellung von Schalenobjekten aus Quadern.

-   **Stoß** (Junction) ist in diesem Falle nicht das Ergebnis dieses Werkzeuges, welches eine Lücke zischen aneinandergrenzenden ebenen Flächen ist, sondern beschreibt eher die Stelle, an der sich zwei ebene Flächen des fertigen realen Objekts treffen, um verschweißt zu werden, zum Beispiel.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-Junction-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet oder, wenn es sich in einem [PartDesign-Körper](PartDesign_Body/de.md) befindet, von einem [PartDesign Formelement](PartDesign_Feature/de.md) und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{Properties_Title/de|Parameters}}

-    **base Object|LinkSub**: \"Base Object\". Verweise zu den Kanten, die die Position der Stöße bzw. Lücken bestimmen.

-    **gap|Length**: \"Junction Gap\". Standardwert: {{value|2,00 mm}}. Spaltweite des hinzuzufügenden Stoßes.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal AddJunction/de
