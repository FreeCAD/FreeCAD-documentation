---
- GuiCommand   */de
   Name   *TechDraw SectionView
   Name/de   *TechDraw SchnittAnsicht
   MenuLocation   *TechDraw → Schnittansicht einfügen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso   *[TechDraw Ansicht einfügen](TechDraw_View/de.md),[TechDraw Projektionsgruppe einfügen](TechDraw_ProjectionGroup/de.md)
---

# TechDraw SectionView/de

## Beschreibung

Das Werkzeug Schnittansicht erstellt eine Schnittdarstellung (kurz   * einen Schnitt) aus einer bereits bestehenden Bauteilansicht.

<img alt="" src=images/TechDraw_Section_example.png  style="width   *250px;"> 
*Schnitt (Schnittdarstellung) einer bereits platzierten Ansicht, der die innenliegenden Bohrungen und eine schattierte Schnittfläche zeigt*

## Anwendung

1.  Eine Bauteilansicht in der 3D-Ansicht oder in der Baumansicht auswählen.
2.  Die Schaltfläche **<img src="images/TechDraw_SectionView.svg" width=16px> [Schnittansicht einfügen](TechDraw_SectionView/de.md)** drücken.
3.  Ein Dialogfeld wird geöffnet, das bei der Berechnung der verschiedenen Schnitteigenschaften hilft. Das Dialogfeld berechnet sinnvolle Ausgangspunkte für die Schnittnormale (Section Normal) und Ausrichtung der Ansicht, die jedoch nach der Erstellung für spezielle Anforderungen angepasst werden können.
4.  Tritt beim Einrichten der Schnittparameter ein Fehler auf, oder entscheidet man sich während der Einstellung um, kann man die Teste **Reset** drücken und von vorne beginnen.

![](images/TechDraw_Section_Taskview.png ) 
*Aufgabenbereich zum Definieren des Schnitts einer Ansicht*

## Properties Section View 

See also [TechDraw View](TechDraw_View#Properties.md).

### Daten


{{TitleProperty|Cut Surface Format}}


<div class="mw-translate-fuzzy">

#### Cut Surface Format 

-    {{PropertyData/de|Cut Surface Display}}   * Darstellung der Schnittfläche. Optionen   *

    -   *Hide*   * Verbirgt die Schnittfläche, nur der Umriss wird angezeigt.
    -   *Color*   * Färbt die Schnittfläche entsprechend der Einstellung **Farbe für Schnittflächen** in den [TechDraw Einstellungen](TechDraw_Preferences/de.md).
    -   *SvgHatch*   * Schraffiert den Schnitt, mit einer [Schraffur](TechDraw_Hatch/de.md).
    -   *PatHatch*   * Schraffiert den Schnitt mit einer [geometrischen Schraffur](TechDraw_GeometricHatch/de.md).

-    {{PropertyData/de|File Hatch Pattern}}   * Vollständiger Pfad zur SVG-Schraffurmusterdatei.

-    {{PropertyData/de|File Geom Pattern}}   * Vollständiger Pfad zur PAT-Musterdatei.

-    {{PropertyData/de|Svg Included}}   * Vollständiger Pfad zur enthaltenen SVG-Schraffurmusterdatei.

-    {{PropertyData/de|Pat Included}}   * Vollständiger Pfad zur enthaltenen PAT-Musterdatei.

-    {{PropertyData/de|Name Geom Pattern}}   * Name des zu verwendenden PAT-Musters (wird bei der Einstellung *SvgHatch* von **Cut Surface Display** ignoriert).


</div>


{{TitleProperty|Section}}


<div class="mw-translate-fuzzy">

#### Section

-    {{PropertyData/de|Base View}}   * Die Ansicht, auf der dieser Schnitt basiert.

-    {{PropertyData/de|Section Normal}}   * Ein Vektor, der die Richtung normal (senkrecht) zur Schnittebene beschreibt.

-    {{PropertyData/de|Section Origin}}   * Ein Vektor, der einen Punkt auf der Schnittebene beschreibt. Typischerweise der Schwerpunkt des Originalteils.

-    {{PropertyData/de|Fuse Before Cut}}   * Vereinigt die Ausgangsformen, bevor der Schnitt erzeugt wird.


</div>

### Ansicht


{{TitleProperty|Cut Surface}}


<div class="mw-translate-fuzzy">

#### Cut Surface 

-    {{PropertyView/de|Cut Surface Color}}   * Farbton für Flächenhervorhebung. Wird verwendet, wenn **Cut Surface Display** auf *Color* eingestellt ist.


</div>


{{TitleProperty|Surface Hatch}}


<div class="mw-translate-fuzzy">

#### Surface Hatch 

-    {{PropertyView/de|Hatch Color}}   * Farbe für Oberflächenschraffurlinien.

-    {{PropertyView/de|Weight Pattern}}   * Linienstärke für Oberflächenschraffurlinien.


</div>

## Properties Base View 


<div class="mw-translate-fuzzy">

Eine Schnittansicht erbt alle anwendbaren Eigenschaften der Ansicht, die in der {{{PropertyData/de|BaseView}}} angegeben ist. In den Eigenschaften der Ansicht kann die Darstellung der Schnittlinie geändert werden   *


</div>


<div class="mw-translate-fuzzy">

-    {{PropertyView/de|Section Line Color}}   * Farbe der Schnittlinie.

-    {{PropertyView/de|Section Line Style}}   * Linienart der Schnittlinie.


</div>

Die Standardeinstellungen für diese Parameter werden über die Einstellungen **Section Line** und **Section Line Style** in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) eingestellt.

## Hinweise

-   **Schnittlinienformat**   * sowohl das herkömmliche Schnittlinienformat (wie oben abgebildet) als auch die \"Referenzpfeil Methode\" werden unterstützt. Diese Option wird durch die Voreinstellung \"Mod/TechDraw/Format/SectionFormat\" gesteuert (siehe [Std_DlgParameter](Std_DlgParameter/de.md)). 0 für die herkömmliche Linienmethode, 1 für die Referenzpfeilmethode.
-   **SchneideOberflächeAnzeige**   * die Schnittfläche kann ausgeblendet, in einer Volltonfarbe gemalt, mit einem Svg Muster (Standard) schraffiert oder mit einem PAT Muster schraffiert werden. Siehe [Schraffur](TechDraw_Hatching/de.md).
-   **VerschmelzenVorSchneiden**   * Die Querschnittsoperation kann manchmal die Ausgangsformen nicht schneiden. Wenn VerschmelzenVorSchneiden wahr ist, werden die Ausgangsformen zu einer einzigen Form zusammengeführt, bevor die Schnittoperation versucht wird. Wenn du Probleme mit der Abschnittsoperation hast, versuche, diesen Wert umzudrehen.

## Skripten


**Siehe auch   ***

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Neue Abschnittswerkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus mit den folgenden Funktionen verwendet werden   *


```python
view = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewPart','View')
rc = page.addView(view)
view.Source = box
view.Direction = (0.0,0.0,1.0)

section = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewSection','Section')
rc = page.addView(section)
section.Source = box
section.BaseView = view
section.Direction = (0.0,1.0,0.0)
section.SectionNormal = (0.0,0.0,1.0)
section.SectionOrigin = (5.0,5.0,5.0)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SectionView/de
