---
- GuiCommand   */de
   Name   *Sketcher ConstrainHorizontal
   Name/de   *Skizzierer BeschränkeHorizontal
   MenuLocation   *Skizze → Skizzierer Beschränkungen → Beschränke Horizontal
   Workbenches   *[Skizzierer](Sketcher_Workbench/de.md)
   Shortcut   ***H**
   SeeAlso   *[Beschränkung Vertikal](Sketcher_ConstrainVertical/de.md)
---

# Sketcher ConstrainHorizontal/de

## Beschreibung

Die Einschränkung \'Horizontal\' sorgt dafür, dass eine oder mehrere gewählte Linien parallel zur horizontalen Achse der Skizze sind.

## Anwendung

<img alt="" src=images/HorizontalConstraint1.png  style="width   *500px;"> 
*Wähle eine Linie in der Skizze durch daraufklicken aus.*

<img alt="" src=images/HorizontalConstraint2.png  style="width   *500px;"> 
*Die Linie wird dunkelgrün.*


<div class="mw-translate-fuzzy">

<img alt="" src=images/HorizontalConstraint3.png  style="width   *500px;"> 
*Wende die horizontale Beschränkung durch anklicken auf **[<img src=images/Sketcher_ConstrainHorizontal.svg style="width   *16px"> [Beschränkung horizontal](Sketcher_ConstrainHorizontal/de.md)* in der Skizzierer Beschränkungs Werkzeugleiste oder durch Auswahl des Menüpunkts Horizontal beschränken im Untermenü Skizzierer Beschränkungen des Skizzierer Menüpunkts im Skizzierer Arbeitsbereich (oder des Part Design Menüpunkts des Part Design Arbeitsbereichs). Die ausgewählte Linie wird so beschränkt, dass sie parallel zur horizontalen Achse der Skizze verläuft.**


</div>

<img alt="" src=images/HorizontalConstraint4.png  style="width   *500px;"> 
*Mehrere Linien können ausgewählt werden
*

<img alt="" src=images/HorizontalConstraint5.png  style="width   *500px;"> 
*und dann die Beschränkung wie oben beschrieben anwenden, sie werden so eingeschränkt, dass sie parallel zur horizontalen Achse der Skizze liegen.
*

## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

Die [Skizzierer Skripten](Sketcher_scripting.md)-Seite erklärt die Werte, die für `Line` verwendet werden können und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/de
