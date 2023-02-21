---
- GuiCommand:/pl
   Name:PartDesign InvoluteGear
   Name/pl:Projekt Części: Koło zębate ewolwentowe
   Icon:PartDesign_InternalExternalGear.svg
   MenuLocation:Projekt części → Koło zębate ewolwentowe ...
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   SeeAlso:[FCGear](FCGear_Workbench/pl.md)
---

# PartDesign InvoluteGear/pl



## Opis

Narzędzie to pozwala na utworzenie dwuwymiarowego profilu koła zębatego lub krzywej złożonej. Ten profil 2D jest w pełni parametryczny i może być wyciągnięty funkcją [Wyciągnięcie](PartDesign_Pad/pl.md) lub [Addytywna helisa](PartDesign_AdditiveHelix/pl.md).

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

1.  Wybierz profil koła zębatego w [widoku drzewa](Tree_view/pl.md).
2.  Naciśnij przycisk **<img src="images/PartDesign_Pad.svg" width=24px> [Wyciągnij](PartDesign_Pad/pl.md)**.
3.  Ustaw **Długość** wyciągnięcia na żądaną szerokość powierzchni czołowej koła zębatego.
4.  Kliknij na przycisk **OK**.



### Utworzenie koła zębatego walcowego 


{{Version/pl|0.19}}

1.  Wybierz profil koła zębatego w [widoku drzewa](Tree_view/pl.md).
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



### Wycięcie piasty dla wału wielowypustowego ewolwentowego 


{{Version/pl|1.0}}

1.  Activate the correct body.
2.  Create an internal involute gear profile with the required number of grooves and adapt the values of pressure angle, addendum-, dedendum- and root fillet coefficient. See also the table in [Notes](#Notes.md) below for feasible values. For example:
    -   
        **External Gear**
        
        : False

    -   
        **Number Of Teeth**
        
        : 12

    -   
        **Pressure Angle**
        
        : 37.5°

    -   
        **Addendum Coefficient**
        
        : 0.45

    -   
        **Dedendum Coefficient**
        
        : 0.7

    -   
        **Root Fillet Coefficient**
        
        : 0.3
3.  Select the gear profile in the [Tree view](Tree_view.md).
4.  Press the **<img src="images/PartDesign_Pocket.svg" width=16px> '''Pocket'''** button.
5.  Set the pocket\'s **Type** to **Through All**.
6.  Check the pocket\'s **Symmetric To Plane** option.
7.  Click **OK**.



## Właściwości

-    **Zarys zewnętrzny**: przyjmuje wartość {{True/pl}} lub {{False/pl}}

-    **Wysoka dokładność**: przyjmuje wartość {{True/pl}} lub {{False/pl}}

-    **Modułowość**: średnica podziałki podzielona przez liczbę zębów.

-    **Liczba zębów**: ustawia liczbę zębów.

-    **Kąt przyporu**: kąt ostry między linią działania a normalną do linii łączącej środki kół zębatych. Domyślnie jest to 20°

. Zobacz stronę [koło zębate ewolwentowe](https://en.wikipedia.org/wiki/Involute_gear) aby uzyskać więcej informacji.

-    **Addendum Coefficient**: The height of the tooth from the pitch circle up to its tip, normalized by the module. Default is 1.0 for the standard full-depth system. <small>(v1.0)</small> 

-    **Dedendum Coefficient**: The height of the tooth from the pitch circle down to its root, normalized by the module. Default is 1.25 for the standard full-depth system. <small>(v1.0)</small> 

-    **Root Fillet Coefficient**: The radius of the fillet at the root of the tooth, normalized by the module. Default is 0.38 as defined by the ISO rack. <small>(v1.0)</small> 

## Notes

-   In order for two gears to mesh they need to share the same module and pressure angle. [Expressions](Expressions.md) may help to ensure consistency. Their center distance needs to be `(NumberOfTeeth + OtherGear.NumberOfTeeth) * Modules / 2` (subtract the number of teeth in case of an internal gear).

-   When visually checking for proper meshing or interferences a much lower value for **Deviation** is helpful, e.g. 0.05 instead of the default 0.5. Otherwise the representation in the [3D view](3D_view.md) may be too coarse.

-   For standard gears the most common pressure angle is 20 °, followed by 14,5 °. Other applications, notably [splines](https://en.wikipedia.org/wiki/Spline_(mechanical)), use higher angles.

-   The standard full-depth system uses an addendum coefficient of 1.0 and a dedendum coefficient of 1.25, resulting in a clearance of 0.25 (the difference between the addendum of the one gear and the dedendum of the other). The actual tooth length is the sum of both coefficients, multiplied by the module.

-   Tooth length reduction may be required to prevent undercut or to strengthen the teeth (see [stub teeth](https://khkgears.net/new/gear_knowledge/gear-nomenclature/stub-teeth.html)). For internal gears the addendum (here pointing inwards) may need shortening to avoid certain interferences or non-involute flanks; when indicated in combination with longer teeth of the pinion.

-   For splined shafts and hubs ISO 4156 defines the following parameters:

:   {\| class=\"wikitable\"

\|- ! Pressure Angle !! 30 ° (flat root) !! 30 ° (fillet root) !! 37,5 ° !! 45 ° \|- \| Addendum Coefficient \|\| 0.5 \|\| 0.5 \|\| 0.45 \|\| 0.4 \|- \| Dedendum Coefficient \|\| 0.75 \|\| 0.9 \|\| 0.7 \|\| 0.6 \|- \| Root Fillet Coefficient \|\| 0.2 \|\| 0.4 \|\| 0.3 \|\| 0.25 \|}



## Ograniczenia

-   Obecnie nie ma możliwości regulacji grubości zęba. Ząb i przestrzeń zęba są rozmieszczone równomiernie na kole podziałowym. Dlatego jedynym sposobem na kontrolowanie luzu jest dostosowanie odległości środka w parowaniu przekładni.
-   Obecnie nie ma [podcięcia](https://www.tec-science.com/mechanical-power-transmission/involute-gear/undercut/) w generowanym profilu przekładni. Oznacza to, że koła zębate z małą liczbą zębów mogą kolidować z zębami współpracującego koła zębatego. Dolna granica zależy od **Kąt docisku** i wynosi około 17 zębów dla 20° i 32 dla 14.5°. Większość praktycznych zastosowań toleruje brak podcięcia dla kół zębatych nieco mniejszych niż ta teoretyczna granica.



## Poradniki

Folm: [Jak zrobić przekładnie zębate w FreeCAD](https://www.youtube.com/watch?v=8VNhTrnFMfE)



## Powiązane

-   [Środowisko pracy FCGear](FCGear_Workbench.md)





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign InvoluteGear/pl
