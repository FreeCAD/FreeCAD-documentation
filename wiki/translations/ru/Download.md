# Download/ru
{{TOCright}}

## Текущая стабильная версия 

Релиз FreeCAD 0.20 (29177) был опубликован 14-06-2022. Чтобы узнать о нововедениях, смотри [примечания к выпуску](Release_notes_0.20/ru.md).

Контрольные суммы SHA256 для проверки целостности вашей загрузки вы можете найти на [странице релиза 0.20](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.20).

Предыдущие версии можно загрузить со страницы [релизов](https   *//github.com/FreeCAD/FreeCAD/releases).

+   *   *+---+   *   *+---+   *   *+
| ![](images/Windows.png )                                                                                                  |   | ![](images/Mac.png )                                                                                |   | ![](images/AppImage-logo.png )         |
|                                                                                                                                 |   |                                                                                                       |   |                                                    |
| [Install on Windows](Installing_on_Windows.md)                                                                          |   | [Install on Mac](Installing_on_Mac.md)                                                        |   | [Install on Linux](Installing_on_Linux.md) |
|                                                                                                                                 |   |                                                                                                       |   |                                                    |
| [64-bit](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.20/FreeCAD-0.20.0-WIN-x64-installer-1.exe) (includes installer) |   | [macOS 64-bit](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.20/FreeCAD-0.20.0-OSX-i386.dmg) |   | [AppImage 64-bit](AppImage.md)             |
++---++---++

### Примечания для пользователей Windows 

-   Поддерживаются следующие версии Windows   * 7/8/10/11.
-   Портативная версия, не требующая установки доступна на странице [релиза](https   *//github.com/FreeCAD/FreeCAD/releases/).
-   Пакет также можно установить из менеджера пакетов [Chocolatey](https   *//chocolatey.org/packages/freecad).

### Примечание для пользователей Mac OS X 

Минимальная поддерживаемая версия Mac OS X   * 10.12 Sierra.

### Примечания для GNU/Linux пользователей 

Большинство дистрибутивов поддерживают FreeCAD из их официальных репозиториев, однако, если дистрибутив не следует модели гладкого обновления, версия может быть устаревшей. Вместо установки из репозитория вы можете загрузить AppImage по ссылке сверху, разрешить загруженному файлу права на исполнения и запустить его без установки.

Смотрите страницу [Установка в Linux](Installing_on_Linux/ru.md) насчёт дополнительных опций установки, включая однодневные сборки для Ubuntu и производных.

Портативную версию, не требующую установки, можно создать, запустив FreeCAD с помощью следующих команд   * {{Version/ru|0.19}} 
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD-0.20.0-Linux-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD-0.20.0-Linux-x86_64.AppImage
```

Дополнительную информацию о переменных среды FreeCAD можно найти на [странице конфигурирования](Start_up_and_Configuration/ru#Переменные_Среды_Окружения.md).

## Разрабатываемые версии 

FreeCAD активно развивается.

-   Для пользователей Linux, посмотрите разрабатыаемую версию [AppImage](AppImage/ru.md).
-   По поводу сборок для MacOS и Windows, а также исходных кодов, смотрите страницу [еженедельных сборок](https   *//github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds)
-   Чтобы скомпилировать новейший исходный код, смотри страницу [Компиляция](Compiling/ru.md).

## Дополнительные модули и макросы 

Сообщество FreeCAD предлагает множество различных модулей и макросов. Начиная с версии 0.17 они могут быть легко установлены напрямую из FreeCAD через [Менеджер дополнений](Std_AddonMgr/ru.md)<img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;">.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Download/ru
