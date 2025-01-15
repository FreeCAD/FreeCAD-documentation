# Installing more workbenches/ru
## Введение

Начиная с v0.17 легко добавить [внешний верстак](external_workbenches/ru.md), используя [Addon Manager](Std_AddonMgr/ru.md). Обычному пользователю ничего не требуется кроме использования этого инструмента.

Читайте далее для получения дополнительной информации относительно установки верстаков.



## Общее описание 

Workbenches are nothing more than collections of files that are placed in a folder. This folder is usually compressed into a zip archive. On installation, this folder is simply uncompressed and copied to


```python
$ROOT_DIR/Mod/
```

where `$ROOT_DIR` is a top level directory searched by FreeCAD on startup. This is essentially what the [Addon Manager](Std_AddonMgr.md) does.

The `Mod/` directories are scanned every time FreeCAD is started, and the available workbenches are automatically added.

## Installing system-wide 

Workbenches installed in this way will be available to all users. Depending on your system, you might need administrator privileges to access the installation directory.

Copy the workbench folder into `$INSTALL_DIR/Mod/`, where `$INSTALL_DIR` is the FreeCAD installation directory.

-   On Linux it is usually `/usr/share/freecad/Mod/`
-   On Windows it is usually `C:\Program Files\FreeCAD\Mod\`
-   On macOS it is usually `/Applications/FreeCAD/Mod/`

## Installing for a single user 

Workbenches installed in this way will be available only to one user, but will not require any administrator privileges.

Copy the workbench folder into `$USER_DIR/Mod/`, where `$USER_DIR` is the FreeCAD directory for a particular `username` (you can find the latter by typing `App.getUserAppDataDir()` in the [Python console](Python_console.md)).

-   On Linux it is usually `/home/username/.local/share/FreeCAD/Mod/`
-   On Windows it is `%APPDATA%\FreeCAD\Mod\`, which is usually `C:\Users\username\Appdata\Roaming\FreeCAD\Mod\`
-   On macOS it is usually `/Users/username/Library/Application Support/FreeCAD/Mod/`.



## Дополнительная информация 

Дополнительная информация о том, как создать пользовательский верстак, может быть найдена на [хабе опытных пользователей](Power_users_hub/ru.md) и [хабе разработчиков](Developer_hub/ru.md).

Смотрите так же детальное описание [как установить дополнительные верстаки](How_to_install_additional_workbenches.md).



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Installing more workbenches/ru
