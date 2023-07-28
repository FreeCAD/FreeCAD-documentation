---
- GuiCommand:/de
   Name:Draft Snap Intersection
   Name/de:Draft EinrastenAufSchnittpunkt
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   SeeAlso:[Draft Einrasten](Draft_Snap/de.md), [Draft EinrastenSperren](Draft_Snap_Lock/de.md)
---

# Draft Snap Intersection/de



## Beschreibung

Die Option <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:24px;"> **Draft EinrastenAufSchnittpunkt** rastet auf dem Schnittpunkt zweier Kanten ein. Die Kanten können zu [Draft](Draft_Workbench/de.md)- oder [Arch](Arch_Workbench/de.md)-Objekten gehören, aber auch zu Objekten, die mit anderen [Arbeitsbereichen ](Workbenches/de.md) erstellt wurden.

Diese Einrast-Option findet offensichtliche Schnittpunkte von (verlängerten) geraden Kanten, wenn auch <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:16px;"> [Draft EinrastenAufArbeitsebene WorkingPlane](Draft_Snap_WorkingPlane/de.md) aktiv ist.

![](images/Draft_Snap_Intersection_example.png ) 
*Einrasten des zweiten Punktes einer Linie auf einem Schnittpunkt zweier Kanten*



## Anwendung

Für allgemeine Informationen zum Einrasten (Fangen) siehe [Draft Fangen](Draft_Snap/de.md).

1.  Einrasten sollte aktiviert sein. Siehe <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft EinrastenSperren](Draft_Snap_Lock/de.md).
2.  Ist *\'Draft EinrastenAufSchnittpunkt* nicht aktiv, gibt es folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Draft_Snap_Intersection.svg" width=16px>** in der Symbolleiste Draft-Einrasten drücken.
    -   Die Schaltfläche **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** im [Draft-Widget Einrasten](Draft_snap_widget/de.md) gedrückt halten und im Ausklappmenü die Option **<img src="images/Draft_Snap_Intersection.svg" width=16px> Schnittstelle fangen** auswählen.
3.  Einen [Draft](Draft_Workbench/de.md)- oder [Arch](Arch_Workbench/de.md)-Befehl auswählen, um die gewünschte Geometrie zu erstellen.
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
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Intersection/de
