---
 GuiCommand:
   Name: Part Loft
   Name: Part Ausformung
   MenuLocation: Formteil , Ausformung...
   Workbenches: Part_Workbench/de
   Version: 0.13
   SeeAlso: Part_Sweep/de
---

# Part Loft/de



## Beschreibung

Der Befel <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Part Loft](Part_Loft.md) erstellt eine Fläche, ein Schalenobjekt oder eine Festkörper-Form aus zwei oder mehr Profilen (Querschnitten).

<img alt="" src=images/Part_Loft_solid_ruled_from3profiles_example_FreeCAD_0_13.jpg  style="width:400px;"> 
*Loft-Objekt über drei Profile, zwei [Part Kreisen](Part_Circle.md) und einer [Part Ellipse](Part_Ellipse/de.md). Die Eigenschaften Solid und Ruled sind auf "True" gesetzt.*



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_Loft.svg" width=16px> [Ausformung...](Part_Loft/de.md)** drücken.
    -   Den Menüeintrag **Part → <img src="images/Part_Loft.svg" width=16px> Ausformung...** auswählen.

2.  Der [Aufgaben-Bereich](Task_panel/de.md) Ausformung (Loft) wird geöffnet.

3.  In der linken Liste *Verfügbare Profiles* das erste Profil auswählen und es dann mit dem Pfeil nach rechts in die rechte Liste *Ausgewählte Profile* verschieben.

4.  Den letzten Schritt wiederholen für das zweite Profil und nochmals für jedes weitere Profil, wenn mehr als zwei Profile verwendet werden sollen.

5.  Wahlweise die Pfeile nach oben und nach unten drücken, um die Reihenfolge der Profile zu ändern.

6.  Die Optionen [Festkörper](#Data.md), [Regelfläche](#Data.md) und [Geschlossen](#Data.md) festlegen.

7.  
    **OK**drücken.



### Akzeptierte Geometrie 

**Profile** können ein Punkt (Knoten), eine Linie (Kante), ein Kantenzug oder eine Fläche sein. Kanten und Kantenzüge können entweder offen oder geschlossen sein. Es gibt verschiedene [Einschränkungen](#Einschränkungen.md), siehe unten.

-   [App-Link](App_Link/de.md)-Objekte, die auf geeignete Objektarten verweisen und [App-Part](App_Part/de.md)-Container, die geeignete sichtbare Objekte enthalten, können auch als Profile verwendet werden. {{Version/de|0.20}}



## Optionen



#### Festkörper erstellen 

Wenn \"Festkörper erstellen\" auf \"wahr\" gesetzt ist, erstellt FreeCAD einen Festkörper, vorausgesetzt, dass die Profile geschlossen sind; wenn auf \"falsch\" gesetzt, erzeugt FreeCAD stets eine Fläche oder eine Hülle, sowohl aus offenen als auch aus geschlossenen Profilen.



#### Regelfläche

Wenn \"Regelfläche\" auf \"wahr\" gesetzt ist, erstellt FreeCAD eine Fläche, eine Hülle oder einen Festkörper aus [Regelflächen.](https://de.wikipedia.org/wiki/Regelfl%C3%A4che)



#### Geschlossen

Wenn \"Close\" \"true\" ist, versucht FreeCAD, das letzte Profil mit dem ersten Profil zu verbinden, um eine geschlossene Figur zu erzeugen.

Weitere Informationen, wie Profile miteinander verbunden werden, befinden sich auf der Seite [Part Ausformung Technische Details](Part_Loft_Technical_Details/de.md).



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Part-Loft-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Loft}}

-    {{PropertyData/de|Sections|LinkList}}: listet die verwendeten Querschnitte.

-    {{PropertyData/de|Solid|Bool}}: true oder false (Standardwert). True bewirkt, dass ein Festkörper (Solid) erstellt wird.

-    {{PropertyData/de|Ruled|Bool}}: true oder false (Standardwert). True bewirkt, dass Regelflächen erstellt werden.

-    {{PropertyData/de|Closed|Bool}}: true oder false (Standardwert). True bewirkt, dass ein geschlossenes Loft-Objekt durch Verbinden des letzten mit dem ersten Profil erstellt wird.

-    {{PropertyData/de|Max Degree|IntegerConstraint}}: Größtmöglicher Grad.



## Einschränkungen

Ein Part-Loft-Objekt hat dieselben Einschränkungen, wie ein [Part-Sweep-Objekt](Part_Sweep/de#Einschränkungen.md).



### Geschlossene Loft-Objekte 

-   Die Ergebnisse eines geschlossenen Loft-Objekts sind nicht immer wie erwartet, das Loft-Objekt kann Verdrehungen oder Knicke entwickeln. Das Austragen von Loft-Objekten reagiert sehr empfindlich auf die Positionierung der Profile und die Komplexität der Kurven, die erforderlich sind, um die zusammengehörigen Knoten in allen Profilen zu verbinden.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/de
