---
 GuiCommand:
   Name: FEM PostCreateFunctionCylinder
   Name/de: FEM NachbereitungFunktionZylinder
   MenuLocation: Ergebnisse , Filterfunktionen , Zylinder
   Workbenches: FEM_Workbench/de
   Version: 0.21
   SeeAlso: FEM_tutorial/de
---

# FEM PostCreateFunctionCylinder/de



## Beschreibung

Die Funktion <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> **FEM NachbereitungFunktionZylinder** legt die Geometrie fest, mit der ein Netzobjekt geschnitten wird. Sie wird von den Werkzeugen <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Funktion Schnitt-Filter](FEM_PostFilterCutFunction/de.md) und <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Region Ausschnitt-Filter](FEM_PostFilterClipRegion/de.md) verwendet.



## Anwendung



### Zylinderfunktion erstellen 

1.  Drücke den **<img src="images/FEM_PostCreateFunctionCylinder.svg" width=16px> [Zylinder](FEM_PostCreateFunctionCylinder/de.md)** oder wähle **Ergebnisse → Filterfunktionen → <img src="images/FEM_PostCreateFunctionCylinder.svg" width=16px> Zylinder** aus dem Menü.
2.  Das [Aufgabenfenster](Task_panel/de.md) wird geöffnet.
3.  Lege optional die Werte für den Mittelpunkt und den Radius des Schnittzylinders fest.
4.  Drücke die Schaltfläche **OK**, um den Vorgang abzuschließen.



### Zylinderfunktion bearbeiten 

Wenn der Zylinder in der [3D-Ansicht](3D_view/de.md) nicht sichtbar ist wähle in der [Baumansicht](Tree_view/de.md) das Zylinderobjekt <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> und drücke **Space**, um es sichtbar zu machen.

<img alt="" src=images/FEM_Cylinder-Cut-Function-Example.png  style="width:400px;">



#### Den Zylinder bewegen 

-   Klicke und ziehe den großen weißen Quader, um den Zylinder entlang seines Normalenvektors zu bewegen.
-   Klicke und ziehe das weiße Gitter.



#### Den Zylinder drehen und neigen 

-   Klicken und ziehe die Linie, die die kleinen Würfel mit dem großen weißen Quader verbindet, um den Zylinder um seinen Ursprung zu drehen und zu kippen.



#### Die Zylindergröße anpassen 

-   Klicke und ziehe einenn der 6 kleinen Würfel, um den Zylinder zu skalieren.



## Hinweise

-   Vorhandene Funktionen können für unterschiedliche Filter und für unterschiedliche <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [Ergebnis-Pipelines](FEM_PostPipelineFromResult/de.md) genutzt werden. Es wird allerdings dazu geraten, für jede Pipeline einen separaten Satz von Funktionen zu verwenden, um den Überblick über die Elemente in der [Baumansicht](Tree_view/de.md) zu behalten.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionCylinder/de
