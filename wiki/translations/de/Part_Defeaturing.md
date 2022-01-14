---
- GuiCommand:/de
   Name:Part Defeaturing
   Name/de:Part Beseitigen der Funktionalität
   MenuLocation:Part → Beseitigen der Funktionalität
   Workbenches:[Part](Part_Workbench/de.md)
   Version:0.18
---

# Part Defeaturing/de

## Beschreibung

Das Werkzeug **Merkmal aus einer Form entfernen** ist für die Entfernung ausgewählter Merkmale aus dem Modell vorgesehen. In diesem Zusammenhang sind Grundelemente als Löcher, Vorsprünge, Lücken, Fasen, Verrundungen usw. gemeint, die sich auf dem Modell befinden.

Das Werkzeug \'Merkmal aus einer Form entfernen\' kann in verschiedenen Zusammenhängen sehr nützlich sein:

-   Um einen importierten Festkörper zu bearbeiten, wenn keine Historie der Operationen verfügbar ist;
-   Beheben von Fehlern im Modell, z. B. Füllen von Lücken, Löchern usw.
-   Modellvereinfachung für die numerische Analyse, Anzeige auf mobilen Geräten, usw.

Die entfernten Grundelemente werden durch die Verlängerung der angrenzenden Flächen gefüllt, so dass keine unerwarteten Teile im Ergebnis erscheinen sollten. Bitte beachte, dass das Ergebnis eine neue Form ist, die nicht mit dem Original verbunden ist; es ist also nicht-parametrisch.

Um verfügbar zu sein, muss FreeCAD auf Open Cascade 7.3.0 oder höher basieren. Falls es in deiner Version von FreeCAD nicht verfügbar ist, kannst du einen Blick auf die [Merkmal aus einer Form entfernen](Defeaturing_Workbench/de.md) Erweiterung werfen, die ähnliche Funktionen auch mit älteren Versionen von OCC oder FreeCAD anbietet.

![](images/Part_Defeaturing_example.png )

## Anwendung

1.  Wähle die zu entfernende(n) Fläche(n) auf dem Modell.
2.  Klicke auf die Schaltfläche **[<img src=images/Part_Defeaturing.svg style="width:24px"> '''Merkmal aus einer Form entfernen'''**
3.  Ein neues Objekt wird in der Modell [Baumansicht](Tree_view/de.md) mit der Bezeichnung *\'Defeatured* erstellt und das ursprüngliche Objekt wird nicht mehr angezeigt.

## Verweise

-   [3D Model Defeaturing](https://dev.opencascade.org/index.php?q=node/1211), die offizielle Ankündigung auf dem Open Cascade Collaborative Development Portal.
-   <img alt="" src=images/Defeaturing_workbench_icon.svg  style="width:24px;"> [ Arbeitsbereich Merkmal aus einer Form entfernen](Defeaturing_Workbench/de.md)

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Defeaturing/de
