---
 GuiCommand:
   Name: Reinforcement DrawingDimensioning
   Name/pl: Zbrojenie: Wymiarowanie rysunku zbrojenia
   MenuLocation: 
   Workbenches: Reinforcement_Workbench/pl
   Version: 0.19
   SeeAlso: 
---

# Reinforcement DrawingDimensioning/pl



## Opis

Narzędzie **Wymiarowanie rysunku zbrojenia** umożliwia użytkownikowi tworzenie rysunków i wymiarowanie prętów zbrojeniowych.

To polecenie jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) [Zbrojenie](Reinforcement_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) poprzez menu **Przybory → Menadżera dodatków → Zbrojenie**.

<img alt="" src=images/Arch_Rebar_Drawing_Dimensioning_example.svg  style="width:800px;"> 
*Rysunek i wymiarowanie prętów zbrojeniowych.*



## Użycie

1\. Otwórz model FreeCAD zawierający pręty zbrojeniowe utworzone za pomocą środowiska pracy [Zbrojenie](Reinforcement_Workbench/pl.md).

2\. Wybierz obiekt **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)**, a następnie wybierz **<img src="images/Reinforcement_DrawingDimensioning.svg" width=16px> '''Wymiarowanie rysunku zbrojenia'''** z narzędzi prętów zbrojeniowych.

3\. Na ekranie pojawi się okno dialogowe, jak pokazano poniżej.

:   <img alt="" src=images/ArchRebarDrawingDimensioning_dialog1.png  style="width:800px;">

4\. Wprowadź wszystkie szczegóły związane z szerokością obrysu i kolorem prętów zbrojeniowych i konstrukcji.

5\. Kliknij przycisk **Dalej**, a okno dialogowe zostanie zaktualizowane w sposób pokazany poniżej.

:   <img alt="" src=images/ArchRebarDrawingDimensioning_dialog2.png  style="width:800px;">

6\. Wprowadzanie opcji widoków rysunku, wymiarowania i szczegółów odsunięcia.

7\. Kliknij **Dalej**, a okno dialogowe zostanie zaktualizowane w sposób pokazany poniżej.

:   <img alt="" src=images/ArchRebarDrawingDimensioning_dialog3.png  style="width:800px;">

8\. Wprowadź etykietę wymiaru i szczegóły dotyczące linii.

9\. Kliknij przycisk **Dalej**, a okno dialogowe zostanie zaktualizowane w sposób pokazany poniżej.

:   <img alt="" src=images/ArchRebarDrawingDimensioning_dialog4.png  style="width:800px;">

10\. Wprowadź szczegóły wymiarów pojedynczego pręta zbrojeniowego i wielu prętów zbrojeniowych.

11\. Kliknij **Dalej**, a okno dialogowe zostanie zaktualizowane w sposób pokazany poniżej.

:   <img alt="" src=images/ArchRebarDrawingDimensioning_dialog5.png  style="width:800px;">

12\. Wprowadź szczegóły wymiarów i odsunięć linii wymiarowych.

13\. Kliknij przycisk **Zakończ**, aby wygenerować rysunki.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wymiarowanie rysunku zbrojenia** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:



### Tworzenie rysunków i wymiarowanie zbrojenia 


```python
from ReinforcementDrawing import make_reinforcement_drawing

structure_drawing_page_dict = make_reinforcement_drawing.makeStructuresReinforcementDrawing(
    structure_list=None,
    rebars_list=None,
    view="Front",
    rebars_stroke_width=0.35,
    rebars_color_style="Automatic",
    rebars_color=(0.67, 0.0, 0.0),
    structure_stroke_width=0.5,
    structure_color_style="Automatic",
    structure_color=(0.3, 0.9, 0.91),
    drawing_left_offset=20,
    drawing_top_offset=20,
    drawing_min_right_offset=20,
    drawing_min_bottom_offset=20,
    drawing_max_width=0,   # It is set to 0 to automatically set the default width based on other parameters
    drawing_max_height=0,  # It is set to 0 to automatically set the default height based on other parameters
    template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
    perform_dimensioning=True,
    dimension_rebars_filter_list=None,
    dimension_label_format="%M %C⌀%D,span=%S",
    dimension_font_family="DejaVu Sans",
    dimension_font_size=3,
    dimension_stroke_width=0.25,
    dimension_line_style="Continuous",
    dimension_line_color=(0.0, 0.0, 0.50),
    dimension_text_color=(0.0, 0.33, 0.0),
    dimension_single_rebar_line_start_symbol="None",
    dimension_single_rebar_line_end_symbol="FilledArrow",
    dimension_multi_rebar_line_start_symbol="FilledArrow",
    dimension_multi_rebar_line_end_symbol="FilledArrow",
    dimension_line_mid_point_symbol="Dot",
    dimension_left_offset=10,
    dimension_right_offset=10,
    dimension_top_offset=10,
    dimension_bottom_offset=10,
    dimension_left_offset_increment=6,
    dimension_right_offset_increment=6,
    dimension_top_offset_increment=6,
    dimension_bottom_offset_increment=6,
    dimension_single_rebar_outer_dim=False,
    dimension_multi_rebar_outer_dim=True,
    dimension_single_rebar_text_position_type="StartOfLine",
    dimension_multi_rebar_text_position_type="MidOfLine",
)
```

-   Zwraca `structure_drawing_page_dict`, słownik ze strukturą jako kluczem i odpowiednią stroną rysunku zbrojenia jako wartością.

-    `structure_list`jest listą obiektów konstrukcyjnych do wygenerowania ich rysunku zbrojenia. Jeśli nie zostanie podana, konstrukcje zostaną wybrane z aktywnego dokumentu działającego jako obiekt główny dla prętów zbrojeniowych.

-    `rebars_list`jest listą obiektów prętów zbrojeniowych, które mają zostać uwzględnione na rysunku. Jeśli nie zostanie podana, obiekty prętów zbrojeniowych posiadające obiekt główny na liście structure_list zostaną wybrane z aktywnego dokumentu.

-    `view`określa widok rysunku, który ma zostać wygenerowany. Może to być \"Front\", \"Rear\", \"Left\", \"Right\", \"Top\" lub \"Bottom\".

-    `rebars_stroke_width`określa szerokość obrysu prętów zbrojeniowych w rysunku SVG.

-    `rebars_color_style`określa styl kolorów prętów zbrojeniowych. Ustaw na \"Automatic\", aby automatycznie wybrać kolor prętów zbrojeniowych lub \"Custom\", aby wybrać wartość koloru kształtu ze zmiennej `rebars_color`.

-    `rebars_color`określa kolor wypełnienia prętów zbrojeniowych w rysunku SVG.

   Format: (r, g, b)
   Wartość r, g, b powinna wynosić od 0 do 1, więc może być konieczne podzielenie wartości r, g, b przez 255, aby uzyskać wartość od 0 do 1.
   Upewnij się, że wartości r, g, b muszą być zmiennoprzecinkowe.
   Przykład: (0.67, 0.0, 0.0)

-    `structure_stroke_width`określa szerokość obrysu struktury w rysowaniu SVG.

-    `structure_color_style`określa styl wypełnienia konstrukcji. Ustaw na \"Automatyczny\", aby automatycznie wybrać kolor konstrukcji lub \"Niestandardowy\", aby wybrać wartość koloru konstrukcji ze zmiennej `structure_color`.

-    `structure_color`określa kolor wypełnienia konstrukcji podczas rysowania SVG. Format: (r, g, b)

-    `drawing_left_offset`określa lewe odsunięcie widoku rysunku na `template_file`.

-    `drawing_top_offset`określa górne odsunięcie widoku rysunku na `template_file`.

-    `drawing_min_right_offset`określa minimalne odsunięcie widoku rysunku w prawo na `template_file`.

-    `drawing_min_bottom_offset`określa minimalne dolne odsunięcie widoku rysunku na `template_file`.

-    `drawing_max_width`określa maksymalną szerokość rysunku na `template_file`.

-    `drawing_max_height`określa maksymalną wysokość rysunku na `template_file`.

-    `template_file`to plik szablonu, który ma być używany dla strony rysunku zbrojenia.

-    `perform_dimensioning`określa, czy należy utworzyć wymiarowanie dla prętów zbrojeniowych na rysunku.

-    `dimension_rebars_filter_list`to lista prętów zbrojeniowych do wymiarowania. Ustaw na Brak, aby zwymiarować wszystkie widoczne pręty zbrojeniowe na rysunku.

-    `dimension_label_format`to format używany dla etykiety wymiaru.

   Przykład: "%M %C⌀%D,span=%S"
   Gdzie: %M -> Rebar.Mark
          %C -> Rebar.Amount
          %D -> Rebar.Diameter
          %S -> Rebar span length

-    `dimension_font_family`to rodzina czcionki etykiety wymiaru.

-    `dimension_font_size`to rozmiar czcionki etykiety wymiaru.

-    `dimension_stroke_width`to szerokość obrysu linii wymiaru.

-    `dimension_line_style`to styl obrysu linii wymiarowej. Może to być \"Continuous\", \"Dash\", \"Dot\", \"DashDot\" lub \"DashDotDot\".

-    `dimension_line_color`to kolor linii wymiarowej.

   Format: (r, g, b)
   Wartość r, g, b powinna zawierać się w przedziale od 0 do 1, więc może być konieczne podzielenie wartości r, g, b przez 255, aby uzyskać wartość od 0 do 1.
   Upewnij się, że r, g, b muszą być zmiennoprzecinkowe

-    `dimension_text_color`to kolor etykiety wymiaru.

-    `dimension_single_rebar_line_start_symbol`to symbol początku linii wymiarowej, w przypadku gdy widoczny jest pojedynczy pręt zbrojeniowy. Może to być \"FilledArrow\", \"Tick\", \"Dot\" lub \"None\".

-    `dimension_single_rebar_line_end_symbol`to symbol końca linii wymiarowej, w przypadku gdy widoczny jest pojedynczy pręt zbrojeniowy. Może to być \"FilledArrow\", \"Tick\", \"Dot\" lub \"None\".

-    `dimension_multi_rebar_line_start_symbol`to symbol początku linii wymiarowej, w przypadku gdy widocznych jest wiele prętów zbrojeniowych. Może to być \"FilledArrow\", \"Tick\", \"Dot\" lub \"None\".

-    `dimension_multi_rebar_line_end_symbol`to symbol końca linii wymiarowej, w przypadku gdy widocznych jest wiele prętów zbrojeniowych. Może to być \"FilledArrow\", \"Tick\", \"Dot\" lub \"None\".

-    `dimension_line_mid_point_symbol`to symbol punktu środkowego linii wymiarowej. Może to być \"Tick\", \"Dot\" lub \"None\".

-    `dimension_left_offset`określa lewe odsunięcie wymiaru od rysunku.

-    `dimension_right_offset`określa prawe odsunięcie wymiaru od rysunku.

-    `dimension_top_offset`określa górne odsunięcie wymiaru od rysunku.

-    `dimension_bottom_offset`określa dolne odsunięcie wymiaru od rysunku.

-    `dimension_left_offset_increment`to przyrost lewego odsunięcia w celu odsunięcia każdej nowej etykiety wymiaru od rysunku.

-    `dimension_right_offset_increment`to przyrost prawego odsunięcia w celu odsunięcia każdej nowej etykiety wymiaru od rysunku.

-    `dimension_top_offset_increment`to przyrost górnego odsunięcia w celu odsunięcia każdej nowej etykiety wymiaru od rysunku.

-    `dimension_bottom_offset_increment`to przyrost dolnego odsunięcia w celu odsunięcia każdej nowej etykiety wymiaru od rysunku.

-    `dimension_single_rebar_outer_dim`określa, czy linie wymiarowe mają znajdować się poza rysunkiem zbrojenia, w przypadku gdy widoczny jest pojedynczy pręt zbrojeniowy.

-    `dimension_multi_rebar_outer_dim`określa, czy linie wymiarowe mają znajdować się poza rysunkiem zbrojenia, w przypadku gdy widocznych jest wiele prętów zbrojeniowych.

-    `dimension_single_rebar_text_position_type`określa typ pozycji etykiety wymiaru, w przypadku gdy widoczny jest pojedynczy pręt zbrojeniowy. Może to być \"StartOfLine\", \"MidOfLine\" lub \"EndOfLine\".

-    `dimension_multi_rebar_text_position_type`określa typ pozycji etykiety wymiaru, w przypadku gdy widocznych jest wiele prętów zbrojeniowych. Może to być \"StartOfLine\", \"MidOfLine\" lub \"EndOfLine\".


<div class="mw-collapsible toccolours mw-collapsed">



#### Przykład


<div class="mw-collapsible-content">


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing

Rect = Draft.makeRectangle(400, 400)
Structure1 = Arch.makeStructure(Rect, height=1600)
Structure1.ViewObject.Transparency = 80
Structure2 = Arch.makeStructure(Rect, height=1600)
Structure2.ViewObject.Transparency = 80
Structure2.Placement = FreeCAD.Placement(FreeCAD.Vector(1000, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0, 0, 1), 0))
FreeCAD.ActiveDocument.recompute()

# Create Straight Rebars
TwoTiesSixRebars.makeTwoTiesSixRebars(
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
TwoTiesSixRebars.makeTwoTiesSixRebars(
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

# Create Reinforcement Drawing and Dimensioning
for drawing_view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
    struct_drawing_page_dict = make_reinforcement_drawing.makeStructuresReinforcementDrawing(
        structure_list=None,
        rebars_list=None,
        view="Front",
        rebars_stroke_width=0.35,
        rebars_color_style="Automatic",
        rebars_color=(0.67, 0.0, 0.0),
        structure_stroke_width=0.5,
        structure_color_style="Automatic",
        structure_color=(0.3, 0.9, 0.91),
        drawing_left_offset=20,
        drawing_top_offset=20,
        drawing_min_right_offset=20,
        drawing_min_bottom_offset=20,
        drawing_max_width=0,   # It is set to 0 to automatically set the default width based on other parameters
        drawing_max_height=0,  # It is set to 0 to automatically set the default height based on other parameters
        template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
        perform_dimensioning=True,
        dimension_rebars_filter_list=None,
        dimension_label_format="%M %C⌀%D,span=%S",
        dimension_font_family="DejaVu Sans",
        dimension_font_size=3,
        dimension_stroke_width=0.25,
        dimension_line_style="Continuous",
        dimension_line_color=(0.0, 0.0, 0.50),
        dimension_text_color=(0.0, 0.33, 0.0),
        dimension_single_rebar_line_start_symbol="None",
        dimension_single_rebar_line_end_symbol="FilledArrow",
        dimension_multi_rebar_line_start_symbol="FilledArrow",
        dimension_multi_rebar_line_end_symbol="FilledArrow",
        dimension_line_mid_point_symbol="Dot",
        dimension_left_offset=10,
        dimension_right_offset=10,
        dimension_top_offset=10,
        dimension_bottom_offset=10,
        dimension_left_offset_increment=6,
        dimension_right_offset_increment=6,
        dimension_top_offset_increment=6,
        dimension_bottom_offset_increment=6,
        dimension_single_rebar_outer_dim=False,
        dimension_multi_rebar_outer_dim=True,
        dimension_single_rebar_text_position_type="StartOfLine",
        dimension_multi_rebar_text_position_type="MidOfLine",
    )
    for drawing_page in struct_drawing_page_dict.values():
        drawing_view = drawing_page.Views[0]
        drawing_view.setExpression(
            "LeftOffset",
            u".Template.Width.Value / 2 - .Width.Value * .Scale / 2",
        )
        drawing_view.setExpression(
            "TopOffset",
            u".Template.Height.Value / 2 - .Height.Value * .Scale / 2",
        )
        drawing_view.recompute(True)
        drawing_page.recompute(True)
```


</div>


</div>



# Rysunek zbrojenia 



## Użycie 

1\. Otwórz model FreeCAD zawierający pręty zbrojeniowe utworzone za pomocą środowiska pracy [Zbrojenie](Reinforcement_Workbench/pl.md).

2\. W konsoli FreeCAD Python skopiuj poniższy fragment kodu, aby wygenerować rysunek zbrojenia z różnych widoków dla każdego elementu [konstrukcji](Arch_Structure/pl.md). 
```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeStructuresReinforcementDrawing,
)

for view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
    makeStructuresReinforcementDrawing(view=view)
```



## Obiekt ReinforcementDrawingView 

Obiekt widoku SVG rysunku prętów zbrojeniowych.



### Właściwości

-    **Structure**: Obiekt konstrukcji działający jako element główny dla prętów zbrojeniowych, które mają zostać uwzględnione na rysunku.

-    **Rebars**: Lista obiektów prętów zbrojeniowych, które mają zostać uwzględnione na rysunku.

-    **View**: Widok rysunku zbrojenia do wygenerowania. Może to być \"Przód\", \"Tył\", \"Lewo\", \"Prawo\", \"Góra\" lub \"Dół\".

-    **PositionType**: Typ położenia zbrojenia narysowanego na szablonie. Może przyjąć wartość \"Automatycznie\", aby obliczyć położenie rysunku przy użyciu **LeftOffset**, **TopOffset**, **MinRightOffset** i **MinBottomOffset**. LUB \"Niestandardowy \", aby ustawić rozmieszczenie za pomocą **X** i **Y**.

-    **RebarsStrokeWidth**: Szerokość obrysu prętów zbrojeniowych w rysunku zbrojenia SVG.

-    **RebarsColorStyle**: Styl koloru prętów zbrojeniowych w rysunku zbrojenia SVG. Ustaw na \"Automatycznie \", aby automatycznie wybrać kolor prętów zbrojeniowych LUB \"Niestandardowy \", aby wybrać wartość koloru kształtu z **RebarsColor**.

-    **RebarsColor**: Kolor prętów zbrojeniowych w rysunku zbrojenia SVG.

-    **StructureStrokeWidth**: Szerokość obrysu konstrukcji w rysunku zbrojenia SVG.

-    **StructureColorStyle**: Styl koloru konstrukcji w rysunku zbrojenia SVG. Ustaw na \"Automatycznie\", aby automatycznie wybrać kolor prętów zbrojeniowych, \"Niestandardowy\", aby wybrać wartość koloru kształtu z **StructureColor**. LUB \"Brak\", aby nie wypełniać struktury.

-    **StructureColor**: Kolor konstrukcji w rysunku zbrojenia SVG.

-    **Template**: Szablon dla widoku rysunku zbrojenia.

-    **Width**: Szerokość widoku rysunku zbrojenia SVG.

-    **Height**: Wysokość widoku SVG rysunku zbrojenia.

-    **LeftOffset**: Lewe odsunięcie widoku rysunku zbrojenia na szablonie.

-    **TopOffset**: Górne odsunięcie widoku rysunku zbrojenia na szablonie.

-    **MinRightOffset**: Minimalne prawe odsunięcie widoku rysunku zbrojenia na szablonie.

-    **MinBottomOffset**: Minimalne dolne odsunięcie widoku rysunku zbrojenia w szablonie.

-    **MaxWidth**: Maksymalna szerokość widoku rysunku zbrojenia.

-    **MaxHeight**: Maksymalna wysokość widoku rysunku zbrojenia.

-    **VisibleRebars**: Lista widocznych obiektów prętów zbrojeniowych w widoku rysunku.

-    **DimensionLeftOffset**: Lewe odsunięcie dla każdego nowego obiektu ReinforcementDimensioning.

-    **DimensionRightOffset**: Prawe odsunięcie dla każdego nowego obiektu ReinforcementDimensioning.

-    **DimensionTopOffset**: Górne odsunięcie dla każdego nowego obiektu ReinforcementDimensioning.

-    **DimensionBottomOffset**: dolne odsunięcie dla każdego nowego obiektu ReinforcementDimensioning.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wymiarowanie rysunku zbrojenia** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:



### Tworzenie rysunku zbrojenia 



#### Dla jednej konstrukcji 


```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeReinforcementDrawing,
)

reinforcement_drawing_page = makeReinforcementDrawing(
    structure,
    rebars_list,
    view,
    rebars_stroke_width,
    rebars_color_style,
    rebars_color,
    structure_stroke_width,
    structure_color_style,
    structure_color,
    drawing_left_offset,
    drawing_top_offset,
    drawing_min_right_offset,
    drawing_min_bottom_offset,
    drawing_max_width,
    drawing_max_height,
    template_file,
    dimension_left_offset,
    dimension_right_offset,
    dimension_top_offset,
    dimension_bottom_offset,
)
```

-   Tworzy obiekt {{Incode|ReinforcementDrawingView}} dla podanej listy obiektów [konstrukcji](Arch_Structure/pl.md) i [prętów](Arch_Rebar/pl.md).

-   Zwraca {{Incode|Reinforcement_drawing_page}} typu {{Incode|TechDraw::DrawPage}}.

-    `view`określa widok rysunku, który ma zostać wygenerowany. Może przyjmować wartości \"Przód\", \"Tył\", \"Lewo\", \"Prawo\", \"Góra\" lub \"Dół\".

-    `rebars_stroke_width`określa szerokość obrysu prętów zbrojeniowych w rysunku SVG.

-    `rebars_color_style`określa styl kolorów prętów zbrojeniowych. Ustaw na \"Automatycznie\", aby automatycznie wybrać kolor prętów zbrojeniowych lub \"Niestandardowy\", aby wybrać wartość koloru kształtu ze zmiennej `rebars_color`.

-    `rebars_color`określa kolor wypełnienia prętów zbrojeniowych w rysunku SVG.

   Format: (r, g, b)
   Wartość r, g, b powinna wynosić od 0 do 1, więc może być konieczne podzielenie wartości r, g, b przez 255, aby uzyskać wartość od 0 do 1.
   Upewnij się, że wartości r, g, b muszą być zmiennoprzecinkowe.
   Przykład: (0.67, 0.0, 0.0)

-    `structure_stroke_width`określa szerokość obrysu konstrukcji w rysunku SVG.

-    `structure_color_style`określa styl wypełnienia konstrukcji. Ustaw na \"Automatycznie\", aby automatycznie wybrać kolor konstrukcji lub \"Niestandardowy\", aby wybrać wartość koloru konstrukcji ze zmiennej `structure_color`.

-    `structure_color`określa kolor wypełnienia konstrukcji w rysunku SVG. Format: (r, g, b)

-    `drawing_left_offset`określa lewe odsunięcie widoku rysunku na `template_file`.

-    `drawing_top_offset`określa górne odsunięcie widoku rysunku na `template_file`.

-    `drawing_min_right_offset`określa minimalne prawe odsunięcie widoku rysunku na `template_file`.

-    `drawing_min_bottom_offset`określa minimalne dolne odsunięcie widoku rysunku na `template_file`.

-    `drawing_max_width`określa maksymalną szerokość rysunku na `template_file`.

-    `drawing_max_height`określa maksymalną wysokość rysunku na `template_file`.

-    `template_file`jest plikiem szablonu, który ma być użyty dla strony rysunku zbrojenia.

-    `dimension_left_offset`określa lewe odsunięcie wymiaru od rysunku.

-    `dimension_right_offset`określa prawe odsunięcie wymiaru od rysunku.

-    `dimension_top_offset`określa górne odsunięcie wymiaru od rysunku.

-    `dimension_bottom_offset`określa dolne odsunięcie wymiaru od rysunku.


<div class="mw-collapsible toccolours mw-collapsed">



##### Przykład 


<div class="mw-collapsible-content">


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

# Tworzenie prostych prętów zbrojeniowych.
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
    structure=Structure,
    facename="Face6",
)

rebars = Draft.get_objects_of_type(FreeCAD.ActiveDocument.Objects, "Rebar")

# Utwórz rysunek zbrojenia.
for drawing_view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
    make_reinforcement_drawing.makeReinforcementDrawing(
        structure=Structure,
        rebars_list=rebars,
        view=drawing_view,
        rebars_stroke_width=0.35,
        rebars_color_style="Automatic",
        rebars_color=(0.67, 0.0, 0.0),
        structure_stroke_width=0.5,
        structure_color_style="Automatic",
        structure_color=(0.3, 0.9, 0.91),
        drawing_left_offset=20,
        drawing_top_offset=20,
        drawing_min_right_offset=20,
        drawing_min_bottom_offset=20,
        drawing_max_width=0,   # It is set to 0 to automatically set the default width based on other parameters
        drawing_max_height=0,  # It is set to 0 to automatically set the default height based on other parameters
        template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
        dimension_left_offset=10,
        dimension_right_offset=10,
        dimension_top_offset=10,
        dimension_bottom_offset=10,
    )
```


</div>


</div>



#### Dla wielu konstrukcji 


```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeStructuresReinforcementDrawing,
)

structure_drawing_page_dict = makeStructuresReinforcementDrawing(
    structure_list=None,
    rebars_list=None,
    view="Front",
    rebars_stroke_width=REBARS_STROKE_WIDTH,
    rebars_color_style=REBARS_COLOR_STYLE,
    rebars_color=REBARS_COLOR,
    structure_stroke_width=STRUCTURE_STROKE_WIDTH,
    structure_color_style=STRUCTURE_COLOR_STYLE,
    structure_color=STRUCTURE_COLOR,
    drawing_left_offset=DRAWING_LEFT_OFFSET,
    drawing_top_offset=DRAWING_TOP_OFFSET,
    drawing_min_right_offset=DRAWING_MIN_RIGHT_OFFSET,
    drawing_min_bottom_offset=DRAWING_MIN_BOTTOM_OFFSET,
    drawing_max_width=DRAWING_MAX_WIDTH,
    drawing_max_height=DRAWING_MAX_HEIGHT,
    template_file=TEMPLATE_FILE,
)
```

-   Zwraca `structure_drawing_page_dict`, słownik z konstrukcją jako kluczem i odpowiednią stroną rysunku zbrojenia jako wartością.

-    `structure_list`jest listą obiektów konstrukcyjnych do wygenerowania ich rysunku zbrojenia. Jeśli nie zostanie podana, konstrukcje zostaną wybrane z aktywnego dokumentu działającego jako host dla obiektów prętów zbrojeniowych.

-    `rebars_list`jest listą obiektów prętów zbrojeniowych, które mają zostać uwzględnione na rysunku. Jeśli nie zostanie podana, obiekty prętów zbrojeniowych posiadające obiekt główny na liście structure_list zostaną wybrane z aktywnego dokumentu.


<div class="mw-collapsible toccolours mw-collapsed">



##### Przykład 


<div class="mw-collapsible-content">


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing

Rect = Draft.makeRectangle(400, 400)
Structure1 = Arch.makeStructure(Rect, height=1600)
Structure1.ViewObject.Transparency = 80
Structure2 = Arch.makeStructure(Rect, height=1600)
Structure2.ViewObject.Transparency = 80
Structure2.Placement = FreeCAD.Placement(FreeCAD.Vector(1000, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0, 0, 1), 0))
FreeCAD.ActiveDocument.recompute()

# Tworzenie prostych prętów zbrojeniowych.
TwoTiesSixRebars.makeTwoTiesSixRebars(
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

# Utwórz pręty zbrojeniowe w kształcie litery L z hakiem wzdłuż osi X.
TwoTiesSixRebars.makeTwoTiesSixRebars(
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

# Utwórz rysunek zbrojenia.
for drawing_view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
    make_reinforcement_drawing.makeStructuresReinforcementDrawing(
        structure_list=None,
        rebars_list=None,
        view=drawing_view,
        rebars_stroke_width=0.35,
        rebars_color_style="Automatic",
        rebars_color=(0.67, 0.0, 0.0),
        structure_stroke_width=0.5,
        structure_color_style="Automatic",
        structure_color=(0.3, 0.9, 0.91),
        drawing_left_offset=20,
        drawing_top_offset=20,
        drawing_min_right_offset=20,
        drawing_min_bottom_offset=20,
        drawing_max_width=0,   # It is set to 0 to automatically set the default width based on other parameters
        drawing_max_height=0,  # It is set to 0 to automatically set the default height based on other parameters
        template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
        dimension_left_offset=10,
        dimension_right_offset=10,
        dimension_top_offset=10,
        dimension_bottom_offset=10,
    )
```


</div>


</div>



# Wymiarowanie zbrojenia 



## Użycie 

1\. Otwórz model FreeCAD zawierający pręty zbrojeniowe utworzone za pomocą środowiska pracy [Zbrojenie](Reinforcement_Workbench/pl.md).

2\. W konsoli FreeCAD Python skopiuj poniższy fragment kodu, aby wygenerować rysunek zbrojenia z wymiarowaniem z różnych widoków dla każdego elementu [konstrukcji](Arch_Structure/pl.md).


```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeStructuresReinforcementDrawing,
)

for view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
    struct_drawing_page_dict = makeStructuresReinforcementDrawing(
        view=view, perform_dimensioning=True
    )
    for drawing_page in struct_drawing_page_dict.values():
        drawing_view = drawing_page.Views[0]
        drawing_view.setExpression(
            "LeftOffset",
            u".Template.Width.Value / 2 - .Width.Value * .Scale / 2",
        )
        drawing_view.setExpression(
            "TopOffset",
            u".Template.Height.Value / 2 - .Height.Value * .Scale / 2",
        )
        drawing_view.recompute(True)
        drawing_page.recompute(True)
```



## Obiekt ReinforcementDimensioning 

Obiekt widoku SVG wymiarowania prętów zbrojeniowych.



## Właściwości 

-    **ParentDrawingView**: Nadrzędny obiekt ReinforcementDrawingView zawierający rysunek obiektu [Pręta](Arch_Rebar.md).

-    **Rebar**: Obiekt [Pręta zbrojeniowego](Arch_Rebar.md) do wykonania wymiarowania.

-    **WayPointsType**: Typ WayPoints linii wymiarowej. Może to być \"Automatycznie\" (aby automatycznie wykonać wymiarowanie obiektu [Rebar](Arch_Rebar.md)) lub \" Niestandardowo \", aby użyć **WayPoints** do wykonania wymiarowania.

-    **WayPoints**: Lista punktów wektorowych, które zostaną użyte do wygenerowania linii wymiarowej.

-    **TextPositionType**: Typ pozycji tekstu wymiaru. Może przyjmować wartość \"StartOfLine\", \"MidOfLine\" lub \"EndOfLine\".

-    **DimensionFormat**: Format etykiety wymiaru.

   Przykład: "%M %C⌀%D,span=%S".
   Tutaj: %M -> Rebar.Mark
          %C -> Rebar.Amount
          %D -> Rebar.Diameter
          %S -> Rebar span length

-    **Font**: Rodzina czcionek etykiety wymiaru.

-    **FontSize**: Rozmiar czcionki etykiety wymiaru.

-    **StrokeWidth**: Szerokość obrysu linii wymiaru.

-    **LineStyle**: Styl obrysu linii wymiarowej. Może przyjmować wartość \" Ciągła\", \"Kreska\", \"Kropka\", \"KreskaKropka\" lub \"KreskaKropkaKropka\".

-    **LineColor**: Kolor linii wymiarowej.

-    **TextColor**: Kolor etykiety wymiaru.

-    **LineStartSymbol**: Symbol początkowy linii wymiaru. Może przyjmować wartość \"FilledArrow\", \"Tick\", \"Dot\" lub \"None\".

-    **LineEndSymbol**: Symbol końca linii wymiarowej. Może przyjmować wartość \"FilledArrow\", \"Tick\", \"Dot\" lub \"None\".

-    **LineMidPointSymbol**: Symbol punktu środkowego linii wymiarowej. Może przyjmować wartość \"Tick\", \"Dot\" lub \"None\".

-    **DimensionLeftOffset**: Lewe odsunięcie dla automatycznego wymiarowania zbrojenia.

-    **DimensionRightOffset**: Prawe odsunięcie dla automatycznego wymiarowania zbrojenia.

-    **DimensionTopOffset**: Górne odsunięcie dla automatycznego wymiarowania zbrojenia.

-    **DimensionBottomOffset**: Dolne odsunięcie dla automatycznego wymiarowania zbrojenia.

-    **SingleRebar_LineStartSymbol**: Symbol początku linii wymiarowej, w przypadku gdy widoczny jest pojedynczy pręt zbrojeniowy. Może przyjmować wartość \"FilledArrow\", \"Tick\", \"Dot\" lub \"None\". Jest używany tylko wtedy, gdy **WayPointsType** jest ustawiony na \"Automatic\".

-    **SingleRebar_LineEndSymbol**: Symbol końca linii wymiarowej, w przypadku gdy widoczny jest pojedynczy pręt zbrojeniowy. Może to być \"FilledArrow\", \"Tick\", \"Dot\" lub \"None\". Jest używany tylko wtedy, gdy **WayPointsType** jest ustawiony na \"Automatic\".

-    **MultiRebar_LineStartSymbol**: Symbol początku linii wymiarowej, w przypadku gdy widocznych jest wiele prętów zbrojeniowych. Może to być \"FilledArrow\", \"Tick\", \"Dot\" lub \"None\". Jest używany tylko wtedy, gdy **WayPointsType** jest ustawiony na \"Automatycznie\".

-    **SingleRebar_OuterDimension**: Określa, czy linie wymiarowe mają znajdować się poza rysunkiem zbrojenia, w przypadku gdy widoczny jest pojedynczy pręt zbrojeniowy. Jest używany tylko wtedy, gdy **WayPointsType** jest ustawiony na \"Automatycznie\".

-    **MultiRebar_OuterDimension**: Określa, czy linie wymiarowe mają znajdować się poza rysunkiem zbrojenia, w przypadku gdy widocznych jest wiele prętów zbrojeniowych. Jest używany tylko wtedy, gdy **WayPointsType** jest ustawiony na \"Automatycznie\".

-    **SingleRebar_TextPositionType**: Określa typ położenia etykiety wymiaru, w przypadku gdy widoczny jest pojedynczy pręt zbrojeniowy. Może przyjmować wartości \"StartOfLine\", \"MidOfLine\" lub \"EndOfLine\". Jest używany tylko wtedy, gdy **WayPointsType** jest ustawiony na \"Automatycznie\".

-    **MultiRebar_TextPositionType**: Określa typ położenia etykiety wymiaru w przypadku, gdy widocznych jest wiele prętów zbrojeniowych. Może przyjmować wartości \"StartOfLine\", \"MidOfLine\" lub \"EndOfLine\". Jest używany tylko wtedy, gdy **WayPointsType** jest ustawiony na \"Automatycznie\".



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wymiarowanie rysunku zbrojenia** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:



### Tworzenie obiektu wymiarowania zbrojenia 


```python
from ReinforcementDrawing.ReinforcementDimensioning import (
    makeReinforcementDimensioningObject,
)

dimension_object = makeReinforcementDimensioningObject(
    rebar,
    parent_drawing_view,
    drawing_page=None,
    dimension_label_format="%M %C⌀%D,span=%S",
    dimension_font_family="DejaVu Sans",
    dimension_font_size=3,
    dimension_stroke_width=0.25,
    dimension_line_style="Continuous",
    dimension_line_color=(0.0, 0.0, 0.50),
    dimension_text_color=(0.0, 0.33, 0.0),
    dimension_single_rebar_line_start_symbol="None",
    dimension_single_rebar_line_end_symbol="FilledArrow",
    dimension_multi_rebar_line_start_symbol="FilledArrow",
    dimension_multi_rebar_line_end_symbol="FilledArrow",
    dimension_line_mid_point_symbol="Dot",
    dimension_left_offset_increment=10,
    dimension_right_offset_increment=10,
    dimension_top_offset_increment=10,
    dimension_bottom_offset_increment=10,
    dimension_single_rebar_outer_dim=False,
    dimension_multi_rebar_outer_dim=True,
    dimension_single_rebar_text_position_type="StartOfLine",
    dimension_multi_rebar_text_position_type="MidOfLine",
)
```

-   Tworzy i zwraca obiekt `ReinforcementDimensioning` dla danego obiektu `rebar`.

-    `parent_drawing_view`jest obiektem `ReinforcementDrawingView` zawierającym rysunek obiektu `rebar`.

-    `drawing_page`jest obiektem typu TechDraw::DrawPage używanym do wyświetlania `parent_drawing_view`.

-    `dimension_label_format`jest formatem używanym dla etykiety wymiaru.

   Przykład: "%M %C⌀%D,span=%S".
   Tutaj: %M -> Rebar.Mark
          %C -> Rebar.Amount
          %D -> Rebar.Diameter
          %S -> Rebar span length

-    `dimension_font_family`to rodzina czcionki etykiety wymiaru.

-    `dimension_font_size`to rozmiar czcionki etykiety wymiaru.

-    `dimension_stroke_width`to szerokość obrysu linii wymiaru.

-    `dimension_line_style`to styl obrysu linii wymiarowej. Może przyjmować wartość \"Ciągła\", \"Kreska\", \"Kropka\", \"KreskaKropka\" lub \"KreskaKropkaKropka\".

-    `dimension_line_color`to kolor linii wymiarowej.

   Format: (r, g, b)
   Wartość r, g, b powinna zawierać się w przedziale od 0 do 1, więc może być konieczne podzielenie wartości r, g, b przez 255, aby uzyskać wartość od 0 do 1.
   Upewnij się, że r, g, b muszą być zmiennoprzecinkowe

-    `dimension_text_color`to kolor etykiety wymiaru.

-    `dimension_single_rebar_line_start_symbol`to symbol początku linii wymiarowej, w przypadku gdy widoczny jest pojedynczy pręt zbrojeniowy. Może przyjmować wartość \"FilledArrow\", \"Tick\", \"Dot\" lub \"None\".

-    `dimension_single_rebar_line_end_symbol`to symbol końca linii wymiarowej, w przypadku gdy widoczny jest pojedynczy pręt zbrojeniowy. Może przyjmować wartość \"FilledArrow\", \"Tick\", \"Dot\" lub \"None\".

-    `dimension_multi_rebar_line_start_symbol`to symbol początku linii wymiarowej, w przypadku gdy widocznych jest wiele prętów zbrojeniowych. Może przyjmować wartość \"FilledArrow\", \"Tick\", \"Dot\" lub \"None\".

-    `dimension_multi_rebar_line_end_symbol`to symbol końca linii wymiarowej, w przypadku gdy widocznych jest wiele prętów zbrojeniowych. Może to być \"FilledArrow\", \"Tick\", \"Dot\" lub \"None\".

-    `dimension_line_mid_point_symbol`to symbol punktu środkowego linii wymiarowej. Może to być \"Tick\", \"Dot\" lub \"None\".

-    `dimension_left_offset_increment`to przyrost lewego odsunięcia w celu odsunięcia każdej nowej etykiety wymiaru od rysunku.

-    `dimension_right_offset_increment`to przyrost prawego odsunięcia w celu odsunięcia każdej nowej etykiety wymiaru od rysunku.

-    `dimension_top_offset_increment`to przyrost górnego odsunięcia w celu odsunięcia każdej nowej etykiety wymiaru od rysunku.

-    `dimension_bottom_offset_increment`to przyrost dolnego odsunięcia w celu odsunięcia każdej nowej etykiety wymiaru od rysunku.

-    `dimension_single_rebar_outer_dim`określa, czy linie wymiarowe mają znajdować się poza rysunkiem zbrojenia, w przypadku gdy widoczny jest pojedynczy pręt zbrojeniowy.

-    `dimension_multi_rebar_outer_dim`określa, czy linie wymiarowe mają znajdować się poza rysunkiem zbrojenia, w przypadku gdy widocznych jest wiele prętów zbrojeniowych.

-    `dimension_single_rebar_text_position_type`określa typ pozycji etykiety wymiaru, w przypadku gdy widoczny jest pojedynczy pręt zbrojeniowy. Może przyjmować wartość \"StartOfLine\", \"MidOfLine\" lub \"EndOfLine\".

-    `dimension_multi_rebar_text_position_type`określa typ pozycji etykiety wymiaru, w przypadku gdy widocznych jest wiele prętów zbrojeniowych. Może przyjmować wartość \"StartOfLine\", \"MidOfLine\" lub \"EndOfLine\".


<div class="mw-collapsible toccolours mw-collapsed">



#### Przykład 


<div class="mw-collapsible-content">


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing
from ReinforcementDrawing.ReinforcementDimensioning import (
    makeReinforcementDimensioningObject,
)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

# Create Straight Rebars
TwoTiesSixRebars.makeTwoTiesSixRebars(
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
    structure=Structure,
    facename="Face6",
)

rebars = Draft.get_objects_of_type(FreeCAD.ActiveDocument.Objects, "Rebar")

# Create Reinforcement Drawing
drawing_page = make_reinforcement_drawing.makeReinforcementDrawing(
    structure=Structure,
    rebars_list=rebars,
    view="Front",
    rebars_stroke_width=0.35,
    rebars_color_style="Automatic",
    rebars_color=(0.67, 0.0, 0.0),
    structure_stroke_width=0.5,
    structure_color_style="Automatic",
    structure_color=(0.3, 0.9, 0.91),
    drawing_left_offset=20,
    drawing_top_offset=20,
    drawing_min_right_offset=20,
    drawing_min_bottom_offset=20,
    drawing_max_width=0,                    # It is set to 0 to automatically set the default width based on other parameters
    drawing_max_height=0,                   # It is set to 0 to automatically set the default height based on other parameters
    template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
    dimension_left_offset=10,
    dimension_right_offset=10,
    dimension_top_offset=10,
    dimension_bottom_offset=10,
)

visible_rebars = drawing_page.Views[0].VisibleRebars

# Create Reinforcement Dimensioning for single rebar
makeReinforcementDimensioningObject(
    visible_rebars[0],
    parent_drawing_view,
    drawing_page=None,
    dimension_label_format="%M %C⌀%D,span=%S",
    dimension_font_family="DejaVu Sans",
    dimension_font_size=3,
    dimension_stroke_width=0.25,
    dimension_line_style="Continuous",
    dimension_line_color=(0.0, 0.0, 0.50),
    dimension_text_color=(0.0, 0.33, 0.0),
    dimension_single_rebar_line_start_symbol="None",
    dimension_single_rebar_line_end_symbol="FilledArrow",
    dimension_multi_rebar_line_start_symbol="FilledArrow",
    dimension_multi_rebar_line_end_symbol="FilledArrow",
    dimension_line_mid_point_symbol="Dot",
    dimension_left_offset_increment=10,
    dimension_right_offset_increment=10,
    dimension_top_offset_increment=10,
    dimension_bottom_offset_increment=10,
    dimension_single_rebar_outer_dim=False,
    dimension_multi_rebar_outer_dim=True,
    dimension_single_rebar_text_position_type="StartOfLine",
    dimension_multi_rebar_text_position_type="MidOfLine",
)

# Create Reinforcement Dimensioning for all visible rebars in drawing view
for visible_rebar in visible_rebars:
    makeReinforcementDimensioningObject(
        visible_rebar,
        parent_drawing_view,
        drawing_page=None,
        dimension_label_format="%M %C⌀%D,span=%S",
        dimension_font_family="DejaVu Sans",
        dimension_font_size=3,
        dimension_stroke_width=0.25,
        dimension_line_style="Continuous",
        dimension_line_color=(0.0, 0.0, 0.50),
        dimension_text_color=(0.0, 0.33, 0.0),
        dimension_single_rebar_line_start_symbol="None",
        dimension_single_rebar_line_end_symbol="FilledArrow",
        dimension_multi_rebar_line_start_symbol="FilledArrow",
        dimension_multi_rebar_line_end_symbol="FilledArrow",
        dimension_line_mid_point_symbol="Dot",
        dimension_left_offset_increment=10,
        dimension_right_offset_increment=10,
        dimension_top_offset_increment=10,
        dimension_bottom_offset_increment=10,
        dimension_single_rebar_outer_dim=False,
        dimension_multi_rebar_outer_dim=True,
        dimension_single_rebar_text_position_type="StartOfLine",
        dimension_multi_rebar_text_position_type="MidOfLine",
    )
```


</div>


</div>



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement DrawingDimensioning/pl
