# TechDraw Templates/de
{{TOCright}}

## Überblick

Jede TechDraw Seite basiert auf einem Vorlagenobjekt. Die Vorlage steuert die Papiergröße und enthält feste Textgrafiken und Text, z.B. einen Seitenrahmen oder eine Umrandung.

Die Vorlage kann auch änderbare Textfelder für Attribute wie *Titel*, *Untertitel*, *Autor*, *Datum*, *Maßstab*, \'\'Gewicht\", *Zeichnungsnummer* und *Blatt*.

Die Vorlagen sind [SVG](SVG.md)-Dateien, die außerhalb von FreeCAD erstellt und geändert werden können, mit einer Anwendung wie [Inkscape](https   *//de.wikipedia.org/wiki/Inkscape).

## Eigenschaften

-    **Orientierung**   * Hoch- oder Querformat

-    **Breite**   * Papierbreite in mm

-    **Höhe**   * Papierhöhe in mm

-    **Seitenergebnis**   * Eine Kopie der originalen Vorlagendatei einschließlich aller Änderungen bearbeitbarer Texte. Dies erlaubt Anwendern, die möglicherweise keine Kopie der Vorlagendatei haben, die Seite wie vorgesehen anzuzeigen. Für Endbenutzer in der Regel nicht nützlich.

-    **Vorlage**   * Eine Referenz auf die Kopie der ursprünglichen Vorlagendatei, die in dieser \*.FCSTD Datei eingebunden ist. Außerdem kann hier ein Dateipfad zu einem Vorlagenordner ausgewählt werden. Dazu auf das Dateiauswahl-Zeichen **\[\...\]** klicken, um zu einer anderen Vorlage zu wechseln.

## Ändern der Vorlagendatei 

Um die Vorlage einer Zeichnung zu ändern

1.  klicke die gewünschte Seite im Baum an
2.  wenn nicht bereits geöffnet, sollte der Baum einen kleinen Unterbaum mit mehreren Blättern öffnen
3.  Wähle das Vorlagenblatt aus
4.  in der Eigenschaftsleiste/Datenreiter/Vorlage ist der Pfad zur Vorlagendatei. Um die Datei zu ändern, drücke die Ellipsentaste (\'\...\'). Dadurch wird dein Standardvorlagenordner (wie in Einstellungen/TechDraw eingestellt) geöffnet.
5.  wähle eine andere Vorlagendatei.

Die neue Datei wird direkt geöffnet.

Wenn du eine geänderte Vorlagendatei aktualisieren möchtest, beachte, dass du eine andere Datei laden musst, bevor du die gleiche Datei erneut auswählen kannst. Dies liegt daran, dass die Auswahl der gleichen Datei ignoriert wird.

## Benutzerdefinierte Vorlagen 

Eine begrenzte Anzahl vorformatierter Vorlagen in verschiedenen Standardseitengrößen sind in FreeCAD enthalten. Diese sind zu finden in


```python
$INSTALL_DIR/Mod/TechDraw/Templates/
```

wobei `$INSTALL_DIR` das Verzeichnis ist, wo FreeCAD installiert wurde, z.B.


```python
/usr/share/freecad/Mod/TechDraw/Templates/
```

Benutzerdefinierte Vorlagen können auch als Standard in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) festgelegt werden.

Siehe auch [So wird eine benutzerdefinierte TechDraw Vorlage erstellt](TechDraw_TemplateHowTo/de.md)

## Hinweise

-   TechDraw-Vorlagen sind nicht vollständig austauschbar mit [Drawing Templates](Drawing_templates.md).
-   Im allgemeinen funktionieren die Zeichnungsvorlagen in TechDraw, es können jedoch Probleme mit bearbeitbaren Texten auftreten.

-   Svg Transformationsklauseln **werden Probleme verursachen** in benutzerdefinierten Vorlagen. Siehe eine Stackoverflow Diskussion auf [Entfernen von Transformationsklauseln in SVG Dateien](https   *//stackoverflow.com/questions/13329125/removing-transforms-in-svg-files).

-   Die **xml   *space=\"preserve\"** Klausel verursacht manchmal Probleme mit der Textgröße und -positionierung. Es ist am besten, diese Klausel aus dem SVG Code Ihrer benutzerdefinierten Vorlage zu vermeiden/entfernen.

-   Vorlagen funktionieren am besten, wenn sie keinen überflüssigen SVG Code enthalten (von manchen als \"Müll SVG\" bezeichnet). Es gibt einen guten Artikel über [Entfernen von Müll aus SVG hier](https   *//freecad-gost.ru/news/gost-templates-techdraw-09-01-2020/). Der Artikel ist auf Russisch.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Templates/de
