---
 GuiCommand:
   Name: Reinforcement Bar Bending Schedule
   Name/pl: Zbrojenie: Schemat gięcia prętów
   MenuLocation: brak
   Workbenches: Arch_Workbench/pl, BIM_Workbench/pl
   Version: 0.19
   SeeAlso: Reinforcement_Workbench/pl, Arch_Rebar_BOM/pl, Arch_Rebar_Drawing_Dimensioning/pl
---

# Reinforcement Bar Bending Schedule/pl



## Opis

Narzędzie **Schemat gięcia prętów** umożliwia użytkownikowi utworzenie harmonogramu gięcia prętów zbrojeniowych.

To polecenie jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) [Zbrojenie](Reinforcement_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) poprzez menu **Przybory → Menadżera dodatków → Zbrojenie**.

<img alt="" src=images/Reinforcement_Bar_Bending_Schedule_example.svg  style="width:1300px;">



*Schemat gięcia prętów zbrojeniowych*



## Użycie

1\. Wybierz obiekty **<img src="images/Arch_Rebar.svg" width=16px> [Prętów](Arch_Rebar/pl.md)** i Prętów2, które chcesz uwzględnić w harmonogramie gięcia prętów. Lub wybierz obiekty **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)** do uwzględnienia obiektów **<img src="images/Arch_Rebar.svg" width=16px> [Pręta](Arch_Rebar/pl.md)** i Pręta2 w harmonogramie gięcia prętów. Jeśli nic nie zostanie zaznaczone, wygenerowany zostanie harmonogram gięcia prętów dla wszystkich **<img src="images/Arch_Rebar.svg" width=16px> obiektów [Prętów](Arch_Rebar/pl.md)** i Prętów2 obecnych w modelu.

2\. Następnie wybierz **<img src="images/Reinforcement_Bar_Bending_Schedule.svg" width=16px> '''Schemat gięcia prętów'''** z narzędzi prętów zbrojeniowych.

3\. Na ekranie pojawi się okno dialogowe, jak pokazano poniżej.

![](images/Reinforcement_Bar_Bending_Schedule_Dialog.png )



*Okno dialogowe narzędzia Schemat gięcia prętów zbrojeniowych*

4\. Zmodyfikuj dane, aby dostosować je do swoich wymagań.

5\. Kliknij **OK** lub **Zastosuj**, aby wygenerować zestawienie gięcia prętów zbrojeniowych.

6\. Kliknij **Anuluj**, aby zamknąć okno dialogowe.



## Właściwości

**Ogólne:**

-    **Grupowanie zbrojenia według**: określa sposób grupowania obiektów zbrojenia w zestawieniu gięcia prętów, tj. \"Obiekt\" lub \"Oznaczenie\".

-    **Typ długości pręta**: określa typ długości pręta zbrojeniowego używany do obliczeń BOM, tj. \"Długość rzeczywista\" lub \"Długość z ostrymi krawędziami\".

-    **Nagłówki kolumn**: Słownik z column_data jako kluczem i krotką *(column_display_header, column_sequence)* jako wartością.

-    **Jednostki kolumn**: Słownik z kluczami: \"Średnica\", \"Długość pręta zbrojeniowego\", \"Długość całkowita pręta zbrojeniowego\" i odpowiadającymi im jednostkami jako wartością.

-    **Rodzaj czcionki**: Rodzina czcionki tekstu w zestawieniu gięcia prętów SVG.

-    **Rozmiar czcionki**: Rozmiar czcionki w mm.

-    **Szerokość kolumny**: Szerokość każdej kolumny w harmonogramie gięcia prętów SVG.

-    **Wysokość wiersza**: Wysokość każdego wiersza w harmonogramie gięcia prętów SVG.

-    **Plik wyjściowy SVG**: Plik wyjściowy SVG, do zapisu wygenerowanej listy cięć kształtów prętów zbrojeniowych.

**Dane kolumny Kształt pręta zbrojeniowego:** Dane związane z kolumną Kształt pręta zbrojeniowego w Zestawieniu gięcia prętów.

-    **Nagłówek kolumny**: definiuje nagłówek kolumny dla kolumny kształtu pręta zbrojeniowego.

-    **Przesunięcie przedłużonej krawędzi strzemienia**: określa przesunięcie przedłużonych krawędzi końcowych strzemion, tak aby krawędzie końcowe strzemion o kącie zagięcia 90 stopni nie pokrywały się z krawędziami strzemion.

-    **Szerokość skoku prętów zbrojeniowych**: definiuje szerokość obrysu prętów zbrojeniowych w kolumnie kształtu prętów zbrojeniowych..

-    **Styl koloru prętów zbrojeniowych**: definiuje styl koloru prętów zbrojeniowych.

**Dane wymiarowe kolumny Kształt pręta zbrojeniowego:** Dane związane z wymiarami kształtu pręta zbrojeniowego w kolumnie Kształt pręta zbrojeniowego.

-    **Uwzględnij wymiary**: Jeśli opcja ta ma wartość {{True/pl}}, wówczas każdy wymiar krawędzi pręta zbrojeniowego i wymiary kąta gięcia zostaną uwzględnione na liście cięć kształtu pręta zbrojeniowego.

-    **Uwzględnij jednostki w etykiecie wymiaru**: Jeśli ma wartość {{True/pl}}, jednostki długości krawędzi prętów zbrojeniowych będą wyświetlane w etykiecie wymiaru.

-    **Jednostki wymiaru krawędzi prętów zbrojeniowych**: Jednostki używane dla wymiarów długości krawędzi prętów zbrojeniowych.

-    **Dokładność wymiarowania krawędzi prętów zbrojeniowych**: Liczba miejsc dziesiętnych, które powinny być wyświetlane dla długości krawędzi pręta zbrojeniowego jako etykieta wymiaru.

-    **Rodzina czcionki wymiaru**: Rodzina czcionki tekstu wymiaru.

-    **Rozmiar czcionki wymiaru**: Rozmiar czcionki tekstu wymiaru.

-    **Lista wykluczeń wymiaru kąta zagięcia**: Lista kątów giętych, których wymiary nie będą uwzględniane.

-    **Format etykiety wymiaru spiralnego pręta zbrojeniowego**: Format etykiety wymiaru spiralnego pręta zbrojeniowego. np. \"%L,r=%R,pitch=%P\", gdzie %L → Długość spiralnego pręta zbrojeniowego, %R → Promień spirali spiralnego pręta zbrojeniowego, %P → Skok spirali spiralnego pręta zbrojeniowego.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Schemat gięcia prętów** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:



### Tworzenie zestawienia gięcia prętów 


```python
getBarBendingSchedule(
    rebar_objects: Optional[List] = None,
    column_headers: Optional[Dict[str, Tuple[str, int]]] = None,
    column_units: Optional[Dict[str, str]] = None,
    dia_weight_map: Optional[Dict[float, FreeCAD.Units.Quantity]] = None,
    rebar_length_type: Optional[
        Literal["RealLength", "LengthWithSharpEdges"]
    ] = None,
    reinforcement_group_by: Optional[Literal["Mark", "Host"]] = None,
    font_family: Optional[str] = None,
    font_size: float = 5,
    column_width: float = 60,
    row_height: float = 30,
    rebar_shape_column_header: str = "Rebar Shape (mm)",
    rebar_shape_view_directions: Union[
        Union[FreeCAD.Vector, WorkingPlane.Plane],
        List[Union[FreeCAD.Vector, WorkingPlane.Plane]],
    ] = FreeCAD.Vector(0, 0, 0),
    rebar_shape_stirrup_extended_edge_offset: float = 2,
    rebar_shape_color_style: str = "shape color",
    rebar_shape_stroke_width: float = 0.35,
    rebar_shape_include_dimensions: bool = True,
    rebar_shape_dimension_font_size: float = 3,
    rebar_shape_edge_dimension_units: str = "mm",
    rebar_shape_edge_dimension_precision: int = 0,
    include_edge_dimension_units_in_dimension_label: bool = False,
    rebar_shape_bent_angle_dimension_exclude_list: Union[
        List[float], Tuple[float, ...]
    ] = (45, 90, 180),
    helical_rebar_dimension_label_format: str = "%L,r=%R,pitch=%P",
    output_file: Optional[str] = None,
) -> xml.ElementTree.Element
```

-   Generuje i zwraca element zestawienia SVG gięcia prętów dla danego `rebar_objects`.

-    `rebar_objects`jest listą obiektów \<ArchRebar.\_Rebar\> lub \<rebar2.BaseRebar\>, aby wygenerować ich zestawienie gięcia prętów. Jeśli nie zostanie podana, wybrane zostaną wszystkie obiekty ArchRebar i rebar2.BaseRebar z unikalnym znakiem z ActiveDocument.

-    `column_headers`jest słownikiem z kluczami: \"Obiekt\", \"Oznaczenie\", \"Liczba prętów zbrojeniowych\", \"Średnica\", \"Długość pręta zbrojeniowego\", \"Całkowita długość pręta zbrojeniowego\", a wartości są krotkami nagłówków kolumn i ich numerów sekwencji.

  Przykład: {
                "Host": ("Member", 1),
                "Mark": ("Mark", 2),
                "RebarsCount": ("No. of Rebars", 3),
                "Diameter": ("Diameter in mm", 4),
                "RebarLength": ("Length in m/piece", 5),
                "RebarsTotalLength": ("Total Length in m", 6),
            }
            ustaw numer sekwencji kolumny na 0, aby ukryć kolumnę.

-    `column_units`jest słownikiem z kluczami: \"Średnica\", \"Długość pręta zbrojeniowego\", \"Całkowita długość pręta zbrojeniowego\" i odpowiadającymi im jednostkami jako wartością.

  Przykład: {
                "Diameter": "mm",
                "RebarLength": "m",
                "RebarsTotalLength": "m",
            }

-    `dia_weight_map`jest słownikiem ze średnicą jako kluczem i odpowiadającą jej wagą jako wartością.

  Składnia: {
                6: FreeCAD.Units.Quantity("0.222 kg/m"),
                8: FreeCAD.Units.Quantity("0.395 kg/m"),
                10: FreeCAD.Units.Quantity("0.617 kg/m"),
                12: FreeCAD.Units.Quantity("0.888 kg/m"),
                ...,
            }

-    `rebar_length_type`określa typ długości pręta zbrojeniowego używany do obliczeń rozkładu zginania prętów. Może to być \"Długość rzeczywista\" lub \"Długość z ostrymi krawędziami\".

-    `reinforcement_group_by`określa sposób grupowania obiektów zbrojenia. Może to być \"Oznaczenie\" lub \"Obiekt\".

-    `font_family`określa krój czcionek tekstu danych.

-    `font_size`określa rozmiar czcionki tekstu danych.

-    `column_width`określa szerokość każdej kolumny w zestawieniu SVG zginania prętów.

-    `row_height`określa wysokość każdego wiersza w zestawieniu SVG gięcia prętów.

-    `rebar_shape_column_header`określa nagłówek kolumny dla kolumny kształtu pręta zbrojeniowego.

-    `rebar_shape_view_directions`to lista kierunków widoku dla każdego kształtu pręta zbrojeniowego. Może być typu `FreeCAD.Vector` lub `WorkingPlane.Plane`. LUB ich lista. Zachowaj `FreeCAD.Vector(0, 0, 0)`, aby automatycznie wybrać view_directions.

-    `rebar_shape_stirrup_extended_edge_offset`określa przesunięcie przedłużonych krawędzi końcowych strzemienia, tak aby krawędzie końcowe strzemienia o kącie zagięcia 90 stopni nie pokrywały się z krawędziami strzemienia.

-    `rebar_shape_color_style`określa styl koloru prętów zbrojeniowych. Może to być \"kolor kształtu\" lub \"color_name lub hex_value_of_color\". \"kolor kształtu\" oznacza wybór koloru kształtu pręta zbrojeniowego.

-    `rebar_shape_stroke_width`określa szerokość obrysu prętów zbrojeniowych w zestawieniu SVG kształtu pręta zbrojeniowego.

-    `rebar_shape_include_dimensions`określa, czy każdy wymiar krawędzi pręta zbrojeniowego i wymiary kąta gięcia mają być zawarte w SVG kształtu pręta zbrojeniowego.

-    `rebar_shape_dimension_font_size`określa rozmiar czcionki tekstu wymiaru w SVG kształtu pręta zbrojeniowego.

-    `rebar_shape_edge_dimension_units`określa jednostki używane dla wymiarów długości krawędzi pręta zbrojeniowego w SVG kształtu pręta zbrojeniowego.

-    `rebar_shape_edge_dimension_precision`określa liczbę miejsc dziesiętnych, które powinny być wyświetlane dla długości pręta zbrojeniowego jako etykieta wymiaru w zestawieniu SVG kształtu pręta zbrojeniowego. Ustaw wartość \"Brak\", aby użyć preferowanej przez użytkownika precyzji jednostki z preferencji FreeCAD.

-    `include_edge_dimension_units_in_dimension_label`określa, czy jednostki długości krawędzi prętów zbrojeniowych mają być wyświetlane w etykiecie wymiaru w zestawieniu SVG kształtu pręta zbrojeniowego.

-    `rebar_shape_bent_angle_dimension_exclude_list`określa listę kątów gięcia, których wymiary nie mają być uwzględniane w zestawieniu SVG kształtu pręta zbrojeniowego.

-    `helical_rebar_dimension_label_format`określa format etykiety wymiaru spiralnego pręta zbrojeniowego w zestawieniu SVG kształtu pręta zbrojeniowego. Np. \"%L,r=%R,pitch=%P\" gdzie:

   %L → długość spiralnego pręta zbrojeniowego
   %R → promień spirali spiralnego pręta zbrojeniowego
   %P → skok spirali spiralnego pręta zbrojeniowego

-    `output_file`określa plik wyjściowy do zapisu wygenerowanego zestawienia SVG gięcia prętów.



#### Przykład


```python
from pathlib import Path

import FreeCAD, Draft, Arch
from ColumnReinforcement import SingleTie
from BarBendingSchedule import BBSfunc

Rect1 = Draft.makeRectangle(400, 400)
Structure1 = Arch.makeStructure(Rect1, height=1600)
Structure1.ViewObject.Transparency = 80
Rect2 = Draft.makeRectangle(500, 500)
Structure2 = Arch.makeStructure(Rect2, height=1600)
Structure2.ViewObject.Transparency = 80
Structure2.Placement = FreeCAD.Placement(FreeCAD.Vector(1000, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0, 0, 1), 0))
FreeCAD.ActiveDocument.recompute()

# Tworzenie prostych prętów zbrojeniowych.
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

# Przypisz znak do prostych prętów zbrojeniowych.
for straight_rebar in rebar_group.RebarGroups[1].MainRebars:
    straight_rebar.Mark = "main_sb"


# Utwórz pręty zbrojeniowe w kształcie litery L z hakiem wzdłuż osi x.
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

# Przypisz znak do prętów zbrojeniowych w kształcie litery L.
for lshape_rebar in rebar_group.RebarGroups[1].MainRebars:
    lshape_rebar.Mark = "main_lb"

FreeCAD.ActiveDocument.recompute()

COLUMN_UNITS = {
    "Diameter": "mm",
    "RebarLength": "m",
    "RebarsTotalLength": "m",
}

COLUMN_HEADERS = {
    "Host": ("Member", 1),
    "Mark": ("Mark", 2),
    "RebarsCount": ("No. of Rebars", 3),
    "Diameter": ("Diameter in " + COLUMN_UNITS["Diameter"], 4),
    "RebarLength": ("Length in " + COLUMN_UNITS["RebarLength"] + "/piece", 5),
    "RebarsTotalLength": ("Total Length in " + COLUMN_UNITS["RebarsTotalLength"], 6),
}

DIA_WEIGHT_MAP = {
    6: FreeCAD.Units.Quantity("0.222 kg/m"),
    8: FreeCAD.Units.Quantity("0.395 kg/m"),
    10: FreeCAD.Units.Quantity("0.617 kg/m"),
    12: FreeCAD.Units.Quantity("0.888 kg/m"),
    14: FreeCAD.Units.Quantity("1.206 kg/m"),
    16: FreeCAD.Units.Quantity("1.578 kg/m"),
    18: FreeCAD.Units.Quantity("2.000 kg/m"),
    20: FreeCAD.Units.Quantity("2.466 kg/m"),
    22: FreeCAD.Units.Quantity("2.980 kg/m"),
    25: FreeCAD.Units.Quantity("3.854 kg/m"),
    28: FreeCAD.Units.Quantity("4.830 kg/m"),
    32: FreeCAD.Units.Quantity("6.313 kg/m"),
    36: FreeCAD.Units.Quantity("7.990 kg/m"),
    40: FreeCAD.Units.Quantity("9.864 kg/m"),
    45: FreeCAD.Units.Quantity("12.490 kg/m"),
    50: FreeCAD.Units.Quantity("15.410 kg/m"),
}

output_file = str(Path.home() / "BarBendingSchedule.svg")

# Utwórz harmonogram gięcia prętów dla wszystkich prętów zbrojeniowych w modelu.
BBSfunc.getBarBendingSchedule(
    rebar_objects=None,
    column_headers=COLUMN_HEADERS,
    column_units=COLUMN_UNITS,
    dia_weight_map=DIA_WEIGHT_MAP,
    rebar_length_type="LengthWithSharpEdges",
    reinforcement_group_by="Host",
    font_family="DejaVu Sans",
    font_size=5,
    column_width=60,
    row_height=30,
    rebar_shape_column_header="Rebar Shape (" "mm)",
    rebar_shape_view_directions=FreeCAD.Vector(0, 0, 0),
    rebar_shape_stirrup_extended_edge_offset=2,
    rebar_shape_color_style="shape color",
    rebar_shape_stroke_width=0.35,
    rebar_shape_include_dimensions=True,
    rebar_shape_dimension_font_size=3,
    rebar_shape_edge_dimension_units="mm",
    rebar_shape_edge_dimension_precision=0,
    include_edge_dimension_units_in_dimension_label=False,
    rebar_shape_bent_angle_dimension_exclude_list=(45, 90, 180),
    helical_rebar_dimension_label_format="%L,r=%R,pitch=%P",
    output_file=output_file,
)
```



---
⏵ [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement Bar Bending Schedule/pl
