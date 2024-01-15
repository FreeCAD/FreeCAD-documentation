---
 GuiCommand:
   Name: FCGear WormGear
   Name/pl: FCGear: Przekładnia ślimakowa
   MenuLocation: Gear , Przekładnia ślimakowa
   Workbenches: FCGear_Workbench/pl
   Shortcut: None
   Version: v0.16
   SeeAlso: PartDesign_InvoluteGear/pl
---

# FCGear WormGear/pl



## Opis

Ślimak można uznać za szczególny przypadek koła zębatego walcowego. Wyobraź sobie, że na kole zębatym czołowym znajduje się tylko jeden ząb. Teraz zwiększ kąt pochylenia linii śrubowej tak bardzo, że ząb owija się wokół koła zębatego czołowego kilka razy, zanim pojawi się po przeciwnej stronie. Rezultatem będzie ślimak z pojedynczym gwintem.

W przypadku ślimaka o pojedynczym rozruchu każdy pełny obrót *(360 stopni)* ślimaka przesuwa przekładnię o jeden ząb. Zatem przekładnia z 24 zębami zapewni redukcję przełożenia 24:1. W przypadku ślimaka wielostartowego redukcja przekładni jest równa liczbie zębów koła zębatego podzielonej przez liczbę uruchomień ślimaka.

Ślimak może być używany tylko z kołem ślimakowym. Nazywa się to napędem ślimakowym. Podobnie jak inne przekładnie, napęd ślimakowy może zmniejszać prędkość obrotową lub przenosić wyższy moment obrotowy. Jedną z głównych zalet przekładni ślimakowych jest to, że mogą one przenosić ruch pod kątem 90 stopni. Przekładnia ślimakowa jest również samoblokująca.

![](images/Worm-Gear_example.png ) 
*Przekładnia ślimakowa ''(liczba zębów 3)''*



## Użycie

1.  Przejdź do środowiska pracy <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **[<img src=images/FCGear_WormGear.svg style="width:16px"> '''Przekładnia ślimakowa'''** na pasku narzędzi.
    -   Wybierz z menu opcję **Gear → [<img src=images/FCGear_WormGear.svg style="width:16px"> Przekładnia ślimakowa**.
3.  Zmień parametry zębatki na wymagane *(patrz [Właściwości](#Właściwości.md))*.



## Właściwości

Obiekt Przekładnia ślimakowa wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **średnica|Length**: Wartością domyślną jest {{Value|5 mm}}. Średnica podziałki.

-    **wysokość|Length**: Wartością domyślną jest {{Value|5 mm}}. Wartość długości ślimaka.

-    **moduł|Length**: Wartością domyślną jest {{Value|1 mm}}. Moduł jest stosunkiem średnicy referencyjnej koła zębatego podzielonej przez liczbę zębów *(patrz [Uwagi](#Uwagi.md))*.

-    **odwrotny_skok|Bool**: Wartością domyślną jest {{False/pl}}, {{True/pl}} zmienia kierunek obrotu z prawego na lewy.

-    **zęby|Integer**: Wartością domyślną jest {{Value|3}}. Ilość zębów *(patrz [Uwagi](#Uwagi.md))*.


{{Properties_Title|Obliczone}}

-    **beta|Angle**: (tylko do odczytu) Kąt natarcia *(zobacz także informacje w sekcji [Uwagi](#Uwagi.md) i [Przydatne wzory](#Przydatne_wzory.md))*.


{{Properties_Title|Ewolwenta}}

-    **kąt_natarcia|Angle**: Wartością domyślną jest {{Value|20 °}} *(patrz sekcja [Uwagi](#Uwagi.md))*.


{{Properties_Title|Tolerancja}}

-    **prześwit|Float**: Domyślną wartością jest {{Value|0.25}}. *(patrz sekcja [Uwagi](#Uwagi.md))*.

-    **head|Float**: Domyślną wartością jest {{Value|0}}. Ta wartość jest używana do zmiany wysokości zęba.


{{Properties_Title|Wersja}}

-    **Wersja|String**:



## Uwagi

-    **beta**: Jeśli kąt wyprzedzenia jest mniejszy niż 5°, jest to przekładnia samohamowalna. Typowym przykładem są kołki strojeniowe na gitarze lub ukulele.

-    **luz**: W przypadku przekładni ślimakowej, luz jest odległością pomiędzy wierzchołkiem zęba ślimaka a nasadą zęba koła ślimakowego.

-    **moduł**: Korzystając z wytycznych ISO *(Międzynarodowej Organizacji Normalizacyjnej)*, rozmiar modułu jest określany jako jednostka reprezentująca rozmiary zębów przekładni. Moduł *(m)*: m = 1 (p = 3,1416), m = 2 (p = 6,2832), m = 4 (p = 12,566). Jeśli pomnożymy moduł przez Pi, otrzymamy Skok (p). Skok to odległość między odpowiednimi punktami na sąsiednich zębach. Jeśli moduł zostanie zmieniony, zmieni się również kąt wyprzedzenia (**beta**).

-    **zęby**: Liczba zębów w ślimacznicy nazywana jest liczbą zwojów. W związku z tym mówi się o ślimacznicach jedno-, dwu- lub wielokrotnych. Ogólnie rzecz biorąc, produkowane są głównie pojedyncze ślimacznice, ale w szczególnych przypadkach liczba startów może wynosić do czterech *(czasami także więcej)*. Jeśli zmienia się liczba zębów, zmienia się również **beta**.

-    **pressure_parameter**: Parametr należy zmieniać tylko wtedy, gdy dostępna jest wystarczająca wiedza na temat geometrii przekładni.



## Przydatne wzory 

-    **beta ''(kąt natarcia)''**= arctan (**moduł** \* **ilość zębów** : **pitchdiameter ''(średnica)''**)

-    **podziałka osiowa**= **pi** \* **moduł** \* **ilość zębów**

-    **beta ''(kąt natarcia)''**= arctan (**podziałka osiowa** : (**pitchdiameter ''(średnica)''** \* **pi**))

-    **długość ślimacznicy**= 4,5 \* **moduł** \* **pi**



## Koło ślimakowe 

Koło ślimakowe musi być zaprojektowane ręcznie. W tym celu można użyć [koła zębatego ewolwentowego](FCGear_InvoluteGear/pl.md) aby uprościć konstrukcję. W każdym przypadku wymagana jest dogłębna znajomość typów przekładni.

![](images/Worm-Gear_example3.png ) 
*Ślimak z kołem ślimakowym.*



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear WormGear/pl
