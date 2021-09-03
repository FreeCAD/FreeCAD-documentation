---
- GuiCommand:/pl
   Name:Sketcher ValidateSketch
   Name/pl:Szkicownik: Sprawdź poprawność szkicu
   MenuLocation:Sketch → Sprawdź poprawność szkicu ...
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md), [Projekt części](PartDesign_Workbench/pl.md)
   SeeAlso:[Szkicownik: Wiązanie zbieżności punktów](Sketcher_ConstrainCoincident/pl.md), [Topological naming problem](Topological_naming_problem.md)
---

## Opis

Narzędzie **Sprawdzanie poprawności szkicu** może być używane do analizowania i naprawiania szkicu, który nie jest już edytowalny lub ma nieprawidłowe wiązania, lub do dodawania brakujących [zbieżności punktów](Sketcher_ConstrainCoincident/pl.md) do szkicu utworzonego z importowanej geometrii, takiej jak pliki DXF. Może być również przydatny do zlokalizowania brakującej zbieżności w rodzimym szkicu, który generuje błąd **nie można zatwierdzić uszkodzonej powierzchni** podczas próby zastosowania elementu ze środowiska Projekt części.

![](images/Sketcher_ValidateSketch_taskpanel.png ) *Panel zadań sprawdzania poprawności w środowisku pracy Szkicownik*

## Użycie

1.  Tego narzędzia nie można użyć na szkicu, który jest w trybie edycji. W razie potrzeby wyjdź z trybu edycji, wykonując jedną z następujących czynności:
    -   Naciśnij przycisk **<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [Opuść szkic](Sketcher_LeaveSketch/pl.md)**.
    -   Naciśnij przycisk **Zamknij** w górnej części [panelu zadań](Task_panel/pl.md).
    -   Użyj skrótu klawiaturowego: **Esc** *(jeśli opcja jest włączona w [Preferencjach szkicownika](Sketcher_Preferences/pl#Informacje_og.C3.B3lne.md))*.
2.  W [widoku drzewa](Tree_view/pl.md) wybierz szkic, który ma zostać sprawdzony, lub kliknij jedną z krawędzi w oknie [widoku 3D](3D_view/pl.md).
3.  Aby otworzyć narzędzie sprawdzania poprawności szkicu, wykonaj jedną z następujących czynności:
    -   Wybierz z menu opcję **Sketch → Validate sketch...**.
    -   Naciśnij przycisk **<img src=images/Sketcher_ValidateSketch.svg style="width:16px">. [Sprawdź poprawność szkicu](Sketcher_ValidateSketch/pl.md)** *(nie jest dostępny w środowisku pracy [Projekt części](PartDesign_Workbench/pl.md))*.
4.  Zobacz [Opcje](#Opcje.md) poniżej, aby zapoznać się z dostępnymi operacjami.
5.  Po zakończeniu naciśnij przycisk **Zamknij**.

## Opcje

### Brakujące zbieżności 

Wyszukuje brakujące zbieżności dla nakładających się wierzchołków i dodaje je. Wciśnij przycisk **Znajdź**, pojawi się okno dialogowe informujące o liczbie znalezionych brakujących zbieżności, będą one widoczne w oknie widoku 3D jako żółte krzyżyki. Naciśnij przycisk **OK**, aby zamknąć okno dialogowe, a następnie naciśnij przycisk **Napraw**, aby dodać brakujące zbieżności.

W razie potrzeby w rozwijanym polu zdefiniować większą wartość tolerancji.

Naciśnij ** Podświetl otwarte wierzchołki **, aby podświetlić wierzchołki, które nie spełniają tej tolerancji.

Tolerancja ta jest również używana przez proces **Znajdź** / **Napraw**.

Pozostaw pole wyboru \"Ignoruj geometrię konstrukcji\" zaznaczone, aby w analizie nie uwzględniać geometrii konstrukcyjnej.

### Nieprawidłowe wiązania 

Sprawdza obecność zniekształconych wiązań.

Na przykład, jeśli istnieje wiązanie Okrąg-Linia-Styczna, ale odwołuje się ono do dwóch linii, jest uważane za niepoprawne.

*(To czasami zdarza się z powodu [problemu nazewnictwa topologicznego](Topological_naming_problem/pl.md), tj. zewnętrzna geometria zmienia typ)*.

Dokonuje również dodatkowych weryfikacji, np. pod kątem występowania nieważnych linków.

### Zdegenerowana geometria 

Zdegenerowana geometria może być wynikiem działania solvera w szkicu.

Na przykład, jeśli linia jest zmuszona do skrócenia długości, tak aby stała się prawie punktem.

Inne przykłady: linia o zerowej długości lub okrąg/łuk o zerowym promieniu.

### Odwrócona geometria zewnętrzna 

Odwrócona geometria zewnętrzna może się pojawić, ponieważ obsługa odwróconej geometrii została zmieniona mniej więcej w wersji 0.15.

Ten proces może być pomocny, jeśli szkice z zewnętrzną geometrią nie dają się rozwiązać z powodu tych zmian.

### Blokowanie orientacji wiązania 

Realizowane są wiązania styczne i prostopadłe *(przez punkt)*.

Wewnętrznie działają one poprzez wiązanie kąta pomiędzy wektorami stycznymi. Na przykład w przypadku wiązania stycznego, kąt może wynosić 0 lub 180 stopni *(wektory współkierunkowe lub przeciwne)*. Rzeczywisty kąt jest zapamiętany w danych wiązania *(orientacja wiązania zablokowana)*, to chroni przed odwróceniem. Ale kąt może być wymazany *(orientacja wiązania odblokowana)* lub zaktualizowany; te narzędzia właśnie to robią.

Mechanizm blokujący zazwyczaj działa dobrze i narzędzie to nie powinno być potrzebne. **Powinno być używane tylko po wykonaniu kopii zapasowej otwartego dokumentu.**.





{{Sketcher Tools navi

}}  
