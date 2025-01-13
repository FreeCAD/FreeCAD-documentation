---
 GuiCommand:
   Name: TechDraw ArchView
   Name/de: TechDraw ArchAnsicht
   MenuLocation: TechDraw, Views From Other Workbenches , Objekt des Arbeitsbereichs BIM einfügen
   Workbenches: TechDraw_Workbench/de, BIM_Workbench/de
   SeeAlso: Arch_SectionPlane/de
---

# TechDraw ArchView/de



## Beschreibung

Das Werkzeug **TechDraw ArchAnsicht** fügt eine Arch-Ansicht, eine Ansicht einer <img alt="" src=images/Arch_SectionPlane.svg  style="width:16px;"> [Arch Schnittebene](Arch_SectionPlane/de.md), auf einem [TechDraw Zeichnungsblatt](TechDraw_PageDefault/de.md) ein.


{{Version/de|1.0}}

: Auch das Werkzeug [TechDraw Ansicht](TechDraw_View/de.md) kann eine Arch-Ansicht erstellen.

<img alt="" src=images/TechDraw_Arch_example.jpg  style="width:500px;">



## Anwendung

1.  Eine Arch-Schnittebene in der [3D-Ansicht](3D_view/de.md) oder der [Baumansicht](Tree_view/de.md) auswählen.
2.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswahl in der [Baumansicht](Tree_view/de.md) zur Auswahl hinzufügen.
    -   Den Menüeintrag **TechDraw → Ansichten von anderen Arbeitsbereichen → <img src="images/TechDraw_ArchView.svg" width=16px> Objekt des Arbeitsbereichs BIM einfügen** auswählen.
3.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und kein Blatt im [Hauptansichtsbereich](Main_view_area/de.md) angezeigt wird und außerdem noch kein Blatt aktiviert wurde, wird das Dialogfenster **Blattauswahl** geöffnet:
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.



## Optionen

-   Die Arch-Ansicht wird durch den Arbeitsbereich [BIM](BIM_Workbench/de.md) gerendert.
-   [Draft-Maße](Draft_Snap_Dimensions/de.md), [Draft-Texte](Draft_Text/de.md) und jedes andere 2D-Objekt (Skizze oder Zeichnung), das von der Schnittebene berücksichtigt wird, wird \"so wie es ist\" (keine Schnitt- oder verdeckte Linien) über der Festkörpergeometrie gerendert.
-   Das Volumen von [Arch-Räumen](Arch_Space/de.md) wird nicht gerendert, nur die Beschriftung wird gerendert
-   Schnittlinien, projizierte Linien (wenn die Eigenschaft Show Hidden auf True gesetzt ist) und 2D-Linien darüber können mit unterschiedlichen Linienbreiten gerendert werden. Dies kann in den Arch-Einstellungen konfiguriert werden.
-   Die Arch-Ansicht verfügt über zwei Rendermodi:
    -   Wireframe, der die OpenCasCade-Algorithmen des Arbeitsbereichs [TechDraw](TechDraw_Workbench.md) verwendet, ist schnell und erzeugt nur Linien (keine Flächenfüllung möglich).
    -   Solid (Festkörper), der auf dem [Maleralgorithmus](https://de.wikipedia.org/wiki/Maleralgorithmus) basiert und in der Lage ist, Flächen mit ihrer Formfarbe gefüllt darzustellen. Er ist jedoch viel langsamer und kann in vielen Situationen versagen.

:   Die Abbildung unten veranschaulicht den Unterschied zwischen den beiden Rendermodi:





:   ![](images/TechDraw_Arch_rendering.jpg )

-   Nur die Basislinie von [Arch-Rohren](Arch_Pipe/de.md) wird gerendert, nicht das volle Volumen des Rohrs:

:   ![](images/TechDraw_Arch_piping.jpg )



## Hinweise

Die Arch-Ansicht wird innerhalb des Arbeitsbereichs [BIM](BIM_Workbench/de.md) gerendert, daher hat TechDraw nur begrenzte Kontrolle über ihr Erscheinungsbild. Möglicherweise müssen Änderungen innerhalb von Arch vorgenommen werden, um die gewünschte Darstellung zu erhalten.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Eine Arch-Ansicht, oder formal ein {{Incode|TechDraw::DrawViewArch}}-Objekt, besitzt die gemeinsamen [Eigenschaften](TechDraw_View/de#Eigenschaften_der_Bauteilansicht.md) aller Ansichtsarten. Sie enthält außerdem die folgenden Eigenschaften:



### Daten


{{TitleProperty|Arch view}}

-    {{PropertyData/de|Source|Link}}: Das anzuzeigende Objekt der Schnittebene.

-    {{PropertyData/de|All On|Bool}}: Gibt an, ob ausgeblendete Objekte angezeigt werden sollen oder nicht. Wenn `False`, werden nur Objekte gerendert, die in der 3D-Ansicht sichtbar sind.

-    {{PropertyData/de|Render Mode|Enumeration}}: Der zu verwendende Rendermodus, {{Value|Solid}} oder {{Value|Wireframe}}.

-    {{PropertyData/de|Fill Spaces|Bool}}: Wenn `True`, werden Arch-Räume als farbige Fläche dargestellt.

-    {{PropertyData/de|Show Hidden|Bool}}: Gibt an, ob die verdeckte Geometrie (der Teil der Geometrie, der hinter der Schnittebene liegt) angezeigt wird oder nicht. Sie wird mit einer Strichlinie dargestellt, die in den Arch-Einstellungen konfiguriert werden kann.

-    {{PropertyData/de|Show Fill|Bool}}: Gibt an, ob geschnittene Bereiche mit einer grauen Farbe gefüllt werden sollen oder nicht.

-    {{PropertyData/de|Line Width|Float}}: Die Breite der Hauptlinien. Die Breitenverhältnisse von Schnittlinien, projizierte und 2D-Linien können in den Arch-Einstellungen konfiguriert werden.

-    {{PropertyData/de|Font Size|Float}}: Die Schriftgröße aller Texte in dieser Ansicht.

-    {{PropertyData/de|Cut Line Width|Float}}: Linienbreite der Schnittlinien in dieser Ansicht.

-    {{PropertyData/de|Join Arch|Bool}}: Wenn `True`, werden Wände und Strukturen aus dem gleichen Material vereinigt.

-    {{PropertyData/de|Line Spacing|Float}}: Der Zeilenabstand, der für mehrzeiligen Text verwendet wird. {{Version/de|1.0}}


{{TitleProperty|Drawing view}}

-    {{PropertyData/de|Symbol|String|Hidden}}: Der SVG-Code, der dieses Zeichnungselement definiert.

-    {{PropertyData/de|Editable Texts|StringList|Hidden}}: Ersatzwert für bearbeitbare Zeichenfolgen in diesem Zeichnungselement.

-    {{PropertyData/de|Owner|Link}}: Element dem dieses Zeichnungselement zugeordnet ist. {{Version/de|1.0}}



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

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
