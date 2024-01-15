---
 GuiCommand:
   Name: Draft SetStyle
   Name/pl: Rysunek Roboczy: Ustaw styl
   MenuLocation: Narzędzia , Ustaw styl
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Shortcut: **S** **S**
   Version: 0.19
   SeeAlso: Draft_AnnotationStyleEditor/pl, Draft_ApplyStyle/pl
---

# Draft SetStyle/pl



## Opis

Polecenie <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> **Ustaw styl** ustawia domyślny styl dla nowych obiektów.

<img alt="" src=images/Draft_SetStyle_Taskpanel.png  style="width:" height="550px;"> 
*Panel zadań ustawień stylu.*



## Użycie

1.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk ![](images/Draft_tray_button_style.png ) w [tacce narzędziowej](Draft_Tray/pl.md). W zależności od bieżących ustawień stylu przycisk ten może wyglądać inaczej.
    -   Wybierz z menu opcję **Narzędzia → <img src="images/Draft_SetStyle.svg" width=16px> Ustaw styl**.
    -   Użyj skrótu klawiaturowego: **S**, a następnie **S**.
2.  Otworzy się panel zadań **Ustawienia stylu**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
3.  Opcjonalnie można zmienić jedno lub więcej ustawień.
4.  Naciśnij przycisk **OK**, aby zapisać ustawienia.
5.  Przycisk w [tacce narzędziowej](Draft_Tray/pl.md) zostanie zaktualizowany.



## Opcje

-   Z rozwijanej listy w górnej części panelu zadań można wybrać bieżące ustawienie stylu.
-   Naciśnij przycisk **<img src="images/Document-save.svg" width=16px>**, aby zapisać bieżące ustawienia stylu jako ustawienie wstępne.
-   W sekcji **Kształty** można określić następujące ustawienia:
    -   
        **Kolor kształtu**
        
        .

    -   
        **Przezroczystość**
        
        .

    -   
        **Kolor linii**
        
        .

    -   
        **Szerokość linii**
        
        .

    -   
        **Kolor punktu**
        
        . {{Version/pl|0.22}}

    -   
        **Rozmiar punktu**
        
        . {{Version/pl|0.22}}

    -   
        **Styl kreślenia**
        
        .

    -   
        **Tryb wyświetlania**
        
        .
-   Ustawienia w sekcji **Adnotacje** mają zastosowanie do [Adnotacja wieloliniowa](Draft_Text.md), [Wymiarów](Draft_Dimension.md) i [Etykiet](Draft_Label.md). Można określić następujące ustawienia (zobacz [Draft Text](Draft_Text#View.md) aby uzyskać szczegółowe informacje):
    -   
        **Kolor tekstu**
        
        .

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
        
        . Jest to odwrotność skali ustawionej w [widżecie skalowania adnotacji](Draft_annotation_scale_widget/pl.md). Jeśli skala wynosi {{value|1:100}}, mnożnik wynosi {{Value|100}}. {{Version/pl|0.22}}
-   W sekcji **Wymiary** można określić następujące ustawienia (zobacz stronę [wymiary](Draft_Dimension/pl#Widok.md) aby uzyskać szczegółowe informacje):
    -   
        **Kolor linii i strzałek**
        
        . {{Version/pl|0.22}}

    -   
        **Szerokość linii**
        
        . {{Version/pl|0.22}}

    -   
        **Styl strzałki**
        
        .

    -   
        **Rozmiar strzałki**
        
        .

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
-   Naciśnij przycisk **<img src="images/Draft_Text.svg" width=16px> Adnotacje**, aby zastosować ustawienia do wszystkich [adnotacja wieloliniowych](Draft_Text/pl.md), [wymiarów](Draft_Dimension/pl.md) i [etykiet](Draft_Label/pl.md) w bieżącym dokumencie. {{Version/pl|0.21}}
-   Naciśnij przycisk **Anuluj**, aby zakończyć polecenie bez zapisywania ustawień.



## Uwagi

-   Ustawienia w sekcji **Kształty**, z wyjątkiem **Styl rysowania** i **Tryb wyświetlania**, są używane nie tylko dla obiektów środowiska Rysunek Roboczy, ale także dla obiektów utworzonych w innych środowiskach pracy.
-   Wszystkie ustawienia, z wyjątkiem **Styl rysowania** i **Tryb wyświetlania**, można również zmienić w preferencjach. Zobacz stronę [Preferencje środowiska Projekt Części](PartDesign_Preferences/pl#Wygląd_kształtu.md) i [Preferencje środowiska Rysunek Roboczy](Draft_Preferences/pl#Teksty_i_wymiary.md).
-   Style są zapisywane w pliku o określonej nazwie: **StylePresets.json**, który jest przechowywany w folderze użytkownika FreeCAD **Draft**:
    -   W systemie Linux jest to zazwyczaj **/home/<nazwa użytkownika>/.local/share/FreeCAD/Draft/**.
    -   W systemie Windows jest to **%APPDATA%\FreeCAD\Draft\**, który zwykle znajduje się w **C:\Users\<username>\Appdata\Roaming\FreeCAD\Draft\**.
    -   Na macOS jest to zazwyczaj **/Users/<username>/Library/Preferences/FreeCAD/Draft/**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SetStyle/pl
