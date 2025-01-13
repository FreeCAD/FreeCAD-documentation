---
 GuiCommand:
   Name: Arch Site
   Name/de: Arch Grundstück
   MenuLocation: 3D/BIM , Grundstück
   Workbenches: BIM_Workbench/de
   Shortcut: **S** **I**
   SeeAlso: 
---

# Arch Site/de



## Beschreibung

Das **Arch Grundstück** ist ein spezielles Objekt, das Eigenschaften eines normalen FreeCAD-Gruppenobjekts mit denen von Arch-Objekten kombiniert. Es ist besonders zur Darstellung einer gesamten Projektfläche bzw. eines Geländes geeignet. In IFC-basierter architektonischer Arbeit dient es der Organisation des CAD-Modells und enthält [Gebäude](Arch_Building/de.md) (Building-Objekte). Das Grundstück wird auch verwendet, um vorhandenes Gelände zu verwalten und anzuzeigen und kann benutzt werden, um das Volumen von aufzufüllender oder abzutragender Erde zu berechnen.



## Anwendung

1.  Wahlweise ein oder mehrere Objekte auswählen, die in eine neues Grundstück übernommen werden sollen.
2.  Die Schaltfläche **<img src="images/Arch_Site.svg" width=16px> [Grundstück](Arch_Site/de.md)** drücken oder das Tastaturkürzel **S** dann **I** verwenden.



## Optionen

-   Nachdem ein Grundstück erstellt wurde, können ihm Objekte hinzugefügt werden, durch Ziehen und Ablegen in der [Baumansicht](Tree_view/de.md) oder durch Verwenden des Werkzeugs **<img src="images/Arch_Add.svg" width=16px> [Arch Hinzufügen](Arch_Add/de.md)**. Dies bestimmt nur, welche Objekte Teil des gegebenen Grundstücks sind, und hat keinen Einfluss auf das Gelände selbst.
-   Objekte können von einem Grundstück entfernt werden, indem sie durch Ziehen & Ablegen in der [Baumansicht](Tree_view/de.md) herausgezogen werden oder durch Verwenden des Werkzeugs **<img src="images/Arch_Remove.svg" width=16px> [Arch Entfernen](Arch_Remove/de.md)**.
-   Ein Geländeobjekt (Terrain-Objekt) kann hinzugefügt werden, indem die {{PropertyData/de|Gelände}} des Grundstücks bearbeitet wird. Das Gelände kann eine offene Hülle (Shell) sein oder ({{Version/de|0.21}}) ein Festkörper.
-   Du kannst Volumenkörper hinzufügen, die zum Basisgelände hinzugefügt oder vom Basisgelände subtrahiert werden sollen, indem du auf das Grundstück doppelklickst und Objekte zu ihren Gruppen Ergänzungen oder Subtraktionen hinzufügst. Die Objekte müssen Festkörper sein.
-   Die {{PropertyData/de|Extrusionsvektor}} kann verwendet werden, wenn das Gelände eine offene Hülle ist und/oder Ergänzugen und Subtraktionen vorhanden sind. Um diese Ergänzugen bzw. Subtraktionen durchzuführen, wird die offene Hülle zu einem Körper extrudiert, der dann entsprechend vereinigt bzw. beschnitten wird. Abhängig von der Geländetopologie kann diese Extrusion mit dem Standard Extrusionsvektor fehlschlagen. Dann kann das Problem möglicherweise behoben werden, indem dieser auf einen anderen Wert geändert wird. Diese Eigenschaft wird ignoriert, wenn das Gelände ein Festkörper ist.



## Eigenschaften



### Daten

-    {{PropertyData/de|Gelände}}: Das Basisgelände dieses Grundstücks.

-    {{PropertyData/de|Addresse}}: Die Straße und Hausnummer dieses Grundstücks.

-    {{PropertyData/de|Postanschrift}}: Die Postanschrift oder Postleitzahl dieses Grundstücks.

-    {{PropertyData/de|Stadt}}: Die Stadt dieses Grundstücks.

-    {{PropertyData/de|Land}}: Das Land dieses Grundstücks.

-    {{PropertyData/de|Breitengrad}}: Der Breitengrad dieses Grundstücks.

-    {{PropertyData/de|Längengrad}}: Der Längengrad dieses Grundstücks.

-    {{PropertyData/de|Url}}: Eine Url, die dieses Grundstück auf einer Kartierungs-Webseite zeigt.

-    {{PropertyData/de|Projizierte Fläche}}: Die Fläche der Projektion dieses Objekts auf die XY-Ebene

-    {{PropertyData/de|Umfang}}: Die Umfangslänge dieses Geländes.

-    {{PropertyData/de|Additionsvolumen}}: Das diesem Gelände hinzuzufügende Erdvolumen.

-    {{PropertyData/de|Subtraktionsvolumen}}: Das Erdvolumen, das von diesem Gelände entfernt werden soll.

-    {{PropertyData/de|Extrusionsvektor}}: Ein Extrusionsvektor zur Verwendung bei der Durchführung boolescher Verknüpfungen.

-    {{PropertyData/de|Splitter entfernen}}: Splitter aus der resultierenden Form entfernen.

-    {{PropertyData/de|Deklination}}: Der Winkel zwischen dem wahren Norden und der Nordrichtung in diesem Dokument, d.h. die Y-Achse. Das bedeutet, dass standardmäßig Norden auf die Y-Achse und Osten auf die X-Achse zeigt; der Winkel wird gegen den Uhrzeigersinn schrittweise erhöht. Diese Eigenschaft war früher als {{PropertyData/de|Nord-Abweichung}} bekannt.

-    {{PropertyData/de|EPW-Datei}}: Ermöglicht das Anhängen einer EPW-Datei von der [Ladybug EPW-Daten-Webseite](https://www.ladybug.tools/epwmap/) an dieses Grundstück. Dies wird benötigt, um Windrosendiagramme anzuzeigen.



### Ansicht

-    {{PropertyView/de|Solardiagram}}: Zeigt das Solardiagramm an oder blendet es aus

-    {{PropertyView/de|Solardiagram Farbe}}: Die Farbe des Solardiagramms

-    {{PropertyView/de|Solardiagram Position}}: Die Position des Solardiagramms.

-    {{PropertyView/de|Solardiagram Maßstab}}: Der Maßstab des Solardiagramms.

-    {{PropertyView/de|Windrose}}: Zeigt das Windrosendiagramm an oder blendet es aus (erfordert, dass die Dateneigenschaft **EPW-Datei** ausgefüllt und das Python-Modul Ladybug installiert ist. (siehe unten)



## Typischer Arbeitsablauf 

Man beginnt damit, ein Objekt zu erstellen, das das Gelände repräsentiert. Es können z.B. einfach Netzdaten importiert werden, die mit dem Menüeintrag **Part → Form aus Netz erstellen** in eine Part-Form umgewandelt werden können. Dann wird ein Grundstück (Site-Objekt) erstellt, und dessen {{PropertyData/de|Gelände}} auf die gerade erstellte Part-Form gesetzt:

![](images/Arch_site_example_01.jpg )

Erstelle einige Volumina (sie müssen Festkörper sein), die die Bereiche repräsentieren, die ausgegraben oder gefüllt werden sollen. Doppelklicke in der Baumansicht auf das Baustellenobjekt und füge diese Volumina zu den Additions- oder Subtraktionsgruppen hinzu. Klicke auf OK.

![](images/Arch_site_example_02.jpg )

Die Baustellengeometrie wird neu berechnet und die Flächen, der Umfang und die Volumeneigenschaften werden neu berechnet.

![](images/Arch_site_example_03.jpg )



## Solar- und Winddiagramme 

Wenn [Ladybug](https://www.ladybug.tools/ladybug.html) auf deinem System installiert ist, kann [Arch Grundstück](Arch_Site/de.md) ein Solardiagramm und/oder eine Windrose anzeigen. Hierfür müssen {{PropertyData/de|Längengrad}}, {{PropertyData/de|Breitengrad}} und {{PropertyData/de|Deklination}} (previously {{PropertyData/de|Nordabweichung}}) korrekt eingestellt und {{PropertyView/de|Solardiagramm}} oder {{PropertyView/de|Windrose}} auf `True` gesetzt sein.

**Hinweis**: Wenn du kein Ladybug hast, wird [pysolar](http://pysolar.org/) immer noch unterstützt, um Solardiagramme zu erstellen, aber keine Windrosen. Pysolar 0.7 oder höher ist erforderlich. Allerdings ist Ladybug ein weitaus leistungsfähigeres Werkzeug, das in Zukunft wahrscheinlich häufiger verwendet werden wird, so dass wir empfehlen, es anstelle von Pysolar zu verwenden. Ladybug kann einfach über [pip](https://github.com/ladybug-tools/ladybug) installiert werden.

![](images/Freecad-solar-diagram.jpg )



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Baustellenwerkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit der folgenden Funktion verwendet werden:


```python
Site = makeSite(objectslist=None, baseobj=None, name="Site")
```

-   Erstellt ein `Baustelle`n Objekt aus `Objekteliste`, die eine Liste von Objekten ist, oder `Basisobj`, das eine `Form` oder `Gelände`.

Beispiel: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Building = Arch.makeBuilding([Wall])
Site = Arch.makeSite([Building])

FreeCAD.ActiveDocument.recompute()
FreeCAD.Gui.ActiveDocument.ActiveView.viewIsometric()
```



### Solardiagramm

Solange das `pysolar` Modul vorhanden ist, kann dem Standort ein Solardiagramm hinzugefügt werden. Stelle den Längen- und Breitengrad und die Deklinationswinkel sowie einen für die Größe deines Modells geeigneten Maßstab ein.

Bitte beachte, dass Pysolar 0.7 oder höher erforderlich ist und diese Version nur mit Python 3 funktioniert.


```python
Site.Longitude = -46.38
Site.Latitude = -23.33
Site.Declination = 30
#Site.Compass = True

Site.ViewObject.SolarDiagram = True
Site.ViewObject.SolarDiagramScale = 10000
FreeCAD.ActiveDocument.recompute()
```



### Sonnendiagramm unabhängig von der Baustelle 

Ein Solardiagramm kann unabhängig von einem beliebigen Standort mit der folgenden Funktion erstellt werden. 
```python
Node = makeSolarDiagram(longitude, latitude, scale=1, complete=False)
```

-   Erstellt ein Solardiagramm als ein Pivy Knoten unter Verwendung von `Längengrad` und `Breitengrad`, mit einem optionalen `Maßstab`.
-   Wenn `vollständig` `True` ist, werden die 12 Monate gezeichnet, was das vollständige Solardiagramm zeigt [analemma](https://en.wikipedia.org/wiki/Analemma).


```python
import FreeCADGui, Arch

Node = Arch.makeSolarDiagram(-46.38, -23.33, scale=10000, complete=True)
FreeCAD.Gui.ActiveDocument.ActiveView.getSceneGraph().addChild(Node)
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Site/de
