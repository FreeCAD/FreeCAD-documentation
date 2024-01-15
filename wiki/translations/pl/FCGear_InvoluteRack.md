---
 GuiCommand:
   Name: FCGear InvoluteRack
   Name/pl: FCGear: Listwa zębata ewolwentowa
   MenuLocation: Gear , Listwa zębata ewolwentowa
   Workbenches: FCGear_Workbench/pl
   Version: v0.16
   SeeAlso: FCGear_InvoluteGear/pl
---

# FCGear InvoluteRack/pl



## Opis

Listwy zębate służą do przekształcania ruchu obrotowego w ruch liniowy lub odwrotnie. Poniższe przykłady pokazują różne zastosowania:

-   Stojak z zamontowaną przekładnią przy jazie oporowym.
-   Różne systemy zębatkowe w kolejach zębatkowych.
-   Układ kierowniczy z zębatką w pojeździe.
-   Wciągarka zębatkowa jako podnośnik mechaniczny *(np. podnośnik samochodowy)*.
-   Pneumatyczne napędy zębatkowe stosowane do sterowania zaworami w transporcie rurociągowym.

![](images/Involute-Rack_example.png ) 
*Od lewej do prawej: Przekładnia czołowa, przekładnia walcowa, podwójna przekładnia walcowa*



## Użycie

1.  Przejdź do środowiska pracy <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **[<img src=images/FCGear_InvoluteRack.svg style="width:16px"> '''Listwa zębata ewolwentowa'''** na pasku narzędzi.
    -   Wybierz z menu opcję **Gear → [<img src=images/FCGear_InvoluteRack.svg style="width:16px"> Listwa zębata ewolwentowa**.
3.  Zmień parametry zębatki na wymagane *(patrz [Właściwości](#Właściwości.md))*.



## Właściwości

Obiekt **Listwa zębata ewolwentowa** wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **dodaj_zakończenia|Bool**: Jeśli wartość to {{True/pl}} *(domyślnie)*, całkowita długość zębatki to zęby \* podziałka. Jeśli jest to {{False/pl}}, wówczas zębatka zaczyna się od boku zęba.

-    **wysokość|Length**: Domyślną wartością jest {{Value|5 mm}}. Wartość szerokości koła zębatego.

-    **moduł|Length**: Domyślną wartością jest {{Value|1 mm}}. Moduł jest stosunkiem średnicy referencyjnej koła zębatego podzielonej przez liczbę zębów (patrz [Uwagi](#Uwagi.md)).

-    **zęby|Integer**: Domyślną wartością jest {{Value|15}}. Liczba zębów.

-    **grubość|Length**: Domyślną wartością jest {{Value|5}}. Wysokość od korzenia zęba do dolnej strony pręta.


{{Properties_Title|Obliczone}}

-    **rozstaw_poprzeczny|Length**: *(tylko do odczytu)* Nachylenie w płaszczyźnie poprzecznej (patrz sekcja [Uwagi](#Uwagi.md)).


{{Properties_Title|zaokrąglenie}}

-    **head_fillet|Float**: Wartość domyślna to {{value|0 mm}}.

-    **root_fillet|Float**: Wartość domyślna to {{value|0 mm}}.


{{Properties_Title|Śrubowy}}

-    **beta|Angle**: Wartość domyślna to {{Value|0 °}}. Z kątem helisy β tworzone jest koło zębate śrubowe - wartość dodatnia → kierunek obrotu w prawo, wartość ujemna → kierunek obrotu w lewo.

-    **double_helix|Bool**: Domyślną wartością jest {{False/pl}}, {{True/pl}} tworzy podwójną helisę *(patrz [Uwagi](#Uwagi.md))*.

-    **properties_from_tool|Bool**: Domyślną wartością jest {{False/pl}}. Jeśli wybrano {{True/pl}} i parametr **beta** nie jest równy zero, parametry koła zębatego są obliczane wewnętrznie dla obróconego koła zębatego.


{{Properties_Title|ewolwenta}}

-    **kąt_natarcia|Angle**: Wartością domyślną jest {{Value|20 °}} *(patrz sekcja [Uwagi](#Uwagi.md))*.


{{Properties_Title|precyzja}}

-    **uproszczony|Bool**: Domyślną wartością jest {{False/pl}}, {{True/pl}} generuje widok uproszczony *(bez zębów)*.


{{Properties_Title|Tolerancja}}

-    **prześwit|Float**: Domyślną wartością jest {{Value|0.25}}. *(patrz sekcja [Uwagi](#Uwagi.md))*.

-    **head|Float**: Domyślną wartością jest {{Value|0}}. Ta wartość jest używana do zmiany wysokości zęba.


{{Properties_Title|Wersja}}

-    **Wersja|String**:



## Uwagi

-    **rozstaw_poprzeczny**: Wartość jest wynikiem mnożenia **moduł * pi**. Oznacza to, że dla standardowej zębatki ewolwentowej FCGear: 15 (**ząb**) \* 3.14 (**rozstaw_poprzeczny**) wynosi 47.12 mm. Zobacz także **moduł** poniżej.

-    **prześwit**: W przypadku pary kół zębatych luz to odległość między wierzchołkiem zęba pierwszego koła zębatego a korzeniem zęba drugiego koła zębatego.

-    **podwójna_helisa**: Aby użyć podwójnej przekładni śrubowej, należy najpierw wprowadzić kąt spirali β (**beta**) dla przekładni śrubowej.

-    **moduł**: Korzystając z wytycznych ISO (Międzynarodowej Organizacji Normalizacyjnej), rozmiar modułu jest określany jako jednostka reprezentująca rozmiary zębów przekładni. Moduł (m): m = 1 (p = 3,1416), m = 2 (p = 6,2832), m = 4 (p = 12,566). Jeśli pomnożymy moduł przez Pi, otrzymamy Skok (p). Skok to odległość między odpowiednimi punktami na sąsiednich zębach. Wynik mnożenia jest wyświetlany w **transverse_pitch**.

-    **parametr_naratcia**: Parametr ten należy zmieniać tylko wtedy, gdy posiadana jest wystarczająca wiedza na temat geometrii koła zębatego.



## Przydatne wzory 

Zobacz stronę [Koło zębate ewolwentowe](FCGear_InvoluteGear/pl#Przydatne_wzory.md).



## Tworzenie skryptów 

Wykorzystaj moc środowiska Python, aby zautomatyzować modelowanie kół zębatych: 
```python
import FreeCAD as App
import freecad.gears.commands
gear = freecad.gears.commands.CreateInvoluteRack.create()
gear.teeth = 20
gear.beta = 20
gear.height = 10
gear.double_helix = True
App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")
```



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear InvoluteRack/pl
