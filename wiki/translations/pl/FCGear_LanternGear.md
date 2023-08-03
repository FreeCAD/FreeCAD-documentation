---
 GuiCommand:
   Name: FCGear LanternGear
   Name/pl: Gear: Koło drabinkowe
   MenuLocation: Gear , Koło drabinkowe
   Workbenches: FCGear_Workbench/pl
   Version: v0.16
   SeeAlso: 
---

# FCGear LanternGear/pl



## Opis

Zębatka latarniowa jest specjalną formą zębatki cykloidalnej, w której koło toczne i koło podziałowe są równej wielkości. Ponadto zęby większego koła w przekładni są zastąpione przez cylindry. Małe koło otrzymuje zazębienie cykloidalne. W ten sposób powstaje jednostronne przełożenie punktowe. Przekładnie latarniowe mogą mieć tylko uzębienie proste.

Ponieważ ich konstrukcja jest bardzo prosta, należą one do najstarszych form przekładni. Przekładnie latarniowe są stosowane, gdy wymagane są duże przełożenia, na przykład w przekładniach obrotowych młynów lub dźwigów do transportu drewna.

Koło zębate latarniowe z łańcuchami rolkowymi to ekonomiczna i wytrzymała alternatywa dla napędów zębatkowych. Prowadząc rozciągnięty łańcuch koła zębatego stycznie wzdłuż koła zębatego, ruch liniowy łańcucha jest przekształcany w ruch obrotowy koła. I odwrotnie, ruch liniowy łańcucha można również uzyskać poprzez ruch obrotowy koła zębatego latarni *(motocykl / rower)*.

![](images/Lantern-Gear_example.png ) 
*Powyżej: Przekładnia latarniowa*



## Użycie

1.  Przejdź do środowiska pracy <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **[<img src=images/FCGear_LanternGear.svg style="width:16px"> '''Koło drabinkowe'''** na pasku narzędzi.
    -   Wybierz z menu opcję **Gear → [<img src=images/FCGear_LanternGear.svg style="width:16px"> Koło drabinkowe**.
3.  Zmień parametry zębatki na wymagane *(patrz [Właściwości](#Właściwości.md))*.



## Właściwości



### Dane

Obiekt LanternGear wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:


{{Properties_Title|dokładność}}

-    **num_profiles|Integer**: Domyślnie {{Value|10}}. Wartość zwykle nie musi być zmieniana.


{{Properties_Title|Podstawowe}}

-    **bolt_radius|Length**: Domyślnie {{Value|1 mm}}. Średnica cylindra na obracającym się dysku, który działa jako drugie \"koło zębate\".

-    **szerokość|Length**: Domyślnie {{Value|5 mm}}. Wartość szerokości koła zębatego.

-    **moduł|Length**: Domyślnie {{Value|1 mm}}. Moduł jest stosunkiem średnicy referencyjnej koła zębatego podzielonej przez liczbę zębów *(patrz [Uwagi](#Uwagi.md))*.


{{Properties_Title|gear_parameter}}

-    **zęby|Integer**: Domyślnie {{Value|15}}. Liczba zębów.


{{Properties_Title|tolerancja}}

-    **head|Float**: Domyślnie {{Value|0}}.


{{Properties_Title|wersja}}

-    **wersja|String**:



## Uwagi

-    **module**: Korzystając z wytycznych ISO (Międzynarodowej Organizacji Normalizacyjnej), rozmiar modułu jest określany jako jednostka reprezentująca rozmiary zębów przekładni. Moduł (m): m = 1 (p = 3,1416), m = 2 (p = 6,2832), m = 4 (p = 12,566). Jeśli pomnożymy moduł przez Pi, otrzymamy Pitch - Skok (p). Skok to odległość między odpowiednimi punktami na sąsiednich zębach.



## Przydatne wzory 


**średnica koła wierzchołkowego**

= **moduł** \* **(zęby +2)**.

-    **średnica podziałowa**= **moduł** \* **zęby**

-    **rozstaw osi**= **średnica podziałowa (średnica kół drabinkowych 1 + 2)** : 2



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear LanternGear/pl
