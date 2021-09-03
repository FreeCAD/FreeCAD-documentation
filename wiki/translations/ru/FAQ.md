




На этой странице содержатся ответы на самые часто задаваемые вопросы на форуме FreeCAD. Если у вас есть проблема или вопрос, касающийся FreeCAD, попробуйте найти на него ответ на этой странице. Затем, если вы не смогли найти ответ на ваш специфический вопрос, обратитесь на [форум FreeCAD](http://forum.freecadweb.org/viewforum.php?f=3)!

## Установка

### Каков самый простой путь для установки FreeCAD в моей системе? {#каков_самый_простой_путь_для_установки_freecad_в_моей_системе}


<div class="mw-translate-fuzzy">

Если Вы используете Windows или Mac OS, то самый простой способ для Вас - перейти на [страницу загрузки](Download/ru.md), где вы найдёте несколько готовых для установки пакетов. Если Вы используете Debian, Fedora, Ubuntu или другой дистрибутив, то FreeCAD уже включён в стандартный программный репозиторий и Вы можете установить его с помощью менеджера программного обеспечения. На Ubuntu команда FreeCAD поддерживает собственный [PPA репозитории](Download#Ubuntu_PPA_packages.md). С более подробными сведениями Вы можете ознакомиться на следующих страницах: ([Установка в Windows](Installing_on_Windows/ru.md), [Установка в Linux](Installing_on_Linux/ru.md) или [Установка в Mac](Installing_on_Mac/ru.md)).


</div>

### Каковы системные требования для запуска FreeCAD? {#каковы_системные_требования_для_запуска_freecad}

In contrast to most 3D CAD software, FreeCAD can run smoothly on the most modest computers - it\'s been known to run on Pentium IV and Intel Core2 Solo CPUs. If your computer is running a current operating system, chances are FreeCAD will run. The only prerequisite is that your graphics card or chipset must support [OpenGL](https://en.wikipedia.org/wiki/OpenGL), preferably no older than v2.0. In case of problems, refer to the [Troubleshooting](Frequently_asked_questions#Troubleshooting.md) section of this FAQ.

#### Многопоточность

FreeCAD\'s underlying geometric modeling kernel, the [OpenCASCADE Technology](http://en.wikipedia.org/wiki/Open_Cascade_Technology) (OCCT) third-party library, [has only partial multi-threading support at this time](https://forum.freecadweb.org/viewtopic.php?f=4&t=17501&p=173095&hilit=Multithread#p173095). See the [multithreading](multithreading.md) page for more details.

#### Для Mac пользователей {#для_mac_пользователей}

Only the MacIntel architecture is supported. There are no builds available for the PowerPC architecture.

### Что, если Я хочу скомпилировать FreeCAD самостоятельно? {#что_если_я_хочу_скомпилировать_freecad_самостоятельно}

The source code of FreeCAD is always available in the project source code repository. Compiling FreeCAD yourself allows you to use the most recent features being developed, but requires a bit of computer knowledge, although the procedure is fairly simple. Access to the source code is explained [here](Compile_on_Linux#Getting_the_source.md), and we have detailed instructions for compiling on [Windows](Compile_on_Windows.md), [Linux](Compile_on_Linux/Unix.md) and [macOS](Compile_on_MacOS.md).

### FreeCAD сообщает, что какой-то модуль или приложение отсутствует {#freecad_сообщает_что_какой_то_модуль_или_приложение_отсутствует}

FreeCAD depends on a lot of things to offer all its functionality. All the main required components are usually bundled within your FreeCAD installation or provided by your package manager, so normally you have nothing to worry about. If you installed FreeCAD from unofficial sources, however, or compiled FreeCAD yourself, some piece might be missing, which is not critical to FreeCAD itself, but might cause some functionality to be unavailable. Some specific file formats such as Collada or DWG also require extra components, which cannot be bundled into FreeCAD, and must be installed by yourself separately.

All those components and the appropriate way to install them are listed on the [Extra python modules](Extra_python_modules.md) page.

## Разрешение проблем {#разрешение_проблем}

### FreeCAD вообще не запускается {#freecad_вообще_не_запускается}

Причин может быть много, скорее всего, отсутствует какая-то библиотека. Попробуйте запустить FreeCAD из терминала (введите {{SystemInput|freecad}} в командной строке терминала, {{SystemInput|FreeCAD}} в некоторых системах) чтобы увидеть, появляются ли какие-либо сообщения об ошибках. Кроме того, прочитайте оставшуюся часть данной странице, поскольку это может дать дополнительные сведения для обнаружения проблемы. Если ничего не помогает, расскажите об этом на [1](http://forum.freecadweb.org/forum), наверняка найдётся кто-нибудь, кто сможет вам помочь.

On some older Windows XP systems you may get an error message like this: **The application can't start, because the side-by-side configuration is wrong. The reinstallation of the application may solve the problem.** The reason for this problem is that on your system either the CRT runtime libraries are missing or the version installed is too old because FreeCAD was linked against a newer version. In this case you have to install the **Microsoft Visual C++ Redistributable Package** which you\'ll find at Microsoft. See also the corresponding [forum message](http://forum.freecadweb.org/viewtopic.php?f=3&t=1298&p=9961).

### FreeCAD запускается нормально, но не все иконки отображаются, некоторые из них заменены на черные значки \'X\' {#freecad_запускается_нормально_но_не_все_иконки_отображаются_некоторые_из_них_заменены_на_черные_значки_x}

Некоторые части FreeCAD зависят от внешнего модуля Python называемого Pivy. В Windows pivy включена в установочный пакет FreeCAD. В системах Debian/Ubuntu пакет python-pivy входит в стандартные репозитории. В других системах в данный момент вам, возможно, придётся самостоятельно собирать pivy. Обратите внимание, что, хотя некоторые инструменты не будут работать без pivy, остальные части FreeCAD будут работать нормально.

### У меня проблемы с отображением, 3D-вид работает неправильно, при перемещении / повороте изображения появляется мусор и т.п. {#у_меня_проблемы_с_отображением_3d_вид_работает_неправильно_при_перемещении_повороте_изображения_появляется_мусор_и_т.п.}

FreeCAD depends on OpenGL for displaying 3D contents, and therefore requires a working OpenGL environment. On some systems, OpenGL is not activated by default, and you might need to install or upgrade your graphics drivers. This problems happens most often on Linux systems or on virtual systems. If you are on a Linux-based system, try the following steps:

-   verify that your computer has a 3D-capable graphics board
-   type {{SystemInput|glxinfo}} in a terminal window, and check in the output that Direct Rendering is set to \"yes\", and that the OpenGL vendor/renderer/version matches your graphics card.
-   install other OpenGL-based software ([Blender](http://www.blender.org), for example) and check if it runs and displays correctly.

### FreeCAD вылетает при запуске {#freecad_вылетает_при_запуске}

Сбой может указывать на более серьезную ошибку или проблему в вашей конфигурации. Большинство сбоев при запуске происходит по одной из двух следующих причин:

#### OpenGL драйвер не установлен или работает не правильно {#opengl_драйвер_не_установлен_или_работает_не_правильно}

Это очень частая причина проблемы. Её симптомы - сбой FreeCAD при запуске, или всякий раз, когда Вы открываете 3D вид (например, при создании нового документа). Постарайтесь выяснить, какой у вас графический чип, затем выясните, поддерживает ли он [OpenGL](http://ru.wikipedia.org/wiki/OpenGL) (самые послежние - поддерживают), затем найдите правильный драйвер и установите его. Хороший способ проверить, работает ли OpenGL - попытаться запустить другое приложение, его использующее, например [blender](http://www.blender.org).

And as a general tip to get some more information about crashes with FreeCAD you can start it with the program parameter {{SystemInput|--write-log}}. This will create the file {{FileName|FreeCAD.log}} in {{FileName|$HOME/.FreeCAD}} on Linux or {{FileName|$HOME/Library/Preferences/FreeCAD}} on macOS or {{FileName|%APPDATA%/FreeCAD}} on Windows systems.

In some rare cases you may have a graphic driver installed that doesn\'t fit to your graphic card. We had a case where the user\'s laptop had an Intel on-board graphic but some ATI drivers were installed. [2](http://forum.freecadweb.org/viewtopic.php?f=13&t=5160&start=10#p41042) After removing the files and re-installing the correct driver FreeCAD started to work.

#### Библиотека, нужная для работы FreeCAD, отсутствует в системе или не найдена {#библиотека_нужная_для_работы_freecad_отсутствует_в_системе_или_не_найдена}

Эта проблема может иметь две причины: либо какая-то библиотека просто отсутствует, поэтому FreeCAD не запускается, либо библиотека есть, но более старая версия, чем требуется для FreeCAD, поэтому при попытке запустить FreeCAD происходит сбой, т. к. FreeCAD пытается использовать функцию из этой библиотеки, которой в ней нет. Типичный пример: когда в вашей системе установлены Qt3 и Qt4, FreeCAD может обнаружить Qt4, но, если Qt не настроенна должным образом, некоторые части Qt3 всё ещё могут использоваться, вызывая сбои.

Please review the installing procedure ([Windows](Installing_on_Windows.md), [Linux](Installing_on_Linux.md) or [Mac](Installing_on_Mac.md)), make sure you installed all the required libraries (on most linux systems this is done automatically), and check what is the minimum version number for each of the components.

If everything seems correct, describe the problem on the [forum](http://forum.freecadweb.org/) or [submit a bug](Tracker.md). If you are on a linux system, it is easy to do a debug backtrace, which provides very useful information about the crash to the developers:

-   in a terminal, type: {{SystemInput|gdb freecad}} (assuming package gdb is installed)
-   inside gdb, type {{SystemInput|run}}
-   after the crash, type {{SystemInput|bt}} to get the backtrace, that you can include in your bug report.

### FreeCAD зависает после запуска {#freecad_зависает_после_запуска}

When starting FreeCAD the GUI appears almost immediately but the GUI is frozen and the cpu is about 99%. This can happen on the KDE desktop when using the Oxygen theme. That\'s a bug in the Oxygen theme and choosing another theme should fix this issue.

### FreeCAD crashes on creating a new document or opening a file {#freecad_crashes_on_creating_a_new_document_or_opening_a_file}

If FreeCAD crashes when it creates a new 3D view, try launching FreeCAD from a terminal. If a message error appears when the crash occurs, mentioning {{SystemOutput|Assertion Failed}}, and a component name beginning with \"So\" ({{SystemOutput|SoBase}}, {{SystemOutput|SoFieldContainer}}, etc.), the chances are very high, especially if you are on Linux, that FreeCAD is trying to use two different versions of the Coin library, which causes the crash. To verify if that is indeed the problem, try the following:

-   Locate the FreeCAD executable (usually in {{FileName|/usr/lib/FreeCAD/bin}})
-   Run the command {{SystemInput|ldd FreeCAD}} from a terminal
-   Note down the version of the {{FileName|libCoin.so}} library that FreeCAD is using (for example {{FileName|libCoin.so.60}})
-   Locate the {{FileName|libSoQt.so}} library (usually in {{FileName|/usr/lib}})
-   run {{SystemInput|ldd libSoQt.so}} and check if it links to the same Coin version as FreeCAD

If there is any difference, either FreeCAD or SoQt must be recompiled (better to recompile the one that uses the oldest Coin version). The normal behavior is to try to contact the people responsible for packaging either SoQt or FreeCAD and kindly ask them to consider recompiling. If you want to undertake that step for yourself, and it is not possible to recompile SoQt because it breaks other applications on your system, you can force FreeCAD to compile with the required Coin version with {{SystemInput|<nowiki>./configure --with-coin=DIR</nowiki>}}. But you have to make sure that the correct development package of this Coin version is installed.

### FreeCAD вылетает после команды Правка → Выравнивание {#freecad_вылетает_после_команды_правка_выравнивание}

Ошибка сегментации происходит в {{SystemOutput|vbo_save_playback_vertex_list()}}. Это означает, что в графическом драйвере плохая реализация VBO. Чтобы избежать кэширования вызовов OpenGL, вы можете попытаться установить переменную среды {{SystemInput | <nowiki> IV_SEPARATOR_MAX_CACHES = 0 </nowiki>}} и перезапустить FreeCAD.


<div class="mw-translate-fuzzy">

### У меня проблемы с запуском FreeCAD на Mac OS X {#у_меня_проблемы_с_запуском_freecad_на_mac_os_x}


</div>


<div class="mw-translate-fuzzy">

Платформу Mac труднее поддерживать чем Windows или Linux, так как ни один из главных разработчиков ей не владеет. Пакеты для OS X скомпилированы волонтёрами-пользователями FreeCAD, и иногда могут некорректно работать на вашем компьютере, в зависимости от вашей системы. Вероятно, лучшее решение для вас - посетить форум, найти темы, связанные с Mac OS X и обсудить там вашу проблему или посмотреть, нашёл ли кто-нибудь её решение.


</div>

### I cannot change numeric values in FreeCAD\'s properties panels {#i_cannot_change_numeric_values_in_freecads_properties_panels}

<img alt="language options" src=images/Jj62l.png  style="width:480px;">

You most likely have bad windows regional settings set-up. Please check if you have the same symbol for decimal separator and digit grouping symbol in your regional settings. If you do, [adapt your system settings](http://forum.freecadweb.org/viewtopic.php?f=4&t=2655&p=20046#p20041) to use different characters for the digit grouping symbol and decimal separator. Note that it is not mandatory to have dot as decimal separator. It is mandatory to use different symbols in these two settings. 

### FreeCAD was running normally, and suddenly it doesn\'t start anymore {#freecad_was_running_normally_and_suddenly_it_doesnt_start_anymore}

This can also happen if you had an older version of FreeCAD installed, and you upgraded to a newer version. In that process, the configuration files of FreeCAD might have been corrupted for some reason, and now FreeCAD cannot read them anymore, and fails to start. The solution is simply to delete these configuration files, so FreeCAD will recreate them on first run.

-   On Windows: Open the file explorer, and write {{FileName|%APPDATA%\FreeCAD}} as the file path. Once there, delete the files {{FileName|user.cfg}} and {{FileName|system.cfg}}
-   On Linux: Navigate to {{FileName|/home/USERNAME/.FreeCAD}} and delete the files {{FileName|user.cfg}} and {{FileName|system.cfg}}
-   On Mac: Navigate to {{FileName|/Users/USERNAME/Library/Preferences/FreeCAD}} and delete the files {{FileName|user.cfg}} and {{FileName|system.cfg}}

FreeCAD should now start again normally with all its settings reset.

There is a [Macro findConfigFiles](Macro_findConfigFiles.md) available to help in locating your configuration files. It can be installed using the Addon Manager in the Tools menu. {{MenuCommand|Tools → Addon Manager → Macros → findConfigFiles}}. The macro will find your config file folder, copy it to the clipboard, and (attempt to) open that location with your default file browser. It makes no changes to your files or settings.

## Использование FreeCAD {#использование_freecad}

### FreeCAD действительно бесплатный? Даже для коммерческого использования? {#freecad_действительно_бесплатный_даже_для_коммерческого_использования}

FreeCAD это [программное обеспечение с открытым исходным кодом](http://ru.wikipedia.org/wiki/Open-source_software), и Вы можете его бесплатно использовать не только для себя или в коммерческих целях, но, также, можете распространять, модифицировать и использовать в приложениях с закрытым исходным кодом. В общем, Вы можете делать с ним (почти) всё, что захотите. См. страницу [Лицензия](Licence/ru.md) для получения более подробной информации.

### Как я могу повернуть 3D вид? {#как_я_могу_повернуть_3d_вид}


<center>

Image:Style\_of\_navigation.png\|От **правой кнопки** мыши Image:Style of navigation menu.png\|Из меню {{MenuCommand|Правка → Настройки →}}


</center>




FreeCAD has several different [navigation modes](Mouse_navigation.md) available, that can be set in the preferences settings dialog or changed by right-clicking in the 3D view. For full details about the modes, see the [Mouse navigation](Mouse_navigation.md) page. For the default mode (\"CAD Navigation\"), the commands are as follows, 


{{CAD Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view<br>First method
|Rotate_view_alt_name=Rotate view<br>Alternate method
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Press the left mouse button over an object you want to select.

Holding down **Ctrl** allows the selection of multiple objects.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Pan_mode_text=Pan mode: hold the **Ctrl** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Zoom_text=Use the mouse wheel to zoom in and out.

Clicking the middle mouse button re-centers the view on the location of the cursor.
|Zoom_mode_text=Zoom mode: hold the **Ctrl** and **Shift** keys, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Rotate_view_text=Hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

The cursor location when the middle mouse button is pressed determines the center of rotation. Rotation works like spinning a ball which rotates around its center. If the buttons are released before you stop the mouse motion, the view continues [spinning](spinning.md), if this is enabled.

A double click with the middle mouse button sets a new center of rotation.
|Rotate_view_mode_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Rotate_view_alt_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

With this method the middle mouse button may be released after the right mouse button is held pressed.

Users who use the mouse with their right hand may find this method easier than the first method.
}}

### What can I do with FreeCAD? Where do I start? {#what_can_i_do_with_freecad_where_do_i_start}

Head to the [Getting started](Getting_started.md) page for a quick description of the tools you can use. There is also a new [Tutorials](Tutorials.md) section containing a few resources. The [User hub](User_hub.md) section contains more detailed information about the different workbenches of FreeCAD. Note that since FreeCAD is relatively new, its user interface is still very bare and doesn\'t feature many tools. But much more advanced functionality is already available to you from [Python scripting](Power_users_hub.md).

### Is there documentation for newcomers? How can I learn to use FreeCAD? {#is_there_documentation_for_newcomers_how_can_i_learn_to_use_freecad}

There is a lot of documentation spread in different places, both on and outside the FreeCAD website. You might want to start with the [Getting started](Getting_started.md) page. The [Tutorials](Tutorials.md) section contains many specialized tutorial pages to help you getting started with the different workbenches. The [Manual:Introduction](Manual:Introduction.md) is a general, complete user-oriented guide to FreeCAD. The [User hub](User_hub.md) section of this wiki lists all pages aimed at end users. On external sites like [Youtube](https://www.youtube.com/results?search_query=freecad), you will also find a load of video tutorials created by users. And, last but not least, the [forum](https://forum.freecadweb.org) contains a lot of replies to questions asked by other newcomers.

### I want to import/export data in format XYZ to/from FreeCAD. How do I do that? {#i_want_to_importexport_data_in_format_xyz_tofrom_freecad._how_do_i_do_that}

Please refer to the page [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md). Maybe your questions are already answered there.

## Работа с геометрией Детали {#работа_с_геометрией_детали}

### How do I extrude stuff into solids? I don\'t get the right result {#how_do_i_extrude_stuff_into_solids_i_dont_get_the_right_result}

The theory is simple: Lines (or wires), when extruded, form faces. Faces, when extruded, form solids. If you extrude something and the result is not a solid, then the something was not a face. If you have lines and you want to extrude a solid from them, you must first select lines that form a closed perimeter (select several objects by pressing **Ctrl**), join them into a wire ([Draft Upgrade tool](Draft_Upgrade.md)), then make a face from that wire (<img alt="" src=images/Draft_Upgrade.svg  style="width:16px;"> Upgrade tool again). There you are, if all went well you can now extrude it to a solid.

Now, there can be many little twists that make you obtain the wrong result. The best way to make sure is to check what\'s inside the object you are extruding. Objects contents can be easily explored with python. Assuming for example you have an object called \"Wire\", you could type this into the Python console:


{{code|code=
obj = FreeCAD.ActiveDocument.Wire
shp = obj.Shape
print shp.Faces
print shp.Wires
if shp.Wires:
    for w in shp.Wires:
        print w.isClosed()
}}

The above code retrieves the shape from an object, shows the faces and wires your object has (if any), and, if there are wires, prints if those wires are closed. If you don\'t have any face, you won\'t get a solid. If there is no closed wire, it won\'t become a face. If you are interested, there is more info about what you can check with Python on the [part scripting](Topological_data_scripting.md) page. If you cannot join several lines into a wire, the most probable cause is that their endpoints don\'t meet, there must be small gaps between (some of) them. There, I\'m afraid, my experience tells me the quickest way would be to redraw a wire on top of them.

### My boolean operations fail, or give weird results {#my_boolean_operations_fail_or_give_weird_results}

The [Open CASCADE](https://en.wikipedia.org/wiki/Open_CASCADE_Technology) geometric modeling kernel used in FreeCAD for Part geometry, although probably the best open-source geometry kernel available, has its flaws and limitations. Indeed the boolean operations (fusion, subtraction, intersection) are not its best features, and often give strange results. This is a current limitation we have no way to solve at once, so your best path is to try obtaining the desired result by modeling another way. For example, problems with primitives such as cylinder can often be solved by using an extruded circle instead. Coplanar surfaces between parts can cause trouble, as well as surface tangency. As a general rule, if a shape doesn\'t work, try remodeling it a different way. In 99% of the cases at the end you will manage to obtain the result you want.

### When I export (or view) my model, the holes are filled in {#when_i_export_or_view_my_model_the_holes_are_filled_in}

Don\'t use **Crtl** + **A** (Select All) to export everything from the hierarchy tree. If the model is of one single item, try selecting only the newest item (usually the last one) in the hierarchy tree.

As we create a model in the [PartDesign Workbench](PartDesign_Workbench.md), each feature takes the shape of the last one and adds or removes something, creating linear dependencies from feature to feature as the model is created. Hence a \"Cut\" feature is not only the cut hole itself, but the whole part with the cut. This is why the user usually should only have the newest item (feature) in the model tree visible, because otherwise the phases of the model overlay each other, and holes are filled in by the earlier model features.

To toggle visibility of an object on or off, select it in the hierarchy tree and press **spacebar** on your keyboard. Usually everything but the last item in the hierarchy tree should be greyed out and therefore not visible in the 3D view.

### My parametric objects break when I modify their base sketches {#my_parametric_objects_break_when_i_modify_their_base_sketches}

You have met the (in)famous toponaming problem. This is currently a major issue in FreeCAD for newcomers. It is present all over FreeCAD, but is more prominent when using [sketches](Sketcher_Workbench.md). The explanation is simple: When recalculating a sketch, the geometric entities (edges, faces\...) are rebuilt in a different order, depending on the constraints precedence. They then receive a different name (Edge1, Edge2, Face1, Face2\...). Most subsequent operations depend on these names to identify which subcomponent they work on. Therefore, when the sketch is rebuilt, features that are based on such subcomponents might suddenly get their base geometry changed and give a wrong result.

This is a very hard problem to overcome (the [Topological Naming Project](Topological_Naming_Project.md) aims at solving it). However, there are many workarounds available to mitigate the problem, and more advanced users generally manage to avoid it completely. A couple of strategies are:

-   Know that sketches are highly sensitive to the problem. Referencing a specific edge of a sketch, or a face of an object built on a sketch, such as a [PartDesign Pad](PartDesign_Pad.md), is dangerous, unless you are pretty confident that these sketches will not change over time or the sketch is very simple. A Pad built on a simple rectangular sketch, for example, will likely be safe as it will generate only one face, so there is no order problem.
-   Prefer other kinds of objects such as [Part](Part_Workbench.md) or [Draft](Draft_Workbench.md) when possible. These objects are always built the same way, and therefore their geometric components usually follow the same order each time they are rebuilt. They are much less susceptible to toponaming problems.
-   To attach further objects onto the faces of sketch-based geometry, prefer using [Datum geometry](PartDesign_Plane.md). These invisible \"helper objects\" don\'t depend on sketch geometry, and therefore stay stable over time.

## Внести вклад в FreeCAD {#внести_вклад_в_freecad}

### FreeCAD is such a great program! How can I help? {#freecad_is_such_a_great_program_how_can_i_help}

There are a lot of different ways to help, even if you are not a programmer. Here are a couple of things you can do:

-   Give some feedback to the FreeCAD developers: It is always useful to know what people think, what they found good, what they miss, etc. Drop a note on the [forum](http://forum.freecadweb.org/) giving your opinion or make a request on our [issue tracker](https://tracker.freecadweb.org/main_page.php)!
-   Help with writing documentation: The documentation we have here on this site is sometimes very limited. If you discovered something that is not well documented, add your knowledge there!
-   Help others newcomers: Hang around the forum, and help new people to solve basic questions, like how do I install, how do I add a cube, etc.
-   [Translate the documentation](Help_FreeCAD#Translate_the_documentation.md) into your own language
-   [Translate FreeCAD](Help_FreeCAD#Translate_FreeCAD.md) into your own language
-   Write [Tutorials](Tutorials.md), or record video tutorials: Tutorials are a very easy way for newcomers to learn a new software. If you did some nice stuff, why not show other people how to do it?
-   Contribute with assets and examples: We are still missing good example files in FreeCAD. If you created something good, share it with us!
-   [Submit bugs](Tracker.md): It is very important to have all possible bugs fixed. If you find one, report it as clearly as possible, so we can understand exactly what\'s happening.
-   Try to do some Python coding: You never programmed before but you want to try? Python is easy. Read our [introduction to Python](Introduction_to_Python.md), but beware, you might get addicted quickly!
-   See the [Help FreeCAD](Help_FreeCAD.md) page for more details on how to contribute.

### How can I get edit permission on the wiki? {#how_can_i_get_edit_permission_on_the_wiki}

See the [Work on the documentation](Help_FreeCAD#Work_on_the_documentation.md) page paragraph for more details on how to contribute.

### Does FreeCAD participate in Google Summer of Code? {#does_freecad_participate_in_google_summer_of_code}

Yes. Beginning in 2016, FreeCAD participates in Google Summer of Code. See [Google Summer of Code 2020](Google_Summer_of_Code_2020.md) for information on past editions, and [Google Summer Of Code 2016](http://forum.freecadweb.org/viewtopic.php?f=8&t=13838) in the forum for the original announcement.

### I want to start translating the wiki in my own language. What do I do? {#i_want_to_start_translating_the_wiki_in_my_own_language._what_do_i_do}

This wiki is hosting a lot of contents. The most up-to-date and interesting material is gathered in the [manual](Online_Help_Toc.md).

See the [Translate the documentation](Help_FreeCAD#Work_on_the_documentation.md) page paragraph for more details on how to translate the wiki.

## Licensing, copying and reuse {#licensing_copying_and_reuse}

### Do I have to pay something to use FreeCAD? {#do_i_have_to_pay_something_to_use_freecad}

No. FreeCAD is totally free to use, to download, to redistribute, or to modify. It is [open-source software](https://en.wikipedia.org/wiki/Open_source), published under the terms of the [GNU Lesser General Public License 2.1](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), which guarantees you those freedoms and, even more important, guarantees you that these freedoms will never be taken from you.

### Can I reuse any part of the FreeCAD artwork or pieces of the website? {#can_i_reuse_any_part_of_the_freecad_artwork_or_pieces_of_the_website}

Sure. All the artwork (icons, banners, etc.) of FreeCAD are licensed LGPL, same as the FreeCAD code. Help yourself on the [Artwork](Artwork.md) page. The website is a standard MediaWiki site, all graphic elements can freely be reused, and if you are curious about how to tweak the MediaWiki software like we did, look for the special Common css and js pages.

### Can I reuse pieces of FreeCAD in another application? {#can_i_reuse_pieces_of_freecad_in_another_application}

Yes, you can use the core parts of FreeCAD in other applications as long as you comply with the terms of the LGPL. Third party libraries, [external workbenches](External_workbenches.md), and [macros](Macros.md) may be subject to their own license terms, so please consult with their authors. More details on the [Licence](Licence.md) page.







[Category:Documentation{{\#translation:}}](Category:Documentation.md)
