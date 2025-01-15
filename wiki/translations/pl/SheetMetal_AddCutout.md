---
 GuiCommand:
   Name: SheetMetal AddCutout
   Name/pl: Arkusz Blachy: Dodaj wycięcie
   MenuLocation: SheetMetal , Dodaj wycięcie
   Workbenches: SheetMetal_Workbench/pl
   Shortcut: **E** **C**
   Version: 0.5.04
---

# SheetMetal AddCutout/pl



## Opis

Polecenie <img alt="" src=images/SheetMetal_AddCutout.svg  style="width:16px;"> [Dodaj wycięcie](SheetMetal_AddCutout/pl.md) tworzy wyciągnięte wycięcie z wyciągnięcia szkicu.

Różnica między \'normalnym\' wycięciem i wyciągniętym wycięciem polega na tym, że w tym drugim przypadku krawędzie są prostopadłe do wskazanej ściany obiektu arkusza blachy. Efekt polecenia jest widoczny tylko gdy szkic nie jest prostopadły do ściany.

![](images/SheetMetal_AddCutout_Example.png )



*Wyciągnięte wycięcie oparte o szkic okręgu*



## Użycie

1.  Wybierz płaską ścianę i szkic z zamkniętym profilem (w dowolnej kolejności).
2.  To polecenie można wywołać na kilka sposobów:
    -   Wciśnij przycisk **<img src="images/SheetMetal_AddCutout.svg" width=16px> [Dodaj wycięcie](SheetMetal_AddCutout/pl.md)**.
    -   Wybierz opcję **SheetMetal → <img src="images/SheetMetal_AddCutout.svg" width=16px> Dodaj wycięcie** z menu.
    -   Kliknij prawym przyciskiem myszy w [widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md) i wybierz opcję **SheetMetal → <img src="images/SheetMetal_AddCutout.svg" width=16px> Dodaj wycięcie** z menu kontekstowego.
    -   Użyj skrótu klawiszowego: **E** a następnie **C**.
3.  Otwarty zostanie [panel zadań](Task_panel/pl.md) **Extruded Cutout Parameters**.
4.  Opcjonalnie wciśnij przycisk **Ściana** aby ponownie wybrać płaską ścianę.
5.  Opcjonalnie wciśnij przycisk **Szkic** aby ponownie wybrać szkic.
6.  Opcjonalnie dostosuj parametry w panelu zadań.
7.  Wciśnij przycisk **OK** aby zakończyć polecenie i zamknąć panel zadań.
8.  Utworzony zostanie obiekt **ExtrudedCutout** składający się z jednego lub większej liczby otworów w linii przez obiekt.
9.  Opcjonalnie dostosuj parametry w [Edytorze właściwości](Property_editor/pl.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt SheetMetal ExtrudedCutout wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) lub, jeśli jest w obrębie [Zawartości środowiska Projekt Części](PartDesign_Body/pl.md), z obiektu [Cechy tego środowiska](PartDesign_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Extruded Cutout}}

-    **Cut Side|Enumeration**: Domyślna wartość to {{value|Inside}}. Strona wycięcia.

-    **Cut Type|Enumeration**: Domyślna wartość to {{value|Through everything both sides}}. Typ wycięcia.

-    **Extrusion Length1|Length|hidden**: Domyślna wartość to {{value|500.0 mm}}. Długość kierunku wyciągnięcia 1.

-    **Extrusion Length2|Length|hidden**: Domyślna wartość to {{value|500.0 mm}}. Długość kierunku wyciągnięcia 2.

-    **Selected Face|LinkSub**: Wskazany obiekt i ściana.

-    **Sketch|Link**: Szkic do wycięcia.


{{Properties_Title|Extruded Cutout Improvements}}

-    **Improve Cut|Bool**: Domyślna wartość to {{value|False}}. Ulepsza geometrię wycięcia jeśli wchodzi ona w obszar cięcia. Wybierz {{value|True}} tylko jeśli cięcie wymaga poprawki, bo może to być wolne.

-    **Improve Level|IntegerConstraint|hidden**: Domyślna wartość to {{value|4}}. Poziom jakości ulepszenia wycięcia. Więcej niż 10 może skutkować bardzo długim czasem.

-    **Refine|Bool**: Domyślna wartość to {{value|False}}. Ulepsza geometrię.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal AddCutout/pl
