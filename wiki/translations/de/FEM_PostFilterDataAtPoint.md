---
 GuiCommand:
   Name: FEM PostFilterDataAtPoint
   Name/de: FEM DatenzuPunktSchnittfilter
   MenuLocation: Ergebnisse , FEM Daten zu Punkt Ausschnittfilter
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_PostPipelineFromResult/de, FEM_tutorial/de
---

# FEM PostFilterDataAtPoint/de



## Beschreibung

Stellt den Wert eines ausgewählten Feldes an einem bestimmten Punkt dar.



## Anwendung

1.  Wähle eine zuvor erstellte [Ergebnis-Pipeline](FEM_PostPipelineFromResult.md) oder einen anderen Filter (außer einem Linienfilter).
2.  Ruf den Befehl entweder durch:
    -   Drücken der Schaltfläche **<img src="images/FEM_PostFilterDataAtPoint.svg" width=16px> '''Daten am Punkt Ausschnitt-Filter'''**, oder,
    -   über das Menü **Ergebnisse → <img src="images/FEM_PostFilterDataAtPoint.svg" width=16px> Daten am Punkt Ausschnitt-filter** auf.
3.  Wähle ein Ergebnis **Feld**.
4.  Dann
    -   klicke entweder auf die Schaltfläche **Punkt wählen** und wähle anschließend den gewünschten Punkt im Netz, oder
    -   ändere die Punktkoordinate.

Der Wert an diesem Punkt für das angegebene **Feld** wird im Dialog ausgegeben. Der Wert des Datenpunktes ist auch jederzeit über die [Eigenschaft](Property_editor/de.md) {{PropertyData/de|Point Data}}.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterDataAtPoint/de
