---
- GuiCommand:
   Name: Arch Panel
   Name/de: Arch Platte
   MenuLocation: Arch - Panel tools - Platte
   Workbenches: [Arch](Arch_Workbench/de.md)
   Shortcut: **P** **A**
   Version: 0.15
   SeeAlso: [Arch Panel Cut](Arch_Panel_Cut/de.md), [Arch Panel Sheet](Arch_Panel_Sheet/de.md)
---

# Arch Panel/de


</div>

## Beschreibung

Mit diesem Werkzeug kannst du alle Arten von platten-artigen Elementen bauen, typischerweise für Plattenkonstruktionen wie das [WikiHouse](http://www.wikihouse.cc/) Projekt, aber auch für alle Arten von Objekten, die auf einem flachen Profil basieren.

<img alt="" src=images/Arch_Panel_example.jpg  style="width:700px;">

*Das obige Bild zeigt eine Reihe von Plattenobjekten, die einfach aus importierten 2D Konturen aus einer DXF Datei erstellt wurden. Sie können dann gedreht und zusammengesetzt werden, um Strukturen zu erzeugen.*

Seit Version <small>(v0.17)</small>  kann Arch Tafel auch zur Erstellung von gewellten oder trapezförmigen Profilen verwendet werden.

<img alt="" src=images/Arch_panel_wave.jpg  style="width:700px;">

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle eine 2D Form (Entwurfsobjekt, Fläche oder Skizze) - optional
2.  Drücke die **<img src="images/Arch_Structure.svg" width=16px>[Arch Tafel](Arch_Panel/de.md)** Schaltfläche oder die **P** und **A** Tasten.
3.  Passe die gewünschten Eigenschaften an.


</div>

### Begrenzungen

-   Es gibt derzeit kein automatisches System zur Herstellung von 2D Schnittplatten aus Plattenobjekten, aber eine solche Funktion ist in den Plänen enthalten und wird in Zukunft hinzugefügt werden.

## Optionen


<div class="mw-translate-fuzzy">

-   Tafeln teilen die gemeinsamen Eigenschaften und Verhaltensweisen aller [Arch Komponenten](Arch_Component/de.md).
-   Die Dicke einer Tafel kann nach der Erstellung angepasst werden.
-   Drücke **Esc** or the **Cancel** Schaltfläche, um den aktuellen Befehl abzubrechen.
-   Durch Doppelklicken auf die Tafel in der Baumansicht nach seiner Erstellung kannst du in den Bearbeitungsmodus wechseln und auf seine Additionen und Subtraktionen zugreifen und diese ändern.
-   Es ist möglich, automatisch Tafeln zu erstellen, die aus mehr als einem Blech eines Materials zusammengesetzt sind, indem man seine Blecheigenschaft erhöht.
-   Tafeln können <img alt="" src=images/Arch_MultiMaterial.svg  style="width:24px;"> [Mehrfachmaterial](Arch_MultiMaterial/de.md) n Anspruch nehmen. Wenn ein Mehrfachmaterial verwendet wird, wird die Platte mehrschichtig, wobei die durch das Mehrfachmaterial vorgegebenen Dicken verwendet werden. Bei jeder Schicht mit einer Dicke von Null wird die Dicke automatisch durch den verbleibenden Raum definiert, der durch den eigenen Dickenwert der Tafel definiert ist, nachdem die anderen Schichten abgezogen wurden.


</div>

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

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>

Das Plattenwerkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole aus mit folgender Funktion verwendet werden: 
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


<div class="mw-translate-fuzzy">

-   [Wikihouse Portierungs Tutorium](Wikihouse_porting_tutorial/de.md)


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel/de
