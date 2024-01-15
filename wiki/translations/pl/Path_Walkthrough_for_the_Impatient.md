---
 TutorialInfo:l
   Topic: środowisko pracy CAM
   Level: początkujący / średnio zaawansowany
   Time: 15 minut
   Author: Chrisb
   FCVersion: 0.19
   Files: brak
---

# Path Walkthrough for the Impatient/pl







## Przeznaczenie

Demonstracja tworzenia **Zadania** środowiska pracy <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> [CAM](Path_Workbench/pl.md) na podstawie modelu 3D. Następnie generowanie poprawnego dialektycznie G-Code dla docelowej frezarki CNC.



## Model 3D 

1\. Projekt rozpoczyna się od prostego modelu FreeCAD zaprojektowanego w środowisku pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [Projekt Części](PartDesign_Workbench/pl.md) prostopadłościanu z kieszenią w kształcie prostokąta,

:   ![](images/Path-SquarePocketModel.png )





:   
    
*Powyżej: Prostopadłościan z kieszenią utworzony w środowisku pracy <img src="images/Workbench_PartDesign.svg" width=24px> [Projekt Części](PartDesign_Workbench/pl.md) obejmujący Zawartość, na podstawie szkicu zorientowanego w 
**![](images/)*_płaszczyźnie_XY.**
    

2\. Po ukończeniu modelu 3D przełącz się na środowisko <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> [CAM](Path_Workbench/pl.md) poprzez *(menu rozwijane)* [wyboru środowiska pracy](Std_Workbench/pl.md)

## Zadanie

3\. Teraz tworzymy [Zadanie](Path_Job/pl.md) za pomocą jednej z następujących metod:

-   Naciskamy przycisk **![](images/)_[Zadanie](Path_Job/pl.md)** z paska narzędzi.
-   Używając skrótu klawiaturowego **P**, a następnie **J**.
-   Używając polecenia z menu głównego **CAM → Zadanie**.

![](images/Path-JobCreationDialog.png )

:   

    :   
        
*Powyżej: Okienko dialogowe [Utwórz zadanie](Path_Job/pl.md)*
        

4\. Zostanie otwarte okno dialogowe edycja zadania. W tym oknie dialogowym kliknij **OK**, aby zaakceptować Zawartość jako model podstawowy, bez szablonu.



### Konfiguracja

5\. Okno Edycja zadania zostanie otwarte w oknie zadań, a w oknie widoku modelu zostanie wyświetlony element materiału jako prostopadłościan szkieletu otaczający podstawową Zawartość. Zostanie wybrana karta **Konfiguracja**.



### Wyjście zadania 

6\. Zakładka Wyjście definiuje ścieżkę pliku wyjściowego, nazwę, rozszerzenie i postprocesor. Zaawansowani użytkownicy mogą dostosować Argumenty postprocesora *(wskazanie kursorem myszki powoduje wyświetlenie podpowiedzi typowych argumentów)*.

:   ![](images/Path-JobOutput.png )

:   
    
*Powyżej: Okienko dialogowe Edycja [zadania](Path_Job/pl.md) z wybraną zakładką '''Wyjście'''*
    



### Narzędzia

:   ![](images/Path-JobTools.png )

:   
    
*Powyżej: Okienko dialogowe Edycja [zadania](Path_Job/pl.md) z wybraną zakładką '''Narzędzia'''*
    

7\. Zmodyfikuj domyślne narzędzie, zaznaczając je i klikając przycisk **Edycja**. Spowoduje to otwarcie okna **Edytor kontrolera narzędzi**.

:   ![](images/Path-ToolConfig.gif )

:   
    
*Powyżej: Okienko dialogowe Edycja [zadania](Path_Job/pl.md) Kontrolera narzędzi*
    

8\. Nazwa nadana narzędziu i numer narzędzia odpowiadają numerowi narzędzia maszyny. W oknie dialogowym (patrz wyżej) jest to narzędzie nr 4. Sterownik narzędzia jest skonfigurowany dla posuwu poziomego i pionowego `2mm/s` i prędkości wrzeciona `2000 rpm`.

9\. Wybierz zakładkę **Narzędzia** w Kontrolerze narzędzi. Ustaw średnicę *(a jeśli chcesz użyć narzędzia <img alt="" src=images/Path_Simulator.svg  style="width:24px;"> [Symulator](Path_Simulator/pl.md) później: dodaj kąt krawędzi tnącej i wysokość krawędzi tnącej)*.

:   ![](images/Path-ToolAdd.gif )

:   
    
*Powyżej: Okienko dialogowe Edycja [zadania](Path_Job/pl.md) Kontrolera narzędzi i zakładka '''Narzędzia'''*
    

10\. Wartości są potwierdzane przyciskiem **OK**.

Uwaga: Aby ułatwić dostęp, wszystkie narzędzia można wstępnie zdefiniować i wybrać z <img alt="" src=images/Path_ToolLibraryEdit.svg  style="width:24px;"> [Menadżera narzędzi](Path_ToolLibraryEdit/pl.md).



### Plan pracy 

Zakładka **Plan pracy** jest początkowo wyświetlana jako pusta. Następnie jest wypełniana sekwencją operacji zadania, poleceń ścieżki częściowej i elementów wykończenia ścieżki. Kolejność tych elementów jest tutaj uporządkowana.

To drzewo jest wyświetlane po konfiguracji zadania, po rozwinięciu zadania ścieżki:

:   ![](images/Path-TreeWithJob.png )



## Operacje

11\. Dwie operacje zostaną dodane w celu wygenerowania ścieżek frezowania dla tego zadania ścieżki. Operacja [Kontur](Path_Profile/pl.md) tworzy ścieżkę wokół prostopadłościanu, a operacja [Kształt kieszeni](Path_Pocket_Shape/pl.md) tworzy ścieżkę dla wewnętrznej kieszeni.

12\. Na razie zachowamy prostotę. Przycisk <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Kontur](Path_Profile/pl.md) otwiera panel Kontur. Po potwierdzeniu przyciskiem **OK** przy użyciu domyślnych wartości, widoczna jest zielona ścieżka wokół obiektu.

13\. Wybranie spodu kieszeni, a następnie przycisku <img alt="" src=images/Path_Pocket_Shape.svg  style="width:32px;"> [Kształt kieszeni](Path_Pocket_Shape/pl.md) otwiera okno Kształt kieszeni. Używane są domyślne wartości Geometrii bazowej, Głębokości i Wysokości, wybrana jest zakładka Operacja, a wartość procentowa Kroku nad jest ustawiona na wartość 50.

:   ![](images/Path-PocketOperation.gif )

:   
    
*Powyżej: Okno dialogowe Kształt kieszeni z wybranym panelem Operacja*
    

14\. Wzór zostanie zmieniony na \"Odsunięcie\", a zadanie dla konfiguracji kieszeni zostanie potwierdzone przyciskiem **OK**.

Rezultatem jest model z dwiema ścieżkami:

:   ![](images/Path-WalkThroughResult.gif )

:   
    
*Powyżej: wynik dla modelu z dwiema ścieżkami*
    



## Sprawdzanie ścieżek 

Istnieją dwa sposoby weryfikacji utworzonych ścieżek. Można sprawdzić G-code, w tym podświetlić odpowiednie segmenty ścieżki. Proces frezowania zadania ścieżki może być również symulowany w celu zademonstrowania wyidealizowanych ścieżek narzędzia, wymaganych dla geometrii narzędzia do frezowania materiału.

Aby sprawdzić G-Code użyj narzędzia <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> [Przeglądaj polecenia ścieżki](Path_Inspect/pl.md). Wybranie odpowiednich linii G-code w oknie G-code podświetla poszczególne segmenty ścieżki.

:   ![](images/Path-InspectWindow.gif )

:   
    
*Powyżej: Narzędzie [Przeglądaj polecenia ścieżki](Path_Inspect/pl.md) otwiera okno dialogowe G-code*
    

Aby rozpocząć symulację, użyj narzędzia <img alt="" src=images/Path_Simulator.svg  style="width:32px;"> [Symulator CAM](Path_Simulator/pl.md).

Dostosuj prędkość i dokładność i rozpocznij symulację za pomocą przycisku <img alt="" src=images/Path_BPlay.svg  style="width:24px;"> *(Play)*.

:   ![](images/Path-Simulation.gif )

:   
    
*Powyżej: [Symulacja CAM](Path_Simulator/pl.md) w toku*
    

Jeśli chcesz zakończyć symulację, kliknij przycisk **Anuluj**, co spowoduje usunięcie półproduktu utworzonego na potrzeby symulacji. Jeśli klikniesz przycisk **OK**, obiekt ten zostanie zachowany w zadaniu.



## Przetwarzanie końcowe zadania 

Ostatnim krokiem do wygenerowania G-code dla docelowej frezarki jest postprocessing zadania. Powoduje to przesłanie G-code do pliku, który można przesłać do docelowego sterownika maszyny CNC. Aby wywołać postprocesor:

-   Wybierz obiekt Zadanie w oknie [Widoku drzewa](Tree_view/pl.md).
-   Wybierz narzędzie <img alt="" src=images/Path_Post.svg  style="width:32px;"> [Przetwarzanie końcowe](Path_Post/pl.md) do przetwarzania pliku. Spowoduje to otwarcie okna G-code umożliwiającego sprawdzenie końcowego pliku wyjściowego przed jego zapisaniem.

:   ![](images/Path-PostOutput.gif )

:   
    
*Powyżej: Okno G-code umożliwiające przeglądanie końcowego pliku wyjściowego*
    


{{Path Tools navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Walkthrough for the Impatient/pl
