---
 GuiCommand:
   Name: Sketcher CreatePointFillet
   Name/de: Sketcher PunktVerrundungErstellen
   MenuLocation: Sketch , Skizzengeometrien , Eckenerhaltende Verrundung erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **F** **P**
   Version: 0.19
   SeeAlso: Sketcher_CreateFillet/de
---

# Sketcher CreatePointFillet/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:24px;"> [Sketcher PunktVerrundungErstellen](Sketcher_CreatePointFillet/de.md) erstellt einen Bogen zwischen zwei nicht parallelen Kanten. Werden zwei gerade Kanten verrundet, die mit einer Randbedingung [Koinzident festlegen](Sketcher_ConstrainCoincident/de.md) verbunden sind, bleibt der dazugehörige gemeinsame Punkt erhalten, indem ein [Punktobjekt](Sketcher_CreatePoint/de.md) hinzugefügt wird, das jeweils durch die Randbedingung [PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md) mit beiden Kanten verbunden ist. Randbedingungen, die mit dem gemeinsamen Punkt verbunden waren, werden auf den neuen Punkt übertragen. Davon abgesehen, ist das Werkzeug indentisch mit dem Werkzeug [Verrundung erstellen](Sketcher_CreateFillet.md). Siehe dort für weitere Informationen.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Drücken Sie die **<img src="images/Sketcher_CreatePointFillet.svg" width=16px> [PunktVerrundungErstellen](Sketcher_CreatePointFillet.md)** Schaltfläche.
    -   Wählen Sie den **Sketcher → Sketcher-Geometrien → <img src="images/Sketcher_CreatePointFillet.svg" width=16px> PunktVerrundungErstellen** aus dem Menü.
    -   Klicken Sie mit der rechten Maustaste in die [3D-Ansicht](3D_view.md) und wählen Sie den **<img src="images/Sketcher_CreatePointFillet.svg" width=16px> PunktVerrundungErstellen** aus dem Kontextmenü.
    -   Verwenden Sie das Tastaturkürzel: **G** dann **F**, dann **P**.
2.  Für weitere Schritte siehe [Sketcher CreateFillet](Sketcher_CreateFillet#Usage.md).



## Hinweise

Siehe [Sketcher VerrundungErstellen](Sketcher_CreateFillet/de#Hinweise.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePointFillet/de
