# Getting started/bg







{{TOCright}}

## Увод


<div class="mw-translate-fuzzy">

FreeCAD е 3D CAD/CAE [програма за параметрично моделиране](About_FreeCAD/bg.md). Основно е предназначена за механичен дизайн но има приложение и във всички други области изискващи точно моделиране на 3D обекти.


</div>


<div class="mw-translate-fuzzy">

FreeCAD е все още в ранен стадии на своето развитие. Макар и вече да предоставя много [възможности](Feature_list/bg.md), все още много елементи липсват, особенно в сравнение с някои платени продукти. Може все още да не е достатъчно развита за използване в продукция. FreeCAD има бързо растящо [общество](http://forum.freecadweb.org/index.php) of потребители и вече може да намерите [много примери](https://forum.freecadweb.org/viewforum.php?f=24) на качествени проекти разработени с FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Както всички проекти с отворен код, FreeCAD не е просто едноседмичен проект доставен веднъж от неговите автори. Програмата разчита на активното общество от потребители и програмисти за да расте, добавя нови възможности и да се стабилизира (тоест да се оправят бъгове). Моля не забравяйте че след като започнете да използвате FreeCAD, ако го харесвате, може директно да [участвате](Help_FreeCAD/bg.md) в неговото развитие.


</div>

See also:

-   [Migrating to FreeCAD from Fusion360](Migrating_to_FreeCAD_from_Fusion360.md)
-   [Tutorials](Tutorials.md)
-   [Video tutorials](Video_tutorials.md)

## Инсталация


<div class="mw-translate-fuzzy">

Първо (ако все още не сте го направили) свалете и инсталирайте FreeCAD. Вижте страницата [Download](Download/bg.md) за линкове за сваляне на последната версия, и страницата [Инсталация](Installing/bg.md) за информация как да инсталирате FreeCAD. Има готови инсталатори заWindows (.msi), Ubuntu и Debian (.deb) openSUSE (.rpm) и Mac OSX. Тъй като FreeCAD е с отворен код, ако сте готови за приключение, може да видите (и работите върху) най-новите разработки в прогрмата като свалите сорс кода и сами [компилирате](Compiling/bg.md) FreeCAD.


</div>


<div class="mw-translate-fuzzy">

## Да Опознаем FreeCAD 


</div>

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_interface.png  style="width:1024px;">


</div>


<div class="mw-translate-fuzzy">

1.  Прозореца 3D показва обекта върху които работите
2.  Прозореца \"tree view\" (дърво на обектите), показва йерархията и историята на конструиране на всички обекти в документа
3.  Прозореца [properties editor](property_editor/bg.md), видите и промените свойствата на избраните в момента обекти
4.  В прозореца report (също наричан output window), which is where FreeCAD принтира съобщения и грешки
5.  В Конзолата на python се принтират всички python команди които се изпълняват от FreeCAD. Там също може да въведете и свой python код.
6.  Полето [workbench selector](Workbenches/bg.md), ви позволява да смените активния работен плот


</div>


<div class="mw-translate-fuzzy">

Основната концепция в интерфейса на FreeCAD е разделението на различни [работни плотове](workbenches/bg.md). Един Работен Плот е сбор от определни инструменти и туул-барове които ви позволяват да изпълните определна задача. Например работния плот [meshes](Mesh_Workbench/bg.md) ви позволява да работите с меш-ове. Има работен плот за [2D обекти](Draft_Workbench/bg.md), за [скици чрез ограничения](Sketcher_Workbench/bg.md) и т.н. Може да сменяте настоящия работен плот с полето workbench selector (6). Може да [променяте](Interface_Customization/bg.md) инструментите показани във всеки плот, да добавяте инструменти от други плотове, и дори да добавяте инструменти които сами сте създали (например [макроси](macros/bg.md)). Има и \"пълен работен плот\" в който са събрани наи-често използваните инструменти от други работни плотове.


</div>


<div class="mw-translate-fuzzy">

Когато отворите FreeCAD за първи път, ше видите \"началния център\" (start center):


</div>

<img alt="" src=images/Start_center_0.18_screenshot.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Startcenter.jpg  style="width:1024px;">


</div>


<div class="mw-translate-fuzzy">

\"Началния Център\" ви позволява бързо да превключите в някой от наи-често използваните работни плотове, да отворите наскоро ползвани файлове, и да видите последните новини в света на FreeCAD. Може да смените работния плот който да се показва по подразбиране (вместо \"началния център) в менюто [preferences](Preferences_Editor/bg.md).


</div>

## Навигация в тримерното пространство 


<div class="mw-translate-fuzzy">

FreeCAD има няколко различни режима за [навигация с мишка](Mouse_Model/bg.md) който променят ефекта на мишката и върху обектите и върхи ориентацията в порстранството. Един от тези режими е специално направен за [работа с тъч-падове (на лаптопи)](Mouse_Model/bg#Touchpad_Navigation.md), където няма среден бутон на мишката.Следната талица описва режима по подразбиране **CAD Navigation** (може да смените сегашния режим на навигация с мишката като натиснете с десния бутон върху празно място в 3D прозореца):


</div>


<div class="mw-translate-fuzzy">


{{CAD Navigation/bg}}


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

The cursor location when the middle mouse button is pressed determines the center of rotation. Rotation works like spinning a ball which rotates around its center. If the buttons are released before you stop the mouse motion, the view continues [[spinning]], if this is enabled.

A double click with the middle mouse button sets a new center of rotation.
|Rotate_view_mode_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Rotate_view_alt_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

With this method the middle mouse button may be released after the right mouse button is held pressed.

Users who use the mouse with their right hand may find this method easier than the first method.
}}


</div>

Holding down **Ctrl** allows the selection of multiple objects. \|Pan\_text=Hold the middle mouse button, then move the pointer. \|Pan\_mode\_text=Pan mode: hold the **Ctrl** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small>  \|Zoom\_text=Use the mouse wheel to zoom in and out.

Clicking the middle mouse button re-centers the view on the location of the cursor. \|Zoom\_mode\_text=Zoom mode: hold the **Ctrl** and **Shift** keys, press the right mouse button once, then move the pointer. <small>(v0.17)</small>  \|Rotate\_view\_text=Hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

The cursor location when the middle mouse button is pressed determines the center of rotation. Rotation works like spinning a ball which rotates around its center. If the buttons are released before you stop the mouse motion, the view continues [spinning](spinning.md), if this is enabled.

A double click with the middle mouse button sets a new center of rotation. \|Rotate\_view\_mode\_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small>  \|Rotate\_view\_alt\_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

With this method the middle mouse button may be released after the right mouse button is held pressed.

Users who use the mouse with their right hand may find this method easier than the first method. }}


<div class="mw-translate-fuzzy">

Имате няколко предифинирани погледа върху обектите (отгоре(top view), отпред(front view), и т.н) в менюто View и във View туулбарът (бутоните с кубовете с една попълнена стена). Може да изберете поглед върху обектите и с клавиатурни комбинации (**1**, **2**, etc\...). Също ако натиснете десния бутон на мишката върху обект или празно пространство ще имате избор на изглед или възможност да намерите на обект в дървото на обектите (Tree view).


</div>

## Първи стъпки с FreeCAD 


<div class="mw-translate-fuzzy">

Силата на FreeCAD\'s е в точното моделиране на 3D обекти, точния контрол върху обектите (тоест възможността да се връщаме назад в историята от промените в модела, и да променяме всяко свойство на обектите), и в интеграцията с 3D принтери и CNC стругове позволяващо лесно автоматично построяване. Поради този си фокус FreeCAD е различен от други програми за 3D моделиране като например програми за създаване на анимационни филми (Blender, 3dmax, Maya). Първоначално научаването на програмата може да е трудно, особенно ако за първи път се захващате с 3D моделиране. Ако сте заседнали някъде, може да се обърнете към общността от потребители на [форумът на FreeCAD](http://forum.freecadweb.org/index.php).


</div>


<div class="mw-translate-fuzzy">

Работния плот който ще използвате зависи от работата която искате да свършите: например за механически модели (или общо казано по-малки обекти), вероятно искате да използвате [Плотът за дезайн на части](PartDesign_Workbench/bg.md). Ако ще работите само в двумерно пространство, тогава използвайте [Draft Плотът](Draft_Workbench/bg.md). За скици с ограничения използвайте [Плотът за скициране](Sketcher_Workbench/bg.md). Ако искате да правите БИМ, пуснете [Плотът за архитектура](Arch_Workbench/bg.md). Ако искате да моелирате кораби, има специален [работен плот за тази цел](Ship_Workbench/bg.md). Ако искате да работите със [OpenSCAD](https://en.wikipedia.org/wiki/OpenSCAD.md) използвайте [работния плот за OpenSCAD](OpenSCAD_Workbench/bg.md).


</div>


<div class="mw-translate-fuzzy">

Може да сменяте работните плотове по всяко време, и да [променяте](Interface_Customization/bg.md) интерфейса на всеки работен плот, както и да добавяте нови инструменти във всеки плот.


</div>

## Работа с работните пловоте за дезайн на елементи и скициране 


<div class="mw-translate-fuzzy">

Работния плот за [дезайн на елементи](PartDesign_Workbench/bg.md) е създаден специално за построяването на сложни обекти от прости форми (цилиндри, паралелепипети и т.н.). Обекта се построява като се добавят или изваждат части (наричаме ги \"фийчъри\" (features)) докато не получим това което искаме. Всички елементи (фийчъри) които използваме за да построим обекта можем да намерим в прозореца [tree view](Document_structure/bg.md) организирани като дърво. В този прозорец се намират и всички други обекти в нашия документ. Може да мислите за обекта моделиран по този начин като редица операции, всяка приложена към резултата от предишната. В прозореца tree view виждате финалния обект организиран като дърво където последната операция е в корена, а предишните операции са деца на корена. Можете да отворите всяко под-дърво на финалния обект, за да видите по-ранни версии на обекта (или казано по друг начин - подобектите от които той е съставен). Може да променяте параметрите на всеки под-обект, и това автоматично ще се отрази на целия обект.


</div>


<div class="mw-translate-fuzzy">

Работния плот за дезайн на елемент често използва и друг работен плот - [плотът за скициране с ограничения](Sketcher_Workbench/bg.md). Плотът за скициране с ограничения позволява да чертаете двумерни фигури, които се дефинират като се приложи ограничение върху проста(и) 2D форма(и). Например, можете да нарисувате правоугулник, и можете да определите дължината на страната му като приложите ограничението за дължина върху тази страна. След като сложите това ограничение, тази страна на правоъгълника не може повече да се променя, докото не промените или махнете ограничението което сте добавили.


</div>

2D формите нарисувани в плота за скициране с ограничения се използват често в плота за дизайн на елементи. Например, за да създадете 3D обем, или за да изрежете дупка в страната на 3D обекта върху които работите. Ето типичния работен процес за дизайн на елемент:

1.  Отваряте двумерна скица (тоест влизате в работния плот за скициране с ограничения)
2.  В двумерната скица създавате затворена двумерна форма
3.  Затваряте двумерната скица (тоест връщате се в работния плот за дизайн на елемент)
4.  Издигате скицата в плътен 3D обект използвайки инструмента pad
5.  Избирате едно от лицата на новопостроения 3D обект
6.  Създавате нова скица (този път върху избраното лице)
7.  Чертаете нова 2D затворена фигура
8.  Затваряте скицата
9.  Създавате дупка (pocket) във обекта, със формата на втората скица

Би трябвало да получите обект подобен на този:

<img alt="" src=images/Partdesign_example.jpg  style="width:1024px;">

Във всеки един момент може да изберете и промените оригиналната скица, или височината на издигнатия елемент(pad extrusion parameters), или дълбочината на дупката която сте създали. Вашите промени веднага ще бъдат отразени върху крайния обект.

## Работния плот Draft и Архитектурния работен плот(Arch) 


<div class="mw-translate-fuzzy">

Работните плотове [Draft](Draft_Workbench/bg.md) и [Архитектура](Arch_Workbench/bg.md) са по-различни от гореописаните работни плотове, макар и да следват някои от същите общи правила. На кратко, докато Плотовете за Скициране с Ограничения, и за дизайн на елементи да са основно за работа върху един елемент, плотовете Draft и Архитектура се използват за работа с няколко по-малки обекти.


</div>


<div class="mw-translate-fuzzy">

Плотът [Draft](Draft_Workbench/bg.md) предлага 2D инструменти подобни на по-традиционните 2D програми като [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD). Тъй като стандартното 2D чертане не е основния фокус на FreeCAD, в него няма да намерите всички инструменти които има в програми специално за тази цел (като AutoCAD). Повечето инструменти в плота Draft работят не само в 2D равнини но и в 3D пространството и могат да бъдат интегрирани със помощни системи като [Work planes](Draft_SelectPlane/bg.md) и [object snapping](Draft_Snap/bg.md).


</div>


<div class="mw-translate-fuzzy">

[Архитектурния работен плот](Arch_Workbench/bg.md) добавя [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) инструменти към FreeCAD, които ви разрешават да създавате архитектурни модели с параметрични обекти. Архитектурния плит изпозва плотове като Draft и Скициране с ограничения. Всички инструменти от Draft плота например са достъпни и в Архиткетурния плот. Повечето инструменти в Архитектурния полт използват части от Draft модула за своята работа.


</div>

Ето пример за типичен работен процес в Архитектурния/Draft работни плотове:

1.  Начертайте няколко линии с инструмента Draft Line
2.  Изберете всяка линия и натиснете върху инструмента Wall за да построите стена върху всяка от тях
3.  Съединете стените като ги изберете и натиснтете инструмента Arch Add
4.  Създайте подов обект (floor object) и преместете стените във него във прозореца Tree view
5.  Съзадайте обект \"сграда\" (building object) и преместете подовия обект в него във прозореца Tree view
6.  Създайте прозорец като натистнете върху инструмента Window tool, изберете запеметен тип на прозорец, и натиснете върху лицето на стена в която да се постави прозореца
7.  Изберете измерения като първи изберете работната равнина (ако е нужно) и след това използвате инструмента Draft Dimension

Би трябвало да получите нещо подобно на следния обект:

<img alt="" src=images/Arch_workflow_example.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

За повече информация вижте страницата [Tutorials/bg](Tutorials/bg.md).


</div>


<div class="mw-translate-fuzzy">

## Скриптиране


</div>

Freecad, as an open source software, offers the possibility to supplement its workbenches with addons.

The [Addon](Addon.md) principle is based on the development of a workbench complement. Any user can develop a function that he or she deems to be missing for her/his own needs or, ultimately, for the community. With the forum, the user can request an opinion, help on the forum. It can share, or not, the object of its development according to copyright rules to define. Free to her/him. To develop, the user has available [scripting](scripting.md) functions.

There are two types of addons:

1.  [Macros](Macros.md): short snippets of Python code that provide a new tool or functionality. Macros usually start as a way to simplify or automate the task of drawing or editing a particular object. If many of these macros are collected inside a directory, the entire directory may be distributed as a new workbench.
2.  [External workbenches](External_workbenches.md): collections of tools programmed in Python or C++ that extend FreeCAD in an important way. If a workbench is sufficiently developed and is well documented, it may be included as one of the base workbenches in FreeCAD. Under [External workbenches](External_workbenches.md), you\'ll find the principle and a list of existing library.

## Scripting


<div class="mw-translate-fuzzy">

Накрая, една от най-гъвкавите способности на FreeCAD е неговата среда за [скриптиране](scripting/bg.md). От вградената конзола за python (или от външен Python скрипт), вие имате достъп до почти всяка част на FreeCAD. Може да създавате или модифицирате геометрични обекти, как тази обекти се представят в 3D сцена или дори да използвате и променяте интерфейса на FreeCAD. Python скриптове се използват иза писането на [макроси](macros/bg.md), които дават лесен начин за писане на нови команди и инструменти.


</div>


<div class="mw-translate-fuzzy">

## Какво Ново 


</div>


<div class="mw-translate-fuzzy">

-   [Version 0.17 Release notes](Release_notes_0.17.md) : Вижте какво ново в версия 0.17 на FreeCAD
-   [Version 0.16 Release notes](Release_notes_0.16.md) : Вижте какво ново в версия 0.16 на FreeCAD
-   [Version 0.15 Release notes](Release_notes_0.15.md) : Вижте какво ново в версия 0.15 на FreeCAD
-   [Version 0.14 Release notes](Release_notes_0.14.md) : Вижте какво ново в версия 0.14 на FreeCAD
-   [Version 0.13 Release notes](Release_notes_0.13.md) : Вижте какво ново в версия 0.13 на FreeCAD
-   [Version 0.12 Release notes](Release_notes_0.12.md) : Вижте какво ново в версия 0.12 на FreeCAD
-   [Version 0.11 Release notes](Release_notes_0.11.md) : Вижте какво ново в версия 0.11 на FreeCAD


</div>


<div class="mw-translate-fuzzy">


{{docnav|Install on Mac/bg|Mouse Model/bg}}


</div>




[Category:User Documentation/bg](Category:User_Documentation/bg.md)
