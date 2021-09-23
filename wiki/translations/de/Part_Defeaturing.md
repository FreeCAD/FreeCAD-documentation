---
- GuiCommand:/de
   Name:Part Defeaturing
   Name/de:Part Beseitigen der Funktionalität
   MenuLocation:Part → Beseitigen der Funktionalität
   Workbenches:[Part](Part_Workbench/de.md)
   Version:0.18
---

# Part Defeaturing/de


</div>

## Beschreibung

Das Werkzeug **Beseitigen der Funktionalität** ist für die Entfernung ausgewählter Merkmale aus dem Modell vorgesehen. In diesem Zusammenhang sind Grundelemente als Löcher, Vorsprünge, Lücken, Fasen, Verrundungen usw. gemeint, die sich auf dem Modell befinden.

Das Werkzeug Beseitigen der Funktionalität kann in verschiedenen Zusammenhängen sehr nützlich sein:

-   Um einen importierten Festkörper zu bearbeiten, wenn keine Historie der Operationen verfügbar ist;
-   Beheben von Fehlern im Modell, z. B. Füllen von Lücken, Löchern usw.
-   Modellvereinfachung für die numerische Analyse, Anzeige auf mobilen Geräten, usw.

Die entfernten Grundelemente werden durch die Verlängerung der angrenzenden Flächen gefüllt, so dass keine unerwarteten Teile im Ergebnis erscheinen sollten. Bitte beachte, dass das Ergebnis eine neue Form ist, die nicht mit dem Original verbunden ist; es ist also nicht-parametrisch.

Um verfügbar zu sein, muss FreeCAD auf Open Cascade 7.3.0 oder höher basieren. Falls es in deiner Version von FreeCAD nicht verfügbar ist, kannst du einen Blick auf die [Arbeitsbereich Beseitigen der Funktionalität](Defeaturing_Workbench/de.md) Erweiterung werfen, die ähnliche Funktionen auch mit älteren Versionen von OCC oder FreeCAD anbietet.

![](images/Part_Defeaturing_example.png )

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle die zu entfernende(n) Fläche(n) auf dem Modell.
2.  Drücke die **<img src=images/Part_Defeaturing.svg style="width:24px"> '''Defeaturing'''** Schaltfläche
3.  Ein neues Objekt wird in der Modell [Baumansicht](Tree_view/de.md) mit der Bezeichnung *\'Defeatured* erstellt, und das ursprüngliche Objekt wird nicht mehr angezeigt.


</div>

## Verweise


<div class="mw-translate-fuzzy">

-   [3D Model Defeaturing](https://dev.opencascade.org/index.php?q=node/1211), die offizielle Ankündigung auf dem Open Cascade Collaborative Development Portal.
-   [Freecad 0.18 Defeaturing](https://peertube.mastodon.host/videos/watch/c6bc5abd-2eb7-48c7-af67-c4d8e6783872), eine Videodemonstration (auf Deutsch) an einem komplexen Modell auf PeerTube; auch ohne die Sprache zu verstehen, ist es ziemlich einfach zu folgen.
-   <img alt="" src=images/Defeaturing_workbench_icon.svg  style="width:24px;"> [ Arbeitsbereich Beseitigen der Funktionalität](Defeaturing_Workbench/de.md)


</div>


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Defeaturing/de
