---
 GuiCommand:
   Name: Draft Snap Intersection
   Name/de: Draft EinrastenAufSchnittpunkt
   MenuLocation: Einrasten , Einrasten auf Schnittpunkt
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   SeeAlso: Draft_Snap/de, Draft_Snap_Lock/de
---

# Draft Snap Intersection/de



## Beschreibung

Die Option <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:24px;"> **Draft EinrastenAufSchnittpunkt** rastet auf dem Schnittpunkt zweier Kanten ein. Die Kanten können zu [Draft](Draft_Workbench/de.md)- oder [BIM](BIM_Workbench/de.md)-Objekten gehören, aber auch zu Objekten, die mit anderen [Arbeitsbereichen ](Workbenches/de.md) erstellt wurden.

Diese Einrast-Option findet offensichtliche Schnittpunkte von (verlängerten) geraden Kanten, wenn auch <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:16px;"> [Draft EinrastenAufArbeitsebene WorkingPlane](Draft_Snap_WorkingPlane/de.md) aktiv ist.

![](images/Draft_Snap_Intersection_example.png ) 
*Einrasten des zweiten Punktes einer Linie auf einem Schnittpunkt zweier Kanten*



## Anwendung

Für allgemeine Informationen zum Einrasten (Fangen) siehe [Draft Fangen](Draft_Snap/de.md).

1.  Einrasten sollte aktiviert sein. Siehe <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft EinrastenSperren](Draft_Snap_Lock/de.md).
2.  Ist **Draft EinrastenAufSchnittpunkt** nicht aktiv, gibt es folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Draft_Snap_Intersection.svg" width=16px> [Einrasten auf Schnittpunkt](Draft_Snap_Intersection/de.md)** in der Symbolleiste Draft-Einrasten drücken.
    -   [Draft](Draft_Workbench/de.md): Die Schaltfläche **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** im [Draft-Widget Einrasten](Draft_snap_widget/de.md) gedrückt halten und im Ausklappmenü die Option **<img src="images/Draft_Snap_Intersection.svg" width=16px> Einrasten auf Schnittpunkt** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Einrasten → <img src="images/Draft_Snap_Intersection.svg" width=16px> Einrasten auf Schnittpunkt** auswählen oder die Menüoption im Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen.
3.  Einen Draft- oder BIM-Befehl auswählen, um die gewünschte Geometrie zu erstellen.
4.  Man beachte, dass die Einrast-Optionen auch dann geändert werden können, wenn ein Befehl aktiv ist.
5.  Den Mauszeiger auf eine der Kanten bewegen, die sich schneiden.
6.  Die Kante wird hervorgehoben.
7.  Den Mauszeiger auf die andere Kante bewegen.
8.  Die Kante wird hervorgehoben.
9.  Wurde ein Schnittpunkt ermittelt, wird der Punkt markiert und das Symbol <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:16px;"> wird neben dem Mauszeiger angezeigt.
10. Hat die Kante mehrere Schnittpunkte: wahlweise den Mauszeiger näher an einen anderen Schnittpunkt heran bewegen.
11. Klicken, um den Punkt zu bestätigen.



## Einstellungen

Siehe [Draft-Einrasten](Draft_Snap/de#Einstellungen.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Intersection/de
