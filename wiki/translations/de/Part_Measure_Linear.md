---
- GuiCommand:
   Name: Part Measure Linear
   Name/de: Part Messung Abstand
   MenuLocation: Messen -> Linear messen
   Workbenches: Part_Workbench/de
   SeeAlso: Std_MeasureDistance/de, Draft_Dimension/de
---

# Part Measure Linear/de



## Beschreibung

Dieser Befehl misst den Abstand zwischen zwei ausgewählten topologischen Elementen (Eckpunkt, Kante, Fläche) und zeigt Maße in der [3D Ansicht](3D_view/de.md) an. Der kürzeste Abstand zwischen den beiden Elementen und die Delta-Abstände parallel zu den globalen X-,Y-, Z-Achsen werden dargestellt.

Die Darstellung der Maße kann in den [Einstellungen](PartDesign_Preferences/de#Messen.md) angepasst werden.

<img alt="" src=images/MeasureLinear3D1.png  style="width:400px;"> <img alt="" src=images/MeasureLinearDelta1.PNG  style="width:400px;">



## Anwendung

1.  Eine beliebige Kombination zweier Elemente (Eckpunkte, Kanten, Flächen) auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_Measure_Linear.svg" width=16px> [Linear messen](Part_Measure_Linear/de.md)** drücken.
    -   Den Menüeintrag **Messen → <img src="images/Part_Measure_Linear.svg" width=16px> Linear messen** auswählen.
3.  Alternativ kann der Befehl ohne vorherige Auswahl gestartet werden. Dann öffnet sich ein Auswahldialog im [Aufgabenbereich](Task_panel/de.md). Ein Steuerungswidget bietet ebenfalls Schaltflächen zum Zurücksetzen der Auswahl, zum Umschalten der Maßdarstellung in der [3D-Ansicht](3D_view/de.md) und zum Löschen aller Maße.
4.  Messungen werden automatisch beim Schließen des Dokuments verworfen.



## Hinweise

-   Die Fangwerkzeuge des Arbeitsbereichs [Draft](Draft_Workbench/de.md) können nicht mit diesem Befehl zusammen verwendet werden.
-   Um einer Zeichnung Maße hinzuzufügen, werden die Bemaßungswerkzeuge des Arbeitsbereichs [TechDraw](TechDraw_Workbench/de.md) verwendet.
-   Für umfangreichere Messwerkzeuge kann der [externe Arbeitsbereich](External_workbenches/de.md) <img alt="" src=images/Manipulator_workbench_icon.svg  style="width:24px;"> [Manipulator](Manipulator_Workbench/de.md) installiert werden.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Measure Linear/de
