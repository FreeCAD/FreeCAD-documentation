# Import from STL or OBJ/pl
{{TutorialInfo/pl
|Topic= Importowanie plików STL lub OBJ
|Level= Początkujący
|Time= 30 minut
|Author=r-frank
|FCVersion=0.16.6703
|Files= nie dołączono
}}

## Wprowadzenie

W tym poradniku omówimy jak importować pliki STL/OBJ do programu FreeCAD. Ponieważ formaty STL/OBJ są opisane przez siatkę wielokątów i nie posiadają przypisanych konkretnych jednostek wielkości, FreeCAD przyjmuje, że wszystkie wartości podane w pliku są podane w mm. Jeśli jest inaczej, trzeba przeskalować model w aplikacji, w której został stworzony *(przed jego wyeksportowaniem)* lub przeskalować model w FreeCAD po jego zaimportowaniu i konwersji do bryły.

## Przykładowy plik 

Dla tego przykładu możesz użyć swojego pliku STL lub stworzyć plik demo w ten sposób:

-   Otwórz FreeCAD.
-   Stwórz nowy dokument.
-   Zmień Środowisko pracy na **mesh**.
-   Dodaj torus przez ** Meshes** → **<img src="images/Mesh_BuildRegularSolid.svg" width=32px> Regular solid...** wybierają opcje:
    -   Radius1: 10mm
    -   Radius2: 2mm
    -   Sampling: 50
-   kliknij ** Create** a następnie ** Close**
-   Zapisz plik za pomocą ** File** → ** Save**

Aby zaimportować plik STL lub OBJ, stwórz nowy dokument FreeCAD i wybierz ** File** → ** Import** z głównego menu.

## Czyszczenie i naprawianie pliku STL/OBJ w celu przygotowania go do importu 

FreeCAD może zaimportować każdy plik STL/OBJ. Ale naszym celem jest stworzenie bryły, która może być potem modyfikowana *(dodając wyciągnięcia lub kieszenie)*. Aby konwersja z siatki wielokątów do bryły się powiodła, musimy mieć pewność że siatka jest wodoszczelna *(nie zawiera dziur)* lub nie ma żadnych innych błędów.
Warto pamiętać, że FreeCAD nie jest dobrym edytorem siatki wielokątów, jest on zaprojektowany do pracy z bryłami. FreeCAD ma pewne funkcje do operacji na siatce 3D w Środowisku pracy Mesh i OpenSCAD *(niektóre operacje wymagają zainstalowanego i skonfigurowanego OpenSCAD)*
Niektórzy użytkownicy lubią używać innych zewnętrznych narzędzi do naprawienia siatki wielokątów np:

-   [Netfabb Basic](http://www.netfabb.com/downloadcenter.php?basic=1) *(Linux/Mac/Windows)* - darmowy do użytku domowego *(dostępne automatyczne naprawianie siatki)*,
-   [Meshlab](http://meshlab.sourceforge.net/) *(Linux/Mac/Windows)* - Open Source.

W tym poradniku użyjemy Środowiska pracy Mesh dostępnego standardowo w programie FreeCAD, do czyszczenia/naprawiania/weryfikowania naszego przykładowego pliku.

### Automatyczne testowanie i naprawianie 

-   Otwórz FreeCAD i przykładowy plik zawierający obiekt siatki.
-   Zmień Środowisko pracy na Mesh.
-   Upewnij się że Twój obiekt mesh został wybrany w widoku drzewa po lewej.
-   Wybierz **Meshes** → **Analyze** → **Evaluate & Repair mesh...** z górnego menu.
-   Upewnij się, że w rozwijanym menu w prawym górnym rogu wyświetla się nazwa twojego obiektu mesh.
-   Kliknij na **Analyze** przy \"All above tests together\" *(na dole)*
-   Teksty obok pola wyboru z nazwą obiektu mesh zmienią się, aby odzwierciedlić wyniki różnych testów.
-   Jeśli zostaną wykryte błędy, odpowiednie pola wyboru zostaną zaznaczone i będziesz mógł wybrać **Repair**.
-   Kliknij **Close** aby zamknąć menu.

### Porządkuj wektory normalne 

Porządkowanie wektorów normalnych *(harmonizing normals)* siatki obiektu może być robione przez:

-   wybranie obiektu \"mesh\" w widoku drzewa
-   wybranie **Meshes** → **<img src="images/Mesh_HarmonizeNormals.svg" width=32px> Harmonize normals** z górnego menu.

Wskazówka: Wybierając obiekt siatkowy w widoku drzewa, przechodząc do zakładki widok w widoku właściwości i zmieniając oświetlenie z **Two Side** do **One Side** można zidentyfikować trójkąty z odwróconymi wektorami normalnymi. Jeśli wektor normlny jest skierowana w siatkę, trójkąt będzie pokazany na czarno.

### Zaklejanie dziur 

Możesz również ręcznie zakleić otwory w obiekcie mesh za pomocą:

-   wybierz obiekt mesh w drzewie widoku
-   wybierz ** Meshes** → ** Fill holes...** z górnego menu
-   określ maksymalną liczbę krawędzi do wypełnienia (domyślnie 3)
-   Ponieważ STL i OBJ są siatkami składającymi się z trójkątów, domyślna liczba krawędzi powinna wystarczyć.

Inna metoda ręcznego zaklejenia otworów w obiekcie mesh:

-   wybierz obiekt mesh w drzewie widoku
-   Wybierz ** Meshes** → **<img src="images/Mesh_FillInteractiveHole.svg" width=32px> Close hole** z głównego menu
-   Wybierz jedną z krawędzi otworu w widoku 3d
-   kliknij prawym przyciskiem myszy na widoku 3d i wybierz ** Leave hole-filling mode** aby wyjść z tej komendy.

## Konwersja siatki do bryły 

-   przejdź do <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Środowiska roboczego Part](Part_Workbench/pl.md),
-   upewnij się, że obiekt siatki jest zaznaczony w widoku drzewa, w przeciwnym razie zaznacz go,
-   wybierz opcję **Part** → **<img src="images/Part_ShapeFromMesh.svg" width=32px> Utwórz kształt  siatki ...** z menu u góry,
-   należy określić tolerancję dla kształtu szwów *(domyślnie 0,1)*,
-   w widoku drzewa zostanie utworzony nowy obiekt *(z niebieską ikoną kształtu zamiast zielonej ikony siatki)*,
-   wybierz nowo stworzony obiekt w widoku drzewa,
-   wybierz opcję ** Part** → **Create a copy** → **<img src="images/Part_RefineShape.svg" width=32px> Refine shape** z menu u góry.
-   w widoku drzewa zostanie utworzony nowy obiekt , a poprzedni zostanie ukryty,
-   wybierz nowo stworzony obiekt w widoku drzewa,
-   użyj opcję ** Part** → **Konwertuj na bryłę** z menu u góry,
-   w widoku drzewa zostanie utworzony nowy obiekt, do jego nazwy zostanie dodany przedrostek \"(Solid)\", aby wskazać, że jest to obiekt typu bryła.

Ponieważ utworzona bryła nie posiada historii i żadnych edytowalnych funkcji *(jak prosta kopia w FreeCAD)*, z widoku drzewa można usunąć wszystkie poprzednie obiekty. W ten sposób rozmiar pliku projektu będzie mniejszy \...

## Linki

-   [Eksport do formatu STL or OBJ](Export_to_STL_or_OBJ.md)
-   [Import i eksport](Import_Export/pl.md)


 

[<img src="images/Property.png" style="width:16px"> File\_Formats](Category_File_Formats.md)

---
[documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Import](Import_Workbench.md) > Import from STL or OBJ/pl
