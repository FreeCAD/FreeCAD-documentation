---
- GuiCommand   */de
   Name   *TechDraw DraftView
   Name/de   *TechDraw DraftAnsicht
   MenuLocation   *TechDraw → Objekt des Draft-Arbeitsbereiches einfügen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md), [Draft](Draft_Workbench/de.md)
   SeeAlso   *[TechDraw ArchAnsicht](TechDraw_ArchView/de.md)
---

# TechDraw DraftView/de

## Beschreibung

Das Werkzeug <img alt="" src=images/TechDraw_DraftView.svg  style="width   *24px;"> [DraftAnsicht](TechDraw_DraftView/de.md) fügt eine Ansicht eines ausgewählten [Part](Part_Workbench/de.md)-basierten Objekts oder eines Gruppenobjekts in ein Zeichnungsblatt ein. Anders als beim Standardwerkzeug <img alt="" src=images/TechDraw_View.svg  style="width   *24px;"> [Ansicht](TechDraw_View/de.md), werden die mit diesem Werkzeug erstellten Ansichten mit dem Arbeitsbereich <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> [Draft](Draft_Workbench/de.md) bearbeitet und sind besonders für die Darstellung von 2D-Objekten entwickelt. Siehe Anmerkungen unter Begrenzungen.

![](images/TechDraw_DraftView_example.png ) 
*Draft-Elemente wie Kreise und Anordnungen importiert in ein TechDraw-Zeichnungsblatt*

## Anwendung

1.  Ein Draft-Objekt in der 3D-Ansicht oder im Baum auswählen.
2.  Sind in dem Dokument mehrere Zeichnungsseiten vorhanden, musst die gewünschte Seite im Baum ausgewählt werden.
3.  Die Schaltfläche **<img src="images/TechDraw_DraftView.svg" width=16px> [Objekt des Draft-Arbeitsbereiches einfügen](TechDraw_DraftView/de.md)** drücken.
4.  Eine Ansicht des Draft-Objekts erscheint auf der Seite.

### Begrenzungen

Die Draft-Ansicht wird innerhalb des Arbeitsbereiches [Draft](Draft_Workbench/de.md) gerendert, daher hat TechDraw nur eingeschränkte Kontrolle über ihr Erscheinungsbild. Man muss möglicherweise Änderungen innerhalb von Draft vornehmen, um die gewünschte Darstellung zu erhalten.

## Optionen

-   Das Erstellen einer Draft-Ansicht (DraftView-Objekt) von einer Ebene verwendet rekursiv alle Objekte, die auf dieser Ebene gefunden wurden. Die Ansicht wird automatisch aktualisiert, wenn sich der Inhalt der Ebene ändert.
-   Es werden keine verdeckten Kanten entfernt. Jede Fläche, die in dem (den) verwendeten Objekt(en) gefunden wird, wird einfach entlang des Richtungsvektors projiziert, es werden keine besonderen Maßnahmen ergriffen, wenn sich Flächen überlappen.
-   Die Draft-Ansicht unterstützt auch alle Draft-Objekte, die nicht auf Bauteilen basierten, wie z.B. Maße und Texte.
-   Farbe, Linienbreite und Linienart können in den Eigenschaften angegeben werden. Linienarten können durch direkte Angabe eines [stroke-dasharray](https   *//www.w3.org/TR/SVG/painting.html#StrokeProperties) Wertes, wie z.B. 3,5 fein abgestimmt werden.
-   Projizierte Flächen werden mit der Flächenfarbe gefüllt

## Eigenschaften

-    {{PropertyData/de|Source}}   * Das Draft-Objekt, das angezeigt werden soll

-    {{PropertyData/de|Line Width}}   * Die Breite der Linien, unabhängig vom Maßstab

-    {{PropertyData/de|Font Size}}   * Die Schrifthöhe aller Texte in dieser Ansicht (Texte und Maße).

-    {{PropertyData/de|Direction}}   * Die zu verwendende Projektionsrichtung

-    {{PropertyData/de|Color}}   * Die Linienfarbe

-    {{PropertyData/de|Linienstil}}   * Eine Linienart, die für diese Ansicht zu verwenden ist. Kann Solid, Dashed, Dashdot, Dot (für Voll-, Strich-, Strich-Punkt-, Punktlinie) oder ein SVG-Linienmuster wie 0.20,0.20 sein.

-    {{PropertyData/de|Line Spacing}}   * Der zu verwendende Zeilenabstand bei mehrzeiligen Texten.

Hinweis   * Die Draft-Ansicht erbt alle anwendbaren grundlegenden Ansicht-Eigenschaften.

## Skripten


**Siehe auch   ***

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug DraftAnsicht kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgenden Funktionen verwendet werden   *


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewDraft','TestDraft')
dv.Source = myDraftbject
rc = page.addView(dv)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DraftView/de
