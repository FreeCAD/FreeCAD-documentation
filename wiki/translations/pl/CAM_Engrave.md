---
 GuiCommand:
   Name: CAM Engrave
   Name/pl: CAM: Grawer
   MenuLocation: CAM , Grawer
   Workbenches: CAM_Workbench/pl
---

# CAM Engrave/pl



## Opis

Narzędzie <img alt="" src=images/CAM_Engrave.svg  style="width:24px;"> [Grawer](CAM_Engrave/pl.md) służy głównie do grawerowania obiektów <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;"> [Rysunek Roboczy: Kształt z tekstu](Draft_ShapeString/pl.md) na częściach. Może być jednak użyteczne do innych operacji 2D.



## Użycie

Pusto



## Opcje

Pusto



## Właściwości



### Dane


{{TitleProperty|Podstawa}}

-    **Placement**:

-    **Label**: Dostosowywalna nazwa obiektu (UTF-8)


{{TitleProperty|Głębokość}}

-    **Clearance Height**: Wysokość potrzebna do ominięcia zacisków i przeszkód

-    **Final Depth**: Ostateczna głębokość narzędzia - najniższa wartość w osi Z

-    **Safe Height**: Wysokość, powyżej której dozwolone są ruchy szybkie

-    **Start Depth**: Początkowa głębokość narzędzia - pierwsza głębokość cięcia w osi Z

-    **Step Down**: Przyrostowa głębokość narzędzia


{{TitleProperty|Ścieżka}}

-    **Active**: Ustaw na Fałsz, aby zapobiec generowaniu kodu dla tej operacji

-    **Base**: Geometria bazowa dla tej operacji

-    **Comment**: Opcjonalny komentarz do tej operacji

-    **Coolant Mode**: Tryb chłodzenia dla tej operacji

-    **Cycle Time**: Szacowany czas cyklu dla tej operacji

-    **Start Vertex**: Indeks wierzchołka, od którego zaczyna się ścieżka

-    **Tool Controller**: Kontroler narzędziowy, który będzie używany do obliczenia ścieżki

-    **User Label**: Etykieta przypisana przez użytkownika


{{TitleProperty|Ukryte}}

-    **Base Object**:

-    **Base Shapes**:

-    **Expression Engine**:

-    **Label2**:

-    **Path**:

-    **Proxy**:

-    **Visibility**:



### Widok

Pusto



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Przykład:


```python
#Place code example here.
```





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Engrave/pl
