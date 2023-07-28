---
- GuiCommand:/pl
   Name:FCGear InternalInvoluteGear
   Name/pl:FCGear: Wewnętrzna zębatka ewolwentowa
   MenuLocation:Gear → Wewnętrzna zębatka ewolwentowa
   Workbenches:[FCGear](FCGear_Workbench/pl.md)
   Version:0.21
   SeeAlso:[Koło zębate ewolwentowe](FCGear_InvoluteGear/pl.md)
---

# FCGear InternalInvoluteGear/pl



## Opis

<img alt="" src=images/FCGear_InternalInvoluteGear-01.png  style="width:300px;">



*Wewnętrzne przekładnie ewolwentowe od lewej do prawej: Przekładnia czołowa, przekładnia walcowa, podwójna przekładnia walcowa.*



## Użycie

1.  Przejdź do środowiska pracy <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **[<img src=images/FCGear_InternalInvoluteGear.svg style="width:16px"> '''Wewnętrzna zębatka ewolwentowa'''** na pasku narzędzi.
    -   Wybierz z menu opcję **Gear → [<img src=images/FCGear_InvoluteGear.svg style="width:16px"> Wewnętrzna zębatka ewolwentowa**.
3.  Zmień parametry zębatki na wymagane *(patrz [Właściwości](#Właściwości.md))*.



## Właściwości

Obiekt InternalInvoluteGear wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Dokładność}}

-    **numpoints|Integer**: Wartość domyślna to {{value|6}}. Zmiana profilu ewolwentowego. Zmiana wartości może prowadzić do nieoczekiwanych rezultatów.


{{Properties_Title|Podstawowe}}

-    **wysokość|Length**: Domyślnie {{value|5 mm}}. Wartość szerokości koła zębatego.

-    **moduł|Length**: Domyślnie {{value|1 mm}}. Moduł jest stosunkiem średnicy referencyjnej koła zębatego podzielonej przez liczbę zębów *(patrz [Uwagi](FCGear_InvoluteGear/pl#Uwagi.md))*.

-    **zęby|Integer**: Domyślnie {{value|15}}. Liczba zębów *(patrz [Uwagi](FCGear_InvoluteGear/pl#Uwagi.md))*.

-    **grubość|Length**: Domyślnie {{value|5 mm}}. Grubość nieobciętej zewnętrznej części koła zębatego.


{{Properties_Title|Obliczone}}

-    **angular_backlash|Angle**: *(tylko do odczytu)*.

-    **da|Length**: *(tylko do odczytu)* Średnica wewnętrzna, mierzona na wierzchołku zęba *(końcówki zębów)*.

-    **df|Length**: *(tylko do odczytu)* Średnica korzenia, mierzona u podstawy zębów.

-    **dw|Length**: *(tylko do odczytu)* Średnica podziałki roboczej.

-    **outside_diameter|Length**: *(tylko do odczytu)* Średnica zewnętrzna.

-    **transverse_pitch|Length**: *(tylko do odczytu)* Podziałka w płaszczyźnie obrotu.


{{Properties_Title|Zaokrąglenia}}

-    **head_fillet|Float**: Domyślnie {{value|0 mm}}.

-    **root_fillet|Float**: Domyślnie {{value|0 mm}}.


{{Properties_Title|Śrubowy}}

-    **beta|Angle**: Domyślnie {{value|0 °}}. Z kątem helisy β tworzone jest koło zębate śrubowe - wartość dodatnia → kierunek obrotu w prawo, wartość ujemna → kierunek obrotu w lewo *(patrz [Uwagi](FCGear_InvoluteGear/pl#Uwagi.md))*.

-    **double_helix|Bool**: Domyślną wartością jest {{False/pl}}, wartość {{True/pl}} pozwala utworzyć podwójną helisę *(patrz [Uwagi](FCGear_InvoluteGear/pl#Uwagi.md))*.

-    **properties_from_tool|Bool**: Domyślną wartością jest {{False/pl}}. Jeśli parametr przyjmie wartość {{True/pl}} i **beta** nie jest równy zero, parametry koła zębatego są ponownie obliczane wewnętrznie dla obróconego koła zębatego.


{{Properties_Title|Ewolwenta}}

-    **kąt_natarcia|Angle**: Domyślnie {{Value|20 °}} *(patrz [Uwagi](FCGear_InvoluteGear/pl#Uwagi.md))*.

-    **przesunięcie|Float**: Domyślnie {{Value|0}}. Generuje dodatnie i ujemne przesunięcie profilu *(patrz [Uwagi](FCGear_InvoluteGear/pl#Uwagi.md))*.


{{Properties_Title|Precyzja}}

-    **simple|Bool**: Domyślną wartością jest {{false/pl}}, wartość {{true/pl}} generuje uproszczony obraz *(bez zębów i tylko cylinder o średnicy podziałowej)*.


{{Properties_Title|Tolerancja}}

-    **backlash|Length**: Domyślnie {{Value|0}}. Luz zwrotny, zwany również lagiem lub swobodnym biegiem, to odległość między zębami w parze kół zębatych.

-    **prześwit|Float**: Domyślnie {{Value|0.25}}. *(patrz [Uwagi](FCGear_InvoluteGear/pl#Uwagi.md))*.

-    **head|Float**: Domyślnie {{Value|0}}. Wartość ta jest używana do zmiany wysokości zęba.

-    **reversed_backlash|Bool**: Wartość {{True/pl}} zmniejsza luz lub {{False/pl}} *(domyślnie)* i właściwość backslash zwiększa luz *(patrz [Uwagi](FCGear_InvoluteGear/pl#Uwagi.md))*.


{{Properties_Title|Wersja}}

-    **Wersja|String**:



## Uwagi

Zobacz stronę [Koło zębate ewolwentowe](FCGear_InvoluteGear/pl#Uwagi.md).



## Przydatne wzory 

Zobacz stronę [Koło zębate ewolwentowe](FCGear_InvoluteGear/pl#Przydatne_wzory.md).



## Tworzenie skryptów



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear InternalInvoluteGear/pl
