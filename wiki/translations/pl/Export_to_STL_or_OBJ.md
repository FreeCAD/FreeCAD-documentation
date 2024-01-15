---
 TutorialInfo:l
   Topic:  Eksport do formatu STL lub OBJ
   Level:  Początkujący
   Time:  20 minut
   Author: r-frank
   FCVersion: 0.16.6703
   Files:  nie dołączono
---

# Export to STL or OBJ/pl







## Wprowadzenie

W tym poradniku omówimy, jak wykonać eksport plików STL / OBJ z FreeCAD. Format siatki STL / OBJ jest bezwymiarowy. FreeCAD zakłada przy eksporcie, że jednostki użyte w modelu są w mm. Jeśli tak nie jest, należy przeskalować model. Jednym ze sposobów jest użycie narzędzia <img alt="" src=images/Draft_Scale.svg  style="width:24px;">. [Skaluj](Draft_Scale/pl.md) środowiska pracy Rysunek Roboczy.



## Przykładowa część 

Możesz użyć własnego pliku FreeCAD, ale możesz także utworzyć szybki plik testowy poprzez:

1.  Uruchomienie FreeCAD.
2.  Utworzenie nowego dokumentu.
3.  Przełączenie na środowisko pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md).
4.  Wstaw sześcian klikając w <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Sześcian](Part_Box/pl.md).
5.  Wstaw stożek klikając w <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Stożek](Part_Cone/pl.md).
6.  Zaznacz oba obiekty w oknie [Widoku drzewa](Tree_view/pl.md).
7.  Zastosuj scalenie klikając w <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Połączenie](Part_Fuse/pl.md).
8.  Zapisz plik.



## Metoda eksportu 1: Korzystanie z opcji \"Plik → Eksportuj\" 

1.  Przy ustawieniach domyślnych ta metoda tworzy siatkę z zauważalnie postrzępionymi krzywymi. Aby uzyskać gładsze wykończenie podczas np. drukowania 3D, należy skonfigurować rozdzielczość siatki:
    1.  Upewnij się, że środowisko pracy <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Siatka](Mesh_Workbench/pl.md) zostało załadowane *(domyślnie nie jest załadowany)*.
    2.  Przejdź do menu **Edycja → Preferencje ... → Import-Export → Formaty siatki**.
    3.  Zmień **Maksymalne odchylenie siatki**. Niższa wartość spowoduje utworzenie siatki o wyższej rozdzielczości.
2.  Wybierz bryłę do wyeksportowania w widoku drzewa.
3.  Wybierz Plik **File → Eksportuj ...** i ustaw typ pliku na **STL mesh (*.stl *.ast)**.
4.  Wprowadź nazwę pliku. Domyślne rozszerzenie to **.stl**. Musisz dołączyć rozszerzenie **.ast**, aby utworzyć plik **.ast**.
5.  Wybierz **Zapisz**.



## Metoda eksportu 2: Korzystanie z środowiska pracy Siatka w programie FreeCAD 

1.  Przełącz się do środowiska pracy <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Siatka](Mesh_Workbench/pl.md)
2.  Wybierz bryłę do zazębienia w widoku drzewa.
3.  Wybierz **Siatki** → **<img src="images/Mesh_FromPartShape.svg" width=32px> Utwórz siatkę z kształtu ...** z menu głównego.
4.  Wybierz jedną z dostępnych siatek i określ dostępne opcje. Więcej informacji można znaleźć na stronie [Kształt z siatki](Mesh_FromPartShape/pl.md).
5.  Wybierz **OK**. Obiekt siatki zostanie utworzony w widoku drzewa *(z zieloną ikoną siatki <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;">)*.
6.  Kliknij prawym przyciskiem myszy obiekt siatki w widoku drzewa i wybierz **<img src="images/Mesh_Export.svg" width=32px> Eksportuj siatkę ...**.
7.  Wpisz nazwę pliku. Rozszerzenie nie jest konieczne. Rozszerzenie zostanie ustawione na podstawie typu pliku. W przypadku podania rozszerzenia, które nie pasuje do wybranego typu pliku, rozszerzenie dla wybranego typu zostanie dodane podczas zapisywania pliku. W przypadku podania rozszerzenia pasującego do typu pliku, dodatkowe rozszerzenie nie zostanie dodane.
8.  Domyślnym typem pliku jest **Binary STL (*.stl)**. Zmień typ, jeśli chcesz.
9.  Wybierz **Zapisz**.



## Którą metodę wybrać 

-   Metoda 1 może być używana w większości sytuacji, w których wymagany jest plik siatki.
-   W metodzie 2 można zweryfikować siatkę w programie FreeCAD. A jeśli masz więcej niż jedną bryłę do przekonwertowania, możesz użyć narzędzi z <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Siatka](Mesh_Workbench/pl.md). Na przykład można połączyć siatki przed eksportem.



## Odnośniki internetowe 

-   [Import z formatu STL or OBJ](Import_from_STL_or_OBJ.md)
-   [Import i eksport](Import_Export/pl.md)



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Export to STL or OBJ/pl
