---
 GuiCommand:
   Name: CAM Profile
   Name/pl: CAM: Profil
   MenuLocation: CAM , Profil
   Workbenches: CAM_Workbench/pl
   Version: 0.19
---

# CAM Profile/pl



## Opis

Narzędzie <img alt="" src=images/CAM_Profile.svg  style="width:16px;"> [Profil](CAM_Profile/pl.md) tworzy operację konturowania na podstawie wybranych cech modelu. Narzędzie to zostało wprowadzone w wersji 0.19. Oferuje trzy operacje, które były obsługiwane przez oddzielne narzędzia w poprzednich wersjach.

Wszytkie operacje tworzą obiekty, które stają się częścią **<img src="images/CAM_Job.svg" width=24px> [Zadania CAM](CAM_Job/pl.md)**.

Oto dostępne operacje:



### Operacja Kontur 

Operacja **Kontur** jest domyślną operacją. Tworzy prosty zewnętrzny kontur cięcia obiektów 3D opartych na <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [środowiski Część](Part_Workbench/pl.md). Cały model Zadania służy jako dane wejściowe dla operacji, niezależnie od tego, czy podczas wywoływania polecenia Kontur wybrana jest jakakolwiek geometria bryły.



### Operacja Ściana profilu 

Operacja **Ściana profilu** tworzy prostą ścieżkę konturową z jednej lub więcej wybranych powierzchni obiektu.



### Operacja Krawędzie profilu 

Operacja **Krawędzie profilu** tworzy prostą ścieżkę konturową z wybranych krawędzi.

<img alt="" src=images/Path_profile_example.jpg  style="width:600px;">



## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/CAM_Profile.svg" width=16px> [Profil](CAM_Profile/pl.md)**.
    -   Wybierz opcję **CAM → <img src="images/CAM_Profile.svg" width=16px> Profil** z menu.
2.  Aktywuj sekcję Geometria podstawowa, klikając jej zakładkę, i wybierz cechy z modelu roboczego.
    -   Jeśli żadne cechy nie są wybrane, polecenie domyślnie wykonuje operację **Kontur**, konturując cały model.
    -   Jeśli wybrane są powierzchnie, wynikiem będzie operacja **Ściana profilu**.
    -   Jeśli wybrane są krawędzie, wynikiem będzie operacja **Krawędzie profilu**.
        **UWAGA**: Ta operacja otrzymała ulepszenia, które umożliwiają funkcjonalność w przypadku niektórych otwartych krawędzi (bez pętli). Zobacz sekcję [Uwagi dotyczące użycia](#Uwagi_dotyczące_użycia.md) poniżej, aby uzyskać dodatkowe informacje na temat najlepszych praktyk dla profilowania otwartych krawędzi.
3.  Aktywuj sekcję Operacja, klikając jej zakładkę, i dostosuj ustawienia operacji według potrzeb.
4.  Opcjonalnie naciśnij przycisk **Zastosuj**, aby podgląd operacji z bieżącymi ustawieniami.
5.  Kliknij przycisk **OK** lub **Anuluj**, aby utworzyć lub anulować operację.

**Ważna uwaga: Profil nie uwzględnia innych szczegółów obiektu. Musisz starannie dostosować właściwości, szczególnie głębokość końcową, ponieważ błąd może zniszczyć twój element roboczy.**

Punkt startowy można włączyć na zakładce Operacja w edytorze okna zadań, używając lokalizacji zdefiniowanej w **Widok właściwości → Dane → Punkt startowy**.

Dokonaj dodatkowych ustawień operacji, modyfikując właściwości operacji na karcie Dane w Widoku właściwości. Wszelkie zaawansowane właściwości będą dostępne tutaj, jeśli takie istnieją.



#### Uwagi dotyczące użycia 

-   Operacja **<img src="images/CAM_Profile.svg" width=16px> [Profil](CAM_Profile/pl.md)** jest w stanie profilować **otwarte krawędzie** (jedną lub więcej ciągłych krawędzi, które nie tworzą pętli w widoku z góry).
    -   Najlepiej jest wybrać górne krawędzie (najwyższe krawędzie) do zaznaczenia. Po dokonaniu wyboru, należy ręcznie ustawić Głębokość końcową dla operacji. Wybór tylko dolnych krawędzi jest nieprzewidywalny i w wielu przypadkach może zwrócić niepożądane ścieżki; jednak w niektórych sytuacjach zwróci poprawne ścieżki.
    -   Wybrane krawędzie muszą tworzyć ciągłą krawędź *w widoku z góry*. Wybrane górne krawędzie mogą mieć różne wysokości, o ile łączą się w wspólnym punkcie (X, Y) - różne wysokości Z są akceptowalne w *niektórych**\*\**** przypadkach.
        **\*\***W niektórych przypadkach użytkownik będzie musiał uwzględnić w swoim zaznaczeniu prostą pionową krawędź łączącą dwie sąsiednie krawędzie o różnych wysokościach, które mają wspólny punkt (X, Y).
    -   Ponieważ wybierane są górne krawędzie, Głębokość końcowa dla operacji będzie musiała zostać ustawiona ręcznie.
    -   Podczas profilowania otwartych krawędzi, właściwość \Strona\ lub \Strona obróbki\ jest wewnętrznie wyłączona, chociaż prawdopodobnie będzie widoczna w oknie edytora zadań i na liście właściwości w zakładce Dane.
-   Podczas profilowania całego modelu (pełny kontur modelu) właściwość \Strona\ lub \Strona obróbki\ jest domyślnie ustawiona na \Na zewnątrz\. Użytkownik może dostosować ją w zależności od konfiguracji części.



## Właściwości

***Uwaga***: Nie wszystkie z tych właściwości są dostępne w edytorze okna zadań. Niektóre są dostępne tylko na karcie Dane w panelu Widok właściwości dla tej operacji.


{{TitleProperty|Podstawa}}

Uwaga: Zaleca się, aby nie edytować właściwości Umiejscowienie operacji ścieżki. W razie potrzeby należy raczej przesunąć lub obrócić model zadania CAM.

-    **Placement**: Ogólne umiejscowienie \[pozycja i rotacja\] obiektu - względem początku (lub początku kontenera obiektu nadrzędnego)

    -   
        **Angle**
        
        : Kąt w stopniach stosowany do rotacji obiektu wokół wartości właściwości Axis

    -   
        **Axis**
        
        : Oś (jedna lub więcej), wokół której rotuje obiekt, ustawiona w podwłaściwościach: x, y, z

        -   
            **X**
            
            : Wartość osi x

        -   
            **Y**
            
            : Wartość osi y

        -   
            **Z**
            
            : Wartość osi z

    -   
        **Position**
        
        : Pozycja obiektu, ustawiona w podwłaściwościach: x, y, z - względem początku (lub początku kontenera obiektu nadrzędnego)

        -   
            **X**
            
            : Wartość odległości osi x

        -   
            **Y**
            
            : Wartość odległości osi y

        -   
            **Z**
            
            : Wartość odległości osi z

-    **Label**: Nazwa obiektu nadana przez użytkownika (UTF-8)


{{TitleProperty|Głębokość}}

-    **Clearance Height**: Wysokość potrzebna do usunięcia zacisków i przeszkód

-    **Final Depth**: Końcowa głębokość narzędzia - najniższa wartość w osi Z

-    **Finish Depth**: Maksymalna ilość materiału usuniętego podczas ostatniego przejścia. Wysokość (grubość) ostatniego poziomu cięcia - *ustawiana dla lepszego wykończenia*.

-    **Safe Height**: Wysokość, powyżej której dozwolone są ruchy szybkie. (Bezpieczna wysokość szybkiego ruchu między lokalizacjami)

-    **Start Depth**: Początkowa głębokość narzędzia - *pierwsza głębokość cięcia w osi Z*

-    **Step Down**: Przyrostowa głębokość cięcia narzędzia podczas operacji

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:300px;"> 
*Wizualne odniesienie do właściwości ''(ustawień)'' głębokości*


{{TitleProperty|Ścieżka}}

-    **Active**: Ustaw na False, aby zapobiec generowaniu kodu

-    **Base**: Geometria podstawowa dla tej operacji

-    **Comment**: Opcjonalny komentarz do tej operacji

-    **Coolant Mode**: Tryb chłodzenia dla tej operacji

-    **Cycle Time**: Szacowany czas cyklu dla tej operacji

-    **Tool Controller**: Definiuje kontroler narzędzia używany w operacji

-    **User Label**: Etykieta przypisana przez użytkownika


{{TitleProperty|Profil}}

-    **Direction**: Kierunek, w jakim ścieżka narzędzia powinna otaczać część: W prawo (CW) lub W lewo (CCW)

-    **Expand Profile**: Rozszerz profil usuwania poza Dodatkowe odsunięcie.

-    **Expand Profile Step Over**: Ustaw procent przesunięcia, oparty na średnicy narzędzia.

-    **Handle Multiple Features**: Wybierz sposób przetwarzania wielu cech podstawowej geometrii.

-    **OffsetExtra**: Dodatkowa wartość, aby unikać ostatecznego profilu - dobra do wstępnego usuwania materiału.

-    **Process Circles**: Zaznacz, jeśli chcesz, aby ta operacja profilowania obejmowała również otwory cylindryczne, *które zazwyczaj są wiercone*.

-    **Process Holes**: Zaznacz, jeśli ta operacja profilowania powinna również przetwarzać otwory w podstawowej geometrii. **Uwaga**: Nie obejmuje to otworów cylindrycznych.

-    **Process Perimeter**: Zaznacz, jeśli ta operacja profilowania powinna również przetwarzać zewnętrzny obwód kształtów podstawowej geometrii.

-    **Side**: (Strona cięcia) Strona krawędzi, którą narzędzie powinno ciąć. Ma to znaczenie tylko wtedy, gdy \Use Compensation\ jest zaznaczone.

-    **Use Compensation**: Jeśli zaznaczone, operacja profilowania jest przesunięta o promień narzędzia. Kierunek przesunięcia jest określany przez stronę cięcia.


{{TitleProperty|Obrót}}

-    **Attempt Inverse Angle**: Automatycznie spróbuj użyć kąta odwrotnego, jeśli początkowa rotacja jest niepoprawna.

-    **Enable Rotation**: Włącz obrót, aby uzyskać dostęp do kieszeni lub obszarów nieprostopadłych do osi Z.

-    **Inverse Angle**: Odwróć kąt obrotu. ***Przykład:** zmień rotację z -22,5 na 22,5 stopnia.*

-    **Limit Depth To Face**: Wymuś głębokość Z wybranej powierzchni jako najniższą wartość dla ostatecznej głębokości. Wyższe wartości użytkownika dla ostatecznej głębokości będą przestrzegane.

-    **Reverse Direction**: Odwróć orientację operacji o 180 stopni.


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



## Układ edytora w oknie zadań 

*Opisy ustawień znajdują się w powyższej liście właściwości.* Ta sekcja to po prostu mapa układu ustawień w edytorze okien operacji.



### Geometria podstawowa 

-   **Dodaj**: Dodaje wybrane elementy, które powinny być bazą dla ścieżek.
-   **Usuń**: Usuwa wybrane elementy z listy Geometria podstawowa.
-   **Wyczyść**: Czyści wszystkie elementy na liście Geometria podstawowa.



### Głębokości

-    **Start Depth**
    

-    **Final Depth**
    

-    **Step Down**
    



### Wysokości

-    **Safe Height**
    

-    **Clearance Height**
    



### Operacja

-    **Tool Controller**
    

-    **Coolant Mode**
    

-    **Cut Side**
    

-    **Direction**
    

-    **Extra Offset**
    

-    **Enable Rotation**
    

-    **Use Start Point**
    

-    **Use Compensation**
    

-    **Process Holes**
    

-    **Process Circles**
    

-    **Process Perimeter**
    

**\*\*** Dostępność zmienia się w zależności od wyborów w sekcji Geometria podstawowa.



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
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Profile/pl
