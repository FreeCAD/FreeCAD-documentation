---
 GuiCommand:
   Name: FCGear CycloidRack
   Name/pl: FCGear: Listwa zębata cykloidalna
   MenuLocation: Gear , Listwa zębata cykloidalna
   Workbenches: FCGear_Workbench/pl
   Shortcut: None
   Version: 0.22
   SeeAlso: FCGear_CycloidGear/pl
---

# FCGear CycloidRack/pl



## Opis

<img alt="" src=images/FCGear_CycloidRack-01.png  style="width:200px;">



*Przekładnie cykloidalne od lewej do prawej: Przekładnia czołowa, przekładnia walcowa, podwójna przekładnia walcowa.*



## Użycie

1.  Przejdź do środowiska pracy <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk na pasku narzędzi **[<img src=images/FCGear_CycloidRack.svg style="width:16px"> '''Listwa zębata cykloidalna'''**.
    -   Wybierz z menu opcję **Gear → [<img src=images/FCGear_CycloidRack.svg style="width:16px"> Listwa zębata cykloidalna**.
3.  Zmień parametry zębatki na wymagane *(patrz [Właściwości](#Właściwości.md))*.



## Właściwości

Obiekt **Listwa zębata cykloidalna** wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:


{{Properties_Title|Dokładność}}

-    **numpoints|Integer**: Wartością domyślną jest {{value|15}}. Liczba punktów dla splajnu.


{{Properties_Title|Podstawowe}}

-    **Dodaj_zakończenia|bool**: Jeśli wartość to {{True}} (domyślnie), całkowita długość zębatki to zęby \* podziałka. Jeśli jest to {{False}}, wówczas zębatka zaczyna się od boku zęba.

-    **Wysokość|Length**: Wartością domyślną jest {{value|5 mm}}. Wartość szerokości koła zębatego.

-    **Zęby|Integer**: Wartość domyślna to {{value|15}}. Liczba zębów.

-    **Grubość|Length**: Domyślnie {{value|5 mm}}. Grubość nieobciętej części zębatki.


{{Properties_Title|Obliczone}}

-    **Rozstaw_poprzeczny|Length**: *(tylko do odczytu)* Skok w płaszczyźnie poprzecznej.


{{Properties_Title|cykloidalna}}

-    **Średnica_wewnętrzna|Float**: Wartością domyślną jest {{value|7.5}}. Średnica toczącego się okręgu hipocykloidy, znormalizowana przez **moduł** *(patrz [Uwagi](FCGear_CycloidGear#.md))*.

-    **Średnica_zewnętrzna|Float**: Wartością domyślną jest {{value|7.5}}. Średnica toczącego się okręgu epicykloidy, znormalizowana przez **moduł** *(patrz [Uwagi](FCGear_CycloidGear#.md))*.


{{Properties_Title|Zaokrąglenie}}

-    **head_fillet|Float**: Wartość domyślna to {{value|0 mm}}.

-    **root_fillet|Float**: Wartość domyślna to {{value|0 mm}}.


{{Properties_Title|Śrubowy}}

-    **beta|Angle**: Domyślną wartością jest {{Value|0 °}}. ZKąt pochylenia linii śrubowej β tworzy przekładnię śrubową *(wartość dodatnia → kierunek obrotów w prawo, wartość ujemna → kierunek obrotów w lewo)*.

-    **Podwójna_helisa|Bool**: Domyślną wartością jest {{False/pl}}, {{True/pl}} tworzy podwójną helisę *(patrz [Uwagi](FCGear_CycloidGear/pl#Uwagi.md))*.


{{Properties_Title|Ewolwenta}}

-    **moduł|Length**: Wartością domyślną jest {{value|1 mm}}. W przypadku listew moduł jest równy podziałce, podobnie jak odległość między odpowiednimi punktami na sąsiednich zębach *(patrz [Uwagi](FCGear_CycloidGear/pl#Uwagi.md))*.


{{Properties_Title|Precyzja}}

-    **uproszczony|Bool**: Wartością domyślną jest {{false/pl}}. Jeśli wybrano {{true/pl}}, zębatka jest rysowana ze stałą liczbą zębów, aby uniknąć topologicznej zmiany nazwy.


{{Properties_Title|Tolerancja}}

-    **Prześwit|Float**: Domyślną wartością jest {{Value|0.25}} *(patrz [Uwagi](FCGear_CycloidGear/pl#Uwagi.md))*.

-    **head|Float**: Domyślną wartością jest {{Value|0}}. Dodatkowa długość wierzchołka zębów, znormalizowana przez **moduł**.


{{Properties_Title|Wersja}}

-    **Wersja|String**:



## Uwagi

Zobacz stronę [Koło zębate cykloidalne](FCGear_CycloidGear/pl#Uwagi.md).



## Przydatne wzory 

Zobacz stronę [Koło zębate cykloidalne](FCGear_CycloidGear/pl#Przydatne_wzory.md).



## Tworzenie skryptów



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear CycloidRack/pl
