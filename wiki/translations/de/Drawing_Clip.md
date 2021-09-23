# Drawing Clip/de
---
- GuiCommand:/de   Name/de:Drawing Ausschnitt   Workbenches:[[Drawing Workbench/de   Drawing]], Complete|MenuLocation:Drawing → Ausschnitt   Shortcut:-   SeeAlso:----


**Die Entwicklung des Drawing-Moduls wurde gestoppt und ein neuer in v0.17 eingeführter [TechDraw-Arbeitsbereich](TechDraw_Workbench/de.md) zielt darauf, es zu setzen. Beide Module stehen in v0.17 zur Verfügung, aber das Drawing-Modul könnte in zukünftigen Ausgaben entfernt werden.**

## Beschreibung

Dieser Befehl erlaubt, ein beschneidendes Rechteck auf einer [Zeichnungsseite](Drawing_Landscape_A3/de.md) zu platzieren. [Zeichnungsansicht](Drawing_View/de.md)-Objekte können dann zu diesem Rechteck hinzugefügt werden und ihre Ansicht wird durch die Ränder des Rechtecks beschnitten.

## Anwendung

1.  Erstelle eine [Zeichnungsseite](Drawing_Landscape_A3/de.md)
2.  [Aktualisiere](Std_Refresh.md) die Ansicht, falls keine Zeichnungsansicht geöffnet war
3.  Drücke den **<img src="images/Drawing_Clip.png" width=16px> [Zeichnung Ausschnitt](Drawing_Clip/de.md)**-Button
4.  Passe die gewünschten Eigenschaften an, wie Größe und Position.
5.  Ziehe die [Zeichnungsansicht](Drawing_View/de.md)-Objekte auf das Ausschnittsobjekt in der Baumansicht und lasse sie dort fallen (drag & drop)

## Optionen

-   Eine Eigenschaft erlaubt das Anzeigen oder Verstecken des beschneidenden Rechtecks selbst.

## Einschränkungen

-   Beschneidende Objekte werden nicht sauber durch den internen Qt-basierten Svg-Viewer angezeigt, aber der [Open Browser](Drawing_Openbrowser/de.md)-Befehl zeigt sie korrekt.


{{docnav/de
|[Anmerkung](Drawing_Annotation/de.md)
|[Browser-Ansicht öffnen](Drawing_Openbrowser/de.md)
|[Drawing-Arbeitsbereich](Drawing_Workbench/de.md)
|IconL=Drawing_Annotation.png
|IconC=Workbench_Drawing.svg
|IconR=Drawing_Openbrowser.png
}}


{{Drawing Tools navi

}}

---
[documentation index](../README.md) > [Drawing](Drawing_Workbench.md) > Drawing Clip/de
