---
 GuiCommand:
   Name: Draft Snap WorkingPlane
   Name/de: Draft EinrastenAufArbeitsebene
   MenuLocation: Einrasten , Einrasten auf Arbeitsebene
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   SeeAlso: Draft_Snap/de, Draft_Snap_Lock/de, Draft_SelectPlane/de
---

# Draft Snap WorkingPlane/de



## Beschreibung

Die Option <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:24px;"> **Draft EinrastenAufArbeitsebene** projiziert Einrast-Punkte auf die aktuelle [Arbeitsebene](Draft_SelectPlane/de.md). Sie kann nur in Kombination mit anderen Einrast-Optionen verwendet werden.

![](images/Draft_Snap_WorkingPlane_example.png ) 
*Einrasten des zweiten Punktes einer Linie auf den projizierten Endpunkt einer Kante*



## Anwendung

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Wahlweise die [Arbeitsebene](Draft_SelectPlane/de.md) wechseln.
2.  Einrasten sollte aktiviert sein. Siehe <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft EinrastenSperren](Draft_Snap_Lock/de.md).
3.  Ist **Draft EinrastenAufArbeitsebene** nicht aktiv, gibt es folgende Möglichkeiten:
    -   Die Schaltfläche **<img src="images/Draft_Snap_WorkingPlane.svg" width=16px> [Einrasten auf Arbeitsebene](Draft_Snap_WorkingPlane/de.md)** in der Symbolleiste Draft-Einrasten drücken.
    -   [Draft](Draft_Workbench/de.md): Die Schaltfläche **<img src="images/Draft_Snap_WorkingPlane.svg" width=16px> [Einrasten auf Arbeitsebene](Draft_Snap_WorkingPlane/de.md)** im [Draft-Widget Einrasten](Draft_snap_widget/de.md) drücken.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Einrasten → <img src="images/Draft_Snap_WorkingPlane.svg" width=16px> Einrasten auf Arbeitsebene** auswählen oder dei Menüoption im Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Sicherstellen, dass mindestens eine weitere Einrast-Option aktiviert ist.
5.  Einen Draft- oder BIM-Befehl auswählen, um die gewünschte Geometrie zu erstellen.
6.  Man beachte, dass die Einrast-Optionen auch dann geändert werden können, wenn ein Befehl aktiv ist.
7.  Den Mauszeiger auf das Objekt bewegen, auf das eingerastet wrden soll.
8.  Das Objekt wird hervorgehoben.
9.  Wurde ein Einrast-Punkt ermittelt, wird er auf die [Arbeitsebene](Draft_SelectPlane/de.md) projiziert und dort markiert.
10. Klicken, um den Punkt zu bestätigen.



## Einstellungen

Siehe [Draft-Einrasten](Draft_Snap/de#Einstellungen.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap WorkingPlane/de
