# Frequently asked questions/ru
На этой странице содержатся ответы на самые часто задаваемые вопросы на форуме FreeCAD. Если у вас есть проблема или вопрос, касающийся FreeCAD, попробуйте найти на него ответ на этой странице. Затем, если вы не смогли найти ответ на ваш специфический вопрос, обратитесь на [форум FreeCAD](http://forum.freecadweb.org/viewforum.php?f=3)!



## Установка



### Как проще всего установить FreeCAD в моей системе? 

Если Вы используете Windows или macOS, то самый простой способ для Вас - перейти на страницу [Загрузки](Download/ru.md), где вы найдёте несколько готовых для установки пакетов. Если Вы используете Debian, Fedora, Ubuntu или другой дистрибутив, то FreeCAD уже включён в стандартные репозитории программного обеспечения и вы можете установить его с помощью менеджера программ. На Ubuntu команда FreeCAD поддерживает собственный [PPA репозиторий](Installing_on_Linux#Stable_PPA_version.md). Дополнительные сведения об установке смотрите на странице установки для вашей операционной системы ([Windows](Installing_on_Windows/ru.md), [Linux](Installing_on_Linux/ru.md) или [Mac](Installing_on_Mac/ru.md)).



### Какие системные требования для запуска FreeCAD? 

В отличие от большинства 3D CAD программ, FreeCAD может без проблем работать на самых скромных компьютерах --- известно, что он работает на процессорах Pentium IV и Intel Core2 Solo. Если на вашем компьютере установлена современная операционная система, скорее всего, FreeCAD будет работать. Единственным условием является то, что ваша видеокарта или чипсет должны поддерживать [OpenGL](https://en.wikipedia.org/wiki/OpenGL), желательно не старше версии 2.0. В случае возникновения проблем обратитесь к разделу [Устранение проблем](Frequently_asked_questions/ru#Troubleshooting.md) FAQ.



#### Многопоточность

Базовое геометрическое ядро FreeCAD, сторонняя библиотека [OpenCASCADE Technology](http://ru.wikipedia.org/wiki/Open_Cascade_Technology) (OCCT), [в настоящее время имеет только частичную поддержку многопоточности](https://forum.freecadweb.org/viewtopic.php?f=4&t=17501&p=173095&hilit=Multithread#p173095). Подробности смотрите на странице [многопоточность](multithreading/ru.md).



### Что, если Я хочу скомпилировать FreeCAD самостоятельно? 

The source code of FreeCAD is always available in the project source code repository. Compiling FreeCAD yourself allows you to use the most recent features being developed, but requires a bit of computer knowledge, although the procedure is fairly simple. Access to the source code is explained [here](Compile_on_Linux#Getting_the_source.md), and we have detailed instructions for compiling on [Windows](Compile_on_Windows.md), [Linux](Compile_on_Linux.md) and [macOS](Compile_on_MacOS.md).



### FreeCAD сообщает, что какой-то модуль или приложение отсутствует 

FreeCAD depends on a lot of things to offer all its functionality. All the main required components are usually bundled within your FreeCAD installation or provided by your package manager, so normally you have nothing to worry about. If you installed FreeCAD from unofficial sources, however, or compiled FreeCAD yourself, some piece might be missing, which is not critical to FreeCAD itself, but might cause some functionality to be unavailable. Some specific file formats such as Collada or DWG also require extra components, which cannot be bundled into FreeCAD, and must be installed by yourself separately.

All those components and the appropriate way to install them are listed on the [Extra python modules](Extra_python_modules.md) page.



## Устранение проблем 

### Known OS-specific issues 

Find known OS-specific issues on this [forum thread](https://forum.freecad.org/viewtopic.php?t=30573)



### FreeCAD вообще не запускается 

Причин может быть много, скорее всего, отсутствует какая-то библиотека. Попробуйте запустить FreeCAD из терминала (введите {{SystemInput|freecad}} в командной строке терминала, {{SystemInput|FreeCAD}} в некоторых системах) чтобы увидеть, появляются ли какие-либо сообщения об ошибках. Кроме того, прочитайте оставшуюся часть данной странице, поскольку это может дать дополнительные сведения для обнаружения проблемы. Если ничего не помогает, расскажите об этом на [1](http://forum.freecadweb.org/forum), наверняка найдётся кто-нибудь, кто сможет вам помочь.

On some older Windows XP systems you may get an error message like this: **The application can't start, because the side-by-side configuration is wrong. The reinstallation of the application may solve the problem.** The reason for this problem is that on your system either the CRT runtime libraries are missing or the version installed is too old because FreeCAD was linked against a newer version. In this case you have to install the **Microsoft Visual C++ Redistributable Package** which you\'ll find at Microsoft. See also the corresponding [forum message](http://forum.freecadweb.org/viewtopic.php?f=3&t=1298&p=9961).



### FreeCAD запускается нормально, но не все иконки отображаются, некоторые из них заменены на черные значки \'X\' 

Некоторые части FreeCAD зависят от внешнего модуля Python называемого Pivy. В Windows pivy включена в установочный пакет FreeCAD. В системах Debian/Ubuntu пакет python-pivy входит в стандартные репозитории. В других системах в данный момент вам, возможно, придётся самостоятельно собирать pivy. Обратите внимание, что, хотя некоторые инструменты не будут работать без pivy, остальные части FreeCAD будут работать нормально.



### Проблемы с отображением, 3D-Вид работает некорректно, при его перемещении или повороте появляются артефакты и т.д. 

FreeCAD depends on OpenGL for displaying 3D contents, and therefore requires a working OpenGL environment. On some systems, OpenGL is not activated by default, and you might need to install or upgrade your graphics drivers. This problems happens most often on Linux systems or on virtual systems. If you are on a Linux-based system, try the following steps:

-   verify that your computer has a 3D-capable graphics board
-   type {{SystemInput|glxinfo}} in a terminal window, and check in the output that Direct Rendering is set to \"yes\", and that the OpenGL vendor/renderer/version matches your graphics card.
-   install other OpenGL-based software ([Blender](http://www.blender.org), for example) and check if it runs and displays correctly.



### FreeCAD вылетает при запуске 

Сбой может указывать на более серьезную ошибку или проблему в вашей конфигурации. Большинство сбоев при запуске происходит по одной из двух следующих причин:



#### OpenGL драйвер не установлен или работает не правильно 

Это очень частая причина проблемы. Её симптомы - сбой FreeCAD при запуске, или всякий раз, когда Вы открываете 3D вид (например, при создании нового документа). Постарайтесь выяснить, какой у вас графический чип, затем выясните, поддерживает ли он [OpenGL](http://ru.wikipedia.org/wiki/OpenGL) (самые послежние - поддерживают), затем найдите правильный драйвер и установите его. Хороший способ проверить, работает ли OpenGL - попытаться запустить другое приложение, его использующее, например [blender](http://www.blender.org).

And as a general tip to get some more information about crashes with FreeCAD you can start it with the program parameter {{SystemInput|--write-log}}. This will create the file **FreeCAD.log** in **$XDG_CONFIG_HOME/FreeCAD** (<small>(v0.20)</small> ) or **$HOME/.FreeCAD** ({{VersionMinus|0.19}}) on Linux, or **$HOME/Library/Preferences/FreeCAD** on macOS, or **%APPDATA%/FreeCAD** on Windows systems.

In some rare cases you may have a graphic driver installed that doesn\'t fit to your graphic card. We had a case where the user\'s laptop had an Intel on-board graphic but some ATI drivers were installed. Refer to forum thread in German [FreeCAD startet nicht](http://forum.freecadweb.org/viewtopic.php?f=13&t=5160&start=10#p41042). After removing the files and re-installing the correct driver FreeCAD started to work.



#### Библиотека, нужная для работы FreeCAD, отсутствует в системе или не найдена 

Эта проблема может иметь две причины: либо какая-то библиотека просто отсутствует, поэтому FreeCAD не запускается, либо библиотека есть, но более старая версия, чем требуется для FreeCAD, поэтому при попытке запустить FreeCAD происходит сбой, т. к. FreeCAD пытается использовать функцию из этой библиотеки, которой в ней нет. Типичный пример: когда в вашей системе установлены Qt3 и Qt4, FreeCAD может обнаружить Qt4, но, если Qt не настроенна должным образом, некоторые части Qt3 всё ещё могут использоваться, вызывая сбои.

Please review the installing procedure ([Windows](Installing_on_Windows.md), [Linux](Installing_on_Linux.md) or [Mac](Installing_on_Mac.md)), make sure you installed all the required libraries (on most linux systems this is done automatically), and check what is the minimum version number for each of the components.

If everything seems correct, describe the problem on the [forum](http://forum.freecadweb.org/) or [submit a bug](Tracker.md). If you are on a linux system, it is easy to do a debug backtrace, which provides very useful information about the crash to the developers:

-   in a terminal, type: {{SystemInput|gdb freecad}} (assuming package gdb is installed)
-   inside gdb, type {{SystemInput|run}}
-   after the crash, type {{SystemInput|bt}} to get the backtrace, that you can include in your bug report.



### FreeCAD зависает после запуска 

При запуске FreeCAD графический интерфейс появляется почти моментально, но он зависает и загрузка процессора составляет около 99%. Такая ситуация может произойти на рабочем столе KDE при использовании темы Oxygen. Причиной является ошибка в теме Oxygen, выбор другой темы должен решить эту проблему.

### FreeCAD crashes on creating a new document or opening a file 

If FreeCAD crashes when it creates a new 3D view, try launching FreeCAD from a terminal. If a message error appears when the crash occurs, mentioning {{SystemOutput|Assertion Failed}}, and a component name beginning with \"So\" ({{SystemOutput|SoBase}}, {{SystemOutput|SoFieldContainer}}, etc.), the chances are very high, especially if you are on Linux, that FreeCAD is trying to use two different versions of the Coin library, which causes the crash. To verify if that is indeed the problem, try the following:

-   Locate the FreeCAD executable (usually in **/usr/lib/FreeCAD/bin**)
-   Run the command {{SystemInput|ldd FreeCAD}} from a terminal
-   Note down the version of the **libCoin.so** library that FreeCAD is using (for example **libCoin.so.60**)
-   Locate the **libSoQt.so** library (usually in **/usr/lib**)
-   run {{SystemInput|ldd libSoQt.so}} and check if it links to the same Coin version as FreeCAD

If there is any difference, either FreeCAD or SoQt must be recompiled (better to recompile the one that uses the oldest Coin version). The normal behavior is to try to contact the people responsible for packaging either SoQt or FreeCAD and kindly ask them to consider recompiling. If you want to undertake that step for yourself, and it is not possible to recompile SoQt because it breaks other applications on your system, you can force FreeCAD to compile with the required Coin version with {{SystemInput|<nowiki>./configure --with-coin=DIR</nowiki>}}. But you have to make sure that the correct development package of this Coin version is installed.



### FreeCAD вылетает после команды Правка → Выравнивание 

Ошибка сегментации происходит в {{SystemOutput|vbo_save_playback_vertex_list()}}. Это означает, что в графическом драйвере плохая реализация VBO. Чтобы избежать кэширования вызовов OpenGL, вы можете попытаться установить переменную среды {{SystemInput | <nowiki> IV_SEPARATOR_MAX_CACHES = 0 </nowiki>}} и перезапустить FreeCAD.

### I cannot change numeric values in FreeCAD\'s properties panels 

<img alt="language options" src=images/Jj62l.png  style="width:480px;">

You most likely have bad windows regional settings set-up. Please check if you have the same symbol for decimal separator and digit grouping symbol in your regional settings. If you do, [adapt your system settings](http://forum.freecadweb.org/viewtopic.php?f=4&t=2655&p=20046#p20041) to use different characters for the digit grouping symbol and decimal separator. Note that it is not mandatory to have dot as decimal separator. It is mandatory to use different symbols in these two settings. 



### FreeCAD работал нормально, но вдруг перестал запускаться 

Данная ситуация может произойти, если у вас была установлена более старая версия FreeCAD, и вы обновили её до более новой версии. В процессе обновления файлы конфигурации FreeCAD могли быть по какой-то причине повреждены, и теперь FreeCAD больше не может их читать и не запускается. Решение состоит в том, чтобы просто удалить эти файлы конфигурации, чтобы FreeCAD заново их воссоздал при первом запуске.

-   On Windows: Open the file explorer, and write **%APPDATA%\FreeCAD** as the file path. Once there, delete the files **user.cfg** and **system.cfg**
-   On Linux: Navigate to **/home/USERNAME/.local/share/FreeCAD** (<small>(v0.20)</small> ) or **/home/USERNAME/.FreeCAD** ({{VersionMinus|0.19}}) and delete the files **user.cfg** and **system.cfg**
-   On Mac: Navigate to **/Users/USERNAME/Library/Preferences/FreeCAD** and delete the files **user.cfg** and **system.cfg**

Теперь FreeCAD должен нормально запуститься со сбросом всех настроек.

There is a [Macro findConfigFiles](Macro_findConfigFiles.md) available to help in locating your configuration files. It can be installed using the Addon Manager in the Tools menu. **Tools → Addon Manager → Macros → findConfigFiles**. The macro will find your config file folder, copy it to the clipboard, and (attempt to) open that location with your default file browser. It makes no changes to your files or settings.



## Использование FreeCAD 



### FreeCAD действительно бесплатный? Даже для коммерческого использования? 


<div class="mw-translate-fuzzy">

FreeCAD это [программное обеспечение с открытым исходным кодом](http://ru.wikipedia.org/wiki/Open-source_software), и Вы можете его бесплатно использовать не только для себя или в коммерческих целях, но, также, можете распространять, модифицировать и использовать в приложениях с закрытым исходным кодом. В общем, Вы можете делать с ним (почти) всё, что захотите. См. страницу [Лицензия](License/ru.md) для получения более подробной информации.


</div>



### Как я могу повернуть 3D вид? 


<center>

Image:Style_of_navigation.png\|От **правой кнопки** мыши Image:Style of navigation menu.png\|Из меню **Правка → Настройки →**


</center>




FreeCAD has several different [navigation modes](Mouse_navigation.md) available, that can be set in the preferences settings dialog or changed by right-clicking in the 3D view. For full details about the modes, see the [Mouse navigation](Mouse_navigation.md) page.

### What can I do with FreeCAD? Where do I start? 

Head to the [Getting started](Getting_started.md) page for a quick description of the tools you can use. There is also a new [Tutorials](Tutorials.md) section containing a few resources. The [User hub](User_hub.md) section contains more detailed information about the different workbenches of FreeCAD. Note that since FreeCAD is relatively new, its user interface is still very bare and doesn\'t feature many tools. But much more advanced functionality is already available to you from [Python scripting](Power_users_hub.md).

### Is there documentation for newcomers? How can I learn to use FreeCAD? 

There is a lot of documentation spread in different places, both on and outside the FreeCAD website. You might want to start with the [Getting started](Getting_started.md) page. The [Tutorials](Tutorials.md) section contains many specialized tutorial pages to help you getting started with the different workbenches. The [Manual:Introduction](Manual_Introduction.md) is a general, complete user-oriented guide to FreeCAD. The [User hub](User_hub.md) section of this wiki lists all pages aimed at end users. On external sites like [Youtube](https://www.youtube.com/results?search_query=freecad), you will also find a load of video tutorials created by users. And, last but not least, the [forum](https://forum.freecadweb.org) contains a lot of replies to questions asked by other newcomers.

### I want to import/export data in format XYZ to/from FreeCAD. How do I do that? 

Please refer to the [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md) page. Maybe your questions are already answered there.



### Где можно найти варианты решений для недостающих возможностей FreeCAD? 

Обратитесь к странице [обходные пути для решения некоторых задач](Workarounds/ru.md).



## Работа с геометрией Детали 

### How do I extrude stuff into solids? I don\'t get the right result 

The theory is simple: Lines (or wires), when extruded, form faces. Faces, when extruded, form solids.

If you extrude something and the result is not a solid, then the something was not a face. If you have lines and you want to extrude a solid from them, you must first select lines that form a closed perimeter (select several objects by pressing **Ctrl**), join them into a wire ([Draft Upgrade](Draft_Upgrade.md) tool), then make a face from that wire (<img alt="" src=images/Draft_Upgrade.svg  style="width:16px;"> [Draft Upgrade](Draft_Upgrade.md) tool again). There you are, if all went well you can now extrude it to a solid.

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

### My boolean operations fail, or give weird results 

Like all solid modeling kernels, the [Open CASCADE](https://en.wikipedia.org/wiki/Open_CASCADE_Technology) geometric modeling kernel used in FreeCAD for Part geometry, although probably the best open-source geometry kernel available, has flaws and limitations. Boolean operations (fusion, subtraction, intersection) are complicated operations, and often give strange results. This is a current limitation we have no way to solve at once, so your best path is to try obtaining the desired result by modeling another way. For example, problems with primitives such as cylinder can often be solved by using an extruded circle instead. Coplanar surfaces between parts can cause trouble, as well as surface tangency. As a general rule, if a shape doesn\'t work, try remodeling it a different way. In 99% of the cases at the end you will manage to obtain the result you want.

To understand boolean operations better, see these articles:

-   <https://wiki.mcneel.com/rhino/booleanfaq>
-   <https://dev.opencascade.org/doc/overview/html/specification__boolean_operations.html#autotoc_md293>

### When I export (or view) my model, the holes are filled in 

Don\'t use **Ctrl** + **A** (Select All) to export everything from the hierarchy tree. If the model is of one single item, try selecting only the newest item (usually the last one) in the hierarchy tree.

As we create a model in the [PartDesign Workbench](PartDesign_Workbench.md), each feature takes the shape of the last one and adds or removes something, creating linear dependencies from feature to feature as the model is created. Hence a \"Cut\" feature is not only the cut hole itself, but the whole part with the cut. This is why the user usually should only have the newest item (feature) in the model tree visible, because otherwise the phases of the model overlay each other, and holes are filled in by the earlier model features.

To toggle visibility of an object on or off, select it in the hierarchy tree and press **spacebar** on your keyboard. Usually everything but the last item in the hierarchy tree should be greyed out and therefore not visible in the [3D view](3D_view.md).



### Параметрические объекты ломаются, после изменения их базовых эскизов 

Вы столкнулись с проблемой именования геометрических объектов. В настоящее время это основная проблема FreeCAD для начинающих пользователей. Она присутствует во всем FreeCAD, но наиболее заметна при использовании [эскизов](Sketcher_Workbench/ru.md). Объяснение простое: при перерасчете эскиза геометрические объекты (ребра, грани\...) перестраиваются в другом порядке, в зависимости от порядка существующих в нем ограничений (constraints). Они заново получают имена (Edge1, Edge2\... Face1, Face2\... и т.д.). Большинство последующих операций (выдавливание, скругление и т.д.) привязаны к старым именам. Т.е. при перестроении эскиза операции будут обращаться к именам которые были заложены в них изначально, а не к тем, что были получены заново уже после редактирования, что соответственно приведет к неправильному результату.

This is a very hard problem to overcome (the [Topological Naming Project](Topological_Naming_Project.md) aims at solving it). However, there are many workarounds available to mitigate the problem, and more advanced users generally manage to avoid it completely. A couple of strategies are:

-   Know that sketches are highly sensitive to the problem. Referencing a specific edge of a sketch, or a face of an object built on a sketch, such as a [PartDesign Pad](PartDesign_Pad.md), is dangerous, unless you are pretty confident that these sketches will not change over time or the sketch is very simple. A Pad built on a simple rectangular sketch, for example, will likely be safe as it will generate only one face, so there is no order problem.
-   Prefer other kinds of objects such as [Part](Part_Workbench.md) or [Draft](Draft_Workbench.md) when possible. These objects are always built the same way, and therefore their geometric components usually follow the same order each time they are rebuilt. They are much less susceptible to toponaming problems.
-   To attach further objects onto the faces of sketch-based geometry, prefer using [Datum geometry](PartDesign_Plane.md). These invisible \"helper objects\" don\'t depend on sketch geometry, and therefore stay stable over time.



## Как внести свой вклад в развитие FreeCAD 



### Чем можно помочь для развития FreeCAD? 

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



### Как получить доступ к редактированию вики? 

See the [Work on the documentation](Help_FreeCAD#Work_on_the_documentation.md) page paragraph for more details on how to contribute.

### Does FreeCAD participate in Google Summer of Code? 

Yes. Beginning in 2016, FreeCAD participates in Google Summer of Code. See [Google Summer of Code 2020](Google_Summer_of_Code_2020.md) for information on past editions, and [Google Summer Of Code 2016](http://forum.freecadweb.org/viewtopic.php?f=8&t=13838) in the forum for the original announcement.

### I want to start translating the wiki in my own language. What do I do? 

This wiki is hosting a lot of contents. The most up-to-date and interesting material is gathered in the [manual](Online_Help_Toc.md).

See the [Translate the documentation](Help_FreeCAD#Work_on_the_documentation.md) page paragraph for more details on how to translate the wiki.



### Можно ли приобрести мерч? 

FreeCAD не предлагает \"фирменные\" сувениры собственного производства, которые вы можете заказать для поддержки проекта. Но вы можете их создать самостоятельно. Инструкции см. на нашей странице [Сувениры](Swag/ru.md).



## Лицензирование, авторские права и использование 

### Do I have to pay something to use FreeCAD? 

No. FreeCAD is totally free to use, to download, to redistribute, or to modify. It is [open-source software](https://en.wikipedia.org/wiki/Open_source), published under the terms of the [GNU Lesser General Public License 2.1](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), which guarantees you those freedoms and, even more important, guarantees you that these freedoms will never be taken from you.

### Can I reuse any part of the FreeCAD artwork or pieces of the website? 

Sure. All the artwork (icons, banners, etc.) of FreeCAD are licensed LGPL, same as the FreeCAD code. Help yourself on the [Artwork](Artwork.md) page. The website is a standard MediaWiki site, all graphic elements can freely be reused, and if you are curious about how to tweak the MediaWiki software like we did, look for the special Common css and js pages.

### Can I reuse pieces of FreeCAD in another application? 

Yes, you can use the core parts of FreeCAD in other applications as long as you comply with the terms of the LGPL. Third party libraries, [external workbenches](External_workbenches.md), and [macros](Macros.md) may be subject to their own license terms, so please consult with their authors. More details on the [License](License.md) page.



---
⏵ [documentation index](../README.md) > [Documentation](Category_Documentation.md) > Frequently asked questions/ru
