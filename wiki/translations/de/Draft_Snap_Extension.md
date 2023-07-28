---
- GuiCommand:/de
   Name:Draft Snap Extension
   Name/de:Draft EinrastenAufVerlängerung
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   SeeAlso:[Draft Einrasten](Draft_Snap/de.md), [Draft EinrastenSperren](Draft_Snap_Lock/de.md)
---

# Draft Snap Extension/de



## Beschreibung

Die Option <img alt="" src=images/Draft_Snap_Extension.svg  style="width:24px;"> **Draft EinrastenAufVerlängerung** rastet auf einer gedachten Geraden außerhalb der Endpunkte einer geraden Kante ein. Die Kanten können zu [Draft](Draft_Workbench/de.md)- oder [Arch](Arch_Workbench/de.md)-Objekten gehören, aber auch zu Objekten, die mit anderen [Arbeitsbereichen ](Workbenches/de.md) erstellt wurden.

Auf bis zu 2 (oder 8 {{Version/de|0.20}}) Kanten können diese Einrast-Option und [Draft EinrastenParallel](Draft_Snap_Extension/de.md) referenzieren, und ermöglichen so das Einrasten auf virtuelle Schnittpunkte. Beide Einrast-Optionen können auch mit anderen Einrast-Optionen kombiniert werden.

![](images/Draft_Snap_Extension_example.png ) 
*Einrasten des zweiten Punktes einer Linie auf der Verlängerung einer Kante*



## Anwendung

Für allgemeine Informationen zum Einrasten (Fangen) siehe [Draft Einrasten](Draft_Snap/de.md).

1.  Einrasten sollte aktiviert sein. Siehe <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft EinrastenSperren](Draft_Snap_Lock/de.md).
2.  Ist **Draft EinrastenAufVerlängerung** nicht aktiv, gibt es folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Draft_Snap_Extension.svg" width=16px>** in der Symbolleiste Draft-Einrasten drücken.
    -   Die Schaltfläche **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** im [Draft-Widget Einrasten](Draft_snap_widget/de.md) gedrückt halten und im Ausklappmenü die Option **<img src="images/Draft_Snap_Extension.svg" width=16px> Einrast-Erweiterung** auswählen.
3.  Einen [Draft](Draft_Workbench.md)- oder [Arch](Arch_Workbench.md)-Befehl auswählen, um die gewünschte Geometrie zu erstellen.
4.  Man beachte, dass die Einrast-Optionen auch dann geändert werden können, wenn ein Befehl aktiv ist.
5.  Den Mauszeiger auf eine gerade Kante bewegen.
6.  Die Kante wird hervorgehoben.
7.  Wird der Mauszeiger jetzt hinter die Endpunkte der Kante bewegt, erscheint eine Strichlinie, sobald sich der Mauszeiger auf der verlängerten Kante befindet.
8.  Der Punkt wird markiert und das Symbol <img alt="" src=images/Draft_Snap_Extension.svg  style="width:16px;"> wird neben dem Mauszeiger angezeigt.
9.  Klicken, um den Punkt zu bestätigen.



## Einstellungen

Siehe [Draft-Einrasten](Draft_Snap/de#Einstellungen.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Extension/de
