---
 GuiCommand:
   Name: FCGear CrownGear
   Name/pl: FCGear: Koło zębate koronowe
   MenuLocation: Gear , Koło zębate koronowe
   Workbenches: FCGear_Workbench/pl
   Shortcut: Brak
   Version: v0.16
   SeeAlso: FCGear_InvoluteGear/pl
---

# FCGear CrownGear/pl



## Opis

Koło koronowe przypomina zakrzywiony pierścień. Kąt nacisku zmniejsza się w sposób ciągły od średnicy zewnętrznej do wewnętrznej. W ten sposób zmienna prędkość obwodowa koła koronowego jest kompensowana stałą prędkością obwodową zębnika. Spiczaste zęby zewnętrzne i strome boki zębów na średnicy wewnętrznej ograniczają użyteczną szerokość zębów. Przekładnie koronowe osiągają podobną sprawność jak przekładnie czołowe. Jedno koło koronowe może napędzać kilka zębników.

Znany zakres zastosowań przekładni koronowych:

-   Napędy tylnej osi samochodów i motocykli.
-   Mechanizm obrotowy do stołów operacyjnych.
-   Głowice frezarskie kątowe.
-   Napędzane systemy narzędziowe z wieloma zębnikami i przekładnią koronową.

![](images/Crown-Gear_example.png ) 
*Powyżej: Przekładnia koronowa.*



## Użycie

1.  Przełącz się na środowisko pracy <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk na pasku narzędzi **[<img src=images/FCGear_CrownGear.svg style="width:16px"> [Koło zębate koronowe](FCGear_CrownGear/pl.md)**.
    -   Wybierz opcję z menu **Gear → [<img src=images/FCGear_CrownGear.svg style="width:16px"> Koło zębate koronowe**.
3.  Przekładnia koronowa jest domyślnie wyświetlana bez zębów. ({{Version/pl|0.21}})
4.  Zmień parametry koła zębatego na wymagane *(zobacz akapit [Właściwości](#Właściwości.md))*.
5.  Ustaw wartość właściwości **Tryb_podglądu** na {{false/pl}}, aby wyświetlić zęby *(patrz [Uwagi](#Uwagi.md))*.



## Właściwości

Obiekt Koło zębate koronowe wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Dokładność}}

-    **Ilość_profili|Integer**: Wartością domyślną jest {{Value|4}}. Liczba profili używanych dla wyciągnięcia przez profile.

-    **Tryb_podglądu|Bool**: Wartością domyślną jest {{True/pl}}.


{{Properties_Title|Podstawowe}}

-    **Wysokość|Length**: Wartością domyślną jest {{Value|2 mm}}. Wartość dla szerokości zęba.

-    **Moduł|Length**: Wartością domyślną jest {{Value|1 mm}}. Moduł jest stosunkiem średnicy referencyjnej koła zębatego podzielonej przez liczbę zębów (patrz [Uwagi](#Uwagi.md)).

-    **other_teeth|Integer**: Wartością domyślną jest {{Value|15}}. Liczba zębów przekładni konstrukcyjnej *(zębnika)* *(patrz [Uwagi](#Uwagi.md))*.

-    **zęby|Integer**: Wartością domyślną jest {{Value|15}}. Liczba zębów.

-    **grubość|Length**: Wartością domyślną jest {{Value|5 mm}}. Wysokość od wierzchołka zęba do dolnej części koła koronowego.


{{Properties_Title|Ewolwenta}}

-    **kąt_natarcia|Angle**: Wartością domyślną jest {{Value|20 °}} *(patrz sekcja [Uwagi](#Uwagi.md))*.


{{Properties_Title|Wersja}}

-    **Wersja|String**:



## Uwagi

-   Właściwość **tryb_podglądu** jest domyślnie ustawiona na {{true/pl}}, a po utworzeniu koła zębatego w widoku raportu pojawi się ten komunikat:

    :   *Środowisko pracy Gear: Utworzono koło zębate koronowe, tryb podglądu = {{true/pl}} dla lepszej wydajności. Ustaw właściwość tryb podglądu na false, gdy będziesz gotowy do wycięcia zębów.*

-    **moduł**: Korzystając z wytycznych ISO *(Międzynarodowej Organizacji Normalizacyjnej)*, rozmiar modułu jest określany jako jednostka reprezentująca rozmiary zębów koła zębatego. Moduł (m): m = 1 (p = 3,1416), m = 2 (p = 6,2832), m = 4 (p = 12,566). Jeśli pomnożymy moduł przez Pi, otrzymamy Skok (p). Pitch to odległość między odpowiednimi punktami na sąsiednich zębach.

-    **inne_zęby**: Na jednym kole koronowym można użyć kilku zębników o tej samej liczbie zębów.

-    **pressure_parameter**: Parametr można zmienić tylko wtedy, gdy dostępna jest wystarczająca wiedza na temat geometrii koła zębatego.

-   Geometria koła koronowego jest przede wszystkim określona przez geometrię zębnika czołowego (**inne_zęby**).

-   Utwórz koło zębate czołowe za pomocą narzędzia [Koło zębate ewolwentowe](FCGear_InvoluteGear/pl.md). Liczba zębów musi być identyczna z parametrem **inne_zęby** koła koronowego.

-   Dostosowania optymalnej charakterystyki pracy można dokonać za pomocą parametrów przekładni ewolwentowej.



## Przegląd zestawu kół zębatych koronowych i czołowych 

![](images/Crown-spur-gear-set_example.png )

-   \(1\) Koło zębate czołowe.
-   \(2\) Koło koronowe.
-   \(3\) Szerokość zębów.
-   \(4\) Średnica wewnętrzna.
-   \(5\) Średnica zewnętrzna.



## Przydatne wzory 

-   **Średnica wewnętrzna (4)**
    -   
        **inner diamter**
        
        = **moduł (przekładnia czołowa)**. \* **zęby (przekładnia koronowa)** \* **cos pressure_parameter (pinion)** : **cos pressure_parameter (przekładnia koronowa)**

-   **Średnica zewnętrzna (5)**
    -   
        **średnica zewnętrzna**
        
        = **średnica wewnętrzna** + **2x wysokość (szerokość zęba koła koronowego)**.



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear CrownGear/pl
