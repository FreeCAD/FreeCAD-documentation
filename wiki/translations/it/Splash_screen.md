# Splash screen/it
## Descrizione

La schermata iniziale è un\'immagine che appare durante l\'avvio di FreeCAD. Per ogni nuova versione, viene selezionata in una votazione aperta dai contributi degli utenti. Si può disabilitare la schermata iniziale nell\'[Editor Preferenze](Preferences_Editor/it.md) deselezionando l\'opzione **Abilita la schermata iniziale all\'avvio**.



## Schermata iniziale personalizzata 

Per utilizzare una schermata iniziale personalizzata, si deve inserire un\'immagine denominata **splash_image.png** in una delle seguenti directory a seconda del sistema operativo:

-   **Linux:** **$XDG_DATA_HOME/FreeCAD/Gui/images/** (normalmente corrisponde a **~/.local/share/FreeCAD/Gui/images/**)
-   **Windows:** **%APPDATA%\FreeCAD\Gui\images\** (normalmente **C:\Users\username\AppData\Roaming\FreeCAD\Gui\images\** )
-   **MacOS:** **~/Library/Application Support/FreeCAD/Gui/images/**\$XDG_DATA_HOME

La directory può essere trovata utilizzando il comando {{Incode|App.getUserAppDataDir()}} nella [console Python](Python_console/it.md). Potrebbe essere necessario creare prima le cartelle {{Incode|Gui}} e {{Incode|images}}. La stessa schermata iniziale personalizzata verrà utilizzata per tutte le versioni di FreeCAD su un determinato computer.



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > Splash screen/it
