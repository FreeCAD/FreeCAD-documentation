---
- GuiCommand:
   Name:FCGear InvoluteGear
   Name/pl:FCGear: Koło zębate ewolwentowe
   MenuLocation:Gear - Koło zębate ewolwentowe
   Workbenches:[FCGear](FCGear_Workbench/pl.md)
   Version:v0.16
   SeeAlso:[Koło zębate cykloidalne](FCGear_CycloideGear/pl.md)
---

# FCGear InvoluteGear/pl



## Opis

Ze względu na korzystny współczynnik zazębienia i stosunkowo prostą produkcję, przekładnie ewolwentowe są najczęściej stosowaną formą zębów w inżynierii mechanicznej. Koła zębate można znaleźć wszędzie tam, gdzie ruch i siła mają być przenoszone z jednej części na drugą. Na przykład można je znaleźć w maszynach, samochodach, zegarkach lub urządzeniach gospodarstwa domowego. Ruch jest często przenoszony bezpośrednio z jednego koła zębatego na drugie, ale czasami również za pomocą łańcucha. Ponadto można zmienić kierunek obrotu. Możliwa jest również łatwa zmiana ruchu promieniowego na liniowy za pomocą [ewolwentowej listwy zębatej](FCGear_InvoluteRack/pl.md).

![](images/Involute-Gear_example.png ) 
*Od lewej do prawej: Przekładnia czołowa, przekładnia walcowa, podwójna przekładnia walcowa*



## Użycie

1.  Przejdź do środowiska pracy <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **[<img src=images/FCGear_InvoluteGear.svg style="width:16px"> '''Koło zębate ewolwentowe'''** na pasku narzędzi.
    -   Wybierz z menu opcję **Gear → [<img src=images/FCGear_InvoluteGear.svg style="width:16px"> Koło zębate ewolwentowe**.
3.  Zmień parametry zębatki na wymagane *(patrz [Właściwości](#Właściwości.md))*.



## Właściwości

Obiekt InvoluteGear wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Dokładność}}

-    **liczba punktów|Integer**: Domyślnie {{Value|6}}. Zmiana profilu ewolwentowego. Zmiana wartości może prowadzić do nieoczekiwanych rezultatów.

-    **uprość|Bool**: Wartością domyślną jest {{False/pl}}, {{True/pl}} generuje uproszczone wyświetlanie *(bez zębów i tylko cylinder o średnicy podziałowej)*.


{{Properties_Title|Podstawowe}}

-    **wysokość|Length**: Wartością domyślną jest {{Value|5 mm}}. Wartość szerokości koła zębatego.

-    **moduł|Length**: Domyślnie {{Value|1 mm}}. Moduł jest stosunkiem średnicy referencyjnej koła zębatego podzielonej przez liczbę zębów *(patrz [Uwagi](#Uwagi.md))*.

-    **zęby|Integer**: Domyślną wartością jest {{Value|15}}. Liczba zębów *(patrz [Uwagi](#Uwagi.md))*.


{{Properties_Title|Obliczone}}

-    **angular_backlash|Angle**: *(tylko do odczytu)*.

-    **da|Length**: *(tylko do odczytu)* Średnica zewnętrzna, mierzona na wierzchołku zęba *(końcówki zębów)*.

-    **df|Length**: *(tylko do odczytu)* Średnica korzenia, mierzona u podstawy zębów.

-    **dw|Length**: *(tylko do odczytu)* Średnica podziałki roboczej.

-    **transverse_pitch|Length**: *(tylko do odczytu)* Podziałka w płaszczyźnie obrotu.


{{Properties_Title|Zaokrąglenie}}

-    **zaokrąglenie_głowy|Float**: Domyślnie {{Value|0 mm}}.

-    **zaokrąglenie_stopy|Float**: Domyślnie {{Value|0 mm}}.

-    **podcięcie|Bool**: Domyślną wartością jest {{False/pl}}, {{True/pl}} zmienia profil korzenia zęba *(patrz [Uwagi](#Uwagi.md))*.


{{Properties_Title|Śrubowy}}

-    **beta|Angle**: Domyślnie {{Value|0 °}}. Z kątem helisy β tworzone jest koło zębate śrubowe - wartość dodatnia → kierunek obrotu w prawo, wartość ujemna → kierunek obrotu w lewo *(patrz [Uwagi](#Uwagi.md))*.

-    **double_helix|Bool**: Domyślną wartością jest {{False/pl}}, {{True/pl}} tworzy podwójną helisę *(patrz [Uwagi](#Uwagi.md))*.

-    **properties_from_tool|Bool**: Domyślną wartością jest {{False/pl}}. Jeśli wybrano {{True/pl}} i parametr **beta** nie jest równy zero, parametry koła zębatego są obliczane wewnętrznie dla obróconego koła zębatego.


{{Properties_Title|Ewolwenta}}

-    **kąt_natarcia|Angle**: Domyślnie {{Value|20 °}} *(patrz [Uwagi](#Uwagi.md))*.

-    **przesunięcie|Float**: Domyślnie {{Value|0}}. Generuje dodatnie i ujemne przesunięcie profilu *(patrz [Uwagi](#Uwagi.md))*.


{{Properties_Title|tolerancja}}

-    **backlash|Length**: Domyślnie {{Value|0}}. Luz zwrotny, zwany również lagiem lub swobodnym biegiem, to odległość między zębami w parze kół zębatych.

-    **prześwit|Float**: Domyślnie {{Value|0.25}}. *(patrz [Uwagi](#Uwagi.md))*.

-    **head|Float**: Domyślnie {{Value|0}}. Wartość ta jest używana do zmiany wysokości zęba.

-    **reversed_backlash|Bool**: Wartość {{True/pl}} zmniejsza luz lub {{False/pl}} *(domyślnie)* i właściwość backslash zwiększa luz *(patrz [Uwagi](#Uwagi.md))*.


{{Properties_Title|wersja}}

-    **Wersja|String**:



## Uwagi

-    **beta**: Gdy zmienia się **beta**, zmienia się również **pitch diameter**. Poniższy wzór ilustruje wzajemne oddziaływanie parametrów: d = m \* Z / cos beta *(Z = liczba zębów, d = średnica podziałowa, m = moduł)*. Oznacza to, że dla koła zębatego czołowego: cos beta = 0, a dla koła zębatego walcowego: cos beta \> 0. Jednak kąt pochylenia linii śrubowej mniejszy niż 10° nie ma prawie żadnych zalet w porównaniu z zębami prostymi.

-    **prześwit**: W przypadku pary kół zębatych prześwit to odległość między wierzchołkiem zęba pierwszego koła zębatego a korzeniem zęba drugiego koła zębatego.

-    **double_gear**: Aby użyć podwójnej przekładni śrubowej, należy najpierw wprowadzić kąt spirali β (**beta**) dla przekładni śrubowej.

-    **moduł**: Korzystając z wytycznych ISO (Międzynarodowej Organizacji Normalizacyjnej), rozmiar modułu jest określany jako jednostka reprezentująca rozmiary zębów przekładni. Moduł *(m)*: m = 1 *(p = 3,1416)*, m = 2 *(p = 6,2832)*, m = 4 *(p = 12,566)*. Jeśli pomnożymy moduł przez Pi, otrzymamy Skok - Pitch *(p)*. Skok to odległość między odpowiednimi punktami na sąsiednich zębach.

-    **przesunięcie**: Przesunięcie profilu nie służy wyłącznie do zapobiegania podcięciu. Może być używane do regulacji odległości między dwoma kołami zębatymi. Jeśli stosowana jest dodatnia korekta, np. w celu zapobieżenia podcięciu w zębniku, grubość zęba na górze jest mniejsza.

-    **zęby**: Jeśli zmienia się liczba zębów, zmienia się również średnica podziałowa (**dw**).

-    **podcięcie**: Podcięcie jest stosowane, gdy liczba zębów koła zębatego jest zbyt mała. W przeciwnym razie współpracujące koło zębate wbije się w korzeń zęba. Podcięcie nie tylko osłabia ząb za pomocą talii podobnej do osy, ale także usuwa część użytecznej ewolwenty przylegającej do koła podstawowego.

-    **pressure_angle**: 20° jest tutaj wartością standardową. Kąt nacisku jest definiowany jako kąt pomiędzy linią działania *(wspólną styczną do okręgów bazowych)* a prostopadłą do linii środków. Tak więc, dla standardowych kół zębatych, koła zębate o kącie natarcia 14,5° mają koła bazowe znacznie bliżej korzeni zębów niż koła zębate o kącie natarcia 20°. Z tego powodu koła zębate 14,5° napotykają większe problemy z podcinaniem niż koła zębate 20°. Kąt natarcia zmienia się wraz ze zmianą profilu. Parametr należy zmieniać tylko wtedy, gdy dostępna jest wystarczająca wiedza na temat geometrii koła zębatego.

-    **reversed_backlash**: Jeśli istnieje kilka przełożeń, należy zwrócić uwagę na to, dla którego przełożenia ustawiony jest parametr.



## Ograniczenia

Profil zęba 2D, uzyskany przez ustawienie właściwości **wysokość** na zero, nie może być używany z elementami wymagającymi kształtu 2D. Na przykład funkcje [Wyciągnij](PartDesign_Pad/pl.md) i [Addytywna helisa](PartDesign_AdditiveHelix/pl.md) nie akceptują takiego profilu jako podstawy. Szczegóły techniczne można znaleźć w powiązanym [problemie w serwisie GitHub](https://github.com/looooo/freecad.gears/issues/97).



## Przydatne wzory 



### Standardowe koła zębate czołowe 

Tutaj \"standard\" odnosi się do tych kół zębatych czołowych, które nie mają współczynnika zmiany profilu *($x$)*.

+++++
| Symbol   | Terminy                                          | Formuła                            | Parametry FCGear                            |
+==========+==================================================+====================================+=============================================+
| $m$      | *Moduł*                                          | \-                                 | $\texttt{module}$                           |
+++++
| $z$      | *Liczba zębów*                                   | \-                                 | $\texttt{teeth}$                            |
+++++
| $\alpha$ | *Kąt natarcia*                                   | \-                                 | $\texttt{pressure} {\_} \texttt{parameter}$ |
|          |                                                  | Typowo, $\alpha = 20^\circ$        |                                             |
+++++
| d        | *Średnica odniesienia* lub *Średnica podziałowa* | $z \cdot m$                        | \-                                          |
+++++
| $h^*_a$  | *współczynnik Addendum*                          | \-                                 | $h^*_a = 1 + \texttt{ head}$                |
|          |                                                  | Typowo, $h^*_a = 1$                |                                             |
+++++
| $h^*_f$  | *współczynnik Dedendum*                          | \-                                 | $h^*_f = 1 + \texttt{ clearance}$           |
|          |                                                  | Typowo, $h^*_f = 1.25$             |                                             |
+++++
| $h_a$    | *Addendum*                                       | $h_a = h^*_a \cdot m$              | \-                                          |
+++++
| $h_f$    | *Dedendum*                                       | $h_f = h^*_f \cdot m$              | \-                                          |
+++++
| $h$      | *Wysokość zęba* lub *Głębokość zęba*             | $h = h_a + h_f$                    | \-                                          |
|          |                                                  | Typowo, $h = 2.25 \cdot m$         |                                             |
+++++
| $x$      | *Współczynnik przesunięcia profilu*              | \-                                 | $\texttt{shift}$                            |
|          |                                                  | Dla standardowych zębatek, $x = 0$ |                                             |
+++++

: style=\"text-align: left;\" \| Podstawowe wzory wspólne dla wewnętrznych i zewnętrznych standardowych kół zębatych czołowych

++++
| Symbol | Terminy             | Formuła                           |
+========+=====================+===================================+
| $d_a$  | *Średnica końcówki* | $d_a = d + 2 \cdot h_a$           |
|        |                     | Typowo, $d_a = (z + 2) \cdot m$   |
++++
| $d_f$  | *Średnica korzenia* | $d_f = d - 2 \cdot h_f$           |
|        |                     | Typowo, $d_f = (z - 2.5) \cdot m$ |
++++

: style=\"text-align: left;\" \| Podstawowe wzory specyficzne dla zewnętrznych standardowych kół zębatych czołowych

++++
| Symbol | Terminy             | Formuła                           |
+========+=====================+===================================+
| $d_a$  | *Średnica końcówki* | $d_a = d - 2 \cdot h_a$           |
|        |                     | Typowo, $d_a = (z - 2) \cdot m$   |
++++
| $d_f$  | *Średnica korzenia* | $d_f = d + 2 \cdot h_f$           |
|        |                     | Typowo, $d_f = (z + 2.5) \cdot m$ |
++++

: style=\"text-align: left;\" \| Basic formulas specific to internal standard spur gears

++++
| Symbol | Terminy                                     | Formuła                    |
+========+=============================================+============================+
| $a$    | *Odległość od środka*                       | $d = \frac{d_1 + d_2}{2}$  |
++++
| $c$    | *Prześwit pomiędzy końcówkami i korzeniami* | $c_1 = h_{f2} - h_{a1}$    |
|        |                                             | $c_2 = h_{f1} - h_{a2}$    |
|        |                                             | Typowo, $c = 0.25 \cdot m$ |
++++

: style=\"text-align: left;\" \| Basic formulas specific for a pair of external standard spur gears

-   **Zębatka walcowa i podwójna zębatka walcowa**
    -   
        **średnica podziałowa (dw)**
        
        = **moduł** \* **zęby** : **cos beta**

    -   
        **rozstaw osi**
        
        = **(średnica podziałowa (dw) 1 + 2)** : 2

    -   
        **średnica koła wierzchołkowego**
        
        = **średnica podziałowa (dw)** + 2 \* **moduł**

    -   
        **moduł**
        
        = **średnica podziałowa (dw)** \* **cos beta** : **zęby**



## Tworzenie skryptów 

Wykorzystaj moc środowiska Python, aby zautomatyzować modelowanie kół zębatych: 
```python
import FreeCAD as App
import freecad.gears.commands
gear = freecad.gears.commands.CreateInvoluteGear.create()
gear.teeth = 20
gear.beta = 20
gear.height = 10
gear.double_helix = True
App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear InvoluteGear/pl
