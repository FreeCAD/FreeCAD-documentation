---
 GuiCommand:
   Name: Part CrossSections
   Name/de: Part Querschnitte
   MenuLocation: Formteil , Schnitte...
   Workbenches: Part_Workbench/de
   SeeAlso: Part_Section/de
---

# Part CrossSections/de



## Beschreibung

Das Dienstprogramm \"Querschnitte\" erstellt einen oder mehrere Schnitte durch die ausgewählte Form, parallel zu einer der globalen (Koordinaten-)Ebenen (XY, XZ oder YZ).



## Kurzanleitung

1.  Eine Form auswählen.

2.  Die Schaltfläche **[24px|link=Part_CrossSections/de](File:Part_CrossSections.svg.md) '''Schnitte'''** drücken.

3.  Die leitende Ebene festlegen.

4.  Die Position (Höhe des Schnittes) festlegen.

5.  Wahlweise **Schnitte** aktivieren, um mehr als einen Querschnitt zu erstellen:
    -   Wird *Beidseitig* aktiviert, werden die Querschnitte auf beide Seiten der leitenden Ebene verteilt.
    -   Die Anzahl festlegen.

6.  
    **OK**drücken.

 {{Part Tools navi/de}}

-   [App-Link](App_Link/de.md)-Objekte, die mit geeigneten Objektarten verknüpft sind und [App-Part](App_Part/de.md)-Container, die geeignete sichtbare Objekte beinhalten, können auch als Ausgangsobjekte verwendet werden. {{Version/de|0.20}}
-   Das resultierende Objekt ist nicht parametrisch, d.h. es ist nicht mit der ursprünglichen Form verbunden.
-   Es wird ein einziges Objekt erstellt, sogar bei mehr als einem Querschnitt.



## Beispiel

![Select an object](images/SectionCross1.png )

![Dialog window](images/SectionCross2.png )

![Result](images/SectionCross3.png )





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CrossSections/de
