---
- GuiCommand:
   Name: Draft Snap Ortho
   Name/de: Draft EinrastenOrtho
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   SeeAlso: Draft_Snap/de, Draft_Snap_Lock/de
---

# Draft Snap Ortho/de



## Beschreibung

Die Option <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:24px;"> **Draft EinrastenOrtho** rastet auf gedachten Linien ein, die unter Winkeln, die Vielfache von 45° sind, durch den vorhergehenden Punkt verlaufen. Die Linien und Winkel sind mit Bezug zur XY-Ebene des Koordinatensystems der [Arbeitsebene](Draft_SelectPlane/de.md) angeordnet.

![](images/Draft_Snap_Ortho_example.png ) 
*Einrasten des zweiten Punktes einer Linie auf eine gedachte Linie, die unter einem Winkel von 45° zur X-Achse verläuft; die kleinen magentafarbenen Kreise zeigen alle möglichen Richtungen an.*



## Anwendung

Für allgemeine Informationen zum Einrasten (Fangen) siehe [Draft Einrasten](Draft_Snap/de.md).

1.  Einrasten sollte aktiviert sein. Siehe <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft EinrastenSperren](Draft_Snap_Lock/de.md).
2.  Ist **Draft EinrastenOrtho** nicht aktiv, gibt es folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Draft_Snap_Ortho.svg" width=16px>** in der Symbolleiste Draft-Einrasten drücken.
    -   Die Schaltfläche **<img src="images/Draft_Snap_Ortho.svg" width=16px>** im [Draft-Widget Einrasten](Draft_snap_widget/de.md) drücken.
3.  Einen [Draft](Draft_Workbench/de.md)- oder [Arch](Arch_Workbench/de.md)-Befehl auswählen, um die gewünschte Geometrie zu erstellen.
4.  Man beachte, dass die Einrast-Optionen auch dann geändert werden können, wenn ein Befehl aktiv ist.
5.  Einen ersten Punkt auswählen. Diese Einrast-Option erfordert einen vorherigen Punkt.
6.  Wird der Mauszeiger um den vorherigen Punkt herum bewegt, kann man einen \"Magnet-\"Effekt feststellen, wenn sich der Mauszeiger auf einer gedachten Geraden befindet, die unter einem Winkel von 0°, 45°, 90° oder 135° durch diesen Punkt verläuft.
7.  Der Punkt wird markiert und das Symbol <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:16px;"> wird neben dem Mauszeiger angezeigt.
8.  Klicken, um den Punkt zu bestätigen.



## Einstellungen

Siehe [Draft-Einrasten](Draft_Snap/de#Einstellungen.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Ortho/de
