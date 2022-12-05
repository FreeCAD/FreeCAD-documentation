# TechDraw Templates/de
{{TOCright}}

## Überblick

Jedes TechDraw-Zeichnungsblatt (Page-Objekt) basiert auf einer Vorlage (Template-Objekt). Die Vorlage steuert die Blattgröße und enthält unveränderliche grafische Elemente und Text, z.B. einen Zeichnugsrahmen oder eine Beschnittkante.

Die Vorlage kann auch editierbare Textfelder für Attribute wie *Titel*, *Untertitel*, *Autor*, *Datum*, *Maßstab*, *Gewicht\",*Zeichnungsnummer*und*Blatt\'\'.

Die Vorlagen sind [SVG](SVG.md)-Dateien, die außerhalb von FreeCAD mit einer Anwendung wie [Inkscape](https://de.wikipedia.org/wiki/Inkscape) erstellt und geändert werden können.

## Eigenschaften

-    **Orientation**: Hoch- oder Querformat

-    **Width**: Blattbreite in mm

-    **Height**: Blatthöhe in mm

-    **Page Result**: Eine Kopie der originalen Vorlagendatei einschließlich aller Änderungen an editierbaren Texten. Dies erlaubt Anwendern, die möglicherweise keine Kopie der Vorlagendatei haben, die Seite wie vorgesehen anzuzeigen. Für Endanwender in der Regel nicht nützlich.

-    **Template**: a) Ein Verweis auf die Kopie der ursprünglichen Vorlagendatei, die in dieser \*.FCStd Datei eingebunden ist. b) Ein Dateipfad zu einer auf dem aktuellen Rechner vorhandenen Vorlage. Auf das Dateiauswahl-Zeichen (\...) klicken, um zu einer anderen Vorlage zu wechseln.

## Eine andere Vorlagendatei auswählen 

Um eine andere Vorlage einer Zeichnung auszuwählen:

1.  Die gewünschte Seite in der [Baumansicht](Tree_view/de.md) ermitteln.
2.  Den Knoten des Zeichnungsblattes (Page-Objekt) aufklappen, wenn nötig.
3.  Die Vorlage (Template-Objekt) auswählen.
4.  Im [Eigenschafteneditor](Property_editor.md) in das Eingabefeld der {{PropertyData/de|Template}} klicken.
5.  Die Schaltfläche **...** (Ellipse) drücken, die erscheint.
6.  Ein Dateidialog öffnet das Verzeichnis, das die aktuelle Vorlage enthält. Wurde das Zeichnungsblatt in der laufenden FreeCAD-Sitzung erstellt, wird dies das Standard-Vorlagenverzeichnis sein (wie in den [TechDraw Einstellungen](TechDraw_Preferences/de#Dateien.md) gespeichert).
7.  Wahlweise zu einem anderen Verzeichnis wechseln.
8.  Eine andere Vorlagedatei auswählen.
9.  Die Schaltfläche **OK** drücken.

Wurde eine Vorlagendatei geändert und das dazugehörige Zeichnungsblatt, das in der aktuellen FreeCAD-Sitzung erstellt wurde, die diese Vorlage verwendet, soll aktualisiert werden, wählt man zuerst temporär eine andere Datei aus und dann wieder die geänderte Datei.

## Benutzerdefinierte Vorlagen 

Eine begrenzte Anzahl vorformatierter Vorlagen in verschiedenen Standardformaten (Blattgrößen) sind in FreeCAD enthalten. Diese sind zu finden in


```python
$INSTALL_DIR/Mod/TechDraw/Templates/
```

wobei `$INSTALL_DIR` das Verzeichnis ist, in dem FreeCAD installiert wurde, z.B.


```python
/usr/share/freecad/Mod/TechDraw/Templates/
```

Benutzerdefinierte Vorlagen können auch als Standard in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) festgelegt werden.

Siehe auch [So wird eine benutzerdefinierte TechDraw Vorlage erstellt](TechDraw_TemplateHowTo/de.md)

## Hinweise

-   TechDraw-Vorlagen sind nicht vollständig austauschbar mit [Drawing-Vorlagen](Drawing_templates/de.md).
-   Im allgemeinen funktionieren die Drawing-Vorlagen in TechDraw, es können jedoch Probleme mit editierbaren Texten auftreten.

-   Svg-Transformationsanweisungen **werden Probleme verursachen** in benutzerdefinierten Vorlagen. Siehe eine Stackoverflow-Diskussion unter [removing transform clauses in SVG files](https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files) (engl.).

-   Die Anweisung **xml:space=\"preserve\"** verursacht manchmal Probleme mit der Textgröße und -positionierung. Es ist am besten, diese Anweisung zu vermeiden bzw. aus dem SVG-Code der benutzerdefinierten Vorlage entfernen.

-   Vorlagen funktionieren am besten, wenn sie keinen überflüssigen SVG-Code enthalten (von manchen als \"SVG-Müll\" bezeichnet). Es gibt einen guten Artikel über [Entfernen von Müll aus SVG hier](https://freecad-gost.ru/news/gost-templates-techdraw-09-01-2020/). Der Artikel ist auf Russisch.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Templates/de
