# AppImage/ru
**По состоянию на 7 июля 2019 года сообщество FreeCAD отмечает, что загрузка AppImages из Github, похоже, истекает по таймауту до завершения. Мы не уверены, почему это происходит. Если это произойдет с вами, попробуйте загрузить еще раз. Это займет несколько попыток. Рекомендуется использовать [функцию автоматического обновления](#Автообновление/ru.md) AppImage, которая восстановит загрузку с того места, где произошла ошибка.**


{{TOCright}}

## Что такое AppImage? 

![](images/AppImage-logo.png ) **Упакуй раз и запускай везде. Дойдите до пользователей всех основных дистрибутивов рабочих столов Linux.**

AppImage это \"универсальный двоичный пакет\", предназначенный для распространения приложений на любой дистрибутив Linux. Читайте дальше о нём на [домашней странице Appimage](https   *//appimage.org) и в [Wikipedia](https   *//ru.wikipedia.org/wiki/AppImage).

Для запуска сделайте его исполняемым, и введите относительный или полный путь к файлу.


```python
chmod +x FreeCAD_xxx-x86_64.AppImage
./FreeCAD_xxx-x86_64.AppImage
```

Для других типов установки смотрите [Download](Download/ru.md).

## AppImages FreeCADа 


<div class="mw-translate-fuzzy">


**Если приведенные ниже загрузочные ссылки не работают, загрузите файлы вручную из раздела «Assets» [https   *//github.com/FreeCAD/FreeCAD/releases '''FreeCAD Github Releases''']**


</div>

  Stable                                                                                                                                                                                                                                                                                                              Development
   
  ![](images/AppImage-logo.png ) [0.19.3](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.19.3/FreeCAD_0.19.3-Linux-Conda_glibc2.12-x86_64.AppImage) ([SHA256](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.19.3/FreeCAD_0.19.3-Linux-Conda_glibc2.12-x86_64.AppImage-SHA256.txt))   ![](images/AppImage-logo.png ) \[<https   *//github.com/FreeCAD/FreeCAD-Bundle/releases/download/weekly-builds/FreeCAD_weekly-builds->{{   *Template   *Development-Version}}-Linux-Conda\_glibc2.12-x86\_64.AppImage {{   *Template   *Development-Version}}\] (\[<https   *//github.com/FreeCAD/FreeCAD-Bundle/releases/download/weekly-builds/FreeCAD_weekly-builds->{{   *Template   *Development-Version}}-Linux-Conda\_glibc2.12-x86\_64.AppImage-SHA256.txt SHA256\])

     * style=\"text-align   * center; font-size   * 150%; \| Available FreeCAD AppImages \|+

**Важные замчания   ***

-   Разработка происходит ежедневно и быстро, ссылка на самую последнюю версию AppImage постоянно меняется.
-   Ссылка на разработку выше должна быть актуальной, потому что она обновляется с помощью скрипта.
-   Многие пользователи форума используют версию для разработки.
-   Его можно запускать в той же системе параллельно с другой версией FreeCAD.
-   Пользователи используют версию для разработчиков, чтобы воспользоваться последними функциями и исправлениями ошибок (поскольку FreeCAD имеет длительный цикл выпуска). Они также используют его для тестирования и поиска ошибок, чтобы стимулировать разработку и улучшение FreeCAD.

#### Необходимое предупреждение 

По большей части разрабатываемая версия стабильна, но, конечно, важно добавить обязательное заявление, чтобы использовать ее на свой страх и риск. Хотя у большинства людей, которые используют резервные копии и «часто сохраняют», все хорошо.

## Автообновление

AppImage имеет умный и экономичный способ обновления. Он вычисляет разницу между новым AppImage и старым и загружает только изменения между их версиями. Теоретически пользователь каждый раз загружает около 15% вместо совершенно нового AppImage.

Автоматическое обновление выполняется несколькими возможными методами. В настоящее время существует 4 метода   * 2 - через графический интерфейс (GUI) и 2 - через интерфейс командной строки/терминала (CLI).

### Экспериментальное обновление в приложении 

Несколько ключевых разработчиков прилагают [постоянные усилия](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=44324) по интеграции функции, которая позволяет **самообновлять AppImage изнутри FreeCAD**. Начиная с FC 0.19.21514 существует раздел AppImage, который можно найти через **Правка → Настройки → AppImage**. Пожалуйста, проверьте эту возможность и сообщите о своем опыте в [обсуждении на форуме](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=44324).

### Метод через GUI №1 (официальный) 

Это официальное приложение с графическим интерфейсом AppImageUpdate.

1.  Загрузить [AppImageUpdate-x86\_64.AppImage](https   *//github.com/AppImage/AppImageUpdate/releases/download/continuous/AppImageUpdate-x86_64.AppImage).
2.  Сделайте его исполняемым, щелкнув правой кнопкой мыши по файлу, войдя в свойства и установив «Запускать как исполняемый файл».
3.  Дважды щелкните значок AppImage, появится диалоговое окно, в котором вам будет предложено указать, какой AppImage вы хотите обновить.
4.  Укажите путь к существующему AppImage.
5.  После обновления AppImage нажмите кнопку **Run updated AppImage**.

### Метод через GUI №2 (неофициальный) 

This is a sleeker 3rd-party unofficial version of AppImageUpdate named   * **AppImageUpdater**. It is still in development (at the time of this wiki edit) but nevertheless, quite nice to use.

1.  Download [AppImageUpdater-\*-x86\_64.AppImage](https   *//github.com/antony-jr/AppImageUpdater/releases/tag/continuous)
2.  Make it executable   * 
```pythonchmod +x AppImageUpdater*-x86_64.AppImage```
3.  Run it   * 
```pythonsource AppImageUpdater*-x86_64.AppImage```
4.  Find your current FreeCAD AppImage and drag-drop it on to the AppImageUpdater

Result   * Follow the AppImageUpdater prompts

### Метод через командную строку №1 (официальный) 

Выполните следующие инструкции в своем терминале


```python
wget https   *//github.com/AppImage/AppImageUpdate/releases/download/continuous/appimageupdatetool-x86_64.AppImage
chmod +x ./appimageupdatetool-x86_64.AppImage
./appimageupdatetool.AppImage path/to/old/FreeCAD.AppImage
chmod +x path/to/updated/FreeCAD.AppImage
./path/to/updated/FreeCAD.AppImage
```


<div class="mw-translate-fuzzy">

Примечания   *

-   Имена файлов будут уникальными, поскольку в них встроена информация о версии. Приведенные выше инструкции упрощены для удобства.
-   Запустите `./appimageupdatetool-x86_64.AppImage --help`, чтобы узнать о таких функциях, как `-r` и `--self-update`.
-   Также есть версия i386; см. страницу [AppImageUpdate release](https   *//github.com/AppImage/AppImageUpdate/releases).


</div>

Todo   * share a script that can be added as an alias or cron job.

### Метод через командную строку №2 (неофициальный) 

Similarly to the Graphical methods having an official and unofficial approaches to downloading AppImages, the same applies to the command line. This is a sleeker 3rd-party command line option to download AppImages

1.  Download [appimageupdater-\*-x86\_64.AppImage](https   *//github.com/antony-jr/AppImageUpdater/releases/tag/continuous-cli)
2.  Make it executable   * 
```pythonchmod +x appimageupdater*-x86_64.AppImage```
3.  Run it   * 
```pythonsource appimageupdater*-x86_64.AppImage /path/to/old/FreeCAD-AppImage.AppImage```

**Result**   * Updates specified AppImage file if update exists

# Experimental

## Fixing AppImage zsync 

It may happen that an AppImage won\'t update because it\'s target file changed in some way. Instead of downloading a whole new appimage, it\'s possible to rewrite the zsync file that is used by the AppImage to download the delta. More info can be found at <https   *//github.com/antony-jr/appimage-update-info-writer>.

This section needs more details.

## Downloading via Bittorrent 

An experimental feature that the FreeCAD packaging team is exploring (thanks to the work of Antony-jr) is being able to download an appimage delta of FreeCAD via bittorrent. The repository issue is at <https   *//github.com/FreeCAD/FreeCAD-Bundle/issues/49>

# Секция разработчика 


**Примечание   ***

следующая секция предназначена для разработчиков

## Распаковка AppImage 

Очень удобный аспект FreeCAD заключается в том, что большая его часть построена на [Python](Python/ru.md), который не нужно компилировать вручную, как C ++. По сути, файл Python можно изменить, и после перезапуска FreeCAD эти изменения будут интегрированы в приложение. Разработчик может быстро работать над последней версией FreeCAD, используя эту технику и в AppImage. Более того, использование AppImage никоим образом не изменяет среду вашей системы, то есть ничего не устанавливается и никакие переменные среды не изменяются.

### Модификация AppImage 

В AppImage встроена файловая система со всем, что требуется для запуска приложения. Чтобы изменить его, необходимо извлечь файловую систему.


```python
./FreeCAD_xxx.AppImage --appimage-extract
cd squashfs-root/
```

Теперь откройте необходимые исходные файлы Python в предпочитаемом вами редакторе кода, измените их и сохраните. Затем запустите приложение.


```python
./AppRun
```

### Переупаковка AppImage 

Если вы изменили код и теперь хотите повторно упаковать AppImage с последними изменениями, примените [appimagetool- x86\_64](https   *//github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage) к извлеченной файловой системе.


```python
cd ..
wget "https   *//github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
chmod +x appimagetool-x86_64.AppImage
./appimagetool-x86_64.AppImage squashfs-root
```

## Персонализация AppImage 

Thanks to the work of **realthunder**, author of [App Link](App_Link.md) and [Assembly3 Workbench](Assembly3_Workbench.md), it is possible to build custom AppImages using a set of scripts.

This makes it very convenient to release images for a specific branch of the source code for others to test. Although AppImages only work on Linux, realthunder\'s scripts make it possible to generate AppImages also on Windows and MacOS.

The repository for these scripts is at [realthunder/FreeCADMakeImage](https   *//github.com/realthunder/FreeCADMakeImage). Please read the [Readme.md](https   *//github.com/realthunder/FreeCADMakeImage/blob/master/Readme.md) for more details.

## Related

-   [Snap](Ubuntu_Snap.md) packages.
-   [Flatpak](Flatpak.md) packages.



[Category   *Packaging](Category_Packaging.md) [Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Testing](Category_Testing.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > [Testing](Category_Testing.md) > AppImage/ru
