---
- GuiCommand:
   Name: TechDraw SectionView
   Name/de: TechDraw Schnittansicht
   MenuLocation: TechDraw- TechDraw Ansichten - Schnittansicht einfügen
   Workbenches: [TechDraw](TechDraw_Workbench/de.md)
   SeeAlso: [TechDraw KomplexerSchnitt](TechDraw_ComplexSection/de.md), [TechDraw Ansicht einfügen](TechDraw_View/de.md), [TechDraw Ansichtengruppe einfügen](TechDraw_ProjectionGroup/de.md)
---

# TechDraw SectionView/de



## Beschreibung

Das Werkzeug **TechDraw Schnittansicht** Fügt, von einer bestehenden Bauteilansicht ausgehend, (dem Zeichnungsblatt) eine Schnittansicht (kurz: einen Schnitt) hinzu.

<img alt="" src=images/TechDraw_section_ANSI.png  style="width:350px;">
<img alt="" src=images/TechDraw_section_ISO.png  style="width:350px;"> 
*Schnitt (Schnittdarstellung) einer bereits vorhandenen Ansicht, der die innenliegende Bohrung und eine schraffierte Schnittfläche zeigt.<br>
Das obere Bild zeigt die Schnittpfeile nach ANSI-Vorgabe.<br>
Das untere Bild zeigt die Schnittpfeile nach ISO-Vorgabe.
*



## Anwendung

1.  Eine Bauteilansicht in der 3D-Ansicht oder in der Baumansicht auswählen.
2.  Es gibt mehrere Möglichkeiten dieses Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_SectionView.svg" width=16px> [Schnittansicht](TechDraw_SectionView/de.md)** drücken.
    -   Den Menüeintrag **TechDraw→ TechDraw Views → <img src="images/TechDraw_SectionView.svg" width=16px> Schnittansicht einfügen** auswählen.
3.  Im Aufgabenbereich wird ein Dialog geöffnet, der bei der Berechnung verschiedener Eigenschaften hilft. Es werden sinnvolle Werte für die Blickrichtung errechnet; diese können aber geändert werden.

![](images/TechDraw_Section_Taskview.png ) 
*Aufgabenbereich zum Definieren des Schnitts einer Ansicht*



## Eigenschaften Schnittansicht 

Siehe auch [TechDraw Ansicht](TechDraw_View/de#Eigenschaften.md)



### Daten


{{TitleProperty|Cut Operation}}

-    {{PropertyData/de|Fuse Before Cut|Bool}}: Vereinigt die Ausgangsformen vor der Ausführung der Schnittoperation.

-    {{PropertyData/de|Trim After Cut|Bool}}: Führt eine zusätzliche Beschnittoperation am Ergebnisobjekt aus, um nach dem Schnitt alle unerwünschten Elemente zu entfernen.


{{TitleProperty|Cut Surface}}

-    {{PropertyData/de|Cut Surface Display|Enumeration}}: Darstellung der Schnittfläche. Optionen:

    -   
        {{Value|Hide}}
        
        : Verbirgt die Schnittfläche, nur der Umriss wird angezeigt.

    -   
        {{Value|Color}}
        
        : Färbt die Schnittfläche entsprechend der Einstellung **Farbe für Schnittflächen** in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) ein.

    -   
        {{Value|SvgHatch}}
        
        : Schraffiert den Schnitt, mit einer [Schraffur](TechDraw_Hatch/de.md).

    -   
        {{Value|PatHatch}}
        
        : Schraffiert den Schnitt mit einer [geometrischen Schraffur](TechDraw_GeometricHatch/de.md).

-    {{PropertyData/de|File Hatch Pattern|File}}: Vollständiger Pfad zur SVG-Schraffurmusterdatei.

-    {{PropertyData/de|File Geom Pattern|File}}: Vollständiger Pfad zur PAT-Musterdatei.

-    {{PropertyData/de|Svg Included|FileIncluded}}: Vollständiger Pfad zur enthaltenen SVG-Schraffurmusterdatei.

-    {{PropertyData/de|Pat Included|FileIncluded}}: Vollständiger Pfad zur enthaltenen PAT-Musterdatei.

-    {{PropertyData/de|Name Geom Pattern|String}}: Name des zu verwendenden PAT-Musters.

-    **Hatch Scale|Float**: Größenanpassung des Schraffurmusters.


{{TitleProperty|Section}}

-    {{PropertyData/de|Section Symbol|String}}: Bezeichner für diesen Schnitt.

-    {{PropertyData/de|Base View|Link}}: Die Ansicht, auf der dieser Schnitt basiert.

-    {{PropertyData/de|Section Normal|Vector}}: Ein Vektor, der die Richtung normal (senkrecht) zur Schnittebene beschreibt.

-    {{PropertyData/de|Section Origin|Vector}}: Ein Vektor, der einen Punkt auf der Schnittebene beschreibt. Typischerweise der Schwerpunkt des Originalteils.

-    **Section Direction|Enumeration**: Die Richtung dieser Schnittansicht in der Basisansicht. Optionen: {{Value|Aligned}}, {{Value|Right}}, {{Value|Left}}, {{Value|Up}} or {{Value|Down}}.



### Ansicht


{{TitleProperty|Cut Surface}}

-    {{PropertyView/de|Cut Surface Color|Color}}: Farbton für Flächenhervorhebung. Wird verwendet, wenn **Cut Surface Display** auf {{Value|Color}} eingestellt ist.

-    {{PropertyView/de|Show Cut Surface|Bool|Hidden}}: Schaltet die Sichtbarkeit der Schnittfläche ein/aus.


{{TitleProperty|Surface Hatch}}

-    **Geom Hatch Color|Color**: Farbe des geometrischen Schraffurmusters.

-    {{PropertyView/de|Hatch Color|Color}}: Farbe des SVG-Schraffurmusters.

-    **Hatch Cut Surface|Bool|Hidden**: Schraffiert die Schnittfläche.

-    {{PropertyView/de|Weight Pattern|Float}}: Linienstärke für geometrische Schraffurmuster.



## Eigenschaften Basisansicht 

Eine Schnittansicht erbt alle anwendbaren Eigenschaften der Ansicht, die in der {{{PropertyData/de|Base View}}} angegeben sind. In den Eigenschaften dieser Ansicht kann die Darstellung der Schnittlinie geändert werden:

-    {{PropertyView/de|Section Line Color}}: Farbe der Schnittlinie.

-    {{PropertyView/de|Section Line Style}}: Linienart der Schnittlinie.

Die Standardeinstellungen für diese Parameter werden über die Einstellungen **Section Line** und **Section Line Style** in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) eingestellt.



## Hinweise

-   **Section Line Format**: Zwei Arten zur Schnittliniendarstellung werden unterstützt (wie oben abgebildet) und durch die Einstellung \"Normbasis für Schnittlinien\" (Section Line Standard) auf dem Reiter Anmerkung bestimmt. Die Option {{Value|ANSI}} verwendet \"ziehende Peile\" (in einigen Regionen auch als \"traditionelles Format\" bekannt) und die Option {{Value|ISO}} verwendet \"schiebende Pfeile\" (auch als \"Reference Arrow Format\", Referenzpfeilmethode bekannt).
-   **Fuse Before Cut**: Die Schnittoperation kann manchmal die Ausgangsformen nicht schneiden. Wenn Fuse Before Cut den Wert TRUE besitzt, werden die Ausgangsformen zu einer einzigen Form zusammengeführt, bevor die Schnittoperation versucht wird. Wenn es Probleme mit der Schnittoperation gibt, kann es helfen, diesen Wert umzuschalten.
-   **Trim After Cut**: Die Schnittoperation lässt manchmal (ungewollte) Anteile der Ausgangsform übrig. Wenn **Trim After Cut** den Wert TRUE besitzt, wird an dem Ergebnis des ersten Schnittes eine zusätzliche Beschnittoperation ausgeführt, die alle ungewollten Anteile entfernen sollte.
-   **Cut Surface Display**: Die Schnittfläche kann ausgeblendet, mit Farbe gefüllt, mit einem SVG-Muster schraffiert oder mit einem PAT-Muster schraffiert werden. Siehe [Schraffieren](TechDraw_Hatching/de.md).



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Eine Schnittansicht kann mit [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen erstellt werden:


```python
doc = FreeCAD.ActiveDocument
box = doc.Box
page = doc.Page

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = box
view.Direction = (0, 0, 1)

section = doc.addObject("TechDraw::DrawViewSection", "Section")
page.addView(section)
section.Source = box
section.BaseView = view
section.Direction = (0, 1, 0)
section.SectionNormal = (-1, 0, 0)

doc.recompute()
```



## Beispiele

Für weitere Information über Schnittansichten und einige Beispiele siehe: [TechDraw Schnittbeispiele](TechDraw_Section_Examples/de.md).

<img alt="" src=images/TechDraw_ExampleSection-10.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-13.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-15.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-17.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-34.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-35.png  style="width:80px;">





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SectionView/de
