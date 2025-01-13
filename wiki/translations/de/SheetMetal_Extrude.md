---
 GuiCommand:
   Name: SheetMetal Extrude
   Name/de: SheetMetal KanteVerlängern
   MenuLocation: SheetMetal , Extend Face
   Workbenches: SheetMetal_Workbench/de
   Shortcut: **E**
---

# SheetMetal Extrude/de



## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **Kante verlängern** erweitert eine Blechplatte an einer ausgewählten Kantenfläche.

Er erzeugt eine **einfache Verlängerung** in Richtung der Flächennormalen der ausgewählten Kantenfläche:

<img alt="" src=images/SheetMetal_Extrude-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-02.png  style="width:200px;">

Wenn eine Konturskizze hinzugefügt wird, erzeugt er **verzahnte Geometrie** um ein Profil zu schließen:

<img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Drei Profile mit hinzuzufügenden Konturskizzen → Drei Ergebnisse*



## Anwendung



### Einfache Verlängerung 

1.  Eine oder mehrere Flächen auswählen, die verlängert werden sollen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/SheetMetal_Extrude.svg" width=16px> [Kante verlängern](SheetMetal_Extrude/de.md)** drücken.
    -   Den Menüeintrag **Sheet Metal → <img src="images/SheetMetal_Extrude.svg" width=16px> Kante verlängern** auswählen.
    -   Ein Rechtsklick in die [Baumansicht](Tree_view/de.md) oder die [3D-Ansicht](3D_view/de.md) und die Menüoption **Sheet Metal → <img src="images/SheetMetal_Extrude.svg" width=16px> Kante verlängern** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **E**.
3.  Das [Aufgaben-Fenster](Task_panel/de.md) **Extend Parameters** wird geöffnet (eingeführt in Version 0.5.00).
4.  Wahlweise die Schaltfläche **Auswählen** drücken, um weiter Flächen hinzuzufügen.
    -   Die Schaltfläche **Vorschau** drücken, um die Auswahl abzuschließen und die Äderungen anzuzeigen.
5.  Wahlweise die Parameter im Aufgaben-Fenster anpassen.
6.  Die Schaltfläche **OK** drücken, um den Befehl abzuschließen und das Aufgaben-Fenster zu schließen.
7.  Ein **Extend**-Objekt wird erstellt, das eine neue Flächenverlängerung an jeder ausgewählten Kante enthält.
8.  Wahlweise die Eigenschaften im [Eigenschafteneditor](Property_editor/de.md) anpassen.



### Verzahnte Erweiterung 

:   (Eine <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Skizze](Sketcher_Workbench/de.md) für die Verzahnung vorbereiten)

1.  Die Kantenfläche auswählen, die erweitert werden soll.
2.  Den Befehl aktivieren, wie oben beschrieben.
3.  Die Schaltfläche **OK** drücken, um den Befehl abzuschließen und das Aufgaben-Fenster zu schließen.
4.  Im [Eigenschafteneditor](Property_editor/de.md) die Schaltfläche **...** der {{PropertyData/de|Sketch}} drücken.
5.  Das Dialogfenster \"Link\" wird geöffnet.
    -   Die vorbereitete Skizze in der Liste auswählen.
    -   Die Schaltfläche **OK** drücken, um das Dialogfenster zu schließen.
6.  Die {{PropertyData/de|Ausschneiden}} auf `True` setzen, um Ausschnitte zu erstellen, die Platz für die Erweiterungen schaffen.
7.  Den Wert der {{PropertyData/de|Offset}} verändern, um den Spalt um die Erweiterung herum einzustellen.

<img alt="" src=images/SheetMetal_Extrude-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Drei Profile → Position der Skizzen → Ergebnisse ohne Ausschnitte → Endergebnisse*



### Hinweise

-   Eine Skizze kann mehr als nur eine Kontur enthalten.

:   Nach dem Einfügen einer Skizze muss mindestens eine ihrer Konturen eine gegenüberliegende Fläche wenigstens berühren, andernfalls kann das Werkzeug weder eine Erweiterung noch einen Ausschnitt erzeugen.





:   Nur eine Kontur, die eine gegenüberliegende Fläche berührt, reicht um Erweiterungsgeometrie von allen Konturen einer Skizze zu erzeugen.

-   Jeder Ausschnitt hat die Gestalt eines Quaders, egal welche form die zugehörige Konturskizze hat.

-   Alle Formen außer Rechtecken können sich etwas merkwürdig verhalten und auch wenn das Objekt abgewickelt werden kann, wird das Ergebnis anders ausfallen als erwartet.

<img alt="" src=images/SheetMetal_Extrude-07.png  style="width:250px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-08.png  style="width:250px;">



*Drei Konturskizzen und ihre resultierenden Erweiterungen: einzelne Dreiecksplatte mit rechteckigem Ausschnitt, Kreis ohne Spalt → Abwicklungskörper wurde an unerwarteter Stelle aufgetrennt*

-   Für eine Erweiterung wird empfohlen, die {{PropertyData/de|Refine}} auf `True` (default) gesetzt zu lassen.

-   Die Operation KanteVerlängern mit einer verknüpften Skizze könnte aufgrund von Komplanar-Problemen versagen, wenn die Fläche auf der Skizzenseite und die Fläche auf der gegenüberliegenden Seite komplanar sind aber mit gegensätzlichen Ausrichtungen. Ein kleiner Versatz könnte in so einem Fall helfen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-Extend-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet oder, wenn es sich in einem [PartDesign-Körper](PartDesign_Body/de.md) befindet, von einem [PartDesign Formelement](PartDesign_Feature/de.md) und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|base Object|LinkSub}}: \"Base object\". Verweis zu der ebenen Fläche, die erweitert werden soll.

-    {{PropertyData/de|gap1|Distance}}: \"Gap from the left side\". Abstand von der linken Seite, Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|gap2|Distance}}: \"Gap from the right side\". Abstand von der rechten Seite, Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|length|Length}}: \"Length of Wall\". Kantenlänge, Standardwert: {{value|10,00 mm}}.


{{Properties_Title/de|Parameters Ext.}}

-    {{PropertyData/de|Offset|Distance}}: \"Offset for subtraction\". Abstand zur Aussparung, Standardwert: {{value|20,00 µm}}.

-    {{PropertyData/de|Refine|Bool}}: \"Use Refine\". Standardwert: `True`.

-    {{PropertyData/de|Sketch|Link}}: \"Wall Sketch\". Skizze für den zu erweiternden Bereich

-    {{PropertyData/de|Use Subtraction|Bool}}: \"Use Subtraction\". Aussparung anwenden, Standardwert: `False`



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Extrude/de
