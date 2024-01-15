---
 GuiCommand:
   Name: FEM PostFilterContours
   Name/pl: Filtr konturów
   MenuLocation: Wyniki , Filtr konturów
   Workbenches: FEM_Workbench/pl
   Version: 0.21
   SeeAlso: FEM_PostPipelineFromResult/pl, FEM_PostCreateFunctions/pl, FEM_tutorial/pl
---

# FEM PostFilterContours/pl



## Opis

Tworzy izokontury i izolinie w siatce wynikowej.

<img alt="" src=images/FEM_PostFilterContours_Example.png  style="width:400px;"> 
*Izokontury przedstawiające składową Y bezwzględnej gęstości strumienia magnetycznego<br> w i wokół miedzianego przewodu, wokół którego przepływa prąd elektryczny z częstotliwością 100 kHz.<br> Więcej informacji o tym modelu można znaleźć w sekcji 14 dokumentu [https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf Poradnik Elmer].*



## Użycie

1.  Zaznacz wcześniej utworzony [obiekt prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md).
2.  Utwórz filtr poprzez wciśnięcie przycisku **<img src="images/FEM_PostFilterContours.svg" width=16px> '''Filtr konturów'''** lub poprzez wybranie opcji **Wyniki → <img src="images/FEM_PostFilterContours.svg" width=16px> Filtr konturów** z menu.
3.  Dostosuj **Opcje wyświetlania wyników** jak dla [obiektu prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md). Może być konieczne ukrycie obiektu prezentacji graficznej wyników aby zobaczyć efekt filtra w podglądzie.
4.  W oknie dialogowym ustaw pole wyników i liczbę konturów.
5.  Wciśnij przycisk **OK** aby zakończyć polecenie.



## Opcje

Okno dialogowe oferuje następujące ustawieniaː

-   **Pole**: Pole wyników do wyświetlenia.
-   **Wektor**: Składowe wektora jeśli **Pole** jest wektorem.
-   **Liczba konturów**: Liczba konturów do utworzenia. **Uwaga:** w zależności od geometrii, utworzona liczba konturów może być wyższa niż podana. Wynika to z algorytmu tworzenia konturów. Jednak w przypadku geometrii 2D i prostych 3D, liczba konturów powinna się zgadzać.
-   **Bez koloru**: Nie stosuj koloru do konturów.

**Uwaga**: **Pole** może być ustawione tylko jeśli funkcja filtra istnieje i została zastosowana przy pomocy <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:16px;"> [Zastosuj zmiany](FEM_PostApplyChanges/pl.md). Alternatywnie, możesz ponownie otworzyć okno dialogowe filtra.



## Informacja o rozmiarze plików 

Ustawienie filtra konturów może znacząco zwiększyć rozmiar pliku. Powodem jest to, że algorytm musi skopiować [obiekt prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md). Pojedynczy kontur nie wymaga całej siatki i algorytm wymaga tylko połowy miejsca przechowywania obiektu prezentacji wyników do utworzenia konturu. Ale to będzie wzrost rozmiaru dla każdego konturu. Przykładowo, jeśli rozmiar przechowywania obiektu prezentacji wyników to 1 MB, dodanie filtra konturów z 10 konturami będzie prowadziło do zwiększenia rozmiaru pliku o 5 MB.

Rozmiar przechowywania obiektu prezentacji graficznej wyników zależy od używanej siatki. Im ona gęstsza, tym większy rozmiar obiektu prezentacji graficznej wyników. Zatem należy być ostrożnym jeśli używa się gęstych siatek i dużej liczby konturów.

Jeśli używasz konturów tylko na części siatki, np. gdy masz filtr odcięcia, wtedy utwórz filtr konturów na filtrze odcięcia zamiast na obiekcie prezentacji graficznej wyników. Jeśli potrzebny Ci jest cały obiekt prezentacji graficznej wyników, zacznij od kilku konturów i krok po kroku zwiększaj ich liczbę aż rozmiar pliku będzie nadal akceptowalny podczas gdy wizualizacja będzie taka, jak oczekiwana.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterContours/pl
