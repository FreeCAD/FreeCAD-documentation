---
 GuiCommand:
   Name: Sketcher CreateFillet
   Name/de: Sketcher VerrundungErstellen
   MenuLocation: Skizze , Sketcher-Werkzeuge , Verrundung erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **F** **F**
   SeeAlso: 
---

# Sketcher CreateFillet/de



## Beschreibung

das Werkzeug <img alt="" src=images/Sketcher_CreateFillet.png  style="width:24px;"> [VerrundungErstellen](Sketcher_CreateFillet/de.md): Erstellt eine Verrundung zwischen zwei nicht parallelen Kanten. {{Version/de|1.0}}: Das Werkzeug kann auch eine Fase erstellen


{{Version/de|1.0}}

: Werden zwei gerade Kanten, die durch eine Randbedingung [Koinzident festlegen](Sketcher_ConstrainCoincident/de.md) verbunden sind, mit einer Verrundung oder Fase versehen, kann der Eckpunkt wahlweise erhalten bleiben. Das Werkzeug fügt dann ein [Punkt](Sketcher_CreatePoint/de.md)-Objekt hinzu, dass durch die Randbedingung [PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md) mit beiden Kanten verbunden wird. Randbedingungen des Eckpunktes werden auf das neue Punkt-Objekt übertragen.

![](images/SketcherCreateFilletExample.png‎ )



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_CreateFillet.svg" width=16px> [Verrundung erstellen](Sketcher_CreateFillet/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Werkzeuge → <img src="images/Sketcher_CreateFillet.svg" width=16px> Verrundung  erstellen** auswählen.
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_CreateFillet.svg" width=16px> Verrundung erstellen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **G** dann **F** dann **F**.
2.  Eine vorhandene Auswahl wird gelöscht; das Werkzeug akzeptiert keine Vorauswahl.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Der Abschnitt **Parameter der Verrundung/Fase** ({{Version/de|1.0}}) wird im oberen Bereich des [Sketcher-Dialogs](Sketcher_Dialog/de.md) eingefügt.
5.  Wahlweise die **U**-Taste drücken oder die Checkbox **Eckpunkt erhalten** im Abschnitt **Parameter der Verrundung/Fase** deaktivieren, um die Option abzuwählen. {{Version/de|1.0}}
6.  Wahlweise die **M**-Taste drücken oder einen Eintrag in der Ausklappliste **Modus** im Abschnitt **Parameter der Verrundung/Fase** auswählen, um den Werkzeugmodus zu wechseln:
    -   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:16px;"> 
**Fillet**
    -   <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:16px;"> 
**Chamfer**
7.  Eine der folgenden Möglichkeiten auswählen:
    -   Einen Punkt auswählen, der zwei gerade, nicht parallele Kanten mit einer Randbedingung [Koinzident festlegen](Sketcher_ConstrainCoincident/de.md) verbindet.
    -   Zwei nicht parallele Kanten auswählen. Jede der Kanten kann eine gerade [Linie](Sketcher_CreateLine/de.md), ein [Kreisbogen](Sketcher_CreateArc/de.md), ein [Ellipsenbogen](Sketcher_CreateArcOfEllipse/de.md), ein [Hyperbelbogen](Sketcher_CreateArcOfHyperbola/de.md) oder ein [aParabelbogen](Sketcher_CreateArcOfParabola/de.md) sein. [B-Splines](Sketcher_Workbench/de#Sketcher_CompCreateBSpline.md) werden zurzeit nicht unterstützt.
8.  Die Verrundung bzw. Fase wird erstellt, inklusive eines Punkt-Objekts falls eine Ecke erhalten wurde. Für eine Fase wird auch ein Hilfsgeometriebogen erstellt.
9.  Dieses Werkzeug läuft immer im Fortsetzen-Modus: wahlweise weitere Punkte und/oder Kanten auswählen.
10. Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



## Hinweise

-   Der Hilfsgeometriebogen einer Fase ist nicht sichtbar außerhalb der Skizze. Er kann nicht gelöscht werden, ohne die Geometrie der Fase aufzubrechen.
-   Einige ([Kegelschnitt](Sketcher_Workbench/de#Sketcher_CompCreateConic.md))-Kurven müssen [zugeschnitten](Sketcher_Trimming/de.md) werden, bevor sie verrundet werden können.
-   Der Verrundungsradius hängt von der Auswahlmethode ab. Wird eine Randbedingung [Koinzident festlegen](Sketcher_ConstrainCoincident/de.md) ausgewählt, die zwei gerade Kanten verbindet, wird der Verrundungsradius von der Länge der kürzesten Kante abgeleitet. Werden zwei Kanten ausgewählt, ist der Radius gleich dem Abstand vom ersten angeklickten Punkt zum Schnittpunkt der (verlängerten) Kanten.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateFillet/de
