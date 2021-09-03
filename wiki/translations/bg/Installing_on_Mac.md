





<div class="mw-translate-fuzzy">

FreeCAD може да бъде инсталиран на Mac OS X само с една стъпка използвайки инсталаторът по-долу.


</div>


{{DownloadMacStable}}

and the weekly build can be downloaded from

<img alt="" src=images/Nightly.png  style="width:30px;">[Weekly](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds)

You can also use a package manager such as HomeBrew to keep your software updated. Instructions to install HomeBrew can be seen [here](https://brew.sh/). When HomeBrew installed you can simply install FreeCAD 0.18.4 through your bash terminal with


```python
brew install --cask freecad
```

and to use the latest version available (0.19pre) on HomeBrew you may run


```python
brew install freecad
```

If there are any issues with the HomeBrew Cask or Formula you may report them to [here](https://github.com/FreeCAD/homebrew-freecad).

Тази страница описва употребата на FreeCAD инсталаторът. Също включва инструкции за деинсталиране. След като инсталирате FreeCAD вижте страницата [първи стъпки](Getting_started/bg.md)!

### Проста Инсталация 

FreeCAD инсталаторът е под формата на инсталационнен пакет (.mpkg) съдържащ се в disk image file.

The FreeCAD installer is provided as a app package (.app) enclosed in a disk image file.

Може да свалите последния инсталатор от страницата [Download](Download/bg.md). След като свалите файлът монтирайте (mount) го и натиснете върху **Install FreeCAD**.

![](images/mac_installer_1.png )

Инсталаторът ще ви предложи списък от компоненти които можете да инсталирате (екранът **Customize Installation**). Ако имате някои от тези компоненти вече инсталирани можете да ги деселектирате. Ако не сте сигурни, оставте всички опции селектирани.

### Деинсталация

В момента няма деинсталатор на FreeCAD за Mac. За да махнете FreeCAD напълно, заедно с всички инсталирани компоненти, преместете следните файлове и директории в боклука:

-   В /Applications:
    -   FreeCAD


<div class="mw-translate-fuzzy">

Това е. Надяваме се в бъдеще да предлагаме FreeCAD като самостоятелен пакет, който се деинсталира по-лесно.


</div>


<div class="mw-translate-fuzzy">


{{docnav|Install on Unix/bg|Getting started/bg}}


</div>



