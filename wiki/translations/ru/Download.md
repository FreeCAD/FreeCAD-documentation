# Download/ru
## Текущая стабильная версия 

Релиз FreeCAD версии 0.20.2 (29603) был опубликован 07.12.2022. Чтобы узнать о нововведениях, ознакомьтесь с [примечаниями к выпуску](Release_notes_0.20/ru.md).

Контрольные суммы SHA256 для проверки целостности вашей загрузки вы можете найти на [странице релиза 0.20.2](https://github.com/FreeCAD/FreeCAD/releases/tag/0.20.2).

Предыдущие версии можно загрузить со страницы [релизов](https://github.com/FreeCAD/FreeCAD/releases).

+::+::+::+
| ![](images/Windows.png )                                                                                         | ![](images/Mac.png )                                                                                                             | ![](images/Linux_with_text.png )     |
|                                                                                                                        |                                                                                                                                    |                                                    |
| [Install on Windows](Installing_on_Windows.md)                                                                 | [Install on Mac](Installing_on_Mac.md)                                                                                     | [Install on Linux](Installing_on_Linux.md) |
|                                                                                                                        |                                                                                                                                    |                                                    |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/0.20.2/FreeCAD-0.20.2-WIN-x64-installer-3.exe) | [macOS 64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.20.2/FreeCAD_0.20.2-2022-12-27-conda-macOS-x86_64-py310.dmg) | [AppImage 64-bit](AppImage.md)             |
++++

### Примечания для пользователей Windows 

-   Поддерживаются следующие версии Windows: 64-разрядные версии 7/8/10/11. 32-разрядная версия Windows не поддерживается.
-   Портативная версия, не требующая установки доступна на странице [релиза](https://github.com/FreeCAD/FreeCAD/releases/).
-   Пакет также можно установить из менеджера пакетов [Chocolatey](https://chocolatey.org/packages/freecad).

### Примечания для пользователей macOS 

macOS 10.12 Sierra --- минимальная поддерживаемая версия.



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

FreeCAD активно развивается.

-   Для получения информации о сборках и исходном коде разработки, смотрите страницу [weekly builds](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds).
-   Чтобы скомпилировать новейший исходный код, смотри страницу [Компиляция](Compiling/ru.md).



## Дополнительные модули и макросы 

Сообщество FreeCAD предлагает множество различных модулей и макросов. Начиная с версии 0.17 они могут быть легко установлены напрямую из FreeCAD через <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Менеджер дополнений](Std_AddonMgr/ru.md).



---
⏵ [documentation index](../README.md) > Download/ru
