# Installing more workbenches/it



## Introduction

Since v0.17 it is easy to add [external workbenches](external_workbenches.md) by using the [Addon Manager](Std_AddonMgr.md). A regular user doesn\'t need to do more than use this tool.

Keep reading for more information regarding installation of workbenches.


<div class="mw-translate-fuzzy">

## Descrizione

Aggiungere [ambienti esterni](external_workbenches/it.md) a FreeCAD è facile .


</div>


<div class="mw-translate-fuzzy">

Gli ambienti sono contenuti in una cartella in cui devono semplicemente essere copiati.


</div>


```python
$ROOT_DIR/Mod/
```


<div class="mw-translate-fuzzy">

dove `$ROOT_DIR` è una directory di primo livello ricercata da FreeCAD all\'avvio.


</div>

Le directory `Mod/` vengono scansionate ogni volta che viene avviato FreeCAD e gli ambienti disponibili vengono aggiunti automaticamente.


<div class="mw-translate-fuzzy">

### Installazione a livello di sistema 

Gli ambienti installati in questo modo sono disponobili per tutti gli utenti. Secondo il sistema, può essere necessario avere i privilegi di amministratore o di superutente per accedere alla directory di installazione.


</div>

Workbenches installed in this way will be available to all users. Depending on your system, you might need administrator privileges to access the installation directory.


<div class="mw-translate-fuzzy">

Copiare la cartella dell\'ambiente in `$INSTALL_DIR/Mod/`, dove `$INSTALL_DIR` è la directory di installazione di FreeCAD.

-   Su Linux di solito è `/usr/share/freecad/Mod/`
-   Su Windows di solito è `C:\Program Files\FreeCAD\Mod\`
-   Su Mac OSX di solito è `/Applications/FreeCAD/Mod/`


</div>


<div class="mw-translate-fuzzy">

### Installazione per un singolo utente 

Gli ambienti installati in questo modo sono disponibili per un solo utente del sistema, ma non è necessario alcun privilegio di amministratore o di superutente.


</div>

Workbenches installed in this way will be available only to one user, but will not require any administrator privileges.


<div class="mw-translate-fuzzy">

Copiare la cartella dell\'ambiente in `$USER_DIR/Mod/`, dove `$USER_DIR` è la directory di FreeCAD per un particolare `nome utente`.

-   Su Linux di solito è `/home/username/.FreeCAD/Mod/`
-   Su Windows è `%APPDATA%\FreeCAD\Mod\`, che di solito è `C:\Users\''username''\Appdata\Roaming\FreeCAD\Mod\`
-   Su Mac OSX di solito è `/Users/username/Library/Preferences/FreeCAD/Mod/`. Un modo per accedere alla directory delle preferenze è utilizzare la voce di menu \"Finder\"

**Go → Go to Folder**, e inserire `~/Library/Preferences/FreeCAD`.


</div>

### Informazioni aggiuntive 

Ulteriori informazioni su come creare un ambiente di lavoro personalizzato si trovano in [Hub sviluppatori](Developer_hub/it.md) e in [Hub utenti avanzati](Power_users_hub/it.md).

Vedere anche la pagina [Come installare ambienti aggiuntivi](How_to_install_additional_workbenches/it.md).


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md)
