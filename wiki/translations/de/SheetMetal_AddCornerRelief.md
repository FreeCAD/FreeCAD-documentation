---
- GuiCommand:/de
   Name:SheetMetal AddCornerRelief
   Name/de:SheetMetal EckentlastungHinzufügen
   MenuLocation:SheetMetal → Add Corner Relief
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**C** **R**
---

# SheetMetal AddCornerRelief/de

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:24px;"> [Eckentlastung hinzufügen](SheetMetal_AddCornerRelief/de.md) fügt einen Ausschnitt zur Eckentlastung hinzu. Ein Entlastungsausschnitt wird normalerweise an Ecken erstellt, an denen sich zwei Kanten (Abstellungen, Bördel) treffen, aber der Befehl kann auch an offenen ecken Entlastungsausschnitte erstellen.

Der Befehl erstellt einen Entlastungsausschnitt zur Zeit.

<img alt="" src=images/SheetMetal_AddCornerRelief-01.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-02.png  style="width:300px;"> 
*Standardecke zweier Kanten → Ecke mit hinzugefügter Eckentlastung*

<img alt="" src=images/SheetMetal_AddCornerRelief-03.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-04.png  style="width:300px;"> 
*Offene Standardecke → Offene Ecke mit hinzugefügter Eckentlastung*

## Anwendung

1.  Zwei Kanten einer Ecke auswählen.
2.  Den Befehl <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:16px;"> **SheetMetal AddCornerRelief** aktivieren durch:
    -   Die Schaltfläche **<img src="images/SheetMetal_AddCornerRelief.svg" width=16px> [Add Corner Relief](SheetMetal_AddCornerRelief.md)**.
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_AddCornerRelief.svg" width=16px> Add Corner Relief**.
    -   Das Tastenkürzel **C** dann **R**.

## Formen der Entlastungsausschnitte 

Die Gestalt einer Eckentlastung kann durch Einstellung der Werte ihrer Eigenschaften verändert werden.

Der Wert der {{PropertyData/de|ReliefSketch}} kann aus einer Liste ausgewählt werden: {{value|Circle}} (default), {{value|Circle-Scaled}}, {{value|Square}}, {{value|Square-Scaled}}, {{value|Sketch}}.

-    {{value|Circle}}und {{value|Square}} verwenden den Wert der {{PropertyData/de|Size}}, um die Größe des Entlastungsausschnitts zu variieren.

-    {{value|Circle-Scaled}}und {{value|Square-Scaled}} verwenden den Wert der {{PropertyData/de|Size Ratio}}, um die Größe des Entlastungsausschnitts zu variieren.

-    {{value|Sketch}}Aktiviert die Verwendung der Skizze, die in der {{PropertyData/de|Sketch}} abgelegt ist, um die Form des Entlastungsausschnitts festzulegen.

<img alt="" src=images/SheetMetal_AddCornerRelief-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-07.png  style="width:200px;"> 
*Kreisförmige Entlastung (mit Standardeinstellungen) → Quadratische Entlastung (mit Standardeinstellungen) → Skizzenbasierte Entlastung*

## Eine nähere Betrachtung der Größe von Entlastungsausschnitten 

Um eine Vorstellung davon zu bekommen, wie und wo ein Entlastungsausschnitt platziert wird, wird die Abwicklung einer Standardecke ohne Entlastungsausschnitt erstellt.

<img alt="" src=images/SheetMetal_AddCornerRelief-08.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-09.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-10.png  style="width:200px;">



*Standardecke zweier Kanten → Ecke mit Abwicklungskörper → Ecke in der Draufsicht*

Der nächste Schritt ist das Öffnen der Abwicklungsskizze, das Erstellen eines Kreises durch drei Punkte und das Erzeugen eines Maßes für den Radius.
Nun fügt man eine Eckentlastung hinzu, erstellt den dazugehörigen Abwicklungskörper und öffnet die erste Abwicklungsskizz erneut.
Ein konzentrischer Kreis mit 3 mm Durchmesser zeigt uns, dass wir herausgefunden haben, wie der interne Kreis platziert wird, da der neue Kreis perfekt in den Ausschnitt des Abwicklungskörpers der Eckentlastung passt.

<img alt="" src=images/SheetMetal_AddCornerRelief-11.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-12.png  style="width:300px;">



*Standardecke mit Abwicklungsskizze → Ecke mit Standardentlastungsausschnitt und derselben Abwicklungsskizze*

Der Versuch die {{PropertyData/de|Size}} auf einen Wert unter 1,67 mm zu setzen, wird zu einem Fehler führen; jeder Wert darüber sollte funktionieren.

Die Auswahl von Circle-Scaled und das Erstellen eines weiteren Abwicklungskörpers zeigt, dass 1,67 mm auch die Basis der **Size Ratio** ist.

## Hinweise

-   der K-Faktor legt fest, wo sich innerhalb der Wandstärke eines Bleches die neutrale Faser befindet.

:   (Es wäre schön zu wissen, ob dieser Faktor auf ISO- oder ANSI-Norm basiert\...)

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-CornerRelief-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|ReliefSketch|Enumeration}}: \"Corner Relief Type\". {{value|Circle}} (standard), {{value|Circle-Scaled}}, {{value|Square}}, {{value|Square-Scaled}}, {{value|Sketch}}.

-    {{PropertyData/de|Size|Length}}: \"Size of Shape\". Größe der Form, Standardwert: {{value|3,00 mm}}.

-    {{PropertyData/de|Size Ratio|Float}}: \"Size Ratio of Shape\". Größenverhältnis der Form, Standardwert: {{value|1,50}}.

-    {{PropertyData/de|base Object|LinkSub}}: \"Base Object\". Verweis zu dem Kantenpaar, das die Lage der Eckentlastung bestimmt.

-    {{PropertyData/de|kfactor|FloatConstraint}}: \"Neutral Axis Position\". Lage der neutralen Faser, Standardwert: {{value|0,50}}.


{{Properties_Title/de|Parameters1}}

-    {{PropertyData/de|Sketch|Link}}: \"Corner Relief Sketch\".

-    {{PropertyData/de|XOffset|Distance}}: \"Gap from side one\". Abstand von der ersten Seite, Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|YOffset|Distance}}: \"Gap from side two\". Abstand von der zweiten Seite, Standardwert: {{value|0,00 mm}}.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddCornerRelief/de
