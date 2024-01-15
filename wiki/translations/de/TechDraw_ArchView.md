---
 GuiCommand:
   Name: TechDraw ArchView
   Name/de: TechDraw ArchAnsicht
   MenuLocation: TechDraw, Views From Other Workbenches , Objekt des Arbeitsbereichs Arch einfügen
   Workbenches: TechDraw_Workbench/de, Arch_Workbench/de
   SeeAlso: Arch_SectionPlane/de
---

# TechDraw ArchView/de



## Beschreibung

Das Werkzeug **TechDraw ArchAnsicht** fügt eine Ansicht einer **<img src="images/Arch_SectionPlane.svg" width=16px> [Arch Schnittebene](Arch_SectionPlane/de.md)** auf einem [TechDraw Zeichnungsblatt](TechDraw_PageDefault/de.md) ein.

![](images/TechDraw_Arch_example.jpg )



## Anwendung

1.  Eine Arch Schnittebene in der [3D-Ansicht](3D_view/de.md) oder der [Baumansicht](Tree_view/de.md).
2.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswahl in der [Baumansicht](Tree_view/de.md) zur Auswahl hinzufügen.
3.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_ArchView.svg" width=16px> [Objekt des Arbeitsbereichs Arch einfügen](TechDraw_ArchView/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Views From Other Workbenches → <img src="images/TechDraw_ArchView.svg" width=16px> Objekt des Arbeitsbereichs Arch einfügent** auswählen.
4.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und noch kein Blatt aktiviert wurde, wird das Dialogfeld **Blattauswahl** geöffnet: {{Version/de|0.20}}
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.



## Optionen

-   Die Arch-Ansicht wird durch den Arbeitsbereich [Arch](Arch_Workbench/de.md) gerendert.
-   [Draft-Maße](Draft_Snap_Dimensions/de.md), [Draft Texte](Draft_Text/de.md) und jedes andere 2D-Objekt (Skizze oder Entwurf), das von der Schnittebene betrachtet wird, wird \"so wie es ist\" (keine Schnitt- oder verdeckte Linien) über der Festkörpergeometrie gerendert.
-   Das Volumen von [Arch-Räumen](Arch_Space/de.md) wird nicht gerendert, nur die Beschriftung wird gerendert
-   Schnittlinien, projizierte Linien (wenn die Eigenschaft Show Hidden auf True gesetzt ist) und 2D-Linien darüber können mit unterschiedlichen Linienbreiten gerendert werden. Dies kann in den Arch-Einstellungen konfiguriert werden.
-   Die Arch-Ansicht verfügt über zwei Rendermodi:
    -   Wireframe, der die OpenCasCade-Algorithmen des Arbeitsbereichs [TechDraw](TechDraw_Workbench.md) verwendet, ist schnell und erzeugt nur Linien (keine Flächenfüllung möglich).
    -   Solid (Festkörper), der auf dem [Maleralgorithmus](https://de.wikipedia.org/wiki/Maleralgorithmus) basiert und in der Lage ist, Flächen mit ihrer Formfarbe gefüllt darzustellen. Er ist jedoch viel langsamer und kann in vielen Situationen versagen.

:   Die Abbildung unten veranschaulicht den Unterschied zwischen den beiden Rendermodi:





:   ![](images/TechDraw_Arch_rendering.jpg )

-   Nur die Basislinie von [Arch Rohre](Arch_Pipe/de.md) werden gerendert, nicht das volle Volumen des Rohrs:

:   ![](images/TechDraw_Arch_piping.jpg )



## Hinweise

Die ArchView wird innerhalb des [Arch Arbeitsbereichs](Arch_Workbench/de.md) gerendert, daher hat TechDraw nur begrenzte Kontrolle über sein Erscheinungsbild. Möglicherweise musst du Änderungen innerhalb von Arch vornehmen, um die gewünschte Darstellung zu erhalten.



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
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ArchView/de
