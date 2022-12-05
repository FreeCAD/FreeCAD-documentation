# Developer hub/ru
{{TOCright}} <img alt="" src=images/Crystal_Clear_app_tutorials.png  style="width:64px;">



Это раздел для тех, кто хочет принять участие в разработке FreeCAD.

Этот раздел находятся в стадии разработки. Если вы не можете найти информацию, которую ищете, или нашли полезную информацию, на которую мы не сослались, пожалуйста, оставьте комментарий на [форуме](http://forum.freecadweb.org/index.php?sid=5f84150e79db8842e277b042077097ff) и кто-нибудь заглянет в него (или, если вы уверены в своих знаниях, почему бы не отредактировать эту страницу самостоятельно!).

## Документация для Разработчиков 

Документация для разработчиков включает в себя следующие разделы:

### Компиляция FreeCAD 

-   [Github репозиторий](https://github.com/FreeCAD/FreeCAD). Если вы новичок, в git изучите [управление исходным кодом](Source_code_management/ru.md)
-   [Компиляция с Docker](Compile_on_Docker/ru.md)
-   [Компиляция в Windows](Compile_on_Windows/ru.md)
-   [Компиляция в Linux](Compile_on_Linux/ru.md)
-   [Компиляция в MacOS](Compile_on_MacOS/ru.md)
-   [Детали лицензий](Licence/ru.md) про FreeCAD лицензии
-   [Сторонние Библиотеки](Third_Party_Libraries/ru.md)
-   [Сторонние Инструменты](Third_Party_Tools/ru.md)
-   [Запуск и Конфигурирование](Start_up_and_Configuration/ru.md)
-   [Документирование исходников](Source_documentation/ru.md)
-   Используйте [Систему отслеживания Багов](Tracker/ru.md) когда у вас есть проблема или вы думаете, что, возможно, нашли ошибку

### Упаковывание

[Упаковка](Packaging.md) заключается в том, чтобы взять скомпилированные двоичные файлы и исходные файлы Python FreeCAD и распространить их для использования в определенной системе.

-   [Упаковывание в Linux](Linux_packaging/ru.md)
    -   [Debian разработка](Debian_development/ru.md)
    -   [Debian Unstable](Debian_Unstable/ru.md)
    -   [Git build пакет](Git_buildpackage/ru.md)
-   [Упаковывание в Windows](Windows_packaging/ru.md)
-   [Упаковывание в MacOS](MacOS_packaging/ru.md)

### Инструменты Поддержки Сборки 


<div class="mw-translate-fuzzy">

-   The [Инструметы сборки FreeCAD](FreeCAD_Build_Tool/ru.md)
    -   [Создание Модулей](Module_Creation/ru.md) в FreeCAD
-   [Отладка](Debugging/ru.md) FreeCAD
-   [Тестирование](Testing/ru.md) FreeCAD
-   [Компиляция FreeCAD (способы ускорения)](Compiling_(Speeding_up)/ru.md)
-   [(CI) Непрерывная Интеграция](Continuous_Integration/ru.md)


</div>

### Модифицирование FreeCAD 

-   Объяснение структуры [исходного кода FreeCAD](The_FreeCAD_source_code/ru.md)
-   [Отправка патчей](Tracker/ru#Отправка_патчей.md)
-   Добавление [особенностей](Gui_Command/ru.md) в FreeCAD или в Верстак
-   [Брендинг](Branding/ru.md) или *как придать FreeCAD уникальный вид*
-   [Иллюстрации](Artwork/ru.md), которые мы создали для FreeCAD и которые вы можете свободно использовать повторно
-   [Руководство по оформлению](Artwork_Guidelines/ru.md) \"стандарты\" для иконок
-   [Локализация и Перевод FreeCAD](Localisation/ru.md)
-   [Дополнительные модули Python](Extra_python_modules/ru.md), или *как как разширить возможности python внутри FreeCAD*
-   [Google Summer of Code](Google_Summer_of_Code.md) для тех кто хочет принять участие в программе поддержки студентов Google
-   [Тонкая настройка](Fine-tuning/ru.md) содержит информацию о различных параметрах и переключателях параметров, которые могут помоч устранить некоторые проблемы
-   [Обертывание C++ класса в Python](Wrapping_a_Cplusplus_class_in_Python/ru.md) содержит информацию о том, как создать Python обертку для C++ класса

-   [Перевод внешних верстаков](Translating_an_external_workbench/ru.md)

### Руководство для разработчика модуля 

[FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide): This is an ebook under writing on github, please fork and send pull request to contribute.

Chapters:

-   Overview and Software Architecture
-   Source code structure
-   Base and App module
-   Gui module
-   Python wrapping
-   Modular design
-   Fem module source analysis (mixed C++ and Python)
-   Development of CFD Module (pure Python)
-   Module testing and debugging
-   Contribute code with git

Latest pdf preview can be downoaded from [pdf folder](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide/tree/master/pdf) of this git repo

### Внутренние устройство 

#### OpenCascade Documentation 

OpenCascade is a software development platform for 3D surface and solid modeling, CAD data exchange, and visualization, mostly in the form of C++ libraries.

-   [Roman Lygin\'s tutorials](http://opencascade.wikidot.com/romansarticles)
-   [Full Online Documentation](https://dev.opencascade.org/cdoc/overview/html/index.html)
-   [Reference Manual](https://dev.opencascade.org/doc/refman/html/index.html)
-   [The openCascade wiki](http://opencascade.wikidot.com) (currently containing ?? Chinese spam)

#### Про формат файла 


<div class="mw-translate-fuzzy">

[Формат файла FCStd](File_Format_FCStd.md). Файлы, созданные с помощью FreeCAD, являются `.zip` файлами, включающими в себя BREP геометрию, а также XML-данные, описывающие документ.


</div>

#### Решатель Эскизов (Sketcher solver) 

-   [Sketcher Solver Architecture Booklet](https://forum.freecadweb.org/viewtopic.php?f=10&t=36355) (forum thread), [source](https://github.com/abdullahtahiriyo/FreeCADBooks/tree/master/FreeCAD_Solver_Architecture) in GitHub.
-   [PlaneGCS solver](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/) in the FreeCAD source code; important files are [GCS.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/GCS.cpp) and [SubSystem.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Sketcher/App/planegcs/SubSystem.cpp).
-   [Recent Several Sketcher improvements](https://forum.freecadweb.org/viewtopic.php?f=9&t=29192).

The sketcher solver isn\'t perfect, as there are some issues with numerical precision when using large values, see [Adventure of fixing sketcher solver for large sketches](https://forum.freecadweb.org/viewtopic.php?f=10&t=40502).

The development of a new solver architecture could improve the way the solver is used both in the [Sketcher Workbench](Sketcher_Workbench.md), and for assembly of 3D bodies. See [Reimplementing constraint solver](https://forum.freecadweb.org/viewtopic.php?f=20&t=40525).

## Дорожная карта проекта 

FreeCAD, though usable in certain areas, is at the beginning of a long way into the CAD mainstream. There is still a lot to do to reach a state where we can compete with commercial software.

[FreeCAD 1.0 Development Cycle](FreeCAD_1.0_Development_Cycle.md)

## Сообщество

-   [IRC channel](irc://chat.freenode.net/freecad) ,synchronized with [gitter channel](https://gitter.im/FreeCAD/FreeCAD)
-   [Development forum](https://forum.freecadweb.org/viewforum.php?f=6)

-   [Development roadmap](Development_roadmap.md)

## Авторы

[Участники проекта](Contributors/ru.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Hubs](Category_Hubs.md) > [Developer Documentation](Category_Developer Documentation.md) > Developer hub/ru
