# Compile on Windows/ru
{{TOCright}}


<div class="mw-translate-fuzzy">

На этой странице шаг за шагом объясняется \"как скомпилировать FreeCAD 0.19 или новее в Windows\"\". Для других платформ см.[Compiling](Compiling.md).


</div>



## Требования

Для компиляции FreeCAD в Windows требуется несколько инструментов и библиотек.



### Требования 


<div class="mw-translate-fuzzy">

-   Компилятор. FreeCAD тестируется с помощью Visual Studio (MSVC)---другие компиляторы могут работать, но инструкции по использованию здесь не включены. Более подробная информация в [#Compiler](#Compiler.md), находится ниже.


</div>

-   [Git](http://git-scm.com/) (Для Git также доступны графические интерфейсы, см. Следующий раздел.)

-   [CMake](https://cmake.org/download/) версия 3.11.x или более новая.  \"Подсказка:\" Выбор опции *Add CMake to the system PATH for all users* при установке CMake сделает CMake доступным из командной строки Windows, что может быть полезно.


<div class="mw-translate-fuzzy">

-   LibPack (так называемый FreeCADLibs). Это единый пакет, содержащий все библиотеки, необходимые для компиляции FreeCAD в Windows. Загрузите версию LibPack, соответствующую версии FreeCAD, которую вы хотите скомпилировать. Чтобы скомпилировать FreeCAD 0.19 или последнюю версию разработки 0.20, загрузите [LibPack для 0.19/0.20](https://github.com/apeltauer/FreeCAD/releases/tag/LibPack_12.5.2) (только 64-разрядная версия). Извлеките пакет LibPack в удобное место. (Если ваш компьютер не распознает расширение .7z, вам следует установить программу [7-zip](https://www.7-zip.org).)  \"Примечание\": Настоятельно рекомендуется компилировать FreeCAD с версией компилятора, для которой предназначен LibPack. Например, вы можете столкнуться с проблемами при компиляции FreeCAD 0.19 с использованием MSVC 15, поскольку LibPack для 0.19 предназначен для сборки с MSVC 17.


</div>



### Опционные программы 

-   Графический интерфейс для Git. Существует несколько доступных интерфейсов, см. [this list](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs). Основное преимущество интерфейса заключается в том, что вам не нужно изучать команды Git, чтобы получить исходный код FreeCAD или отправлять исправления в репозиторий FreeCAD на GitHub.

Ниже мы опишем обработку исходного кода с использованием интерфейса [TortoiseGit](https://tortoisegit.org/). Этот интерфейс интегрируется непосредственно в проводник файлов Windows и имеет большое сообщество пользователей, которые могут получить помощь в случае возникновения проблем.

-   [NSIS](http://sourceforge.net/projects/nsis/) используется для создания установщика Windows FreeCAD.



### Исходный код 

Теперь вы можете получить исходный код FreeCAD:



#### Использование интерфейса 

При использовании TortoiseGit [Интерфейс Git](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs):

1.  Создайте новую папку, в которую будет загружен исходный код.
2.  Щелкните правой кнопкой мыши на этой папке в проводнике файлов Windows и выберите \"\'Git Clone\" в контекстном меню.
3.  Появится диалоговое окно. В нем введите URL-адрес репозитория FreeCAD Git

*<https://github.com/FreeCAD/FreeCAD.git>*

и нажмите \"ОК\".

Последний исходный код будет загружен из репозитория FreeCAD Git, и Git будет отслеживать папку.



#### Использование командной строки 

Чтобы создать локальную ветвь отслеживания и загрузить исходный код, откройте терминал (command prompt) и перейдите в каталог, в котором вы хотите получить исходный код, затем введите:


```python
git clone https://github.com/FreeCAD/FreeCAD.git
```



### Компилятор

По умолчанию (recommended) используется компилятор MS Visual Studio (MSVC). Хотя, возможно, можно использовать другие компиляторы, например gcc через Cygwin или MinGW, это не тестируется и не рассматривается здесь.

Вы можете получить бесплатную версию MSVC (для индивидуального использования), загрузив [*Community* edition of MS Visual Studio](https://visualstudio.microsoft.com/vs/community/).

Для тех, кто хочет избежать установки огромного MSVC только для того, чтобы иметь компилятор, см. [CompileOnWindows - Reducing Disk Footprint](CompileOnWindows_-_Reducing_Disk_Footprint.md).

\"Примечание:\" Несмотря на то, что \"Community\" выпуск MSVC является бесплатным, для использования среды IDE в течение более чем 30-дневного пробного периода необходимо создать учетную запись Майкрософт. Если вы будете компилировать только с помощью командной строки, вам не понадобится среда разработки и, следовательно, учетная запись Microsoft.

В качестве бесплатной и альтернативной среды разработки с открытым исходным кодом вы можете использовать [KDevelop](https://www.kdevelop.org/download). Вы можете использовать KDevelop для изменения и написания кода на C++, но для компиляции необходимо использовать командную строку.



### Дополнительная конфигурация системного пути 

При необходимости вы можете включить пути к некоторым папкам в переменную системного ПУТИ. Это полезно, если вы хотите получить доступ к программам в этих папках из командной строки/powershell или если вы хотите, чтобы компилятор или CMake находили специальные программы. Кроме того, добавление папок в ПУТЬ может потребоваться, если вы не использовали соответствующие параметры при установке программы.

-   Вы можете включить папку вашего LibPack в переменную системного ПУТИ. Это полезно, если вы планируете создавать несколько конфигураций/версий FreeCAD.
-   Если вы не использовали опцию добавления CMake в ПУТЬ при его установке, добавьте папку его установки

\"C:\\Program Files\\CMake\\bin\" по ПУТИ.

-   Если вы не использовали опцию добавления TortoiseGit в ПУТЬ при его установке, добавьте папку его установки

*C:\\Program Files\\TortoiseGit\\bin* по ПУТИ.

Чтобы добавить пути к папкам в переменную PATH:

1.  В меню \"Start\" Windows щелкните правой кнопкой мыши на \"Computer\" и выберите \"Properties\".
2.  В появившемся диалоговом окне нажмите \"Advanced system settings\".
3.  Откроется другое диалоговое окно. Нажмите там на вкладке \"Advanced\" в разделе \"Environment Variables\".
4.  Снова откроется другое диалоговое окно. Затем выберите переменную \"Path\" и нажмите \"Edit\".
5.  И снова откроется другое диалоговое окно. Нажмите там на \"New\" и добавьте в путь к папке Git или LibPack.
6.  Наконец, нажмите \"ОК\" и закройте все диалоговые окна, также нажав \"ОК\".



### Конфигурация


<div class="mw-translate-fuzzy">

Как только у вас будут все необходимые инструменты, библиотеки и исходный код FreeCAD, вы будете готовы приступить к процессу настройки и компиляции. Этот процесс будет проходить в пять этапов:

1.  Запустите CMake один раз, чтобы проверить вашу систему и начать процесс настройки (это сообщит о том, что она не удалась).
2.  Настройте необходимые параметры CMake, чтобы установить расположение пакета LibPack и включить Qt5.
3.  Повторно запустите CMake, чтобы завершить настройку (на этот раз она должна завершиться успешно).
4.  Используйте CMake для создания системы сборки Visual Studio.
5.  Используйте Visual Studio для создания FreeCAD.


</div>

### CMake


<div class="mw-translate-fuzzy">

Во-первых, настройте среду сборки с помощью CMake:

1.  Откройте графический интерфейс CMake
2.  Укажите исходную папку FreeCAD.
3.  Укажите папку сборки (не используйте исходную папку-CMake создаст эту папку, если она не существует).
4.  Нажмите кнопку \"Configure\".
5.  В появившемся диалоговом окне укажите генератор, который вы хотите использовать: в большинстве случаев вы будете использовать значения по умолчанию в этом диалоговом окне. Для стандартной MS Visual Studio используйте \"Visual Studio xx 2yyy\", где xx-версия компилятора, а 2yyy-год его выпуска. Рекомендуется использовать опцию по умолчанию \"Use default native compilers\".


</div>

**Примечание:** Важно указать правильный вариант разрядности. Если у вас есть 64-разрядный вариант LibPack, вы также должны использовать компилятор x64.

Это приведет к началу настройки и \"завершится ошибкой\" из-за отсутствия настроек. Это нормально, вы еще не указали местоположение пакета LibPack. Однако могут возникнуть и другие сбои, которые потребуют некоторых дальнейших действий с вашей стороны.


<div class="mw-translate-fuzzy">

Если произойдет сбой с сообщением о том, что Visual Studio не найдена, поддержка CMake в MSVC еще не установлена. Для этого:

1.  Откройте среду разработки MSVC
2.  Используйте меню Tools → Get Tools и Features
3.  На вкладке \"Workloads\" включите \"Desktop development with C++\".
4.  На правой стороне теперь вы должны видеть, что будет установлен компонент \"Visual C++ tools for CMake\".
5.  Установите его.


</div>


<div class="mw-translate-fuzzy">

Если он завершится ошибкой с сообщением о неверной версии Python или отсутствующем Python, то:

1.  Используйте поле \"Search:\" в CMake для поиска строки \"Python\".
2.  Если вы видите там путь, подобный \"C:/Program Files/Python38/python.exe\", CMake распознал Python, который уже установлен на вашем компьютере, но эта версия несовместима с LibPack. Поскольку LibPack включает совместимую версию Python, измените следующие параметры Python в CMake в соответствии с его путями (при условии, что LibPack находится в папке \"D:\\FreeCAD-build\\FreeCADLibs_12.5.2_x64_VC17\"):

![](images/CMake_Python_settings.png )


</div>


<div class="mw-translate-fuzzy">

Если нет ошибки в Visual Studio или Python, все в порядке, но CMake еще не знает всех необходимых настроек. Поэтому сейчас:

1.  Найдите в CMake переменную \"FREECAD_LIBPACK_DIR\" и укажите местоположение папки LibPack, которую вы загрузили ранее.
2.  Только если сборка FreeCAD 0.19, найдите переменную \"\'BUILD_QT5\" и включите эту опцию.
3.  Нажмите \"Configure\" еще раз.


</div>

Теперь ошибок быть не должно. Если вы по-прежнему сталкиваетесь с ошибками, которые не можете диагностировать, посетите [Install/Compile forum](https://forum.freecadweb.org/viewforum.php?f=4) на веб-сайте форума FreeCAD. Если CMake прошел правильно, нажмите на кнопку \"Generate\". После этого вы можете закрыть CMake и начать компиляцию FreeCAD с помощью Visual Studio. Однако для первой компиляции держите его открытым на случай, если вам захочется или потребуется изменить некоторые параметры процесса сборки.



### Параметры процесса сборки 

Система сборки CMake дает вам контроль над некоторыми аспектами процесса сборки. В частности, вы можете включать и выключать некоторые функции или модули с помощью переменных CMake.

Вот описание некоторых из этих переменных:


<div class="mw-translate-fuzzy">

  Variable name                       Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Default
    
  BUILD_XXX                           Создайте FreeCAD с компонентом XXX. Если вы не хотите/не нуждаетесь в компиляции, например, рабочего стола \"OpenSCAD\", отключите переменную \"BUILD_OPENSCAD\". Тогда у FreeCAD не будет этого верстака. \"\"Примечание: \"\" Некоторые компоненты требуются для других компонентов. Если вы, например, снимите флажок \"BUILD_ROBOT\", CMake сообщит вам, что компонент \"Путь\" не может быть правильно скомпилирован. Поэтому проверьте вывод CMake после изменения параметра BUILD_XXX!                                                        depends
  BUILD_ENABLE_CXX_STD                Версия стандарта языка C++. \"C++14\" является максимально возможным для FreeCAD 0.19, в то время как для FreeCAC 0.20 требуется как минимум \"C++17\". См. Также примечание в разделе [Building with Visual Studio 15 (2017) and 16 (2019)](#Release_Build.md)                                                                                                                                                                                                                                                                              depends
  CMAKE_INSTALL_PREFIX                Выходная папка при создании целевой \"INSTALL\" см. также раздел [Running and installing FreeCAD](#Running_and_installing_FreeCAD.md)                                                                                                                                                                                                                                                                                                                                                                                                        Windows\' default program installation folder
  FREECAD_COPY_DEPEND_DIRS_TO_BUILD   Копии библиотек, необходимых для выполнения FreeCAD.exe в папку сборки. См. также раздел [Running and installing FreeCAD](#Running_and_installing_FreeCAD.md). \"Примечание:\" параметры FREECAD_COPY_XXX отображаются только в том случае, если библиотеки еще не были скопированы. Поэтому при переходе на другую версию LibPack важно удалить все папки в папке сборки, кроме папки LibPack. В CMake удалите кэш и начните так, как будто вы компилируете в первый раз, и вы получите параметры FREECAD_COPY_XXX options.   OFF
  FREECAD_COPY_PLUGINS_BIN_TO_BUILD   Copies Qt\'s plugin files needed to execute the FreeCAD.exe to the build folder. См. также раздел [Running and installing FreeCAD](#Running_and_installing_FreeCAD.md).                                                                                                                                                                                                                                                                                                                                                                      OFF
  FREECAD_LIBPACK_USE                 Switch the usage of the FreeCAD LibPack on or off                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ON
  FREECAD_LIBPACK_DIR                 Directory where the LibPack is                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       FreeCAD\'s source code folder
  FREECAD_RELEASE_PDB                 Create debug libraries also for release builds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ON


</div>



## Сборка FreeCAD 


<div class="mw-translate-fuzzy">

В зависимости от вашего компилятора процесс создания FreeCAD будет немного отличаться. В следующих разделах описаны известные вам рабочие процессы. Если вы создаете с помощью Qt Creator, перейдите к [Building with Qt Creator](#Building_with_Qt_Creator.md), в противном случае продолжайте напрямую:


</div>


<div class="mw-collapsible mw-collapsed toccolours">




<div class="mw-translate-fuzzy">

### Сборка в Visual Studio 15 (2017) и 16 (2019) 


</div>


<div class="mw-collapsible-content">



#### Сборка релиза 

1.  Запустите среду разработки Visual Studio. Это можно сделать либо нажатием кнопки \"Open Project\" в графическом интерфейсе CMake, либо двойным щелчком по файлу \"FreeCAD.sln\", который вы найдете в папке сборки.
2.  На панели инструментов среды разработки MSVC убедитесь, что вы используете для первой компиляции \"Release\".
3.  Есть окно под названием \"Solution Explorer\". В нем перечислены все возможные цели компиляции. Чтобы начать полную компиляцию, щелкните правой кнопкой мыши на целевом объекте \"ALL_BUILD\", а затем выберите \"Build\".

Теперь это займет довольно много времени.


<div class="mw-translate-fuzzy">

Чтобы скомпилировать готовый к использованию FreeCAD, скомпилируйте целевую \"INSTALL\", см. раздел [Running and installing FreeCAD](#Running_and_installing_FreeCAD.md).


</div>

Если вы не получили никаких ошибок, значит все готов. \"Поздравляю!\" Теперь вы можете выйти из MSVC или оставить его открытым.


<div class="mw-translate-fuzzy">

\"Примечание:\" Для FreeCAD 0.20 требуется, по крайней мере, стандартная версия языка C++ 17, но сторонний компонент \"flann\" из LibPack еще не готов для этого. Поэтому вы получите ошибки компиляции для целевого \"обратного проектирования\". Чтобы исправить это, щелкните правой кнопкой мыши на этом целевом объекте в обозревателе решений MSVC и выберите в контекстном меню последнюю запись \"Properties\". В появившемся диалоговом окне измените \"C++ Language Standard\" на \"ISO C++14\". Наконец, снова создайте цель \"ALL_BUILD\".


</div>



#### Отладочная сборка 

Для отладочной сборки необходимо использовать Python, который входит в пакет LibPack. Чтобы гарантировать это:

1.  Поиск в графическом интерфейсе CMake \"Python\"
2.  Если вы видите там путь, подобный \"C:/Program Files/Python38/python.exe\", CMake распознал Python, установленный на вашем компьютере, а не тот, который входит в LibPack. В этом случае адаптируйте эти различные настройки Python в CMake к этому (при условии, что LibPack находится в папке \"D:\\FreeCAD-build\\FreeCADLibs_12.5.2_x64_VC17\"):

![](images/CMake_Python_settings.png )

As prerequisite for the debug build, you need to do this:

1.  Copy the content of the LibPack folder *bind* to the *bin* folder of the FreeCAD build folder (overwrite the existing files).
2.  Copy the content of the LibPack folder *libd* to the *lib* folder of the FreeCAD build folder.


<div class="mw-translate-fuzzy">

Теперь

1.  Запустите среду разработки Visual Studio. Это можно сделать либо нажатием кнопки \"Open Project\" в графическом интерфейсе CMake, либо двойным щелчком по файлу \"FreeCAD.sln\", который вы найдете в папке сборки.
2.  На панели инструментов среды разработки MSVC убедитесь, что вы используете для первой компиляции \"Debug\".
3.  Есть окно под названием \"Solution Explorer\". В нем перечислены все возможные цели компиляции. Чтобы начать полную компиляцию, щелкните правой кнопкой мыши на целевом объекте \"ALL_BUILD\", а затем выберите \"Build\" в контекстном меню.

Теперь это займет довольно много времени. Если ошибок компиляции не было, вы можете запустить отладочную сборку:

1.  Щелкните правой кнопкой мыши на целевой \"FreeCADMain\", а затем выберите \"Set as Startup Project\" в контекстном меню.
2.  Наконец, нажмите на панели инструментов на кнопку с зеленым треугольником под названием \"Local Windows Debugger\".


</div>

If there were no compilation errors, and if the **FREECAD_COPY\_\*** options mentioned in the [CMake Configuration step](#CMake.md) above were enabled, you can start the debug build:

1.  Right-click on the target **FreeCADMain** and then choose **Set as Startup Project** in the context menu.
2.  Finally click in the toolbar on the button with the green triangle named **Local Windows Debugger**.

Это запустит отладочную сборку FreeCAD, и вы сможете использовать среду разработки MSVC для ее отладки.

#### Видеоресурс

Учебник по английскому языку, который начинается с настройки в графическом интерфейсе CMake и продолжается командой \"Build\" в Visual Studio 16 2019, доступен без списка на YouTube по адресу [Tutorial: Build FreeCAD from source on Windows 10](https://youtu.be/s4pHvlDOSZQ).


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Сборка с помощью Qt Creator (устарело) 


<div class="mw-collapsible-content">



#### Инсталяция и настройка Qt Creator 

-   Загрузите и установите [Qt Creator](https://www.qt.io/offline-installers)
-   Tools → Options → Text Editor → Behavior tab:
    -   File Encodings → Default Encodings:
    -   Установите значение: \"\'ISO-8859-1 /\...csISOLatin1\"\' (Некоторые символы создают ошибки/предупреждения с помощью Qt Creator, если оставить значение UTF-8. Это, кажется, все исправляет.)
-   Tools → Options → Build & Run:
    -   CMake tab
        -   Заполните поле Исполняемый файл путем к cmake.exe
    -   Kits tab
        -   Name: MSVC 2008
        -   Compiler: Microsoft Visual C++ Compiler 9.0 (x86)
        -   Debugger: Auto detected\...
        -   Версия Qt: Отсутствует
    -   General tab
        -   Снимите флажок: Всегда создавайте проект перед его развертыванием
        -   Снимите флажок: Всегда развертывайте проект перед его запуском



#### Импорт проекта и здания 

-   File → Open File or Project
-   Открыть \"\'CMakeLists.txt\"\' который находится на верхнем уровне источника
-   Это запустит CMake
-   Выберите каталог сборки и нажмите кнопку Далее
-   Установите для генератора значение \"NMake Generator (MSVC 2008)\"\'
-   Нажмите кнопку Запустить CMake. Следуйте инструкциям, приведенным выше, чтобы настроить CMake по своему вкусу.

Теперь FreeCAD можно построить

-   Build → Build All
-   Это займет много времени\...

После завершения его можно запустить: В левом нижнем углу есть 2 зеленых треугольника. Один из них-отладка. Другой \"run\". Выбери, что тебе больше нравится.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">



### Сборка из командной строки 


<div class="mw-collapsible-content">


<div class="mw-translate-fuzzy">

Шаги по компиляции из командной строки зависят от компилятора. Для MSVC 2017 следующие шаги:

1.  В меню \"Пуск\" Windows перейдите в **Visual Studio 2017 → Visual Studio Tools** и выберите \"\"Командная строка разработчика для VS 2017\"\"
2.  Перейдите в папку сборки.
3.  Выполните команду


</div>


```pythonmsbuild ALL_BUILD.vcxproj /p:Configuration=Release```

или


```pythonmsbuild INSTALL.vcxproj /p:Configuration=Release```


<div class="mw-translate-fuzzy">

Эти шаги также могут быть автоматизированы. Вот, например, решение для MSVC 2017:

1.  Скачать скрипт [compile-FC.txt](https://forum.freecadweb.org/download/file.php?id=92135).
2.  Переименуйте его в \"compile-FC.bat\".
3.  В проводнике файлов Windows Shift+Right-click на папке сборки и используйте из контекстного меню \"Command prompt here\".
4.  Выполните команду


</div>


```pythoncompile-FC install```

Вместо вызова **compile-FC** с опцией *install* вы также можете использовать *debug* или *release*.:

*debug*   - компиляция FreeCAD в конфигурации отладки

*release* - компиляция FreeCAD в конфигурации выпуска

*install*    - скомпилируйте FreeCAD в конфигурации выпуска и создайте установку установки


</div>


</div>



## Запуск и установка FreeCAD 

Существует 2 метода для запуска скомпилированного FreeCAD:

\"Метод 1\": Вы выполняете FreeCAD.exe которые вы найдете в своей папке сборки во вложенной папке \"bin\"

\"Метод 2\": Вы создаете целевую \"УСТАНОВКУ\"

Метод 2 является более простым, поскольку он автоматически гарантирует, что все библиотеки, необходимые для запуска FreeCAD.exe находятся в нужной папке. В FreeCAD.exe и библиотеки будут выведены в папку, указанную вами в переменной CMake \"CMAKE_INSTALL_PREFIX\".


<div class="mw-translate-fuzzy">

Для метода 1 вам нужно поместить библиотеки в папку \"bin\" вашей папки сборки (где FreeCAD.exe есть). Это можно легко сделать:

1.  Откройте графический интерфейс CMake.
2.  Найдите там параметр переменной \"FREECAD_COPY_DEPEND_DIRS_TO_BUILD\" и проверьте его. Если такой опции нет, библиотеки уже были скопированы, см. [description of the options](#Options_for_the_build_process.md).
3.  Найдите там параметр переменной \"FREECAD_COPY_LIBPACK_BIN_TO_BUILD\" и проверьте его.
4.  Найдите там параметр переменной \"FREECAD_COPY_PLUGINS_BIN_TO_BUILD\" и проверьте его.
5.  Нажмите на кнопку \"Configure\". В конце настройки CMake автоматически скопирует необходимые библиотеки из папки LibPack.


</div>

### Troubleshooting

When running FreeCAD you may encounter missing DLLs when using certain workbenches or features of workbenches. The error message in FreeCAD\'s console will not tell you what DLL is missing. To find this out you must use an external tool:

-   Download the latest release of the program **Dependencies**: <https://github.com/lucasg/Dependencies/releases> (choose the file *Dependencies_x64_Release.zip*)
-   In the FreeCAD [Python console](Python_console.md) execute these commands:

import os
os.system(r"~\DependenciesGui.exe")

**Note**: Instead of the \~ you must specify the full path to the *DependenciesGui.exe* on your system.

-   Now drag in the \*.pyd file of the workbench with which you get missing DLLs reported.



## Обновление сборки 

FreeCAD очень активно развивается. Поэтому его исходный код меняется почти ежедневно. Добавляются новые функции и исправляются ошибки. Чтобы извлечь выгоду из этих изменений исходного кода, вы должны перестроить свой FreeCAD. Это делается в два этапа:

1.  Обновление исходного кода
2.  Перекомпиляция



## Обновление исходного кода 



#### Использование интерфейса 

При использовании [Git frontend](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit:

1.  Щелкните правой кнопкой мыши папку с исходным кодом FreeCAD в проводнике файлов Windows и выберите в контекстном меню \"\"Pull\"\".
2.  Появится диалоговое окно. Выберите там, какую ветвь разработки вы хотите получить. \"master\" - это основная ветвь. Поэтому используйте это, если вы не хотите скомпилировать специальную новую функцию из ветви, которая еще не была объединена в \"master\". (Для получения дополнительной информации о ветвях Git см. [Git development process](Source_code_management#Git_development_process.md).)

Наконец, нажмите \"ОК\".



#### Использование командной строки 

Откройте терминал (командная строка) и переключитесь там в свой исходный каталог. Затем введите:


```python
git pull https://github.com/FreeCAD/FreeCAD.git master
```

где \"master\" - название основной ветви разработки. Если вы хотите получить код из другой ветви, используйте ее имя вместо \"master\".



#### Сборник


<div class="mw-translate-fuzzy">

1.  Откройте среду разработки MSVC, дважды щелкнув файл \"FreeCAD.sln\" или файл \"ALL_BUILD.vcxproj\" в папке сборки.
2.  Перейдите к шагу 2 из раздела [Building with Visual Studio 15 2017](#Building_with_Visual_Studio_15_2017.md).


</div>

## Updating the LibPack 

If a new major version of a third-party dependency like Open Cascade is released, or if a third-party dependency has important bug fixes, a new LibPack is released. You can find the latest version [here](https://github.com/FreeCAD/FreeCAD-LibPack/releases/).

To update your LibPack the following recipe is best practice:

1.  Delete the *bin* folder in your build folder.
2.  Switch to your local LibPack folder and delete everything there.
3.  Extract the content of the new LibPack ZIP file into the existing, but now empty, local LibPack folder.
4.  Open CMake and there press the button **Configure** and then the button **Generate**. This recreates the *bin* folder you just deleted and also copies the new LibPack files into it.
5.  In CMake click the button **Open Project** and the MSVC IDE will open.
6.  In the MSVC IDE build the target *INSTALL*.



## Инструменты

Для того, чтобы включиться к разработке FreeCAD, вы должны скомпилировать и установить следующие инструменты:



#### Плагин Qt designer 

FreeCAD использует [Qt](https://en.wikipedia.org/wiki/Qt_(software)) в качестве инструментария для его пользовательского интерфейса. Все диалоговые окна настраиваются в UI-файлах, которые можно редактировать с помощью программы [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html), который является частью любой установки Qt, а также включен в пакет LibPack. FreeCAD имеет свой собственный набор виджетов Qt для предоставления специальных функций, таких как добавление единицы измерения в поля ввода и настройка свойств настроек.



#### Сборник 


<div class="mw-translate-fuzzy">

DLL не может быть загружена как плагин, если она была скомпилирована с использованием другой версии Qt, чем тот, на котором основан ваш Qt Designer/Qt Creator. В этом случае вы должны скомпилировать DLL самостоятельно. Это делается следующим образом:


</div>

-   In the CMake options (see [this section above](Compile_on_Windows#Options_for_the_build_process.md)) enable the option BUILD_DESIGNER_PLUGIN and reconfigure.
-   open MSVC and build the target **FreeCAD_widgets**

As result you will get the plugin file *\'FreeCAD_widgets.dll* in the folder*\~\\src\\Tools\\plugins\\widget\\Release*



### Установка


<div class="mw-translate-fuzzy">

1.  Скачать [this ZIP](https://forum.freecadweb.org/download/file.php?id=124239) файл. (Скомпилирован с использованием Qt 5.12, см. [below](#Compilation.md).)
2.  Извлеките DLL-файл в ZIP-файле и скопируйте его

-   Если вы используете LibPack: в папку\"\~\\FreeCADLibs_12.5.2_x64_VC17\\bin\\designer\", так как там будет только папка \"bin\", и вы должны сначала создать подпапку \"конструктор\".
-   Если у вас полная установка Qt: вы можете выбрать между folder\"C:\\Qt\\5.15.2\\msvc2019_64\\plugins\\designer\"or\"C:\\Qt\\5.15.2\\msvc2019_64\\bin\\designer\" (сначала вы должны создать подпапку \"конструктор\".)(адаптируйте пути к вашей установке!).


</div>


<div class="mw-translate-fuzzy">

(Повторно)Запустите Qt Designer и проверьте его меню **Help → Plugins**. Если плагин \"\' FreeCAD_widgets.dll\"\' указана как загружаемая, теперь вы можете создавать и изменять файлы .ui FreeCAD. Если нет, вы должны [compile](#Compilation.md) создать библиотеку DLL самостоятельно.


</div>


<div class="mw-translate-fuzzy">

Если вы предпочитаете использовать [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator) вместо Qt Designer библиотека DLL должна быть помещена в эту папку:\"C:\\Qt\\Qt5.15.2\\Tools\\QtCreator\\bin\\plugins\\designer\"(Повторно)Запустите Qt Creator, переключитесь в режим \"Design\", а затем проверьте меню **Tools → Form Editor → About Qt Designer Plugins**. Если плагин \"\' FreeCAD_widgets.dll\"\' указана как загружаемая, теперь вы можете создавать и изменять файлы .ui FreeCAD. Если нет, вы должны [compile](#Compilation.md) создать библиотеку DLL самостоятельно.


</div>



### Поставщик миниатюр 

FreeCAD имеет функцию предварительного просмотра миниатюр для файлов \*.FCStd. Это означает, что в проводнике файлов Windows \*.FCStd файлы отображаются со снимком экрана модели, которую он содержит. Чтобы предоставить эту функцию, FreeCAD должен иметь файл \"\'FCStdThumbnail.dll\"\" где установлено в Windows.



### Установка 

Библиотека DLL устанавливается таким образом:

1.  Скачать [this ZIP file](https://forum.freecadweb.org/download/file.php?id=13404) и извлеките его.
2.  Откройте командную строку Windows с правами администратора (эти права являются обязательным требованием).
3.  Перейдите в папку, в которой находится библиотека DLL.
4.  Выполните эту команду 
```pythonregsvr32 FCStdThumbnail.dll```

Поэтому проверьте, работает ли это, убедитесь, что в FreeCAD включена опция настроек \"[Save thumbnail into project file when saving document](Preferences_Editor#Document.md)\"\" и сохраните модель. Затем просмотрите в проводнике Windows папку сохраненной модели, используя представление символов. Теперь вы должны увидеть снимок экрана модели в представлении папок.



#### Сборник 

Для компиляции FCStdThumbnail.dll

1.  Перейдите в исходную папку FreeCAD\"\~\\src\\Tools\\thumbs\\ThumbnailProvider\"
2.  Откройте графический интерфейс CMake
3.  Укажите там в качестве исходной папки ту, в которой вы находитесь в данный момент.
4.  Используйте ту же папку, что и папка сборки.
5.  Нажмите \"Configure\".
6.  В появившемся диалоговом окне укажите генератор в соответствии с тем, который вы хотите использовать. Для стандартной MS Visual Studio используйте \"Visual Studio xx 2yyy\", где xx-версия компилятора, а 2yyy-год его выпуска. Рекомендуется использовать опцию по умолчанию \"Использовать собственные компиляторы по умолчанию\".\"Примечание:\" Важно указать правильный вариант бита. Если у вас 64-битный вариант LibPack, вы также должны использовать компилятор x64.
7.  Нажмите на кнопку \"Generate\".
8.  Теперь у вас должен быть файл \"ALL_BUILD.vcxproj\" в папке \"\~\\src\\Tools\\thumbs\\ThumbnailProvider\". Дважды щелкните по нему, и откроется среда разработки MSVC.
9.  На панели инструментов среды разработки MSVC убедитесь, что вы используете целевой объект компиляции \"Release\".
10. Есть окно под названием \"Solution Explorer\". Щелкните правой кнопкой мыши на \"ALL_BUILD\", а затем выберите \"Build\".
11. В результате у вас теперь должно быть \"\'FCStdThumbnail.dll\"\' в папке \"\~\\src\\Tools\\thumbs\\ThumbnailProvider\\release\", который вы можете установить, как описано выше.




<div class="mw-translate-fuzzy">

## Компиляция OpenCascade 


</div>


<div class="mw-translate-fuzzy">

Стандартный пакет Libpack поставляется с версией OpenCascade, подходящей для общего использования. Однако при некоторых обстоятельствах вы можете захотеть скомпилировать с альтернативной версией OpenCascade, такой как один из их официальных релизов или исправленная ветвь. Обратите внимание, что нет никакой гарантии, что FreeCAD будет работать со всеми версиями OpenCascade, и использование версии, отличной от Libpack, предназначено только для продвинутых пользователей. Обратите также внимание, что если вы используете библиотеку Netgen, она использует OpenCascade для некоторых своих функций и должна быть скомпилирована с той же версией OpenCascade, которую вы используете при компиляции FreeCAD.


</div>

When compiling Open Cascade for FreeCAD note that there is no guarantee that FreeCAD will work with all versions of Open Cascade. Note also that when you are using the Netgen library, you must use the a NetGen version that it approved to compile with the Open Cascade version you like to compile.


<div class="mw-translate-fuzzy">

Сначала получите исходный код OpenCascade либо непосредственно со страницы выпуска по адресу [OpenCASCADE.org](https://old.opencascade.com/content/latest-release), через [git](https://git.dev.opencascade.org/repos/occt.git), или путем клонирования чужой вилки, например [вилка \"blobfish\"](https://gitlab.com/blobfish/occt) поддерживается участником форума FreeCAD [tanderson69](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=208).


</div>


<div class="mw-translate-fuzzy">

Затем используйте CMake для настройки системы сборки аналогично созданию FreeCAD. Примечательными вариантами CMake для OpenCascade являются:

-   **3RDPARTY_DIR** - Место расположения ваших сторонних библиотек, обычно заданное в каталоге FreeCAD Libpack
-   **INSTALL_DIR** - Где устанавливают готовые библиотеки. Рекомендуется использовать изолированный каталог в вашей системе, а не устанавливать его глобально или перезаписывать версию Libpack.


</div>

-   Open the project in Visual Studio and first build the ALL_BUILD and then INSTALL targets in the **Release** mode.
-   Repeat building the two targets in the **Debug** mode.

To build FreeCAD using the self-compiled Open Cascade, you must do the following:

-   Copy all folders from the INSTALL_DIR to your LibPack folder (overwrite the existing files)
-   Switch to the LibPack folder and go there to the subfolder *cmake*
-   Open there the file *OpenCASCADEDrawTargets.cmake* with a text editor
-   Search there for absolute paths to your LibPack folder and remove them. So e.g. the absolute path*D:/FreeCADLibs_12.5.4_x64_VC17/lib/freetype.lib*becomes just *freetype.lib*
-   Do the same for the file *OpenCASCADEVisualizationTargets.cmake*

## Compiling Netgen 

The LibPack comes with a version of [Netgen](https://ngsolve.org) that will was tested to be build with the Open Cascade version of the LibPack. The problem is that every new release of Netgen changes the API. Also every new release of Open Cascade does the same. Therefore one cannot just easily change the Netgen version.

However, you might build Netgen nevertheless. This is an easy task:

-   First obtain the Netgen source code, either directly from [Netgen \'s git repository](https://github.com/NGSolve/netgen).
-   Then open the CMake GUI to configure the build system in a similar manner to building FreeCAD. These CMake options have to be set:

  Variable name          Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Default
    
  CMAKE_INSTALL_PREFIX   The output folder when building the target *INSTALL*. If the build was successful, take the files from this folder to update your LibPack.                                                                                                                                                                                                                                                                                                                                                                                                        C:/netgen
  OpenCasCade_DIR        The path to the CMake files of Open Cascade. If you built Open Cascade as described in the section [Compiling Open Cascade](#Compiling_Open_Cascade.md) you can use the subfolder *cmake* of there folder you used as INSTALL_DIR. If not, use the subfolder *cmake* of your LibPack. Note hereby that the LibPack must then already contain a proper Open Cascade build. Independent what folder you use, you must now also create there a subfolder *lib* and copy in the files *freetype.lib* and *freetyped.lib* from your LibPack.   empty
  USE_GUI                set it to **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ON
  USE_NATIVE_ARCH        set it to **OFF**; this is only necessary important to support older CPU that don\'t have the [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) instruction set                                                                                                                                                                                                                                                                                                                                                                    ON
  USE_OCC                set it to **ON**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  OFF
  USE_PYTHON             set it to **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ON
  USE_SUPERBUILD         set it to **OFF**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ON
  ZLIB_INCLUDE_DIR       The path to the necessary 3rdparty component [zlib](https://en.wikipedia.org/wiki/Zlib). It is recommended to use the folder as input where your used LibPack is.                                                                                                                                                                                                                                                                                                                                                                                 empty
  ZLIB_LIBRARY_DEBUG     The path to the ZLib file *zlibd.lib*. It is located in the subfolder *lib* of your LibPack folder.                                                                                                                                                                                                                                                                                                                                                                                                                                               empty
  ZLIB_LIBRARY_RELEASE   The path to the ZLib file *zlib.lib*. It is located in the subfolder *lib* of your LibPack folder.                                                                                                                                                                                                                                                                                                                                                                                                                                                empty

-   Additionally you need to add a new CMake entry:

name: *CMAKE_DEBUG_POSTFIX*, type: *string*, content: **\_d** This assures that he file names of the debug libraries get another name than the release libraries and can later not be accidentally exchanged.

-   Press the *Configure* button in CMake to generate the \*.cmake files.
-   Only necessary if older CPU should be supported that don\'t have the AVX2 instruction set:
    -   Search your Netgen build folder for the file *netgen-targets.cmake* and open it with a text editor. Remove the setting *;/arch:AVX2* in the Option INTERFACE_COMPILE_OPTIONS.
    -   Press the *Configure* button in CMake again.
-   Press the *Generate* button in CMake.
-   Open the project in Visual Studio and first build the ALL_BUILD and then INSTALL targets in the **Release** mode.
-   Repeat building the two targets in the **Debug** mode.

To build FreeCAD using the self-compiled Netgen, you must do the following:

-   Copy all folders from the CMAKE_INSTALL_PREFIX to your LibPack folder (overwrite the existing files)



## Ссылки на литературу 


<div class="mw-translate-fuzzy">

Смотрите также

-   [Compiling - Speeding up](Compiling_(Speeding_up).md)


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on Windows/ru
