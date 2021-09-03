





{{VeryImportantMessage|Существует экспериментальный контейнер FreeCAD Docker, который протестирован для разработки FreeCAD. Подробнее на странице [Компиляция в Docker](Compile_on_Docker/ru.md)}}


{{TOCright}}

## Обзор

В последних дистрибутивах Linux, FreeCAD, как правило, собирается легко, поскольку все зависимости обычно предоставляются менеджером пакетов. В основном сборка включает 3 этапа:

1.  Получение исходного кода FreeCAD.
2.  Получение зависимостей, или пакетов, от которых зависит FreeCAD
3.  Настройка с помощью `cmake` и компиляция с помощью `make`.

Ниже вы найдете подробное описание процесса сборки, некоторых [скриптов компиляции](#Automatic_build_scripts.md) и особенностей, с которыми Вы можете столкнуться. Если вы найдете ошибки, устаревшие сведения (дистрибутивы Linux меняются быстро), или если вы используете дистрибутив, которого нет в списке, обсудите вопрос на [форуме](https://forum.freecadweb.org/index.php), и помогите нам исправить это.

<img alt="" src=images/FreeCAD_source_compilation_workflow.svg  style="width:800px;">


*Общий рабочий процесс для компиляции FreeCAD из исходников. В систем должны быть как сторонние зависимости, так и исходные коды самого FreeCAD. CMake конфигурирует систему так чтобы весь проект скомпилировался одной инструкцией make.*

## Получение исходных кодов {#получение_исходных_кодов}

### Git


<div class="mw-translate-fuzzy">

Лучший способ получить код это клонировать только-для-чтения [репозиторий Git](https://github.com/FreeCAD/FreeCAD). Для этого вам потребуется программа `git`, которую легко установить в большинстве дистрибутивов Linux, или получить на [официальном веб-сайте](http://git-scm.com/).


</div>

Git can be installed via the following command:


{{Code|lang=bash|code=
sudo apt install git
}}


<div class="mw-translate-fuzzy">

Следующая команда, копирует последнюю версию исходного кода FreeCAD в папку `freecad-source`.


</div>


{{Code|lang=bash|code=
git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
}}


<div class="mw-translate-fuzzy">

Для получения дополнительной информации об использовании Git и внесении кода в проект, посмотрите [управление исходным кодом](Source_code_management/ru.md).


</div>

### Архив с исходным кодом {#архив_с_исходным_кодом}

Кроме того, вы можете загрузить исходники непосредственно с [GitHub](https://github.com/FreeCAD/FreeCAD/releases/latest), в качестве `.zip` или `.tar.gz` архива, и распаковать его в заданный каталог.

## Установка зависимостей (Dependencies) {#установка_зависимостей_dependencies}

Для компиляции FreeCAD необходимо установить требуемые зависимости (dependencies), упомянутые в [сторонних библиотеках](Third_Party_Libraries/ru.md); пакеты, содержащие эти зависимости для различных дистрибутивов Linux, перечислены ниже. Обратите внимание, что имена и доступность библиотек будут зависеть от вашего конкретного дистрибутива; если ваш дистрибутив устарел, некоторые пакеты могут быть недоступны или иметь другое имя. В этом случае посмотрите раздел [↓ старые и нестандартные дистрибутивы](#Older_and_non-conventional_distributions.md) расположенный ниже.


<div class="mw-translate-fuzzy">

Как только у вас будут установлены все зависимости, приступайте к [сборке FreeCAD](#Сборка_FreeCAD.md).


</div>

Обратите внимание, что размер исходного кода FreeCAD составляет около 500 МБ; он может быть в три раза больше, если вы клонируете репозиторий Git со всей историей его изменений. Для получения всех зависимостей может потребоваться загрузка 500 МБ или более новых файлов; при распаковке этих файлов может потребоваться 1500 МБ или более места. Также имейте в виду, что в процессе компиляции может быть создано до 1500 МБ дополнительных файлов, поскольку система копирует и изменяет весь исходный код. Поэтому при попытке компиляции убедитесь, что на вашем жестком диске достаточно свободного места, по крайней мере, не менее 4 ГБ.


<div class="mw-collapsible mw-collapsed toccolours">

### Debian и Ubuntu {#debian_и_ubuntu}


<div class="mw-collapsible-content">

В системах основанных на Debian (Debian, Ubuntu, Mint, и т.п.) довольно легко установить все необходимые зависимости. Большинство библиотек доступны через `apt` или менеджер пакетов Synaptic.

Если вы уже установили FreeCAD из официальных репозиториев, вы можете установить зависимости (dependencies) для его сборки с помощью этой единственной строки кода в терминале:


```python
sudo apt build-dep freecad
```

Однако, если версия FreeCAD в репозиториях старая, зависимости (dependencies) могут быть уже устаревшими для компиляции последней версии FreeCAD. Поэтому, пожалуйста, убедитесь, что вы установили следующие пакеты.

Эти пакеты необходимы для успешной компиляции в целом:

-    `build-essential`, устанавливает компиляторы C и C++ , библиотеки разработки C и `make` утилиту.

-    `cmake`, необходимый инструмент для настройки исходников FreeCAD. Вы также можете установить `cmake-gui` и `cmake-curses-gui` чтобы иметь графический интерфейс для данной утилиты.

-    `libtool`, необходимые инструменты для создания shared библиотек.

-    `lsb-release`, стандартная утилита базовой отчетности обычно уже установлена в системе Debian и позволяет программно различать чистую установку Debian или ее вариант, такой как Ubuntu или Linux Mint. Не удаляйте этот пакет, так как от него могут зависеть многие другие системные пакеты.

При компиляции FreeCAD используется язык Python, и он также используется в runtime в качестве языка сценариев. Если вы используете дистрибутив на основе Debian, интерпретатор Python как правило уже установлен в нем.

-    `python3`
    

-    `swig`, это инструмент, который создает интерфейсы между кодом C++ и Python.

Пожалуйста, убедитесь, что у вас установлен Python 3. Python 2 устарел в 2019 году, свежая разработка FreeCAD не тестируется с этой версией языка.

Boost библиотеки должны быть обязательно установлены:

-    `libboost-dev`
    

-    `libboost-date-time-dev`
    

-    `libboost-filesystem-dev`
    

-    `libboost-graph-dev`
    

-    `libboost-iostreams-dev`
    

-    `libboost-program-options-dev`
    

-    `libboost-python-dev`
    

-    `libboost-regex-dev`
    

-    `libboost-serialization-dev`
    

-    `libboost-thread-dev`
    

Должны быть установлены Coin библиотеки:

-    `libcoin80-dev`, для Debian Jessie, Stretch, Ubuntu с 16.04 до 18.10, или

-    `libcoin-dev`, для Debian Buster, Ubuntu 19.04 и выше, а так же Ubuntu 18.04/18.10 вместе с [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Official_Ubuntu_repository.md) должны быть добавлены в иходники.

Несколько библиотек, которые занимаются вычислениями, триангулированными поверхностями, сортировкой, мешами (meshes), компьютерным зрением, картографическими проекциями, 3D-визуализацией, оконной системой X11, парсингом XML и чтением Zip-файлов:

-    `libeigen3-dev`
    

-    `libgts-bin`
    

-    `libgts-dev`
    

-    `libkdtree++-dev`
    

-    `libmedc-dev`
    

-    `libopencv-dev`or `libcv-dev`

-    `libproj-dev`
    

-    `libvtk7-dev`or `libvtk6-dev`

-    `libx11-dev`
    

-    `libxerces-c-dev`
    

-    `libzipios++-dev`
    


<div class="mw-collapsible mw-collapsed" style="background-color:#e0e0e0">

#### Python 2 и Qt4 {#python_2_и_qt4}

Python 2 и Qt4 уже устарели и не рекомендуются к применению. Начиная с версии 0.20, в FreeCAD они больше не поддерживаются.


<div class="mw-collapsible-content">

При компиляции FreeCAD в Debian Jessie, Stretch, Ubuntu 16.04, используйте Python 2 и Qt4, установив следующие зависимости:

-    `qt4-dev-tools`
    

-    `libqt4-dev`
    

-    `libqt4-opengl-dev`
    

-    `libqtwebkit-dev`
    

-    `libshiboken-dev`
    

-    `libpyside-dev`
    

-    `pyside-tools`
    

-    `python-dev`
    

-    `python-matplotlib`
    

-    `python-pivy`
    

-    `python-ply`
    

-    `python-pyside`
    


</div>


</div>

#### Python 3 и Qt5 {#python_3_и_qt5}

При компиляции FreeCAD в Debian Buster, Ubuntu 19.04 и выше, а также Ubuntu 18.04/18.10 с [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Official_Ubuntu_repository.md) добавленным в ваш исходный код, установите следующие зависимости.

-    `qtbase5-dev`
    

-    `qttools5-dev`
    

-    `qt5-default`(if compiling 0.20 on a machine that still has Qt4)

-    `libqt5opengl5-dev`
    

-    `libqt5svg5-dev`
    

-    `libqt5webkit5-dev`or `qtwebengine5-dev`

-    `libqt5xmlpatterns5-dev`
    

-    `libqt5x11extras5-dev`
    

-    `libpyside2-dev`
    

-    `libshiboken2-dev`
    

-    `pyside2-tools`
    

-    `pyqt5-dev-tools`
    

-    `python3-dev`
    

-    `python3-matplotlib`
    

-    `python3-pivy`
    

-    `python3-ply`
    

-    `python3-pyside2.qtcore`
    

-    `python3-pyside2.qtgui`
    

-    `python3-pyside2.qtsvg`
    

-    `python3-pyside2.qtwidgets`
    

-    `python3-pyside2uic`
    

#### Ядро OpenCascade {#ядро_opencascade}

Ядро OpenCascade - это основная графическая библиотека для создания 3D-фигур. Она существует в виде официальной версии OCCT и виде версии для сообщества OCE. Версия для сообщества к применению больше не рекомендуется, так как она устарела.

Для Debian Buster и Ubuntu 18.10 и выше, а так же для Ubuntu 18.04 с [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Official_Ubuntu_repository.md) добавлеными в ваши исходники, установите официальные пакеты.

-    `libocct*-dev`-   
        `libocct-data-exchange-dev`
        

    -   
        `libocct-draw-dev`
        

    -   
        `libocct-foundation-dev`
        

    -   
        `libocct-modeling-algorithms-dev`
        

    -   
        `libocct-modeling-data-dev`
        

    -   
        `libocct-ocaf-dev`
        

    -   
        `libocct-visualization-dev`
        

-    `occt-draw`
    

Для Debian Jessie, Stretch, Ubuntu 16.04 и выше, установите community edition пакеты.

-    `liboce*-dev`-   
        `liboce-foundation-dev`
        

    -   
        `liboce-modeling-dev`
        

    -   
        `liboce-ocaf-dev`
        

    -   
        `liboce-ocaf-lite-dev`
        

    -   
        `liboce-visualization-dev`
        

-    `oce-draw`
    

Вы можете установить библиотеки по отдельности или сразу несколько с похожим именами используя символ звездочку \'\*\'. Замените `occ` на `oce` если вы хотите установить community редакцию библиотек.


```python
sudo apt install libocct*-dev
```

#### Необязательные к установке пакеты {#необязательные_к_установке_пакеты}

При желании вы также можете установить эти дополнительные пакеты:

-    `libsimage-dev`, чтобы Coin поддерживал дополнительные форматы файлов изображений.

-    `doxygen`и `libcoin-doc` (или `libcoin80-doc` для старых систем), если вы хотите автоматический генерировать документацию к исходному коду.

-    `libspnav-dev`, для поддержки [устройств 3D ввода](3D_input_devices/ru.md), таких как 3Dconnexion \"Space Navigator\" или \"Space Pilot\".

-    `checkinstall`, если вы хотите зарегистрировать установленные файлы в диспетчере пакетов вашей системы, чтобы вы могли удалить их позже.

#### Устаовка Python 3 и Qt5 одной командой {#устаовка_python_3_и_qt5_одной_командой}

Требуется, чтобы Pyside2 был доступен в Debian buster и [freecad-stable/freecad-daily PPAs](Installing_on_Linux#Official_Ubuntu_repository.md).


```python
sudo apt install cmake cmake-gui libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside2-dev libqt5opengl5-dev libqt5svg5-dev libqt5webkit5-dev libqt5x11extras5-dev libqt5xmlpatterns5-dev libshiboken2-dev libspnav-dev libvtk7-dev libx11-dev libxerces-c-dev libzipios++-dev occt-draw pyside2-tools python3-dev python3-matplotlib python3-pivy python3-ply python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qtsvg python3-pyside2.qtwidgets python3-pyside2uic qtbase5-dev qttools5-dev swig
```


<div class="mw-translate-fuzzy">

ПРИМЕЧАНИЕ: В некоторых версиях Ubuntu и некоторых версиях Qt вы получите сообщение об ошибке, что python3-pyside2uic не может быть найден-в этих системах вы можете безопасно опустить его. В Ubuntu 20.04 вам нужно будет добавить `pyqt5-dev-tools`. Более подробную информацию можно найти в [это обсуждение на форуме](https://forum.freecadweb.org/viewtopic.php?t=51324).


</div>


<div class="mw-collapsible mw-collapsed" style="background-color:#e0e0e0">

#### Установка Python 2 и Qt4 одной коммандой {#установка_python_2_и_qt4_одной_коммандой}

Это не рекомендуется для более новых установок, поскольку и Python 2 и Qt4 являются устаревшими.


<div class="mw-collapsible-content">


```python
sudo apt install cmake debhelper dh-exec dh-python libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin80-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside-dev libqt4-dev libqt4-opengl-dev libqtwebkit-dev libshiboken-dev libspnav-dev libvtk6-dev libx11-dev libxerces-c-dev libzipios++-dev lsb-release occt-draw pyside-tools python-dev python-matplotlib python-pivy python-ply swig
```

Пользователи Ubuntu 16.04, пожалуйста, ознакомьтесь также с обсуждением компиляции на форуме: [Компиляция в Linux (Kubuntu): CMake не может найти VTK](http://forum.freecadweb.org/viewtopic.php?f=4&t=16292).


</div>


</div>


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Raspberry Pi {#raspberry_pi}


<div class="mw-collapsible-content">

Выполните те же действия, что и в Debian и Ubuntu.

Сообщалось о проблемах при попытке компиляции в Raspbian с Python 3 и Qt5, но комбинация Python 3 и Qt4, похоже, работает для более старых версий FreeCAD.

Для более новых версий FreeCAD компиляция с Py3/Qt5 проходит успешно, если установлена операционная система Ubuntu 20.04.

Из-за различных проблем с Qt в этой версии обычные PySide tools не будут найдены. {{Code|lang=bash|code=
E: Unable to locate package python3-pyside2uic
}}

В этом случае мы можем установить пакеты из PyQt и создать символические ссылки на необходимые инструменты. {{Code|lang=bash|code=
sudo apt-get install pyqt5-dev
sudo apt-get install pyqt5-dev-tools
cd /usr/bin/
ln -s pyrcc5 pyside2-rcc
ln -s pyuic5 pyside2-uic
}}

Теперь компиляция может быть продолжена. {{Code|lang=bash|code=
cd freecad-build/
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DUSE_PYBIND11=ON
make -j2
}}

Параметр `-j` для `make` не должен превышать 3, поскольку Raspberry Pi имеет ограниченную память. На компиляцию уйдет несколько часов, поэтому лучше сделать это за ночь.

Дополнительная информация, [FreeCAD и Raspberry Pi 4](https://forum.freecadweb.org/viewtopic.php?f=42&t=37458&start=160#p396652).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Fedora


<div class="mw-collapsible-content">

Вам нужны следующие пакеты :

-   gcc-c++ (or possibly another C++ compiler?)
-   cmake
-   doxygen
-   swig
-   gettext
-   dos2unix
-   desktop-file-utils
-   libXmu-devel
-   freeimage-devel
-   mesa-libGLU-devel
-   OCE-devel
-   python
-   python-devel
-   python-pyside-devel
-   pyside-tools
-   boost-devel
-   tbb-devel
-   eigen3-devel
-   qt-devel
-   qt-webkit-devel
-   qt5-qtxmlpatterns
-   qt5-qttools-static
-   ode-devel
-   xerces-c
-   xerces-c-devel
-   opencv-devel
-   smesh-devel
-   Coin3
-   Coin3-devel


<div class="mw-translate-fuzzy">

(Не перепутайте \"Coin\" с \"coin\" - тот что с маленькой буквы это финансовый пакет. Апрель 2021, Coin4 и Coin4-devel доступны ) (если coin2 является последней доступной версией для вашей версии Fedora, используйте пакеты из <http://www.zultron.com/rpm-repo/>)


</div>

-   SoQt-devel
-   freetype
-   freetype-devel
-   vtk
-   med
-   med-devel

И дополнительно :


<div class="mw-translate-fuzzy">

-   libspnav-devel (для поддержки устройств 3Dconnexion, вроде Space Navigator или Space Pilot)
-   pivy ( <https://bugzilla.redhat.com/show_bug.cgi?id=458975> Pivy не обязателен, но нужен для модуля Draft)


</div>


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Gentoo


<div class="mw-collapsible-content">

Простейший путь проверить, какие пакеты нужны для компиляции FreeCAD это проверить через portage:

emerge -pv freecad

Вы получите список дополнительных пакетов, которые следует установить на Вашей системе.

Если FreeCAD недоступен в portage, он доступен в оверлее [waebbl](https://github.com/waebbl/waebbl-gentoo). Система отслеживания ошибок на оверлее waebbl Github может помочь решить некоторые проблемы, с которыми вы можете столкнуться. Оверлей предоставляет  freecad-9999 \</ tt\>, который вы можете выбрать для компиляции или просто использовать для получения зависимостей.

layman -a waebbl


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE


<div class="mw-collapsible-content">

#### Tumbleweed

Следующие команды установят пакеты, необходимые для создания FreeCAD с Qt5 и Python 3.


```python
zypper in --no-recommends -t pattern devel_C_C++ devel_qt5

zypper in libqt5-qtbase-devel libqt5-qtsvg-devel libqt5-qttools-devel boost-devel swig libboost_program_options-devel libboost_mpi_python3-devel libboost_system-devel libboost_program_options-devel libboost_regex-devel libboost_python3-devel libboost_thread-devel libboost_system-devel libboost_headers-devel libboost_graph-devel python3 python3-devel python3-matplotlib python3-matplotlib-qt5 python3-pyside2 python3-pyside2-devel python3-pivy gcc gcc-fortran cmake occt-devel libXi-devel opencv-devel libxerces-c-devel Coin-devel SoQt-devel freetype2-devel eigen3-devel libode6 vtk-devel libmed-devel hdf5-openmpi-devel openmpi2-devel netgen-devel freeglut-devel libspnav-devel f2c doxygen dos2unix glew-devel
```

Следующая команда установит Qt Creator и отладчик проекта GNU.


```pythonzypper in libqt5-creator gdb```

Если какие-либо пакеты отсутствуют, вы можете проверить Tumbleweed [1](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/FreeCAD.spec) \"FreeCAD.spec\" файл на [2](https://build.opensuse.org/package/show/openSUSE:Factory/FreeCAD) Откройте Службу сборки.

Также, проверьте, есть ли какие-либо исправления, которые вам необходимо использовать (например [0001-find-openmpi2-include-files.patch](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/0001-find-openmpi2-include-files.patch)).

#### Leap

Если есть разница между доступными пакетами на Tumbleweed и Leap, то вы можете прочитать Leap [3](https://build.opensuse.org/package/view_file/openSUSE:Leap:15.0/FreeCAD/FreeCAD.spec) файл \"FreeCAD.spec\" на [4](https://build.opensuse.org/) Откройте службу сборки, чтобы определить необходимые пакеты.

Смотрите [piano\_jonas unofficial \"Compile On openSUSE\" guide](https://forum.freecadweb.org/viewtopic.php?f=4&t=49726).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Arch Linux {#arch_linux}


<div class="mw-collapsible-content">

Вам понадобятся следующие библиотеки из официальных архивов:

-   boost
-   curl
-   desktop-file-utils
-   glew
-   hicolor-icon-theme
-   jsoncpp
-   libspnav
-   opencascade
-   shiboken2
-   xerces-c
-   pyside2
-   python-matplotlib
-   python-netcdf4
-   qt5-svg
-   qt5-webkit
-   qt5-webengine
-   cmake
-   eigen
-   git
-   gcc-fortran
-   pyside2-tools
-   swig
-   qt5-tools
-   shared-mime-info
-   coin
-   python-pivy
-   med


```python
sudo pacman -S boost curl desktop-file-utils glew hicolor-icon-theme jsoncpp libspnav opencascade shiboken2 xerces-c pyside2 python-matplotlib python-netcdf4 qt5-svg qt5-webkit qt5-webengine cmake eigen git gcc-fortran pyside2-tools swig qt5-tools shared-mime-info coin python-pivy med
```


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Более старые и нетрадиционные дистрибутивы {#более_старые_и_нетрадиционные_дистрибутивы}


<div class="mw-collapsible-content">

В других дистрибутивах у нас очень мало отзывов от пользователей, поэтому может быть сложнее найти необходимые пакеты.

Сначала попробуйте найти необходимые библиотеки, упомянутые в [сторонние библиотеки](Сторонние_библиотеки.md) в диспетчере пакетов. Остерегайтесь, что у некоторых из них может быть немного другое имя пакета; ищите `name`, но также `libname`, `name-dev`, `name-devel` и аналогичные. Если это невозможно, попробуйте скомпилировать эти библиотеки самостоятельно.

Для FreeCAD требуется версия компилятора GNU g++, равная или выше 3.0.0, так как FreeCAD в основном написан на C++. Во время компиляции выполняются некоторые сценарии Python, поэтому интерпретатор Python должен работать должным образом. Чтобы избежать каких-либо проблем с компоновщиком, также рекомендуется иметь пути к библиотеке в переменной `LD_LIBRARY_PATH` или в файле `ld.so.conf`. Это уже сделано в современных дистрибутивах Linux, но, возможно, потребуется установить в более старых.


</div>


</div>

### Pivy


<div class="mw-translate-fuzzy">

Pivy (обертки Python для Coin3d) не требуется для сборки FreeCAD или его запуска, но он необходим в качестве зависимости от среды выполнения для рабочего стола проекта. Если вы не собираетесь использовать эти инструментальные средства, вам не понадобится Pivy. Однако обратите внимание, что рабочий стол проекта используется внутри других рабочих столов, таких как Arch и BIM, поэтому для использования этих инструментальных средств также необходимо установить Pivy.


</div>

К ноябрю 2015 года устаревшая версия Pivy, включенная в исходный код FreeCAD, больше не будет компилироваться во многих системах. Это не большая проблема, так как обычно вы должны получить Pivy от менеджера пакетов вашего дистрибутива; если вы не можете найти Pivy, вам, возможно, придется скомпилировать его самостоятельно, см. Инструкции по компиляции Pivy.

### Отладочные символы {#отладочные_символы}

Для устранения неполадок в FreeCAD полезно иметь отладочные символы важных библиотек зависимостей, таких как Qt. Для этого попробуйте установить пакеты зависимостей, которые заканчиваются на `-dbg`, `-dbgsym`, `-debuginfo` или аналогичные, в зависимости от вашего дистрибутива Linux.


<div class="mw-translate-fuzzy">

Для Ubuntu вам, возможно, придется включить специальные репозитории, чтобы иметь возможность просматривать и устанавливать эти отладочные пакеты с помощью диспетчера пакетов. См.[Debug Symbol Packages](https://wiki.ubuntu.com/Debug_Symbol_Packages) для получения дополнительной информации.


</div>

## Сборка FreeCAD {#сборка_freecad}


{{VeryImportantMessage|Python 2 и Qt4 при сборке больше не поддерживается, а в версии 0.20 больше не поддерживается вообще. Допускается компиляция с Python 3 и Qt5. А для версии 0.20 требуется как минимум Python3.6 и Qt 5.9.}}

FreeCAD использует CMake в качестве основной системы сборки, она доступна во всех основных операционных системах. Компиляция с помощью CMake обычно очень проста и происходит в два этапа.

1.  CMake проверяет наличие в вашей системе всех необходимых программ и библиотек и создает `Makefile`, настроенный для второго шага. FreeCAD имеет несколько вариантов конфигурации на выбор, но он поставляется с разумными настройками по умолчанию. Некоторые альтернативы подробно описаны ниже.
2.  Сама компиляция, которая выполняется с помощью программы `make`, которая генерирует исполняемые файлы FreeCAD.

Поскольку FreeCAD - это крупное приложение, компиляция всего исходного кода может занять от 10 минут до одного часа, в зависимости от вашего процессора и количества ядер процессора, используемых для компиляции.

Вы можете создать код либо в исходном каталоге, либо из него. Строительство вне источника, как правило, является лучшим вариантом.

### Сборка вне папки исходников {#сборка_вне_папки_исходников}

Создание в отдельной папке удобнее, чем создание в том же каталоге, где находится исходный код, поскольку каждый раз, когда вы обновляете исходный код, CMake может разумно определить, какие файлы изменились, и перекомпилировались только то, что необходимо. Это очень полезно при тестировании различных ветвей Git, так как вы не путаете систему сборки.

Для сборки из исходного кода просто создайте каталог сборки `freecad-build`, отличный от вашей исходной папки FreeCAD, `freecad-source`; затем из этой точки каталога сборки `cmake` в нужную исходную папку. Вы также можете использовать `cmake-gui` или `ccmake` вместо `cmake` в приведенных ниже инструкциях. Как только `cmake` завершит конфигурацию среды, используйте `make` для запуска актуальной компиляции.


{{Code|lang=bash|code=
mkdir freecad-build
cd freecad-build
cmake ../freecad-source
make -j$(nproc --ignore=2)
}}

Примечание: если вы компилируете ветвь выпуска 0.19, вы должны конкретно указать, что вы компилируете с Qt5 и Python 3 \-- замените команду CMake выше на: {{Code|lang=bash|code=
cmake ../freecad-source -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3
}}

Опция `-j` `make` определяет, сколько задач (файлов) компилируется параллельно. Программа `nproc` выводит количество ядер процессора в вашей системе; используя ее вместе с опцией `-j`, вы можете обработать столько файлов, сколько у вас ядер, чтобы ускорить общую компиляцию программы. В приведенном выше примере он будет использовать все ядра вашей системы, кроме двух; это позволит вашему компьютеру реагировать на другие виды использования, пока компиляция выполняется в фоновом режиме. Исполняемый файл FreeCAD в конечном итоге появится в каталоге `freecad-build/bin`. См. также [Compiling (speeding up)](Compiling_(Speeding_up).md) для повышения скорости компиляции.

### Сборка в папке исходников {#сборка_в_папке_исходников}

Сборки с исходным кодом подходят, если вы хотите быстро скомпилировать версию FreeCAD и не собираетесь часто обновлять исходный код. В этом случае вы можете удалить скомпилированную программу и исходный код, только удалив одну папку.

Перейдите в исходный каталог и укажите `cmake` на текущий каталог (обозначенный одной точкой):


{{Code|lang=bash|code=
cd freecad-source
cmake . -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3
make -j$(nproc --ignore=2)
}}

Исполняемый файл FreeCAD будет находиться в каталоге `freecad-source/bin`

### Как восстановить папку с исходными кодами {#как_восстановить_папку_с_исходными_кодами}

Если вы случайно выполнили компиляцию в каталоге исходного кода или добавили странные файлы и хотели бы восстановить содержимое только в исходном исходном коде, вы можете выполнить следующие действия.


{{Code|lang=bash|code=
> .gitignore
git clean -df
git reset --hard HEAD
}}

Первая строка очищает файл `.gitignore`. Это гарантирует, что следующие команды clean и reset будут влиять на все в каталоге и не будут игнорировать элементы, соответствующие выражениям в `.gitignore`. Вторая строка удаляет все файлы и каталоги, которые не отслеживаются репозиторием git, затем последняя команда сбрасывает все изменения в отслеживаемых файлах, включая первую команду, которая очистила файл `.gitignore`.

Если вы не очистите исходный каталог, следующие запуски `cmake` могут не включить новые параметры в систему, если код изменится.

### Конфигурирование

Передавая различные параметры в `cmake`, вы можете изменить способ компиляции FreeCAD. Синтаксис выглядит следующим образом.


```python
cmake -D <var>:<type>=<value> $SOURCE_DIR
```

Где `$SOURCE_DIR` - каталог, содержащий исходный код. `<type>` в большинстве случаев может быть опущен. Пробел после параметра `-D` также может быть опущен.

Например, чтобы избежать создания [FEM Workbench](FEM_Workbench.md):


{{Code|lang=bash|code=
cmake -D BUILD_FEM:BOOL=OFF ../freecad-source
cmake -DBUILD_FEM=OFF ../freecad-source
}}

Все возможные переменные перечислены в файле `InitializeFreeCADBuildOptions.cmake`, расположенном в каталоге `CMake/FreeCAD_Helpers`. В этом файле найдёте слово `option`, чтобы перейти к переменным, которые можно задать, и просмотреть их значения по умолчанию.

    # ==============================================================================
    # =================   All the options for the build process    =================
    # ==============================================================================

    option(BUILD_FORCE_DIRECTORY "The build directory must be different to the source directory." OFF)
    option(BUILD_GUI "Build FreeCAD Gui. Otherwise you have only the command line and the Python import module." ON)
    option(FREECAD_USE_EXTERNAL_ZIPIOS "Use system installed zipios++ instead of the bundled." OFF)
    option(FREECAD_USE_EXTERNAL_SMESH "Use system installed smesh instead of the bundled." OFF)
    ...

В качестве альтернативы используйте команду `cmake-LH` для отображения текущей конфигурации и, следовательно, всех переменных, которые можно изменить. Вы также можете установить и использовать `cmake-gui` для запуска графического интерфейса, отображающего все переменные, которые можно изменить. В следующих разделах мы перечислим некоторые из наиболее важных опций, которые вы, возможно, захотите использовать.

#### Для Debug сборки {#для_debug_сборки}

Создайте сборку `Debug` для устранения неполадок в FreeCAD. Имейте в виду, что при такой сборке [Sketcher](Sketcher_Workbench.md) становится очень медленным при работе со сложными эскизами.


{{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Debug ../freecad-source
}}

#### Для Release сборки {#для_release_сборки}

Создайте сборку `Release` для тестирования кода, который не завершается сбоем. Сборка `Release` будет выполняться намного быстрее, чем сборка `Debug`.


{{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Release ../freecad-source
}}

#### Сборка на основе Python 3 и Qt5 {#сборка_на_основе_python_3_и_qt5}

По умолчанию FreeCAD 0.19 и более ранние версии созданы для Python 2 и Qt4. Поскольку эти два пакета устарели, лучше создавать для Python 3 и Qt5. Поддержка Python 2 и Qt4 была удалена в FreeCAD 0.20, и нет необходимости явно включать Qt5 и Python 3 при компиляции последних версий разработки.

В современном дистрибутиве Linux вам нужно указать только две переменные, указывающие использование Qt5, и путь к интерпретатору Python.

Для 0.19: {{Code|lang=bash|code=
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
}}

Для 0.20\_dev: {{Code|lang=bash|code=
cmake ../freecad-source
}}

Обратите внимание, что при переключении между сборками 0.19 и 0.20 может потребоваться удалить CMakeCache.txt до запуска cmake.

#### Сборка с применением особых версий Python {#сборка_с_применением_особых_версий_python}

Если по умолчанию исполняемый файл `python` в вашей системе является символической ссылкой на Python 2, `cmake` попытается настроить FreeCAD для этой версии. Вы можете выбрать другую версию Python, указав путь к определенному исполняемому файлу:


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
}}

Если это не сработает, вам, возможно, придется определить дополнительные переменные, указывающие на требуемые библиотеки Python, и включить каталоги:


{{Code|lang=bash|code=
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
    -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m \
    -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
    -DPYTHON_PACKAGES_PATH=/usr/lib/python3.6/site-packages/ \
    ../freecad-source
}}

В одной системе, возможно, имеет несколько независимых версий Python, поэтому расположение и номера версий ваших файлов Python будут зависеть от вашего конкретного дистрибутива Linux. Используйте `python3-V` для отображения версии Python, которую вы используете в настоящее время; необходимы только первые два числа; например, если результатом является `Python 3.6.8`, вам необходимо указать каталоги, относящиеся к версии 3.6. Если вы не знаете нужных каталогов, попробуйте выполнить их поиск с помощью команды `locate`.


```python
locate python3.6
```

Вы можете использовать `python3 -m site` в терминале для определения каталога `site-packages` или `dist-packages` для систем Debian.

#### Сборка в Qt Creator на основе Python 3 и Qt5 {#сборка_в_qt_creator_на_основе_python_3_и_qt5}

1\. Запустите Qt Creator.

2\. Кликните на {{MenuCommand|Open Project}}.

3\. Перейдите в каталог, в котором находится исходный код, `freecad-source/`, и выберите самый верхний файл {{incode/CMakeLists.txt}}.

4\. Выбрав файл, он автоматически запустит `cmake` на нем, но может выйти из строя, если соответствующие параметры установлены неправильно.

5\. Перейдите в {{MenuCommand|Projects → Build & Run → Imported Kit → Build → Build Settings → CMake}}. Установите соответствующий каталог сборки, `freecad-build/`.

6\. Установите соответствующие переменные в диалоговом окне Key-Value типов `String` и `Bool`. 
```python
PYTHON_EXECUTABLE=/usr/bin/python3
BUILD_QT5=ON
```

7\. Если переменные загружают проект неправильно, возможно, вам придется перейти к {{MenuCommand|Projects → Manage Kits → Kits → Default (or Imported Kit or similar) → CMake Configuration}}. Затем нажмите **Change**, и добавьте соответствующую конфигурацию, как описано выше. Возможно, вам придется добавить дополнительные переменные о путях Python, если системный Python не найден. 
```python
PYTHON_EXECUTABLE:STRING=/usr/bin/python3.7
PYTHON_INCLUDE_DIR:STRING=/usr/include/python3.7m
PYTHON_LIBRARY:STRING=/usr/lib/x86_64-linux-gnu/libpython3.7m.so
PYTHON_PACKAGES_PATH:STRING=/usr/lib/python3.7/site-packages
BUILD_QT5:BOOL=ON
```

7.1. Нажмите **Apply**, затем **OK**.

7.2. Убедитесь, что остальные параметры заданы правильно, например, {{MenuCommand|Qt version}} должна быть текущей версией, установленной в системе, как `Qt 5.9.5 in PATH (qt5)`.

Нажмите **Apply**, затем **OK**, чтобы закрыть конфигурацию.

Программа `cmake` должна снова запуститься автоматически, и она должна заполнить весь диалог Key-Value всеми переменными, которые можно настроить.

8\. Перейдите в {{MenuCommand|Projects → Build & Run → Imported Kit → Run → Run Settings → Run → Run Configuration}} и выберите `FreeCADMain` для компиляции графической версии FreeCAD или `FreeCADMainCMD` для компиляции только версии командной строки.

9\. Наконец, перейдите в меню {{MenuCommand|Сборка → Проект сборки "FreeCAD"}}. Если это новая компиляция, она должна занять несколько минут, включительно часов, в зависимости от количества доступных процессоров.

#### Плагин Qt designer {#плагин_qt_designer}

Если Вы хотите разрабатывать Qt-код для FreeCAD, Вам понадобится плагин к Qt Designer, который обеспечивает все пользовательские виджеты FreeCAD.

Перейдите в дополнительный каталог исходного кода, запустите `qmake` с указанным файлом проекта для создания `Makefile`; затем запустите `make` для компиляции плагина.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
qmake plugin.pro
make
}}

Если вы компилируете для Qt5, убедитесь, что двоичный файл `qmake` предназначен для этой версии, чтобы результирующий `Makefile` содержал необходимую информацию для Qt5.


{{Code|lang=bash|code=
cd freecad-source/src/Tools/plugins/widget
$QT_DIR/bin/qmake plugin.pro
make
}}

где `$QT_DIR` - это каталог, в котором хранятся двоичные библиотеки Qt, например, `/usr/lib/x86_64-linux-gnu/qt5`.

Созданная библиотека `libFreeCAD_widgets.so`, которую необходимо скопировать в `$QT_DIR/плагины/конструктор`.


{{Code|lang=bash|code=
sudo cp libFreeCAD_widgets.so $QT_DIR/plugins/designer
}}

#### Внешний или встроенный Pivy {#внешний_или_встроенный_pivy}

В прошлом, версия Pivy была включена в исходный код FreeCAD (internal). Если вы хотели использовать системную копию Pivy (external), вам нужно было использовать -DFREECAD_USE_EXTERNAL_PIVY=1.

Использование внешнего Pivy стало по умолчанию во время разработки FreeCAD 0.16, поэтому эту опцию больше не нужно устанавливать вручную.

#### Документирование посредством Doxygen {#документирование_посредством_doxygen}

Если у вас установлен Doxygen, вы можете создать документацию по исходному коду. См. инструкции в [source documentation](source_documentation.md).

### Дополнительная документация {#дополнительная_документация}

Исходный код FreeCAD очень обширен, и с помощью CMake можно настроить множество параметров. Обучение полному использованию CMake может быть полезно для выбора правильных вариантов для ваших особых потребностей.

-   [CMake Reference Documentation](https://cmake.org/documentation/)

от Kitware.

-   [How to Build a CMake-Based Project](https://preshing.com/20170511/how-to-build-a-cmake-based-project/)

(блог), предварительно изучив программирование.

-   [Learn CMake\'s Scripting Language in 15 Minutes](https://preshing.com/20170522/learn-cmakes-scripting-language-in-15-minutes/)

(блог) , предварительно изучив программирование.

### Создание пакета debian {#создание_пакета_debian}

Если Вы планируете собрать пакет Debian вне исходников, вам следует сначала установить следующие пакеты:


{{Code|lang=bash|code=
sudo apt install dh-make devscripts lintian
}}

Перейдите в папку FreeCAD и выполните


{{Code|lang=bash|code=
debuild
}}

Когда пакет построен, Вы можете использовать `lintian` для проверки, содержит ли пакет ошибки


{{Code|lang=bash|code=
lintian freecad-package.deb
}}

## Обновление исходного кода {#обновление_исходного_кода}

Система CMake позволяет разумно обновлять исходный код и перекомпилировать только то, что изменилось, что ускоряет следующие компиляции.

Перейдите в то место, где исходный код FreeCAD был впервые загружен, и извлеките новый код:


{{Code|lang=bash|code=
cd freecad-source
git pull
}}

Затем перейдите в каталог сборки, в котором код был скомпилирован изначально, и запустите `cmake`, указав текущий каталог (denoted by a dot); затем запустите повторную компиляцию с помощью `make`.


{{Code|lang=bash|code=
cd ../freecad-build
cmake .
make -j$(nproc --ignore=2)
}}

## Разрешение проблем {#разрешение_проблем}

### Примечание для 64-битных систем {#примечание_для_64_битных_систем}

При компиляции FreeCAD на 64-бит известна проблема с 64-битным пакетом OpenCASCADE. Чтобы FreeCAD правильно заработал, Вам нужно запустить скрипт `configure` и установить дополнительно `CXXFLAGS`:


{{Code|lang=bash|code=
./configure CXXFLAGS="-D_OCC64"
}}

Для систем на базе Debian эта опция не требуется при использовании готовых пакетов OpenCASCADE, поскольку эти пакеты устанавливают правильно `CXXFLAGS` внутри.

## Скрипты автоматической компиляции {#скрипты_автоматической_компиляции}

Это всё, что Вам нужно для полной компиляции FreeCAD. Это односкриптовое решение, работающее на свежеустановленном дистрибутиве. Команда запросит пароль root для установки пакетов новых онлайновых репозиториев. Эти скрипты должны запускаться на 32- и 64-битных версиях. Они написаны для разных версий, но, скорее всего, будут работать для позднейший версий с небольшими изменениями или без них.

Если у вас есть такой скрипт для вашего выбранного дистрибутива, пожалуйста, обсудите его на [Форум FreeCAD](https://forum.freecadweb.org/viewforum.php?f=21&sid=e3c22dca9da076fefb56b1d5c5fb3134), чтобы мы могли его включить.


<div class="mw-collapsible mw-collapsed toccolours">

### Ubuntu


<div class="mw-collapsible-content">

Эти скрипты обеспечивают надёжный путь для установки верного набора зависимостей, требуемых для сборки и запуска FreeCAD в Ubuntu. Они используют репозитории PPA Ubuntu FreeCAD, и должны работать на любой версии Ubuntu, для которой есть целевой PPA. PPA на [freecad-daily](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) нацелен на последнюю версию Ubuntu, а [\'стабильный\'](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable) PPA нацелен на официально поддерживаемые версии Ubuntu.

Этот скрипт устанавливает дневной скомпилированный снимок FreeCAD и его зависимостей. Он добавляет дневной репозиторий, получает зависимости для создания этой версии и устанавливает необходимые пакеты. Затем он продолжает извлекать исходный код в определенный каталог, создает каталог сборки и вносит в него изменения, настраивает среду компиляции с помощью `cmake` и, наконец, создает всю программу с помощью `make`. Сохраните сценарий в файл, сделайте его исполняемым и запустите его, но не используйте `sudo`; привилегии суперпользователя будут запрашиваться только для выбранных команд.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-daily && sudo apt-get update
sudo apt-get build-dep freecad-daily
sudo apt-get install freecad-daily

git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DFREECAD_USE_PYBIND11=ON ../freecad-source
make -j$(nproc --ignore=2)
}}

При желании вы можете удалить предварительно скомпилированную версию FreeCAD (`freecad-daily`), оставив зависимости на месте, однако, если этот пакет будет установлен, менеджер пакетов также сможет обновлять свои зависимости; это наиболее полезно, если вы намерены следить за развитием FreeCAD, а также постоянно обновлять и компилировать исходные тексты из репозитория Git.

Предыдущий скрипт предполагает, что вы хотите скомпилировать последнюю версию FreeCAD, поэтому вы используете репозиторий \"daily\" для получения зависимостей. Однако вместо этого вы можете получить зависимости сборки \"стабильной\" версии для вашего текущего выпуска Ubuntu. Если это так, замените верхнюю часть предыдущего сценария следующими инструкциями. Для Ubuntu 12.04 опустите `--enable-source` в команде.


{{Code|lang=bash|code=
#!/bin/sh
sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-stable && sudo apt-get update
sudo apt-get build-dep freecad
sudo apt-get install freecad
}}

Как только вы установите пакет `freecad` из репозитория `freecad-stable`, он заменит исполняемый файл FreeCAD, доступный из репозитория Ubuntu Universe. Исполняемый файл будет называться просто `freecad`, а не `freecad-stable`.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### openSUSE {#opensuse_1}


<div class="mw-collapsible-content">


<div class="mw-translate-fuzzy">

Никаких внешних репозиториев не требуется для компиляции FreeCAD. Однако существует несовместимость с python3-devel, которую необходимо удалить. FreeCAD может быть скомпилирован из GIT


</div>


{{Code|lang=bash|code=
# install needed packages for development
sudo zypper install gcc cmake OpenCASCADE-devel libXerces-c-devel \
python-devel libqt4-devel python-qt4 Coin-devel SoQt-devel boost-devel \
libode-devel libQtWebKit-devel libeigen3-devel gcc-fortran git swig
 
# create new dir, and go into it
mkdir FreeCAD-Compiled 
cd FreeCAD-Compiled
 
# get the source
git clone https://github.com/FreeCAD/FreeCAD.git free-cad
 
# Now you will have a subfolder in this location called free-cad. It contains the source
 
# make another dir for compilation, and go into it
mkdir FreeCAD-Build1
cd FreeCAD-Build1 
 
# build configuration 
cmake ../free-cad
 
# build FreeCAD
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}

Поскольку вы используете git, в следующий раз, когда захотите скомпилировать, вам не нужно клонировать все подряд просто извлеките из git и скомпилируйте еще раз


{{Code|lang=bash|code=
# go into free-cad dir created earlier
cd free-cad
 
# pull
git pull
 
# get back to previous dir
cd ..
 
# Now repeat last few steps from before.
 
# make another dir for compilation, and go into it
mkdir FreeCAD-Build2
cd FreeCAD-Build2
 
# build configuration 
cmake ../free-cad
 
# build FreeCAD
# Note: to speed up build use all CPU cores: make -j$(nproc)
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Debian Squeeze {#debian_squeeze}


<div class="mw-collapsible-content">


{{Code|lang=bash|code=
# get the needed tools and libs
sudo apt-get install build-essential python libcoin60-dev libsoqt4-dev \
libxerces-c2-dev libboost-dev libboost-date-time-dev libboost-filesystem-dev \
libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev \
libboost-serialization-dev libboost-signals-dev libboost-regex-dev \
libqt4-dev qt4-dev-tools python2.5-dev \
libsimage-dev libopencascade-dev \
libsoqt4-dev libode-dev subversion cmake libeigen2-dev python-pivy \
libtool autotools-dev automake gfortran
 
# checkout the latest source
git clone https://github.com/FreeCAD/FreeCAD.git freecad
 
# go to source dir
cd freecad
 
# build configuration 
cmake .
 
# build FreeCAD
# Note: to speed up build use all CPU cores: make -j$(nproc)
make
 
# test FreeCAD
cd bin
./FreeCAD -t 0
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Fedora 27/28/29 {#fedora_272829}


<div class="mw-collapsible-content">

Опубликовано пользователем [http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666 PrzemoF](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=3666_PrzemoF.md) на форуме.


{{Code|lang=bash|code=
#!/bin/bash

ARCH=$(arch)

MAIN_DIR=FreeCAD
BUILD_DIR=build

#FEDORA_VERSION=27
#FEDORA_VERSION=28
FEDORA_VERSION=29

PACKAGES="gcc cmake gcc-c++ boost-devel zlib-devel swig eigen3 qt-devel \
shiboken shiboken-devel pyside-tools python-pyside python-pyside-devel xerces-c \
xerces-c-devel OCE-devel smesh graphviz python-pivy python-matplotlib tbb-devel \
 freeimage-devel Coin3 Coin3-devel med-devel vtk-devel"

FEDORA_29_PACKAGES="boost-python2 boost-python3 boost-python2-devel boost-python3-devel"

if [ "$FEDORA_VERSION" = "29" ]; then
    PACKAGES="$PACKAGES $FEDORA_29_PACKAGES"
fi

echo "Installing packages required to build FreeCAD"
sudo dnf -y install $PACKAGES
cd ~
mkdir $MAIN_DIR <nowiki>||</nowiki> { echo "~/$MAIN_DIR already exist. Quitting.."; exit; }
cd $MAIN_DIR
git clone https://github.com/FreeCAD/FreeCAD.git
mkdir $BUILD_DIR <nowiki>||</nowiki> { echo "~/$BUILD_DIR already exist. Quitting.."; exit; }
cd $BUILD_DIR
cmake ../FreeCAD 
make -j$(nproc)
}}


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

### Arch с использованием AUR {#arch_с_использованием_aur}


<div class="mw-collapsible-content">

[Arch User Repository (AUR)](https://aur.archlinux.org/) - это коллекция пользовательских рецептов для создания пакетов, которые официально не поддерживаются сопровождающими распространения / сообществом. Обычно они в безопасности. Вы можете увидеть, кто поддерживал посылку и как долго он это делал. Рекомендуется проверить общестроительные файлы. Также в этой области доступно программное обеспечение с открытым исходным кодом, даже если оно поддерживается официальной компанией-владельцем.

Обязательное требование : git

Шаги :

1.  Откройте терминал. При необходимости создайте каталог, например. {{incode | mkdir git}}. При необходимости измените каталог, например. `cd git`.
2.  Клонировать репозиторий AUR : `git clone http://aur.archlinux.org/packages/freecad-git`
3.  Войдите в папку репозитория AUR : `cd freecad-git`
4.  Компиляция с использованием [Arch makepkg](https://wiki.archlinux.org/index.php/Makepkg) : `makepkg -s`. Флаг -s или \--syncdeps также установит необходимые зависимости.
5.  Установите созданный пакет : `makepkg --install` или дважды щелкните имя файла pkgname-pkgver.pkg.tar.xz в вашем браузере файлов.

Чтобы обновить FreeCAD до последней версии, просто повторите шаг 3. Обновите репозиторий, когда в рецепте произойдет какое-либо изменение или появятся новые функции, используя `git checkout-f` внутри каталога.







[Category:Developer\_Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Developer{{\#translation:}}](Category:Developer.md)
