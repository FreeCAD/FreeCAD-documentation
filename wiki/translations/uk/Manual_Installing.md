# Manual:Installing/uk
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

FreeCAD поширюється за ліцензією [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License). Ви можете завантажувати, встановлювати, поширювати та використовувати FreeCAD будь-яким способом, незалежно від виконуваної із ним роботи (коммерційної або некоммерційної). Ви не пов\'язані ніякими обмеженнями і всі файли, які Ви зробили за допомогою FreeCAD, належать виключно Вам. Одна річ, яку забороняє Вам ліцензія, це стверджувати, що Ви самі написали FreeCAD!


</div>

FreeCAD працює однаково як на Windows, так і на Mac OS та Linux. Але метод встановлення відрізняється у залежності від Вашої платформи. На Windows та Mac спільнота FreeCAD забезпечує прекомпільовані пакети (завантажувачі), готові до завантаження, в той час як на Linux розробникам дістрибутивів надається вихідний код, і вже вони відповідають за складання пакетів для їх дістрибутива. У результаті Ви як правило маєте можливість встановити FreeCAD з програмного менеджера пакетів.

Офіційна сторінка завантаження FreeCAD для Windows та Mac OS знаходиться за адресою: <https://github.com/FreeCAD/FreeCAD/releases>

**Версії FreeCAD**

Офіційні випуски FreeCAD, які Ви маєте можливість знайти на сторінці вказаній зверху і у менеджері пакетів Вашого дістрибутива, це стабільні версії. Тим не менш, FreeCAD разробляється швидко! Нові можливості та виправлення помилок додаються майже кожен день. Оскільки часом треба багато часу до стабільного випуску, Вас може зацікавити остання версія FreeCAD. Ці версії для розробників, або пре-релізы, завантажуються час від часу на вишевказану сторінку завантаження [download page](https://github.com/FreeCAD/FreeCAD/releases) або, якщо Ви використовуєте Ubuntu чи Fedora, спільнота FreeCAD також підтримує \"збірки кожного дня\" [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) та [1](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/copr), які регулярно змінюються найновішими зміненнями.

Якщо ж Ви встановили FreeCAD на віртуальну машину - враховуйте погану швидкість роботи (або навіть непрацездатність у деяких випадках) через обмеження підтримки [OpenGL](https://ru.wikipedia.org/wiki/OpenGL) на більшості віртуальних машин.



### Встановлення на Windows 

1.  Встановіть пакет завантажувача(.exe), який підходить до вашої версії Windows (32bit або 64bit) звідси:[download page](https://github.com/FreeCAD/FreeCAD/releases). Завантажувач FreeCAD працює на будь-якій версії, починая з Windows 7.
2.  Два рази натисніть на встановлений завантажувач.
3.  Прийміть вимоги ліцензії LGPL. Це один з тих випадків, коли Ви дійсно можете без страху нажати кнопку \"accept\" без читання тексту. Ніяких схованих тверджень: ![](images/Freecad-windows-install-01.jpg )
4.  Можна залишити путь за замовчуванням, або змінити за бажанням: ![ничего](images/Freecad-windows-install-02.jpg )
5.  Переменную PYTHONPATH устанавливать не требуется, если Вы не планируете сложного программирования на python, в в таком случае Вы, вероятно, уже знаете, для чего это: ![](images/Freecad-windows-install-03.jpg )
6.  Під час встановлення деякі додаткові компоненти, включені до пакету, будуть також встановлені: ![](images/Freecad-windows-install-04.jpg )
7.  Усе, FreeCAD встановлено. Ви можете знайти його у стартовому меню. ![](images/Freecad-windows-install-05.jpg )

**Завантаження версії для розробника**

Пакування FreeCAD та створення завантажувача потребує деякого часу та уваги, через що версії разробника (так звані pre-release) надаються як архіви .zip (або .7z). Їм не потрібне встановлення, просто розпакуйте їх та запустіть FreeCAD подвійним натисканням на файлі FreeCAD.exe, який знаходиться всередині. Це також надасть можливість Вам мати одночасно \"стабільну\" та \"нестабільну\" версію на одному компьютері.



### Встановлення на Linux 

На більшості сучасних дистрибутивів Linux (Ubuntu, Fedora, OpenSUSE, Debian, Mint, Elementary і т.д.) FreeCAD може бути встановлено у декілька кліків, прямо із застосунку керування програмами дистрибутиву (його вид може не бути схожий на зображення знизу, так як кожен дистрибутив використовує власні інструменти).

1.  Відкрийте менеджер застосунків та знайдіть \"Freecad\":
    <img alt="" src=images/Freecad-linux-install-01.jpg  style="width:800px;">
2.  Натисніть позначку \"install\". Готово, FreeCAD встановлено. Не забудьте потім виставити йому рейтинг!
    <img alt="" src=images/Freecad-linux-install-02.jpg  style="width:800px;">

**Альтернативні методи**

Одні з головних радощів використання Linux - це різноманіття можливостей для налаштування своїх програм, тому не обмежуйте себя. В Ubuntu та його похідних FreeCAD також може бути встановлено з цього сайту: [PPA](https://launchpad.net/~freecad-maintainers), який підтримується співтовариством FreeCAD (сайт містить як стабільну, так і нестабільну версію). У Fedora останні версії FreeCAD, які розробляються, можуть бути встановлені звідси: [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/). А виходячі з того, що ці програми надаються з доступним вихідним кодом, Ви також можете легко [скомпілювати FreeCAD самостійно](Compiling/ru.md).



### Встановлення на Mac OS X 

Завантаження FreeCAD на Mac OS X це тепер така ж легка справа, як і встановлення програми на інші платформи. Тим не менш, зважаючи на те, що у співтоваристві розробників FreeCAD мало людей мають Mac - доступні пакети часто затримуються на декілька версій у порівнянні з іншими платформами.

1.  Download a zipped package corresponding to your version from the [download page](https://github.com/FreeCAD/FreeCAD/releases).
2.  Open the Downloads folder, and expand the downloaded zip file: ![](images/Freecad-mac-01.jpg )
3.  Drag the FreeCAD application from inside the zip to the Applications folder: ![](images/Freecad-mac-02.jpg )
4.  That\'s it, FreeCAD is installed! ![](images/Freecad-mac-03.jpg )

5\. If the system prevents FreeCAD from launching due to restricted permissions for applications not coming from the App store, you will need to enable it in the system settings: ![](images/Freecad-mac-04.jpg )

### Uninstalling

Hopefully you won\'t want to uninstall FreeCAD, but it is good to know how. On Windows and Linux, uninstalling FreeCAD is very straightforward. On Windows, use the standard \"remove software\" option found in the control panel; on Linux, remove it with the same software manager you used to install it. On Mac OS, simply remove it from the Applications folder.

### Setting basic preferences 

Once FreeCAD is installed, you might want to open it and change some preferences. Preference settings in FreeCAD are located under menu **Edit → Preferences**. Listed below are some basic settings you may wish to change; you can browse through the preference pages to see if there is anything else you want to change.

1.  **Language**: (*General* category, *General* tab) FreeCAD will automatically pick the language of your operating system, but you might want to change that. FreeCAD is almost fully translated into five or six languages; others are currently only partially translated. You can easily [help translating FreeCAD](https://crowdin.com/project/freecad). ![](images/Freecad-basic-options01.jpg )
2.  **Auto-load module**: (*General* category, *General* tab) Normally, FreeCAD will start by showing you the start page. You can skip this and begin a FreeCAD session directly in the workbench of your choice, listed under *Startup*, *Auto load module after startup*. [Workbenches](Workbenches.md) will be explained in detail in the [next chapter](Manual_The_FreeCAD_Interface.md).
3.  **Create new document at startup**: (*General* category, *Document* tab) Combined with the *Auto-load module* option above, if checked this starts FreeCAD ready for work. ![](images/Freecad-basic-options02.jpg )
4.  **Storage options**: (*General* category, *Document* tab) As with any complex application, FreeCAD likely contains bugs causing it to crash occasionally. Here you can configure options to help you to recover your work in case of a crash.
5.  **Authoring and license**: (*General* category, *Document* tab) Here you set the values to be used for new files you create. Consider making your files shareable right from the start, by using a friendlier, [copyleft](https://en.wikipedia.org/wiki/Copyleft) license like [Creative Commons](https://creativecommons.org/).
6.  **Redirect internal python messages**: (*General* category, *Output window* tab) These two options are always good to check, as they will cause messages from the internal python interpreter to show up in the [Report View](Manual:The_FreeCAD_Interface#Report_view.md) when there\'s a problem running a python script. ![](images/Freecad-basic-options03.jpg )
7.  **Units**: (*General* category, *Units* tab) Here you can set the default units system you wish to use. ![](images/Freecad-basic-options04.jpg )
8.  **Zoom at cursor**: (*Display* category, *3D* tab) If set, zoom operations will be focused at the mouse pointer. If unset, the center of the current view is the zoom focus.
9.  **Invert zoom**: (*Display* category, *3D* tab) Inverts the direction of zooming relative to mouse movement. ![](images/FreeCAD-v0-18-Preferences-Display.png )

### Installing additional content 

As the FreeCAD project and its community grows quickly, and also because it is easy to extend, external contributions and side-projects made by community members and other enthusiasts begin to appear everywhere on the internet. Most of these external projects are workbenches or macros, and can be easily installed right from within FreeCAD via the [Addon Manager](Std_AddonMgr.md) located under menu **Tools**. The addons manager will allow you to install many interesting components, for example:

1.  A [Parts library](https://github.com/FreeCAD/FreeCAD-library), which contains all kinds of useful models, or pieces of models, created by FreeCAD users that can be freely used in your projects. The library can be used and accessed right from inside your FreeCAD installation.
2.  [Additional workbenches](https://github.com/FreeCAD/FreeCAD-addons), that extend the functionality of FreeCAD for certain tasks, for example animate parts of your models, or areas, such as sheet metal folding or BIM. Further explanations of each workbench and what tools it contains is given on each addon page, that you can visit by clicking the corresponding link on the addon manager.
3.  A [collection of macros](https://github.com/FreeCAD/FreeCAD-macros), which are also available [on the FreeCAD wiki](Macros_recipes.md) along with documentation about how to use them.

<img alt="" src=images/FreeCAD-addon-manager01.jpg  style="width:800px;">

If you are using the Ubuntu operating system, some of the addons above are also available as packages on the [FreeCAD addons PPA](https://launchpad.net/freecad-extras)

**Read more**

-   [More download options](Download.md)
-   [FreeCAD PPA for Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [FreeCAD addons PPA for Ubuntu](https://launchpad.net/freecad-extras)
-   [Compile FreeCAD yourself](Compiling.md)
-   [FreeCAD translations](https://crowdin.com/project/freecad)
-   [FreeCAD github page](https://github.com/FreeCAD)
-   [The FreeCAD addons manager](Std_AddonMgr.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Installing/uk
