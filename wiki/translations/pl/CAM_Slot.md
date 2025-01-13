---
 GuiCommand:
   Name: CAM Slot
   Name/pl: CAM: Rowek
   MenuLocation: CAM , Rowek
   Workbenches: CAM_Workbench/pl
   Version: 0.19
---

# CAM Slot/pl



## Opis

Narzędzie <img alt="" src=images/CAM_Slot.svg  style="width:24px;"> [Rowek](CAM_Slot/pl.md) tworzy prostą operację rowkowania korzystając z różnych metod wejściowych.

Wejścia obejmują:

-   wskazanie jednej lub więcej ścian lub krawędzi.
-   wskazanie dwóch wierzchołków.
-   wprowadzenie dwóch niestandardowych punktów.

Obiekt CAM Slot jest dodawany jako część <img alt="" src=images/CAM_Job.svg  style="width:24px;"> [Zadania CAM](CAM_Job/pl.md).



## Użycie

1.  Wybierz geometrię odniesienia na modelu:
    -   jedną lub więcej powierzchni lub krawędzi.
    -   dwa wierzchołki.
    -   ***nic*** aby użyć dwóch niestandardowych punktów wprowadzonych w Widoku właściwości zakładki Dane: Custom Point1 i Custom Point2.
2.  Wywołaj polecenie Rowek na jeden z kilku sposobów:
    -   Naciskając przycisk **<img src="images/CAM_Slot.svg" width=24px> [Rowek](CAM_Slot/pl.md)** na pasku narzędzi.

#\* Używając opcji ** CAM** → **<img src="images/CAM_Slot.svg" width=24px> [Rowek](CAM_Slot/pl.md)** z górnego menu.

1.  Dostosuj żądane właściwości. Opisy dostępnych właściwości znajdują się poniżej.



#### Uwagi dotyczące użycia 

-   Wszystkie rowki:
    -   Zarówno początek, jak i koniec ścieżki rowka mogą być wydłużane lub skracane. Użyj właściwości \Extend Path Start\ i \Extend Path End\.
    -   Użyj właściwości \Layer Mode\, aby wyciąć rowek w trybie \Single-pass\ na ostateczną głębokość lub w trybie \Multi-pass\ z użyciem dostępnej właściwości \Step Down\.
    -   Przełącz właściwość \Reverse Direction\, aby odwrócić kierunek ścieżki cięcia.

-   Rowki liniowe:
    -   Obecnie brak możliwości przesunięcia rowków liniowych bocznie (równolegle do ścieżki ruchu). ***Przykład:*** Jeśli średnica narzędzia jest mniejsza niż szerokość obszaru rowka, który chcesz wyczyścić. Obecne działanie tej operacji polega na stworzeniu zestawu ścieżek w płaszczyźnie wzdłuż osi wyznaczonego rowka, co skutkuje niepełnym usunięciem objętości rowka. Niektórzy użytkownicy chcieliby, aby operacja tworzyła wiele ścieżek przesuniętych bocznie, aby oczyścić cały obszar rowka; obecnie nie jest to bezpośrednio możliwe, ale można to osiągnąć, używając \"Custom Points\", patrz \"Frezowanie pionowych ścian\" poniżej. Alternatywnie, użyj operacji Pocket do takiego czyszczenia.
    -   Utwórz niestandardowy rowek liniowy, używając właściwości \Custom Point1\ i \Custom Point2\ bez wyboru geometrii. ***Przykład:*** Zainicjuj operację Rowek w GUI i kliknij \OK\, aby zapisać. Teraz zlokalizuj i edytuj właściwości \Custom Point1\ i \Custom Point2\ w zakładce Dane nowo utworzonej operacji Rowek. Ponownie przelicz operację, aby zaktualizować ścieżkę.

-   Frezowanie pionowych ścian:
    -   Większość narzędzi CAM nie jest w stanie stworzyć ścieżki na pojedynczej pionowej płaszczyźnie, ponieważ rzutowanie na płaszczyznę poziomą ma zerową powierzchnię (wewnętrzne ograniczenie). Operacja Rowek umożliwia to, wybierając \"Punkty niestandardowe\", które definiują linię równoległą do pionowej płaszczyzny oraz odpowiednie parametry głębokości.

-   Rowki łukowe/cylindryczne:
    -   Tworzenie rowków łukowych/cylindrycznych:
        1.  Należy wybrać jeden dolny łuk rowka. Spowoduje to utworzenie ścieżki bezpośrednio na krawędzi wybranego łuku.
        2.  Następnie trzeba edytować właściwość \Extend Radius\ w zakładce Dane operacji. Używając edytora wyrażeń, ustaw ją na wartość \OpToolDiameter / 2.0\ lub jej wersję ujemną \OpToolDiameter / -2.0\, w zależności od tego, czy wybrano łuk wewnętrzny czy zewnętrzny rowka.
        3.  Przelicz ponownie operację.
        4.  Pamiętaj, że jeśli średnica narzędzia nie jest równa szerokości rowka, ścieżka \'**\'nie**\' będzie znajdować się w prawidłowej lokalizacji. W takim przypadku dostosuj wartość we właściwości \Extend Radius\, o której mowa powyżej.
    -   Obecnie użytkownicy nie mogą tworzyć niestandardowej ścieżki łukowej/cylindrycznej. Należy dodać trzecią właściwość \Custom Center\ oraz dodatkowe modyfikacje w kodzie źródłowym.



## Właściwości

***Uwaga***: Nie wszystkie z tych właściwości są dostępne w edytorze okna zadań. Niektóre są dostępne tylko na karcie Dane w panelu Widok właściwości dla tej operacji.


{{TitleProperty|Podstawa}}

Uwaga: Zaleca się, aby nie edytować właściwości Umiejscowienie operacji ścieżki. W razie potrzeby należy raczej przesunąć lub obrócić model zadania CAM.

-    **Placement**: Ogólne umiejscowienie \[pozycja i rotacja\] obiektu względem początku (lub początku kontenera obiektów nadrzędnych)

    -   
        **Angle**
        
        : Kąt w stopniach zastosowany do rotacji obiektu wokół wartości właściwości Axis

    -   
        **Axis**
        
        : Oś (jedna lub więcej), wokół której należy obrócić obiekt, ustawiona w podwłaściwościach: X, Y, Z

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
        
        : Pozycja obiektu, ustawiona w podwłaściwościach: X, Y, Z - względem początku (lub początku kontenera obiektów nadrzędnych)

        -   
            **X**
            
            : Wartość odległości osi X

        -   
            **Y**
            
            : Wartość odległości osi Y

        -   
            **Z**
            
            : Wartość odległości osi Z

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


{{TitleProperty|Rowek}}

-    **Custom Point1**: Wprowadź niestandardowy punkt startowy dla ścieżki rowka.

-    **Custom Point2**: Wprowadź niestandardowy punkt końcowy dla ścieżki rowka.

-    **Cut Pattern**: Ustaw wzór geometryczny czyszczenia do użycia w operacji.

-    **Extend Path End**: Dodatnia wartość wydłuża koniec ścieżki, ujemna skraca.

-    **Extend Path Start**: Dodatnia wartość wydłuża początek ścieżki, ujemna skraca.

-    **Extend Radius**: Dla łuków/kręgów, przesuwanie promienia dla ścieżki.

-    **Layer Mode**: Wykonaj operację w jednym przejściu na głębokości lub w wielu przejściach do końcowej głębokości.

-    **Path Orientation**: Wybierz orientację ścieżki względem wybranych cech.

-    **Reference1**: Wybierz punkt do użycia na pierwszej wybranej cechy.

-    **Reference2**: Wybierz punkt do użycia na drugiej wybranej cechy.

-    **Reverse Direction**: Włącz, aby odwrócić kierunek cięcia ścieżki rowka.


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

*Opisy ustawień znajdują się na powyższej liście właściwości*.

Ta sekcja jest po prostu mapą układu ustawień w edytorze okien dla operacji.



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

-    **Tool Controller**: Narzędzie i jego ustawienia używane w tej operacji.

-    **Coolant Mode**: Tryb chłodzenia dla tej operacji.

-    **Start Reference ****: Wybierz punkt do użycia na pierwszym wybranym elemencie.

-    **End Reference ****: Wybierz punkt do użycia na drugim wybranym elemencie.

-    **Extend Path End**: Dodatnia wartość wydłuża koniec ścieżki, ujemna skraca.

-    **Extend Path Start**: Dodatnia wartość wydłuża początek ścieżki, ujemna skraca.

-    **Layer Mode**: Zakończ operację w jednym przejściu na głębokości lub w wielu przejściach do ostatecznej głębokości.

-    **Path Orientation ****: Wybierz orientację ścieżki względem wybranych cech.

-    **Reverse Direction**: Włącz, aby odwrócić kierunek cięcia ścieżki rowka.

**\*\*** Widoczność zmienia się w zależności od wybranej geometrii podstawowej.



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
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Slot/pl
