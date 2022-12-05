# Macro FCInfo/ru
**[left|45px|link=](File:Under_construction_icon-blue.svg.md) изображение и страница ещё не обновлены с новой функцией... ждём<br>(Эта вики-страница соответствует версии 1.22, 12/11/2020 и не включает в себя новые функции)**


{{Macro
|Name=Macro FCInfo
|Icon=FCInfo.png
|Description=Предоставляет информацию о выбранной форме и может отображать преобразование длины, наклона (градусы, радианы, уклоны, процент), площади, объема и веса в различных единицах (метрических и британских). Теперь макрос также работает для элементов эскиза в режиме редактирования.
<br />Французская Версия [https://gist.githubusercontent.com/mario52a/6afc64081c4eb8be3b93/raw/795cac01c84fbbfa7ea68703c7138667119995d8/FCInfo_fr_Ver_1-26c-rmu_Docked.FCMacro Version française]
|Author=Mario52
|Version=1.26c
|Date=2022/04/19
|FCVersion=All
|SeeAlso=[Arch Survey|<img src=images/Arch_Survey.svg style="width:24px"> [Arch Survey](Arch_Survey.md)<br /> [Macro_SimpleProperties|<img src=images/Macro_SimpleProperties.png style="width:24px"> [Macro SimpleProperties](Macro_SimpleProperties.md)<br /> [<img src=images/Macro_FCInfoGlass.png style="width:24px"> [Macro FCInfoGlass](Macro_FCInfoGlass.md)
}}

## Описание

Предоставляет информацию о выбранной форме и может отображать преобразование длины, наклона (градусы, радианы, уклоны, процент), площади, объёма и веса в различных единицах (метрических и британских). Теперь макрос также работает для элементов эскиза в режиме редактирования.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/5577cf1a8818a4cbc5790cce335df158713b5841/FCInfo_en_Ver_1-26c-rmu_Docked.FCMacro}}

<img alt="" src=images/Macro_FCInfo_00_en.png  style="width:480px;"> 
*FCInfo*

## Использование

Выберите объект или запустите приложение и выберите объект, после чего появится ряд сведений. Его расчеты основаны на единице измерения FreeCAD, которой является **мм** при каждом новом выделении, единица длины всегда указывается в **мм**, а угол - в **десятичных градусах**. <img alt="upper window" src=images/Macro_FCInfo_06.png  style="width:200px;"><img alt="lower window" src=images/Macro_FCInfo_07.png  style="width:200px;">




**Сектор 1: Документ**

-   Название документа
-   Метка объекта
-   Внутреннее имя объекта
-   Имя субэлемента объекта
-   Тип объекта


<div class="mw-translate-fuzzy">

**Сектор 2: Координаты щелкают мышью**

-   Координаты X, Y и Z щелкают мышью
-   Кнопка создания в точке, оси, плоскости, копировать векторную ось формы **FreeCAD.Vector (-24.0, 240.0, 7.0)**


</div>


<div class="mw-translate-fuzzy">

**Сектор 3: Ценность**

-   Длина объекта, если объект отображается по периметру лица, можно выбрать размер единицы измерения:
    km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique. Если объект является кругом, то одна секунда lineEdit открыта и отображает радиус круга.
-   Периметр формы


</div>


<div class="mw-translate-fuzzy">

**Сектор 4: вершины и детали**

-   CheckBox для поиска или не все детали объекта, если не отмечен, отображаются только основные значения.
-   Вершины и детали фигуры (compt_Edge), (compt_Faces), (compt_Vector of Face)
    макс. 200 строк в таблице, если отображается более 200 строк (! + 200) и количество строки
    (полная информация может быть сохранена с помощью кнопки **Save** в файле в формате CSV, и его можно просмотреть в электронной таблице с помощью **Read** или с помощью внешней таблицы в виде[LibreOffice](https://www.libreoffice.org/) [OpenOffice](http://openoffice.apache.org/downloads.html) or other)


</div>


<div class="mw-translate-fuzzy">

**Сектор 5: Наклон**

-   Наклоны объекта могут отображаться в:
-   **десятичная степень**, например: 174.831872611 °
-   **Вторая минута градусов**, например: 174 ° 49 \'54.741401\' \'
-   **радиан**, например: 3.05139181449 рад
-   *\'оценка*, например: 194.257636235 гон
-   **pourcent** ex: 30 ° = 57,74%
-   Наклоны в плоскостях XY, YZ, ZX и их координаты
-   **Направление объекта**, укажите направление объекта для расчета: координируйте_1 - координируйте_2 = направление (или обратное)
    -   
        **Line**
        
        эта кнопка создает линию в направлении объекта
-   **ValueAt**, возвращает трехмерный вектор, соответствующий значению параметра.


</div>


<div class="mw-translate-fuzzy">

**Сектор 6: Поверхность и Объем**

-   Поверхность формы отображается размер блока может быть выбран
-   Поверхность лица отображается размер блока может быть выбран
-   Объем формы отображается размер блока может быть выбран
-   плотность материала в **kg by dm3**
    (\"spinBox\" установлен в \"7,5\" kg, средняя плотность стали. Если вы хотите другое значение по умолчанию изменить значение плотности, строка 204)
-   Можно выбрать единицу массы **gram**:
    ton,quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy)
    lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
-   Вес формы отображается единица массы может быть выбран


</div>


<div class="mw-translate-fuzzy">

*\'Сектор 7: BoundBox\'*

-   BoundBox экстремальные размеры фигуры


</div>


<div class="mw-translate-fuzzy">

**Сектор 8: Центр:**

-   Центр формы и эти координаты XYZ
-   Центр масс и эти координаты XYZ
-   Кнопка создания в точке, оси, плоскости, копировать векторную ось формы **FreeCAD.Vector (-24.0, 240.0, 7.0)**


</div>


<div class="mw-translate-fuzzy">

**Сектор 9: Инерция**

-   Момент инерции и эти координаты длины и веса
-   Кнопка создания в точке, оси, плоскости, копировать векторную ось формы **FreeCAD.Vector (-24.0, 240.0, 7.0)**
    -   линия действий 1: x1, y1, z1
    -   линия действия 2: x2, y2, z2
    -   линия действия 3: x3, y3, z3
    -   диагональ действия 4: x1, y2, z3

одинаковы по длине и весу

-   Определитель 1: вычисляет определитель матрицы научного значения
-   Определитель 2: вычисляет определитель десятичного значения матрицы


</div>

**Раздел 10: Электронная таблица**

-    **Read**: читать данные в сохраненной электронной таблице **.FCInfo** или в формате txt, asc, csv

-    **Save**: сохранить данные на диск в форме, выбранной ниже **.FCInfo** или txt, asc, csv

-    **Tabulation**: разделитель - Tabulation

-    **Comma**: разделитель - запятая

-    **Semicolon**: разделитель точка с запятой

-    **Space**: разделитель - Space


<div class="mw-translate-fuzzy">

Возможность сохранить или прочитать электронную таблицу с другим разделителем, табуляцией, запятой, точкой с запятой, пробелом
Табуляция является разделителем для модуля электронных таблиц FreeCAD.
Число этих четырех разделителей рассчитывается для справки, если неизвестно
COMMA - это старый (01.16 и ранее) разделитель макроса FCInfo
Теперь для совместимости с таблицей FreeCAD и начиная с версии 01.17 TABULATION является разделителем по умолчанию.
Если вы хотите преобразовать свою старую электронную таблицу FCInfo: откройте ее в FCInfo и сохраните ее, выбрав опцию Tabulation


</div>


<div class="mw-translate-fuzzy">

**Раздел 11: Главный**

-    **CheckBox Clip Board**: если флажок установлен, координаты сохраняются в форме clipBoard: **FreeCAD.Vector (-24.0, 240.0, 7.0)**

-    **CheckBox Point**: если установлен флажок, в отображаемой координате создается одна точка: **FreeCAD.Vector (-24.0, 240.0, 7.0)**

-    **CheckBox Axis**: если установлен флажок, создается одна ось в отображаемой форме координат: **FreeCAD.Vector (-24.0, 240.0, 7.0)**

-    **CheckBox Plane**: если проверено, создается одна плоскость оси в отображаемой форме координат: **FreeCAD.Vector (-24.0, 240.0, 7.0)**

-    **Ref**: обновить отображение данных в представлении отчета

-    **Exit**: выйти из макроса (необходимо перезапустить с помощью кнопки панели инструментов или меню \"Вид → Панели → FCInfo\"

-    **CheckBox****1**: если этот флажок установлен, информация отображается в окне просмотра отчета

-    **CheckBox****2**: если этот флажок не установлен, макрос окна отображается справа (по умолчанию). Если это отмечено, макрос окна отображается слева


</div>

После запуска макроса макрос остается активным, а окно остается видимым. Чтобы выйти из макроса, нажмите **Exit**. Если вы уйдете крестиком, макрос останется в памяти, а данные появятся в \"представлении отчета\" FreeCAD.


<div class="mw-translate-fuzzy">


<center>

Image:Macro_FCInfo_04.png\|Docked to rigth, Image:Macro FCInfo 05.png\|or left with Combo view and reachable by a tab, or not docked to the choice.


</center>





</div>

## Options


<div class="mw-translate-fuzzy">

## Варианты

### Используемая единица 

#### Единица длины: 

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.


</div>

#### Length unit: 

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.

#### Angle degrees : 


<div class="mw-translate-fuzzy">

#### Угол градусов : 

1.  **decimal degree**, ex: 174.831872611°
2.  degree minute seconde, ex: 174° 49\' 54.741401\'\'
3.  radian, ex: 3.05139181449 rad
4.  grade, ex: 194.257636235 gon
5.  pourcent ex: 30° = 57.74%


</div>

Понимание углов в дисплее FCInfo.


<center>

Image:Macro FCInfo 02.png\|Understanding of angles in FCInfo display Image:Macro FCInfo 03.gif\|Understanding of angles in poucent in FCInfo display
click twice to see the animation (the image must be in full screen)


</center>




#### Weight unit : 


<div class="mw-translate-fuzzy">

#### Единица измерения веса : 

ton, quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
the \"spinBox\" is set to **7,5** kg, средняя плотность стали. Если вы хотите другое значение по умолчанию, измените значение плотности, линии 208


</div>


```python
 global densite       ; densite       = 7.5  # (steel = 7.5 kg par dm3)
```


<div class="mw-translate-fuzzy">

Файл может быть создан кнопкой **Save**. Файл записан в виде файла [csv](https://fr.wikipedia.org/wiki/Comma-separated_values) таким образом, данные могут быть изучены в электронной таблице в FreeCAD or Openoffice, LibreOffice\...


</div>


<div class="mw-translate-fuzzy">

## скрипт

Скопируйте содержимое макроса в файл с именем \"FCInfo.FCMacro\"

-   Windows: the form is usually **\" drive:\\Users\\your_user_name\\AppData\\Roaming\\FreeCAD\\ \"**
-   Ubuntu: the form is usually **\" /home/your_user_name/.FreeCAD \"**.

Или прямо в интерфейсе FreeCAD
Значок должен находиться в том же каталоге, что и макрос.
Загрузите расположение изображения на иконке <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> а затем перетащите мышкой правой кнопкой мыши «сохранить как» (не меняйте название)


</div>

Copy the contents of the macro in a file named \"FCInfo.FCMacro\"

-   Windows: the form is usually **\" drive:\\Users\\your_user_name\\AppData\\Roaming\\FreeCAD\\ \"**
-   Ubuntu: the form is usually **\" /home/your_user_name/.FreeCAD \"**.

Or, directly in the interface of FreeCAD
The icon must be in the same directory as the macro.
Download image positioning on the icon <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> and then drag the mouse right click \"save as\" (do not change the name)


<div class="mw-translate-fuzzy">

**PS: слишком долго, чтобы содержаться на вики-странице (в настоящее время вики-страницы принимают только 64 КБ), код макроса размещен на форуме**


</div>


<div class="toccolours mw-collapsible mw-collapsed">


<div class="mw-translate-fuzzy">

Существует также FCInfo_Alternate_Linux только для FreeCAD версии 0.13 \... и PyQt4


<div class="mw-collapsible-content">


</div>


<div class="mw-translate-fuzzy">

Также есть [Macro_FCInfo_Alternate_Linux](http://www.freecadweb.org/wiki/index.php?title=Macro_FCInfo_Alternate_Linux) здесь код изменяется (из-за ошибки отображения символов : **² ³ ° μ** порядковый номер не в диапазоне (128)\") что создает проблемы в определенных конфигурациях, функции одинаковы
Example : 
```python
global uniteSs       ; uniteSs       = u"mm²"
global uniteVs       ; uniteVs       = u"mm³"
global uniteAs       ; uniteAs       = u"°"
``` remplacés par 
```python
global uniteSs       ; uniteSs       = "mm"+iso8859(unichr(178))
global uniteVs       ; uniteVs       = "mm"+iso8859(unichr(179))
global uniteAs       ; uniteAs       = iso8859(unichr(176))
``` **Файлы, сохраненные в этой версии, несовместимы с другой версией (закрепленной или нет)**


</div>


</div>



</div>

Example : 
```python
global uniteSs       ; uniteSs       = u"mm²"
global uniteVs       ; uniteVs       = u"mm³"
global uniteAs       ; uniteAs       = u"°"
``` remplacés par 
```python
global uniteSs       ; uniteSs       = "mm"+iso8859(unichr(178)) # also:  carre    hex="\xb2"  # also:  html=<span>&#178;</span>
global uniteVs       ; uniteVs       = "mm"+iso8859(unichr(179)) # also:  cube     hex="\xb3"  # also:  html=<span>&#179;</span>
global uniteAs       ; uniteAs       = iso8859(unichr(176))      # also:  degrees  hex="\xb0"  # also:  html=<span>&#176;</span>
                                     = iso8859(unichr(181))      # also:  micro    hex="\xB5"  # also:  html=<span>&#181;</span>
``` **Files saved with this version is incompatible with the other version (docked or not)**


</div>


</div>



<div class="mw-translate-fuzzy">

Загрузите файл макроса в gist **docked to right**


</div>


<div class="mw-translate-fuzzy">


{{CodeDownload|https://gist.github.com/mario52a/8d40ab6c018c2bde678f|последняя версия Macro_FCInfo и значки в конце страницы}}


</div>


<div class="mw-translate-fuzzy">

(Или **[На форуме.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=47748#p47748)**)
**PS:** этот макрос использует **getSelection ()**, и список объектов начинается с 1 ex: для блока **Edge1 to Edge12** и код в консоли начинается с 0 ex: для поля **Edge \[0\] to Edge\[11\]**
Это нормально, когда подсчет массивов/списков внутри OpenCascade всегда начинается с **1, а не с 0**


</div>

### Limitations


<div class="mw-translate-fuzzy">

### Ограничения

Всегда оставляйте кнопку **Exit**. Если выйти из программы, не нажимая кнопку **Exit**, программа останется в памяти и продолжит работу, а дисплей останется в «отчете о просмотре». Вы должны оставить FreeCAD, чтобы стереть его из памяти.
В таблице видны только первые 200 элементов объекта, если в объекте более 200 элементов, сигнал будет отображаться как **(! +200)**. Полный список данных отображается в файле, сохраненном кнопкой **Save**.


</div>


<div class="mw-translate-fuzzy">

Если макрос окна не виден после запуска, см. Нижнее окно:


</div>

![](images/Macro_FCInfo_08.png )

![](images/FCInfo_begin_00.gif ) 


<div class="mw-translate-fuzzy">

проект:
~~читает файл прямо в таблице.~~ готово
~~соответствует \"краям\" и их координатам~~ выполнено
Ассоциация вещества по его плотности
~~наклон элемента, а не глобального объекта~~ готово
~~вставка прямо в интерфейс FreeCAD~~ выполнена


</div>

## Version


<div class="mw-translate-fuzzy">

-   ver 1.22 , 12/11/2020 : now the macro is totally uninstalled i use :


</div>

-   ver 1.26b 20/02/2022 upgrade for detect BSpline in SubObject

-   ver 1.26 06/02/2022 add info on Mesh and Points objects, decode colours, duplicate object or subObject, memorize the latest path and other preferences options

-   ver 1.25e 18/12/2021 add info detailed to BSpline (ToByArcs) and info \"sel\[0\].TypeId\"
-   ver 1.25d 12/12/2021 \-\--
-   ver 1.25c 12/12/2021 correct \"strAround((\" by \"str(Around(\" and other little \...
-   ver 1.25b 11/12/2021 correction error in change/modify new material and reorganization
-   ver 1.25 10/12/2021 PySide2 and add comboBox materials
-   ver 1.24 02/12/2021 add [adjustedGlobalPlacement](https://forum.freecadweb.org/viewtopic.php?f=22&t=59852) modified by edwilliams16 for placement with Body, boundbox tracing
-   ver 1.23cb 25/11/2021 delete **\"import Sketcher \* \"** create conflict with \"**open(OpenName, \"r\")**\" ??

Adding 
```python
FreeCAD.ActiveDocument.openTransaction(u"FCInfo")    # memorise les actions (avec annuler restore)
FreeCAD.ActiveDocument.commitTransaction()           # restore les actions  (avec annuler restore)
#FreeCAD.ActiveDocument.abortTransaction()            # abandonne les actions(avec annuler restore)
```

-   ver 1.25d, 13/12/2021 little correction material field uncomment the \"\'try\...Except\" !!!
-   ver 1.25c, 12/12/2021 little correction new material
-   ver 1.23b, 20/11/2021 little correction, add text info in beginning run macro, and ordinal the text code
-   ver 1.23 , 19/11/2021 include icon in macro, number decimal displayed, text height, configure options in the Preference FC, correct info for elements of sketch in edit mode.
-   ver 1.22 , 12/11/2020 : now the macro is totally uninstalled i use :


```python
try:
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)    # destroy
        self.window.deleteLater()                                     # destroy
        self.window.destroy()                                         # destroy
except Exception:
        None
```

[How do i exit from FreeCAD instead of Python?](https://forum.freecadweb.org/viewtopic.php?f=22&t=48013#p411508)

instead: 
```python
self.window.hide()
``` and i adding the possibility display or not the \"Error Message\" window \"False\" by default, if you wand activate the warning window go to : 
```python
FreeCAD >Menu >Tools >Edit parameters... >BaseApp/Preferences/Macros/FCMmacros/FCInfo > switchWarning
```

-   ver 1.21-3.01 , 07/11/2019 \# 07/11/2019 ver \"01.21-3-rmu\" replace character micro = \"U\", square = \"2\", cube = \"3\", degrees = \" deg\" see \"<https://forum.freecadweb.org/viewtopic.php?f=3&t=6005&start=70#p345819>\"
-   ver 1.21.01 (1.21-rmu) 30/05/2019 rmu change fixed positions to qt layouts grid.addWidget() by rmu75 see the rmu75 fork \"<https://gist.github.com/rmu75/b165147bd1c2f2659c014103793ae1d8>\"
-   ver 1.20 , 29/01/2018 optimization
-   ver 1.19 , 20/01/2018 create checkBox for use detection all elements of the object if wanted or not , the macro is faster. Optimisation
-   ver 1.18 , 19/12/2017 \...
-   ver 1.17c , 14/12/2017 create plane with coordinate give in one project in other project and replace \"FCInfo\" by \"\_\_title\_\_\"
-   ver 1.17b , 13/12/2017 little correction replace FCTreeView to FCInfo
-   ver 1.17 , 12/12/2017 add upgrade Moment of inertia mm and kg by pinq [FCMacro and moment of inertia of assembly](https://forum.freecadweb.org/viewtopic.php?t=23888), and create plane, axis, point, and add options separator for spreadsheet
-   ver 1.16 , 21/06/2017 add control height police (here PointSize 8) and checkbox for position the window to right or left
-   ver 1.15 , 19/12/2015 suppression PyQt4 option [see](http://forum.freecadweb.org/viewtopic.php?f=12&t=13541) , add checkBox for editing infos in report view
-   ver 1.14 , 04/08/2014 replace PyQt4 and PySide and correct tooltip not displayed cause on PySide and add fg
-   ver 1.13 , 27/07/2014 replace FCInfo_en_Ver_1-12_Docked.FCMacro to FCInfo_en_Ver_1-13_Docked.FCMacro accept PyQt4 and PySide
-   ver 1.12 , 10/03/2014 adding tooltip
-   ver 1.11 , 04/03/2014 adding µm, nm, pm, fm, µg, ng, pg, pourcent, fixed of grandeur carat ~~\"cd\"~~ in **\"ct\"**, display of the label and internal name, fixed calculation of angles XY YZ ZX could give an error on a compound shape, window dockable in FreeCAD
-   ver 1.10.b , 19/11/2013 buttons outside the scrollbar and the dimensions of the window blocking

(ver 1.10 , 18/11/2013 create scrollbar)
\*ver 1.08.b , 10/11/2013 translation units in English, error correction to display the area of the faces listed in the table and replacement of the\"**print**\" by \"**App.Console.PrintMessage**\"
~~ver 1.09 , 04/11/2013 works perfectly on Windows and Linux (cause of errors on Linux the characters : ² ³ ° \"ordinal not in range(128)\")~~
In a Linux distribution and in the case of an error of **\"ordinal not in range (128)\"** an alternative version exists on this page [Macro_FCInfo_Alternate_Linux](Macro_FCInfo_Alternate_Linux.md)
\*ver 1.08 , 24/10/2013 correction of high top \"Faces\" and \"Edges\" displaying 100 objects (in the saved file)
\*ver 1.07 , 11/10/2013 matches the \"Faces\" and their coordinates.
\*ver 1.06 , 22/09/2013 matches the \"Edges\" and their coordinates, inclination on the element rather than the global object
\*ver 1.05 , 17/09/2013 added an icon for the spreadsheet, conversion barrel fr, affichage des dimensions overall instead of coordinates.
\*ver 1.04 , 11/09/2013: read the file directly in a table.
\*ver 1.03 , 09/09/2013: clearer display in view report and replacement by \"typeObject = sel\[0\].Shape.ShapeType\"
\*ver 1.02 , 7/09/2013 : small updates
\*ver 1.00 , 6/09/2013

## Ссылки

Смотрите также: <img alt="Arch Survey" src=images/Arch_Survey.svg  style="width:36px;"> [Arch Survey](Arch_Survey/ru.md)

Вы можете поделиться своими комментариями на форуме [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)
Здесь еще один пост [FCInfo Macro](http://forum.freecadweb.org/viewtopic.php?f=8&t=6005)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCInfo/ru
