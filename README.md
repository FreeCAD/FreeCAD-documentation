# The FreeCAD documentation

**Note**: This repository contains an automatic conversion of the FreeCAD wiki located at https://wiki.freecadweb.org to the [markdown format](https://en.wikipedia.org/wiki/Markdown). The conversion is done automatically through the [migrate.py](./migrate.py) script located within this repository. The script downloads the wiki contents in XML format using the MediaWiki API and uses [pandoc](https://pandoc.org/) to convert between MediaWiki and markdown formats. This is a work in progress towards a more usable version of the documentation.

This documentation can be installed via the FreeCAD [addons manager](wiki/Std_AddonMgr.md) for offline browsing.



## Introduction

This is the officiadocumentation of [FreeCAD](http://www.freecadweb.org). There are several ways to use this documentation: by exploring the **hubs**, by following the **manual**, or by **searching** for a specific page. The **Help menu** entries from within FreeCAD also allow you to browse this documentation, online or offline. This documentation is a work in progress, written by the community of users and developers of FreeCAD. If you find information that is wrong or missing, please [help](Special:MyLanguage/help_FreeCAD.md)! 



## The hubs 

#### <img alt="Crystal_Clear_app_display.png" src=wiki/images/Crystal_Clear_app_display.png  style="width:32px;"> [Users hub](wiki/User_hub.md)
This page contains documentation useful for FreeCAD users in general: a list of all the workbenches, detailed instructions on how to install and use the FreeCAD application, tutorials, and all you need to get started.

#### <img alt="" src=wiki/images/Crystal_Clear_app_terminal.png  style="width:32px;"> [Power users hub](wiki/Power_users_hub.md)

This page gathers documentation for advanced users and people interested in writing python scripts. There you will also find a repository of macros, instructions on how to install and use them, and more information about customizing FreeCAD to your specific needs. 

#### <img alt="" src=wiki/images/Crystal_Clear_app_tutorials.png  style="width:32px;">[Developers hub](wiki/Developer_hub.md)

This section contains material for developers: How to compile FreeCAD yourself, how the FreeCAD source code is structured, how to navigate the source code, how to develop new workbenches, and embed FreeCAD in your own application. 



## Manual

#### <img alt="" src=wiki/images/Crystal_Clear_manual.png  style="width:32px;"> [The FreeCAD manual](wiki/Manual:Introduction.md)

The manual is another, more linear way to present the information contained in this wiki. It is designed to be read like a book, and will gently introduce you to many other pages from the hubs above. [ebook versions](https://www.gitbook.com/book/yorikvanhavre/a-freecad-manual/details) are also available, as well as [a couple of translations in pdf format](https://www.freecadweb.org/manual/). 



## Translations

This documentation is fully translatable by users to other languages, and is in a continuous process of translation. Several partially or fully translated versions of this documentation are available:

|   |   |   |
|---|---|---|
| ![Flag hr](wiki/images/Flag-hr.jpg) [Croatian / hrvatski](wiki/translations/hr/Main_Page.md) | ![Flag uk](wiki/images/Flag-uk.jpg) [Ukrainian / українська](wiki/translations/uk/Main_Page.md) | ![Flag cs](wiki/images/Flag-cs.jpg) [Czech / čeština](wiki/translations/cs/Main_Page.md) |
| ![Flag ko](wiki/images/Flag-ko.jpg) [Korean / 한국어](wiki/translations/ko/Main_Page.md) | ![Flag pt](wiki/images/Flag-pt.jpg) [Portuguese / português](wiki/translations/pt/Main_Page.md) | ![Flag bg](wiki/images/Flag-bg.jpg) [Bulgarian / български](wiki/translations/bg/Main_Page.md) |
| ![Flag tr](wiki/images/Flag-tr.jpg) [Turkish / Türkçe](wiki/translations/tr/Main_Page.md) | ![Flag ro](wiki/images/Flag-ro.jpg) [Romanian / română](wiki/translations/ro/Main_Page.md) | ![Flag ja](wiki/images/Flag-ja.jpg) [Japanese / 日本語](wiki/translations/ja/Main_Page.md) |
| ![Flag zh-cn](wiki/images/Flag-zh-cn.jpg) [Chinese (China) / 简体中文](wiki/translations/zh-cn/Main_Page.md) | ![Flag pl](wiki/images/Flag-pl.jpg) [Polish / polski](wiki/translations/pl/Main_Page.md) | ![Flag es](wiki/images/Flag-es.jpg) [Spanish / español de España](wiki/translations/es/Main_Page.md) |
| ![Flag fr](wiki/images/Flag-fr.jpg) [French / français](wiki/translations/fr/Main_Page.md) | ![Flag zh](wiki/images/Flag-zh.jpg) [Chinese / 简体中文](wiki/translations/zh/Main_Page.md) | ![Flag it](wiki/images/Flag-it.jpg) [Italian / italiano](wiki/translations/it/Main_Page.md) |
| ![Flag sv](wiki/images/Flag-sv.jpg) [Swedish / svenska](wiki/translations/sv/Main_Page.md) | ![Flag de](wiki/images/Flag-de.jpg) [German / Deutsch](wiki/translations/de/Main_Page.md) | ![Flag zh-tw](wiki/images/Flag-zh-tw.jpg) [Chinese (Taiwan) / 繁體中文](wiki/translations/zh-tw/Main_Page.md) |
| ![Flag ru](wiki/images/Flag-ru.jpg) [Russian / русский](wiki/translations/ru/Main_Page.md) | ![Flag pt-br](wiki/images/Flag-pt-br.jpg) [Portuguese (Brazil) / português](wiki/translations/pt-br/Main_Page.md) 



## Get involved with FreeCAD

### How to participate 

There is plenty to do inside the FreeCAD project, if you are interested in helping the project to develop. Of course, there are programming tasks for C++ or Python programmers, but there are also many things you can do even if you cannot code, such as:

-   writing, updating and translating this documentation
-   helping newcomers
-   translating the FreeCAD application
-   helping with the packaging of the latest release of FreeCAD for your favourite operating system
-   helping other people around you to discover FreeCAD
-   testing new functionality, and report bugs

The [help FreeCAD](Special:MyLanguage/help_FreeCAD.md) page describes it all with more details. Starting from 2016, FreeCAD also participates in the [Google Summer of Code](Google_Summer_of_Code.md). The [Contributors hub](wiki/Contributors_hub.md) page is another effort to gather the possible ways to help and contribute to the FreeCAD project.

### Working with the source code 

FreeCAD can be compiled on all platforms using [CMake](https://cmake.org/). The source code is [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)-licensed and hosted on [GitHub](https://github.com/FreeCAD/FreeCAD) and mirrored on [GitLab](https://gitlab.com/freecad/FreeCAD) and [CodeBerg](https://codeberg.org/FreeCAD/FreeCAD). There are build instructions for [Windows](wiki/Compile_on_Windows.md), [Linux](wiki/Compile_on_Linux.md) and [MacOS](wiki/Compile_on_MacOS.md). The source code documentation is [hosted here](http://www.freecadweb.org/api/), generated by [Doxygen](Doxygen.md), and [documented on the wiki](wiki/Source_documentation.md).

### About the development 

Check the [Development roadmap](wiki/Development_roadmap.md) for news about what is being planned, the [Changelog](http://www.freecadweb.org/tracker/changelog_page.php) and [Roadmap](http://www.freecadweb.org/tracker/roadmap_page.php) pages on the [FreeCAD tracker](http://www.freecadweb.org/tracker) to see the progress towards next release, or the [Project statistics](http://www.ohloh.net/p/freecad) for even more information about the FreeCAD codebase. All the development communication happens on the [forum](http://forum.freecadweb.org), so be sure to visit it if you are interested in participating.

