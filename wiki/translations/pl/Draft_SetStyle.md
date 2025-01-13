---
 GuiCommand:
   Name: Draft SetStyle
   Name/pl: Rysunek Roboczy: Ustaw styl
   MenuLocation: Narzędzia , Ustaw styl
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   Shortcut: Rysunek Roboczy: **S** **S**
   Version: 0.19
   SeeAlso: Draft_AnnotationStyleEditor/pl, Draft_ApplyStyle/pl
---

# Draft SetStyle/pl



## Opis

Polecenie <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> **Ustaw styl** ustawia domyślny styl dla nowych obiektów.

<img alt="" src=images/Draft_SetStyle_Taskpanel_Tab_Shape.png  style="width:" height="500px;"> <img alt="" src=images/Draft_SetStyle_Taskpanel_Tab_Annotation.png  style="width:" height="500px;"> 
*Dwie zakładki ({{Version/pl|1.0*) panelu zadań ustawień stylu}}



## Użycie

1.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk ![](images/Draft_tray_button_style.png ) w [tacce narzędziowej](Draft_Tray/pl.md). W zależności od bieżących ustawień stylu przycisk ten może wyglądać inaczej.
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Wybierz opcję **Narzędzia → <img src="images/Draft_SetStyle.svg" width=16px> Ustaw styl** z menu lub menu kontekstowego [widoku drzewa](Tree_view/pl.md) bądź [widoku 3D](3D_view/pl.md).
    -   Rysunek Roboczy: Użyj skrótu klawiaturowego: **S**, a następnie **S**.
2.  Otworzy się panel zadań **Ustawienia stylu**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
3.  Opcjonalnie można zmienić jedno lub więcej ustawień.
4.  Naciśnij przycisk **OK**, aby zapisać ustawienia.
5.  Przycisk w [tacce narzędziowej](Draft_Tray/pl.md) zostanie zaktualizowany.



## Opcje

-   Z rozwijanej listy w górnej części panelu zadań można wybrać bieżące ustawienie stylu.
-   Naciśnij przycisk **<img src="images/Document-save.svg" width=16px>**, aby zapisać bieżące ustawienia stylu jako ustawienie wstępne.
-   W sekcji **Kształty** można określić następujące ustawienia:
    -   
        **Wygląd kształtu**
        
        -   
            **Kolor kształtu**
            
            .

        -   
            **Kolor kształtu otoczenia**
            
            . {{Version/pl|1.0}}

        -   
            **Kolor kształtu emisyjny**
            
            . {{Version/pl|1.0}}

        -   
            **Kolor kształtu lustrzany**
            
            . {{Version/pl|1.0}}

        -   
            **Przezroczystość**
            
            .

        -   
            **Połysk kształtu**
            
            . {{Version/pl|1.0}}

    -   
        **Inne**
        
        .

        -   
            **Kolor linii**
            

        -   
            **Szerokość linii**
            
            .

        -   
            **Kolor punktu**
            
            . {{Version/pl|1.0}}

        -   
            **Rozmiar punktu**
            
            . {{Version/pl|1.0}}

        -   
            **Styl kreślenia**
            
            .

        -   
            **Tryb wyświetlania**
            
            .
-   Ustawienia w sekcji **Adnotacje** mają zastosowanie do [Adnotacja wieloliniowa](Draft_Text.md), [Wymiarów](Draft_Dimension.md) i [Etykiet](Draft_Label.md). Można określić następujące ustawienia *(zobacz [Adnotacja wieloliniowa](Draft_Text#Widok.md) i [Wymiar](Draft_Dimension/pl#Widok.md) aby uzyskać szczegółowe informacje)*:
    -   
        **Teksty**
        
        -   
            **Nazwa czcionki**
            
            .

        -   
            **Rozmiar czcionki**
            
            . W rzeczywistości jest to domyślna wysokość wiersza, litery są mniejsze.

        -   
            **Odstępy między wierszami**
            
            . Nie używane dla wymiarów.

        -   
            **Mnożnik skali**
            
            . Jest to odwrotność skali ustawionej w [widżecie skalowania adnotacji](Draft_annotation_scale_widget/pl.md). Jeśli skala wynosi {{value|1:100}}, mnożnik wynosi {{Value|100}}. {{Version/pl|1.0}}

        -   
            **Kolor tekstu**
            
            .

    -   
        **Linie i strzałki**
        
        -   
            **Szerokość linii**
            
            . {{Version/pl|1.0}}

        -   
            **Styl strzałki**
            
            .

        -   
            **Rozmiar strzałki**
            
            .

        -   
            **Kolor linii i strzałek**
            
            . {{Version/pl|1.0}}

    -   
        **Wymiary**
        
        -   
            **Wyświetlaj jednostki**
            
            .

        -   
            **Zastępuj jednostki**
            
            .

        -   
            **Przedłużenie wymiaru**
            
            . {{Version/pl|0.21}}

        -   
            **Linie pomocnicze**
            
            . {{Version/pl|0.21}}

        -   
            **Przedłużenie linii pomocniczych**
            
            . {{Version/pl|0.21}}

        -   
            **Odstępy w tekście**
            
            .
-   Naciśnij przycisk **<img src="images/Draft_SetStyle.svg" width=16px> Zaznaczone**, aby zastosować ustawienia do wybranych obiektów lub grup. Obiekty można zaznaczać, gdy panel zadań jest otwarty.
-   Naciśnij przycisk **<img src="images/Draft_Text.svg" width=16px> Adnotacje**, aby zastosować ustawienia do wszystkich [adnotacji wieloliniowych](Draft_Text/pl.md), [wymiarów](Draft_Dimension/pl.md) i [etykiet](Draft_Label/pl.md) w bieżącym dokumencie. {{Version/pl|0.21}}
-   Naciśnij przycisk **Anuluj**, aby zakończyć polecenie bez zapisywania ustawień.



## Uwagi

-   Ustawienia w sekcji **Kształt**, z wyjątkiem **Styl rysowania** i **Tryb wyświetlania**, są używane nie tylko dla obiektów środowiska Rysunek Roboczy, ale także dla obiektów utworzonych w innych środowiskach pracy.
-   Wszystkie ustawienia, z wyjątkiem **Styl rysowania** i **Tryb wyświetlania**, można również zmienić w preferencjach. Zobacz stronę [Preferencje środowiska Projekt Części](PartDesign_Preferences/pl#Wygląd_kształtu.md) i [Preferencje środowiska Rysunek Roboczy](Draft_Preferences/pl#Teksty_i_wymiary.md).
-   Style są zapisywane w pliku o określonej nazwie: **StylePresets.json**, który jest przechowywany w folderze użytkownika FreeCAD **Draft**:
    -   W systemie Linux jest to zazwyczaj **/home/<nazwa_użytkownika>/.local/share/FreeCAD/Draft/**.
    -   W systemie Windows jest to **%APPDATA%\FreeCAD\Draft\**, który zwykle znajduje się w **C:\Users\<nazwa_użytkownika>\Appdata\Roaming\FreeCAD\Draft\**.
    -   W systemie macOS jest to zazwyczaj **/Users/<nazwa_użytkownika>/Library/Preferences/FreeCAD/Draft/**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SetStyle/pl
