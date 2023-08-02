---
- GuiCommand:
   Name: Sketcher MapSketch
   Name/de: Sketcher SkizzeZuordnen
   MenuLocation: Sketch /Skizze  -> Skizze einer Fläche zuordnen...
   Workbenches: Sketcher_Workbench/de, PartDesign_Workbench/de
   SeeAlso: Sketcher_NewSketch/de
---

# Sketcher MapSketch/de



## Beschreibung

Dieses Werkzeug ordnet eine vorhandene Skizze der Fläche einer Form zu. PartDesign Formelemente, die aus dieser Skizze erstellt werden, werden bei additiven Formelementen (Polster, Umlauf) mit dem darunter liegenden Festkörper verschmolzen oder bei subtraktiven Formelementen (Tasche, Nut) vom darunter liegenden Festkörper subtrahiert.

Bitte beachte, daß dieses Werkzeug nicht zum Erstellen neuer Skizzen verwendet wird. Es ordnet lediglich eine vorhandene Skizze der Fläche eines Festkörpers oder einem PartDesign Formelement zu oder ordnet diese neu zu. Typische Anwendungsfälle sind:

-   Die Skizze wurde auf einer Standardebene (XY, XZ, YZ) erstellt, und du möchtest sie der Fläche eines Festkörpers zuordnen, um darauf ein Formelement aufzubauen.
-   Die Skizze wurde einer bestimmten Fläche eines Festkörpers zugeordnet, aber du musst sie einer anderen Fläche zuordnen.
-   Reparieren eines kaputten Modells.

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width:480px;">



## Anwendung

-   Eine Fläche eines PartDesign-Formelements oder eines Festkörpers auswählen.
-   Auf die Schaltfläche **<img src="images/Sketcher_MapSketch.svg" width=16px> [Skizze einer Fläche zuordnen...](Sketcher_MapSketch/de.md)** in der Werkzeugleiste klicken (oder zum Menü PartDesign oder Skizze gehen, abhängig davon, welcher Arbeitsbereich aktiv ist)
-   Im Dialogfenster **Skizze auswählen**, das sich öffnet, wählt man aus der Liste die Skizze aus, die der Fläche zugeordnet werden soll, und klickt OK.
-   Die Skizze wird automatisch im Bearbeitungsmodus geöffnet.



## Anwendung beim Reparieren eines kaputten Modells 

Sketcher SkizzeZuordnen wird häufig bei der Reparatur eines kaputten Modells verwendet.

Ein häufiger Anwendungsfall ist, wenn der Abhängigkeitsgraph beschädigt wurde. (Du kannst den Abhängigkeitsgraph mit **Werkzeuge** anzeigen. → **[Abhängigkeitsgraph](Std_DependencyGraph/de.md)**.) Dies kann passieren, wenn du ein Formelement in der Mitte deines Modellbaums löschst. Im folgenden Beispiel wird ein Modell beschädigt und repariert.

Dies ist das Basismodell. Es hat ein Polster, eine Tasche, und ein Polster innerhalb der Tasche. Beachte, dass der Abhängigkeitsgraph linear ist.

![](images/JschremppFCADEdit1.png )

Nun wurde die Vertiefung sowie die Skizze, die die Vertiefung erzeugt hat, gelöscht (Pocket and Sketch001). Dies hat zur Folge, dass der Abhängigkeitsgraph unterbrochen ist. Um das Modell zu reparieren, soll die Skizze Sketch002 der oberen Fläche von Pad zugeordnet werden. In der Ansicht des Modells ist zu erkennen, dass leicht die falsche Fläche gewählt werden kann.

![](images/JschremppFCADEdit2.png )

Um das Modell zu reparieren, wird zuerst die Sichtbarkeit der Körper geändert. Pad001 wird unsichtbar gemacht und Pad sichtbar.

![](images/JschremppFCADEdit3.png )

Nun wird die obere Fläche von Pad ausgewählt und das Werkzeug \"Skizze einer Fläche zuordnen\" angeklickt. In dem sich öffnenden Dialog wird Sketch002 ausgewählt. Das Modell ist nun repariert. In dem Modellbaum machen wir Pad001 sichtbar und Pad unsichtbar, so dass das korrekte Modell zu sehen ist.

![](images/JschremppFCADEdit4.png )





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher MapSketch/de
