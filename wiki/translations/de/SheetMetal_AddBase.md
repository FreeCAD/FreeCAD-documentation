---
 GuiCommand:
   Name: SheetMetal AddBase
   Name/de: SheetMetal BasisprofilErstellen
   MenuLocation: SheetMetal , Make Base Wall
   Workbenches: SheetMetal_Workbench/de
   Shortcut: **C** **B**
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
2.  Es ist mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/SheetMetal_AddBase.svg" width=16px> [Basisobjekt erstellen](SheetMetal_AddBase/de.md)** drücken.
    -   Den Menüeintrag **Sheet Metal → <img src="images/SheetMetal_AddBase.svg" width=16px> Basisobjekt erstellen** auswählen.
    -   Ein Rechtsklick in die [Baumansicht](Tree_view/de.md) oder die [3D-Ansicht](3D_view/de.md) und die Menüoption **Sheet Metal → <img src="images/SheetMetal_AddBase.svg" width=16px> Basisobjekt erstellen** im Kontextmenü auswählen.
    -   Das Tastenkürzel **C** dann **B**.
3.  Ein **BaseBend**-Objekt wird erstellt; Ecken im Verlauf der Kontur werden automatisch in zylindrische Bögen gewandelt.
4.  Die Parameter des Profils im [Eigenschafteneditor](Property_editor/de.md) anpassen:
    -   Die {{PropertyData/de|length}} für die Extrusionslänge des Profils.
    -   Die {{PropertyData/de|thickness}} für die Wandstärke des Profils.
    -   Die {{PropertyData/de|radius}} für den Innenradius der automatisch hinzugefügten Bögen.



### Platine

1.  Eine <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Skizze](Sketcher_Workbench/de.md) **mit geschlossener Kontur** auswählen.
2.  Den Befehl aufrufen, wie oben beschrieben.
3.  Die Parameter der Platinne im [Eigenschafteneditor](Property_editor/de.md) anpassen:
    -   Die {{PropertyData/de|thickness}} für die Wandstärke der Platine.

:   

    :   (Die {{PropertyData/de|length}} und {{PropertyData/de|radius}} werden für Platinen nicht verwendet.)



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-BaseBend-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet oder, wenn es sich in einem [PartDesign-Körper](PartDesign_Body/de.md) befindet, von einem [PartDesign Formelement](PartDesign_Feature/de.md) und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|Bend Side|Enumeration}}: Profillage, legt fest, zu welcher Seite der Profilkurve die Wandstärke aufgetragen wird. {{value|Outside}} außen (Standardwert), {{value|Inside}} innen oder {{value| Middle}} mittig. (wird nicht für Platinen verwendet)

-    {{PropertyData/de|Bend Sketch|Link}}: \"Wall Sketch object\". Verweis zur Profil- bzw. Umriss-Skizze.

-    {{PropertyData/de|Mid Plane|Bool}}: Symmetrisch zur Ebene extrudieren. Die Ausdehnung eines Profils oder die Wandstärke einer Platine befindet sich auf einer Seite der der Skizzenebene, wenn `False` gesetzt ist (Standardwert) oder ist symmetrisch zur Skizzenebene, wenn `True` gesetzt ist.

-    {{PropertyData/de|Reverse|Bool}}: Kehrt die Richtung der Extrusion eines Profils bzw. der Wandstärke einer Platine um. Standardwert: `False`.

-    {{PropertyData/de|length|Length}}: Extrusionslänge eines Profils. Standardwert: {{value|100,00 mm}}. (wird nicht für Platinen verwendet)

-    {{PropertyData/de|radius|Length}}: Innenradius der automatisch hinzugefügten Bögen. Standardwert: {{value|1,00 mm}}. (wird nicht für Platinen verwendet)

-    {{PropertyData/de|thickness|Length}}: Wandstärke eines Blechprofils oder einer Platine. Standardwert: {{value|1,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddBase/de
