---
 GuiCommand:
   Name: FCGear TimingGear
   Name/pl: FCGear: Koło pasa zębatego
   MenuLocation: Gear , Koło pasa zębatego
   Workbenches: FCGear_Workbench/pl
   Shortcut: Brak
   Version: v0.16
   SeeAlso: 
---

# FCGear TimingGear/pl



## Opis

Celem kół zębatych rozrządu jest umożliwienie wałowi rozrządu i wału korbowego obracanie łańcucha rozrządu. Wał korbowy obraca się, aby poruszać tłokami w górę i w dół wewnątrz cylindrów. Wałek rozrządu obraca się, aby umożliwić otwieranie i zamykanie zaworów wlotowych i wylotowych w cylindrach. Te elementy są ważne dla prawidłowego sterowania rozrządem silnika.

Koła zębate są połączone z paskiem rozrządu lub łańcuchem rozrządu.

![](images/Timing-Gear_example.png ) 
*Powyżej: Koło pasa zębatego*



## Użycie

1.  Przejdź do środowiska pracy <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **[<img src=images/FCGear_TimingGear.svg style="width:16px"> '''Koło pasa zębatego'''** na pasku narzędzi.
    -   Wybierz z menu opcję **Gear → [<img src=images/FCGear_TimingGear.svg style="width:16px"> Koło pasa zębatego**.
3.  Zmień parametry zębatki na wymagane *(patrz [Właściwości](#Właściwości.md))*.



## Właściwości

Obiekt Koło pasa zębatego wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **wysokość|Length**: Domyślnie {{Value|5 mm}}. Wartością domyślną jest szerokości koła zębatego.

-    **zęby|Integer**: Wartością domyślną jest {{Value|15}}. Liczba zębów.

-    **typ|Enumeration**: Wartością domyślną jest {{Value|gt2}}. Typ koła zębatego - podziałka profilu dla pasków zębatych *(patrz [Uwagi](#Uwagi.md))*.


{{Properties_Title|Obliczone}}

-    **h|Length**: *(tylko do odczytu)* Promieniowa wysokość zębów.

-    **offset|Length**: *(tylko do odczytu)* Przesunięcie X punktu środkowego drugiego łuku.

-    **podziałka|Length**: *(tylko do odczytu)* Skok koła zębatego.

-    **r0|Length**: *(tylko do odczytu)* Promień pierwszego łuku.

-    **r1|Length**: *(tylko do odczytu)* Promień drugiego łuku.

-    **rs|Length**: *(tylko do odczytu)* Promień trzeciego łuku.

-    **u|Length**: *(tylko do odczytu)* Różnica promieniowa między skokiem \... średnicą a głowicą koła zębatego.


{{Properties_Title|Wersja}}

-    **Wersja|String**:



## Uwagi

-    **typ**: Podziałka pasów zębatych *(odległość od środka zęba do środka kolejnego zęba)* jest określona w typach. GT2 ma podziałkę 2 mm, GT3 - 3 mm, GT5 - 5 mm itd.



## Przydatne wzory 

-    **średnica wierzchołkowa**= **średnica podziałowa** + 2 \* **moduł**

-    **długość pasa**= 2 \* **rozstaw osi** + **podziałka zębów pasa** : 2 \* **(zęby 1 + 2)** + **podziałka zębów pasa²** : 4 \* pi² \* **rozstaw osi** \* **(zęby 1 - 2)²**

-    **rozstaw osi**= **długość pasa** : 4 - **podziałka zębów pasa** : 8 \* **(zęby 1+2)** + ¼ \* pierwiastek kwadratowy \[**długość pasa** - ½ \* **podziałka zębów pasa** \* **(zęby 1+2)²** - 2 \* **podziałka zębów pasa²** \* **(zęby 1+2)²** : pi²\]



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External%20Command%20Reference.md) > FCGear TimingGear/pl
