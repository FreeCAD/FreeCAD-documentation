---
 GuiCommand:
   Name: Std Import
   Name/pl: Std: Importuj
   MenuLocation: Plik , Importuj ...
   Workbenches: wszystkie
   Shortcut: **Ctrl** + **I**
   SeeAlso: Std_Open/pl, Import_Export/pl, Import_Export_Preferences/pl
---

# Std Import/pl



## Opis

Polecenie **Importuj** importuje geometrię z innego formatu pliku do aktywnego dokumentu. Obsługiwanych jest wiele formatów plików, a dla niektórych formatów istnieje wiele opcji importu. Zobacz stronę [Import eksport](Import_Export/pl.md), aby uzyskać więcej informacji.


{{Version/pl|0.21}}

: Po wybraniu formatu obrazu polecenie utworzy [Płaszczyznę obrazu](#Płaszczyzna_obrazu.md).



## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Wybierz z menu opcję **Plik → <img src="images/Std_Import.svg" width=16px> Importuj ...**.
    -   Użyj skrótu klawiaturowego: **Ctrl** + **I**.
2.  Opcjonalnie wybierz odpowiedni format pliku w oknie dialogowym.
3.  Wybierz plik.
4.  Naciśnij przycisk **Otwórz**.



## Opcje

-   Naciśnij przycisk **Esc** lub przycisk **Anuluj** aby przerwać wykonywanie polecenia.



## Uwagi

-   Aby przekształcić zaimportowany obiekt [siatki](Mesh_Workbench.md) w bryłę, zobacz poradnik [Importowanie plików STL lub OBJ](Import_from_STL_or_OBJ/pl.md).
-   Aby zaimportować obiekt do nowego dokumentu można użyć polecenia [Otwórz](Std_Open/pl.md).
-   Niektóre środowiska pracy mają dodatkowe polecenia importu. Zobacz stronę: [Import Export](Import_Export/pl.md).



## Ustawienia

-   Zobacz stronę: [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl.md).
-   Zapamiętana jest ostatnio używana lokalizacja pliku: **Przybory → Edycja parametrów ... → BaseApp → Preferences → General → FileOpenSavePath**.
-   Zapamiętany jest ostatni używany filtr eksportu: **Przybory → Edycja parametrów ... → BaseApp → Preferences → General → FileExportFilter**.



## Płaszczyzna obrazu 

Płaszczyzna obrazu to płaska reprezentacja obrazu w oknie [widoku 3D](3D_view/pl.md). Może być na przykład używana podczas tworzenia modelu na podstawie zdjęć istniejącego obiektu.

Domyślnie płaszczyzna obrazu jest umieszczana na globalnej płaszczyźnie XY. Początkowy rozmiar płaszczyzny obrazu jest obliczany przy użyciu rozdzielczości 96 px/cal.



### Edycja

1.  Aby edytować płaszczyznę obrazu, wykonaj jedną z poniższych czynności:
    -   Kliknij dwukrotnie Płaszczyznę obrazu w oknie [Widoku drzewa](Tree_view/pl.md).
    -   Kliknij prawym przyciskiem myszy Płaszczyznę obrazu w oknie Widoku drzewa i wybierz z menu kontekstowego **<img src="images/Image-scaling.svg" width=16px> Modyfikuj obraz ...
**
2.  Jeśli płaszczyzna obrazu nie jest równoległa do płaszczyzny XY, XZ lub YZ globalnego układu współrzędnych, zostanie ona wyrównana do płaszczyzny XY.
3.  Otworzy się panel zadań **Ustawienia płaszczyzny obrazu**:
    -   Wybierz płaszczyznę globalnego układu współrzędnych **Płaszczyzna XY**, **Płaszczyzna XZ** lub **Płaszczyzna YZ**.
    -   Zaznacz **Odwróć kierunek**, aby obrócić płaszczyznę obrazu o 180°. Oś obrotu zależy od wybranej płaszczyzny. Dla płaszczyzny XY jest to globalna oś X. Dla płaszczyzny XZ i YZ jest to globalna oś Z.
    -   Opcjonalnie można zmienić **Odsunięcie**. **Odsunięcie**, **Odległość X** i **Odległość Y** są względne w stosunku do układu współrzędnych Płaszczyzny obrazu. Niewielkie ujemne przesunięcie może być przydatne podczas śledzenia obrazu za pomocą geometrii [szkicu](Sketcher_Workbench/pl.md) lub środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md).
4.  Opcjonalnie zmień **Przezroczystość**.
5.  Opcje **Rozmiar obrazu**:
    -   Skaluj według danych numerycznych:
        1.  Opcjonalnie odznacz **Zachowaj proporcje** dla nierównomiernego skalowania.
        2.  Wprowadź **Szerokość** i / lub **Wysokość**.
    -   Skalowanie przez wybieranie punktów:
        1.  Opcjonalnie zaznacz **Kalibruj**.
        2.  Naciśnij przycisk **Interaktywnie**.
        3.  Wybierz dwa punkty wewnątrz obrazu.
        4.  Zostanie wyświetlona linia wymiarowa.
        5.  Wprowadź pożądaną odległość.
        6.  Naciśnij **Enter** lub przycisk **Zastosuj** dla potwierdzenia zmian.
6.  Naciśnij przycisk **OK**, aby potwierdzić zmiany i zamknąć panel zadań.



### Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Płaszczyzna obrazu wywodzi się z obiektu [App: Cechy geometrii](App_GeoFeature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



#### Dane


{{TitleProperty|Płaszczyzna obrazu}}

-    **Plik obrazu|FileIncluded**: Plik obrazu używany dla Image Plane. Plik ten jest przechowywany w pliku **.FCStd**.

-    **RozmiarX|Length**: Szerokość płaszczyzny obrazu.

-    **RozmiarY|Length**: Wysokość płaszczyzny obrazu.



#### Widok


{{TitleProperty|Styl obiektu}}

-    **Oświetlenie|Enumeration**: Sposób oświetlenia płaszczyzny obrazu w oknie [widoku 3D](3D_view/pl.md). Może przyjmować wartość {{value|Dwie strony}} lub {{value|Jedna strona}}.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Import/pl
