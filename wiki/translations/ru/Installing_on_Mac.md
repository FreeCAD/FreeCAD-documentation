# Installing on Mac/ru
<div class="mw-translate-fuzzy">

FreeCAD можно установить на macOS из пакета .dmg, который вы можете просто перетащить в вашу папку приложений:


</div>

If you would like to download a development version, which may be unstable, see the [Weekly builds download](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds) page.


<div class="mw-translate-fuzzy">

Для обновления программного обеспечения, Вы также можете использовать менеджер пакетов, например такой как HomeBrew. Инструкции по установке HomeBrew можно посмотреть [здесь](https://brew.sh/). После установки HomeBrew вы можете просто установить FreeCAD 0.18.4 через свой bash терминал


</div>


```python
brew install --cask freecad
```


<div class="mw-translate-fuzzy">

и чтобы использовать последнюю доступную версию (0.19 pre) на HomeBrew, вы должны запустить


</div>


```python
brew install freecad
```

Если у вас есть какие-либо проблемы с HomeBrew Cask или Formula, вы можете сообщить о них [здесь](https://github.com/FreeCAD/homebrew-freecad).


<div class="mw-translate-fuzzy">

На этой странице описано использование и функции установщика FreeCAD. Есть также инструкция по удалению. После установки вы можете [ начать работать](Getting_started.md)!


</div>



### Простая установка 

Установщик FreeCAD предоставляется в виде пакета приложения (.app), помещенного в файл образа.

Установщик FreeCAD предоставляется в виде пакета приложений (.app), заключенного в файл образа диска.

Вы можете загрузить последнюю версию установщика со страницы [Download](Download.md). После загрузки файла просто смонтируйте образ диска, затем перетащите его в папку «Приложение» или в папку по вашему выбору.

![](images/mac_installer_1.png )


<div class="mw-translate-fuzzy">

Вот и все. Просто нажмите на приложение, чтобы запустить FreeCAD. Если у вас появляется сообщение «FreeCAD не может быть запущен, так как его разработчик неизвестен». Откройте папку (Приложение) и щелкните правой кнопкой мыши на приложении, затем нажмите «Открыть» и «Подтвердить», чтобы открыть приложение.


</div>



### Удаление

В настоящее время для FreeCAD нет деинсталятора. Чтобы полностью удалить FreeCAD и все установленные компоненты, перетащите следующие файлы и папки в корзину:


<div class="mw-translate-fuzzy">

-   В /Приложения:
    -   FreeCAD


</div>


<div class="mw-translate-fuzzy">

Если вы установили FreeCAD вместе с homebrew, просто используйте команду `brew uninstall freecad`. Это все, что требуется.


</div>



---
⏵ [documentation index](../README.md) > Installing on Mac/ru
