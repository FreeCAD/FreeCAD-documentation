---
- GuiCommand:/de
   Name:Sketcher ConstrainAngle
   Name/de:Skizzierer BeschränkeWinkel
   MenuLocation:Skizze → Skizzierer Beschränkungen → Winkel beschränken
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Shortcut:**A**
   SeeAlso:[Skizzierer Beschränke Abstand](Sketcher_ConstrainDistance/de.md), [Skizzierer Beschränkung Senkrecht](Sketcher_ConstrainPerpendicular/de.md)
---

# Sketcher ConstrainAngle/de

## Beschreibung

Die Winkelbeschränkung ist eine [Bezugsbeschränkung](Sketcher_Workbench/de#Skizzierer_Beschränkungen.md), die dazu dient, Winkel in der Skizze festzulegen. Sie ist in der Lage, die Neigungen einzelner Linien, Winkel zwischen den Linien, Winkel der Schnittpunkte von Kurven und Winkelbereiche von Kreisbögen festzulegen.

## Anwendung

Es gibt vier verschiedene Möglichkeiten, wie die Beschränkung angewendet werden kann:

-   auf einzelne Linien
-   zwischen Linien
-   zu Schnittpunkten von Kurven
-   zu Kreisbögen

Um die Winkelbeschränkung anzuwenden, sollte man den Schritten folgen:

1.  Wähle ein, zwei oder drei Elemente in der Skizze aus. Der Modus wird abhängig von der Auswahl gewählt.
2.  Rufe die Beschränkung mit verschiedenen Methoden auf:
    -   Drücken der **[<img src=images/Sketcher_ConstrainAngle.svg style="width:16px"> [Beschränke Winkel](Sketcher_ConstrainAngle/de.md)** Schaltfläche in der Werkzeugleiste.
    -   Verwendung der **A** Tastaturkürzel. (**A**\' steht für **A**ngle, engl.: Winkel)
    -   Verwendung des **Skizze → Skizzierer Beschränkungen → [<img src=images/Sketcher_ConstrainAngle.svg style="width:16px"> Beschränke Winkel** aus dem obersten Menüeintrag
3.  Ein Bezugs Bezugsbearbeitungsdialogfeld klappt auf.
4.  Ändere den Winkel, falls erforderlich. **Hinweis:** Der Winkel kann als Ausdruck eingegeben werden, der ausgewertet und als Ergebnis gespeichert wird.
5.  Klicke **OK**

Wie bei jeder Bezugsbeschränkung ist es möglich, den Winkelwert später zu ändern, durch Doppelklick der Beschränkung in der Beschränkungsliste oder der 3D Ansicht. Die Eingabe eines negativen Wertes führt zum Umkippen der Winkelrichtung.

## Beschränkungsmodi

### Linienneigungswinkel

**Akzeptierte Auswahl:** Linie

<img alt="" src=images/Sketcher_ConsraintAngle_mode1.png  style="width:600px;">

Die Beschränkung legt den Polwinkel der Linienrichtung fest. Es ist der Winkel zwischen der Linie und der X Achse der Skizze.


<div class="mw-translate-fuzzy">

### Bogenspanne (v0.15) 


</div>

**akzeptierte Auswahl:** Kreisbogen

<img alt="" src=images/Sketcher_ConsraintAngle_mode2.png  style="width:600px;">

In diesem Modus fixiert die Beschränkung die Winkelspannweite eines Kreisbogens.

### Zwischen Linien 

**Akzeptierte Auswahl:** Linie + Linie

<img alt="" src=images/Sketcher_ConsraintAngle_mode3.png  style="width:600px;">

In diesem Modus legt die Beschränkung den Winkel zwischen zwei Linien fest. Es ist nicht erforderlich, dass sich die Linien schneiden.


<div class="mw-translate-fuzzy">

### Zwischen Kurven am Schnittpunkt (Winkel-über-Punkt) (v0.15) 


</div>

**Akzeptierte Auswahl:** jede Linie/Kurve + jede Linie/Kurve + jeder Punkt

<img alt="" src=images/Sketcher_ConsraintAngle_mode4.png  style="width:600px;">

In diesem Modus wird der Winkel zwischen zwei Kurven an ihrem Schnittpunkt beschränkt. Der Schnittpunkt kann auf der Verlängerung der Kurven liegen. Der Punkt sollte explizit angegeben werden, da sich Kurven typischerweise in mehr als einem Punkt schneiden.

Damit die Beschränkung korrekt funktioniert, muss der Punkt auf beiden Kurven liegen. Wenn die Beschränkung aufgerufen wird, wird der Punkt automatisch auf beiden Kurven beschränkt ([Hilfsbeschränkungen](Sketcher_helper_constraint/de.md) wird hinzugefügt, falls erforderlich), und der Winkel zwischen den Kurven wird an dem Punkt beschränkt. Diese [Hilfsbeschränkungen](Sketcher_helper_constraint/de.md) sind einfache, gewöhnliche Beschränkungen. Sie können manuell hinzugefügt oder gelöscht werden. Auf dem obigen Beispielbild gibt es keine Hilfsbeschränkungen, da der ausgewählte Punkt bereits der Schnittpunkt von Kurven ist.

## Skripten

Winkelbeschränkung kann aus [Makros](Macros/de.md) und aus der Python Konsole wie folgt erstellt werden: 
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

:\* `Sketch` ein Skizzenobjekt ist

:\* `iline, iline1, iline2` sind ganze Zahlen, die die Zeilen durch ihre Ordnungszahlen in `Sketch` angeben.

:\* `pointpos1, pointpos2` sollte 1 für den Startpunkt und 2 für den Endpunkt sein. Die Wahl der Endpunkte ermöglicht die Einstellung des internen (oder externen) Winkels, und sie beeinflusst die Art und Weise, wie die Beschränkung auf dem Bildschirm gezeichnet wird.

:\* `geoidpoint` und `pointpos` in `AngleViaPoint` sind die Indizes, die den Schnittpunkt angeben.

:\* `angle` ist der Winkelwert im Bogenmaß. Der Winkel wird zwischen Tangentenvektoren im Gegenuhrzeigersinn gezählt. Tangentenvektoren zeigen für die Linien von Anfang bis Ende (oder umgekehrt, wenn der Endpunkt im Modus Winkel zwischen den Linien angegeben wird) und für Kreise, Bögen und Ellipsen entlang der Richtung entgegen dem Uhrzeigersinn. Die Menge wird auch als Winkel akzeptiert (z.B. `App.Units.Quantity('45 deg'))`

Die [Skizzierer Skripten](Sketcher_scripting/de.md)-Seite erklärt die Werte, die für `iline`, `iline1`, `iline2`, `pointpos1`, `pointpos2`, `geoidpoint` und `pointpos` verwendet werden können und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainAngle/de
