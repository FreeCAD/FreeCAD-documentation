---
- GuiCommand:/de
   Name:TechDraw DraftView
   Name/de:TechDraw Entwurfsansicht
   MenuLocation:TechDraw → Entwurfsarbeitsbereichsobjekt einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md), [Entwurf Arbeitsbereich](Draft_Workbench/de.md)
   SeeAlso:[TechDraw ArchAnsicht](TechDraw_ArchView/de.md)
---

## Beschreibung

Das <img alt="" src=images/TechDraw_DraftView.svg  style="width:24px;"> [EntwurfAnsicht](TechDraw_DraftView/de.md) Werkzeug fügt eine Ansicht eines ausgewählten [Part](Part_Workbench/de.md)-basierten oder Gruppenobjekts in ein Zeichenblatt ein. Im Gegensatz zum Standard <img alt="" src=images/TechDraw_View.svg  style="width:24px;"> [Ansicht](TechDraw_View/de.md) Werkzeug, werden die mit diesem Werkzeug erstellten Ansichten mit dem <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Entwurf Arbeitsbereich](Draft_Workbench/de.md) bearbeitet und speziell für die Darstellung von 2D-Objekten entwickelt. Siehe Anmerkungen.

![](images/TechDraw_DraftView_example.png ) *Entwurfselemente wie Kreise und Anordnungen importiert in eine TechDraw Zeichnungsseite*

## Anwendung

1.  Wähle ein Entwurfsobjekt in der 3D Ansicht oder im Baum
2.  Wenn du mehrere Zeichnungsseiten in deinem Dokument hast, musst du die gewünschte Seite im Baum auswählen.
3.  Drücke die **<img src="images/TechDraw_DraftView.svg" width=16px> [Entwurf Arbeitsbereichsobjekt einfügen](TechDraw_DraftView/de.md)** Schaltfläche
4.  Eine Ansicht des Entwurfsobjekts erscheint auf der Seite.

### Begrenzungen

Die EntwurfsAnsicht wird innerhalb der [Entwurf Arbeitsbereich](Draft_Workbench/de.md) gerendert, daher hat TechDraw nur eingeschränkte Kontrolle über ihr Erscheinungsbild. Möglicherweise musst du innerhalb von Draft Änderungen vornehmen, um die gewünschte Darstellung zu erhalten.

## Optionen

-   Das Erstellen einer Entwurfsansicht einer Ebene behandelt rekursiv alle Objekte, die in dieser Ebene gefunden wurden. Die Ansicht wird automatisch aktualisiert, wenn sich der Inhalt der Ebene ändert.
-   Es werden keine versteckten Linien entfernt. Jede Fläche, die in dem/den behandelten Objekt(en) gefunden wird, wird einfach entlang des Richtungsvektors projiziert, es werden keine besonderen Maßnahmen ergriffen, wenn sich Flächen überlappen.
-   Die Entwurfsansicht unterstützt auch alle Entwurfsobjekte, die nicht teilbasiert sind, wie z.B. Bemaßungen und Texte
-   Farbe, Linienbreite und Linienmuster können in den Eigenschaften angegeben werden. Linienmuster können durch direkte Angabe eines [stroke-dasharray](https://www.w3.org/TR/SVG/painting.html#StrokeProperties) Wertes, wie z.B. 3,5 fein abgestimmt werden.
-   Projizierte Flächen werden mit der Flächenfarbe gefüllt

## Eigenschaften

-    {{PropertyData/de|Quelle}}: Das Entwurfsobjekt, das angezeigt werden soll

-    {{PropertyData/de|Linienbreite}}: Die Breite der Linien, unabhängig vom Maßstab

-    {{PropertyData/de|TextGröße}}: Die Textgröße für alle Texte in dieser Ansicht (Texte und Abmessungen).

-    {{PropertyData/de|Richtung}}: Die zu verwendende Projektionsrichtung

-    {{PropertyData/de|Farbe}}: Die Linienfarbe

-    {{PropertyData/de|LinienStil}}: Eine Linienart, die für diese Ansicht zu verwenden ist. Kann durchgehend, gestrichelt, strichpunktiert, Punkt oder ein SVG Linienmuster wie 0.20,0.20 sein.

-    {{PropertyData/de|Zeilenabstand}}: Der zu verwendende Zeilenabstand bei mehrzeiligen Texte.

Hinweis: EntwurfAnsicht erbt alle anwendbaren Basisansichtseigenschaften.

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Neue Entwurfswerkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit folgenden Funktionen verwendet werden:


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDraft','TestDraft')
dv.Source = myDraftbject
rc = page.addView(dv)
```





{{TechDraw Tools navi

}} 
