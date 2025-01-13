---
 GuiCommand:
   Name: Draft Snap Endpoint
   Name/de: Draft EinrastenAufEndpunkt
   MenuLocation: Einrasten , Einrasten auf Endpunkt
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   SeeAlso: Draft_Snap/de, Draft_Snap_Lock/de
---

# Draft Snap Endpoint/de



## Beschreibung

Die Option <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:24px;"> **Draft EinrastenAufEndpunkt** rastet auf Endpunkten von Kanten ein. Die Kanten können zu [Draft](Draft_Workbench/de.md)- oder [BIM](BIM_Workbench/de.md)-Objekten gehören, aber auch zu Objekten, die mit anderen [Arbeitsbereichen ](Workbenches/de.md) erstellt wurden.

![](images/Draft_Snap_Endpoint_example.png ) 
*Fangen des zweiten Punkts einer Linie am Endpunkt einer Kante*



## Anwendung

Für allgemeine Informationen zum Einrasten (Fangen) siehe [Draft Fangen](Draft_Snap/de.md).

1.  Einrasten sollte aktiviert sein. Siehe <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft EinrastenSperren](Draft_Snap_Lock/de.md).
2.  Ist **Draft EinrastenAufEndpunkt** nicht aktiv, gibt es folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Draft_Snap_Endpoint.svg" width=16px> [Einrasten auf Endpunkt](Draft_Snap_Endpoint/de.md)** in der Symbolleiste Draft-Einrasten drücken.
    -   [Draft](Draft_Workbench/de.md): Die Schaltfläche **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** im [Draft-Widget Einrasten](Draft_snap_widget/de.md) gedrückt halten und im Ausklappmenü die Option **<img src="images/Draft_Snap_Endpoint.svg" width=16px> Einrasten auf Endpunkt** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Einrasten → <img src="images/Draft_Snap_Endpoint.svg" width=16px> Einrasten auf Endpunkt** auswählen oder die Menüoption im Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen.
3.  Einen Draft- oder BIM-Befehl auswählen, um die gewünschte Geometrie zu erstellen.
4.  Man beachte, dass die Einrast-Optionen auch dann geändert werden können, wenn ein Befehl aktiv ist.
5.  Den Mauszeiger auf eine Kante bewegen.
6.  Die Kante wird hervorgehoben.
7.  Wurde ein Endpunkt ermittelt, wird der Punkt markiert und das Symbol <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:16px;"> wird neben dem Mauszeiger angezeigt.
8.  Wahlweise den Mauszeiger näher an den anderen Endpunkt heran bewegen, um diesen Punkt stattdessen auszuwählen.
9.  Klicken, um den Punkt zu bestätigen.



## Einstellungen

Siehe [Draft-Einrasten](Draft_Snap/de#Einstellungen.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Endpoint/de
