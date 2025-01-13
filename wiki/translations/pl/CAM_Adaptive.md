---
 GuiCommand:
   Name: CAM Adaptive
   Name/pl: CAM: Adaptacyjnie
   MenuLocation: CAM , Adaptacyjnie
   Workbenches: CAM_Workbench/pl
---

# CAM Adaptive/pl



## Opis

Algorytm operacji <img alt="" src=images/CAM_Adaptive.svg  style="width:24px;"> [Adaptacyjnie](CAM_Adaptive/pl.md) tworzy ścieżki do czyszczenia i profilowania. Operacja zmienia zaangażowanie narzędzia tak, aby usuwanie materiału nigdy nie przekraczało maksymalnej wartości.



## Użycie

Instrukcje używania operacji [Adaptacyjnie](CAM_Adaptive/pl.md) są tu przedstawione.



#### Operacja podstawowe 

1.  Naciśnij ikonę **<img src="images/CAM_Adaptive.svg" width=16px> [Adaptacyjnie](CAM_Adaptive/pl.md)**, lub wybierz opcję **CAM** → **<img src="images/CAM_Adaptive.svg" width=24px> [Adaptacyjnie](CAM_Adaptive/pl.md)** z górnego menu.
2.  Wybierz kontroler narzędzia dla operacji z okna dialogowego kontrolera narzędzi, jeśli zostaniesz o to poproszony.
3.  Dostosuj głębokości operacji w zakładce Głębokość: Głębokość początkowa, Głębokość końcowa, Krok w dół.
4.  W razie potrzeby dokonaj poprawek w zakładce Wysokości.
5.  Skonfiguruj ustawienia w zakładce Operacja:
    1.  (**Zobacz sekcję [Właściwości](#Właściwości.md) → Adaptacyjnie poniżej.**)
    2.  Ustaw wartość Szerokość skrawania jako procent średnicy narzędzia.
6.  Jeśli chcesz zobaczyć podgląd wyników przed zaakceptowaniem ustawień, kliknij **Zastosuj**.
7.  Kliknij **OK**, aby potwierdzić i wygenerować ścieżki.



### Wstępne uwagi na temat czyszczenia adaptacyjnego 

-   W zależności od rozmiaru i złożoności obszaru operacji, może być lepiej nie przeliczać operacji po każdej zmianie właściwości; zamiast tego rozważ:
    -   dezaktywowanie operacji za pomocą narzędzia **<img src="images/CAM_OpActiveToggle.svg" width=16px> [Aktywne](CAM_OpActiveToggle/pl.md)**, wprowadzenie zmian we właściwościach operacji, a następnie ponowne kliknięcie ikony **<img src="images/CAM_OpActiveToggle.svg" width=16px> [Aktywne](CAM_OpActiveToggle/pl.md)** w celu ponownego aktywowania operacji - co wywoła wewnętrzne przeliczenie.
-   Operacja **<img src="images/CAM_Adaptive.svg" width=16px> [Adaptacyjnie](CAM_Adaptive/pl.md)** może zawierać kilka błędów, które nie zostały jeszcze jednoznacznie zidentyfikowane. Prosimy zgłaszać błędy i problemy na [Forum FreeCAD Path/CAM](https://forum.freecadweb.org/viewforum.php?f=15).
-   Nie wszystkie kształty narzędzi mogą być uwzględniane w tej operacji. Sprawdź forum FreeCAD w celu uzyskania dalszych informacji.
-   Jeśli zdecydujesz się uruchomić symulator ścieżek w środowisku pracy CAM, używa on tylko standardowego frezu końcowego do symulacji ścieżek. Dlatego nie zobaczysz usuwania materiału specyficznego dla kształtu narzędzia. Usuwanie materiału jest pokazane przy użyciu kształtu frezu końcowego.



## Właściwości

***Uwaga***: Nazwy niektórych właściwości na tej liście różnią się nieco od tych samych ustawień używanych w edytorze okna dialogowego.


{{TitleProperty|Adaptacyjnie}}

-    **Force Inside-Out**: Wymuś wchodzenie w materiał od środka i usuwanie w kierunku krawędzi

-    **Helix Angle**: Kąt rampy spiralnej (stopnie)

-    **Helix Cone Angle**: Kąt (stopnie) stożka spiralnego

-    **Helix Diameter Limit**: Ograniczenie średnicy wejścia spiralnego, jeśli limit jest większy niż średnica narzędzia lub 0, używana jest średnica narzędzia

-    **Keep Tool Down Ratio**: Maksymalna długość ścieżki trzymania narzędzia w dół w porównaniu do bezpośredniej odległości między punktami

-    **Lift Distance**: Odległość podnoszenia podczas szybkich ruchów

-    **Operation Type**: Rodzaj operacji adaptacyjnej: Usuwanie lub Profilowanie

-    **Side**: Strona wybranych powierzchni, którą narzędzie powinno ciąć: Wewnętrzna lub Zewnętrzna

-    **Step Over**: Procent średnicy narzędzia, który należy przesunąć na każdej ścieżce

-    **Stock to Leave**: Ile materiału pozostawić (np. na osobną operację wykończeniową)

-    **Tolerance**: Wpływa na dokładność i wydajność

-    **Use Helix Arcs**: Użyj łuków (G2) dla rampy spiralnej


{{TitleProperty|Podstawa}}

Uwaga: Zaleca się, aby nie edytować właściwości Umiejscowienie operacji ścieżki. W razie potrzeby należy raczej przesunąć lub obrócić model zadania CAM.

-    **Placement**: Ogólne umiejscowienie \[położenie i rotacja\] obiektu - względem początku (lub początku kontenera obiektu nadrzędnego)

    -   
        **Angle**
        
        : Kąt w stopniach stosowany do obrotu obiektu wokół wartości właściwości Axis

    -   
        **Axis**
        
        : Oś (jedna lub wiele), wokół której obiekt ma być obracany, ustawiona w pod-właściwościach: X, Y, Z

        -   
            **X**
            
            : Wartość osi X

        -   
            **Y**
            
            : Wartość osi Y

        -   
            **Z**
            
            : Wartość osi Z

    -   
        **Position**
        
        : Położenie obiektu, ustawione w pod-właściwościach: X, Y, Z - względem początku (lub początku kontenera obiektu nadrzędnego)

        -   
            **X**
            
            : Wartość odległości w osi X

        -   
            **Y**
            
            : Wartość odległości w osi Y

        -   
            **Z**
            
            : Wartość odległości w osi Z

-    **Label**: Nazwa obiektu dostarczona przez użytkownika (UTF-8)


{{TitleProperty|Głębokość}}

-    **Clearance Height**: Wysokość potrzebna do usunięcia zacisków i przeszkód

-    **Final Depth**: Ostateczna głębokość narzędzia - najniższa wartość w osi Z

-    **Finish Depth**: Maksymalna ilość materiału usuwanego podczas ostatniego przejazdu

-    **Safe Height**: Wysokość powyżej której dozwolone są szybkie ruchy

-    **Start Depth**: Początkowa głębokość narzędzia - pierwsza głębokość cięcia w osi Z

-    **Step Down**: Stopniowe zagłębianie narzędzia


{{TitleProperty|Ścieżka}}

-    **Active**: Ustaw na False, aby zapobiec generowaniu kodu przez operację

-    **Comment**: Opcjonalny komentarz dla tej operacji

-    **Tool Controller**: Określa kontroler narzędzia używany w operacji

-    **User Label**: Etykieta przypisana przez użytkownika



## Układ edytora w oknie zadań 

*Opisy ustawień znajdują się na powyższej liście właściwości*.

Ta sekcja jest po prostu mapą układu ustawień w edytorze okien dla operacji.



### Geometria podstawowa 

-   **Dodaj**: Dodaje wybrane elementy, które powinny być bazą dla ścieżek.
-   **Usuń**: Usuwa wybrane elementy z listy Geometria podstawowa.
-   **Wyczyść**: Czyści wszystkie elementy na liście Geometria podstawowa.



### Głębokości

-    **Start Depth**
    

-    **Final Depth**
    

-    **Finish Depth**
    

-    **Step Down**
    

### Heights

-    **Safe Height**
    

-    **Clearance Height**
    



### Operacja

-    **Tool Controller**
    

-    **Cut Region**(Side)

-    **Operation Type**
    

-    **Step Over Percent**
    

-    **Accuracy vs Performance**(Tolerance)

-    **Helix Ramp Angle**
    

-    **Helix Cone Angle**
    

-    **Helix Max Diameter**(Helix Diameter Limit)

-    **Lift Distance**
    

-    **Keep Tool Down Ratio**
    

-    **Stock to Leave**
    

-    **Force Clearing Inside-Out**
    

-    **Stop**
    



## Znane problemy 

W przypadku gdy CAM: Adaptacyjnie tworzy niepożądane ścieżki, spróbuj ustawić **Stock to Leave** na {{Value|0,001 mm}} lub więcej. Możesz zmniejszyć średnicę narzędzia o dwukrotność tej wartości, aby utrzymać dokładność ścieżek.

Dostępne jest poniższe rozwiązanie (ale nikt go nie implementuje):

<https://github.com/FreeCAD/FreeCAD/pull/5276>



## Źródła

-   Strona GitHub autora o oryginalnym projekcie: [kreso-t/FreeCAD_Mod_Adaptive_Path](https://github.com/kreso-t/FreeCAD_Mod_Adaptive_Path)
-   Temat na forum FreeCAD o operacji Adaptacyjnie: [Adaptive Path/CAM Operation](https://forum.freecadweb.org/viewtopic.php?f=15&t=30127)





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Adaptive/pl
