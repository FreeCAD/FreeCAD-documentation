---
 GuiCommand:
   Name: FCGear BevelGear
   Name/pl: FCGear: Koło zębate stożkowe
   MenuLocation: Gear , Koło zębate stożkowe
   Workbenches: FCGear_Workbench/pl
   Version: v0.16
---

# FCGear BevelGear/pl



## Opis

Częściowo ze względu na generowany przez nie hałas, przekładnie stożkowe nie są używane tak często, jak inne rodzaje przekładni. Są one jednak nadal używane w niektórych sektorach, takich jak pakowanie żywności i żywności w puszkach, sprzęt do pielęgnacji trawników i ogrodów, maszyny takie jak wiertarki i młyny, systemy kompresji na rynku gazu i ropy oraz zawory sterujące przepływem.

Spiralne koła zębate stożkowe mają zakrzywione zęby, które zapewniają łagodniejsze zazębianie i większy kontakt między zębami w porównaniu z prostymi kołami zębatymi stożkowymi. Zmniejsza to wibracje i hałas. Mogą być używane przy dużych prędkościach i są zwykle stosowane w przekładniach motocyklowych i rowerowych.

![](images/Bevel-Gear_example.png ) 
*Od lewej do prawej: Przekładnia czołowa, przekładnia spiralna.*



## Użycie

1.  Przejdź do środowiska pracy <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **[<img src=images/FCGear_BevelGear.svg style="width:16px"> '''Koło zębate stożkowe'''** na pasku narzędzi.
    -   Wybierz z menu opcję **Gear → [<img src=images/FCGear_BevelGear.svg style="width:16px"> Koło zębate stożkowe**.
3.  Zmień parametry zębatki na wymagane *(patrz [Właściwości](#Właściwości.md))*.



## Właściwości

Obiekt Koło zębate stożkowe wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Wysokość|Length**: Wartością domyślną jest {{Value|5}}. Wartość szerokości koła zębatego stożkowego.

-    **moduł|Length**: Wartością domyślną jest {{Value|1}}. Moduł jest stosunkiem średnicy referencyjnej koła zębatego podzielonej przez liczbę zębów (patrz [Uwagi](#Uwagi.md)).

-    **reset_origin|Bool**: Jeśli przyjmie wartość {{True/pl}} *(domyślnie)* środek osi znajduje się na środku dolnej części koła zębatego (patrz [Uwagi](#Uwagi.md)).

-    **Zęby|Integer**: Wartością domyślną jest {{Value|15}}. Liczba zębów.


{{Properties_Title|Obliczone}}

-    **luz_kątowy|Angle**: *(tylko do odczytu)*.

-    **dw|Length**: *(tylko do odczytu)* Średnica podziałki roboczej.


{{Properties_Title|Śrubowy}}

-    **beta|Angle**: Wartością domyślną jest {{Value|0 °}}. Przy kącie linii śrubowej β tworzone jest stożkowe koło zębate - wartość dodatnia → kierunek obrotu w prawo, wartość ujemna → kierunek obrotu w lewo.


{{Properties_Title|Ewolwenta}}

-    **kąt_skoku|Angle**: Wartością domyślną jest {{Value|45 °}}. Kąt zwężenia.


{{Properties_Title|parametr_ewolwenty}}

-    **kąt_natarcia|Angle**: Wartością domyślną jest {{Value|20 °}} *(patrz sekcja [Uwagi](#Uwagi.md))*.


{{Properties_Title|Precyzja}}

-    **numpoints|Integer**: Wartość domyślna to {{value|6}}. Zmiana profilu ewolwentowego. Zmiana wartości może prowadzić do nieoczekiwanych rezultatów.


{{Properties_Title|Tolerancja}}

-    **Luz międzyzębowy|Length**: Wartością domyślną jest {{Value|0}}. Luz zwrotny, zwany również luzem lub swobodnym biegiem, to odległość między zębami w parze kół zębatych.

-    **Prześwit|Float**: Wartością domyślną jest {{Value|0.1}}. *(patrz [Uwagi](#Uwagi.md))*.


{{Properties_Title|Wersja}}

-    **Wersja|String**:



## Uwagi

-    **prześwit**: W przypadku pary kół zębatych prześwit to odległość między wierzchołkiem zęba pierwszego koła zębatego a korzeniem zęba drugiego koła zębatego.

-    **moduł**: Korzystając z wytycznych ISO *(Międzynarodowej Organizacji Normalizacyjnej)*, rozmiar modułu jest określany jako jednostka reprezentująca rozmiary zębów kół zębatych. Moduł (m): m = 1 (p = 3,1416), m = 2 (p = 6,2832), m = 4 (p = 12,566). Jeśli pomnożymy moduł przez Pi, otrzymamy skok (p). Skok to odległość między odpowiednimi punktami na sąsiednich zębach.

-    **reset_origin**: Dla celów montażowych korzystne może być ustawienie tego parametru na wartość {{false/pl}}. Początek korpusu znajduje się wówczas na wierzchołku stożka podziałowego.

-    **pressure_parameter**: Parametr ten można zmienić tylko wtedy, gdy dostępna jest wystarczająca wiedza na temat geometrii koła zębatego.



## Przydatne wzory 

-    **średnica podziałowa**= **moduł** \* **zęby**

-    **średnica wierzchołkowa**= **średnica podziałowa** + 2 \* **moduł** \* **cos reference cone angle**

-    **tip angle 1**= **(teeth 1 + 2)** \* **(cos reference cone angle 1)** : **(teeth 2 - 2)** \* **(sin reference cone angle 1)**

-    **tip angle 2**= **(teeth 2 + 2)** \* **(cos reference cone angle 2)** : **(teeth 1 - 2)** \* **(sin reference cone angle 2)**

-    **reference cone angle 1**= **(teeth 1)** : **(teeth 2)**

-    **reference cone angle 2**= **(teeth 2)** : **(teeth 1)**

-    **axis angle total**= **reference cone angle 1** + **reference cone angle 2**

Merytoryczny kąt stożka odniesienia \[TECH.\]



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear BevelGear/pl
