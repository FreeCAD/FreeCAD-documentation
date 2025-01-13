---
 GuiCommand:
   Name: CAM Drilling
   Name/pl: CAM: Wiercenie
   MenuLocation: CAM , Wiercenie
   Workbenches: CAM_Workbench/pl
---

# CAM Drilling/pl



## Opis

Narzędzie <img alt="" src=images/CAM_Drilling.svg  style="width:16px;"> [Wiercenie](CAM_Drilling/pl.md) generuje Operację wiercenia w Zadaniu.

<img alt="" src=images/Path_Drilling_Sample.png  style="width:400px;"> 
*Powyżej: Przykład operacji wiercenia*



## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/CAM_Drilling.svg" width=16px> [Wiercenie](CAM_Drilling/pl.md)**.
    -   Wybierz opcję **CAM → <img src="images/CAM_Drilling.svg" width=16px> Wiercenie** z menu.
2.  W sekcji **Operacja**:
    -   Wybierz **Kontroler narzędzi**.
    -   Wybierz **Tryb chłodzenia**.
    -   Opcjonalnie włącz i dostosuj następujące ustawienia:
        -   
            **Zagłębienie**
            
            ustaw **Głębokość**.

        -   
            **Postój**
            
            ustaw **Czas** w sekundach.

        -   
            **Pogłębienie**
            
            .
3.  W sekcji **Geometria podstawowa** upewnij się, że lista odpowiada otworom przeznaczonym do obróbki, i w razie potrzeby dodaj, włącz lub wyłącz otwory. Otwory można dodać, wybierając powierzchnie ścian otworów.
4.  W sekcji **Głębokość** sprawdź i, jeśli to konieczne, dostosuj **Głębokość początkową** i **Głębokość końcową**.
5.  W sekcji **Wysokości** sprawdź i, jeśli to konieczne, dostosuj **Wysokość bezpieczną** i **Odstęp bezpieczeństwa**.
6.  Naciśnij przycisk **OK**, aby wygenerować ścieżkę wiercenia.



## Uwagi

-   Podczas używania krawędzi jako Geometrii podstawowej, zawsze wybieraj dolną krawędź otworu.
-   Zawsze sprawdzaj, czy wybrane narzędzie ma odpowiednią średnicę do wybranych otworów.
-   **Zagłębienie wyłączone** generuje (cykle wiercenia G81). **Zagłębienie włączone** generuje (cykle wiercenia G83).
-   **Postój włączony** jest obecnie nieobsługiwany, ale ma generować (cykle wiercenia G82).



## Właściwości

***Uwaga***: Nie wszystkie z tych właściwości są dostępne w edytorze okna zadań. Niektóre są dostępne tylko na karcie Dane w panelu Widok właściwości dla tej operacji.


{{TitleProperty|Podstawa}}

Uwaga: Zaleca się, aby nie edytować właściwości Umiejscowienie operacji ścieżki. W razie potrzeby należy raczej przesunąć lub obrócić model zadania CAM.

-    **Placement**: Ogólne umiejscowienie \[pozycja i rotacja\] obiektu względem początku układu współrzędnych (lub początku kontenera obiektu nadrzędnego)

    -   
        **Angle**
        
        : Kąt w stopniach zastosowany do obrotu obiektu wokół wartości właściwości Oś

    -   
        **Axis**
        
        : Oś (jedna lub wiele), wokół której obraca się obiekt, ustawiona w podwłaściwościach: X, Y, Z

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
        
        : Pozycja obiektu, ustawiona w podwłaściwościach: X, Y, Z - względem początku układu współrzędnych (lub początku kontenera obiektu nadrzędnego)

        -   
            **X**
            
            : Wartość odległości X

        -   
            **Y**
            
            : Wartość odległości Y

        -   
            **Z**
            
            : Wartość odległości Z

-    **Label**: Nazwa obiektu nadana przez użytkownika (UTF-8)

-    **Disabled**: Lista wyłączonych funkcji


{{TitleProperty|Głębokość}}

-    **Clearance Height**: Wysokość potrzebna do usunięcia zacisków i przeszkód

-    **Final Depth**: Ostateczna głębokość narzędzia - najniższa wartość w osi Z

-    **Safe Height**: Wysokość, powyżej której dozwolone są szybkie ruchy (szybka wysokość bezpieczeństwa między lokalizacjami)

-    **Start Depth**: Początkowa głębokość narzędzia - *pierwsza głębokość cięcia w osi Z*


{{TitleProperty|Wiertło}}

-    **Add Tip Length**: Oblicz długość końcówki i odejmij od ostatecznej głębokości

-    **Dwell Enabled**: Włącz zatrzymanie

-    **Dwell Time**: Czas zatrzymania między cyklami skrawania

-    **Peck Depth**: Głębokość wiercenia przed cofnięciem w celu oczyszczenia wiórów

-    **Peck Enabled**: Włącz zagłębienie

-    **Retract Height**: Wysokość, na której zaczyna się posuw i wysokość cofania narzędzia po zakończeniu ścieżki

-    **Return Level**: Kontroluje sposób cofania narzędzia, Domyślnie=G98


{{TitleProperty|Ścieżka}}

-    **Active**: Ustaw na False, aby zapobiec generowaniu kodu operacji

-    **Comment**: Opcjonalny komentarz do tej operacji

-    **User Label**: Etykieta przypisana przez użytkownika

-    **Tool Controller**: Definiuje kontroler narzędzia używanego w operacji


{{TitleProperty|Obrót}}

(*gdy dostępne*)

-    **Attempt Inverse Angle**: Automatycznie spróbuj odwrócić kąt, jeśli początkowy obrót jest niepoprawny.

-
-    **Enable Rotation**: Włącz obroty, aby uzyskać dostęp do otworów nieprostopadłych do osi Z.

-    **Inverse Angle**: Odwróć kąt obrotu. ***Przykład:** zmiana obrotu z -22,5 na 22,5 stopnia.*

-    **Reverse Direction**: Odwróć orientację operacji o 180 stopni.



## Układ edytora w oknie zadań 

*Opisy ustawień znajdują się na powyższej liście właściwości*.

Ta sekcja jest po prostu mapą układu ustawień w edytorze okien dla operacji.



### Geometria podstawowa 

-   **Dodaj**: Dodaje wybrane elementy, które powinny być bazą dla ścieżek.
-   **Usuń**: Usuwa wybrane elementy z listy Geometria podstawowa.
-   **Wyczyść**: Czyści wszystkie elementy na liście Geometria podstawowa.



### Lokalizacja bazowa 

-   **Add**: Dodaj współrzędne (X,Y) do bieżącej operacji wiercenia.
-   **Remove**: Usuń wybrane elementy z listy lokalizacji bazowej.
-   **Edit**: Edytuj wybrany element lokalizacji.



### Głębokości

-   **Start Depth**:
-   **Final Depth**:



### Wysokości

-   **Safe Height**:
-   **Clearance Height**:



### Operacja

-   **Tool Controller**:
-   **Retract Height**:
-   **Peck**:
-   **Peck Depth**:
-   **Dwell**:
-   **Dwell Time**:
-   **Use Tip Length**:



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
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Drilling/pl
