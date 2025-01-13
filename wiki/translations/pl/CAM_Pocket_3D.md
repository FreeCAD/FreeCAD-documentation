---
 GuiCommand:
   Name: CAM Pocket 3D
   Name/pl: CAM: Obróbka kieszeni
   MenuLocation: CAM , Obróbka kieszeni
   Workbenches: CAM_Workbench/pl
---

# CAM Pocket 3D/pl



## Opis

To polecenie wstawia obiekt ścieżki <img alt="" src=images/CAM_3DPocket.svg  style="width:24px;"> [Obróbka kieszeni](CAM_Pocket_3D/pl.md) do Zadania. Operacja ta uwzględnia dolną powierzchnię kieszeni, jak również wybrane ściany, które nie są pionowe. W obecnym stanie operacja ta służy do zgrubnego wycinania kieszeni o ścianach, które nie są pionowe i/lub dnie, które nie jest poziome. Powszechną techniką wykańczania jest użycie kulistego frezu wraz z eksperymentalną operacją <img alt="" src=images/CAM_Surface.svg  style="width:24px;"> [Powierzchnia 3D](CAM_Surface/pl.md).

<img alt="" src=images/Path_3D_Pocket_Sample.png  style="width:600px;"> 
*Przykładowa operacja obróbki kieszeni użyta do wyczyszczenia cylindrycznego uchwytu baterii.*



## Użycie



### Tworzenie kieszeni 3D 

1.  Wewnątrz Zadania wybierz jedną lub więcej ścian z modelu zadania do uwzględnienia jako geometrię podstawową.
2.  Uruchom polecenie **<img src="images/CAM_3DPocket.svg" width=16px> [Kieszeń 3D](CAM_Pocket_3D/pl.md)** lub wybierz opcję ** CAM** → **<img src="images/CAM_3DPocket.svg" width=16px> [Kieszeń 3D](CAM_Pocket_3D/pl.md)** z górnego menu.
3.  Wybierz kontroler narzędzia z okna dialogowego wyboru.
4.  Dodaj lub usuń elementy geometrii podstawowej w celu skonfigurowania operacji.
5.  Sprawdź zakładkę Głębokość, aby upewnić się, że Głębokość początkowa, Głębokość końcowa i Krok w dół są poprawnie ustawione. Ostateczna głębokość jest określana przez wybór geometrii i nie może być modyfikowana.
6.  Sprawdź zakładkę Wysokości, aby upewnić się, że Wysokość bezpieczna i Odstęp bezpieczeństwa są odpowiednie.
7.  Sprawdź zakładkę Operacja, gdzie można ponownie wybrać kontroler narzędzia, skonfigurować tryb cięcia na Podejście lub Konwencjonalne, ustawić Wzór, dostosować procent szerokości skrawania i zastosować Zakres przejść.
8.  Kliknij **Zastosuj**, aby zobaczyć ścieżkę frezowania dla przejść operacji. Dostosuj parametry, aż będziesz zadowolony z operacji.
9.  Kliknij **OK**, aby zapisać operację.



## Uwagi

-   Wszystkie ścieżki generowane przez tę operację są oparte na standardowym frezie walcowym, używając średnicy narzędzia wybranego dla operacji Kieszeni 3D.
-   Frezy kuliste i inne kształty nie są brane pod uwagę przy generowaniu ścieżki, nawet jeśli zostały wybrane jako narzędzie dla tej operacji.



## Opcje

-   Użyj właściwości **Adaptive Pocket Finish**, aby spróbować zminimalizować frezowanie w powietrzu poniżej kieszeni 3D, gdy kieszeń jest otworem przez model.
-   Użyj właściwości **Adaptive Pocket Start**, aby spróbować zminimalizować frezowanie w powietrzu podczas wchodzenia do kieszeni. Na przykład, spójrz na obrazek w sekcji [Opis](CAM_Pocket_3D/pl#Opis.md) tej strony. Aby zmniejszyć frezowanie w powietrzu nad kieszenią 3D, ustaw tę właściwość na True, a ścieżki będą zaczynać się bliżej kieszeni, znacznie bliżej miejsca, gdzie kieszeń faktycznie się zaczyna. Zobacz poniższy obrazek i zauważ różnicę w wysokości początku ścieżki. Frezowanie w powietrzu jest zredukowane.

<img alt="" src=images/3D_Pocket_Sample_Adaptive_Start.png  style="width:600px;"> 
*Przykład operacji Kieszeni 3D użytej do wyczyszczenia cylindrycznego uchwytu baterii z opcją Adaptive Pocket Start włączoną aby zredukować frezowanie w powietrzu po wejściu.*

-   Jeśli chcesz przetworzyć cały model i surowiec jako całość, użyj właściwości **Process Stock Area** ustawionej na True, bez wybranej geometrii podstawowej.



## Właściwości



### Dane


{{TitleProperty|Podstawa}}

Uwaga: Zaleca się, aby nie edytować właściwości Umiejscowienie operacji ścieżki. Zamiast tego, przesuń lub obróć model Zadania CAM w razie potrzeby.

-    **Placement**: Ogólne umiejscowienie \[pozycja i rotacja\] obiektu - względem punktu początkowego (lub punktu początkowego kontenera obiektu nadrzędnego)

    -   
        **Angle**
        
        : Kąt w stopniach zastosowany do rotacji obiektu wokół wartości właściwości Axis

    -   
        **Axis**
        
        : Oś (jedna lub wiele) wokół której obraca się obiekt, ustawiana w podwłaściwościach: X, Y, Z

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
        
        : Pozycja obiektu, ustawiana w podwłaściwościach: X, Y, Z - względem punktu początkowego (lub punktu początkowego kontenera obiektu nadrzędnego)

        -   
            **X**
            
            : Wartość odległości w osi X

        -   
            **Y**
            
            : Wartość odległości w osi Y

        -   
            **Z**
            
            : Wartość odległości w osi Z

-    **Label**: Nazwa obiektu nadana przez użytkownika (UTF-8)


{{TitleProperty|Głębokość}}

-    **Clearance Height**: Wysokość potrzebna do usunięcia zacisków i przeszkód

-    **Final Depth**: Ostateczna głębokość narzędzia - najniższa wartość w osi Z

-    **Finish Depth**: Maksymalna ilość materiału usuwanego podczas ostatniego przejazdu

-    **Safe Height**: Wysokość powyżej której dozwolone są szybkie ruchy

-    **Start Depth**: Początkowa głębokość narzędzia - pierwsza głębokość cięcia w osi Z

-    **Step Down**: Stopniowe zagłębianie narzędzia


{{TitleProperty|Ściana}}

-    **Offset Pattern**: Wzór czyszczenia do użycia. (Wybierz sposób, w jaki powinny być wykonywane poziome ruchy.)


{{TitleProperty|Ścieżka}}

-    **Active**: Ustaw na False, aby zapobiec generowaniu kodu przez operację

-    **Base**: Geometria podstawowa dla tej operacji

-    **Comment**: Opcjonalny komentarz do tej operacji

-    **Coolant Mode**: Tryb chłodzenia dla tej operacji

-    **Cycle Time**: Szacunkowy czas cyklu dla tej operacji

-    **Tool Controller**: Określa kontroler narzędzia używany w operacji

-    **User Label**: Etykieta przypisana przez użytkownika


{{TitleProperty|Kieszeń}}

-    **Adaptive Pocket Finish**: Użyj algorytmu adaptacyjnego, aby wyeliminować nadmierne frezowanie w powietrzu poniżej dna płaskiej kieszeni.

-    **Adaptive Pocket Start**: Użyj algorytmu adaptacyjnego, aby wyeliminować nadmierne frezowanie w powietrzu powyżej górnej krawędzi płaskiej kieszeni.

-    **Cut Mode**: Kierunek, w którym narzędzie ma obracać się wokół części: zgodnie z ruchem wskazówek zegara (CW) lub przeciwnie do ruchu wskazówek zegara (CCW).

-    **Extra Offset**: Dodatkowe przesunięcie do zastosowania w operacji. Kierunek zależy od operacji.

-    **Handle Multiple Features**: Wybierz sposób przetwarzania wielu cech Geometrii podstawowej.

-    **Keep Tool Down**: Próbuje unikać niepotrzebnych podniesień narzędzia.

-    **Min Travel**: Użyj sortowania 3D ścieżki

-    **Process Stock Area**: Przetwórz model i materiał w operacji bez wybranej Geometrii podstawowej.

-    **Start At**: Rozpocznij frezowanie od środka lub krawędzi

-    **Step Over**: Procent średnicy narzędzia do przesunięcia na każdym przejściu

-    **Zig Zag Angle**: Kąt wzoru zygzakowatego


{{TitleProperty|Obrót}}

Uwaga: Obrót nie jest dostępny dla Kieszeni 3D na ten moment (wersja 0.19).

-    **Enable Rotation**: Włącz obrót, aby uzyskać dostęp do kieszeni lub obszarów, które nie są normalne do osi Z.


{{TitleProperty|Punkt początkowy}}

-    **Start Point**: Niestandardowy punkt początkowy ścieżki tej operacji.

    -   
        **X**
        
        : Wartość odległości w osi X

    -   
        **Y**
        
        : Wartość odległości w osi Y

    -   
        **Z**
        
        : Wartość odległości w osi Z

-    **Use Start Point**: Ustaw na True, jeśli ręcznie określasz punkt początkowy. Ustaw punkt początkowy w polu danych właściwości Start Point.



### Widok

Pusto



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Przykład:


```python
#Place code example here.
```





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Pocket 3D/pl
