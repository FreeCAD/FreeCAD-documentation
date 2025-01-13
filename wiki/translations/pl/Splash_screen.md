# Splash screen/pl
## Opis

**Ekran powitalny** to obraz, który jest prezentowany podczas uruchamiania programu FreeCAD. Możesz wyłączyć wyświetlanie ekran powitalnego w menu [Preferencji](Preferences_Editor#General_2/pl.md) FreeCAD, wyłączając opcję **Włącz ekran powitalny podczas uruchamiania**.


{{Version/pl|1.0}}

: Obraz ekranu powitalnego jest wybierany losowo spośród wielu obrazów, w tym modeli użytkownika i wybranych dodatkowych środowisk pracy.



## Własny ekran powitalny 

Aby użyć niestandardowego ekranu powitalnego, należy umieścić obraz o nazwie **splash_image.png** w jednym z następujących katalogów, w zależności od systemu operacyjnego:

-   **Linux:** **$XDG_DATA_HOME/FreeCAD/Gui/images/** *(zazwyczaj odpowiada to **~/.local/share/FreeCAD/Gui/images/**)*,
-   **MacOS:** **~/Library/Application Support/FreeCAD/Gui/images/**,
-   **Windows:** **%APPDATA%\FreeCAD\Gui\images\** *(zazwyczaj **C:\Users\username\AppData\Roaming\FreeCAD\Gui\images\**)*.

Lokalizację katalogu można wyświetlić za pomocą polecenia {{Incode|App.getUserAppDataDir()}} w [konsoli Python](Python_console/pl.md). Katalogi {{Incode|Gui}} i {{Incode|images}} trzeba utworzyć samodzielnie. Ten sam niestandardowy ekran powitalny będzie używany dla wszystkich wersji FreeCAD na danym komputerze.



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > Splash screen/pl
