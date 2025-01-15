---
 GuiCommand:
   Name: Reinforcement BeamRebars
   Name/pl: Zbrojenie: Zbrojenie belki
   MenuLocation: 3D/BIM , Narzędzia zbrojenia , Zbrojenie belki
   Workbenches: Reinforcement_Workbench/pl, BIM_Workbench/pl
   Version: 0.17
   SeeAlso: 
---

# Reinforcement BeamRebars/pl



## Opis

Narzędzie **Zbrojenie belki** pozwala użytkownikowi na tworzenie prętów zbrojeniowych wewnątrz obiektu [konstrukcji](Arch_Structure/pl.md) belki.

To polecenie jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) [Zbrojenie](Reinforcement_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) poprzez menu **Przybory → Menadżera dodatków → Zbrojenie**.

![](images/Arch_Rebar_BeamReinforcement_example.png ) 
*Zbrojenie belki wewnątrz [konstrukcji architektury](Arch_Structure/pl.md)* belki.



## Użycie

1\. Wybierz prawą ścianę wcześniej utworzonej **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)** belki o długości wzdłuż osi X. Lub wybierz przednią ścianę wcześniej utworzonej **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)** belki o długości wzdłuż osi Y.

2\. Następnie wybierz **<img src="images/Reinforcement_BeamRebars.svg" width=16px> [Zbrojenie belki](Reinforcement_BeamRebars/pl.md)** z narzędzi prętów zbrojeniowych.

3\. Na ekranie pojawi się okno dialogowe, jak pokazano poniżej.

:   <img alt="" src=images/BeamReinforcementDialog_Stirrups.png  style="width:700px;">

:   
    
*Okno dialogowe narzędzia Zbrojenie belki.*
    

4\. Wybierz żądany typ zbrojenia belki.

5\. Podaj dane wejściowe dla danych związanych ze strzemionami.

6\. Kliknij **Dalej**, a okno dialogowe zostanie zaktualizowane w sposób pokazany poniżej.

:   <img alt="" src=images/BeamReinforcementDialog_TopRebars.png  style="width:700px;">

:   
    
*Okno dialogowe dla danych górnych prętów zbrojeniowych.*
    

7\. Wprowadź dane dla górnych prętów zbrojeniowych.


{{ColoredParagraph|#f8f9fa|

: Aby edytować wartość Ilość#Średnica@Odsunięcie, kliknij przycisk **Edytuj** obok etykiety Ilość#Średnica@Odsunięcie. Pojawi się okno dialogowe, jak pokazano poniżej.

: <img src="images/Beam_TopReinforcement_NumberDiameterOffset.png" width=500px>

: Aby edytować wartość typu pręta zbrojeniowego, kliknij przycisk **Edycja** obok etykiety typu pręta zbrojeniowego. Pojawi się okno dialogowe, jak pokazano poniżej.

: <img src="images/Beam_TopReinforcement_RebarType.png" width=300px>

: Aby edytować wartość Orientacja haka, kliknij przycisk **Edycja** obok etykiety Orientacja haka. Pojawi się okno dialogowe, jak pokazano poniżej.

: <img src="images/Beam_TopReinforcement_HookOrientation.png" width=300px>

: Aby edytować wartość Przedłużenie haka, kliknij przycisk **Edycja** obok etykiety Przedłużenie haka. Pojawi się okno dialogowe, jak pokazano poniżej.

: <img src="images/Beam_TopReinforcement_HookExtension.png" width=300px>

: Aby edytować wartość zaokrąglenia dla pręta "L", kliknij przycisk **Edycja** obok etykiety Zaokrąglenie. Pojawi się okno dialogowe, jak pokazano poniżej.

: <img src="images/Beam_TopReinforcement_LRebarRounding.png" width=300px>

: Aby edytować wartość Odstępu między warstwami, kliknij przycisk **Edycja** obok etykiety Odstępu między warstwami. Pojawi się okno dialogowe, jak pokazano poniżej.

: <img src="images/Beam_TopReinforcement_LayerSpacing.png" width=300px>
}}

8\. Kliknij **Dalej**, a okno dialogowe zostanie zaktualizowane w sposób pokazany poniżej.

:   <img alt="" src=images/BeamReinforcementDialog_BottomRebars.png  style="width:700px;">

:   
    
*Okienko dialogowe dla danych dolnych prętów zbrojeniowych.*
    

9\. Wprowadź dane dla dolnych prętów zbrojeniowych podobnie do danych dla górnych prętów zbrojeniowych.

10\. Kliknij **Dalej**, a okno dialogowe zostanie zaktualizowane w sposób pokazany poniżej.

:   <img alt="" src=images/BeamReinforcementDialog_LeftRebars.png  style="width:700px;">

:   
    
*Okienko dialogowe dla danych prętów zbrojeniowych na  lewej ścinanie.*
    

11\. Ustaw dane dla prętów zbrojeniowych na ścinanie po lewej stronie.


{{ColoredParagraph|#f8f9fa|

: Aby edytować wartość Ilość#Średnica@Odsunięcie, kliknij przycisk **Edytuj** obok etykiety Ilość#Średnica@Odsunięcie. Pojawi się okno dialogowe, jak pokazano poniżej.

: <img src="images/Beam_ShearReinforcement_NumberDiameterOffset.png" width=500px>

: Aby edytować wartość typu pręta zbrojeniowego, kliknij przycisk **Edycja** obok etykiety typu pręta zbrojeniowego. Pojawi się okno dialogowe, jak pokazano poniżej.

: <img src="images/Beam_ShearReinforcement_RebarType.png" width=300px>

: Aby edytować wartość Orientacja haka, kliknij przycisk **Edycja** obok etykiety Orientacja haka. Pojawi się okno dialogowe, jak pokazano poniżej.

: <img src="images/Beam_ShearReinforcement_HookOrientation.png" width=300px>

: Aby edytować wartość Przedłużenie haka, kliknij przycisk **Edycja** obok etykiety Przedłużenie haka. Pojawi się okno dialogowe, jak pokazano poniżej.

: <img src="images/Beam_ShearReinforcement_HookExtension.png" width=300px>

: Aby edytować wartość zaokrąglenia dla pręta "L", kliknij przycisk **Edycja** obok etykiety Zaokrąglenie. Pojawi się okno dialogowe, jak pokazano poniżej.

: <img src="images/Beam_ShearReinforcement_LRebarRounding.png" width=300px>
}}

12\. Kliknij **Dalej**, a okno dialogowe zostanie zaktualizowane w sposób pokazany poniżej.

:   <img alt="" src=images/BeamReinforcementDialog_RightRebars.png  style="width:700px;">

:   
    
*Okienko dialogowe dla danych prętów zbrojeniowych na  prawej ścinanie.*
    

11\. Ustaw dane dla prętów zbrojeniowych na prawej ścinanie podobnie jak na lewej stronie.

14\. Kliknij **OK** lub **Zastosuj**, aby wygenerować zbrojenie belki.

15\. Kliknij **Anuluj**, aby zamknąć okno dialogowe.



## Właściwości

**Strzemiona:**

-    **Otulina lewa**: Odległość między lewym końcem opaski a lewą ścianą konstrukcji.

-    **Otulina prawa**: Odległość między prawym końcem opaski a prawą ścianą konstrukcji.

-    **Otulina górna**: Odległość między krawatem a górną ścianą konstrukcji.

-    **Otulina dolna**: Odległość między krawatem a dolną ścianą konstrukcji.

-    **Odsunięcie**: Odległość między opaską a górną/dolną ścianą konstrukcji.

-    **Średnica**: Średnica opaski.

-    **Kąt wygięcia**: Kąt wygięcia określa kąt na końcach cięgna.

-    **Współczynnik rozciągnięcia**: Współczynnik rozciągnięcia określa długość końca opaski, wyrażoną jako wielokrotność średnicy.

-    **Ilość**: Liczba strzemion.

-    **Rozstaw**: Odległość między osiami każdego strzemiona.

**Pręty zbrojeniowe górne / dolne:** Pręty zbrojeniowe obecne w górnej / dolnej części belki

-    **IlośćŚrednicaOdsunięcie**: Krotka ciągu Ilość#Średnica@Odsunięcie. Każdy element krotki reprezentuje zbrojenie dla każdej nowej warstwy.

-    **Typ zbrojenia**: Lista krotek typu prętów zbrojeniowych.

-    **Orientacja haka**: Lista krotek orientacji haków w kształcie litery \"L\".

-    **Wydłużenie haka**: Lista krotek długości haków prętów zbrojeniowych w kształcie \"L\".

-    **Zaokrąglenie**: Lista krotek wartości zaokrąglenia, która ma być zastosowana do narożników prętów zbrojeniowych \"L\", wyrażona w krotności średnicy.

-    **Rozstaw warstw**: Lista odstępów między dwiema kolejnymi warstwami zbrojenia.

**Pręty zbrojeniowe po lewej / prawej stronie:** Pręty zbrojeniowe obecne po lewej / prawej części belki.

-    **IlośćŚrednicaOdsunięcie**: Ciąg Ilość#Średnica@Odsunięcie ustawiony dla prętów zbrojeniowych.

-    **Typ zbrojenia**: Lista typu prętów zbrojeniowych.

-    **Orientacja haka**: Lista orientacji haków w kształcie litery \"L\".

-    **Wydłużenie haka**: Lista długości haków prętów zbrojeniowych w kształcie \"L\".

-    **Zaokrąglenie**: Lista wartości zaokrąglenia, która ma być zastosowana do narożników prętów zbrojeniowych \"L\", wyrażona w krotności średnicy.

-    **Rozstaw warstw**: Lista odstępów między dwiema kolejnymi warstwami zbrojenia.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Zbrojenie belki** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:



### Tworzenie strzemion dwunożnych 


```python
RebarGroup = makeReinforcement(
    l_cover_of_stirrup,
    r_cover_of_stirrup,
    t_cover_of_stirrup,
    b_cover_of_stirrup,
    offset_of_stirrup,
    bent_angle,
    extension_factor,
    dia_of_stirrup,
    number_spacing_check,
    number_spacing_value,
    top_reinforcement_number_diameter_offset,
    top_reinforcement_rebar_type,
    top_reinforcement_layer_spacing,
    bottom_reinforcement_number_diameter_offset,
    bottom_reinforcement_rebar_type,
    bottom_reinforcement_layer_spacing,
    left_rebars_number_diameter_offset,
    left_rebars_type,
    left_rebars_spacing,
    right_rebars_number_diameter_offset,
    right_rebars_type,
    right_rebars_spacing,
    top_reinforcement_l_rebar_rounding=2,
    top_reinforcement_hook_extension=40,
    top_reinforcement_hook_orientation="Front Inside",
    bottom_reinforcement_l_rebar_rounding=2,
    bottom_reinforcement_hook_extension=40,
    bottom_reinforcement_hook_orientation="Front Inside",
    left_l_rebar_rounding=2,
    left_rebars_hook_extension=40,
    left_rebars_hook_orientation="Front Inside",
    right_l_rebar_rounding=2,
    right_rebars_hook_extension=40,
    right_rebars_hook_orientation="Front Inside",
    structure=None,
    facename=None,
)
```

-   Tworzy obiekt `RebarGroup` z podanego `structure`, który jest [konstrukcją architektury](Arch_Structure.md) i `facename`, który jest ścianą tej konstrukcji.
    -   Jeśli nie podano `structure` ani `facename`, jako dane wejściowe zostanie przyjęta ściana wybrana przez użytkownika.

-    `l_cover_of_stirrup`, `r_cover_of_stirrup`, `t_cover_of_stirrup`, `b_cover_of_stirrup` i `offset_of_stirrup` są wewnętrznymi odległościami przesunięcia dla elementów strzemion względem powierzchni struktury. Są to odpowiednio lewe, prawe, górne, dolne i przednie/tylne odsunięcia.

-    `bent_angle`definiuje kąt wierzchołka pętli zbrojenia strzemienia.

-    `extension_factor`określa długość końcówki pętli wzmacniającej strzemienia, wyrażoną jako wielokrotność średnicy.

-    `dia_of_stirrup`to średnica strzemienia.

-    `number_spacing_check`, jeśli ma wartość `number_spacing_value`, utworzy tyle strzemion, ile podano w `number_spacing_value`. Jeśli ma wartość `number_spacing_value`, utworzy strzemiona oddzielone wartością liczbową `number_spacing_value`.

-    `number_spacing_value`określa liczbę strzemion lub wartość odstępu między nimi, w zależności od `number_spacing_check`.

-    `top_reinforcement_number_diameter_offset`i `bottom_reinforcement_number_diameter_offset` są krotkami ciągów number_diameter_offset. Każdy element krotki reprezentuje zbrojenie dla każdej nowej warstwy.

   Składnia: (
               "number1#diameter1@offset1+number2#diameter2@offset2+...",
               "number3#diameter3@offset3+number4#diameter4@offset4+...",
               ...,
           )

-    `top_reinforcement_rebar_type`i `bottom_reinforcement_rebar_type` określa typ górnych/dolnych prętów zbrojeniowych.

   Możliwe wartości:
   1. "PrętyProste" lub "PrętywKształcieL".
', ...), a liczba elementów krotki musi być równa liczbie warstw zbrojenia.
      warstw.
   3. [
', ...),
', ...),
          ...,
      ]
      Każdy element listy jest krotką, która określa typ pręta zbrojeniowego każdej warstwy zbrojenia. Każdy element krotki
      reprezentuje typ rabar_type dla każdego zestawu prętów zbrojeniowych.
   4. [
,
', ...),
          ...,
      ]

-    `top_reinforcement_layer_spacing`i `bottom_reinforcement_layer_spacing` to odstęp między dwiema kolejnymi warstwami zbrojenia.

   Możliwe wartości:

, ...), a liczba elementów krotki musi być
      równa o jeden mniej niż liczba warstw.

-    `left_rebars_number_diameter_offset`i `right_rebars_number_diameter_offset` są ciągami znaków number_diameter_offset.

   Składnia: "number1#diameter1@offset1+number2#diameter2@offset2+..."

-    `left_rebars_type`i `right_rebars_type` określa typ prętów zbrojeniowych lewych/prawych.

   Możliwe wartości:
   1. "StraightRebar" lub "LShapeRebar".
', ...) i każdy element krotki reprezentuje rabar_type dla każdego zestawu prętów zbrojeniowych.

-    `left_rebars_spacing`i `right_rebars_spacing` to wyraźne odstępy między kolejnymi prętami zbrojenia.

-    `top_reinforcement_l_rebar_rounding`i `bottom_reinforcement_l_rebar_rounding` to parametr określający promień gięcia górnych / dolnych prętów zbrojeniowych w kształcie litery L, wyrażony jako wielokrotność średnicy. Możliwa składnia jest podobna do omówionej powyżej dla `top_reinforcement_rebar_type` / `bottom_reinforcement_rebar_type`.

-    `top_reinforcement_hook_extension`i `bottom_reinforcement_hook_extension` to długość haka prętów zbrojeniowych L. Możliwa składnia jest podobna do omówionej powyżej dla `top_reinforcement_rebar_type` / `bottom_reinforcement_rebar_type`.

-    `top_reinforcement_hook_orientation`i `bottom_reinforcement_hook_orientation` określa orientację haka L. Może to być `"Front Inside"`, `"Front Outside"`, `"Rear Inside"` lub `"Rear Outside"`. Możliwa składnia jest podobna do omówionej powyżej dla `top_reinforcement_rebar_type` / `bottom_reinforcement_rebar_type`.

-    `left_l_rebar_rounding`i `right_l_rebar_rounding` to parametr określający promień gięcia lewych / prawych prętów zbrojeniowych w kształcie L, wyrażony jako wielokrotność średnicy. Możliwa składnia jest podobna do omówionej powyżej dla `left_rebars_type` / `right_rebars_type`.

-    `left_rebars_hook_extension`i `right_rebars_hook_extension` to długość haka prętów zbrojeniowych w kształcie L. Możliwa składnia jest podobna do omówionej powyżej dla `left_rebars_type` / `right_rebars_type`.

-    `left_rebars_hook_orientation`i `right_rebars_hook_orientation` określa orientację haka L. Może to być `"Front Inside"`, `"Front Outside"`, `"Rear Inside"` lub `"Rear Outside"`. Możliwa składnia jest podobna do omówionej powyżej dla `left_rebars_type` / `right_rebars_type`.



#### Przykład


```python
import FreeCAD, Arch
from BeamReinforcement import TwoLeggedBeam

Structure = Arch.makeStructure(length=3000.0,width=200.0,height=400.0)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

RebarGroup = TwoLeggedBeam.makeReinforcement(
    l_cover_of_stirrup=20,
    r_cover_of_stirrup=20,
    t_cover_of_stirrup=20,
    b_cover_of_stirrup=20,
    offset_of_stirrup=100,
    bent_angle=135,
    extension_factor=4,
    dia_of_stirrup=8,
    number_spacing_check=False,
    number_spacing_value=200,
    top_reinforcement_number_diameter_offset=("1#20@-60+2#16@-60+1#20@-60", "3#16@-100"),
    top_reinforcement_rebar_type="LShapeRebar",
    top_reinforcement_layer_spacing=30,
    bottom_reinforcement_number_diameter_offset=("1#20@-60+2#16@-60+1#20@-60", "3#16@-100"),
    bottom_reinforcement_rebar_type="LShapeRebar",
    bottom_reinforcement_layer_spacing=30,
    left_rebars_number_diameter_offset="1#16@-100+1#16@-100+1#16@-100",
    left_rebars_type="LShapeRebar",
    left_rebars_spacing=30,
    right_rebars_number_diameter_offset="1#16@-100+1#16@-100+1#16@-100",
    right_rebars_type="LShapeRebar",
    right_rebars_spacing=30,
    top_reinforcement_l_rebar_rounding=2,
    top_reinforcement_hook_extension=100,
    top_reinforcement_hook_orientation="Rear Outside",
    bottom_reinforcement_l_rebar_rounding=2,
    bottom_reinforcement_hook_extension=100,
    bottom_reinforcement_hook_orientation="Rear Outside",
    left_l_rebar_rounding=2,
    left_rebars_hook_extension=80,
    left_rebars_hook_orientation=("Rear Inside", "Front Inside", "Rear Inside"),
    right_l_rebar_rounding=2,
    right_rebars_hook_extension=80,
    right_rebars_hook_orientation=("Front Inside", "Rear Inside", "Front Inside"),
    structure=Structure,
    facename="Face6",
)
```



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement BeamRebars/pl
