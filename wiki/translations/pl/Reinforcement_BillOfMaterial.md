---
 GuiCommand:
   Name: Reinforcement BillOfMaterial
   Name/pl: Zbrojenie: Zestawienie zbrojenia
   MenuLocation: 
   Workbenches: Reinforcement_Workbench/pl
   Version: 0.19
   SeeAlso: 
---

# Reinforcement BillOfMaterial/pl



## Opis

Narzędzie **Zestawienie zbrojenia** umożliwia użytkownikowi utworzenie zestawienia prętów zbrojeniowych.

To polecenie jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) [Zbrojenie](Reinforcement_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) poprzez menu **Przybory → Menadżera dodatków → Zbrojenie**.

<img alt="" src=images/Arch_Rebar_BOM_example.png  style="width:600px;"> 
*Zestawienie materiałowe prętów zbrojeniowych.*



## Użycie

1\. Wybierz obiekty **<img src="images/Arch_Rebar.svg" width=16px> [Prętów](Arch_Rebar/pl.md)** i Prętów2, które chcesz uwzględnić w zestawieniu zbrojenia. Lub wybierz obiekty **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)** do uwzględnienia obiektów **<img src="images/Arch_Rebar.svg" width=16px> [Prętów](Arch_Rebar/pl.md)** w zestawieniu zbrojenia. Jeśli nic nie zostanie zaznaczone, wygenerowane zostanie zestawienie zbrojenia dla wszystkich obiektów **<img src="images/Arch_Rebar.svg" width=16px> [Prętów](Arch_Rebar/pl.md)** i Prętów2 obecnych w modelu.

2\. Następnie wybierz **<img src="images/Reinforcement_BillOfMaterial.svg" width=16px>
'''Zestawienie zbrojenia'''** z menu narzędzi prętów zbrojeniowych.

3\. Na ekranie pojawi się okno dialogowe, jak pokazano poniżej.

:   <img alt="" src=images/BOMDialog_General.png  style="width:500px;">

:   
    
*Okienko dialogowe narzędzia Zestawienie zbrojenia.*
    

4\. Zmodyfikuj dane, aby dostosować je do swoich wymagań.

5\. Aby edytować konfiguracje SVG **<img src="images/Reinforcement_BillOfMaterial.svg" width=16px> '''Zestawienia zbrojenia'''**, kliknij przycisk **Edytuj konfiguracje SVG**. Pojawi się okno dialogowe, jak pokazano poniżej.

:   <img alt="" src=images/BOMDialog_SVG.png  style="width:500px;">

:   
    
*Okno dialogowe edycji konfiguracji SVG zestawienia zbrojenia.*
    

6\. Modyfikuj konfiguracje SVG **<img src="images/Reinforcement_BillOfMaterial.svg" width=16px> '''Zestawienia zbrojenia'''**, a następnie kliknij **OK**, aby zastosować zmiany.

5\. Kliknij **OK** lub **Zastosuj**, aby wygenerować Zestawienie zbrojenia.

8\. Kliknij **Anuluj**, aby zamknąć okno dialogowe.



## Właściwości

**Ogólne:**

-    **Nagłówki kolumn**: Słownik z column_data jako kluczem i krotką *(column_display_header, column_sequence)* jako wartością.

-    **Jednostki kolumn**: Słownik z kluczami: \"Diameter\", \"RebarsLength\", \"RebarsTotalLength\" i odpowiadającymi im jednostkami jako wartością.

-    **Mapa wagi średnicy**: Słownik ze średnicą jako kluczem i odpowiadającą jej wagą jako wartością.

-    **Typ długości pręta zbrojeniowego**: Typ długości pręta zbrojeniowego określa typ długości pręta zbrojeniowego używany do obliczeń BOM, tj. \"RealLength\" lub \"LengthWithSharpEdges\".

-    **Obiekty prętów zbrojeniowych**: Lista obiektów ArchRebar i / lub rebar2 i / lub struktur *(aby wybrać ArchRebar w tej konstrukcji)*.

**SVG:**

-    **Rodzina czcionki**: Rodzina czcionki tekstu w BOM SVG.

-    **Nazwa czcionki**: Nazwa pliku czcionki odpowiadająca rodzinie czcionki wymaganej w trybie konsoli.

-    **Rozmiar czcionki**: Rozmiar czcionki w mm.

-    **Szerokość kolumny**: Szerokość każdej kolumny w tabeli BOM SVG.

-    **Wysokość wiersza**: Wysokość każdego wiersza w tabeli BOM SVG.

-    **Lewy odsunięcie**: Lewe przesunięcie tabeli BOM SVG.

-    **Górne odsunięcie**: Górne przesunięcie tabeli BOM SVG.

-    **Minimalne przesunięcie w prawo**: Minimalne przesunięcie w prawo tabeli BOM SVG.

-    **minimalne odsunięcie dolne**: Minimalne dolne przesunięcie tabeli BOM SVG.

-    **Szerokość maksymalna**: Maksymalna szerokość tabeli BOM SVG.

-    **Wysokość maksymalna**: Maksymalna wysokość tabeli BOM SVG.

-    **Plik szablonu**: Plik szablonu SVG dla BOM SVG.

-    **Plik wyjściowy**: Plik wyjściowy BOM SVG.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Zestawienie zbrojenia** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:



### Tworzenie arkusza kalkulacyjnego zestawienia 


```python
bom_spreadsheet = makeBillOfMaterial(
    column_headers=None,
    column_units=None,
    dia_weight_map=None,
    rebar_length_type=None,
    rebar_objects=None,
    obj_name="RebarBillOfMaterial",
)
```

-   Tworzy obiekt arkusza kalkulacyjnego `RebarBillOfMaterial` dla danego obiektu `rebar_objects`.
    -   Jeśli lista `rebar_objects` jest pusta, arkusz `RebarBillOfMaterial` zostanie utworzony dla wszystkich prętów zbrojeniowych w modelu.

-    `column_headers`jest słownikiem z kluczami: \"Host\", \"Mark\", \"RebarsCount\", \"Diameter\", \"RebarsLength\", \"RebarsTotalLength\", a wartościami są krotki column_header i ich numery porządkowe.

   Przykład: {
                "Host": ("Member", 1),
                "Mark": ("Mark", 2),
                "RebarsCount": ("No. of Rebars", 3),
                "Diameter": ("Diameter in mm", 4),
                "RebarLength": ("Length in m/piece", 5),
                "RebarsTotalLength": ("Total Length in m", 6),
            }
            ustaw numer sekwencji kolumny na 0, aby ukryć kolumnę.

-    `column_units`jest słownikiem z kluczami: \"Diameter\", \"RebarsLength\", \"RebarsTotalLength\" i odpowiadającymi im jednostkami jako wartością.

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

-    `rebar_length_type`określa typ długości pręta zbrojeniowego używany do obliczeń BOM. Może przyjmować wartości \"RealLength\" lub \"LengthWithSharpEdges\".

-    `rebar_objects`jest listą obiektów ArchRebar i / lub rebar2 i / lub structures *(aby wybrać ArchRebar w tej strukturze)*.



#### Przykład


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from BillOfMaterial import BillOfMaterial_Spreadsheet

# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure1 = Arch.makeStructure(Rect, height=1600)
Structure1.ViewObject.Transparency = 80
Structure2 = Arch.makeStructure(Rect, height=1600)
Structure2.ViewObject.Transparency = 80
Structure2.Placement = FreeCAD.Placement(FreeCAD.Vector(1000, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0, 0, 1), 0))
FreeCAD.ActiveDocument.recompute()

# Create Straight Rebars
RebarGroup = TwoTiesSixRebars.makeTwoTiesSixRebars(
    l_cover_of_ties=40,        
    r_cover_of_ties=40,
    t_cover_of_ties=40,
    b_cover_of_ties=40,
    offset_of_ties=100,
    bent_angle_of_ties=135,
    extension_factor_of_ties=2,
    dia_of_ties=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    t_offset_of_rebars=40,
    b_offset_of_rebars=40,
    main_rebars_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    ties_sequence=("Tie1", "Tie2"),
    structure=Structure1,
    facename="Face6",
)

# Create LShaped Rebars with hook along x-axis
RebarGroup = TwoTiesSixRebars.makeTwoTiesSixRebars(
    l_cover_of_ties=40,
    r_cover_of_ties=40,
    t_cover_of_ties=40,
    b_cover_of_ties=40,
    offset_of_ties=100,
    bent_angle_of_ties=135,
    extension_factor_of_ties=2,
    dia_of_ties=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    main_rebars_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    ties_sequence=("Tie1", "Tie2"),
    structure=Structure2,
    facename="Face6",
)

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

# To create Bill Of Material Spreadsheet for all rebars in a model
BillOfMaterial_Spreadsheet.makeBillOfMaterial(
    column_headers=COLUMN_HEADERS,
    column_units=COLUMN_UNITS,
    dia_weight_map=DIA_WEIGHT_MAP,
    rebar_length_type="RealLength",
)

# To create Bill Of Material Spreadsheet for rebars in Structure1
BillOfMaterial_Spreadsheet.makeBillOfMaterial(
    column_headers=COLUMN_HEADERS,
    column_units=COLUMN_UNITS,
    dia_weight_map=DIA_WEIGHT_MAP,
    rebar_length_type="LengthWithSharpEdges",
    rebar_objects=[Structure1],
)
```



### Tworzenie listy materiałów SVG 


```python
makeBillOfMaterialSVG(
    column_headers: Optional[Dict[str, Tuple[str, int]]] = None,
    column_units: Optional[Dict[str, str]] = None,
    dia_weight_map: Optional[Dict[float, FreeCAD.Units.Quantity]] = None,
    rebar_length_type: Optional[
        Literal["RealLength", "LengthWithSharpEdges"]
    ] = None,
    font_family: Optional[str] = None,
    font_filename: Optional[str] = None,
    font_size: Optional[float] = None,
    column_width: Optional[float] = None,
    row_height: Optional[float] = None,
    bom_left_offset: Optional[float] = None,
    bom_top_offset: Optional[float] = None,
    bom_min_right_offset: Optional[float] = None,
    bom_min_bottom_offset: Optional[float] = None,
    bom_table_svg_max_width: Optional[float] = None,
    bom_table_svg_max_height: Optional[float] = None,
    template_file: Optional[str] = None,
    output_file: Optional[str] = None,
    rebar_objects: Optional[List] = None,
    reinforcement_group_by: Optional[Literal["Mark", "Host"]] = None,
    return_svg_only: bool = False,
) -> BOMContent
```

-   Tworzy i zwraca obiekt RebarBillOfMaterial_SVG `BOMContent` dla danego `rebar_objects`.
    -   Jeśli lista `rebar_objects` jest pusta, obiekt `BOMContent` zostanie utworzony dla wszystkich prętów zbrojeniowych w modelu.

-    `column_headers`jest słownikiem z kluczami: \"Host\", \"Mark\", \"RebarsCount\", \"Diameter\", \"RebarsLength\", \"RebarsTotalLength\", a wartościami są krotki nagłówków kolumn i ich numerów sekwencyjnych.

   Przykład: {
                "Host": ("Member", 1),
                "Mark": ("Mark", 2),
                "RebarsCount": ("No. of Rebars", 3),
                "Diameter": ("Diameter in mm", 4),
                "RebarLength": ("Length in m/piece", 5),
                "RebarsTotalLength": ("Total Length in m", 6),
            }
            ustaw numer sekwencji kolumny na 0, aby ukryć kolumnę.

-    `column_units`jest słownikiem z kluczami: \"Diameter\", \"RebarsLength\", \"RebarsTotalLength\" i odpowiadającymi im jednostkami jako wartością.

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

-    `rebar_length_type`określa typ długości prętów zbrojeniowych używany do obliczeń zestawienia materiałów. Może przyjmować wartości \"RealLength\" lub \"LengthWithSharpEdges\".

-    `font_family`określa rodzinę czcionki tekstu danych.

-    `font_filename`określa nazwę pliku czcionki lub pełną ścieżkę do pliku czcionki odpowiadającego font_family. Jest to wymagane, jeśli pracujesz w trybie konsoli, bez GUI.

-    `font_size`określa rozmiar czcionki tekstu danych.

-    `column_width`określa szerokość każdej kolumny w tabeli zestawienia materiałów SVG.

-    `row_height`określa wysokość każdego wiersza w tabeli zestawienia materiałów SVG.

-    `bom_left_offset`określa lewe przesunięcie tabeli materiałów SVG w `template_file`.

-    `bom_top_offset`określa górne przesunięcie tabeli materiałów SVG w `template_file`.

-    `bom_min_right_offset`określa minimalne przesunięcie w prawo pliku SVG listy materiałów w `template_file`.

-    `bom_min_bottom_offset`określa minimalne dolne przesunięcie pliku SVG listy materiałów w `template_file`.

-    `bom_table_svg_max_width`określa maksymalną szerokość tabeli zestawienia materiałów w SVG.

-    `bom_table_svg_max_height`określa maksymalną wysokość tabeli zestawienia materiałów w SVG.

-    `template_file`określa plik szablonu używany do umieszczenia na nim wygenerowanej tabeli zestawienia materiałów. Musi to być prawidłowy plik szablonu Rysunku Technicznego z polami przedstawionymi na stronie [Przestrzeń nazw SVG](Svg_Namespace/pl.md).

-    `output_file`określa plik wyjściowy do zapisu wygenerowanego zestawienia materiałów SVG.

-    `rebar_objects`jest listą obiektów ArchRebar i / lub rebar2 i / lub struktur *(aby wybrać ArchRebar w tej strukturze)*.

-    `reinforcement_group_by`określa sposób grupowania obiektów zbrojenia. Może to być \"Mark\" lub \"Host\".

-    `return_svg_only`określa, czy obiekt `BOMContent` ma zostać utworzony, czy nie. Jeśli `return_svg_only` ma wartość True, to ani obiekt `BOMContent` nie zostanie utworzony, ani plik SVG nie zostanie zapisany w pliku `output_file`. Zwracany jest natomiast element SVG.



#### Przykład 


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from BillOfMaterial import BillOfMaterial_SVG

# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure1 = Arch.makeStructure(Rect, height=1600)
Structure1.ViewObject.Transparency = 80
Structure2 = Arch.makeStructure(Rect, height=1600)
Structure2.ViewObject.Transparency = 80
Structure2.Placement = FreeCAD.Placement(FreeCAD.Vector(1000, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0, 0, 1), 0))
FreeCAD.ActiveDocument.recompute()

# Create Straight Rebars
RebarGroup = TwoTiesSixRebars.makeTwoTiesSixRebars(
    l_cover_of_ties=40,        
    r_cover_of_ties=40,
    t_cover_of_ties=40,
    b_cover_of_ties=40,
    offset_of_ties=100,
    bent_angle_of_ties=135,
    extension_factor_of_ties=2,
    dia_of_ties=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    t_offset_of_rebars=40,
    b_offset_of_rebars=40,
    main_rebars_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    ties_sequence=("Tie1", "Tie2"),
    structure=Structure1,
    facename="Face6",
)

# Create LShaped Rebars with hook along x-axis
RebarGroup = TwoTiesSixRebars.makeTwoTiesSixRebars(
    l_cover_of_ties=40,
    r_cover_of_ties=40,
    t_cover_of_ties=40,
    b_cover_of_ties=40,
    offset_of_ties=100,
    bent_angle_of_ties=135,
    extension_factor_of_ties=2,
    dia_of_ties=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    main_rebars_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    ties_sequence=("Tie1", "Tie2"),
    structure=Structure2,
    facename="Face6",
)

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

# To create Bill Of Material SVG for all rebars in a model
BillOfMaterial_SVG.makeBillOfMaterialSVG(
    column_headers=COLUMN_HEADERS,
    column_units=COLUMN_UNITS,
    dia_weight_map=DIA_WEIGHT_MAP,
    rebar_length_type="RealLength",
    font_family = "DejaVu Sans",
    font_filename = "DejaVuSans.ttf",
    font_size = 3,
    column_width = 30,
    row_height = 10,
    bom_left_offset = 6,
    bom_top_offset = 40,
    bom_min_right_offset = 6,
    bom_min_bottom_offset = 6,
    bom_table_svg_max_width = 0,
    bom_table_svg_max_height = 0,
    template_file = str(Path(BillOfMaterial_SVG.__file__).parent.absolute() / "BOMTemplate.svg"),
    output_file = None,
    reinforcement_group_by = "Host",
)

# To create Bill Of Material SVG for rebars in Structure1
BillOfMaterial_SVG.makeBillOfMaterialSVG(
    column_headers = COLUMN_HEADERS,
    column_units = COLUMN_UNITS,
    dia_weight_map = DIA_WEIGHT_MAP,
    rebar_length_type = "LengthWithSharpEdges",
    font_family = "DejaVu Sans",
    font_filename = "DejaVuSans.ttf",
    font_size = 3,
    column_width = 30,
    row_height = 10,
    bom_left_offset = 6,
    bom_top_offset = 40,
    bom_min_right_offset = 6,
    bom_min_bottom_offset = 6,
    bom_table_svg_max_width = 0,
    bom_table_svg_max_height = 0,
    template_file = str(Path(BillOfMaterial_SVG.__file__).parent.absolute() / "BOMTemplate.svg"),
    rebar_objects=[Structure1],
    reinforcement_group_by = "Host",
)
```



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement BillOfMaterial/pl
