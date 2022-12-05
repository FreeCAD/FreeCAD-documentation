---
- GuiCommand:/de
   Name:TechDraw ArchView
   Name/de:TechDraw ArchAnsicht
   MenuLocation:TechDraw → Arch Arbeitsbereichsobjekt einfügen
   Workbenches:[TechDraw](TechDraw_Workbench.md), [Arch](Arch_Workbench/de.md)
   SeeAlso:[Arch Schnittebene](Arch_SectionPlane/de.md)
---

# TechDraw ArchView/de

## Beschreibung

Das ArchAnsicht Werkzeug fügt eine Ansicht einer **<img src="images/Arch_SectionPlane.svg" width=16px> [Arch SchnittEbene](Arch_SectionPlane/de.md)** auf einer [TechDraw StandardSeite](TechDraw_PageDefault/de.md) ein.

![](images/TechDraw_Arch_example.jpg )

## Anwendung

1.  Wähle eine Arch Schnittebene in der 3D Ansicht oder im Baum
2.  Wenn du mehrere Zeichnungsseiten in deinem Dokument hast, musst du die gewünschte Seite im Baum auswählen.
3.  Drücke die **<img src="images/TechDraw_ArchView.svg" width=24px> [Einfügen Arch Arbeitsbereichsobjekt](TechDraw_ArchView/de.md)** Schaltfläche
4.  Eine Ansicht der Objekte, die von der Schnittebene gesehen werden, erscheint auf der Seite.

### Begrenzungen

Die ArchView wird innerhalb des [Arch Arbeitsbereichs](Arch_Workbench/de.md) gerendert, daher hat TechDraw nur begrenzte Kontrolle über sein Erscheinungsbild. Möglicherweise musst du Änderungen innerhalb von Arch vornehmen, um die gewünschte Darstellung zu erhalten.

## Optionen

-   Die Arch Ansicht wird durch den [Arch-Arbeitsbereich](Arch_Workbench/de.md) gerendert, auf die gleiche Weise wie im [Arbeitsbereich Zeichnen](Drawing_Workbench.md). Siehe Anmerkungen.
-   [Entwurf Abmessungen](Draft_Snap_Dimensions/de.md), [Entwurf Texte](Draft_Text/de.md) und jedes andere 2D Objekt (Skizze oder Entwurf), das von der Schnittebene betrachtet wird, wird \"so wie es ist\" (kein Schnittpunkt oder verdeckte Linien) über der Volumenkörpergeometrie gerendert.
-   Das Volumen von [Arch Räume](Arch_Space/de.md) wird nicht gerendert, nur die Beschriftung wird gerendert
-   Schnittlinien, projizierte Linien (wenn die Ausgeblendet anzeigen Eigenschaft auf True gesetzt ist) und 2D Linien oben können mit unterschiedlichen Linienbreiten gerendert werden. Dies kann in den Arch Einstellungen konfiguriert werden.
-   Die ArchAnsicht verfügt über zwei Renderungsmodi: Wireframe, das die OpenCasCade Algorithmen des [Arbeitsbereich Zeichnen](Drawing_Workbench/de.md) verwendet, ist schnell und erzeugt nur Linien (keine Flächenfüllung möglich), und Festkörper, das auf dem [Maleralgorithmus](https://de.wikipedia.org/wiki/Maleralgorithmus) basiert und in der Lage ist, Flächen mit ihrer Formfarbe gefüllt darzustellen. Er ist jedoch viel langsamer und kann in vielen Situationen versagen. Die Abbildung unten veranschaulicht den Unterschied zwischen den beiden Renderungsmodi:

![](images/TechDraw_Arch_rendering.jpg )

-   Nur die Basislinie von [Arch Rohre](Arch_Pipe/de.md) werden gerendert, nicht das volle Volumen des Rohrs:

![](images/TechDraw_Arch_piping.jpg )

## Eigenschaften

Siehe auch [TechDraw Ansicht](TechDraw_View/de#Eigenschaften.md)

### Daten


{{TitleProperty|Arch view}}

-    {{PropertyData/de|Source|Link}}: Das anzuzeigende Objekt der Schnittebene.

-    {{PropertyData/de|All On|Bool}}: Ob ausgeblendete Objekte angezeigt werden müssen oder nicht. Wenn `False`, werden nur Objekte gerendert, die in der 3D Ansicht sichtbar sind.

-    {{PropertyData/de|Render Mode|Enumeration}}: Der zu verwendende Rendermodus, {{Value|Solid}} oder {{Value|Wireframe}}.

-    {{PropertyData/de|Fill Spaces|Bool}}: Wenn `True`, werden Arch-Spaces als farbige Fläche dargestellt.

-    {{PropertyData/de|Show Hidden|Bool}}: Ob die verdeckte Geometrie (der Teil der Geometrie, der hinter der Schnittebene liegt) angezeigt wird oder nicht. Sie wird mit einer Strichlinie dargestellt, die in den Arch-Einstellungen konfiguriert werden kann.

-    {{PropertyData/de|Show Fill|Bool}}: Ob geschnittene Bereiche mit einer grauen Farbe gefüllt werden müssen oder nicht.

-    {{PropertyData/de|Line Width|Float}}: Die Breite der Hauptlinien. Die Breitenverhältnisse von Schnittlinien, projizierte und 2D-Linien können in den Arch-Einstellungen konfiguriert werden.

-    {{PropertyData/de|Font Size|Float}}: Die Schrifthöhe aller Texte, die in dieser Ansicht erscheinen.

-    {{PropertyData/de|Cut Line Width|Float}}: Linienbreite der Schnittlinien in dieser Ansicht.

-    {{PropertyData/de|Join Arch|Bool}}: Wenn `True`, werden Wände und Strukturen mit Material vereinigt.

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug ArchAnsicht kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewArch','TestArch')
dv.Source = mySectionPlane
rc = page.addView(dv)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ArchView/de
