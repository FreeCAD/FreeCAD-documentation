---
 GuiCommand:
   Name: Reinforcement BarShapeCutList
   Name/pl: Zbrojenie: Zestawienie kształtów i cięć prętów
   MenuLocation: Zbrojenie , Zestawienie kształtów i cięć prętów
   Workbenches: Arch_Workbench/pl, BIM_Workbench/pl
   Version: 0.19
   SeeAlso: 
---

# Reinforcement BarShapeCutList/pl



## Opis

Narzędzie **Zestawienie kształtów i cięć prętów zbrojeniowych** umożliwia użytkownikowi utworzenie listy elementów ciętych kształtów prętów zbrojeniowych.

To polecenie jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) [Zbrojenie](Reinforcement_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md).

<img alt="" src=images/Reinforcement_Bar_Shape_Cut_List_example.svg  style="width:800px;"> 
*Pręty zbrojeniowe. Wykaz kształtów i cięcia*



## Użycie

1\. Wybierz obiekty **<img src="images/Arch_Rebar.svg" width=16px> [Prętów](Arch_Rebar/pl.md)** i Prętów2, które chcesz uwzględnić w zestawieniu kształtów i cięcia. Lub wybierz obiekty **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)** do uwzględnienia obiektów **<img src="images/Arch_Rebar.svg" width=16px> [Pręta](Arch_Rebar/pl.md)** i Pręta2 w zestawieniu kształtów i cięcia. Jeśli nic nie zostanie zaznaczone, wygenerowany zostanie zestawieniu kształtów i cięcia dla wszystkich obiektów **<img src="images/Arch_Rebar.svg" width=16px> [Prętów](Arch_Rebar/pl.md)** i Prętów2 obecnych w modelu.

2\. Następnie wybierz **<img src="images/Reinforcement_BarShapeCutList.svg" width=16px>
'''Zestawienie kształtów i cięć prętów'''** z menu narzędzi prętów zbrojeniowych.

3\. Na ekranie pojawi się okno dialogowe, jak pokazano poniżej.

:   ![](images/Reinforcement_Bar_Shape_Cut_List_Dialog.png )

:   
    
*Okno dialogowe narzędzia Zestawienie kształtów i cięć prętów.*
    

4\. Zmodyfikuj dane, aby dostosować je do swoich wymagań.

5\. Kliknij **OK** lub **Zastosuj**, aby wygenerować Zestawienie kształtów i cięć prętów.

6\. Kliknij **Anuluj**, aby zamknąć okno dialogowe.



## Właściwości

**Ogólne:**

-    **Przesunięcie krawędzi strzemienia**: Przesunięcie przedłużonych krawędzi końcowych strzemienia, tak aby krawędzie końcowe strzemienia o kącie zagięcia 90 stopni nie pokrywały się z jego krawędziami.

-    **Szerokość skoku pręta zbrojeniowego**: Szerokość obrysu prętów zbrojeniowych na liście cięcia kształtu prętów zbrojeniowych.

-    **Styl kolorów prętów zbrojeniowych**: Styl koloru prętów zbrojeniowych.

-    **Wysokość rzędu**: Wysokość każdego rzędu prętów zbrojeniowych na liście prętów zbrojeniowych.

-    **Szerokość kolumny**: Szerokość każdej kolumny kształtu pręta zbrojeniowego na liście wyciętych kształtów prętów zbrojeniowych.

-    **Liczba kolumn**: Liczba kolumn na liście wyciętych kształtów prętów zbrojeniowych.

-    **Wyściółka boczna**: Wypełnienie z każdej strony kształtu pręta zbrojeniowego.

-    **Poziomy kształt pręta zbrojeniowego**: Jeśli wartość ta to {{True/pl}}, kształt pręta zbrojeniowego zostanie ustawiony poziomo poprzez obrócenie maksymalnej długości krawędzi kształtu pręta zbrojeniowego.

-    **Dołącz znak**: Jeśli wartość jest ustawiona na {{True/pl}}, wówczas rebar.Mark zostanie uwzględniony dla każdego kształtu pręta zbrojeniowego na liście cięcia kształtu pręta zbrojeniowego.

-    **Plik wyjściowy SVG**: Plik wyjściowy do zapisu wygenerowanej listy cięć kształtów prętów zbrojeniowych SVG.

**Dane wymiarowe:**

-    **Zawiera wymiary**: Jeśli wartość wynosi {{True/pl}}, wówczas każdy wymiar krawędzi pręta zbrojeniowego i wymiary kąta gięcia zostaną uwzględnione na liście cięć kształtu pręta zbrojeniowego.

-    **Uwzględnij jednostki w etykiecie wymiaru**: Jeśli ma wartość {{True/pl}}, jednostki długości krawędzi prętów zbrojeniowych będą wyświetlane w etykiecie wymiaru.

-    **Jednostki wymiaru krawędzi pręta zbrojeniowego**: Jednostki używane dla wymiarów długości krawędzi prętów zbrojeniowych.

-    **Precyzja wymiarów krawędzi prętów zbrojeniowych**: Liczba miejsc dziesiętnych, które powinny być wyświetlane dla długości krawędzi pręta zbrojeniowego jako etykieta wymiaru.

-    **Rodzina czcionek wymiaru**: Rodzina czcionki tekstu wymiaru.

-    **Rozmiar czcionki**: Rozmiar czcionki tekstu wymiaru.

-    **Wymiar kąta wygięcia Lista nie obejmuje**: Lista kątów giętych, których wymiary nie będą uwzględniane.

-    **Format etykiety wymiaru pręta zbrojeniowego spiralnego**: Format etykiety wymiaru spiralnego pręta zbrojeniowego. np. \"%L,r=%R,pitch=%P\", gdzie %L -\> Długość spiralnego pręta zbrojeniowego, %R -\> Promień spirali spiralnego pręta zbrojeniowego, %P -\> Skok spirali spiralnego pręta zbrojeniowego.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Zestawienie kształtów i cięć prętów** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:



### Utwórz kształt zbrojenia SVG 


```python
getRebarShapeSVG(
    rebar,
    view_direction: Union[FreeCAD.Vector, WorkingPlane.Plane] = FreeCAD.Vector(0, 0, 0),
    include_mark: bool = True,
    stirrup_extended_edge_offset: float = 2,
    rebar_stroke_width: float = 0.35,
    rebar_color_style: str = "shape color",
    include_dimensions: bool = True,
    rebar_dimension_units: str = "mm",
    rebar_length_dimension_precision: int = 0,
    include_units_in_dimension_label: bool = False,
    bent_angle_dimension_exclude_list: Tuple[float, ...] = (45, 90, 180),
    dimension_font_family: str = "DejaVu Sans",
    dimension_font_size: float = 2,
    helical_rebar_dimension_label_format: str = "%L,r=%R,pitch=%P",
    scale: float = 1,
    max_height: float = 0,
    max_width: float = 0,
    side_padding: float = 1,
    horizontal_shape: bool = False,
) -> ElementTree.Element
```

-   Generuje i zwraca element SVG w kształcie pręta zbrojeniowego dla danego obiektu `rebar`.

-   Obiekt `rebar` może być typu \<ArchRebar.\_Rebar\> lub \<rebar2.BaseRebar\>, aby wygenerować jego kształt svg.

-    `view_direction`określa kierunek punktu widzenia dla kształtu pręta zbrojeniowego. Może być typu `FreeCAD.Vector` lub `WorkingPlane.Plane`, choć preferowany jest `WorkingPlane.Plane`.

-    `include_mark`określa, czy rebar.Mark ma być zawarty w SVG kształtu pręta zbrojeniowego, czy nie.

-    `stirrup_extended_edge_offset`to przesunięcie przedłużonych krawędzi końcowych strzemienia, tak aby krawędzie końcowe strzemienia o kącie zagięcia 90 stopni nie pokrywały się z krawędziami strzemienia.

-    `rebar_stroke_width`określa szerokość obrysu prętów zbrojeniowych w svg.

-    `rebar_color_style`określa styl koloru prętów zbrojeniowych. Może to być \"shape color\" lub \"color_name lub hex_value_of_color\". \"shape color\" oznacza wybór koloru kształtu pręta zbrojeniowego.

-    `include_dimensions`określa, czy każdy wymiar krawędzi pręta zbrojeniowego i wymiary kąta gięcia mają być zawarte w SVG kształtu pręta zbrojeniowego.

-    `rebar_dimension_units`określa jednostki, które mają być używane dla wymiarów długości prętów zbrojeniowych.

-    `rebar_length_dimension_precision`określa liczbę miejsc dziesiętnych, które powinny być wyświetlane dla długości pręta zbrojeniowego jako etykieta wymiaru. Ustaw wartość None, aby użyć preferowanej przez użytkownika precyzji jednostki z preferencji jednostki FreeCAD.

-    `include_units_in_dimension_label`określa, czy jednostki długości prętów zbrojeniowych mają być wyświetlane w etykiecie wymiaru.

-    `bent_angle_dimension_exclude_list`określa listę kątów giętych, których wymiary mają nie być uwzględniane.

-    `dimension_font_family`określa rodzaj czcionki tekstu wymiaru.

-    `dimension_font_size`określa rozmiar czcionki tekstu wymiaru.

-    `helical_rebar_dimension_label_format`określa format etykiety wymiaru pręta zbrojeniowego. Np. \"%L,r=%R,pitch=%P\" gdzie:

   %L -> długość spiralnego pręta zbrojeniowego
   %R -> promień spirali spiralnego pręta zbrojeniowego
   %P -> Skok spirali spiralnego pręta zbrojeniowego

-    `scale`określa wartość skali do skalowania SVG prętów zbrojeniowych. Parametr scale pomaga skalować w dół rebar_stroke_width i dimension_font_size, aby uczynić je niezależnymi od rozdzielczości. Jeśli wartość max_height lub max_width jest niezerowa, parametr scale zostanie zignorowany.

-    `max_height`określa maksymalną wysokość kształtu pręta zbrojeniowego SVG. Ustaw wartość 0, aby wysokość SVG kształtu pręta zbrojeniowego była oparta na parametrze skali.

-    `max_width`określa maksymalną szerokość kształtu pręta zbrojeniowego SVG. Ustaw wartość 0, aby uzyskać szerokość SVG w kształcie pręta zbrojeniowego w oparciu o parametr skali.

-    `side_padding`określa wypełnienie po każdej stronie kształtu pręta zbrojeniowego.

-    `horizontal_shape`określa, czy kształt pręta zbrojeniowego ma być poziomy poprzez obrócenie maksymalnej długości krawędzi kształtu pręta zbrojeniowego.



#### Przykład


```python
from pathlib import Path
from xml.dom import minidom
from xml.etree import ElementTree

import Draft, Arch, Stirrup
from RebarShapeCutList import RebarShapeCutListfunc

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = Stirrup.makeStirrup(
    20, 20, 20, 20, 20, 90, 4, 8, 2, True, 10, Structure, "Face6"
)

rebar_shape_svg = RebarShapeCutListfunc.getRebarShapeSVG(
    Rebar,
    view_direction=FreeCAD.Vector(0, 0, 0),
    include_mark=True,
    stirrup_extended_edge_offset=2,
    rebar_stroke_width=0.35,
    rebar_color_style="shape color",
    include_dimensions=True,
    rebar_dimension_units="mm",
    rebar_length_dimension_precision=0,
    include_units_in_dimension_label=True,
    bent_angle_dimension_exclude_list=(45, 90, 180),
    dimension_font_family="DejaVu Sans",
    dimension_font_size=2,
    helical_rebar_dimension_label_format="%L,r=%R,pitch=%P",
    scale=1,
    max_height=100,
    max_width=100,
    side_padding=1,
    horizontal_shape=False,
)

output_file = str(Path.home() / "StirrupRebarShape.svg")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(
        minidom.parseString(
            ElementTree.tostring(rebar_shape_svg, encoding="unicode")
        ).toprettyxml(indent="  ")
    )

```



### Utwórz listę cięć kształtu pręta zbrojeniowego SVG 


```python
getRebarShapeCutList(
    base_rebars_list: Optional[List] = None,
    view_directions: Union[
        Union[FreeCAD.Vector, WorkingPlane.Plane],
        List[Union[FreeCAD.Vector, WorkingPlane.Plane]],
    ] = FreeCAD.Vector(0, 0, 0),
    include_mark: bool = True,
    stirrup_extended_edge_offset: float = 2,
    rebars_stroke_width: float = 0.35,
    rebars_color_style: str = "shape color",
    include_dimensions: bool = True,
    rebar_edge_dimension_units: str = "mm",
    rebar_edge_dimension_precision: int = 0,
    include_units_in_dimension_label: bool = False,
    bent_angle_dimension_exclude_list: Union[Tuple[float, ...], List[float]] = (
        45,
        90,
        180,
    ),
    dimension_font_family: str = "DejaVu Sans",
    dimension_font_size: float = 2,
    helical_rebar_dimension_label_format: str = "%L,r=%R,pitch=%P",
    row_height: float = 40,
    column_width: float = 60,
    column_count: Union[int, Literal["row_count"]] = "row_count",
    side_padding: float = 1,
    horizontal_rebar_shape: bool = True,
    output_file: Optional[str] = None,
) -> ElementTree.Element
```

-   Generuje i zwraca element SVG z listą wyciętych prętów zbrojeniowych dla danej listy `base_rebars_list`.

-    `base_rebars_list`jest listą obiektów \<ArchRebar.\_Rebar\> lub \<rebar2.BaseRebar\>, aby wygenerować ich listę cięć RebarShape. Jeśli nie zostanie podana, wybrane zostaną wszystkie obiekty ArchRebar i rebar2.BaseRebar z unikalnym znacznikiem z ActiveDocument, a pręty zbrojeniowe bez przypisanego znacznika zostaną zignorowane.

-    `view_directions`to lista kierunków punktu widzenia dla każdego kształtu pręta zbrojeniowego. Może być typu `FreeCAD.Vector` lub `WorkingPlane.Plane`. LUB ich lista. Zachowaj `FreeCAD.Vector(0, 0, 0)`, aby automatycznie wybrać view_directions.

-    `include_mark`określa, czy rebar.Mark ma być uwzględniony dla każdego kształtu pręta zbrojeniowego w SVG listy cięcia kształtu pręta zbrojeniowego, czy nie.

-    `stirrup_extended_edge_offset`określa przesunięcie przedłużonych krawędzi końcowych strzemion, tak aby krawędzie końcowe strzemion o kącie zagięcia 90 stopni nie pokrywały się z krawędziami strzemion.

-    `rebars_stroke_width`określa szerokość obrysu prętów zbrojeniowych w liście cięcia kształtu prętów zbrojeniowych SVG.

-    `rebars_color_style`określa styl koloru prętów zbrojeniowych. Może to być \"shape color\" lub \"color_name lub hex_value_of_color\". \"shape color\" oznacza wybór koloru kształtu pręta zbrojeniowego.

-    `include_dimensions`określa, czy każdy wymiar krawędzi pręta zbrojeniowego i wymiary kąta gięcia mają być uwzględnione na liście cięcia kształtu pręta zbrojeniowego.

-    `rebar_edge_dimension_units`określa jednostki używane dla wymiarów długości krawędzi prętów zbrojeniowych.

-    `rebar_edge_dimension_precision`określa liczbę miejsc dziesiętnych, które powinny być wyświetlane dla długości pręta zbrojeniowego jako etykieta wymiaru. Ustaw wartość None, aby użyć preferowanej przez użytkownika precyzji jednostki z preferencji jednostki FreeCAD.

-    `include_units_in_dimension_label`określa, czy jednostki długości krawędzi prętów zbrojeniowych mają być wyświetlane w etykiecie wymiaru.

-    `bent_angle_dimension_exclude_list`określa listę kątów giętych, których wymiary mają nie być uwzględniane.

-    `dimension_font_family`określa rodzaj czcionki tekstu wymiaru.

-    `dimension_font_size`określa rozmiar czcionki tekstu wymiaru.

-    `helical_rebar_dimension_label_format`określa format etykiety wymiaru pręta zbrojeniowego. Np. \"%L,r=%R,pitch=%P\" gdzie:

   %L -> Długość spiralnego pręta zbrojeniowego,
   %R -> Promień spirali spiralnego pręta zbrojeniowego,
   %P -> Skok spirali spiralnego pręta zbrojeniowego.

-    `row_height`określa wysokość każdego wiersza kształtu pręta zbrojeniowego na liście cięcia kształtu pręta zbrojeniowego.

-    `column_width`określa szerokość każdego wiersza pręta zbrojeniowego na liście prętów zbrojeniowych.

-    `column_count`określa liczbę kolumn na liście wyciętych prętów zbrojeniowych. Ustaw na \"row_count\", aby column_count \<= row_count

-    `side_padding`określa wypełnienie po każdej stronie kształtu pręta zbrojeniowego na liście cięcia kształtu pręta zbrojeniowego.

-    `horizontal_rebar_shape`określa, czy kształt pręta zbrojeniowego ma być poziomy poprzez obrócenie maksymalnej długości krawędzi kształtu pręta zbrojeniowego.

-    `output_file`określa plik wyjściowy do zapisu wygenerowanej listy wyciętych kształtów prętów zbrojeniowych SVG.



#### Przykład 


```python
from pathlib import Path

import FreeCAD, Draft, Arch
from ColumnReinforcement import SingleTie
from RebarShapeCutList import RebarShapeCutListfunc

Rect1 = Draft.makeRectangle(400, 400)
Structure1 = Arch.makeStructure(Rect1, height=1600)
Structure1.ViewObject.Transparency = 80
Rect2 = Draft.makeRectangle(500, 500)
Structure2 = Arch.makeStructure(Rect2, height=1600)
Structure2.ViewObject.Transparency = 80
Structure2.Placement = FreeCAD.Placement(FreeCAD.Vector(1000, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0, 0, 1), 0))
FreeCAD.ActiveDocument.recompute()

# Create Straight Rebars
rebar_group = SingleTie.makeSingleTieFourRebars(
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=8,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=40,
    b_offset_of_rebars=40,
    rebar_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    structure=Structure1,
    facename="Face6",
).rebar_group

# Assign Mark to straight rebars
for straight_rebar in rebar_group.RebarGroups[1].MainRebars:
    straight_rebar.Mark = "main_sb"

# Create LShaped Rebars with hook along x-axis
rebar_group = SingleTie.makeSingleTieFourRebars(
    l_cover_of_tie=40,
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=90,
    extension_factor=8,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    rebar_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=100,
    structure=Structure2,
    facename="Face6",
).rebar_group

# Assign Mark to lshape rebars
for lshape_rebar in rebar_group.RebarGroups[1].MainRebars:
    lshape_rebar.Mark = "main_lb"

output_file = str(Path.home() / "RebarShapeCutList.svg")

# Create Rebar Shape Cut List for all base rebars in model
RebarShapeCutListfunc.getRebarShapeCutList(
    base_rebars_list=None,
    view_directions=FreeCAD.Vector(0, 0, 0),
    include_mark=True,
    stirrup_extended_edge_offset=2,
    rebars_stroke_width=0.35,
    rebars_color_style="shape color",
    include_dimensions=True,
    rebar_edge_dimension_units="mm",
    rebar_edge_dimension_precision=0,
    include_units_in_dimension_label=False,
    bent_angle_dimension_exclude_list=(45, 90, 180),
    dimension_font_family="DejaVu Sans",
    dimension_font_size=2,
    helical_rebar_dimension_label_format="%L,r=%R,pitch=%P",
    row_height=40,
    column_width=60,
    column_count="row_count",
    side_padding=1,
    horizontal_rebar_shape=True,
    output_file=output_file,
)
```



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement BarShapeCutList/pl
