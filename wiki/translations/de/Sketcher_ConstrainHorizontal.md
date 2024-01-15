---
 GuiCommand:
   Name: Sketcher ConstrainHorizontal
   Name/de: Sketcher HorizontalFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Horizontal festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **H**
   SeeAlso: Sketcher_ConstrainVertical/de
---

# Sketcher ConstrainHorizontal/de



## Beschreibung

Die Randbedingung HorizontalFestlegen legt fest, dass eine oder mehrere gewählte Linien parallel zur horizontalen Achse der Skizze verlaufen.



## Anwendung

<img alt="" src=images/HorizontalConstraint1.png  style="width:500px;"> 
*Wähle eine Linie in der Skizze durch daraufklicken aus.*

<img alt="" src=images/HorizontalConstraint2.png  style="width:500px;"> 
*Die Linie wird dunkelgrün.*

<img alt="" src=images/HorizontalConstraint3.png  style="width:500px;"> 
*Die Randbedingung HorizontalFestlegen durch das Anklicken der Schaltfläche **[<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> [Horizontal einschränken](Sketcher_ConstrainHorizontal/de.md)* in der Sketcher-Werkzeugleiste für Randbedingungen oder durch Auswahl des Menüeintrags Horizontal einschränken im Untermenü Skizzen-Beschränkungen des Menüpunkts Sketch im Arbeitsbereich Sketcher (oder des Part Design Menüpunkts des Arbeitsbereichs PartDesign). Die ausgewählte Linie wird so festgelegt, dass sie parallel zur horizontalen Achse der Skizze verläuft.**

<img alt="" src=images/HorizontalConstraint4.png  style="width:500px;"> 
*Mehrere Linien können ausgewählt werden
*

<img alt="" src=images/HorizontalConstraint5.png  style="width:500px;"> 
*und dann die Beschränkung wie oben beschrieben anwenden, sie werden so eingeschränkt, dass sie parallel zur horizontalen Achse der Skizze liegen.
*



## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

Die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) erklärt die Werte, die für `Line` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/de
