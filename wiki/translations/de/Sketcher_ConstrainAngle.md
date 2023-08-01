---
- GuiCommand:
   Name:Sketcher ConstrainAngle
   Name/de:Sketcher WinkelFestlegen
   MenuLocation:Sketch → Sketcher constraints → Winkel festlegen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**K** **A**
   SeeAlso:[Sketcher AbstandFestlegen](Sketcher_ConstrainDistance/de.md), [Sketcher RechtwinkligFestlegen](Sketcher_ConstrainPerpendicular/de.md)
---

# Sketcher ConstrainAngle/de



## Beschreibung

Die Randbedingung Winkel festlegen ist eine [maßliche Randbedingung](Sketcher_Workbench/de#Sketcher-Randbedingungen.md), die dazu dient, Winkel in der Skizze festzulegen. Sie ist in der Lage, die Neigungen einzelner Linien, Winkel zwischen den Linien, Winkel der Schnittpunkte von Kurven und Winkelbereiche von Kreisbögen festzulegen.



## Anwendung

Es gibt vier verschiedene Möglichkeiten, wie die Randbedingung angewendet werden kann:

-   auf einzelne Linien
-   zwischen Linien
-   auf Schnittpunkten von Kurven
-   auf Kreisbögen

Um die Randbedingung Winkel festlegen anzuwenden, sollte man diesen Schritten folgen:

1.  Ein, zwei oder drei Elemente in der Skizze auswählen. Der Modus wird abhängig von der Auswahl gewählt.

2.  Die Randbedingung kann mit verschiedenen Methoden aufgerufen werden:
    -   Die Schaltfläche **[<img src=images/Sketcher_ConstrainAngle.svg style="width:16px"> [Winkel festlegen](Sketcher_ConstrainAngle/de.md)** in der Werkzeugleiste drücken.
    -   Das Tastaturkürzel **K** dann **A**.
    -   Den Menüeintrag **Skizze → Skizzen-Beschränkungen → [<img src=images/Sketcher_ConstrainAngle.svg style="width:16px"> Winkel festlegen** auswählen.

3.  Ein Dialogfenster zum Ändern des (Winkel-) Wertes wird geöffnet.

4.  Falls erforderlich, den Winkel ändern. **Hinweis:** Der Winkel kann als Ausdruck eingegeben werden, der ausgewertet und als Ergebnis gespeichert wird.

5.  
    **OK**klicken.

Wie bei jeder maßlichen Randbedingung ist es möglich, den Winkelwert später zu ändern, durch Doppelklick der Randbedingung in der Liste unter Einschränkungen oder der 3D-Ansicht. Die Eingabe eines negativen Wertes führt zum Umklappen der Winkelrichtung.



## Varianten der Randbedingung 



### Neigungswinkel einer Linie 

**Akzeptierte Auswahl:** Linie

<img alt="" src=images/Sketcher_ConsraintAngle_mode1.png  style="width:600px;">

Die Randbedingung legt den polaren Winkel der Linienrichtung fest. Es ist der Winkel zwischen der Linie und der X-Achse der Skizze.



### Winkel eines Kreisbogens 

**Akzeptierte Auswahl:** Kreisbogen

<img alt="" src=images/Sketcher_ConsraintAngle_mode2.png  style="width:600px;">

In diesem Modus fixiert die Randbedingung die Winkelspannweite eines Kreisbogens.



### Zwischen Linien 

**Akzeptierte Auswahl:** Linie + Linie

<img alt="" src=images/Sketcher_ConsraintAngle_mode3.png  style="width:600px;">

In diesem Modus legt die Randbedingung den Winkel zwischen zwei Linien fest. Es ist nicht erforderlich, dass sich die Linien schneiden.



### Zwischen Kurven im Schnittpunkt (Winkel-über-Punkt) 

**Akzeptierte Auswahl:** beliebige Linie/Kurve + beliebige Linie/Kurve + beliebiger Punkt

<img alt="" src=images/Sketcher_ConsraintAngle_mode4.png  style="width:600px;">

In diesem Modus wird der Winkel zwischen zwei Kurven in ihrem Schnittpunkt festgelegt. Der Schnittpunkt kann auf der Verlängerung der Kurven liegen. Der Punkt sollte explizit angegeben werden, da sich Kurven üblicherweise in mehr als einem Punkt schneiden.

Damit die Randbedingung korrekt funktioniert, muss der Punkt auf beiden Kurven liegen. Wenn die Randbedingung aufgerufen wird, wird der Punkt automatisch auf beiden Kurven festgelegt (bei Bedarf werden [Hilfsrandbedingungen](Sketcher_helper_constraint/de.md) hinzugefügt), und der Winkel zwischen den Kurven wird in dem Punkt festgelegt. Diese [Hilfsrandbedingungen](Sketcher_helper_constraint/de.md) sind einfach normale Randbedingungen. Sie können manuell hinzugefügt oder gelöscht werden. Auf dem obigen Beispielbild gibt es keine Hilfsrandbedingungen, da der ausgewählte Punkt bereits der Schnittpunkt der Kurven ist.



## Skripten

Die Randbedingung WinkelFestlegen kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus wie folgt erstellt werden: 
```python
# line slope angle
Sketch.addConstraint(Sketcher.Constraint('Angle',iline,angle))

# angular span of arc
Sketch.addConstraint(Sketcher.Constraint('Angle',iarc,angle))

# angle between lines
Sketch.addConstraint(Sketcher.Constraint('Angle',iline1,pointpos1,iline2,pointpos2,angle))

# angle-via-point (no helper constraints are added automatically when from python)
Sketch.addConstraint(Sketcher.Constraint('AngleViaPoint',icurve1,icurve2,geoidpoint,pointpos,angle))
``` wobei:

  - `Sketch` ein Skizzenobjekt ist

  - `iline, iline1, iline2` sind ganze Zahlen, die die Zeilen durch ihre Ordnungszahlen in `Sketch` angeben.

  - `pointpos1, pointpos2` sollte 1 für den Startpunkt und 2 für den Endpunkt sein. Die Wahl der Endpunkte ermöglicht die Einstellung des internen (oder externen) Winkels, und sie beeinflusst die Art und Weise, wie die Randbedingung auf dem Bildschirm dargestellt wird.

  - `geoidpoint` und `pointpos` in `AngleViaPoint` sind die Indizes, die den Schnittpunkt angeben.

  - `angle` ist der Winkelwert im Bogenmaß. Der Winkel wird zwischen Tangentenvektoren im Gegenuhrzeigersinn gezählt. Tangentenvektoren zeigen für die Linien von Anfang bis Ende (oder umgekehrt, wenn der Endpunkt im Modus Winkel zwischen Linien angegeben wird) und für Kreise, Bögen und Ellipsen entlang der Richtung entgegen dem Uhrzeigersinn. Die Größe wird auch als Winkel akzeptiert (z.B. `App.Units.Quantity('45 deg'))`

Die Seite [Sketcher Skripten](Sketcher_scripting/de.md) erklärt die Werte, die für `iline`, `iline1`, `iline2`, `pointpos1`, `pointpos2`, `geoidpoint` und `pointpos` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainAngle/de
