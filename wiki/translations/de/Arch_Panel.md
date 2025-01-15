---
 GuiCommand:
   Name: Arch Panel
   Name/de: Arch Panel
   MenuLocation: 3D/BIM , Panel<br>Utils , Plattenwerkzeuge , Platte
   Workbenches: BIM_Workbench/de
   Shortcut: **P** **A**
   Version: 0.15
   SeeAlso: Arch_Panel_Cut/de, Arch_Panel_Sheet/de
---

# Arch Panel/de



## Beschreibung

Das Werkzeug **Arch Platte** ermöglicht alle Arten von plattenartigen Elementen zu erstellen, typischerweise für Plattenkonstruktionen wie das [WikiHouse](http://www.wikihouse.cc/)-Projekt, aber auch für alle Arten von Objekten, die auf einem ebenen Profil basieren.

<img alt="" src=images/Arch_Panel_example.jpg  style="width:700px;">

*Das obige Bild zeigt eine Reihe von Plattenobjekten, die einfach aus importierten 2D-Konturen aus einer DXF-Datei erstellt wurden. Sie können dann gedreht und zusammengesetzt werden, um Strukturen zu erzeugen.*

Seit {{VersionPlus/de|0.17}} kann Arch Platte auch zur Erstellung von gewellten oder trapezförmigen Profilen verwendet werden:

<img alt="" src=images/Arch_panel_wave.jpg  style="width:700px;">



## Anwendung

1.  Eine 2D-Form auswählen (Draft-Objekt, Fläche oder Skizze) - optional
2.  Die Schaltfläche **<img src="images/Arch_Panel.svg" width=16px>[Platte](Arch_Panel/de.md)** drücken oder das Tastaturkürzel **P** dann **A**.
3.  Die gewünschten Eigenschaften anpassen.



### Begrenzungen

-   Es gibt derzeit kein automatisches System zur Herstellung von 2D-Schnittbögen aus Plattenobjekten, aber eine solche Funktion ist in Planung enthalten und wird in Zukunft hinzugefügt werden.



## Optionen

-   Platten teilen die gemeinsamen Eigenschaften und Verhaltensweisen aller [Arch Komponenten](Arch_Component/de.md).

-   Die Wandstärke einer Platte kann nach der Erstellung angepasst werden.

-    **Esc**oder die Schaltfläche **Cancel** drücken, um den aktuellen Befehl abzubrechen.

-   Nach ihrer Erstellung kann durch Doppelklicken auf die Platte in der Baumansicht in den Bearbeitungsmodus gewechselt werden und so auf ihre Ergänzungen und Subtraktionen zugegriffen werden, um diese zu ändern.

-   Es ist möglich, automatisch Platten zu erstellen, die aus mehr als einer Lage eines Materials zusammengesetzt sind, indem man den Wert ihrer Eigenschaft Sheets erhöht.

-   Platten können <img alt="" src=images/Arch_MultiMaterial.svg  style="width:24px;"> [Mehrfachmaterial](Arch_MultiMaterial/de.md) in Anspruch nehmen. Wenn ein Mehrfachmaterial verwendet wird, wird die Platte mehrschichtig, wobei die durch das Mehrfachmaterial vorgegebenen Dicken verwendet werden. Bei jeder Schicht mit einer Dicke von Null wird die Dicke automatisch durch den verbleibenden Raum definiert, der durch den eigenen Dickenwert der Tafel definiert ist, nachdem die anderen Schichten abgezogen wurden.



## Eigenschaften

-    **Länge**: Die Länge der Platte

-    **Breite**: Die Breite der Platte

-    **Dicke**: Die Dicke der Platte

-    **Bereich**: Der Bereich des Panels (automatisch)

-    **Bleche**: Die Anzahl der Bleche des Materials, aus dem die Tafel besteht

-    **Wellenlänge**: Die Länge der Welle für Wellplatten

-    **Wellenhöhe**: Die Höhe der Welle für Wellplatten

-    **Wellentyp**: Die Art der Welle für gewellte Platten, gebogen, trapezförmig oder mit Stacheln

-    **Wellenrichtung**: Die Orientierung der Wellen für gewellte Platten

-    **Untere Welle**: Wenn die untere Welle der Tafel flach ist oder nicht



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Platte kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit der folgenden Funktion verwendet werden:


```python
Panel = makePanel(baseobj=None, length=0, width=0, thickness=0, placement=None, name="Panel")
```

-   Erstellt ein `Panel` Objekt aus dem gegebenen `baseobj`, das ein geschlossenes Profil ist, und der gegebenen Extrusion `thickness`.
    -   Wenn kein `baseobj` gegeben ist, kannst du die numerischen Werte für `length`, `width`, und `thickness` angeben, um ein Blocktafel zu erstellen.
-   Wenn ein `placement` gegeben wird, wird es verwendet.

Beispiel:


```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(1000, 400)
Panel = Arch.makePanel(Rect, thickness=36)
```



## Tutorien

-   [Wikihouse Portierungs Tutorium](Wikihouse_porting_tutorial/de.md)



---
⏵ [documentation index](../README.md) > Arch Panel/de
