---
- GuiCommand:/de
   Name:SheetMetal Extrude
   Name/de:SheetMetal KanteVerlängern
   MenuLocation:SheetMetal → Extend Face
   Workbenches:[SheetMetal (Blech)](SheetMetal_Workbench/de.md)
   Shortcut:**E**
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

1.  Eine oder mehrere Flächen auswählen, die verlängert werden soll.
2.  Den Befehl <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> **Kante verlängern** aktivieren durch
    -   Die Schaltfläche **<img src="images/SheetMetal_Extrude.svg" width=16px> [Kante verlängern](SheetMetal_Extrude/de.md)**.
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_Extrude.svg" width=16px> Kante verlängern**.
    -   Das Tastenkürzel: **E**.
3.  Den Wert der {{PropertyData/de|length}} verändern, um die Länge der Verlängerung einzustellen.

### Verzahnte Erweiterung 

1.  Eine Kantenfläche auswählen, die erweitert werden soll.
2.  Den Befehl <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> **Kante verlängern** aktivieren (siehe oben).
3.  Eine komplanare Konturskizze zur {{PropertyData/de|Sketch}} hinzufügen.
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_Extrude.svg" width=16px> Kante verlängern**.
4.  Den Wert der {{PropertyData/de|Offset}} verändern, um den Spalt um die Erweiterung herum einzustellen.

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

-   The extension operation with a linked sketch may fail due to coplanar issues if the face on the sketch side and the face on the opposite side are coplanar, but with opposite orientations. A small offset may help in such a case.

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-Extend-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


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
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Extrude/de
