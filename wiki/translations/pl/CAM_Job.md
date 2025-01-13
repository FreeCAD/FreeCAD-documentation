---
 GuiCommand:
   Name: CAM Job
   Name/pl: CAM: Zadanie
   MenuLocation: CAM , Zadanie
   Workbenches: CAM_Workbench/pl
   Shortcut: **P** **J**
   SeeAlso: CAM_Post/pl, Path_Postprocessor_Customization/pl
---

# CAM Job/pl



## Opis

Narzędzie <img alt="" src=images/CAM_Job.svg  style="width:16px;"> [Zadanie](CAM_Job/pl.md) tworzy nowy obiekt Zadanie w aktywnym dokumencie. Obiekt Zadanie zawiera następujące informacje:

1.  Lista definicji kontrolera narzędzi, określających geometrię, posuwy i prędkości dla narzędzi operacji CAM.
2.  Sekwencyjną listę operacji CAM.
3.  Obiekt bazowy - klon używany do odsunięcia.
4.  Materiał obrabiany, reprezentujący materiał, który będzie podlegał obróbce w środowisku pracy CAM.
5.  Arkusz ustawień, zawierający dane wejściowe używane przez operacje CAM, wliczając wartości statyczne i formuły.
6.  Parametry konfiguracyjne określające ścieżkę docelową dla wyjściowego G-Code, nazwę pliku i rozszerzenie oraz [postprocessor](CAM_Post/pl.md) *(używany do generowania odpowiedniego języka dla docelowego kontrolera CNC i dostosowanych jednostek, zmian narzędzi, zatrzymań itd.)*.



## Użycie

1.  Jest kilka sposobów na wywołanie tego polecenia:
    -   Wciśnij przycisk **<img src="images/CAM_Job.svg" width=16px> [Zadanie](CAM_Job/pl.md)**.
    -   Wybierz opcję **CAM → <img src="images/CAM_Job.svg" width=16px> Zadanie** z menu.
    -   Użyj skrótu klawiszowego: **P** a następnie **J**.

Okno dialogowe Zadania ma sześć pionowo ułożonych zakładek: **Ogólne**, **Wyjście**, **Konfiguracja**, **Narzędzia** oraz **Plan pracy** i **Wartości domyślne operacji**. Użytkownik może w każdej chwili skorzystać z przycisków **OK** lub **Anuluj** w obrębie okna dialogowego.



## Ogólne

![](images/Job_1.jpg )

-   **Etykieta**: Etykieta Zadania wyświetlana w widoku drzewa.
-   **Model**: Obiekt bazowy, który swoim kształtem definiuje ścieżki zadania. Jeśli jest to obiekt środowiska pracy Projekt Części to jest to zwykle Zawartość, która była tam wybrana. Jeśli masz element zaznaczony w drzewie *przed* kliknięciem przycisku \"Dodaj zadanie\" to ten element zostaje od razu dodany. Możesz go zmienić wybierając inny element z listy rozwijanej.
-   **Opis**: Możesz tu dodać jakieś notatki do zadania. Notatki są tylko dla Twojej informacji i nie mają żadnego wpływu na ścieżkę.



## Wyjście

![](images/Job_2.jpg )

-   **Plik wyjściowy**: Ustaw nazwę, rozszerzenie i ścieżkę pliku wyjściowego instrukcji G-Code. Możesz skorzystać z następujących symboli zastępczych:
    -   **%D** ścieżka aktywnego dokumentu,
    -   **%d** nazwa aktywnego dokumentu *(bez rozszerzenia)*,
    -   **%M** ścieżka makr użytkownika,
    -   **%j** nazwa zadania.

-   **Procesor**: Wybierz [postprocesor](CAM_Post/pl.md) dla swojej maszyny.
-   **Parametry**: Dodaj parametry dla [postprocesora](CAM_Post/pl.md) jeśli potrzeba.



## Konfiguracja

![](images/Job_3.jpg )

-   **Przygotówka**: ustaw rozmiar i kształt materiału do obróbki.
-   **Orientacja**: Wybrana ściana lub krawędź jest używana do zorientowania odpowiednio bazy lub półwyrobu.
-   **Wyrównanie**: wybierz wierzchołek aby ustawić początek lub przesunąć bazę lub półwyrób



## Narzędzia

![](images/Job_4.jpg )

Dodaj narzędzia z Twojego [zestawu narzędzi](CAM_ToolLibraryEdit/pl.md), które potrzebujesz do operacji w ramach tego zadania.

Po dodaniu narzędzia możesz ustawić / zmodyfikować prędkość posuwu i prędkość wrzeciona jeśli potrzebujesz innej prędkości posuwu w tym zadaniu. Zmiana tutaj nie zmienia parametrów przechowywanych w zestawie narzędzi.

Domyślne narzędzie, które możesz usunąć jeśli masz dodane własne narzędzie.



## Plan pracy 

![](images/Job_5.jpg )

Jeśli masz zadanie, które zawiera więcej niż jedną operację, możesz określić w jakiej kolejności operacje mają być wykonane. Aby zmienić kolejność, wybierz operację i wciśnij przycisk przesunięcia w górę lub w dół.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Job/pl
