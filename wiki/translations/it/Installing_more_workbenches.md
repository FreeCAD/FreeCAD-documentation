# Installing more workbenches/it
## Introduzione

Dalla versione 0.17 è facile aggiungere gli [ambienti complementari](external_workbenches/it.md) utilizzando [Addon Manager](Std_AddonMgr/it.md). Un utente normale non deve fare altro che utilizzare questo strumento.

Continuare a leggere per ulteriori informazioni sull\'installazione degli ambienti di lavoro.



## Descrizione generale 

Gli ambienti di lavoro non sono altro che raccolte di file inseriti in una cartella. Questa cartella è solitamente compressa in un archivio zip. Al momento dell\'installazione, questa cartella viene semplicemente decompressa e copiata


```python
$ROOT_DIR/Mod/
```

dove `$ROOT_DIR` è una directory di livello superiore cercata da FreeCAD all\'avvio. Questo è essenzialmente ciò che fa [Addon Manager](Std_AddonMgr/it.md).

Le directory `Mod/` vengono scansionate ogni volta che viene avviato FreeCAD e gli ambienti disponibili vengono aggiunti automaticamente.



### Installazione a livello di sistema 

Gli ambienti di lavoro così installati saranno disponibili a tutti gli utenti. A seconda del sistema, si potrebbe aver bisogno dei privilegi di amministratore per accedere alla cartella d\'installazione.

Copiare la cartella dell\'ambiente in `$INSTALL_DIR/Mod/`, dove `$INSTALL_DIR` è la directory di installazione di FreeCAD.

-   Su Linux di solito è `/usr/share/freecad/Mod/`
-   Su Windows di solito è `C:\Program Files\FreeCAD\Mod\`
-   Su macOS di solito è `/Applications/FreeCAD/Mod/`



### Installazione per un singolo utente 

Gli ambienti installati in questo modo sono disponibili per un solo utente del sistema, ma non è necessario alcun privilegio di amministratore o di superutente.

Copiare la cartella dell\'ambiente in `$USER_DIR/Mod/`, dove `$USER_DIR` è la directory di FreeCAD per un particolare `nome utente` (si può trovare quest\'ultimo digitando {{ incode\|App.getUserAppDataDir()}} nella [Console di Python](Python_console/it.md)).

-   Su Linux solitamente è `/home/username/.local/share/FreeCAD/Mod/`.
-   Su Windows è `%APPDATA%\FreeCAD\Mod\`, che di solito è `C:\Users\username\Appdata\Roaming\FreeCAD\Mod\`
-   Su macOS solitamente è `/Users/username/Library/Application Support/FreeCAD/Mod/`.



### Informazioni aggiuntive 

Ulteriori informazioni su come creare un ambiente di lavoro personalizzato si trovano in [Hub sviluppatori](Developer_hub/it.md) e in [Hub utenti avanzati](Power_users_hub/it.md).

Vedere anche la pagina [Come installare ambienti aggiuntivi](How_to_install_additional_workbenches/it.md).



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Installing more workbenches/it
