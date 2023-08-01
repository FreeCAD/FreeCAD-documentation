---
- GuiCommand:/de
   Name:Draft Snap Parallel
   Name/de:Draft EinrastenParallel
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   SeeAlso:[Draft Einrasten](Draft_Snap/de.md), [Draft EinrastenSperren](Draft_Snap_Lock/de.md)
---

# Draft Snap Parallel/de



## Beschreibung

Die Option <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:24px;"> **Draft EinrastenParallel** rastet auf einer gedachten Geraden parallel zu einer geraden Kante ein. Die Kanten können zu [Draft](Draft_Workbench/de.md)- oder [Arch](Arch_Workbench/de.md)-Objekten gehören, aber auch zu Objekten, die mit anderen [Arbeitsbereichen ](Workbenches/de.md) erstellt wurden.

Auf bis zu 2 (oder 8 {{Version/de|0.20}}) Kanten können diese Einrast-Option und [Draft EinrastenAufErweiterung](Draft_Snap_Extension/de.md) referenzieren, und ermöglichen so das Einrasten auf virtuelle Schnittpunkte. Beide Einrast-Optionen können auch mit anderen Einrast-Optionen kombiniert werden.

![](images/Draft_Snap_Parallel_example.png ) 
*Einrasten des zweiten Punktes einer Linie auf einer unsichtbaren Linie, die parallel zu einer Kante verläuft.*



## Anwendung

Für allgemeine Informationen zum Einrasten (Fangen) siehe [Draft Fangen](Draft_Snap/de.md).

1.  Einrasten sollte aktiviert sein. Siehe <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft EinrastenSperren](Draft_Snap_Lock/de.md).
2.  Ist **Draft EinrastenParallel** nicht aktiv, gibt es folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Draft_Snap_Parallel.svg" width=16px>** in der Symbolleiste Draft-Einrasten drücken.
    -   Die Schaltfläche **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** im [Draft-Widget Einrasten](Draft_snap_widget/de.md) gedrückt halten und im Ausklappmenü die Option **<img src="images/Draft_Snap_Parallel.svg" width=16px> Parallel fangen** auswählen.
3.  Einen [Draft](Draft_Workbench/de.md)- oder [Arch](Arch_Workbench/de.md)-Befehl auswählen, um die gewünschte Geometrie zu erstellen.
4.  Man beachte, dass die Einrast-Optionen auch dann geändert werden können, wenn ein Befehl aktiv ist.
5.  Einen ersten Punkt auswählen. Diese Einrast-Option erfordert einen vorherigen Punkt. Die parallele Einrast-Linie wird durch diesen Punkt verlaufen.
6.  Den Mauszeiger auf eine gerade Kante bewegen.
7.  Die Kante wird hervorgehoben.
8.  Wird der Mauszeiger um den vorherigen Punkt herum bewegt, kann man einen \"Magnet-\"Effekt feststellen, wenn sich der Mauszeiger auf der parallelen Einrast-Linie befindet.
9.  Der Punkt wird markiert und das Symbol <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:16px;"> wird neben dem Mauszeiger angezeigt.
10. Klicken, um den Punkt zu bestätigen.



## Einstellungen

Siehe [Draft-Einrasten](Draft_Snap/de#Einstellungen.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Parallel/de
