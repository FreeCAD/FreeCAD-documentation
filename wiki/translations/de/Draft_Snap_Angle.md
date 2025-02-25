---
 GuiCommand:
   Name: Draft Snap Angle
   Name/de: Draft EinrastenAufWinkel
   MenuLocation: Einrasten , Einrastwinkel
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   SeeAlso: Draft_Snap/de, Draft_Snap_Lock/de
---

# Draft Snap Angle/de



## Beschreibung

Die Option <img alt="" src=images/Draft_Snap_Angle.svg  style="width:24px;"> **Draft EinrastenAufWinkel** rastet auf besonderen Hauptpunkten auf kreisförmigen Kanten ein, auf Winkeln, die ein Vielfaches von 30° and 45° sind. Die Kanten können zu [Draft](Draft_Workbench.md)- oder [BIM](BIM_Workbench/de.md)-Objekten gehören, aber auch zu Objekten, die mit anderen [Arbeitsbereichen](Workbenches/de.md) erstellt wurden.

![](images/Draft_Snap_Angle_example.png ) 
*Einrasten des zweiten Punktes einer Linie auf den Punkt bei -30° auf einer kreisförmigen Kante. Die kleinen magentefarbenen Kreise weisen auf alle zur Verfügung stehenden Hauptpunkte an.*



## Anwendung

Für allgemeine Informationen zum Einrasten (Fangen) siehe [Draft Fangen](Draft_Snap/de.md).

1.  Einrasten sollte aktiviert sein. Siehe <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft EinrastenSperren](Draft_Snap_Lock/de.md).
2.  Ist **Draft EinrastenAufWinkel** nicht aktiv, gibt es folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Draft_Snap_Angle.svg" width=16px> [Einrastwinkel](Draft_Snap_Angle/de.md)** in der Symbolleiste Draft-Einrasten drücken.
    -   [Draft](Draft_Workbench/de.md): Die Schaltfläche **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** im [Draft-Widget Einrasten](Draft_snap_widget/de.md) gedrückt halten und im Ausklappmenü die Option **<img src="images/Draft_Snap_Angle.svg" width=16px> Einrastwinkel** auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Einrasten → <img src="images/Draft_Snap_Angle.svg" width=16px> Einrastwinkel** auswählen oder die Menüoption im Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen.
3.  Einen Draft- oder BIM-Befehl auswählen, um die gewünschte Geometrie zu erstellen.
4.  Man beachte, dass die Einrast-Optionen auch dann geändert werden können, wenn ein Befehl aktiv ist.
5.  Den Mauszeiger auf eine kreisförmige Kante bewegen.
6.  Die Kante wird hervorgehoben.
7.  Wurde ein Hauptpunkt ermittelt, wird der Punkt markiert und das Symbol <img alt="" src=images/Draft_Snap_Angle.svg  style="width:16px;"> wird neben dem Mauszeiger angezeigt.
8.  Wahlweise den Mauszeiger näher an einen anderen Hauptpunkt heran bewegen, um diesen Punkt stattdessen auszuwählen.
9.  Klicken, um den Punkt zu bestätigen.



## Einstellungen

Siehe [Draft-Einrasten](Draft_Snap/de#Einstellungen.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Angle/de
