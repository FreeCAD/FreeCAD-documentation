---
- GuiCommand:/de
   Name:TechDraw SectionView
   Name/de:TechDraw SchnittAnsicht
   MenuLocation:TechDraw → Schnittansicht einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Ansicht einfügen](TechDraw_View/de.md),[TechDraw Projektionsgruppe einfügen](TechDraw_ProjectionGroup/de.md)
---

# TechDraw SectionView/de

## Beschreibung

Das Abschnitt Werkzeug erstellt eine Querschnittdarstellung aus einer bereits bestehenden Teilansicht.

<img alt="" src=images/TechDraw_Section_example.png  style="width:250px;"> 
*Schnittdarstellung einer bereits platzierten Ansicht, die die Innenbohrungen und eine schattierte Schnittfläche zeigt*

## Anwendung

1.  Wähle eine Teilansicht im 3D Fenster oder Baum.
2.  Wenn du mehrere Zeichnungsseiten in deinem Dokument hast, musst du auch die gewünschte Seite im Baum auswählen.
3.  Drücke die **<img src="images/TechDraw_SectionView.svg" width=16px> [Schnittansicht einfügen](TechDraw_SectionView.md)** Schaltfläche
4.  Ein Dialogfeld wird geöffnet, das bei der Berechnung der verschiedenen Querschnittseigenschaften hilft. Das Dialogfeld berechnet sinnvolle Startpunkte für SchnittNormal und Ansichtsrichtung, die jedoch nach der Erstellung für spezielle Anforderungen geändert werden können.
5.  Wenn du beim Einrichten der Abschnittsparameter einen Fehler machst oder deine Meinung änderst, drücke die **Reset** Taste und du kannst von vorn beginnen.

![](images/TechDraw_Section_Taskview.png ) *Aufgabenansicht zum Definieren des Schnitts einer Ansicht*

## Eigenschaften

### Daten

#### Abschnitt

-    **Grundansicht**: Die Ansicht, auf der dieser Schnitt basiert.

-    **Abschnitt Normal**: Ein Vektor, der die Richtung senkrecht zur Schnittebene beschreibt.

-    **Abschnitt Ursprung**: Ein Vektor, der einen Punkt auf der Schnittebene beschreibt. Typischerweise der Schwerpunkt des Originalteils.

-    **Verschmelzen vor dem Schneiden**: Verschmelze die Ausgangsformen, bevor du den Abschnittsschnitt durchführst.

#### Schneide Oberflächenformat 

-    {{PropertyData/de|Oberflächenanzeige schneiden}}: Erscheinungsbild der Schnittoberfläche. Optionen:

    -   *Ausblenden* Verbirgt die Schnittfläche, nur der Umriss wird angezeigt.
    -   *Farbe*: Färbt die Schnittfläche mit der Einstellung **Schnittoberflächenfarbe** in den [TechDraw Einstellungen](TechDraw_Preferences/de.md).
    -   *SvgSchraffur*: Schraffiert den Abschnitt, der mit einer [Schraffur](TechDraw_Hatch/de.md) geschnitten wurde.
    -   *PatSchraffur*: Schraffiert den Schnitt des Abschnitts mit einer [geometrischenSchraffur](TechDraw_GeometricHatch/de.md)

-    {{PropertyData/de|Datei Schraffurmuster}}: Vollständiger Pfad zur SVG Schraffurmusterdatei.

-    {{PropertyData/de|Datei Geomuster}}: Vollständiger Pfad zur PAT-Musterdatei.

-    {{PropertyData/de|Svg eingeschlossen}}: Vollständiger Pfad zur enthaltenen SVG-Schraffurmusterdatei.

-    {{PropertyData/de|Pat eingeschlossen}}: Vollständiger Pfad zur enthaltenen PAT Musterdatei.

-    {{PropertyData/de|Name Geomuster}}: Name des zu verwendenden PAT Musters (wird bei der *SvgSchraffur* Einstellung von **Schneide Oberflächen Anzeige** ignoriert).

### Ansicht

#### Cut Surface 

-    **Schneide Oberflächen Farbe**: Einfarbig für Oberflächenhervorhebung. Wird verwendet, wenn **Schnittoberflächenanzeige** auf *Farbe* eingestellt ist.

#### Oberflächen Schraffur 

-    **Schraffurfarbe**: Farbe für Oberflächenschraffurlinien.

-    **Weight Pattern**: Linienstärke für Oberflächenschraffurlinien.

### Grundansicht

Eine Schnittansicht erbt alle anwendbaren Eigenschaften der Ansicht, die als {**BaseView**} angegeben ist. In den Eigenschaften der Ansicht kannst du das Aussehen der Schnittlinie ändern:

-    **Schnitt Linienfarbe**: Farbe der Schnittlinie.

-    **Schnitt Linienstil**: Stil der Schnittlinie.

Die Standardeinstellungen für diese Parameter werden über die Einstellungen **Schnittlinie** und **Schnittlinienstil** in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) eingestellt.

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Neue Abschnittswerkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus mit den folgenden Funktionen verwendet werden:


```python
view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart','View')
rc = page.addView(view)
view.Source = box
view.Direction = (0.0,0.0,1.0)

section = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewSection','Section')
rc = page.addView(section)
section.Source = box
section.BaseView = view
section.Direction = (0.0,1.0,0.0)
section.SectionNormal = (0.0,0.0,1.0)
section.SectionOrigin = (5.0,5.0,5.0)
```

## Hinweise

-   **Schnittlinienformat**: sowohl das herkömmliche Schnittlinienformat (wie oben abgebildet) als auch die \"Referenzpfeil Methode\" werden unterstützt. Diese Option wird durch die Voreinstellung \"Mod/TechDraw/Format/SectionFormat\" gesteuert (siehe [Std\_DlgParameter](Std_DlgParameter/de.md)). 0 für die herkömmliche Linienmethode, 1 für die Referenzpfeilmethode.
-   **SchneideOberflächeAnzeige**: die Schnittfläche kann ausgeblendet, in einer Volltonfarbe gemalt, mit einem Svg Muster (Standard) schraffiert oder mit einem PAT Muster schraffiert werden. Siehe [Schraffur](TechDraw_Hatching/de.md).
-   **VerschmelzenVorSchneiden**: Die Querschnittsoperation kann manchmal die Ausgangsformen nicht schneiden. Wenn VerschmelzenVorSchneiden wahr ist, werden die Ausgangsformen zu einer einzigen Form zusammengeführt, bevor die Schnittoperation versucht wird. Wenn du Probleme mit der Abschnittsoperation hast, versuche, diesen Wert umzudrehen.





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SectionView/de
