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

Narzędzie **Koło zębate stożkowe** tworzy podstawowe koło zębate stożkowe, obiekt bryłowy, który musi zostać przycięty do właściwego kształtu końcowego w kolejnych krokach.

Częściowo ze względu na generowany przez nie hałas, przekładnie stożkowe nie są używane tak często, jak inne rodzaje przekładni. Są one jednak nadal używane w niektórych sektorach, takich jak pakowanie żywności i żywności w puszkach, sprzęt do pielęgnacji trawników i ogrodów, maszyny takie jak wiertarki i młyny, systemy kompresji na rynku gazu i ropy oraz zawory sterujące przepływem.

Spiralne koła zębate stożkowe mają zakrzywione zęby, które zapewniają łagodniejsze zazębianie i większy kontakt między zębami w porównaniu z prostymi kołami zębatymi stożkowymi. Zmniejsza to wibracje i hałas. Mogą być używane przy dużych prędkościach i są zwykle stosowane w przekładniach motocyklowych i rowerowych.

![](images/Bevel-Gear_example.png ) 
*Od lewej do prawej: Przekładnia czołowa, przekładnia spiralna.*



## Użycie

1.  Przejdź do środowiska pracy <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **[<img src=images/FCGear_BevelGear.svg style="width:16px"> '''Koło zębate stożkowe'''** na pasku narzędzi.
    -   Wybierz z menu opcję **Gear → [<img src=images/FCGear_BevelGear.svg style="width:16px"> Koło zębate stożkowe**.
3.  Obiekt BevelGear zostanie utworzony zgodnie z domyślnymi ustawieniami.
4.  Zmień parametry zębatki na wymagane *(patrz [Właściwości](#Właściwości.md))*.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Koło zębate stożkowe wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Wysokość|Length**: Wartością domyślną jest {{Value|5}}. Wartość szerokości koła zębatego stożkowego, mierzona od koła podziałowego.

-    **moduł|Length**: Wartością domyślną jest {{Value|1}}. Moduł jest stosunkiem średnica podziałki koła zębatego podzielonej przez liczbę zębów (patrz [Uwagi](#Uwagi.md)).

-    **reset_origin|Bool**: Jeśli przyjmie wartość {{True/pl}} *(domyślnie)* punkt początkowy koła zębatego znajduje się w środku koła podziałowego *(na dole koła zębatego)*, *(patrz [Uwagi](#Uwagi.md))*.

    :   Jeśli wartość to {{False/pl}}, punkt początkowy koła zębatego znajduje się na wierzchołku stożka podziałowego.

-    **Zęby|Integer**: Wartością domyślną jest {{Value|15}}. Liczba zębów.


{{Properties_Title|Obliczone}}

-    **luz_kątowy|Angle**: *(tylko do odczytu)*.

-    **dw|Length**: *(tylko do odczytu)* Średnica podziałki roboczej.


{{Properties_Title|Śrubowy}}

-    **beta|Angle**: Wartością domyślną jest {{Value|0 °}}. Przy kącie linii śrubowej β tworzone jest stożkowe koło zębate - wartość dodatnia → kierunek obrotu w prawo, wartość ujemna → kierunek obrotu w lewo.


{{Properties_Title|Ewolwenta}}

-    **kąt_skoku|Angle**: Wartością domyślną jest {{Value|45 °}}. Kąt nachylenia stożka podziałowego.


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

-   Przekładnie stożkowe są dość skomplikowane, ponieważ ich właściwości zależą nie tylko od przełożenia, ale także od kąta między osiami przekładni. Domyślna przekładnia stożkowa jest zbudowana dla prostopadłych osi i przełożenia 1:1.

-    **Kąt skoku**: Kąt nachylenia stożka wynosi połowę kąta między osiami koła zębatego dla przełożenia 1:1, czyli 45° dla osi prostopadłych. Kąty nachylenia dla innych kombinacji przełożeń i kątów między osiami można określić geometrycznie w środowisku pracy [Szkicownik](Sketcher_Workbench/pl.md).

-    **prześwit**: W przypadku pary kół zębatych prześwit to odległość między wierzchołkiem zęba pierwszego koła zębatego a korzeniem zęba drugiego koła zębatego.

-    **moduł**: Korzystając z wytycznych ISO *(Międzynarodowej Organizacji Normalizacyjnej)*, rozmiar modułu jest określany jako jednostka reprezentująca rozmiary zębów kół zębatych. Moduł (m): m = 1 (p = 3,1416), m = 2 (p = 6,2832), m = 4 (p = 12,566). Jeśli pomnożymy moduł przez Pi, otrzymamy skok (p). Skok to odległość między odpowiednimi punktami na sąsiednich zębach.

-    **pressure_angle**: Parametr można zmienić tylko wtedy, gdy dostępna jest wystarczająca wiedza na temat geometrii przekładni.

-    **reset_origin**: Zaleca się ustawienie parametru na wartość **false**, aby początek koła zębatego znajdował się na wierzchołku stożka podziałowego. W ten sposób możemy rozszerzyć koło zębate stożkowe poza płaszczyznę koła podziałowego przy użyciu właściwości modułu.

-   Słabym punktem tego narzędzia jest to, że buduje geometrię od średnicy podziałowej w kierunku wierzchołka i ignoruje fakt, że istnieje również geometria w przeciwnym kierunku. Dlatego musimy określić przekrój koła zębatego na okręgu podziałowym należącym do naszego wybranego modułu, aby zdefiniować geometrię cięcia, a następnie użyć rozszerzonego *(skalowanego od wierzchołka)* koła zębatego stożkowego do cięcia. *(patrz*resetowanie początku*powyżej)*



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
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External%20Command%20Reference.md) > FCGear BevelGear/pl
