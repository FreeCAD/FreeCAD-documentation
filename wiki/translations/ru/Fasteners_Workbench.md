# <img alt="Логотип верстака Стандартные изделия (Fasteners)" src=images/Fasteners_workbench_icon.svg  style="width:64px;"> Fasteners Workbench/ru






## Введение

[Внешний](External_workbenches/ru.md) верстак <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Стандартные Изделия (Fasteners)](Fasteners_Workbench/ru.md) позволяет быстро и удобно создавать различные крепёжные изделия а также устанавливать их в посадочные места деталей.

<img alt="" src=images/Fasteners_Toolbars.png  style="width:500px;"> 
*Внешний вид панели инструментов верстака.<br>
Крепёжные изделия с метрическими размерами имеют оранжевые значки.<br>
Крепёжные изделия с дюймовыми размерами имеют зеленые значки.*



## Установка


<div class="mw-translate-fuzzy">

1.  Установите верстак Fasteners через <img alt="" src=images/AddonManager.svg  style="width:24px;"> [менеджер дополнений](Std_AddonMgr/ru.md). В случае установки вручную ознакомьтесь с руководством по [установке дополнительных верстаков](Installing_more_workbenches/ru.md).
2.  Перезапустите FreeCAD.
3.  Выберете верстак <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Fasteners](Fasteners_Workbench/ru.md) в [в списке доступных верстаков](Std_Workbench/ru.md).
4.  При необходимости настройте панель инструментов и расположение меню:
    1.  Перейдите в меню: **Правка → Настройки... → Fasteners → Основные настройки → Toolbar screw icons grouping**.
    2.  Выберите один из доступных вариантов:
        -   
            **None**
            
            : Все крепежные элементы отображаются на одной панели инструментов. Чтобы просмотреть все доступные изделия, используйте кнопку **&gt;&gt;** чтобы развернуть ее.

        -   
            **Separate toolbars**
            
            : Крепежные элементы сгруппированы на нескольких панелях инструментов. Этот вариант выбран по умолчанию.

        -   
            **Dropdown buttons**
            
            : Крепежные элементы сгруппированы на панелях инструментов.
    3.  Перезапустите FreeCAD.


</div>



## Применение


<div class="mw-translate-fuzzy">

Крепёжные элементы могут быть прикреплены к посадочному месту или не прикреплены. У прикрепленныех крепёжных изделий в свойстве **base Object**, указанно ребро круглой формы к которому прикреплено изделие, следовательно свойство **Placement** динамический связано с этим ребом. Команда <img alt="" src=images/Fasteners_Move.svg  style="width:16px;"> [Перемещения крепежа](Fasteners_Move/ru.md) может быть использована для прикрепления или отсоединения крепежа.


</div>



### Добавление изделий без их крепления к чему либо 

1.  Select the desired fastener by clicking its button or by picking it from the menu.
2.  A fastener is created at the origin.
3.  Optionally change the dimensions and other properties of the fastener:
    1.  Select the fastener.
    2.  Go to the **Data** tab of the [Property editor](Property_editor.md).
    3.  Change the required properties.



### Добавление изделий с креплением к посадочным местам 

<img alt="" src=images/Fasteners_Attached_Selected.png  style="width:200px;"> <img alt="" src=images/Fasteners_Attached_Created.png  style="width:200px;"> 
*Слева в посадочных местах выбрано две грани круглой формы. Справа крепёжные изделия установленны в указанные места.*

1.  Specify if the selected holes are tap holes or pass holes by selecting <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:16px;"> [Fasteners MatchTypeInner](Fasteners_MatchTypeInner.md) or <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:16px;"> [Fasteners MatchTypeOuter](Fasteners_MatchTypeOuter.md) respectively (not used for countersunk screws).
2.  Select one or more circular edges and/or faces with circular edges. For countersunk screws the top edge of the chamfered hole must be selected.
3.  Select the desired fastener by clicking its button or by picking it from the menu.
4.  A fastener is attached to each of the selected circular edges.
5.  The default dimensions of each fastener depend on the radius of the circular edge it is attached to. Countersunk screws are matched by their head diameter, other fasteners are matched by their shaft diameter.
6.  Optionally change the dimensions and other properties of the fasteners. See above.
7.  Fasteners that appear upside-down can be inverted with the <img alt="" src=images/Fasteners_Flip.svg  style="width:16px;"> [Fasteners Flip](Fasteners_Flip.md) command or by changing their **Invert** property.
8.  Optionally change the **Offset** property to create space between the fasteners and the edges they are attached to.



## Примечания


<div class="mw-translate-fuzzy">

-   Если вы хотите, чтобы крепеж имел реалистичную резьбу (по умолчанию при добавлении крепежа резьба на нем не строится) его свойство **thread** должно быть установлено как `True`. Создание такой резьбы поглощает много ресурсов. Перерасчет трехмерного Вида (Recompute) занимает гораздо больше времени, если в документе много крепёжных изделий с реалистичной резьбой.
-   Свойства **invert** и **offset** игнорируются для крепёжных изделий которые не установлены в посадочные места.


</div>



## Команды

-   <img alt="" src=images/Fasteners_Flip.svg  style="width:32px;"> [Перевернуть крепёж](Fasteners_Flip/ru.md): Обращает ориентацию уже установленного крепежа на противоположную.

-   <img alt="" src=images/Fasteners_Move.svg  style="width:32px;"> [Переместить крепёж](Fasteners_Move/ru.md): Перемещает и устанавливает крепёж в указанную грань круглой формы. Может также использоваться для отсоединения крепёжа.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_Shape.svg  style="width:32px;"> [Создать непараметрическую копию](Fasteners_Shape/ru.md): Создает непараметрическую копию объекта (стандартного изделия).


</div>

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:32px;"> [Match for tap hole (Установить винты/болты в указанные места)](Fasteners_MatchTypeInner/ru.md): По диаметру выбранных ребер отверстий, автоматический подбирает крепёж по размеру в соответствии со стандартами и прикрепляет его к этим посадочным местам.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:32px;"> [Match screws by outer thread diameter (Pass hole)](Fasteners_MatchTypeOuter.md): подобрать резьбу по диаметру внутренний резьбы (отверстия под метчик).


</div>

-   <img alt="" src=images/Fasteners_BOM.svg  style="width:32px;"> [Спецификация](Fasteners_BOM/ru.md): Создает электронную таблицу со спецификацией крепежных элементов имеющихся в документе.

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:32px;"> [Калькулятор отверстия под резьбу](Fasteners_ScrewCalculator/ru.md): Открывает калькулятор для определения размера отверстия под резьбу определенного диаметра.

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width:32px;"> [Изменить параметры крепежа](Fasteners_ChangeParameters/ru.md): Изменить параметры стандартных изделий.



## Крепёжные изделия 

Крепёжные изделия с метрическими размерами имеют оранжевые значки. Крепёжные изделия с дюймовыми размерами имеют зеленые значки.



### Винты и болты с шестигранной головкой 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width:32px;"> **ASME B18.2.1.6** UNC Винт с шестигранной головкой.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width:32px;"> **ASME B18.2.1.8** UNC Винт с шестигранной головкой и фланцем.

-   <img alt="" src=images/Fasteners_DIN571.svg  style="width:32px;"> **DIN 571** **(Ближайший аналог ГОСТ 11473)** Шуруп с шестигранной головкой (для дерева).

-   <img alt="" src=images/Fasteners_DIN933.svg  style="width:32px;"> **DIN 933** Hexagon head screw.

-   <img alt="" src=images/Fasteners_DIN961.svg  style="width:32px;"> **DIN 961** Hexagon head screw.

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width:32px;"> **EN 1662** Болт с шестигранной головкой и фланцем, легкая серия.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width:32px;"> **EN 1665** Болт с шестигранной головкой и фланцем, тяжёлая серия.

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width:32px;"> 
**ISO 4014** **(ГОСТ Р ИСО 4014)** Болт с шестигранной головкой. *Классы точности А и В.*

-   <img alt="" src=images/Fasteners_ISO4015.svg  style="width:32px;"> **ISO 4015** Hexagon head bolt with reduced shank.

-   <img alt="" src=images/Fasteners_ISO4016.svg  style="width:32px;"> 
**ISO 4016** Hexagon head bolt. *Product grade C.*

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width:32px;"> 
**ISO 4017** **(ГОСТ Р ИСО 4017)** Винт с шестигранной головкой. *Классы точности А и В.*

-   <img alt="" src=images/Fasteners_ISO4018.svg  style="width:32px;"> 
**ISO 4018** Hexagon head screw. *Product grade C.*

-   <img alt="" src=images/Fasteners_ISO4162.svg  style="width:32px;"> 
**ISO 4162** Hexagon bolt with flange, small series. *Product grade A with driving feature of product grade B.*

-   <img alt="" src=images/Fasteners_ISO8676.svg  style="width:32px;"> 
**ISO 8676** Hexagon head screw with fine pitch thread. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO8765.svg  style="width:32px;"> **ISO 8765** Hexagon head bolt with fine pitch thread.

-   <img alt="" src=images/Fasteners_ISO15071.svg  style="width:32px;"> 
**ISO 15071** Hexagon bolt with flange, small series. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO15072.svg  style="width:32px;"> 
**ISO 15072** Hexagon bolt with flange and fine pitch thread, small series. *Product grade A.*



### Винты шестигранным углублением под ключ 

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width:32px;"> **ASME B18.3.1A** UNC Винт с цилиндрической головкой и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1G.svg  style="width:32px;"> **ASME B18.3.1G** UNC Винт с цилиндрической головкой уменьшенной высоты и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width:32px;"> **ASME B18.3.2** UNC Винт с потайной головкой и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width:32px;"> **ASME B18.3.3A** UNC Винт с полукруглой головкой и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width:32px;"> **ASME B18.3.3B** UNC Винт с полукруглой головкой с буртом и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width:32px;"> **ASME B18.3.4** UNC Винт с внутренним шестигранником в головке и утолщенным стержнем.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width:32px;"> **DIN 6912** Винт с цилиндрической головкой уменьшенной высоты и шестигранным углублением под ключ с центрирующим отверстием.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width:32px;"> **DIN 7984** Винт с цилиндрической головкой уменьшенной высоты и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO2936.svg  style="width:32px;"> **ISO 2936** Hexagon socket screw key.

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width:32px;"> **ISO 4762** **(ГОСТ Р ИСО 4762)** Винт с цилиндрической головкой и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width:32px;"> **ISO 7379** **(Ближайший аналог ГОСТ 28962)** Винт с внутренним шестигранником в головке и утолщенным стержнем.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width:32px;"> **ISO 7380-1** **(ГОСТ Р ИСО 7380-1)** Винт с полукруглой головкой и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width:32px;"> **ISO 7380-2** **(ГОСТ Р ИСО 7380-2)** Винт с полукруглой головкой с буртом и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width:32px;"> **ISO 10642** **(ГОСТ Р ИСО 10642)** Винт с потайной головкой и шестигранным углублением под ключ.



### Винты звездообразным углублением под ключ 

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width:32px;"> **ISO 14579** **(ГОСТ Р ИСО 14579)** Винт с цилиндрической головкой и звездообразным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width:32px;"> **ISO 14580** **(ГОСТ Р ИСО 14580)** Винт с низкой цилиндрической головкой и звездообразным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO14581.svg  style="width:32px;"> **ISO 14581** Hexalobular socket countersunk flat head screw.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width:32px;"> **ISO 14582** **(ГОСТ Р ИСО 14582)** Винт с высокой потайной головкой и звездообразным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width:32px;"> **ISO 14583** **(ГОСТ Р ИСО 14583)** Винт со скругленной головкой и звездообразным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width:32px;"> **ISO 14584** **(ГОСТ Р ИСО 14584)** Винт с полупотайной головкой и звездообразным углублением под ключ.



### Винты с прямым шлицем 

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.2.svg  style="width:32px;"> **ASME B18.6.1.2** Slotted flat countersunk head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.4.svg  style="width:32px;"> **ASME B18.6.1.4** Slotted oval countersunk head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width:32px;"> **ASME B18.6.3.1A** UNC Винт с потайной головкой и прямым шлицем.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.4A.svg  style="width:32px;"> **ASME B18.6.3.4A** UNC slotted oval countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.9A.svg  style="width:32px;"> **ASME B18.6.3.9A** UNC slotted pan head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.10A.svg  style="width:32px;"> **ASME B18.6.3.10A** UNC Slotted fillister head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.12A.svg  style="width:32px;"> **ASME B18.6.3.12A** UNC Slotted truss head screws.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.16A.svg  style="width:32px;"> **ASME B18.6.3.16A** UNC Slotted round head screw.

-   <img alt="" src=images/Fasteners_DIN84.svg  style="width:32px;"> 
**DIN 84 (superseded by ISO 1207)** Slotted cheese head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_DIN96.svg  style="width:32px;"> **DIN 96** Slotted half round head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-1.svg  style="width:32px;"> **ГОСТ 1144 (Исполнение 1)** Шуруп с полукруглой головкой.

-   <img alt="" src=images/Fasteners_GOST1144-1.svg  style="width:32px;"> **ГОСТ 1144 (Исполнение 2)** Шуруп с полукруглой головкой.

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width:32px;"> 
**ISO 1207** **(ГОСТ Р ИСО 1580)** Винт с низкой цилиндрической головкой со шлицем. *Класс точности А.*

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width:32px;"> 
**ISO 1580** **(ГОСТ Р ИСО 1580)** Винт с плоской головкой со шлицем. *Класс точности А.*

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width:32px;"> **ISO 2009** **(ГОСТ Р ИСО 2009)** Винт с потайной головкой и прямым шлицем. *Класс точности А*.

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width:32px;"> 
**ISO 2010** **(ГОСТ Р ИСО 2010)** Винт с полупотайной головкой со шлицем. *Класс точности А.*



### Винты с крестообразным шлицем 

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.3.svg  style="width:32px;"> **ASME B18.6.1.3** Flat countersunk head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.5.svg  style="width:32px;"> **ASME B18.6.1.5** Oval countersunk head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1B.svg  style="width:32px;"> **ASME B18.6.3.1B** UNC flat countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.4B.svg  style="width:32px;"> **ASME B18.6.3.4B** UNC oval countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.9B.svg  style="width:32px;"> **ASME B18.6.3.9B** UNC pan head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.10B.svg  style="width:32px;"> **ASME B18.6.3.10B** UNC fillister head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.12C.svg  style="width:32px;"> **ASME B18.6.3.12C** UNC truss head screws.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.16B.svg  style="width:32px;"> **ASME B18.6.3.16B** UNC round head screw.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width:32px;"> **DIN 967** **(Ближайший аналог ГОСТ 11644)** Винт с полукруглой головкой, буртом и крестообразным шлицем.


</div>

-   <img alt="" src=images/Fasteners_DIN7996.svg  style="width:32px;"> **DIN 7996** Pan head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-3.svg  style="width:32px;"> **GOST 1144-3** Pan head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-4.svg  style="width:32px;"> **GOST 1144-4** Pan head wood screw.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width:32px;"> 
**ISO 7045** **(ГОСТ Р ИСО 7045)** Винт со скругленной головкой и крестообразным шлицем типа Н. *Класс точности А.*


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width:32px;"> 
**ISO 7046** **(ГОСТ Р ИСО 7046 две части)** Винт с потайной головкой и крестообразным шлицем типа Н. *Класс точности А.*


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width:32px;"> 
**ISO 7047** **(ГОСТ Р ИСО 7047)** Винт с полупотайной головкой и крестообразным шлицем типа H. *Класс точности А.*


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width:32px;"> **ISO 7048** **(ГОСТ Р ИСО 7048)** Винт с низкой цилиндрической головкой и крестообразным шлицем.


</div>

-   <img alt="" src=images/Fasteners_ISO7049-C.svg  style="width:32px;"> **ISO 7049-C** Pan head self tapping screws with conical point.

-   <img alt="" src=images/Fasteners_ISO7049-F.svg  style="width:32px;"> **ISO 7049-F** Pan head self tapping screws with flat point.

-   <img alt="" src=images/Fasteners_ISO7049-R.svg  style="width:32px;"> **ISO 7049-R** Pan head self tapping screws with rounded point.



### Болты с другими головками 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.1.svg  style="width:32px;"> **ASME B18.2.1.1** UNC square head bolt.

-   <img alt="" src=images/Fasteners_ASMEB18.5.2.svg  style="width:32px;"> **ASME B18.5** UNC Round head square neck bolt.

-   <img alt="" src=images/Fasteners_DIN478.svg  style="width:32px;"> **DIN 478** Square head bolt with collar.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ASMEB18.5.2.svg  style="width:32px;"> **ASME B18.5** UNC Болт с полукруглой головкой и квадратным подголовком.


</div>

-   <img alt="" src=images/Fasteners_ISO2342.svg  style="width:32px;"> **ISO 2342** Headless screw with shank

### Set screws 

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width:32px;"> **ASME B18.3.5A** UNC Винт установочный с шестигранным углублением и плоским концом.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width:32px;"> **ASME B18.3.5B** UNC Винт установочный с шестигранным углублением и коническим концом.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width:32px;"> **ASME B18.3.5C** UNC Винт установочный с шестигранным углублением и цилиндрическим концом.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width:32px;"> **ASME B18.3.5D** UNC Винт установочный с шестигранным углублением и концом с лункой.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width:32px;"> **ISO 4026** **(ГОСТ Р ИСО 4026)** Винт установочный с шестигранным углублением и плоским концом.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width:32px;"> **ISO 4027** **(ГОСТ Р ИСО 4027)** Винт установочный с шестигранным углублением и коническим концом.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width:32px;"> **ISO 4028** **(ГОСТ Р ИСО 4028)** Винт установочный с шестигранным углублением и цилиндрическим концом.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width:32px;"> **ISO 4029** **(ГОСТ Р ИСО 4029)** Винт установочный с шестигранным углублением и концом с лункой.

-   <img alt="" src=images/Fasteners_ISO4766.svg  style="width:32px;"> **ISO 4766** Slotted socket set screw with flat point.

-   <img alt="" src=images/Fasteners_ISO7434.svg  style="width:32px;"> **ISO 7434** Slotted socket set screw with cone point.

-   <img alt="" src=images/Fasteners_ISO7435.svg  style="width:32px;"> **ISO 7435** Slotted socket set screw with long dog point.

-   <img alt="" src=images/Fasteners_ISO7436.svg  style="width:32px;"> **ISO 7436** Slotted socket set screw with cup point.

### Thumb screws 

-   <img alt="" src=images/Fasteners_DIN464.svg  style="width:32px;"> **DIN 464** Knurled thumb screw, high type.

-   <img alt="" src=images/Fasteners_DIN465.svg  style="width:32px;"> **DIN 465** Slotted knurled thumb screw, high type.

-   <img alt="" src=images/Fasteners_DIN653.svg  style="width:32px;"> **DIN 653** Knurled thumb screw, low type.



### Гайки


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width:32px;"> **ASME B18.2.2.1A** UNC Гайка шестигранная общего назначения.


</div>

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1B.svg  style="width:32px;"> **ASME B18.2.2.1B** UNC square machine screw nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.2.svg  style="width:32px;"> **ASME 18.2.2.2** UNC square nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width:32px;"> **ASME B18.2.2.4A** UNC Гайка шестигранная.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width:32px;"> **ASME B18.2.2.4B** UNC Гайка шестигранная низкая.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.5.svg  style="width:32px;"> **ASME 18.2.2.5** UNC hexagon castle nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.12.svg  style="width:32px;"> **ASME 18.2.2.12** UNC hexagon nut with flange.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.13.svg  style="width:32px;"> **ASME 18.2.2.13** UNC hexagon coupling nut.

-   <img alt="" src=images/Fasteners_ASMEB18.6.9A.svg  style="width:32px;"> **ASME 18.6.9A** Wing nut, type A.

-   <img alt="" src=images/Fasteners_DIN315.svg  style="width:32px;"> **DIN 315** Wing nut.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width:32px;"> **DIN 557** **(Ближайший аналог ОСТ 37.001.112)** Гайка квадратная с фаской.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width:32px;"> **DIN 562** **(Ближайший аналог ОСТ 37.001.112)** Гайка квадратная низкая.

-   <img alt="" src=images/Fasteners_DIN917.svg  style="width:32px;"> **DIN 917** **(Ближайший аналог ГОСТ 11860 Исполнение 2)** Гайка колпачковая, низкая.

-   <img alt="" src=images/Fasteners_DIN928.svg  style="width:32px;"> **DIN 928** Square weld nut.

-   <img alt="" src=images/Fasteners_DIN929.svg  style="width:32px;"> **DIN 929** Hexagon weld nut.

-   <img alt="" src=images/Fasteners_DIN934.svg  style="width:32px;"> 
**DIN 934 (superseded by ISO 4035 and ISO 8673)** Hexagon thin nut chamfered. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_DIN935.svg  style="width:32px;"> **DIN 935** Hexagon castle nut.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width:32px;"> **DIN 985** **(Ближайший аналог ГОСТ 50273)** Гайка самоконтрящаяся со стопорным кольцом.

-   <img alt="" src=images/Fasteners_DIN1587.svg  style="width:32px;"> **DIN 1587** **(Ближайший аналог ГОСТ 11860 Исполнение 1)** Гайка колпачковая.

-   <img alt="" src=images/Fasteners_DIN6330.svg  style="width:32px;"> **DIN 6330** Hexagon nut 1.5d high.

-   <img alt="" src=images/Fasteners_DIN6331.svg  style="width:32px;"> **DIN 6331** Hexagon with collar 1.5d high.

-   <img alt="" src=images/Fasteners_DIN6334.svg  style="width:32px;"> **DIN 6334** Hexagon coupling nut.

-   <img alt="" src=images/Fasteners_DIN7967.svg  style="width:32px;"> **DIN 7967** Self-locking counter nut.

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width:32px;"> **EN 1661** **(Ближайший аналог ГОСТ 50592 / ISO 4161 / DIN 6923 )** Гайка шестигранная с фланцем.

-   <img alt="" src=images/Fasteners_GOST11860-1.svg  style="width:32px;"> 
**ГОСТ 11860 (Исполнение 1)** Гайка колпачковая. *Класс точности А.*

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width:32px;"> 
**ISO 4032** **(ГОСТ Р ИСО 4032)** Гайка шестигранная нормальная (тип 1). *Классы точности А и В.*


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width:32px;"> 
**ISO 4033** **(ГОСТ Р ИСО 4033)** Гайка шестигранная высокая (тип 2). *Классы точности А и В.*


</div>

-   <img alt="" src=images/Fasteners_ISO4034.svg  style="width:32px;"> **ISO 4034** Hexagon nut, style 1.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width:32px;"> 
**ISO 4035** **(ГОСТ Р ИСО 4035)** Гайка шестигранная низкая с фаской (тип 0). *Классы точности А и В.*


</div>

-   <img alt="" src=images/Fasteners_ISO4161.svg  style="width:32px;"> **ISO 4161** Hexagon nut with flange.

-   <img alt="" src=images/Fasteners_ISO7040.svg  style="width:32px;"> **ISO 7040** Prevailing torque type hexagon nut (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO7041.svg  style="width:32px;"> **ISO 7041** Prevailing torque type hexagon nut (with non-metallic insert), style 2.

-   <img alt="" src=images/Fasteners_ISO7043.svg  style="width:32px;"> **ISO 7043** Prevailing torque type hexagon nut with flange (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO7044.svg  style="width:32px;"> **ISO 7044** Prevailing torque type all-metal hexagon nut with flange.

-   <img alt="" src=images/Fasteners_ISO7719.svg  style="width:32px;"> **ISO 7719** Prevailing torque type all-metal hexagon nut.

-   <img alt="" src=images/Fasteners_ISO7720.svg  style="width:32px;"> **ISO 7720** Prevailing torque type all-metal hexagon nut, style 2.

-   <img alt="" src=images/Fasteners_ISO8673.svg  style="width:32px;"> 
**ISO 8673** Hexagon nut with fine pitch thread, style 1. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO8674.svg  style="width:32px;"> 
**ISO 8674** Hexagon high nut with fine pitch thread, style 2. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO8675.svg  style="width:32px;"> 
**ISO 8675** Hexagon thin nut with fine pitch thread, style 0. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO10511.svg  style="width:32px;"> **ISO 10511** Prevailing torque type hexagon thin nut (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO10512.svg  style="width:32px;"> **ISO 10512** Prevailing torque type hexagon nut with fine pitch thread (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO10513.svg  style="width:32px;"> **ISO 10513** Prevailing torque type all-metal hexagon nut with fine pitch thread.

-   <img alt="" src=images/Fasteners_ISO10663.svg  style="width:32px;"> **ISO 10663** Hexagon nut with flange and fine pitch thread.

-   <img alt="" src=images/Fasteners_ISO12125.svg  style="width:32px;"> **ISO 12125** Prevailing torque type hexagon nut with flange and fine pitch thread (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO12126.svg  style="width:32px;"> **ISO 12126** Prevailing torque type all-metal hexagon nut with flange and fine pitch thread.

-   <img alt="" src=images/Fasteners_ISO21670.svg  style="width:32px;"> **ISO 21670** Hexagon weld nut with flange.

-   <img alt="" src=images/Fasteners_SAEJ483a1.svg  style="width:32px;"> **SAE J483a 1** Low cap nut.

-   <img alt="" src=images/Fasteners_SAEJ483a2.svg  style="width:32px;"> **SAE J483a 2** High cap nut.

### T-slot fasteners 

-   <img alt="" src=images/Fasteners_DIN508.svg  style="width:32px;"> **DIN 508** Гайка для Т-образных пазов.

-   <img alt="" src=images/Fasteners_GN505.svg  style="width:32px;"> **GN 505** Serrated quarter-turn T-slot nut.

-   <img alt="" src=images/Fasteners_GN505.4.svg  style="width:32px;"> **GN 505.4** Serrated T-slot bolt.

-   <img alt="" src=images/Fasteners_GN506.svg  style="width:32px;"> **GN 506** T-Slot swivel nut.

-   <img alt="" src=images/Fasteners_GN507.svg  style="width:32px;"> **GN 507** T-slot nut.

-   <img alt="" src=images/Fasteners_ISO299.svg  style="width:32px;"> **ISO 299** T-Slot nut.



### Шайбы

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width:32px;"> **ASME B18.21.1.12A** UN Шайба, уменьшенная серия.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width:32px;"> **ASME B18.21.1.12B** UN Шайба, нормальная серия.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width:32px;"> **ASME B18.21.1.12C** UN Шайба, увеличенная серия.

-   <img alt="" src=images/Fasteners_DIN6319C.svg  style="width:32px;"> **DIN 6319C** Spherical washer.

-   <img alt="" src=images/Fasteners_DIN6319D.svg  style="width:32px;"> **DIN 6319D** Conical seat.

-   <img alt="" src=images/Fasteners_DIN6319G.svg  style="width:32px;"> **DIN 6319G** Conical seat.

-   <img alt="" src=images/Fasteners_DIN6340.svg  style="width:32px;"> **DIN 6340** Washer for clamping devices.

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width:32px;"> **ISO 7089** **(Ближайший аналог ГОСТ 11371 Исполнение 1)** Шайба плоская. Нормальная серия. *Класс точности А*.

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width:32px;"> **ISO 7090** **(Ближайший аналог ГОСТ 11371 Исполнение 2)** Шайба плоская с фаской. Нормальная серия. *Класс точности А*.

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width:32px;"> **ISO 7092** **(ГОСТ Р ИСО 7092)** Шайба плоская. Мелкая серия. *Класс точности А*.

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width:32px;"> **ISO 7093-1** **(ГОСТ Р ИСО 7093-1)** Шайба плоская. Крупная серия. *Класс точности А*.

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width:32px;"> **ISO 7094** **(Ближайший аналог ГОСТ 28848)** Шайба плоская. Особо большая. *Класс точности C*.

-   <img alt="" src=images/Fasteners_ISO8738.svg  style="width:32px;"> **ISO 8738** Plain washer for clevis pins.

-   <img alt="" src=images/Fasteners_NFE27-619.svg  style="width:32px;"> **NFE27-619** Шайба-розетка полнотелая для винтов с потайной головкой.

### Rods, taps and dies 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width:32px;"> Метчик произвольного диаметра (с дюймовой резьбой).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width:32px;"> Плашка произвольного диаметра (с дюймовой резьбой).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width:32px;"> **Дюймовая (UNC)** шпилька произвольной длины.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width:32px;"> **DIN 975** шпилька произвольной длины (с метрической резьбой).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width:32px;"> Метчик произвольного диаметра (с метрической резьбой).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width:32px;"> Плашка произвольного диаметра (с метрической резьбой).


</div>




<div class="mw-translate-fuzzy">

### Запрессовочный крепёж и крепёж для Печатных Плат 


</div>

-   <img alt="" src=images/Fasteners_IUTHeatInsert.svg  style="width:32px;"> (Heat staked insert) Резьбовая втулка под горячую запрессовку.

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width:32px;"> (Self-clinching nut) Гайка запрессовочная.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_PEMTHStandoff.svg  style="width:32px;"> (Self-clinching standoff) Втулка запрессовочная полнопроходная резьбовая с шестигранным основанием.


</div>

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width:32px;"> (Self-clinching stud) Шпилька резьбовая запрессовочная.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width:32px;"> (PCB spacer Female/Female) Дистанцирующая стойка для печатных плат.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width:32px;"> (PCB standoff Female/Male) Шестигранная стойка для печатных плат.

-   <img alt="" src=images/Fasteners_4PWTI.svg  style="width:32px;"> 4 prong threaded wood insert (DIN 1624 Tee nuts).

### Retaining rings 

-   <img alt="" src=images/Fasteners_DIN471.svg  style="width:32px;"> **DIN 471** External retaining ring.

-   <img alt="" src=images/Fasteners_DIN472.svg  style="width:32px;"> **DIN 472** Internal retaining ring.

-   <img alt="" src=images/Fasteners_DIN6799.svg  style="width:32px;"> **DIN 6799** E-clip retaining ring.

### Nails

-   <img alt="" src=images/Fasteners_DIN1143.svg  style="width:32px;"> **DIN 1143** Round plain head nail for use in automatic nailing machines.

-   <img alt="" src=images/Fasteners_DIN1144-A.svg  style="width:32px;"> **DIN 1144-A** Nail for the installation of wood wool composite panels, 20mm round head.

-   <img alt="" src=images/Fasteners_DIN1151-A.svg  style="width:32px;"> **DIN 1151-A** Round plain head wire nail.

-   <img alt="" src=images/Fasteners_DIN1151-B.svg  style="width:32px;"> **DIN 1151-B** Round countersunk head wire nail.

-   <img alt="" src=images/Fasteners_DIN1152.svg  style="width:32px;"> **DIN 1152** Round lost head wire nail.

-   <img alt="" src=images/Fasteners_DIN1160-A.svg  style="width:32px;"> **DIN 1160-A** Clout or slate nail.

-   <img alt="" src=images/Fasteners_DIN1160-B.svg  style="width:32px;"> **DIN 1160-B** Clout or slate wide head nail.

### Pins

-   <img alt="" src=images/Fasteners_ISO1234.svg  style="width:32px;"> **ISO 1234** Split pin.

-   <img alt="" src=images/Fasteners_ISO2338.svg  style="width:32px;"> **ISO 2338** Parallel pin.

-   <img alt="" src=images/Fasteners_ISO2339.svg  style="width:32px;"> **ISO 2339** Taper pin.

-   <img alt="" src=images/Fasteners_ISO2340A.svg  style="width:32px;"> **ISO 2340A** Clevis pin.

-   <img alt="" src=images/Fasteners_ISO2340B.svg  style="width:32px;"> **ISO 2340B** Clevis pin without head (with split pin holes).

-   <img alt="" src=images/Fasteners_ISO2341A.svg  style="width:32px;"> **ISO 2341A** Clevis pin with head.

-   <img alt="" src=images/Fasteners_ISO2341B.svg  style="width:32px;"> **ISO 2341B** Clevis pin with head (with split pin hole).

-   <img alt="" src=images/Fasteners_ISO8733.svg  style="width:32px;"> **ISO 8733** Parallel pin with internal thread, unhardened.

-   <img alt="" src=images/Fasteners_ISO8734.svg  style="width:32px;"> **ISO 8734** Dowel pin.

-   <img alt="" src=images/Fasteners_ISO8735.svg  style="width:32px;"> **ISO 8735** Parallel pin with internal thread, hardened.

-   <img alt="" src=images/Fasteners_ISO8736.svg  style="width:32px;"> **ISO 8736** Taper pin with internal thread, unhardened.

-   <img alt="" src=images/Fasteners_ISO8737.svg  style="width:32px;"> **ISO 8737** Taper pin with external thread, unhardened.

-   <img alt="" src=images/Fasteners_ISO8739.svg  style="width:32px;"> **ISO 8739** Full-length grooved pin with pilot.

-   <img alt="" src=images/Fasteners_ISO8740.svg  style="width:32px;"> **ISO 8740** Full-length grooved pin with chamfer.

-   <img alt="" src=images/Fasteners_ISO8741.svg  style="width:32px;"> **ISO 8741** Half-length reverse taper grooved pin.

-   <img alt="" src=images/Fasteners_ISO8742.svg  style="width:32px;"> **ISO 8742** Third-length center grooved pin.

-   <img alt="" src=images/Fasteners_ISO8743.svg  style="width:32px;"> **ISO 8743** Half-length center grooved pin.

-   <img alt="" src=images/Fasteners_ISO8744.svg  style="width:32px;"> **ISO 8744** Full-length taper grooved pin.

-   <img alt="" src=images/Fasteners_ISO8745.svg  style="width:32px;"> **ISO 8745** Half-length taper grooved pin.

-   <img alt="" src=images/Fasteners_ISO8746.svg  style="width:32px;"> **ISO 8746** Grooved pin with round head.

-   <img alt="" src=images/Fasteners_ISO8747.svg  style="width:32px;"> **ISO 8747** Grooved pin with countersunk head.

-   <img alt="" src=images/Fasteners_ISO8748.svg  style="width:32px;"> **ISO 8748** Coiled spring pin, heavy duty.

-   <img alt="" src=images/Fasteners_ISO8750.svg  style="width:32px;"> **ISO 8750** Coiled spring pin, standard duty.

-   <img alt="" src=images/Fasteners_ISO8751.svg  style="width:32px;"> **ISO 8751** Coiled spring pin, light duty.

-   <img alt="" src=images/Fasteners_ISO8752.svg  style="width:32px;"> **ISO 8752** Slotted spring pin, heavy duty.

-   <img alt="" src=images/Fasteners_ISO13337.svg  style="width:32px;"> **ISO 13337** Slotted spring pin, light duty.

## Obsolete


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:32px;"> [Зенкование](Fasteners_ChamferHole/ru.md): Зенковать отверстия (добавить фаску) для крепежа с потайной головкой.


</div>



## Справочные данные 


<div class="mw-translate-fuzzy">

-   Автор: [shaise](http://theseger.com/projects/author/shaise/)
    -   ScrewMaker: Ulrich Brammer
    -   Обертка (wrapper) верстака: Shai Seger
-   Домашняя страница: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Исходный код: <https://github.com/shaise/FreeCAD_FastenersWB>
-   Сообщения об ошибках и запросы: <https://github.com/shaise/FreeCAD_FastenersWB/issues>
-   Тема на форуме: <https://forum.freecadweb.org/viewtopic.php?t=11429>


</div>



## Ссылки


<div class="mw-translate-fuzzy">

-   [Создание отверстий для винтов с потайной головкой в freecad](http://theseger.com/projects/2015/07/generating-holes-for-countersunk-screws-in-freecad/)
-   [BOLTS](https://github.com/jreinhardt/BOLTS): Открытая библиотека технических спецификаций.
-   [Внешние верстаки](External_workbenches/ru.md)
-   [Сборник макросов](Macros_recipes/ru.md)


</div>


{{Fasteners_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [External_Workbenches](Category_External_Workbenches.md) > Fasteners Workbench/ru
