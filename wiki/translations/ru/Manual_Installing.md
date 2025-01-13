# Manual:Installing/ru
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

FreeCAD распространяется под лицензией [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), Вы можете загрузить, установить, распространять и использовать FreeCAD любым способом, вне зависимости от выполняемой с ним работы (коммерческой или некоммерческой). Вы не связаны никакими ограничениями, и все файлы, которые Вы произвели с его помощью, принадлежат только Вам. Единственное, что запрещает Вам лицензия, это утверждать, что Вы сами написали FreeCAD!


</div>


<div class="mw-translate-fuzzy">

FreeCAD работает одинаково на Windows, Mac OS и Linux. Однако способ установки отличается в зависимости от Вашей платформы. На Windows или Mac сообщество FreeCAD обеспечивает прекомпилированные пакеты (установщики), готовые для загрузки, в то время как на Linux майнтайнерам дистрибутивов предоставляется исходный код, и уже они отвечают за составление пакетов для их дистрибутива. В результате Вы обычно можете установить FreeCAD из программного менеджера пакетов.


</div>


<div class="mw-translate-fuzzy">

Официальная страница загрузки FreeCAD для Windows и Mac OS находится по адресу <https://github.com/FreeCAD/FreeCAD/releases>


</div>

**Версии FreeCAD**


<div class="mw-translate-fuzzy">

Официальные выпуски FreeCAD, которые Вы можете найти на странице указанной выше и в менеджере пакетов Вашего дистрибутива, это стабильные версии. Тем не менее, FreeCAD разрабатывается быстро! Новые возможности и исправления ошибок добавляются почти каждый день. Поскольку порой требуется много времени до стабильного выпуска, Вас может заинтересовать последняя версия FreeCAD. Эти версии для разработчиков, или пре-релизы, загружаются время от времени на вышеупомянутую [страницу загрузки](https://github.com/FreeCAD/FreeCAD/releases), или, если Вы используется Ubuntu или Fedora, сообщество FreeCAD так же поддерживает \'ежедневные сборки\' [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (Personal Package Archives) и [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/), которые регулярно обновляются самыми последними изменениями.


</div>


<div class="mw-translate-fuzzy">

Если Вы установили FreeCAD на виртуальной машине, учтите плохую производительность (или даже в некоторых случаях неработоспособность) из-за ограничений поддержки [OpenGL](https://ru.wikipedia.org/wiki/OpenGL) на большинстве виртуальных машин.


</div>



### Установка под Windows 


<div class="mw-translate-fuzzy">

1.  Загрузите пакет установщика (.exe) соответственно вашей версии Windows (32bit или 64bit) со [страницы загрузки](https://github.com/FreeCAD/FreeCAD/releases). Установщик FreeCAD работает на любой версии, начиная с Windows 7.
2.  Дважды кликните на загруженном установщике.
3.  Примите требования лицензии LGPL, это один из тех случаев, когда Вы можете действительно без опаски нажать кнопку \"accept\" без чтения текста. Никаких скрытых утверждений: ![никаких](images/Freecad-windows-install-01.jpg )
4.  Можно оставить путь по умолчанию, или изменить по желанию: ![ничего](images/Freecad-windows-install-02.jpg )
5.  Переменную PYTHONPATH устанавливать не требуется, если Вы не планируете сложного программирования на python, в в таком случае Вы, вероятно, уже знаете, для чего это: ![ничего](images/Freecad-windows-install-03.jpg )
6.  Во время установки некоторые дополнительные компоненты, включённые в пакет, будут так же установлены: ![ничего](images/Freecad-windows-install-04.jpg )
7.  Всё, FreeCAD установлен. Вы можете найти его в стартовом меню. ![ничего](images/Freecad-windows-install-05.jpg )


</div>

**Установка версии для разработчика**


<div class="mw-translate-fuzzy">

Упаковка FreeCAD и создание установщика требует некоторого времени и внимания, так что версии разработчика (так называемые pre-release) предоставляются как архивы .zip (или .7z). Им не требуется установка, просто распакуйте их и запустите FreeCAD двойным кликом на файле FreeCAD.exe, который находится внутри. Это так же позволит Вам иметь одновременно стабильную и \"нестабильную\" версию на одном компьютере.


</div>



### Установка в Linux 


<div class="mw-translate-fuzzy">

В большинстве современных дистрибутивов Linux (Ubuntu, Fedora, openSUSE, Debian, Mint, Elementary и т.д), FreeCAD может быть установлен нажатием кнопки, прямо из приложения управления программами дистрибутива (его вид может отличаться от картинки ниже, поскольку каждый дистрибутив использует свои инструменты).


</div>


<div class="mw-translate-fuzzy">

1.  Откройте менеджер программ и найдите \"freecad\":
    <img alt="" src=images/Freecad-linux-install-01.jpg  style="width:800px;">
2.  Кликните кнопку \"install\", и готово, FreeCAD установлен. Не забудьте потом выставить ему рейтинг!
    <img alt="" src=images/Freecad-linux-install-02.jpg  style="width:800px;">


</div>

**Альтернативные пути**


<div class="mw-translate-fuzzy">

Одна из главных радостей использования Linux это множество возможностей для настройки своих программ, так что не ограничивайте себя. В Ubuntu и их производных FreeCAD так же может быть установлен из [PPA](https://launchpad.net/~freecad-maintainers), поддерживаемых сообществом FreeCAD (он содержит и стабильную, и нестабильную версию). В Fedora, последние разрабатываемые версии FreeCAD могут быть установлены из [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/), и поскольку это программы с исходными кодами, Вы так же можете запросто [скомпилировать FreeCAD самостоятельно](Compiling/ru.md).


</div>



### Установка в Mac OS 

Установка FreeCAD на Mac OSX теперь так же легка, как и для других платформ. Однако, поскольку в сообществе меньше людей имеет Mac, доступные пакеты часто задерживаются на несколько версий относительно других платформ.


<div class="mw-translate-fuzzy">

1.  Загрузите зазипованный пакет, соответствующий Вашей версии, со [страницы загрузки](https://github.com/FreeCAD/FreeCAD/releases).
2.  Откройте папку Downloads, и раскройте загруженный файл .zip: ![](images/Freecad-mac-01.jpg )
3.  Перетащите приложение FreeCAD из zip в папку Applications: ![](images/Freecad-mac-02.jpg )
4.  Всё, FreeCAD установлен! ![](images/Freecad-mac-03.jpg )

5\. Если система запрещает запуск FreeCAD из-за отсутствия разрешения на приложение не из App store, разрешите их в системных установках: ![](images/Freecad-mac-04.jpg )


</div>



### Деинсталляция


<div class="mw-translate-fuzzy">

Надеемся, Вы не захотите деинсталлировать FreeCAD, но всё равно хорошо бы это знать. В Windows и в Linux удаление FreeCAD очень просто. В Windows используйте стандартную опцию \"remove software\" в контрольной панели, В Linux удалите его тем же менеджером пакетов, который Вы использовали для установки FreeCAD. В Mac OS просто удалите его из папки Applications.


</div>



### Установка базовых параметров 


<div class="mw-translate-fuzzy">

Когда FreeCAD установлен, Вам захочется открыть его и настроить. Установка предпочтений в FreeCAD находится в меню **Правка → Параметры**. Ниже перечислены некоторые базовые настройки, которые Вы можете захотеть изменить. Вы можете просмотреть страницы настроек в поисках чего-то ещё, что Вам захочется изменить.


</div>

#### General category, General tab 

![](images/FreeCAD_022_GeneralGen.png )

1.  **Language**: By default, FreeCAD will select your operating system\'s language, but you have the option to change it. Thanks to the dedication of many contributors, FreeCAD is available in a wide array of languages.
2.  **Units**: This setting allows you to choose the default units system for your projects.

#### General category, Document tab 

![](images/FreeCAD_022_GeneralDoc.png )

1.  **Create a new document at startup**: FreeCAD will automatically open a new document each time the program starts.
2.  **Storage options**: Configure settings here to help you recover your work in the event of a crash.
3.  **\'Authoring and license**\': In this area, you can determine the settings for new files. To facilitate sharing, consider starting with a more permissive, copyleft license like Creative Commons.

#### Display category, Navigation tab 

![](images/FreeCAD_022_DisplayNav.png )

1.  **Zoom at cursor**: When enabled, zoom actions center on the mouse cursor. If disabled, zoom focuses on the center of the view.
2.  **Invert zoom**: This option reverses the zoom direction in relation to mouse movement.

#### Workbenches tab 

![](images/FreeCAD_022_WBMenu.png )

Although FreeCAD typically opens to the start page, this setting lets you bypass it. You can start directly in your preferred workbench. Additionally, you can customize which workbenches are displayed in the selector menu.

#### Import-Export tab 

![](images/FreeCAD_022_ImportExport.png )

Here, define basic parameters for importing and exporting in various formats.



### Установка дополнительного содержимого 


<div class="mw-translate-fuzzy">

Поскольку проект FreeCAD и его сообщество быстро растёт, и поскольку его легко расширять, сторонние разработчики и проекты членов сообщества и сторонних энтузиастов начинают появляться в самых неожиданных местах интернета. Большинство из этих внешних проектов представляют собой рабочие среды или макросы и могут быть легко установлены прямо из FreeCAD через [менеджер дополнений](Std_AddonMgr/ru.md) (Addon Manager), находящийся в меню **Инструменты**. Менеджер дополнений позволит вам установить много интересных компонентов, например:


</div>

![](images/FreeCAD_022_AddonsMenu.png )


<div class="mw-translate-fuzzy">

1.  [Библиотека деталей](https://github.com/FreeCAD/FreeCAD-library), которая содержит все виды полезных моделей или частей моделей, созданных пользователями FreeCAD, которые могут свободно использоваться в ваших проектах. Библиотека может использоваться и быть доступна прямо из вашей установки FreeCAD.
2.  [Дополнительные верстаки](https://github.com/FreeCAD/FreeCAD-addons), которые расширяют функциональность FreeCAD для некоторых задач, например, анимация частей ваших моделей, или таких областей как складывание листового металла, или BIM. Дальнейшие объяснения каждого рабочего места и какие инструменты он содержит на каждой странице дополнений, которую вы можете посетить, нажав соответствующую ссылку в менеджере дополнений.




1.  [Коллекция макросов](https://github.com/FreeCAD/FreeCAD-macros), которые так же доступны [на FreeCAD wiki](Macros_recipes/ru.md) вместе с документацией об их использовании.


</div>

As of FreeCAD v0.17.9940, the recommended installation method of any of the above tools is the built-in Addon Manager. However, if for any reason this option is not available, then manual installation is always possible. More information can be found at the [FreeCAD addons page](https://github.com/FreeCAD/FreeCAD-addons)

**Читать далее**

-   [Дополнительные опции загрузки](Download/ru.md)
-   [PPA с FreeCAD для Ubuntu](https://launchpad.net/~freecad-maintainers)
-   [PPA с расширениями FreeCAD для Ubuntu](https://launchpad.net/freecad-extras)
-   [Самостоятельная компиляция FreeCAD](Compiling/ru.md)
-   [Трансляция FreeCAD](https://crowdin.com/project/freecad)
-   [Страница FreeCAD на github](https://github.com/FreeCAD)
-   [Менеджер дополнений FreeCAD](Std_AddonMgr/ru.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Installing/ru
