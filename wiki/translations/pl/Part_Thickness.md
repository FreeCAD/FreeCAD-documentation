---
- GuiCommand:
   Name:Part Thickness
   Name/pl:Część: Grubość
   MenuLocation:Część → Grubość
   Workbenches:[Środowisko pracy Część](Part_Workbench/pl.md)
   SeeAlso:[Odsunięcie](Part_Offset/pl.md)
---

# Part Thickness/pl



## Opis

Narzędzie <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Grubość](Part_Thickness/pl.md) pracuje na kształcie bryły i przekształca ją w pusty obiekt, nadając każdej z jego ścian określoną grubość. Na niektórych bryłach pozwala to znacznie przyspieszyć pracę i uniknąć tworzenia wyciągnięć i kieszeni.



## Użycie

1.  Utwórz bryłę.
2.  Wybierz jedna albo więcej ścian.
3.  Kliknij w przycisk narzędzia **<img src="images/Part_Thickness.svg" width=16px> '''Część: Grubość'''**.
4.  Ustaw wybrane parametry *(zobacz [Opcje](#Opcje.md))*.
5.  Kliknij w przycisk **OK** aby potwierdzić, utworzyć operację i opuścić funkcję.
6.  W tabeli Właściwości w razie potrzeby można dostosować parametry.



## Opcje

-   **Grubość**: Grubość ścianki obiektu wynikowego, należy ustawić żądaną wartość.
    -   Dodatnia wartość spowoduje przesunięcie ścianek na zewnątrz.
    -   Ujemna wartość przesunie ściany do wewnątrz.
-   **Tryb pracy**.
    -   *Powłoka*: Wybierz tę opcję, jeśli chcesz dostać przedmiot jak wazon, bez głowy, ale z dnem.
    -   *Rura*: Wybierz tę opcję, jeśli chcesz uzyskać obiekt taki jak rura, bez głowy i bez dna. W tym przypadku wygodne może być wybranie ścian, które mają zostać usunięte przed uruchomieniem narzędzia. Pomocne mogą być przyciski z predefiniowanymi widokami lub klawisze numeryczne.
    -   *Obie strony*:
-   **Typ dołączenia**.
    -   *Wzdłuż łuku*: usuwa zewnętrzne krawędzie i tworzy zaokrąglenie o promieniu równym zdefiniowanej grubości
    -   *Stycznie*:
    -   *Przecięcie*:
-   **Przecięcie**:
-   **Samoprzecięcie**: Włącza autoprzecięcie.
-   ****Ściany****: Wybierz ściany, które mają zostać usunięte, a następnie kliknij przycisk **Gotowe**.
-   **Aktualizuj widok**: Automatyczna aktualizacja widoku w czasie zmiany parametrów.



## Uwagi

-   Obiekty typu [odnośnik](App_Link/pl.md) powiązane z odpowiednimi typami obiektów mogą być również używane jako kształty i do określania osi. {{Version/pl|0.20}}

Złożone kształty mogą dawać dziwaczne, trudne do przewidzenia rezultaty. Należy dokładnie sprawdzić wynikowy kształt i zapisać pracę przed zastosowaniem operacji.



## Odnośniki

Dobry przykład korzystania z tego narzędzia można odnaleźć na forum:[Re: Pomoc przy projektowaniu prostej obudowy](http://forum.freecadweb.org/viewtopic.php?f=3&t=3766&p=29741&hilit=enclosure#p29547)



## Przykłady

**Wydrążony cylinder**

1.  Utwórz **<img src="images/Part_Cylinder.svg" width=16px> [Walec](Part_Cylinder/pl.md)** o promieniu 10mm i wysokości 20mm,
2.  Wybierz górną i dolną powierzchnię cylindra,
3.  Kliknij na przycisk **<img src="images/Part_Thickness.svg" width=16px> Grubość** *(nie trzeba zmieniać domyślnych ustawień)* i naciśnij przycisk **OK**.

Uwagi:

-   Dla tego kształtu, rozważ użycie narzędzia **<img src="images/Part_Tube.svg" width=16px> [Rura](Part_Tube/pl.md)**.
-   Wybierz tylko górną powierzchnię cylindra, aby utworzyć zbiornik.

![](images/ThicknessEsempio1.png )

![](images/ThicknessEsempio2.png )

**Obudowa**

![](images/ThicknessEsempio3.png )

![](images/ThicknessEsempio4.png )



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Thickness/pl
