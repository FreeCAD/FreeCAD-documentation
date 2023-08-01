---
- GuiCommand:
   Name:Draft Snap Center
   Name/de:Draft EinrastenAufZentrum
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   SeeAlso:[Draft Einrasten](Draft_Snap/de.md), [Draft EinrastenSperren](Draft_Snap_Lock/de.md)
---

# Draft Snap Center/de



## Beschreibung

Die Option <img alt="" src=images/Draft_Snap_Center.svg  style="width:24px;"> **Draft EinrastenAufZentrum** raste auf Mittelpunkten von Flächen oder kreisförmigen Kanten ein und auf den Punkten der {{PropertyData/de|Placement}} von [Draft ArbeitsebenenProxies](Draft_WorkingPlaneProxy/de.md) und [Arch Gebäudeteilen](Arch_BuildingPart/de.md). Die Flächen und Kanten können zu [Draft](Draft_Workbench/de.md)- oder [Arch](Arch_Workbench.md)-Objekten gehören, aber auch zu Objekten, die mit anderen [Arbeitsbereichen](Workbenches.md) erstellt wurden.

![](images/Draft_Snap_Center_example_arc.png ) 
*Einrasten des zweiten Punktes einer Linie auf dem Mittelpunkt einer kreisförmigen Kante*

![](images/Draft_Snap_Center_example_buildingpart.png ) 
*Einrasten des zweiten Punktes einer Linie auf dem Punkt der Positionierung eines Arch-Gebäudeteils*



## Anwendung

Für allgemeine Informationen zum Einrasten (Fangen) siehe [Draft Fangen](Draft_Snap/de.md).

1.  Einrasten sollte aktiviert sein. Siehe <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft EinrastenSperren](Draft_Snap_Lock/de.md).
2.  Ist **Draft EinrastenAufZentrum** nicht aktiv, gibt es folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Draft_Snap_Center.svg" width=16px>** in der Symbolleiste Draft-Einrasten drücken.
    -   Die Schaltfläche **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** im [Draft-Widget Einrasten](Draft_snap_widget/de.md) gedrückt halten und im Ausklappmenü die Option **<img src="images/Draft_Snap_Center.svg" width=16px> Zentrum fangen** auswählen.
3.  Einen [Draft](Draft_Workbench.md)- oder [Arch](Arch_Workbench.md)-Befehl auswählen, um die gewünschte Geometrie zu erstellen.
4.  Man beachte, dass die Einrast-Optionen auch dann geändert werden können, wenn ein Befehl aktiv ist.
5.  Eine der folgenden Möglichkeiten auswählen:
    -   Um einen Mittelpunkt einer Fläche oder einer kreisförmigen Kante auszuwählen:
        -   Den Mauszeiger auf eine Fläche oder Kante bewegen.
        -   Die Kante wird hervorgehoben.
    -   Um den Punkt einer {{PropertyData/de|Placement}} eines [Draft ArbeitsebenenProxys](Draft_WorkingPlaneProxy/de.md) auszuwählen:
        -   Den Mauszeiger auf ein beliebiges Element des Arbeitsebenen-Proxys bewegen.
        -   Der Arbeitsebenen-Proxy wird nicht hervorgehoben.
    -   Um den Punkt einer {{PropertyData/de|Placement}} eines [Arch Gebäudeteils](Arch_BuildingPart/de.md) auszuwählen:
        -   Den Mauszeiger auf eine der Kanten des kleinen Achsensymbols des Gebäudeteils bewegen oder auf den Text in dessen Nähe, der die {{PropertyData/de|Label}} des Gebäudeteils und sein Level anzeigt.
        -   Nur die Kanten des Achsensymbols werden hervorgehoben. Der Text wird nicht hervorgehoben.
6.  Wurde ein Punkt ermittelt, wird der Punkt markiert und das Symbol <img alt="" src=images/Draft_Snap_Center.svg  style="width:16px;"> wird neben dem Mauszeiger angezeigt.
7.  Klicken, um den Punkt zu bestätigen.



## Einstellungen

Siehe [Draft-Einrasten](Draft_Snap/de#Einstellungen.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Center/de
