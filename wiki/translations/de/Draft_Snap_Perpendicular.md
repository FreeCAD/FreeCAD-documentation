---
 GuiCommand:
   Name: Draft Snap Perpendicular
   Name/de: Draft EinrastenSenkrecht
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   SeeAlso: Draft_Snap/de, Draft_Snap_Lock/de
---

# Draft Snap Perpendicular/de



## Beschreibung

Die Option <img alt="" src=images/Draft_Snap_Angle.svg  style="width:24px;"> **Draft EinrastenSenkrecht** rastet auf senkrechten Projektionen eines vorherigen Punktes auf Flächen ({{Version/de|0.21}}) oder Kanten ein. Die Flächen und Kanten können zu [Draft](Draft_Workbench.md)- oder [Arch](Arch_Workbench.md)-Objekten gehören, aber auch zu Objekten, die mit anderen [Arbeitsbereichen](Workbenches/de.md) erstellt wurden.

Diese Einrast-Option findet auch punkte auf verlängerten Flächen und Kanten.

![](images/Draft_Snap_Perpendicular_example.png ) 
*Einrasten des zweiten Punkts einer Linie auf einem Punkt senkrecht zu einer verlängerten Kante*



## Anwendung

Für allgemeine Informationen zum Einrasten (Fangen) siehe [Draft Einrasten](Draft_Snap/de.md).

1.  Einrasten sollte aktiviert sein. Siehe <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft EinrastenSperren](Draft_Snap_Lock/de.md).
2.  Ist **Draft EinrastenSenkrecht** nicht aktiv, gibt es folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Draft_Snap_Perpendicular.svg" width=16px>** in der Symbolleiste Draft-Einrasten drücken.
    -   Die Schaltfläche **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** im [Draft-Widget Einrasten](Draft_snap_widget/de.md) gedrückt halten und im Ausklappmenü die Option **<img src="images/Draft_Snap_Perpendicular.svg" width=16px> Senkrecht fangen** auswählen.
3.  Einen [Draft](Draft_Workbench/de.md)- oder [Arch](Arch_Workbench/de.md)-Befehl auswählen, um die gewünschte Geometrie zu erstellen.
4.  Man beachte, dass die Einrast-Optionen auch dann geändert werden können, wenn ein Befehl aktiv ist.
5.  Einen ersten Punkt auswählen. Diese Einrast-Option erfordert einen vorherigen Punkt. Der senkrechte Punkt wird mit Bezug auf diesen Punkt ermittelt.
6.  Den Mauszeiger auf eine Fläche oder Kante bewegen.
7.  Die Fläche bzw. Kante wird hervorgehoben.
8.  Wurde ein senkrechter Punkt ermittelt, wird der Punkt markiert und das Symbol <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:16px;"> wird neben dem Mauszeiger angezeigt.
9.  Sind mehrere senkrechte Punkte vorhanden: wahlweise den Mauszeiger näher an einen anderen Schnittpunkt heran bewegen. {{Version/de|0.21}}
10. Klicken, um den Punkt zu bestätigen.



## Einstellungen

Siehe [Draft-Einrasten](Draft_Snap/de#Einstellungen.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Perpendicular/de
