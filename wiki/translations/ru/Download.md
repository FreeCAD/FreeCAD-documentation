# Download/ru
## Текущая стабильная версия 


<div class="mw-translate-fuzzy">

Релиз FreeCAD версии 0.21.2 был опубликован 14.11.2023. Чтобы узнать о нововведениях, ознакомьтесь с [примечаниями к выпуску](Release_notes_0.21/ru.md).


</div>


<div class="mw-translate-fuzzy">

Контрольные суммы SHA256 для проверки целостности вашей загрузки вы можете найти на [странице релиза 0.21.2](https://github.com/FreeCAD/FreeCAD/releases/tag/0.21.2).


</div>

Предыдущие версии можно загрузить со страницы [релизов](https://github.com/FreeCAD/FreeCAD/releases).

+::+::+::+
| ![](images/Windows.png )                                                                                                          | ![](images/Mac.png )                                                                                                            | ![](images/Linux_with_text.png )                                                                                  |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [Install instructions](Installing_on_Windows.md)                                                                                | [Install instructions](Installing_on_Mac.md)                                                                              | [Install instructions](Installing_on_Linux.md)                                                                          |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Windows-x86_64-installer-1.exe)       | [ARM (M-series) disk image](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-macOS-arm64-py311.dmg) | [x86_64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Linux-x86_64-py311.AppImage)   |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [64-bit portable version (.7z)](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Windows-x86_64-py311.7z) | [Intel disk image](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-macOS-x86_64-py311.dmg)         | [aarch64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Linux-aarch64-py311.AppImage) |
++++



### Примечания для пользователей Windows 


<div class="mw-translate-fuzzy">

-   Поддерживаются следующие версии Windows: 64-разрядные версии 7/8/10/11. 32-разрядная версия Windows не поддерживается.
-   Пакет также можно установить из менеджера пакетов [Chocolatey](https://chocolatey.org/packages/freecad). Пакет из Chocolatey пока не в новейшей версии.


</div>



### Примечания для пользователей macOS 


<div class="mw-translate-fuzzy">

-   macOS 10.12 Sierra --- минимальная поддерживаемая версия.
-   Для macOS 12 и более ранних версий следует использовать «Неподписанный образ диска Intel», подписанная версия в этих системах не работает.


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



## Разрабатываемые версии 


<div class="mw-translate-fuzzy">

FreeCAD активно развивается.

-   Для получения информации о сборках и исходном коде разработки, смотрите страницу [weekly builds](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds).
-   Чтобы скомпилировать новейший исходный код, смотри страницу [Компиляция](Compiling/ru.md).


</div>



## Дополнительные модули и макросы 


<div class="mw-translate-fuzzy">

Сообщество FreeCAD предлагает множество различных модулей и макросов. Начиная с версии 0.17 они могут быть легко установлены напрямую из FreeCAD через <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Менеджер дополнений](Std_AddonMgr/ru.md).


</div>



---
⏵ [documentation index](../README.md) > Download/ru
