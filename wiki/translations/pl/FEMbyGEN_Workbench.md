# <img alt="Ikonka FreeCAD dla środowiska pracy FEMbyGEN" src=images/FEMbyGEN.svg  style="width:64px;"> FEMbyGEN Workbench/pl






## Wprowadzenie

Środowisko pracy **FEMbyGEN** jest dodatkiem do FreeCAD. Zapewnia prosty interfejs do wyboru najlepszego rozwiązania, pokazując zachowanie strukturalne projektów na ekranie do analizy parametrycznej i wielu sytuacji obciążenia.

<img alt="" src=images/Generative_Design.png  style="width:512px;">



### Zamierzony przepływ pracy 

1.  Kliknij przycisk **Initiate**, aby zdefiniować parametry analizy parametrycznej.
2.  Za pomocą przycisku **Alias** dopasuj wielkość i nazwę parametrów.
3.  Skojarz [Arkusz kalkulacyjny](Spreadsheet_Workbench.md) z modelem.
4.  Skonfiguruj model(e) analizy za pomocą środowiska pracy [MES](FEM_Workbench.md).
5.  Przełącz się z powrotem do środowiska **FEMbyGEN** i za pomocą przycisku **Generate** utwórz wszystkie sekwencje.
6.  Kliknij przycisk **FEA** i Start FEA, aby uruchomić symulacje.
7.  Możesz sprawdzić pliki symulacji, klikając wiersze powiązanej sekwencji.
8.  Kliknij przycisk **Results**, aby pobrać wyniki do pliku głównego.
9.  Podsumowanie wszystkich wyników przypadków obciążeń będzie również dostępne w sekcji Wyniki oknie [Widoku drzewa](Tree_view/pl.md).
10. Jeśli chcesz uzyskać rekomendację dla swojego projektu zamiast analizy parametrycznej, kliknij **CreatGeo**, aby zdefiniować warunki brzegowe projektu, takie jak obciążenia, podpory, geometrie ochronne. Następnie zostanie utworzona ramka otaczająca, a następnie zoptymalizowana w celu zaproponowania najbardziej odpowiedniej geometrii. Możesz użyć suwaka, aby zobaczyć poprzednie sugestie.
11. Kliknij **Topology**, aby uruchomić symulację topologii dla całych generacji lub tylko pliku ze zdefiniowaną analizą MES. Na ekranie można zdefiniować parametry optymalizacji, a następnie wyświetlić wyniki. Dolny suwak pomoże zobaczyć postęp optymalizacji topologii.



### Cechy

-   Parametryczna analiza MES.
-   Obsługa wielu przypadków obciążeń.
-   Podsumowanie wszystkich wyników w tabeli.
-   Sortowanie wyników według wagi wyjściowej.
-   Sumowanie wszystkich przypadków obciążeń.
-   Sugestie dotyczące geometrii na podstawie warunków brzegowych.
-   Optymalizacja topologii.



### Funkcje obsługiwane w przyszłości 

-   Implementacja inna niż metoda topologii BESO.



### Ograniczenia

-   Działa wyłącznie z solwerem CalculiX.



## Instalacja



## Menadżer dodatków 

FEMbyGEN może być łatwo zainstalowany w FreeCAD za pomocą <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) z menu **Przybory → Menadżer dodatków**.

FEMbyGEN jest w trakcie aktywnego rozwoju i będzie często otrzymywać nowe funkcje. W związku z tym należy go regularnie aktualizować za pomocą menu **Przybory → Menedżer dodatków**.

Kod FEMbyGEN jest hostowany i rozwijany w serwisie [GitHub](https://github.com/Serince/FEMbyGEN).



### Podręcznik

Więcej informacji na ten temat znajduje się na stronie [Jak zainstalować dodatkowe środowiska pracy](How_to_install_additional_workbenches/pl.md).



### Wymagania wstępne 

-   FreeCAD w wersji 0.19 lub nowszej.



## Bibliografia

-   Autor: Serdar Ince, Ögeday Yavuz, Rahul Jhuree
-   Kod źródłowy: [FEMbyGEN na GitHub.com](https://github.com/Serince/FEMbyGEN)
-   Forum FreeCAD: <https://forum.freecadweb.org/viewtopic.php?p=626306>
-   Zgłaszanie błędów: Prosimy o zgłaszanie błędów na stronie [FEMbyGEN na GitHub](https://github.com/Serince/FEMbyGEN/issues)



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > FEMbyGEN Workbench/pl
