---
- GuiCommand:/pl
   Name:PartDesign Boolean
   Name/pl:Projekt Części: Operacja logiczna
   MenuLocation:Projekt Części → Operacja logiczna
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
---

# PartDesign Boolean/pl



## Opis

**Operacja logiczna** środowiska Projekt Części importuje jedną lub więcej [zawartości](PartDesign_Body/pl.md) lub [klonów](PartDesign_Clone/pl.md) *(oznaczonych jako \"zawartość narzędziowa\")* do aktywnej bryły Projekt Części i stosuje operację logiczną *(połączenie, przecięcie lub część wspólna)*.

![](images/PartDesign_Boolean_example.png )



*Po lewej: aktywna zawartość ''(A)'' z bryłami narzędziowymi ''(B)'' i ''(C)''. Po prawej: wynik po wykonaniu operacji przecięcia.*



## Użycie

1.  [Aktywuj zawartość](PartDesign_Body/pl#Pojedyncza_ci.C4.85g.C5.82a_bry.C5.82a.md), która ma otrzymać cechę operacji logicznej. \'\'*\' Uwaga*: Ważne jest, aby ani aktywna zawartość, ani żadna z zawartych w niej cech nie były wybrane!\'\'
2.  Naciśnij przycisk **<img src="images/PartDesign_Boolean.svg" width=16px> [Operacja logiczna](PartDesign_Boolean/pl.md)**.
3.  W **Parametrach logicznych** kliknij przycisk **Dodaj zawartość**. Aktywna bryła tymczasowo znika z okna [widoku 3D](3D_view/pl.md), co ułatwia wybór zawartości dla narzędzia.
4.  W w oknie widoku 3D wybierz zawartość, którą chcesz wykorzystać w funkcji logicznej. Powtórz czynność, aby dodać więcej zawartości.
5.  Wybierz typ operacji logicznej w menu rozwijanym *(Scalenie, Wytnij lub Część wspólna)*.
6.  Kliknij przycisk **OK**.

Alternatywnie można wybrać jedną lub więcej brył przed użyciem przycisku Operacji logicznej, zostaną one dodane automatycznie.



## Opcje

-   **Scalenie:** łączy bryłę lub bryły narzędzia z bryłą aktywną.
-   **Wytnij:** odejmuje bryłę lub bryły narzędzia od bryły aktywnej.
-   **Część wspólna:** wycina obszar wspólny z wybranej zawartości, lub kilku zawartości z aktywną zawartością
-   Naciśnij przycisk **Usuń zawartość**, aby usunąć zawartość, zaznaczając ją w oknie [widoku 3D](3D_view/pl.md).



## Właściwości

-    **Typ**: ustawia operację logiczną *(Scalenie, Wytnij, Część wspólna)*

-    **Etykieta**: nazwa nadana operacji, nazwę tę można dowolnie zmieniać.

-    **Grupa**: lista zawartości będących narzędziami.

-    **Wyświetlanie**: ustawia wyświetlanie pomiędzy dwoma trybami:

    -   Wynik *(domyślnie)*: wyświetla wynik działania funkcji logicznej. W tym trybie Zawartości narzędzi nie mogą być wyświetlane w stanie oryginalnym, nawet jeśli ich widoczność jest włączona.
    -   Narzędzia: wyświetla Zawartości narzędzi w ich oryginalnym stanie. Tryb ten jest przydatny, gdy Zawartości narzędzi muszą być edytowane lub używane w późniejszych operacjach.

-    **Wybieralne**: możliwe wartości {{true/pl}} lub {{false/pl}}. Jeśli ustawiono wartość false, element nie może być wybrany w oknie widoku 3D.

-    **Widoczność**: możliwe wartości {{true/pl}} lub {{false/pl}}. Przełącza widoczność elementu w oknie widoku 3D.



## Ograniczenia

-   Aby narzędzie Część wspólna mogło pracować z więcej niż jedną Zawartością jako narzędzia, muszą one przecinać się nawzajem wraz z aktywnym korpusem.
-   Zawartości będące narzędziami przyjmują jako lokalny początek położenia aktywną zawartość. Jeśli aktywna zawartość nie znajduje się w punkcie *(0,0,0)* w globalnym układzie współrzędnych, umieszczenie zawartości narzędzi musi być względne w stosunku do aktywnej bryły. Łatwiejsze może być pozostawienie położenia aktywnej zawartości na początku przed zastosowaniem cechy logicznej niż zmiana jej położenia.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Boolean/pl
