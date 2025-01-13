---
 GuiCommand:
   Name: Draft Trimex
   Name/de: Draft Trimex
   MenuLocation: Änderung , Trimex<br>Bearbeiten , Trimex.
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: **T** **R**
   SeeAlso: Part_Extrude/de
---

# Draft Trimex/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Trimex.svg  style="width:24px;"> **Draft Trimex** [beschneidet oder verlängert ](#Beschneiden_oder_verlängern.md) ein ausgewähltes Objekt. Schnittstellen mit einem anderen Objekt können zum Bestimmen neuer Endpunkte verwendet werden. Der Befehl kann auch verwendet werden, um eine Fläche zu [extrudieren](#Extrudieren.md); in so einem Fall erstellt er ein [Part Extrude](Part_Extrude/de.md)-Objekt.

<img alt="" src=images/Draft_trimex_example.jpg  style="width:400px;"> 
*Oben: ein Draft-Draht verlängert und dann beschnitten.<br>
Unten: eine Fläche zu einem Festkörper extrudiert.*



## Beschneiden oder verlängern 



### Anwendung

1.  Wahlweise ein Objekt auswählen. Das Objekt muss eine [Draft-Linie](Draft_Line/de.md), eine [Draft-Polylinie](Draft_Wire/de.md), ein [Draft-Bogen](Draft_Arc/de.md) oder ein [Draft-Kreis](Draft_Circle/de.md) sein (nur diese lassen sich trimmen). Ist das ausgewählte Objekt geschlossen, muss seine {{PropertyData/de|Make Face}} auf `False` gesetzt werden.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Trimex.svg" width=16px> [Trimex](Draft_Trimex/de.md)** drücken.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Änderung → <img src="images/Draft_Trimex.svg" width=16px> Trimex** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Bearbeiten → <img src="images/Draft_Trimex.svg" width=16px> Trimex** auswählen.
    -   Das Tastaturkürzel **T** dann **R**.
3.  Wurde noch kein Objekt ausgewählt: Ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Der Aufgabenbereich **Trimex** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
5.  Den Mauszeiger in der [3D-Ansicht](3D_view/de.md) bewegen, damit die Vorschau dem gewünschten Ergebnis entspricht. Wenn nötig, die unter [Optionen](#Optionen.md) beschriebenen Auswahltasten verwenden.
6.  Eine der folgenden Möglichkeiten ausführen:
    -   Einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Einen **Abstand** oder einen **Winkel** eingeben. Der Abstand ist ein Delta-Abstand. Diese Option funktioniert nicht wenn Auswahltasten verwendet werden.
    -   Den Mauszeiger über eine Kante, die zu einem anderen Objekt gehört, bewegen und klicken, wenn diese hervorgehoben wird, um das ausgewählte Objekt zu beschneiden bzw. zu verlängern, mit der hervorgehobenen Kante als neuen Endpunkt. Beim Beschneiden wird das standardmäßige Ergebnis von der Projektion des Punktes, an dem die Schnittlinie ausgewählt wurde, auf das zu beschneidende Objekt bestimmt. Dabei ist zu beachten, dass [Draft-Fangfunktionen](Draft_Snap/de.md) hier einen unschönen Einfluss haben können. In einigen Fällen kann es nützlich sein, sie zeitweilig abzuschalten.



### Optionen

Die im Aufgaben-Bereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastaturkürzel sind die voreingestellten Tastaturkürzel.

-   Halte die **Alt** Taste um das Standard Ergebnis des Befehls umzukehren.
-   Halte die **Shift** Taste um den Vorgang auf den aktuellen Abschnitt eines [Draft Linienzug](Draft_Wire/de.md) einzuschränken.
-   Drücke **S** um [Draft Einrasten](Draft_Snap/de.md) ein- oder auszuschalten

Ein Beispiel um die Modifizier Tasten zu erklären. Die linke Kante oder die obere Kante des U-förmigen Drahtes wurden erweitert. Alles [Draft Einrasten](Draft_Snap/de.md) wurde abgeschaltet.

![](images/Draft_Trimex_example2.png )

1.  Der Bogen wurde nahe der unteren linken Ecke des Drahtes angeklickt. Dies ist das Standardmäßige Ergebnis.

2.  
    **Alt**wurde gedrückt gehalten, während der Bogen nahe der unteren linken Ecke des Drahtes angeklickt wurde.

3.  
    **Y**wurde gedrückt und Während der Mauszeiger über der Linken Kante schwebte, wurde **Shift** gedrückt gehalten und dann der Bogen angeklickt. Das Drücken von **Y** ist nur für Kanten erforderlich, die mehr oder weniger parallel zur Y-Achse sind.



## Extrudieren



### Anwendung 

Siehe auch: [Draft Fangen](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Es kann hilfreich sein die [Draft Arbeitsebenezu](Draft_SelectPlane/de.md) wechseln so dass sie nicht in der gleichen Ebene mit der Fläche die du extrudieren möchtest ist.
2.  Wähle optional eine einzelne Fläche oder ein Objekt mit einer einzelnen Fläche.
3.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_Trimex.svg" width=16px> [Draft Trimex](Draft_Trimex/de.md)** Schaltfläche.
    -   Wähle die **Änderung → <img src="images/Draft_Trimex.svg" width=16px> Trimex** Option aus dem Menü.
    -   Verwende die Kurztasten: **T** dann **R**.
4.  Wenn bis jetzt noch kein Objekt oder keine Fläche ausgewählt wurde: wähle ein Objekt mit einer einzelnen Fläche in [3D Ansicht](3D_view/de.md).
5.  Das Aufgabenfenster **Trimex** öffnet. Siehe [Options](#Options_2.md) für weitere Informationen.
6.  Um die Richtung der Verlängerung und den Abstand zu definieren mache eines der folgenden:
    -   Greife einen Punkt in der [3D Ansicht](3D_view/de.md) der nicht in der gleichen Ebene wie die Fläche liegt.
    -   Stelle sicher, dass der Zeiger auf der richtigen Seite der Fläche in der [3D Ansicht](3D_view/de.md) ist, und gib einen **Abstand** ein.



### Optionen 

Die hier verwendete Modifizier Taste kann geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md).

-   Halte **Shift** um in eine Richtung die nicht parallel zur Normalen der Fläche ist zu verlängern.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Es gibt keine Python-Methode zum Trimmen von Objekten. Um Objekte zu extrudieren, wird die Methode `extrude` des Draft-Moduls verwendet.


```python
extrusion = extrude(obj, vector, solid=False)
```

-    `obj`ist das Objekt, das verlängert wird.

-    `vector`ist die Richtung und der Betrag der Verlängerung.

-   Falls `solid` auf `True` ist, dann wird an Stelle einer Schale ein Körper erzeugt.

-    `extrusion`wird mit dem erzeugten Objekt zurückgegeben.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(1500, 500)
doc.recompute()

vector = App.Vector(0, 0, 300)
solid = Draft.extrude(rectangle, vector, solid=True)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Trimex/de
