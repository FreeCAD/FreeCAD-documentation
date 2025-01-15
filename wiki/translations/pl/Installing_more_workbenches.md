# Installing more workbenches/pl
## Wprowadzenie

Od wersji 0.17 można łatwo dodawać [zewnętrzne środowiska pracy](External_workbenches/pl.md) za pomocą [menedżera dodatków](Std_AddonMgr/pl.md). Użytkownik nie musi robić nic więcej niż korzystać z tego narzędzia.

Czytaj dalej, aby uzyskać więcej informacji na temat instalacji środowisk pracy.



## Opis ogólny 

Środowiska pracy to nic innego jak kolekcje plików umieszczone w folderze. Folder ten jest zwykle skompresowany do archiwum zip. Podczas instalacji folder ten jest po prostu rozpakowywany i kopiowany do:


```python
$ROOT_DIR/Mod/
```

gdzie `$ROOT_DIR` jest katalogiem najwyższego poziomu przeszukiwanym przez FreeCAD podczas uruchamiania. Jest to zasadniczo to, co robi [Menadżer dodatków](Std_AddonMgr/pl.md).

Katalogi `Mod/` są skanowane przy każdym uruchomieniu FreeCAD, a dostępne środowiska pracy są automatycznie dodawane.



## Instalacja obejmująca cały system 

Środowiska pracy zainstalowane w ten sposób będą dostępne dla wszystkich użytkowników. W zależności od systemu, dostęp do katalogu instalacyjnego może wymagać uprawnień administratora.

Skopiuj folder środowiska pracy do katalogu `$INSTALL_DIR/Mod/`, gdzie `$INSTALL_DIR` jest katalogiem instalacyjnym programu FreeCAD.

-   W systemie Linux jest to zazwyczaj `/usr/share/freecad/Mod/`.
-   W systemie Windows jest to zwykle `C:\Program Files\FreeCAD\Mod\`.
-   Na macOS jest to zazwyczaj `/Applications/FreeCAD/Mod/`.



## Instalacja dla pojedynczego użytkownika 

Środowiska pracy zainstalowane w ten sposób będą dostępne tylko dla jednego użytkownika, ale nie będą wymagały żadnych uprawnień administratora.

Skopiuj folder środowiska pracy do katalogu `$USER_DIR/Mod/`, gdzie `$USER_DIR` jest katalogiem FreeCAD dla konkretnego `username`. *(można go znaleźć wpisując `App.getUserAppDataDir()` w [konsoli Python](Python_console/pl.md))*.

-   W systemie Linux jest to zazwyczaj `/home/username/.local/share/FreeCAD/Mod/`.
-   W systemie Windows jest to `%APPDATA%\FreeCAD\Mod\`, czyli zwykle `C:\Users\username\Appdata\Roaming\FreeCAD\Mod\`.
-   Na macOS jest to zwykle `/Users/username/Library/Application Support/FreeCAD/Mod/`.



## Informacje dodatkowe 

Dodatkowe informacje na temat tworzenia niestandardowego środowiska pracy można znaleźć na stronach [Centrum Power użytkowników](Power_users_hub/pl.md) i [Centrum programisty](Developer_hub/pl.md).

Zobacz także szczegółowy opis na stronie [Instalacja zewnętrznych środowisk pracy](How_to_install_additional_workbenches/pl.md).



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Installing more workbenches/pl
