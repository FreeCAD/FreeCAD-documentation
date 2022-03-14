# Compile on MinGW/ru
{{TOCright}}

В данном руководстве будут рассмотрены шаги, необходимые для сборки FreeCAD в Windows с использованием среды MSYS2/MinGW. Базовые знания команд оболочки Bash будут полезны для понимания того, что происходит на каждом этапе сборки. Тщательное следование руководству по пунктам, должно привести вас к созданию рабочей сборки, даже если вы не полностью понимаете, что вы сделали, чтобы получить ее.

### Прежде чем вы начнете 

Загрузите и установите [MSYS2](https://www.msys2.org), если вы еще этого не сделали. При запуске MSYS2 используйте 64-разрядную среду выполнения MSYS2 MinGW, если вы не знаете, что делаете, и у вас нет конкретной причины этого не делать. Если вы используете консоль UCRT, убедитесь, что ваша инсталляция адаптирована для использования пакетов UCRT вместо этого.

    pacman -Syu

после чего перезапустите и запустите

    pacman -Su

прежде чем продолжить.

### Установка основных средств разработки 

Во всех следующих шагах, если оболочка MSYS2 будет предлагать установки по умолчанию, для всех случаев дайте согласие нажав \"Enter\", когда вас спросят.

Во-первых, установите набор инструментов mingw-w64 GCC:

    pacman -S --needed base-devel mingw-w64-x86_64-toolchain mingw-w64-x86_64-cmake mingw-w64-x86_64-ninja

Это, вероятно, займет несколько минут, так как набор инструментов компилятора довольно велик.

Установите git:

    pacman -S git

Закройте текущее окно консоли и перезапустите консоль MSYS2 MinGW 64 (в стандартной установке это будет в меню \"Пуск\" в папке MSYS2).

### Загрузка исходников FreeCAD 

Чтобы получить исходный код FreeCAD, клонируйте его из основного репозитория git:

    git clone https://github.com/FreeCAD/FreeCAD

Если вы не хотите компилировать последнюю версию HEAD, как только у вас будет исходный код, вы можете проверить конкретный тег:

    cd FreeCAD
    git checkout tags/1.0 -b releases/FreeCAD-1-0

Или конкретный pull request (в данном примере PR 1234):

    cd FreeCAD
    git fetch origin pull/1234/head:pr/1234
    git checkout pr/1234

Note that not all versions can be compiled on MSYS2, several changes were required to enable it and these were not present in the 0.19 or earlier versions. For example, the 0.19.3 tag will not be compilable.

### Установка необходимых библиотек 


<div class="mw-translate-fuzzy">

FreeCAD включает в свою сборку много сторонних библиотек. Они могут быть установлены по отдельности или в виде единой унифицированной команды. Обновление этого списка является текущей текущей работой этой документации: чтобы помочь, повторно выполните команду cmake из следующего раздела и установите любой следующий пакет, в котором он ошибается. На момент написания этой статьи возникла проблема с pacman-installed OpenCASCADE пакетом.


</div>

Теперь установите следующие необходимые зависимости с помощью pacman:

-   mingw-w64-x86\_64-opencascade
-   mingw-w64-x86\_64-xerces-c
-   mingw-w64-x86\_64-qt5
-   mingw-w64-x86\_64-med
-   mingw-w64-x86\_64-swig
-   mingw-w64-x86\_64-qtwebkit
-   mingw-w64-x86\_64-coin
-   mingw-w64-x86\_64-python-pivy
-   mingw-w64-x86\_64-python-ply
-   mingw-w64-x86\_64-python-six
-   mingw-w64-x86\_64-python-yaml
-   mingw-w64-x86\_64-python-numpy
-   mingw-w64-x86\_64-python-matplotlib
-   mingw-w64-x86\_64-pyside2-qt5
-   mingw-w64-x86\_64-python-markdown
-   mingw-w64-x86\_64-python-pygit2


<div class="mw-translate-fuzzy">

Ниже приведена одна команда для установки всего, кроме OpenCascade:


</div>

    pacman -S mingw-w64-x86_64-opencascade mingw-w64-x86_64-xerces-c mingw-w64-x86_64-qt5 mingw-w64-x86_64-med mingw-w64-x86_64-swig mingw-w64-x86_64-qtwebkit mingw-w64-x86_64-coin mingw-w64-x86_64-python-pivy mingw-w64-x86_64-pyside2-qt5 mingw-w64-x86_64-python-ply mingw-w64-x86_64-python-six mingw-w64-x86_64-python-yaml mingw-w64-x86_64-python-numpy mingw-w64-x86_64-python-matplotlib mingw-w64-x86_64-python-markdown mingw-w64-x86_64-python-pygit2

### Сборка FreeCAD 

Создайте каталог для сборки: обратите внимание, что обычно это не подкаталог исходного каталога (часто бывает полезно иметь возможность удалить либо исходный, либо каталог сборки независимо).

    mkdir FreeCAD-build
    cd FreeCAD-build

Запустите сMake:

    cmake ../FreeCAD

И в завершение:

    cmake --build ./



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on MinGW/ru
