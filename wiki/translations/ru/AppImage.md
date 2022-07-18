# AppImage/ru
**По состоянию на 7 июля 2019 года сообщество FreeCAD отмечает, что загрузка AppImages из Github, похоже, истекает по таймауту до завершения. Мы не уверены, почему это происходит. Если это произойдет с вами, попробуйте загрузить еще раз. Это займет несколько попыток. Рекомендуется использовать [функцию автоматического обновления](#Автообновление/ru.md) AppImage, которая восстановит загрузку с того места, где произошла ошибка.**


{{TOCright}}

## Что такое AppImage? 

![](images/AppImage-logo.png ) **Упакуйте один раз и запускайте везде. Охватите пользователей всех основных дистрибутивов Linux на настольных ПК.**

AppImage это \"универсальный двоичный пакет\", предназначенный для распространения приложений на любой дистрибутив Linux. Читайте дальше о нём на [домашней странице Appimage](https   *//appimage.org) и в [Wikipedia](https   *//ru.wikipedia.org/wiki/AppImage).

Чтобы запустить его, сначала сделайте его исполняемым, а затем введите относительный или полный путь.


```python
chmod +x FreeCAD_xxx-x86_64.AppImage
./FreeCAD_xxx-x86_64.AppImage
```

Для других типов установки смотрите [Download](Download/ru.md).

## AppImage\'и FreeCAD\'а 


**'''Примечание   *''' Разрабатываемые сборки теперь размещаются на [https   *//github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds '''FreeCAD-Bundle'''] репозитория github.<br/>Если приведённые ниже ссылки не работают, загрузите файлы вручную из расширенного раздела «Assets» приведённой выше ссылки.**

  Stable                                                                                                                Development
   
  ![](images/AppImage-logo.png ) [v0.20](https   *//github.com/FreeCAD/FreeCAD-Bundle/releases/tag/0.20)   ![](images/AppImage-logo.png ) [Weekly build](https   *//github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds)

     * style=\"text-align   * center; font-size   * 150%; \| Available FreeCAD AppImages \|+

**Важные замчания   ***

-   Разработка происходит ежедневно и быстро, ссылка на самую последнюю версию AppImage постоянно меняется.
-   Ссылка на разработку выше должна быть актуальной, потому что она обновляется с помощью скрипта.
-   Многие пользователи форума используют версию для разработки.
-   Его можно запускать в той же системе параллельно с другой версией FreeCAD.
-   Пользователи используют версию для разработчиков, чтобы воспользоваться последними функциями и исправлениями ошибок (поскольку FreeCAD имеет длительный цикл выпуска). Они также используют его для тестирования и поиска ошибок, чтобы стимулировать разработку и улучшение FreeCAD.

#### Необходимое предупреждение 

По большей части разрабатываемая версия стабильна, но, конечно, важно добавить обязательное заявление, что вы её используете на свой страх и риск. Хотя у большинства людей, которые используют резервные копии и \'часто сохраняются\', всё довольно хорошо.

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

Это более элегантная сторонняя неофициальная версия AppImageUpdate с именем **AppImageUpdater**. Он всё ещё находится в разработке (на момент этого редактирования вики), но тем не менее, довольно удобен в использовании.

1.  Загрузите [AppImageUpdater-\*-x86\_64.AppImage](https   *//github.com/antony-jr/AppImageUpdater/releases/tag/continuous)
2.  Сделайте его исполняемым   * 
```pythonchmod +x AppImageUpdater*-x86_64.AppImage```
3.  Запустите его   * 
```pythonsource AppImageUpdater*-x86_64.AppImage```
4.  Найдите текущий файл FreeCAD AppImage и перетащите его в AppImageUpdater

Далее   * Следуйте инструкциям AppImageUpdater

### Метод через командную строку №1 (официальный) 

Выполните следующие инструкции в своем терминале


```python
wget https   *//github.com/AppImage/AppImageUpdate/releases/download/continuous/appimageupdatetool-x86_64.AppImage
chmod +x ./appimageupdatetool-x86_64.AppImage
./appimageupdatetool.AppImage path/to/old/FreeCAD.AppImage
chmod +x path/to/updated/FreeCAD.AppImage
./path/to/updated/FreeCAD.AppImage
```

Примечания   *

-   Имена файлов будут уникальными, поскольку в них встроена информация о версии. Приведённые выше инструкции упрощены для удобства.
-   Запустите `./appimageupdatetool-x86_64.AppImage --help`, чтобы узнать о таких функциях, как `--remove-old`, `--overwrite` и `--self-update`.
-   Также есть версия i386; см. страницу [AppImageUpdate release](https   *//github.com/AppImage/AppImageUpdate/releases).

Что нужно сделать   * поделитесь скриптом, который можно добавить в качестве алиаса или задания cron.

### Метод через командную строку №2 (неофициальный) 

Аналогично графическим методам, имеющим официальный и неофициальный подходы к загрузке AppImages, то же самое относится и к командной строке. Это более элегантный сторонний вариант в командной строке для загрузки AppImages.

1.  Загрузите [appimageupdater-\*-x86\_64.AppImage](https   *//github.com/antony-jr/AppImageUpdater/releases/tag/continuous-cli)
2.  Сделайте его исполняемым   * 
```pythonchmod +x appimageupdater*-x86_64.AppImage```
3.  Запустите его   * 
```pythonsource appimageupdater*-x86_64.AppImage /path/to/old/FreeCAD-AppImage.AppImage```

**Результат**   * Обновляет указанный файл AppImage, если обновление существует.

# Экспериментальные функции 

## Исправление AppImage через zsync 

Может случиться так, что AppImage не будет обновляться, потому что его целевой файл каким-то образом изменился. Вместо того, чтобы загружать новый образ приложения, можно переписать файл zsync, который используется AppImage для загрузки дельты. Дополнительную информацию можно найти на странице <https   *//github.com/antony-jr/appimage-update-info-writer>.

Этот раздел требует более подробной информации.

## Загрузка через Bittorrent 

Экспериментальная возможность, которую исследует команда разработчиков пакетов FreeCAD (благодаря работе Antony-jr), позволяет загрузить дельту AppImage FreeCAD через битторрент. Репозиторий исходников находится по адресу <https   *//github.com/FreeCAD/FreeCAD-Bundle/issues/49>.

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

## Персонализированные AppImage 

Благодаря работе **realthunder**, автора [App Link](App_Link/ru.md) и [Верстака Assembly3](Assembly3_Workbench/ru.md), можно создавать пользовательские AppImage с помощью набора скриптов.

Это делает очень удобным выпуск образов определённой ветви исходного кода для тестирования другими. Хотя AppImages работают только в Linux, скрипты realthunder\'а позволяют создавать AppImage также в Windows и MacOS.

Репозиторий этих скриптов находится по адресу [realthunder/FreeCADMakeImage](https   *//github.com/realthunder/FreeCADMakeImage). Дополнительную информацию смотри в [Readme.md](https   *//github.com/realthunder/FreeCADMakeImage/blob/master/Readme.md).

## Связанные ссылки 

-   Пакеты [Snap](Ubuntu_Snap/ru.md).
-   Пакеты [Flatpak](Flatpak.md).



[Category   *Packaging](Category_Packaging.md) [Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Testing](Category_Testing.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > [Testing](Category_Testing.md) > AppImage/ru
