# Download/ru
## Текущая стабильная версия 


<div class="mw-translate-fuzzy">

Релиз FreeCAD версии 0.20.2 (29603) был опубликован 07.12.2022. Чтобы узнать о нововведениях, ознакомьтесь с [примечаниями к выпуску](Release_notes_0.20/ru.md).


</div>


<div class="mw-translate-fuzzy">

Контрольные суммы SHA256 для проверки целостности вашей загрузки вы можете найти на [странице релиза 0.20.2](https://github.com/FreeCAD/FreeCAD/releases/tag/0.20.2).


</div>

Предыдущие версии можно загрузить со страницы [релизов](https://github.com/FreeCAD/FreeCAD/releases).

+::+::+::+
| ![](images/Windows.png )                                                                                                | ![](images/Mac.png )                                                                                                | ![](images/Linux_with_text.png )                                                                        |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [Install instructions](Installing_on_Windows.md)                                                                      | [Install instructions](Installing_on_Mac.md)                                                                  | [Install instructions](Installing_on_Linux.md)                                                                |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-WIN-x64-installer-1.exe)        | [ARM (M1/M2) disk image](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-macOS-arm64.dmg)  | [x86_64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Linux-x86_64.AppImage)   |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [64-bit portable version (.7z)](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Windows-x86_64.7z) | [Intel disk image](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-macOS-intel-x86_64.dmg) | [aarch64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Linux-aarch64.AppImage) |
++++

### Notes for Windows users 


<div class="mw-translate-fuzzy">

### Примечания для пользователей Windows 

-   Поддерживаются следующие версии Windows: 64-разрядные версии 7/8/10/11. 32-разрядная версия Windows не поддерживается.
-   Портативная версия, не требующая установки доступна на странице [релиза](https://github.com/FreeCAD/FreeCAD/releases/).
-   Пакет также можно установить из менеджера пакетов [Chocolatey](https://chocolatey.org/packages/freecad).


</div>

### Notes for macOS users 


<div class="mw-translate-fuzzy">

### Примечания для пользователей macOS 

macOS 10.12 Sierra --- минимальная поддерживаемая версия.


</div>



### Примечания для GNU/Linux пользователей 

Большинство дистрибутивов поддерживают FreeCAD из их официальных репозиториев, однако, если дистрибутив не следует модели гладкого обновления, версия может быть устаревшей. Вместо установки из репозитория вы можете загрузить AppImage по ссылке сверху, разрешить загруженному файлу права на исполнения и запустить его без установки.

Смотрите страницу [Установка в Linux](Installing_on_Linux/ru.md) насчёт дополнительных опций установки, включая однодневные сборки для Ubuntu и производных.

Портативную версию, не требующую установки, можно создать, запустив FreeCAD с следующими командами:


{{Code|lang=text|code=
cd path/to/directory_containing_AppImage/
chmod +x ./name_of_AppImage_file.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./name_of_AppImage_file.AppImage
}}

Дополнительную информацию о переменных среды FreeCAD можно найти на [странице конфигурирования](Start_up_and_Configuration/ru#Переменные_Среды_Окружения.md).

## Development versions 


<div class="mw-translate-fuzzy">

## Разрабатываемые версии 

FreeCAD активно развивается.

-   Для получения информации о сборках и исходном коде разработки, смотрите страницу [weekly builds](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds).
-   Чтобы скомпилировать новейший исходный код, смотри страницу [Компиляция](Compiling/ru.md).


</div>



## Дополнительные модули и макросы 

Сообщество FreeCAD предлагает множество различных модулей и макросов. Начиная с версии 0.17 они могут быть легко установлены напрямую из FreeCAD через <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Менеджер дополнений](Std_AddonMgr/ru.md).



---
⏵ [documentation index](../README.md) > Download/ru
