---
 GuiCommand:
   Name: Sketcher ConstrainTangent
   Name/de: Sketcher TangentialFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Tangential oder kollinear festlegen
   Workbenches: Sketcher_Workbench/de 
   Shortcut: **T**
   SeeAlso: 
---

# Sketcher ConstrainTangent/de



## Beschreibung

The <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [Sketcher ConstrainTangent](Sketcher_ConstrainTangent.md) tool constrains two edges, or an edge and an axis, to be tangent. Lines are treated as infinite, and open curves are virtually extended as well. The constraint can also connect two edges, forcing them to be tangent at the joint. If two lines are selected, or a line and the endpoint of another line, the lines are made collinear.

Die Randbedingung TangentialFestlegen legt fest, dass sich zwei Kurven berühren (sie tangential sind). Linien werden als unendlich angesehen, und Bögen werden wie Vollkreise/Ellipsen behandelt. Die Randbedingung ist auch in der Lage, zwei Kurven miteinander zu verbinden, und sie gleichzeitig an der Verbindungsstelle tangential festzulegen, wodurch die Verbindung glatt wird.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_ConstrainTangent.svg" width=16px> [Tangential oder kollinear festlegen](Sketcher_ConstrainTangent/de.md)** drücken.

    -   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → <img src="images/Sketcher_ConstrainTangent.svg" width=16px> Tangential oder kollinear festlegen** auswählen.

    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **Festlegen → <img src="images/Sketcher_ConstrainTangent.svg" width=16px> Tangential oder kollinear festlegen** im Kontextmenü auswählen.

    -   Das Tastaturkürzel **T**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Eine der folgenden Möglichkeiten auswählen:
    -   Zwei beliebige Kanten, außer B-Splines, auswählen.
    -   Einen Punkt und zwei Kanten auswählen (in dieser Reihenfolge).
    -   Eine Kante, einen Punkt und eine weitere Kante auswählen (wie vorher).
5.  Eine Randbedingung Tangential oder kollinear festlegen wird hinzugefügt. Wurden ein Punkt und zwei Kanten ausgewählt, können bis zu zwei Randbedingungen [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) hinzugefügt werden. Siehe [Beispiele](#Zwischen_zwei_Kanten_in_einem_Punkt.md).
6.  Wahlweise weitere Randbedingungen erstellen.
7.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



### Einmal-Ausführen-Modus 

1.  Eine der folgenden Möglichkeiten auswählen:
    -   Zwei Kanten auswählen (siehe oben).
    -   Zwei Kanten auswählen, die zu unterschiedlichen Kanten gehören.
    -   Eine Kante und den Endpunkt einer anderen Kante auswählen (in beliebiger Reihenfolge).
    -   Einen Punkt und zwei Kanten auswählen (wie vorher).
2.  Das Werkzeug aufrufen, wie oben beschrieben oder mit der folgenden zusätzlichen Möglichkeit:
    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_ConstrainTangent.svg" width=16px> Tangential oder kollinear festlegen** im Kontextmenü auswählen.
3.  Eine Randbedingung Tangential oder kollinear festlegen wird hinzugefügt. Wurden ein Punkt und zwei Kanten ausgewählt, können auch bis zu zwei Randbedingungen [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) hinzugefügt werden. Siehe [Beispiele](#Zwischen_zwei_Kanten_in_einem_Punkt.md).



## Beispiele



### Zwischen zwei Kanten 

<img alt="" src=images/Sketcher_ConsraintTangent_mode1.png  style="width:400px;">

Die zwei Kanten werden tangential ausgerichtet. Ist eine der Kanten ein [Kegelschnitt](Sketcher_Workbench/de#Sketcher_CompCreateConic.md), wird ein [Punktobjekt](Sketcher_CreatePoint/de.md) hinzugefügt, das mit jeweils einer Randbedingung [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) mit beiden (verlängerten) Kanten verbunden ist.

Es wird nicht empfohlen den Berührpunkt manuell zu bestimmen, indem ein Punkt erstellt wird, der auf beiden Kurven liegend festgelegt wird. Dies funktioniert im Prinzip, aber die Konvergenz der Lösung wird erheblich erschwert, sprunghafter und benötigt ungefähr doppelt so viele Iterationen wie normal. Wird der Berührpunkt benötigt, werden stattdessen zwei Kanten und ein vorhandener Punkt ausgewählt.



### Zwischen zwei Endpunkten 

<img alt="" src=images/Sketcher_ConsraintTangent_mode2.png  style="width:400px;">

Die Endpunkte werden koinzident (deckungsgleich) festgelegt und der Winkel zwischen den Kanten in diesem Punkt auf 180° (stumpfe Verbindung) oder 0° (Scharfe Verbindung) festgelegt, abhängig von der Positionierung der Kanten bevor die Randbedingung zugeordnet wurde.



### Zwischen Kante und Endpunkt 

<img alt="" src=images/Sketcher_ConsraintTangent_mode3.png  style="width:400px;">

Der Endpunkt einer Kante wird auf der anderen Kante liegend und die Kanten in diesem Punkt tangential zueinander festgelegt.



### Zwischen zwei Kanten in einem Punkt 

<img alt="" src=images/Sketcher_ConsraintTangent_mode4.png  style="width:400px;">

Die zwei Kanten werden in einem gegebenen Punkt tangential zueinander festgelegt. Der Punkt kann ein beliebiger Punkt sein z.B. der Mittelpunkt eines Kreises, der Endpunkt einer Kante oder der Ursprung; er kann zu einer der Kanten gehören und er kann auch ein [Punktobjekt](Sketcher_CreatePoint/de.md) sein. Wenn erforderlich, werden Randbedingungen [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) hinzugefügt, um sicherzustellen, dass der Punkt auf beiden (verlängerten) Kanten liegt. Diese zusätzlichen Randbedingungen werden These additional constraints are called [Helferrandbedingungen](Sketcher_helper_constraint/de.md) genannt.

Verglichen mit der direkten Tangentialität ist diese Randbedingung langsamer, weil mehr Freiheitsgrade involviert sind, aber wenn der Berührungspunkt benötigt wird, ist dies der empfohlene Modus, weil er eine bessere Konvergenz der Lösung aufweist.



### Zwischen zwei Linien 

<img alt="" src=images/Sketcher_ConstraintTangent_mode5.png  style="width:400px;">

Die beiden Linien werden kollinear zueinander ausgerichtet.



## Skripten

Die Randbedingung TangentialFestlegen kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Befehlen erstellt werden: 
```python
# direct tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,icurve2))

# point-to-point tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2))

# tangent-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('TangentViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
``` wobei

  - `Sketch` ein Skizzenobjekt ist.

  - `icurve1`, `icurve2` zwei ganze Zahlen (integer) sind, die die Kurven identifizieren, die zueinander tangential liegen sollen. Diese Ganzzahlen sind Indexwerte der Skizze (die entsprechenden Rückgabewerte von `Sketch.addGeometry`).

  - `pointpos1`, `pointpos2` 1 für den Startpunkt und 2 für den Endpunkt sein sollten.

  - `geoidpoint` und `pointpos` in `TangentViaPoint` die Indizes sind, die den Berührpunkt festlegen.

Die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) erklärt die Werte, die für `incurve1`, `incurve2`, `pointpos1`, `pointpos2`, `geoidpoint` und `pointpos` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainTangent/de
