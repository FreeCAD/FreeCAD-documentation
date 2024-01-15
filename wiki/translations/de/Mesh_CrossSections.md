---
 GuiCommand:
   Name: Mesh CrossSections
   Name/de: Mesh Schnittkonturen
   MenuLocation: Netze , Schneiden , Schnitte...
   Workbenches: Mesh_Workbench/de
   Version: 0.19
   SeeAlso: Mesh_SectionByPlane/de
---

# Mesh CrossSections/de



## Beschreibung

Der Befehl **Mesh Schnittkonturen** erstellt mehrere Schnittkonturen auf Netzobjekten. Die Schnittkonturen werden parallel zu einer der globale Hauptebenen (XY, XZ oder YZ) angelegt. Für jeden Satz von Schnittkonturen wird ein einzelnes [Part Formelement](Part_Feature/de.md) erstellt.



## Anwendung

1.  Ein oder mehrere Netzobjekte auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Mesh_CrossSections.svg" width=16px> [Schnitte...](Mesh_CrossSections/de.md)** drücken.
    -   Den Menüeintrag **Vetze → Schneiden → <img src="images/Mesh_CrossSections.svg" width=16px> Schnitte...** auswählen.
3.  Der Aufgaben-Bereich **Schnitte** twird geöffnet.
4.  Die Ebenen, die verwendet werden, um die Schnittkonturen zu erstellen, werden in der [3D-Ansicht](3D_view/de.md) ausgewählt; sie werden entsprechend der Eingaben im Aufgaben-Bereich aktualisiert.
5.  Die **Führungsebene** (Bezugsebene) auswählen:
    -   
        **XY**
        

    -   
        **XZ**
        

    -   
        **YZ**
        
6.  Die **Position** (Abstand) von der Bezugsebene festlegen. Der voreingestellte Abstand basiert auf dem Mittelpunkt des Begrenzungsrahmens des ausgewählten Netzobjekts. Die Auswahl einer anderen **Führungsebene** oder das Umschalten der Checkbox **Schnitte** setzt die **Positon** auf die Vorgabewerte zurück.
7.  Wahlweise die Checkbox **Schnitte** aktivieren, um mehrere Schnittkonturen zu erstellen:
    -   
        **Beidseitig**
        
        : Wenn aktiviert, werden Schnittkonturen auf beiden Seiten der Bezugsebene erstellt.

    -   
        **Anzahl**
        
        : die Anzahl der Schnittkonturen.

    -   
        **Entfernung**
        
        : Der Abstand zwischen den Schnittkonturen. Der Vorgabewert basiert auf den Abmaßen des Begrenzungsrahmens, der Option **Beidseitig** und dem Wert **Anzahl**. Das Ändern des Wertes **Anzahl** setzt den Wert **Entfernung** zurück auf diesen Vorgabewert. Das Ändern des Wertes **Beidseiteg** berechnet die **Entfernung** neu ({{value|*2.0}} oder {{value|*0.5}}). Achtung, das Eingabefeld kann ausgegraut sein, aber der Wert kann trotzdem angepasst werden.

    -   Wahlweise Checkbox **Kanten verbinden, wenn die Distanz kleiner ist als** aktivieren und einen Wert festlegen.
8.  Die Schaltfläche {{button|Anwenden}} drücken, um einen Satz Schnittkonturen zu erstellen.
9.  Wahlweise eine oder mehrere Einstellungen anpassen und weitere Schnittkonturen zu erstellen.
10. Die Schaltfläche {{button|OK}} oder die Schaltfläche {{button|Abbrechen}} drücken, um den Aufgaben-Bereich zu schließen und den Befehl abzuschließen.



## Eigenschaften

Siehe [Part Formelement](Part_Feature/de.md).





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh CrossSections/de
