---
- GuiCommand:/de
   Name:SheetMetal AddBase
   Name/de:SheetMetal BasisprofilErstellen
   MenuLocation:SheetMetal → Make Base Wall
   Workbenches:[SheetMetal (Blech)](SheetMetal_Workbench/de.md)
   Shortcut:**C** **B**
---

# SheetMetal AddBase/de



## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> [Basisprofil erstellen](SheetMetal_AddBase/de.md) erzeugt ein SheetMetal-Basisobjekt aus einer Skizze.

Aus einer offenen Kontur erzeugt er ein prismatisches **Profil**:

<img alt="" src=images/SheetMetal_AddBase-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-02.png  style="width:200px;">

Aus einer geschlossenen Kontur erzeugt er eine Grund**platte** (Platine):

<img alt="" src=images/SheetMetal_AddBase-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddBase-04.png  style="width:200px;">



## Anwendung



### Profil

1.  Eine <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Skizze](Sketcher_Workbench/de.md) **mit offener Kontur** auswählen.
2.  Den Befehl <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Basisobjekt erstellen](SheetMetal_AddBase/de.md) aktivieren durch
    -   Die Schaltfläche **<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisobjekt erstellen](SheetMetal_AddBase/de.md)**.
    -   Den Menüeintrag **SheetMetal → <img src="images/SheetMetal_AddBase.svg" width=16px> Basisobjekt erstellen**.
    -   Das Tastenkürzel: **C** dann **B**.
3.  Einstellen der Parameter des Profils durch das Ändern der zugehörigen Werte im [Eigenschafteneditor](Property_editor/de.md):
    -   Die {{PropertyData/de|length}} für die Profillänge.
    -   Die {{PropertyData/de|thickness}} für die Profilwandstärke.
    -   Die {{PropertyData/de|radius}} für den Innenradius der Bögen.



### Platine

1.  Eine <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Skizze](Sketcher_Workbench/de.md) **mit geschlossener Kontur** auswählen.
2.  Den Befehl <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Basisobjekt erstellen](SheetMetal_AddBase/de.md) aktivieren (siehe oben).
3.  Einstellen der Parameter des Profils durch das Ändern der zugehörigen Werte im [Eigenschafteneditor](Property_editor/de.md):
    -   Die {{PropertyData/de|thickness}} für die Wandstärke der Platine.

:   

    :   (Die {{PropertyData/de|length}} und {{PropertyData/de|radius}} werden für Platinen nicht verwendet.)



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-BaseBend-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standard Wert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|Bend Side|Enumeration}}: Profillage. Außen, innen oder mittig (entlang der Skizzenlinie),  Werte: {{value|Outside}} (standard), {{value|Inside}}, {{value| Middle}}.

-    **Bend Sketch|Link**: \"Wall Sketch object\". Verweis zur Profil- bzw. Umriss-Skizze.

-    {{PropertyData/de|Mid Plane|Bool}}: \"Extrude Symmetric to Plane\". Ausdehnung symmetrisch zur Ebene.   `True`, das Profil dehnt sich symmetrisch zu beiden Seiten der Skizzenebene aus.

-    {{PropertyData/de|Reverse|Bool}}: \"Reverse Extrusion Direction\". Extrusionsrichtung umkehren, Standardwert: `False`.

-    {{PropertyData/de|length|Length}}: \"Length of wall\". Länge des Profils, Standardwert: {{value|100,00 mm}}.

-    {{PropertyData/de|radius|Length}}: \"Bend Radius\". Biegeradius, Standardwert: {{value|1,00 mm}}.

-    {{PropertyData/de| thickness|Length}}: \"Thickness of sheetmetal\". Blechstärke, Standardwert: {{value|1,00 mm}}.



---
![](images/Button_right.svg) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddBase/de
