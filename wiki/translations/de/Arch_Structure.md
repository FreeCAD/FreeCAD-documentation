---
 GuiCommand:
   Name: Arch Structure
   Name/de: Arch Struktur
   MenuLocation: Arch , Strukturwerkzeug , Struktur
   Workbenches: Arch_Workbench/de
   Shortcut: **S** **T**
   SeeAlso: Arch_Wall/de, Arch_Rebar/de
---

# Arch Structure/de

## Beschreibung


<div class="mw-translate-fuzzy">

Das [Arch Struktur](Arch_Structure/de.md)-Werkzeug ermöglicht die Konstruktion von Bauelementen wie Ständern oder Querträgern, indem Breite, Länge und Höhe angegeben werden, oder das Element aus einem 2D-Profil heraus erzeugt wird (Fläche, Kantenzug oder Skizze).


</div>

Falls kein Profil angegeben wurde, ist eine Anzahl von Voreinstellungen verfügbar, die eine schnelle Errichtung von Strukturelementen aus einem vordefinierten Standardprofil erlaubt.

![](images/Arch_Structure_example.jpg ) 
*Ein Träger basierend auf einem 2D-Profil; eine Stütze und ein Träger definiert durch Höhe, Länge und Breite, ohne ein Basisprofil; eine metallische Struktur basierend auf einer 2D-Oberfläche*.

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wählen Sie eine 2D-Form (Draft-Objekt, Fläche oder Skizze) (optional)
2.  Drücken Sie den **<img src="images/Arch_Structure.svg" width=16px>[Struktur](Arch_Structure/de.md)
**-Knopf oder die Tasten **S** und **T**
3.  Passen Sie die Eigenschaften des Objektes Ihren Erfordernissen an.


</div>

## Optionen


<div class="mw-translate-fuzzy">

-   Wenn keine Basis-2D-Objekte ausgewählt sind, besitzt das Struktur-Werkzeug

zwei Zeichenmodi: Säule und Träger:

-   -   Im Säulenmodus ist ein Punkt in der Ansicht oder durch Eingabe von Koordinaten anzugeben. Das neue strukturelle Objekt wird an diesem Punkt platziert.
    -   Im Trägermodus sind zwei Punkte in der Ansicht oder durch Eingabe von Koordinaten anzugeben. Das neue strukturelle Objekt wird sich zwischen diesen beiden Punkt erstrecken.

-   Strukturelemente haben die gleichen gemeinsamen Eigenschaften und das Verhalten aller [Architekturkomponenten](Arch_Component/de.md).

-   Drücken von **Esc** oder **Cancel** bricht das aktuelle Kommando ab.

-   Ein Doppelklick auf das Element in der Baumansicht wechselt in den Editiermodus für das Objekt. In diesem Modus können dem Objekt Ergänzungen oder Aussparungen hinzugefügt werden.

-   Im Editiermodus ist es ebenfalls möglich, [Achsensysteme](Arch_Axis/de.md) zum Bauelement hinzuzufügen. Wird ein Achsensystem hinzugefügt, wird das Bauelement auf jede Achse kopiert. Werden zwei Achsensysteme hinzugefügt, wird das Bauelement auf jeden Achsenschnittpunkt kopiert.


</div>

## Eigenschaften

### Daten


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Tool}}: Ein optionaler Extrusionspfad, der jede Art von Linienzug sein kann. Falls diese Eigenschaft leer ist, wird die Extrusion gerade sein und in der durch die Normal-Eigenschaft angegebenen Richtung erfolgen

-    {{PropertyData/de|Normal}}: Gibt die Richtung an, in der die Basisfläche diser Struktur extrudiert wird. Falls diese Eigenschaft auf dem Vorgabewert (0,0,0) bleibt, wird die Richtung automatisch auf die normale Richtung der Basisfläche gesetzt.

-    {{PropertyData/de|Face Maker}}: Typ des zu benutzenden Oberflächenerstellungsalgorithmus, der bei der Erzeugung des Profils verwendet wird (None, Simple, Cheese oder Bullseye).

-    {{PropertyData/de|Length}}: Objektlänge (nur verwendet, wenn Objekt nicht auf einem Profil basiert)

-    {{PropertyData/de|Width}}: Objektbreite (nur verwendet, wenn Objekt nicht auf einem Profil basiert)

-    {{PropertyData/de|Height}}: Objekthöhe (Höhe des Bauelements oder Auszugslänge, wenn auf Profil basierend). Wenn keine Höhe angegeben ist und das Bauelement in einem [Boden/Geschoss](Arch_Floor/de.md)-Objekt mit definierter Höhe ist, übernimmt das Bauelement automatisch den Wert der Bodenhöhe.

-    {{PropertyData/de|Nodes Offset}}: Knotenabstand zwischen der (Mittel)achse (centerline) und den Knotenlinien.


</div>

### Ansicht

-    {{PropertyView/de|Nodes Type}}: Der Typ für Knotenpunkte dieses Objekts, linear oder area.

-    {{PropertyView/de|Show Nodes}}: Zeigt oder versteckt die Knotenpunkte.

## Voreinstellungen

Das Struktur-Werkzeug bietet auch eine Reihe von Voreinstellungen, die die schnelle Erstellung von standardisierten Metallprofilen oder vorgefertigten Betonelementen erlauben.

![](images/Arch_presets_example.jpg ) 
*Einige Voreinstellungen für Stahlstrukturen*

Die Voreinstellungen erhält man durch Auswahl einer **Kategorie** aus dem \"Optionen Struktur\"-Panel. Verfügbare Kategorien sind **Precast concrete** oder eins der Industriestandard-Metallprofile wie etwa **HEA**, **HEB** pder **INP**. Für jede dieser Kategorien ist eine Anzahl von Voreinstellungen verfügbar. Sobald eine Voreinstellung ausgewählt wurde, können die individuellen Parameter wie **Länge**, **Breite** oder **Höhe** angepasst werden. Allerdings wird bei Metallprofilen die Profilgröße durch die Voreinstellungen vorgegeben und kann nicht geändert werden.

Mit der Schaltfläche **Switch L/H** können die Werte von Länge und Höhe vertauscht werden, so dass aus einer vertikalen Säule ein horizontaler Träger wird.

<img alt="" src=images/Arch_precast_example.jpg  style="width:960px;"> 
*Einige Voreinstellungen für vorgefertigte Betonstukturen*

## Knotenpunkte

Bauelemente haben auch die Fähigkeit, Knotenpunkte anzuzeigen. Knotenpunkte sind eine Reihe von 3D-Punkten, die in einer *Nodes*-Eigenschaft gespeichert sind. Durch Umschalten der *Show Nodes*-Ansicht-Eigenschaft (on/off) kann man die Knotenpunkte eines Bauelements sehen:

<img alt="" src=images/Arch_structural_nodes.jpg  style="width:960px;"> 
*Sichtbarmachung von Knotenpunkten für eine Reihe von Bauelementen*


<div class="mw-translate-fuzzy">

-   Knoten werden automatisch berechnet und aktualisiert, solange man sie nicht manuell ändert. Wenn Du das getan hast, werden sie nicht aktualisiert, wenn sich die Form des Struktur-Objekts ändert, außer Du benutzt das \"Reset Nodes\"-Werkzeug weiter unten.
-   Arch-Strukturen können nicht nur lineare Knoten haben, sondern auch planare Knoten. Dafür müssen 1- mindestens drei Vektoren in der \"Nodes\"-Eigenschaft des Objekts vorhanden sein, 2- die \"NodesType\"-Eigenschaft des ViewObject auf \"Area\" gesetzt sein
-   Wenn die Knotenberechnung automatisch erfolgt (Du sie nie manuell verändert hast) und die Role-Eigenschaft einer Struktur auf \"Slab\" gesetzt wird, wird daraus automatisch ein planarer Knoten (es gibt mehr als drei Vektoren und der NodesType wird auf \"Area\" gesetzt).
-   Beim Ändern eines Bauelement-Objekts (Doppelklick) wird eine Reihe von Knotenwerkzeugen im Aufgaben-Reiter verfügbar:
    -   Zurücksetzen der Knoten (reset nodes) auf automatische Berechnung, falls Du sie manuell verändert hast
    -   Graphische Änderung der Knoten, arbeitet genau so wie [Draft Ändern](Draft_Edit/de.md)
    -   Erweitern der Knoten des geänderten Objekts, bis es die Knoten eines anderen Objekts berührt
    -   Sorgt für das Zusammenfallen (coincident) des Knotens dieses Objekts und eines anderen
    -   Umschalten der Anzeige aller Knoten aller Bauelemente des Dokuments (on/off)


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Scripting 


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Struktur-Werkzeug kann in [Makros](macros/de.md) ebenso wie aus der Python-Konsole heraus über folgende Funktion angesprochen werden:


</div>


```python
Structure = makeStructure(baseobj=None, height=None)
Structure = makeStructure(baseobj=None, length=None, width=None, height=None, name="Structure")
```

-   Erstellt ein `Struktur`-Objekt aus dem gegebenen `baseobj`, das ein geschlossenes Profil ist und der gegebenen Extrusions `height`.
    -   Falls kein `baseobj` gegeben ist, kann man die numerischen Werte für `length`, `width` und `height` angeben, um eine Blockstruktur zu erstellen.
    -   Das `baseobj` kann auch ein existierender Volumenkörper sein.

Beispiel: 
```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(200, 300)
Structure1 = Arch.makeStructure(Rect, height=2000)
FreeCAD.ActiveDocument.recompute()

Structure2 = Arch.makeStructure(None, length=500, width=1000, height=3000)
Draft.move(Structure2, FreeCAD.Vector(2000, 0, 0))
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Structure/de
