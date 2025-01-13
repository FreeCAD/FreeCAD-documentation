# Draft Pattern/de
## Beschreibung

[Draft](Draft_Workbench/de.md)-Objekte mit einer {{PropertyData/de|Make Face}} können ein SVG-Schraffurmuster anstelle einer einfarbigen Fläche anzeigen.

![](images/DraftPatternSample.png ) 
*Eine Ellipse und ein Vieleck mit einem SVG-Schraffurmuster*



## Anwendung

1.  Sicherstellen, dass die Objekte geschlossen sowie eben sind und sich nicht selbst schneiden.
2.  Um einen [Draft-Linienzug](Draft_Wire/de.md), einen [Draft-B-Spline](Draft_BSpline/de.md), eine [Draft-KubischeBézierkurve](Draft_CubicBezCurve/de.md) oder eine [Draft-Bézierkurve](Draft_BezCurve/de.md) zu schließen, wird deren {{PropertyData/de|Closed}} auf `True` gesetzt.
3.  Um einen [Draft-Kreis](Draft_Circle/de.md) oder eine [Draft-Ellipse](Draft_Ellipse/de.md) zu schließen, werden ihre {{PropertyData/de|First Angle}} und ihre {{PropertyData/de|Last Angle}} auf denselben Wert gesetzt.
4.  Die Objekte auswählen.
5.  Auf den Reiter **Ansicht** des [Eigenschateneditors](Property_editor/de.md) wechseln.
6.  Die {{PropertyView/de|Display Mode}} muss auf {{Value|Flat Lines}} gesetzt sein.
7.  Ein Schraffurmuster der {{PropertyView/de|Pattern}} auswählen.
8.  Wahlweise die {{PropertyView/de|Pattern Size}} (Größe des Schrafurmusters) ändern. Man beachte, dass ein höherer Wert zu einem dichteren Muster führt.
9.  Das Schrafurmuster wird nicht angezeigt, wenn die Objekte ausgewählt sind. Die Auswahl der Objekte aufheben, um das Ergebnis zu überprüfen.
10. Wahlweise die Objekte erneut auswählen, um die Mustereigenschaften zu ändern.



## Verfügbare Muster 

Image:Aluminium.svg\|aluminium Image:Brick01.svg\|brick01 Image:Concrete.svg\|concrete Image:Cross.svg\|cross Image:Cuprous.svg\|cuprous Image:Diagonal1.svg\|diagonal1 Image:Diagonal2.svg\|diagonal2 Image:Earth.svg\|earth Image:General_steel.svg\|general_steel Image:Glass.svg\|glass Image:Hatch45L.svg\|hatch45L Image:Hatch45R.svg\|hatch45R Image:Hbone.svg\|hbone Image:Line.svg\|line Image:Plastic.svg\|plastic Image:Plus.svg\|plus Image:Simple.svg\|simple Image:Solid.svg\|solid Image:Square.svg\|square Image:Steel.svg\|steel Image:Titanium.svg\|titanium Image:Wood.svg\|wood Image:Woodgrain.svg\|woodgrain Image:Zinc.svg\|zinc



## Hinweise

-   SVG-Schraffurmuster werden in **.SVG**-Dateien gespeichert. Es ist möglich, eigene Muster zu verwenden. Siehe [Einstellungen](#Einstellungen.md).
-   Die Muster selbst werden nicht im FreeCAD-Dokument gespeichert. Objekte, deren {{PropertyView/de|Pattern}} nicht gefunden wird, werden stattdessen mit einer einfarbigen Fläche dargestellt.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   um die {{PropertyView/de|Pattern Size}}, die für neue Objekte verwendet wird, zu ändern: **Bearbeiten → Einstellungen... → Draft → Ansicht → SVG-Mustergröße**.
-   Um ein Verzeichnis mit zusätzlichen SVG-Mustern anzugeben: **Bearbeiten → Einstellungen... → Draft → Ansicht → Ablageort alternativer SVG-Muster**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Pattern/de
