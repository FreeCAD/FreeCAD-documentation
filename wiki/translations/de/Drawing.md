# Drawing/de
## Einleitung

In FreeCAD wird das Wort \"[Zeichnung](Drawing/de.md)\" normalerweise verwendet, um sich auf die 2D-Projektion eines [3D-Modells](model/de.md) zu beziehen. Diese wird normalerweise mit dem Arbeitsbereich [TechDraw](TechDraw_Workbench/de.md) erstellt.



## Anwendung

1.  Beginne mit einem bereits gebauten [3D-Modell](model/de.md), das z.B. mit dem [PartDesign-Arbeitsbereich](PartDesign_Workbench/de.md) erstellt wurde. Tatsächlich funktioniert jedes Objekt, das eine [Form](Shape/de.md) hat, einschließlich 2D-Objekte.
2.  Wechsle zum [TechDraw-Arbeitsbereich](TechDraw_Workbench/de.md).
3.  Drücke **[<img src=images/TechDraw_PageDefault.svg style="width:16px"> [TechDraw StandardSeite](TechDraw_PageDefault/de.md)** oder **[<img src=images/TechDraw_PageTemplate.svg style="width:16px"> [TechDraw SeitenVorlage](TechDraw_PageTemplate/de.md)**, um eine Seite zu erstellen.
4.  Wähle das vorhandene Modell aus, und drücke dann **[<img src=images/TechDraw_View.svg style="width:16px"> [TechDraw Ansicht](TechDraw_View/de.md)** oder **[<img src=images/TechDraw_ProjectionGroup.svg style="width:16px"> [TechDraw ProjektionsGruppe](TechDraw_ProjectionGroup/de.md)**.
5.  Es wird eine 2D-Projektion auf der Seite erstellt.Du kannst nun ihre Eigenschaften wie {{PropertyData/de|Maßstab}}, {{PropertyData/de|Rotation}} und {{PropertyData/de|Richtung}} anpassen.
6.  Wenn die Zeichnung fertig ist, kannst du **[<img src=images/TechDraw_ExportPageSVG.svg style="width:16px"> [TechDraw ExportSeiteSVG](TechDraw_ExportPageSVG/de.md)**, **[<img src=images/TechDraw_ExportPageDXF.svg style="width:16px"> [TechDraw ExportSeiteDXF](TechDraw_ExportPageDXF/de.md)** drücken oder verwende [Std Export](Std_Export/de.md), um die Seite in die Formate SVG, DXF oder PDF zur weiteren Verwendung in einer anderen Software oder zum Drucken zu exportieren.



## Hinweise

Im informellen Gebrauch kann eine \"Zeichnung\" jede geometrische Abbildung sein, die in der [3D Ansicht](3D_view/de.md) sichtbar ist, und daher kann ihr Konzept mit dem von \"[Körper](Body/de.md)\", \"[Part](Part/de.md)\" oder \"[Modell](Model/de.md)\" verwechselt werden.

Wenn jedoch mehr Präzision erforderlich ist, muss eine Unterscheidung getroffen werden.

-   Ein \"[Körper](Body/de.md)\" ([PartDesign Körper](PartDesign_Body/de.md)) ist ein Objekt, das von einem [Part Formelement](Part_Feature/de.md) abgeleitet ist. (`Part::Feature` Klasse), erstellt mit dem [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md).
-   Ein \"[Part](Part/de.md)\" ([Anwendung Part](App_Part/de.md)) wird zum Gruppieren mehrerer \"[Körper](Body/de.md)\" verwendet, um eine Baugruppe zu bilden.
-   Eine \"Zeichnung\" ist eine 2D-Projektion eines \"Körpers\" oder eines \"Teils\".


{{TechDraw Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [TechDraw](Category_TechDraw.md) > Drawing/de
