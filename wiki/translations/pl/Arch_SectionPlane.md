---
 GuiCommand:
   Name: Arch SectionPlane
   Name/pl: BIM: Płaszczyzna przekroju
   MenuLocation: Opisy , Płaszczyzna przekroju
   Workbenches: BIM_Workbench/pl
   Shortcut: **S** **P**
   SeeAlso: Draft_Shape2DView/pl
---

# Arch SectionPlane/pl



## Opis

Narzędzie **Płaszczyzna przekroju** umieszcza w bieżącym dokumencie płaszczyznę przekroju \"rzecz\", która definiuje przekrój lub płaszczyznę widoku. \"Rzecz\" przyjmuje swoje położenie zgodnie z bieżącą [płaszczyzną przekroju](Draft_SelectPlane/pl.md) i może być przenoszona i zmieniana jej orientacja poprzez przesuwanie i obracanie, aż opisze widok 2D, który chcesz uzyskać. Obiekt płaszczyzny przekroju uwzględnia tylko określony zestaw obiektów. Obiekty wybrane podczas tworzenia płaszczyzny przekroju zostaną automatycznie dodane do tego zestawu. Inne obiekty mogą być później dodawane lub usuwane z obiektu Płaszczyzny przekroju za pomocą narzędzi [Połącz obiekty](Arch_Add/pl.md) i [Usuń komponent](Arch_Remove/pl.md) lub poprzez dwukrotne kliknięcie Płaszczyzny przekroju w widoku drzewa.

Sama Płaszczyzna przekroju nie utworzy żadnego widoku swojego zestawu obiektów. W tym celu należy utworzyć [Widok architektury](TechDraw_ArchView/pl.md), aby utworzyć widok na stronie [rysunku technicznego](TechDraw_Workbench/pl.md).

<img alt="" src=images/Arch_SectionPlane_example.jpg  style="width:600px;">



## Użycie

1.  Opcjonalnie ustaw [płaszczyzne roboczą](Draft_SelectPlane/pl.md), aby odzwierciedlała płaszczyznę, na której chcesz umieścić płaszczyznę przekroju.
2.  Wybierz obiekty, które chcesz uwzględnić w widoku przekroju.
3.  Naciśnij przycisk **<img src="images/Arch_SectionPlane.svg" width=16px> '''Płaszczyzna przekroju'''** lub naciśnij **S**, a następnie **P**.
4.  Ustaw płaszczyznę przekroju we właściwej pozycji [przesuwając](Draft_Move/pl.md) / [obracając](Draft_Rotate/pl.md), jeśli to konieczne.
5.  Wybierz płaszczyznę przekroju, jeśli nie została jeszcze wybrana.
6.  Użyj narzędzia [Widok 2D kształtu](Draft_Shape2DView/pl.md) lub [Wstaw obiekt środowiska Architektura](TechDraw_ArchView/pl.md), aby utworzyć widok.



## Opcje

-   Obiekt Płaszczyzny przekroju będzie uwzględniał tylko określony zestaw obiektów, a nie wszystkie obiekty dokumentu. Obiekty mogą być dodawane lub usuwane z obiektu Płaszczyzny przekroju za pomocą narzędzi [Połącz obiekty](Arch_Add/pl.md) i [Usuń komponent](Arch_Remove/pl.md) lub poprzez dwukrotne kliknięcie Płaszczyzny przekroju w widoku drzewa, wybranie obiektów na liście lub w scenie 3D i naciśnięcie przycisków **dodaj** lub **usuń**.

-   Po wybraniu obiektu płaszczyzny przekroju użyj narzędzia [Widok 2D kształtu](Draft_Shape2DView/pl.md), aby utworzyć obiekt kształtu reprezentujący widok przekroju w dokumencie.

<img alt="" src=images/Arch_Section_example2.jpg  style="width:600px;">

-   Utwórz [widok architektury](TechDraw_ArchView/pl.md).

<img alt="" src=images/Arch_Section_example3.jpg  style="width:600px;">

-   Płaszczyzna przekroju może być również użyta do pokazania całego widoku 3D przeciętego nieskończoną płaszczyzną. Ma to jedynie charakter wizualny i nie wpływa na geometrię przecinanych obiektów.

<img alt="" src=images/Arch_SectionPlane_CutView.jpg  style="width:600px;">



## Właściwości

-    **Tylko bryły**: Jeśli ta opcja ma wartość {{True/pl}}, obiekty niebędące bryłami w zestawie nie będą brane pod uwagę.

-    **Długość wyświetlana**: Długość wskaźnika płaszczyzny przekroju w widoku 3D. Nie ma wpływu na widok wynikowy.

-    **Szerokość wyświetlana**: Wysokość wskaźnika płaszczyzny przekroju w widoku 3D. Nie ma wpływu na widok wynikowy.

-    **Rozmiar strzałki**: Rozmiar strzałek narzędzia płaszczyzny przekroju w widoku 3D. Nie ma wpływu na widok wynikowy

-    **Widok wcięcia**: Jeśli opcja ta ma wartość {{True/pl}}, cały widok 3D zostanie przycięty w miejscu tej płaszczyzny przekroju.

-    **Widok wycinka**: Jeśli opcja ma wartość {{True/pl}}, widok zostanie przycięty do wysokości wyświetlania i długości płaszczyzny przekroju. Skutecznie zmienia to płaszczyznę przekroju w kamerę prostopadłą, ograniczając pole widzenia.

<img alt="" src=images/Arch_SectionPlane_ClipView.png  style="width:600px;">



*Płaszczyzna przekroju architektury z opcją widoku wycinka będzie zachowywać się jak kamera, ograniczając pole widzenia.*



## Ulepszenia

-   Ręczne dodanie właściwości o nazwie **RotateSolidRender** typu **App::PropertyAngle** do właściwości **View** płaszczyzny → przekroju *(kliknij prawym przyciskiem myszy widok właściwości → pokaż wszystkie, kliknij ponownie prawym przyciskiem myszy → dodaj właściwość)* umożliwia obrócenie renderowania podczas korzystania z trybu bryłowego. Jest to przydatne, gdy renderowany widok zawiera na przykład elementy środowiska Architektura i Rysunek Roboczy, a renderowanie elementów Architektury jest obrócone w stosunku do elementów Rysunku Roboczego.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Wstaw widok przekroju może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
Section = makeSectionPlane(objectslist=None, name="Section")
```

-   Tworzy obiekt `Section` z `objectslist`, który jest listą obiektów.

Przykład:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
Structure = Arch.makeStructure(length=1000, width=1000, height=200)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor, Structure])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()

Section1 = Arch.makeSectionPlane([Wall1, Wall2])
Section2 = Arch.makeSectionPlane([Structure])
Section3 = Arch.makeSectionPlane([Site])
FreeCAD.ActiveDocument.recompute()
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch SectionPlane/pl
