---
 GuiCommand:
   Name: Draft Snap Near
   Name/de: Draft EinrastenInDerNähe
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   SeeAlso: Draft_Snap/de, Draft_Snap_Lock/de
---

# Draft Snap Near/de



## Beschreibung

Die Option <img alt="" src=images/Draft_Snap_Near.svg  style="width:24px;"> **Draft EinrastenInDerNähe** rastet auf dem am nächsten gelegenen Punkt einer Fläche oder einer Kante ein. Die Flächen und Kanten können zu [Draft](Draft_Workbench/de.md)- oder [Arch](Arch_Workbench/de.md)-Objekten gehören, aber auch zu Objekten, die mit anderen [Arbeitsbereichen erstellt wurden](Workbenches/de.md).

![](images/Draft_Snap_Near_example.png ) 
*Fängt den zweiten Punkt einer Linie zum nächsten Punkt einer Kante*



## Anwendung

Zu allgemeinen Informationen zum Fangen siehe [Draft Fang](Draft_Snap/de.md).

1.  Einrasten sollte aktiviert sein. Siehe <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft EinrastenSperren](Draft_Snap_Lock/de.md).
2.  Ist **Draft EinrastenInDerNähe** nicht aktiv, gibt es folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Draft_Snap_Near.svg" width=16px>** in der Symbolleiste Draft-Einrasten drücken.
    -   Die Schaltfläche **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** im [Draft-Widget Einrasten](Draft_snap_widget/de.md) gedrückt halten und im Ausklappmenü die Option **<img src="images/Draft_Snap_Near.svg" width=16px> In der Nähe fangen** auswählen.
3.  Einen [Draft](Draft_Workbench/de.md)- oder [Arch](Arch_Workbench/de.md)-Befehl auswählen, um die gewünschte Geometrie zu erstellen.
4.  Man beachte, dass die Einrast-Optionen auch dann geändert werden können, wenn ein Befehl aktiv ist.
5.  Den Mauszeiger auf eine Fläche oder Kante bewegen.
6.  Die Fläche bzw. Kante wird hervorgehoben.
7.  Wurde ein am nächsten gelegener Punkt ermittelt, wird der Punkt markiert.
8.  Wahlweise den Mauszeiger entlang der Fläche oder Kante bewegen, um einen anderen am nächsten gelegenen Punkt auszuwählen.
9.  Klicken, um den Punkt zu bestätigen.



## Hinweise

-   Es ist keine gute Idee, [Draft EinrastenInDerNähe](Draft_Snap_Near/de.md) permanent zu aktivieren, da es Vorrang vor vielen anderen Einrast-Optionen erhält.
-   Wird in {{VersionMinus/de|0.20}} auf Kurven eingerastet, rastet [Draft EinrastenInDerNähe](Draft_Snap_Near/de.md) auf deren unterteilten Repräsentanten in der [3D-Ansicht](3D_view/de.md) ein, woraus sich eine Abweichung ergibt. Um einen exakten Kurvenpunkt zu erhalten, zieht man eine [Draft Linie](Draft_Line/de.md) quer über die Kurve und schneidet dann die Linie mit [Draft Trimex](Draft_Trimex/de.md), wobei die Kurve als Schneidwerkzeug verwendet wird.



## Einstellungen

Siehe [Draft Fang Einstellungen](Draft_Snap/de#Einstellungen.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Near/de
