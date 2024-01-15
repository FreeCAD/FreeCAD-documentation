---
 GuiCommand:
   Name: Draft LayerManager
   Name/pl: Rysunek Roboczy: Zarządzaj warstwami
   MenuLocation: Narzędzia , Zarządzaj warstwami ...
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Version: 0.21
   SeeAlso: BIM_Workbench/pl, Draft_Layer/pl
---

# Draft LayerManager/pl



## Opis

Menedżer warstw umożliwia zarządzanie [warstwami](Draft_Layer/pl.md). Warstwy są specjalnym rodzajem grupy, która kontroluje właściwości wizualne obiektów umieszczonych wewnątrz niej. Zmieniając właściwości warstwy, takie jak szerokość linii, kolor linii, kolor kształtu i przezroczystość, zmiany są przekazywane do jej obiektów podrzędnych. Warstwy nie kolidują z żadną inną strukturą FreeCAD, taką jak [grupa](Std_Group/pl.md) lub [część budowli](Arch_BuildingPart/pl.md), więc każdy obiekt może być jednocześnie częścią warstwy i częścią grupy. Warstwy są zawsze automatycznie przechowywane w specjalnej grupie \"Warstwy\".

<img alt="" src=images/BIM_layers_screenshot.png  style="width:400px;">

Warstwy są importowane i eksportowane z / do formatów [IFC](Arch_IFC/pl.md) i [DXF / DWG](Draft_DXF/pl.md).

Menedżer warstw umożliwia zarządzanie warstwami, dodawanie lub usuwanie warstw oraz zmianę ich właściwości wizualnych. Aby dodać obiekty do warstwy, wystarczy przeciągnąć je na warstwę w widoku drzewa. Aby je usunąć, przeciągnij je z warstwy i upuść w katalogu głównym dokumentu.



## Użycie

Do opracowania.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft LayerManager/pl
