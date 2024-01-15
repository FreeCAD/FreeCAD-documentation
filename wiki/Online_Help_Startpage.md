# The FreeCAD documentation

**Note**: This repository contains an automatic conversion of the FreeCAD wiki located at https://wiki.freecadweb.org to the [markdown format](https://en.wikipedia.org/Markdown). The conversion is done automatically through the [migrate.py](./migrate.py) script located within this repository. The script downloads the wiki contents in XML format using the MediaWiki API and uses [pandoc](https://pandoc.org/) to convert between MediaWiki and markdown formats. This is a work in progress towards a more usable and portable version of the documentation, to be used from within FreeCAD through the [Help module](https://github.com/yorikvanhavre/FreeCAD-Help).

This documentation can be installed via the FreeCAD [addons manager](Std_AddonMgr.md) for offline browsing.



## Introduction

This is the official documentation of [FreeCAD](http://www.freecadweb.org). There are several ways to use this documentation: by exploring the **hubs**, by following the **manual**, or by **searching** for a specific page. The **Help menu** entries from within FreeCAD also allow you to browse this documentation, online or offline. This documentation is a work in progress, written by the community of users and developers of FreeCAD. If you find information that is wrong or missing, please [help](Special:MyLanguage/help_FreeCAD.md)! 



## The hubs 

#### <img alt="Crystal_Clear_app_display.png" src=images/Crystal_Clear_app_display.png  style="width:32px;"> [Users hub](User_hub.md)

This page contains documentation useful 
for FreeCAD users in general: 
[frequently](Frequently_asked_questions.md) [asked](Frequently_asked_questions.md) [questions](Frequently_asked_questions.md),
a list of all the [workbenches](Workbenches.md),
detailed instructions on how to [install](Installing.md)
and use the FreeCAD application, [tutorials](Category_Tutorials.md),
[commands](List_of_Commands.md) [reference](List_of_Commands.md),
and all you need to get started.

#### <img alt="" src=images/Crystal_Clear_app_terminal.png  style="width:32px;"> [Power users hub](Power_users_hub.md)

This page gathers documentation for advanced users and people interested in writing [Python](https://python.org) code. There you will also find a repository of [macros](Macro.md), instructions on how to install and use them, [Python API](Category_API.md) documentation, and more information about customizing and extending FreeCAD to your specific needs. 

#### <img alt="" src=images/Crystal_Clear_app_tutorials.png  style="width:32px;">[Developers hub](Developer_hub.md)

This section contains material for developers who want to work with the C++/Python FreeCAD source code: How to [compile FreeCAD](Compiling.md) yourself, how the source code is structured, how to navigate it, how to develop new workbenches, and embed FreeCAD in your own application. 



## Manual

#### <img alt="" src=images/Crystal_Clear_manual.png  style="width:32px;"> [The FreeCAD manual](Manual_Introduction.md)

The manual is another, more linear way to present the information contained in this wiki. It is designed to be read like a book, and will gently introduce you to many other pages from the hubs above. [ebook versions](https://www.gitbook.com/book/yorikvanhavre/a-freecad-manual/details) are also available, as well as [a couple of translations in pdf format](https://www.freecadweb.org/manual/). 



## Translations

This documentation is fully translatable by users to other languages, and is in a continuous process of translation. Several partially or fully translated versions of this documentation are available:

|   |   |   |
|---|---|---|
| ![Flag hr](images/Flag-hr.jpg) [Croatian / hrvatski](translations/hr/Main_Page.md) | ![Flag uk](images/Flag-uk.jpg) [Ukrainian / українська](translations/uk/Main_Page.md) | ![Flag cs](images/Flag-cs.jpg) [Czech / čeština](translations/cs/Main_Page.md) |
| ![Flag ko](images/Flag-ko.jpg) [Korean / 한국어](translations/ko/Main_Page.md) | ![Flag pt](images/Flag-pt.jpg) [Portuguese / português](translations/pt/Main_Page.md) | ![Flag bg](images/Flag-bg.jpg) [Bulgarian / български](translations/bg/Main_Page.md) |
| ![Flag tr](images/Flag-tr.jpg) [Turkish / Türkçe](translations/tr/Main_Page.md) | ![Flag ro](images/Flag-ro.jpg) [Romanian / română](translations/ro/Main_Page.md) | ![Flag ja](images/Flag-ja.jpg) [Japanese / 日本語](translations/ja/Main_Page.md) |
| ![Flag zh-cn](images/Flag-zh-cn.jpg) [Chinese (China) / 简体中文](translations/zh-cn/Main_Page.md) | ![Flag pl](images/Flag-pl.jpg) [Polish / polski](translations/pl/Main_Page.md) | ![Flag es](images/Flag-es.jpg) [Spanish / español de España](translations/es/Main_Page.md) |
| ![Flag fr](images/Flag-fr.jpg) [French / français](translations/fr/Main_Page.md) | ![Flag zh](images/Flag-zh.jpg) [Chinese / 简体中文](translations/zh/Main_Page.md) | ![Flag it](images/Flag-it.jpg) [Italian / italiano](translations/it/Main_Page.md) |
| ![Flag sv](images/Flag-sv.jpg) [Swedish / svenska](translations/sv/Main_Page.md) | ![Flag de](images/Flag-de.jpg) [German / Deutsch](translations/de/Main_Page.md) | ![Flag zh-tw](images/Flag-zh-tw.jpg) [Chinese (Taiwan) / 繁體中文](translations/zh-tw/Main_Page.md) |
| ![Flag ru](images/Flag-ru.jpg) [Russian / русский](translations/ru/Main_Page.md) | ![Flag pt-br](images/Flag-pt-br.jpg) [Portuguese (Brazil) / português](translations/pt-br/Main_Page.md) 



## Other interesting resources

* [Help FreeCAD](Help_FreeCAD.md): How to contribute to the project?
* [Donation](Donate.md) options
* FreeCAD participates to the [Google Summer of Code](Google_Summer_of_Code.md) since 2016. Learn how to participate
* All the development communication happens on the [forum](http://forum.freecadweb.org), so be sure to visit it if you are interested in participating.

