# Download/ru
{{TOCright}}

## Текущая стабильная версия 


<div class="mw-translate-fuzzy">

Первый релиз FreeCAD 0.19.2 (24291) был опубликован 2021-04-22. Чтобы узнать, о нововедениях, см. [примечания к выпуску](Release_notes_0.19/ru.md).


</div>


<div class="mw-translate-fuzzy">

Контрольные суммы SHA256 для проверки целостности вашей загрузки вы можете найти на [страница выпуска 0.19.2](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.19.2).


</div>


<div class="mw-translate-fuzzy">

Предыдущие версии можно загрузить со страницы [всех выпусков](https   *//github.com/FreeCAD/FreeCAD/releases)


</div>

+   *   *+---+   *   *+---+   *   *+
| ![](images/Windows.png )                                                                                                    |   | ![](images/Mac.png )                                                                                          |   | ![](images/AppImage-logo.png )         |
|                                                                                                                                   |   |                                                                                                                 |   |                                                    |
| [Install on Windows](Installing_on_Windows.md)                                                                            |   | [Install on Mac](Installing_on_Mac.md)                                                                  |   | [Install on Linux](Installing_on_Linux.md) |
|                                                                                                                                   |   |                                                                                                                 |   |                                                    |
| [64-bit](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.19.3/FreeCAD-0.19.3-WIN-x64-installer-4.exe) (includes installer) |   | [macOS 64-bit](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.19.3/FreeCAD_0.19.3-OSX-x86_64-conda.dmg) |   | [AppImage 64-bit](AppImage.md)             |
++---++---++


<div class="mw-translate-fuzzy">

### Примечания для Windows пользователей 

-   32-битный установщик (x86) поддерживает следующие версии Windows   * 7/8/10
-   64-битный установщик (x64) поддерживает следующие версии Windows   * 7/8/10
-   portable версия ([64-bit](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD-0.19.2.7b5e18a-WIN-x64-portable1.7z)) не нуждающаяся в установке, находится на странице релиза.
-   Пакет также можно установить из [Chocolatey](https   *//chocolatey.org/packages/freecad) менеджера.


</div>


<div class="mw-translate-fuzzy">

### Примечание для Mac OS X пользователей 

Минимальная поддерживаемая версия   * Mac OS X 10.12 *Sierra*


</div>

### Примечания для GNU/Linux пользователей 

Большинство дистрибутивов поддерживают FreeCAD из их официальных репозиториев, однако, если дистрибутив не следует модели гладкого обновления, версия может быть устаревшей. Вместо установки из репозитория вы можете загрузить AppImage по ссылке сверху, разрешить загруженному файлу права на исполнения и запустить его без установки.

Смотрите страницу [Установка в Linux](Installing_on_Linux/ru.md) насчёт дополнительных опций установки, включая однодневные сборки для Ubuntu и производных.


<div class="mw-translate-fuzzy">

Портативную версию, не требующую установки, можно создать, запустив FreeCAD с помощью следующих команд   * {{Version/ru|0.19}} 
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
```


</div>

Дополнительную информацию о переменных среды FreeCAD можно найти на [странице конфигурирования](Start_up_and_Configuration/ru#Переменные_Среды_Окружения.md).

## Разрабатываемые версии 

FreeCAD активно развивается.

-   Для пользователей Linux, посмотрите разрабатыаемую версию [AppImage](AppImage/ru.md).
-   По поводу сборок для MacOS и Windows, а также исходных кодов, смотрите страницу [еженедельных сборок](https   *//github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds)
-   Чтобы скомпилировать новейший исходный код, см. [Компиляция](Compiling/ru.md).

## Дополнительные модули и макросы 


<div class="mw-translate-fuzzy">

Сообщество FreeCAD предлагает множество различных модулей и макросов. Начиная с версии 0.17 они могут быть легко установлены напрямую из FreeCAD через [Менеджер дополнений](Std_AddonMgr/ru.md)<img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;">.


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Download/ru
