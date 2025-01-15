---
 GuiCommand:Addon/pl
   Name: BIM Layers
   Name/pl: BIM: Warstwy
   MenuLocation: Zarządzanie , Warstwy
   Workbenches: BIM_Workbench/pl
---

# BIM Layers/pl



## Opis

**Menedżer warstw** umożliwia zarządzanie [warstwami](Draft_Layer/pl.md). Warstwy są specjalnym rodzajem grupy, która kontroluje właściwości wizualne obiektów umieszczonych wewnątrz niej. Zmieniając właściwości warstwy, takie jak szerokość linii, kolor linii, kolor kształtu i przezroczystość, zmiany są przekazywane do jej obiektów podrzędnych. Warstwy nie kolidują z żadną inną strukturą FreeCAD, taką jak [grupa](Std_Group/pl.md) lub [część budowli](Arch_BuildingPart/pl.md), więc każdy obiekt może być jednocześnie częścią warstwy i częścią grupy.

<img alt="" src=images/BIM_layers_screenshot.png  style="width:600px;"> 
*Menedżer warstw*

Warstwy są importowane i eksportowane z / do formatów takich jak: [IFC](Arch_IFC/pl.md) i [DXF / DWG](Draft_DXF/pl.md).

Menedżer warstw umożliwia zarządzanie warstwami, dodawanie lub usuwanie warstw oraz zmianę ich właściwości wizualnych. Aby dodać obiekty do warstwy, wystarczy przeciągnąć je na warstwę w [widoku drzewa](Tree_view/pl.md). Aby je usunąć, przeciągnij je z warstwy i upuść w katalogu głównym dokumentu.



## Natywne IFC 

To narzędzie jest dokładnie takie samo jak [Rysunek Roboczy: Menedżer warstw](Draft_LayerManager/pl.md) i tworzy ten sam obiekt warstwy. Jest tylko jedna różnica: obsługuje obiekty [Natywne IFC](NativeIFC/pl.md):

-   Ikona IFC wskazuje, czy warstwa jest częścią projektu IFC, czy nie.
-   Przycisk **Przypisz IFC** umożliwia przeniesienie warstwy do projektu IFC i przekształcenie jej w warstwę IFC.



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Layers/pl
