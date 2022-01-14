---
- GuiCommand:/de
   Name:Arch Site
   Name/de:Arch Baustelle
   Workbenches:[Arch](Arch_Workbench/de.md)
   MenuLocation:Architektur → Baustelle
   Shortcut:**S** **I**
   SeeAlso:[Arch Etage](Arch_Floor/de.md), [Arch Gebäude](Arch_Building/de.md)
---

# Arch Site/de

## Beschreibung

Der Arch Baustelle ist ein spezielles Objekt, das Eigenschaften eines Standard FreeCAD Gruppenobjekts und Arch Objekten kombiniert. Es ist besonders zur Repräsentation einer gesamten Projektfläche bzw. eines Terrains geeignet. In IFC-basierter architektonischer Arbeit dient es der Organisation deines CAD Modells und enthält [Gebäude](Arch_Building/de.md) Objekte. Die Baustelle wird auch verwendet, um vorhandenes Gelände zu verwalten und anzuzeigen und kann benutzt werden, um das Volumen von aufzufüllender oder abzutragender Erde zu berechnen.

## Anwendung

1.  Wähle wahlweise ein oder mehrere Objekte, welche in deine neue Baustelle übernommen werden sollen.
2.  Drücke die **<img src="images/Arch_Site.svg" width=16px> [Baustelle](Arch_Site/de.md)** Schaltfläche oder drücke **S**, dann **I** Tasten.

## Optionen

-   Nachdem du einen Standort erstellt hast, kannst du ihm weitere Objekte hinzufügen, indem du sie per Ziehen & Loslassen in der Baumansicht oder unter Verwendung des **<img src="images/Arch_Add.svg" width=16px> [Arch Hinzufügen](Arch_Add/de.md)** Werkzeugs. Dies bestimmt nur, welches Objekt Teil des gegebenen Standorts ist, und hat keinen Einfluss auf das Gelände selbst.
-   Du kannst Objekte von einem Standort entfernen, indem du sie per Ziehen & Loslassen aus der Baumansicht herausziehst oder durch Verwendung des **<img src="images/Arch_Remove.svg" width=16px> [Arch Entfernen](Arch_Remove/de.md)** Werkzeugs
-   Du kannst ein Geländeobjekt hinzufügen, indem du die **Gelände** Eigenschaft des Standorts bearbeitest. Das Gelände muss eine offene Hülle oder Oberfläche sein.
-   Du kannst Volumina hinzufügen, die zum Basisgelände hinzugefügt oder vom Basisgelände subtrahiert werden sollen, indem du auf den Standort doppelklickst und Objekte zu ihren Subtraktions- oder Additionsgruppen hinzufügst. Die Objekte müssen Volumenkörper sein.
-   Die {{PropertyData/de|Extrusionsvektor}} Eigenschaft kann verwendet werden, um einige Probleme zu lösen, die bei der Arbeit mit Subtraktionen und Additionen auftreten können. Um diese Additionen/Subtraktionen durchzuführen, wird die Geländeoberfläche in einen Körper extrudiert, der dann entsprechend vereinigt/subtrahiert wird. Abhängig von der Geländetopologie kann diese Extrusion mit dem Standard Extrusionsvektor fehlschlagen. Daher kannst du das Problem möglicherweise beheben, indem du diesen auf einen anderen Wert änderst.

## Eigenschaften

### Daten

-    **Gelände**: Das Basisgelände dieses Baustelle

-    **Addresse**: Die Straße und Hausnummer dieser Baustelle.

-    **Postanschrift**: Die Postanschrift oder Postleitzahl dieser Baustelle

-    **Stadt**: Die Stadt dieser Baustelle

-    **Land**: Das Land dieser Baustelle

-    **Breitengrad**: Der Breitengrad dieser Baustelle

-    **Längengrad**: Der Längengrad dieser Baustelle

-    **Url**: Eine Url, die diese Baustelle auf einer Kartierungs Webseite zeigt

-    **Projizierte Fläche**: Die Fläche der Projektion dieses Objekts auf die XY Ebene

-    **Umfang**: Die Umfangslänge dieses Geländes

-    **Additionsvolumen**: Das diesem Gelände hinzuzufügende Erdvolumen

-    **Subtraktionsvolumen**: Das Erdvolumen, das von diesem Gelände entfernt werden soll

-    **Extrusionsvektor**: Ein Extrusionsvektor zur Verwendung bei der Durchführung boolescher Operationen

-    **Splitter entfernen**: Splitter aus der resultierenden Form entfernen

-    **Deklination**: Der Winkel zwischen dem wahren Norden und der Nordrichtung in diesem Dokument, d.h. die Y Achse. <small>(v0.18)</small>  Das bedeutet, dass standardmäßig Norden auf die Y Achse und Osten auf die X Achse zeigt; der Winkel wird gegen den Uhrzeigersinn schrittweise erhöht. Diese Eigenschaft war früher als **Nord Abweichung** bekannt.

-    **EPW Datei**: Erlaube das Anhängen einer EPW Datei von der [Ladybug EPW Daten Webseite](https://www.ladybug.tools/epwmap/) an diese Baustelle. Dies wird benötigt, um Windrosendiagramme anzuzeigen. <small>(v0.19)</small> 

### Ansicht

-    **Solardiagram**: Zeigt das Solardiagramm an oder blendet es aus

-    **Solardiagram Farbe**: Die Farbe des Solardiagramms

-    **Solardiagram Position**: Die Position des Solardiagramms.

-    **Solardiagram Maßstab**: Der Maßstab des Solardiagramms.

-    **Windrose**: Zeigt das Windrosendiagramm an oder blendet es aus (erfordert die **EPW Datei** Dateneigenschaft ausgefüllt und das Ladybug Python Modul installiert (siehe unten)

## Typischer Arbeitsablauf 

Beginne damit, ein Objekt zu erstellen, das dein Gelände repräsentiert. Es muss eine offene Fläche sein, kein Festkörper. Es ist z.B. einfach, Netzdaten zu importieren, die über das Menü {{MenuCommand/de|Teil → Form aus Netz erstellen}} in eine Teilform umgewandelt werden können. Erstelle dann ein Baustellenobjekt, und setze dessen Eigenschaft {{PropertyData/de|Gelände}} auf das gerade erstellte Teil:

![](images/Arch_site_example_01.jpg )

Erstelle einige Volumina (sie müssen Festkörper sein), die die Bereiche repräsentieren, die ausgegraben oder gefüllt werden sollen. Doppelklicke in der Baumansicht auf das Baustellenobjekt und füge diese Volumina zu den Additions- oder Subtraktionsgruppen hinzu. Klicke auf OK.

![](images/Arch_site_example_02.jpg )

Die Baustellengeometrie wird neu berechnet und die Flächen, der Umfang und die Volumeneigenschaften werden neu berechnet.

![](images/Arch_site_example_03.jpg )

## Solar- und Winddiagramme 

Wenn [Ladybug](https://www.ladybug.tools/ladybug.html) auf deinem System installiert ist, kann [Arch Standort](Arch_Site/de.md) ein Solardiagramm und/oder eine Windrose anzeigen. Dazu werden **Längengrad**, **Breitengrad** und **Deklination** (previously **Nordabweichung**) müssen korrekt eingestellt und **Solardiagramm** oder **Windrose** auf `True` gesetzt sein. Betrifft <small>(v0.17)</small>  und <small>(v0.19)</small> 

**Hinweis**: Wenn du keinen Ladybug hast, wird [pysolar](http://pysolar.org/) immer noch unterstützt, um Solardiagramme zu erstellen, aber keine Windrosen. Pysolar 0.7 oder höher ist erforderlich; diese Version funktioniert nur mit Python 3. Wenn du diese Funktion mit Python 2 benötigst, solltest du Pysolar 0.6 haben, da dies die letzte Version ist, die mit Python 2 funktioniert. Allerdings ist Ladybug ein weitaus leistungsfähigeres Werkzeug, das in Zukunft wahrscheinlich häufiger verwendet werden wird, so dass wir empfehlen, es anstelle von Pysolar zu verwenden. Ladybug kann einfach über [pip](https://github.com/ladybug-tools/ladybug) installiert werden.

![](images/Freecad-solar-diagram.jpg )

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Baustellenwerkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole aus mit folgender Funktion verwendet werden:


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

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Site/de
