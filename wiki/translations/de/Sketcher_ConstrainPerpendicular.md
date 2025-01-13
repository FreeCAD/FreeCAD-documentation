---
 GuiCommand:
   Name: Sketcher ConstrainPerpendicular
   Name/de: Sketcher RechtwinkligFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Rechtwinklig festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **N**
   SeeAlso: Sketcher_ConstrainAngle/de
---

# Sketcher ConstrainPerpendicular/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:24px;"> [Sketcher RechtwinkligFestlegen](Sketcher_ConstrainPerpendicular/de.md) legt zwei Linien rechtwinklig zueinander fest oder zwei Kanten bzw. eine Kante und eine Achse an ihrer Verbindungsstelle. Linien werden als unendlich angesehen; offene Kurven werden ebenfalls virtuell verlängert. Die Randbedingung kann auch zwei Kanten verbinden und sie gleichzeitig an der Verbindungsstelle rechtwinklig festlegen.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_ConstrainPerpendicular.svg" width=16px> [Rechtwinklig festlegen](Sketcher_ConstrainPerpendicular/de.md)** drücken.

    -   Den Menüeintrag **Skizze → Sketcher-Randbedingung → <img src="images/Sketcher_ConstrainPerpendicular.svg" width=16px> Rechtwinklig festlegen** auswählen.

    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **Festlegen → <img src="images/Sketcher_ConstrainPerpendicular.svg" width=16px> Rechtwinklig festlegen** im Kontextmenü auswählen.

    -   Das Tastaturkürzel **N**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Eine der folgenden Möglichkeiten auswählen:
    -   Zwei Kanten auswählen. Eine der Kanten muss eine gerade Linie oder eine Achse sein. Die andere kann eine beliebige Kante sein außer einem B-Spline.
    -   Einen Punkt und zwei Kanten auswählen (in dieser Reihenfolge).
    -   Eine Kante, einen Punkt und eine weitere Kante auswählen (wie vorher).
5.  Eine Randbedingung Rechtwinklig festlegen wird hinzugefügt. Wurden ein Punkt und zwei Kanten ausgewählt, werden auch bis zu zwei Randbedingungen [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) hinzugefügt. Siehe [Beispiel](#Zwischen_zwei_Kanten_in_einem_Punkt.md).
6.  Wahlweise weitere Randbedingungen erstellen.
7.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



### Einmal-Ausführen-Modus 

1.  Eine der folgenden Möglichkeiten auswählen:
    -   Zwei Kanten auswählen (siehe oben).
    -   Zwei Endpunkte auswählen, die zu unterschiedlichen Kanten gehören.
    -   Eine Kante und den Endpunkt einer anderen Kante auswählen (in bleliebiger Reihenfolge).
    -   Einen Punkt und zwei Kanten auswählen (wie vorher).
2.  Dieses Werkzeug aufrufen, wie oben beschrieben oder mit der folgenden zusätzlichen Möglichkeit:
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_ConstrainPerpendicular.svg" width=16px> Rechtwinklig festlegen** im Kontextmenü auswählen.
3.  Eine Randbedingung Rechtwinklg festlegen wird hinzugefügt. Wurden ein Punkt und zwei Kanten ausgewählt, können auch bis zu zwei Randbedingungen [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) hinzugefügt werden. Siehe [Beispiele](#Zwischen_zwei_Kanten_in_einem_Punkt.md).



## Beispiele



### Zwischen zwei Kanten 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode1.png  style="width:400px;">

Die beiden Kanten werden an ihrer (virtuellen) Schnittstelle rechtwinklig zueinander angeordnet. Ist eine der Kanten ein [Kegeschnitt](Sketcher_Workbench/de#Sketcher_CompCreateConic.md), wird ein [Punktobjekt](Sketcher_CreatePoint/de.md) hinzugefügt, das mit jeweils einer Randbedingung [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) mit beiden (verlängerten) Kanten verbunden ist.



### Zwischen zwei Endpunkten 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode2.png  style="width:400px;">

Die Endpunkte werden deckungsgleich (koinzident) und die Kanten rechtwinklig zueinander festgelegt.



### Zwischen Kante und Endpunkt 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode3.png  style="width:400px;">

Der Endpunkt einer Kante wird auf der anderen Kante liegend und die Kanten in diesem Punkt rechtwinklig zueinander festgelegt.



### Zwischen zwei Kanten in einem Punkt 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode4.png  style="width:400px;">

Die zwei Kanten werden in einem gegebenen Punkt rechtwinklig zueinander festgelegt. Der Punkt kann ein beliebiger Punkt sein z.B. der Mittelpunkt eines Kreises, der Endpunkt einer Kante oder der Ursprung; er kann zu einer der Kanten gehören und er kann auch ein [Punktobjekt](Sketcher_CreatePoint/de.md) sein. Wenn erforderlich, werden Randbedingungen [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) hinzugefügt, um sicherzustellen, dass der Punkt auf beiden (verlängerten) Kanten liegt. Diese zusätzlichen Randbedingungen werden These additional constraints are called [Helferrandbedingungen](Sketcher_helper_constraint/de.md) genannt.



## Skripten

Die Randbedingung RechtwinkligFestlegen kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Befehlen erstellt werden: 
```python
# direct perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,icurve2))

# point-to-point perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2))

# perpendicular-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('PerpendicularViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
``` wobei

  - `Sketch` ein Skizzenobjekt ist.

  - `icurve1`, `icurve2` zwei ganze Zahlen (integer) sind, die die Kurven identifizieren, die rechtwinklig zueinander liegen sollen. Diese Ganzzahlen sind Indexwerte der Skizze (die entsprechenden Rückgabewerte von `Sketch.addGeometry`).

  - `pointpos1`, `pointpos2` `1` für den Startpunkt und `2` für den Endpunkt sein sollten.

  - `geoidpoint` und `pointpos` in `PerpendicularViaPoint` die Indizes sind, die die Schnittstelle (an der die Rechtwinkligkeit gilt) festlegen.

Die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) erklärt die Werte, die für `incurve1`, `incurve2`, `pointpos1`, `pointpos2` und `geoidpoint` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPerpendicular/de
