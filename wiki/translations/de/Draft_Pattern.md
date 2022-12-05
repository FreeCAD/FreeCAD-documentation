# Draft Pattern/de
{{TOCright}}

## Beschreibung

[Draft](Draft_Workbench/de.md)-Objekte mit einer {{PropertyData/de|Make Face}} können ein SVG-muster anstelle einer einfarbigen Fläche anzeigen.

![](images/DraftPatternSample.png ) 
*Eine Ellipse und ein Vieleck mit einem SVG-Muster*

## Anwendung

1.  Stelle sicher, dass die Objekte geschlossen und planar sind und sich nicht selbst schneiden.
2.  Um einen [Entwurf Draht](Draft_Wire/de.md), einen [Entwurf BSpline](Draft_BSpline/de.md), eine [Entwurf KubischeBezKurve](Draft_CubicBezCurve/de.md) oder eine [Entwurf BezKurve](Draft_BezCurve/de.md) zu schließen, setze deren **Geschlossen** Eigenschaft auf `True`.
3.  Um einen [Entwurf Kreis](Draft_Circle/de.md) oder eine [Entwurf Ellipse](Draft_Ellipse/de.md) zu schließen, setze die Eigenschaften **Erster Winkel** und **Letzter Winkel** auf denselben Wert.
4.  Wähle die Objekte aus.
5.  Wechsle auf den Reiter **Ansicht** des [Eigenschateneditors](Property_editor/de.md).
6.  Der **Anzeigemodus** muss auf {{Value|Flache Linien}} eingestellt sein.
7.  Wähle ein **Muster**.
8.  Ändere optional die **Mustergröße**. Beachte, dass ein höherer Wert zu einem dichteren Muster führt.
9.  Das Muster wird nicht angezeigt, wenn die Objekte ausgewählt sind. Hebe die Auswahl der Objekte auf, um das Ergebnis zu überprüfen.
10. Wähle optional die Objekte erneut aus, um die Mustereigenschaften zu ändern.

## Verfügbare Muster 

Image:Aluminium.svg\|aluminium Image:Brick01.svg\|brick01 Image:Concrete.svg\|concrete Image:Cross.svg\|cross Image:Cuprous.svg\|cuprous Image:Diagonal1.svg\|diagonal1 Image:Diagonal2.svg\|diagonal2 Image:Earth.svg\|earth Image:General_steel.svg\|general_steel Image:Glass.svg\|glass Image:Hatch45L.svg\|hatch45L Image:Hatch45R.svg\|hatch45R Image:Hbone.svg\|hbone Image:Line.svg\|line Image:Plastic.svg\|plastic Image:Plus.svg\|plus Image:Simple.svg\|simple Image:Solid.svg\|solid Image:Square.svg\|square Image:Steel.svg\|steel Image:Titanium.svg\|titanium Image:Wood.svg\|wood Image:Woodgrain.svg\|woodgrain Image:Zinc.svg\|zinc

## Hinweise

-   SVG-Muster werden in **.SVG**-Dateien gespeichert. Es ist möglich, eigene Muster zu verwenden. Siehe [Einstellungen](#Einstellungen.md).
-   Die Muster selbst werden nicht im FreeCAD-Dokument gespeichert. Objekte, deren {{PropertyView/de|Muster}} nicht gefunden werden, werden stattdessen mit einer einfarbigen Fläche dargestellt.

## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Um ein Verzeichnis mit zusätzlichen SVG-Mustern anzugeben: **Bearbeiten → Einstellungen... → Entwurf → Visuelle Einstellungen → Ablageort alternativer SVG-Muster**. Wähle eine Datei im Verzeichnis aus und entferne dann den Dateinamen im Eingabefeld für die Einstellungen, so dass nur der Pfad übrig bleibt. Nach dem Ändern dieser Voreinstellung musst du FreeCAD neu starten.
-   Der Menüeintrag **Bearbeiten → Einstellungen... → Entwurf → Visuelle Einstellungen →  Auflösung des SVG-Musters** wird nicht verwendet.
-   um die {{PropertyView/de|Pattern Size}}, die für neue Objekte verwendet wird zu ändern: **Bearbeiten → Einstellungen... → Entwurf → Visuelle Einstellungen → Standardgröße des SVG-Musters**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Pattern/de
