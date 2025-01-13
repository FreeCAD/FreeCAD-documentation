---
 GuiCommand:
   Name: FEM PostFilterCutFunction
   Name/de: FEM NachbereitungFilterSchnittebene
   MenuLocation: Ergebnisse , Funktion Schnitt-Filter
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_PostPipelineFromResult/de, FEM_PostCreateFunctions/de, FEM_tutorial/de
---

# FEM PostFilterCutFunction/de



## Beschreibung

Zeigt die Ergebnisse auf einer Fläche die entweder durch eine Kugel, eine Ebene, einen Zylinder oder Würfel erzeugt wird.

<img alt="" src=images/FEM_Function-Cut-Filter-Example.png  style="width:400px;">

*Ein Funktionsschnittfilter mit einer Kugel als Schnittfunktion.Die ursprüngliche Pipeline ist das halbtransparente Objekt.*



## Anwendung

1.  Wähle eine zuvor erstellte [Ergebnis-Pipeline](FEM_PostPipelineFromResult/de.md).
2.  Rufe den Befehl entweder durch:
    -   Drücken der Schaltfläche **<img src="images/FEM_PostFilterCutFunction.svg" width=16px> '''Funktion Schnittfilter'''**, oder über
    -   das Menü **Ergebnisse → <img src="images/FEM_PostFilterCutFunction.svg" width=16px> Funktion Schnittfilter** auf.
3.  Passe die **Anzeigeoptionen** wie bei der [Ergebnis Pipeline](FEM_PostPipelineFromResult/de.md) an. Möglicherweise muss die Pipeline ausgeblendet werden, um die Wirkung des Filters in der Vorschau zu sehen.
4.  Entweder
    -   Wenn noch keine [Filterfunktion](FEM_PostCreateFunctions.md) definiert ist, drücke **<img src="images/List-add.svg" width=16px> Erstellen
** und wähle **<img src="images/FEM_PostCreateFunctionPlane.svg" width=16px> Ebene** oder **<img src="images/FEM_PostCreateFunctionSphere.svg" width=16px> Sphäre**
    -   Wähle eine vorhandene Filterfunktion aus der Liste. Passe bei Bedarf die Schnittparameter an, um sicherzustellen, dass sie das Modell schneidet. Beachte, dass geänderte Schnittparameter auch die Parameter der verwendeten Filterfunktion ändern.
5.  Die Ergebnisse werden auf der Oberfläche der Filterfunktion angezeigt.
6.  Klicke auf die Schaltfläche **OK**, um den Befehl zu beenden.

**Hinweis**: Ein **Feld** kann nur gesetzt werden, wenn eine Filterfunktion existiert und mit <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:16px;"> [Änderungen anwenden](FEM_PostApplyChanges/de.md) bestätigt wurde. Alternativ kann der Filterdialog erneut geöffnet werden.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterCutFunction/de
