# Navigation Cube/pl
{{TOCright}}

## Wprowadzenie

**Kostka nawigacyjna** daje wizualną informację o orientacji ujęcia widoku kamery w bieżącym [widoku 3D](3D_view/pl.md) i może być użyta do jej zmiany. Domyślnie jest ona widoczna i znajduje się w prawym górnym rogu okna.

Kostka nawigacyjna została zaktualizowana w wersji 0.20 programu FreeCAD i reszta tej strony opisuje tę wersję. W wersji 0.19 programu FreeCAD główne zachowanie jest takie samo, ale niektóre funkcje nie są dostępne.

![](images/Navigation_Cube_Example.png )

Kostka nawigacyjna składa się z kilku części:

-   [Główny sześcian nawigacyjny](#G.C5.82.C3.B3wny_sze.C5.9Bcian_nawigacyjny.md).
-   [Strzałki kierunkowe](#Strza.C5.82ki_kierunkowe.md).
-   [Przycisk widoku do tyłu](#Przycisk_widoku_do_ty.C5.82u.md) *(u góry po prawej)* {{Version/pl|0.20}}
-   [Menu mini-kostki](#Menu_mini-kostki.md) *(na dole po prawej)*.
-   Wskaźniki osi X, Y i Z

Wszystkie elementy, z wyjątkiem wskaźników osi, można klikać.

## Użycie

### Główny sześcian nawigacyjny 

Główny sześcian posiada 26 ścian: 6 ścian głównych, 12 prostokątnych ścian brzegowych ({{Version/pl|0.20}}) i 8 ścian narożnych. Kliknięcie dowolnej z nich spowoduje zmianę ujęcia widoku kamery tak, aby jej kierunek był prostopadły do wybranej ściany.

### Strzałki kierunkowe 

Istnieje sześć strzałek kierunkowych: cztery trójkątne groty, jedna na górze, na dole, w lewo i w prawo; oraz dwie zakrzywione strzałki. Kliknięcie jednej z trójkątnych strzałek spowoduje obrót [widoku 3D](3D_view/pl.md) wokół linii prostopadłej do kierunku strzałki. Kliknięcie zakrzywionej strzałki spowoduje obrót [widoku 3D](3D_view/pl.md) wokół kierunku widoku.

### Przycisk widoku do tyłu 

Kliknięcie okrągłego przycisku w prawym górnym rogu kostki nawigacyjnej spowoduje obrócenie [widoku 3D](3D_view/pl.md) o 180° wokół pionowej osi widoku.

### Menu mini-kostki 

Kliknięcie małego sześcianu w prawym dolnym rogu Kostki nawigacji spowoduje wyświetlenie menu z następującymi opcjami:

-    **[Ortogonalny](Std_OrthographicCamera/pl.md)**: przełącza na widok ortogonalny.

-    **[Perspektywa](Std_PerspectiveCamera/pl.md)**: przełącza na widok perspektywiczny.

-    **[Isometryczny](Std_ViewIsometric/pl.md)**: przełącza na widok izometryczny.

-    **[Przybliż i dopasuj](Std_ViewFitAll/pl.md)**: powiększa i pochyla ujęcie widoku tak, aby wszystkie widoczne obiekty zmieściły się w aktualnym kadrze.

## Dostosowywanie

### Przesuwanie Kostki Nawigacyjnej 

Możesz przesunąć całą strukturę sterowania kostki nawigacyjnej w inne miejsce obrazu w oknie z widokiem 3D, naciskając myszą w dowolnym miejscu głównego sześcianu i przeciągając. Struktura zacznie się przesuwać dopiero po przesunięciu kursora poza jedną z krawędzi głównego sześcianu.

### Ustawienia

Sześcian nawigacyjny jest konfigurowalny, włącznie z dostosowaniem jego rozmiaru: **Edycja → Preferencje → Wyświetlanie → Nawigacja → Kostka nawigacyjna**. Zobacz [Edytor preferencji](Preferences_Editor/pl#Nawigacja.md).

### Opcje zaawansowane 

Zewnętrzne narzędzie [Menu kostki nawigacyjnej](Interface_Customization/pl#Menu_kostki_nawigacyjnej.md) zapewnia łatwiejszy dostęp do kilku bardziej zaawansowanych opcji dostosowywania.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/pl
