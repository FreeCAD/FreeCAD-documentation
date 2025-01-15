---
 GuiCommand:
   Name: FCGear CycloidGear
   Name/pl: FCGear: Koło zębate cykloidalne
   MenuLocation: Gear , Koło zębate cykloidalne
   Workbenches: FCGear_Workbench/pl
   Shortcut: Brak
   Version: v0.16
   SeeAlso: FCGear_InvoluteGear/pl
---

# FCGear CycloidGear/pl



## Opis

Przekładnie cykloidalne są bardzo wrażliwe na niedokładną regulację odległości między osiami, co prowadzi do zmiany przełożenia. Z tych powodów przekładnie cykloidalne są rzadko spotykane w inżynierii mechanicznej, ale są stosowane tylko w specjalnych przypadkach, takich jak przemysł zegarmistrzowski, do dmuchaw typu root lub do napędu zębatek.

![](images/Cycloid-Gear_example_1.png ) 
*Od lewej do prawej: Przekładnia czołowa, przekładnia walcowa, podwójna przekładnia walcowa*



## Użycie

1.  Przejdź do środowiska pracy <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk na pasku narzędzi **[<img src=images/FCGear_CycloidGear.svg style="width:16px"> '''Koło zębate cykloidalne'''**.
    -   Wybierz z menu opcję **Gear → [<img src=images/FCGear_HypoCycloidGear.svg style="width:16px"> Koło zębate cykloidalne**.
3.  Zmień parametry zębatki na wymagane *(patrz [Właściwości](#Właściwości.md))*.



## Właściwości



### Dane

Obiekt **Koło zębate cykloidalne** wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:


{{Properties_Title|Dokładność}}

-    **numpoints|Integer**: Wartość domyślna to {{value|15}}. Zmiana profilu ewolwentowego. Zmiana wartości może prowadzić do nieoczekiwanych rezultatów.


{{Properties_Title|Podstawowe}}

-    **wysokość|Length**: Wartością domyślną jest {{Value|5 mm}}. Wartość szerokości koła zębatego.

-    **moduł|Length**: Domyślnie {{Value|1 mm}}. Moduł jest stosunkiem średnicy referencyjnej koła zębatego podzielonej przez liczbę zębów *(patrz [Uwagi](#Uwagi.md))*.

-    **zęby|Integer**: Domyślną wartością jest {{Value|15}}. Liczba zębów.


{{Properties_Title|Obliczone}}

-    **luz_kątowy|Angle**: *(tylko do odczytu)*.

-    **dw|Length**: *(tylko do odczytu)* Średnica podziałki roboczej.


{{Properties_Title|cykloidalna}}

-    **Średnica_wewnętrzna|Float**: *(tylko do odczytu)* Średnica toczącego się okręgu hipocykloidy, znormalizowana przez **moduł**. (patrz [Uwagi](#Uwagi.md)).

-    **Średnica_zewnętrzna|Float**: Domyślnie {{Value|7.5}}. Średnica toczącego się okręgu epicykloidy, znormalizowana przez **moduł**. (patrz [Uwagi](#Uwagi.md)).


{{Properties_Title|Zaokrąglenie}}

-    **head_fillet|Float**: Wartość domyślna to {{value|0 mm}}.

-    **root_fillet|Float**: Wartość domyślna to {{value|0 mm}}.


{{Properties_Title|Śrubowy}}

-    **beta|Angle**: Domyślnie {{Value|0 °}}. Z kątem helisy β tworzone jest koło zębate śrubowe - wartość dodatnia → kierunek obrotu w prawo, wartość ujemna → kierunek obrotu w lewo.

-    **Podwójna_helisa|Bool**: Domyślną wartością jest {{False/pl}}, {{True/pl}} tworzy podwójną helisę *(patrz [Uwagi](#Uwagi.md))*.


{{Properties_Title|Tolerancja}}

-    **luz|Length**: Domyślną wartością jest {{Value|0}}. Luz zwrotny, zwany również luzem lub luzem, to odległość między zębami w parze kół zębatych.

-    **Prześwit|Float**: Domyślną wartością jest {{Value|0.25}} *(patrz [Uwagi](#Uwagi.md))*.

-    **head|Float**: Domyślną wartością jest {{Value|0}}. Dodatkowa długość wierzchołka zębów, znormalizowana przez **moduł**.


{{Properties_Title|Wersja}}

-    **Wersja|String**:



## Uwagi

-   Cykloidalne koła zębate muszą być zawsze specjalnie dopasowane do siebie i generalnie nie mogą być dowolnie zamieniane: W parze kół zębatych, wartość parametru **średnica_wewnętrzna** na jednym kole zębatym musi być równa wartości parametru **średnica_zewnętrzna** na drugim kole zębatym i vice versa. Zobacz także informacje w **Właściwości widoku parametrów cykloidy** poniżej.

-    **Prześwit**: W przypadku pary kół zębatych luz to odległość między wierzchołkiem zęba pierwszego koła zębatego a korzeniem zęba drugiego koła zębatego.

-    **Podwójna_helisa**: Aby użyć podwójnej przekładni śrubowej, należy najpierw wprowadzić kąt pochylenia linii śrubowej β (**beta**) dla przekładni śrubowej.

-    **moduł**: Korzystając z wytycznych ISO (Międzynarodowej Organizacji Normalizacyjnej), rozmiar modułu jest określany jako jednostka reprezentująca rozmiary zębów przekładni. Moduł (m): m = 1 (p = 3,1416), m = 2 (p = 6,2832), m = 4 (p = 12,566). Jeśli pomnożymy moduł przez Pi, otrzymamy Pitch (p). Pitch to odległość między odpowiednimi punktami na sąsiednich zębach.



## Przypadki specjalne 



### Linia prosta jako hipocykloida 

Aby uzyskać linię prostą, bezpośrednio w kierunku środka, jako hipocykloidę, użyj następującego [wyrażenia](Expressions/pl.md) dla **średnicy_wewnętrznej**: `teeth / 2`. Taki kształt zębów jest często spotykany w historycznych zegarach i dlatego nazywany jest \"uzębieniem zegara\". Większe **Prześwit** sprawia, że efekt ten jest jeszcze bardziej widoczny.



### Pełna hipocykloida/epicykloida jako ząb 

Aby uzyskać koło zębate zbudowane z kompletnych krzywych hipocykloidalnych i epicykloidalnych, należy użyć następujących [wyrażenia](Expressions/pl.md):

-    **średnica_wewnętrzna**: `0.5 + 1e-6`

-    **średnica_zewnętrzna**: `średnica_wewnętrzna`

-    **Prześwit**: `(-1 + średnica_wewnętrzna/1mm) * 2`

-    **head**: `(-1 + średnica_zewnętrzna/1mm) * 2`

Średnica referencyjna to *d = m \* z*, gdzie *m* to **moduł**, a *z* to **zęby**. Dla pełnej hipocykloidy średnica toczenia musi wynosić *d_i = d / (z\*2) = m\*z / (z\*2)*. A jeśli teraz znormalizujemy to przez moduł, otrzymamy *d_in = m\*z / (z\*2) / m = 1 / 2*. Dodatkowa jawna wartość tolerancji (`1e-6` w powyższym wyrażeniu) jest wymagana do przezwyciężenia problemów z koincydencją.

Teraz średnica koła tocznego cykloidy musi odpowiadać addum/dedendum koła zębatego. Dodatek, tj. długość zęba powyżej koła odniesienia, wynosi 1 + **head**. Dedendum, tj. długość zęba poniżej okręgu odniesienia, wynosi 1 + **prześwit**. Oba są znormalizowane przez moduł, dlatego potrzebujemy wartości head / prześwit równej *1 - d_in*. Dodatkowe ` / 1mm` i ` * 2` są wymagane do przezwyciężenia niedociągnięć już naprawionych w wersji rozwojowej środowiska pracy FCGear, ale przeniesienie tych poprawek z powrotem do wersji stabilnej może zepsuć istniejące modele.

Takie \"koła zębate\" pozwalają na zmniejszenie liczby zębów do \"dwóch\" i są używane jako obrotowe łopatki w pompach lub sprężarkach *(por. [Roots-type Supercharger](https://en.wikipedia.org/wiki/Roots-type_supercharger))*.



### Nieskończenie duża epicykloida 

Jeśli promień toczącego się okręgu epicykloidy staje się nieskończenie duży, staje się ona toczącą się linią prostą. Taka zdegenerowana epicykloida nazywana jest ewolwentą. Koła zębate o takim kształcie zębów są obsługiwane przez narzędzie [Koło zębate ewolwentowe](FCGear_InvoluteGear/pl.md). Jest to obecnie najczęściej spotykany kształt zęba.



## Przydatne wzory 

Zobacz stronę [Koło zębate ewolwentowe](FCGear_InvoluteGear/pl#Przydatne_wzory.md).



## Widok właściwości parametrów cykloidy 

<img alt="" src=images/CycloidGear_inner-outer-diameter_2.svg  style="width:400px;">



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External%20Command%20Reference.md) > FCGear CycloidGear/pl
