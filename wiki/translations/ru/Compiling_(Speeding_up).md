# Compiling (Speeding up)/ru
{{TOCright}}



## Обзор

FreeCAD - это крупное приложение, для полной компиляции которого из исходного когда, может потребоваться от 10 минут до часа. В первую очередь это зависит от используемого процессора и количества ядер, используемых в процессе компиляции. Вот несколько советов, как сократить время процесса сборки.

## CCache


<div class="mw-translate-fuzzy">

### CCache 

Установите `ccache` для кеширования сборок.


</div>

[Ccache](https://ccache.dev/) speeds up recompilation by caching previous compilations and detecting when the same compilation is done again. Ccache is free software, released under GPLv3 or later.

On most systems ccache will be automatically detected and enabled, you can use the `FREECAD_USE_CCACHE` `cmake` option to control this behavior.

## Disable modules 


<div class="mw-translate-fuzzy">

### Отключаемые модули 

При использовании `cmake` для настройки сборки вы можете отключить компиляцию определенных инструментальных средств, которые в данный момент могут вам не понадобиться. Это полезно, если вам нужно протестировать только несколько инструментальных средств.


</div>

Например, чтобы исключить сборку верстаков FEM и Mesh:


```python
cmake -DBUILD_FEM=OFF -DBUILD_MESH=OFF ../freecad-source
```

Используйте `cmake-gui`, `cmake-curses-gui` или `cmake-qt-gui` для отображения всех возможных переменных, которые можно редактировать в конфигурации; с помощью этих интерфейсов вы можете легко включать или выключать различные инструментальные средства.

## Number of jobs in parallel 


<div class="mw-translate-fuzzy">

## Количество параллельных заданий 

После настройки с помощью `cmake` программа `make` запускает настоящий компилятор C++ для работы с файлами исходного кода. Вы можете ускорить компиляцию, работая одновременно с различными файлами. Это достигается с помощью опции `-j` `make`, которая обозначает количество \"задач\" или команд компиляции, выполняемых одновременно. Этот параметр представляет собой целое число.


</div>

Выполняйте четыре команды компиляции параллельно:


```python
make -j4
```

Скомпилируйте параллельно столько файлов, сколько ядер процессора в вашей системе. Это полезно, если у вас много ядер и вы хотите использовать их все для компиляции программного обеспечения.


{{code|code=
make -j$(nproc)
}}

Скомпилируйте параллельно столько файлов, сколько ядер процессора в вашей системе, минус два. Используйте это, чтобы ваша система спокойно реагировала на выполнение какой-либо другой задачи; например, два ядра позволят вам использовать браузер, в то время как остальные ядра продолжают компилировать программное обеспечение в фоновом режиме.


{{code|code=
make -j$(nproc --ignore=2)
}}

## distcc


<div class="mw-translate-fuzzy">

### distcc 

Программа `distcc` может использоваться для выполнения распределенной компиляции кода на языках C и C++ на нескольких компьютерах в сети.


</div>

[Distcc](https://www.distcc.org/) should always generate the same results as a local compilation. It is free, simple to install and use, and often two or more times faster than compiling locally.

FreeCAD dev \'etrombly\' has published a short explanation on [how to install distcc to compile FreeCAD on a network of computers using Docker](https://forum.freecadweb.org/viewtopic.php?f=4&t=50810&p=459142#p458614).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compiling (Speeding up)/ru
