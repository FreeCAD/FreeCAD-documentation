---
- GuiCommand:/pl
   Name:PartDesign InvoluteGear
   Name/pl:Projekt Części: Koło zębate ewolwentowe
   MenuLocation:Projekt części → Involute gear...
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   SeeAlso:[FCGear](FCGear_Workbench.md)
---

# PartDesign InvoluteGear/pl

## Opis

Narzędzie to pozwala na utworzenie dwuwymiarowego profilu koła zębatego. Ten profil 2D jest w pełni parametryczny i może być wyciągnięty funkcją [Wyciągnięcie](PartDesign_Pad/pl.md) lub [Addytywna helisa](PartDesign_AdditiveHelix/pl.md).

Bardziej szczegółowe informacje można znaleźć również na stronach Wiki: [przekładnie](https://en.wikipedia.org/wiki/Gear) oraz [Zarys ewolwentowy](https://en.wikipedia.org/wiki/Involute_gear)

![](images/PartDesign_Involute_Gear_01.png )

## Użycie

### Utworzenie profilu 

1.  Opcjonalnie aktywuj właściwą zawartość.
2.  Przejdź do menu **Projekt Części → [<img src=images/PartDesign_InternalExternalGear.svg style="width:24px"> Przekładnia ewolwentowa ...**.
3.  Ustaw parametry zębatki.
4.  Kliknij **OK**.
5.  Jeśli koło zębate znajduje się poza aktywną zawartością: przeciągnij go i upuść do zawartości, aby zastosować dalsze funkcje, takie jak wyciągnięcie.

### Utworzenie koła zębatego czołowego 

1.  Wybierz profil koła zębatego w widoku drzewa.
2.  Naciśnij przycisk **<img src="images/PartDesign_Pad.svg" width=24px> Wyciągnij**.
3.  Ustaw **Długość** wyciągnięcia na żądaną szerokość powierzchni czołowej koła zębatego.
4.  Kliknij na przycisk **OK**.

### Utworzenie koła zębatego walcowego 


{{Version/pl|0.19}}

1.  Wybierz profil koła zębatego w widoku drzewia.
2.  Naciśnij przycisk **<img src="images/PartDesign_AdditiveHelix.svg" width=24px> [Addytywna helisa](PartDesign_AdditiveHelix/pl.md)**.
3.  Wybierz jako oś, wektor normalny profilu koła zębatego, czyli **Oś normalna szkicu** {{Version/pl|0.20}} *(We wcześniejszych wersjach można użyć **Bazowa oś Z**, o ile płaszczyzna profilu nie została zmieniona)*.
4.  Wybierz tryb **Wysokość - Obrót**.
5.  Ustaw **Wysokość** na żądaną szerokość czołową koła zębatego.
6.  Aby ustawić żądany kąt skrętu należy użyć [Wyrażenia](Expressions/pl.md) dla **Obrotów**.
    1.  Kliknij niebieską ikonę <img alt="" src=images/Bound-expression.svg  style="width:24px;"> po prawej stronie pola wprowadzania danych.
    2.  Wprowadź następującą formułę: `Height * tan(25°) / (InvoluteGear.NumberOfTeeth * InvoluteGear.Modules * pi)`, gdzie `25°` jest przykładem pożądanego kąta spiralnego *(znanego również jako wartość beta)*, a `InvoluteGear` jest **Nazwą** profilu.
    3.  Kliknij w przycisk **OK**, aby zamknąć edytor formuły.
7.  Kliknij w przycisk **OK**, aby zamknąć panel zadań.

Wskazówka: Aby uczynić kąt skrętu dostępnym parametrem, użyj \"właściwości dynamicznej\":

1.  Wybierz profil.
2.  W oknie [Edytora właściwości](Property_editor/pl.md) aktywuj opcję **Wyświetl wszystko** w menu kontekstowym.
3.  Ponownie w menu kontekstowym wybierz opcję **Dodaj właściwość**. Uwaga: ta pozycja jest dostępna tylko wtedy, gdy aktywna jest opcja **Wyświetl wszystko**.
4.  W oknie dialogowym **Dodaj właściwość**:
    1.  Wybierz `App::PropertyAngle` jako Typ.
    2.  Ustaw wartość `Gear` w polu Grupa,
    3.  Ustaw wartość `HelicalAngle` jako nazwę *(bez spacji)*,
    4.  Kliknij **OK**.
5.  Teraz pojawi się nowa właściwość **Helical Angle** *(spacja dodana automatycznie)*, z wartością początkową `0.0°`, staje się dostępna.
6.  Przypisz do nowej właściwości żądany kąt spiralny.
7.  W formule właściwości **Obrót** profilu AdditiveHelix można teraz odwołać się do `InvoluteGear.HelicalAngle` zamiast zakodowanej wartości np. `25°`; ponownie zakładając, że `InvoluteGear` jest właściwością **Nazwy** profilu.

## Właściwości

-    **Zarys zewnętrzny**: przyjmuje wartość {{True/pl}} lub {{False/pl}}

-    **Wysoka dokładność**: przyjmuje wartość {{True/pl}} lub {{False/pl}}

-    **Modułowość**: średnica podziałki podzielona przez liczbę zębów.

-    **Liczba zębów**: ustawia liczbę zębów.

-    **Kąt przyporu**: kąt ostry między linią działania a normalną do linii łączącej środki kół zębatych. Domyślnie jest to 20°

([Więcej informacji](https://en.wikipedia.org/wiki/Involute_gear)).

## Poradniki

[Jak zrobić przekładnie zębate w FreeCAD](https://www.youtube.com/watch?v=8VNhTrnFMfE)

## Powiązane

-   [Środowisko pracy FCGear](FCGear_Workbench.md)





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign InvoluteGear/pl
