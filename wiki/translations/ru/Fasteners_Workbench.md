# <img alt="Логотип верстака Стандартные изделия (Fasteners)" src=images/Fasteners_workbench_icon.svg  style="width   *64px;"> Fasteners Workbench/ru


{{TOCright}}

## Введение

[Внешний](External_workbenches/ru.md) верстак <img alt="" src=images/Fasteners_workbench_icon.svg  style="width   *24px;"> [Стандартные Изделия (Fasteners)](Fasteners_Workbench/ru.md) позволяет быстро и удобно создавать различные крепёжные изделия а также устанавливать их в посадочные места деталей.

![](images/Fasteners_toolbars.png ) 
*Внешний вид панели инструментов верстака.<br>
Крепёжные изделия с метрическими размерами имеют оранжевые значки.<br>
Крепёжные изделия с дюймовыми размерами имеют зеленые значки.*

## Установка

1.  Установите верстак Fasteners через <img alt="" src=images/AddonManager.svg  style="width   *24px;"> [менеджер дополнений](Std_AddonMgr/ru.md). В случае установки вручную ознакомьтесь с руководством по [установке дополнительных верстаков](Installing_more_workbenches/ru.md).
2.  Перезапустите FreeCAD.
3.  Выберете верстак <img alt="" src=images/Fasteners_workbench_icon.svg  style="width   *24px;"> [Fasteners](Fasteners_Workbench/ru.md) в [в списке доступных верстаков](Std_Workbench/ru.md).
4.  При необходимости настройте панель инструментов и расположение меню   *
    1.  Перейдите в меню   * **Правка → Настройки... → Fasteners → Основные настройки → Toolbar screw icons grouping**.
    2.  Выберите один из доступных вариантов   *
        -   
            **None**
            
               * Все крепежные элементы отображаются на одной панели инструментов. Чтобы просмотреть все доступные изделия, используйте кнопку **&gt;&gt;** чтобы развернуть ее.

        -   
            **Separate toolbars**
            
               * Крепежные элементы сгруппированы на нескольких панелях инструментов. Этот вариант выбран по умолчанию.

        -   
            **Dropdown buttons**
            
               * Крепежные элементы сгруппированы на панелях инструментов.
    3.  Перезапустите FreeCAD.

## Применение

Крепёжные элементы могут быть прикреплены к посадочному месту или не прикреплены. У прикрепленныех крепёжных изделий в свойстве **base Object**, указанно ребро круглой формы к которому прикреплено изделие, следовательно свойство **Placement** динамический связано с этим ребом. Команда <img alt="" src=images/Fasteners_Move.svg  style="width   *16px;"> [Перемещения крепежа](Fasteners_Move/ru.md) может быть использована для прикрепления или отсоединения крепежа.

### Добавление изделий без их крепления к чему либо 

1.  Select the desired fastener by clicking its button or by picking it from the menu.
2.  A fastener is created at the origin.
3.  Optionally change the dimensions and other properties of the fastener   *
    1.  Select the fastener.
    2.  Go to the **Data** tab of the [Property editor](Property_editor.md).
    3.  Change the required properties.

### Добавление изделий с креплением к посадочным местам 

<img alt="" src=images/Fasteners_Attached_Selected.png  style="width   *200px;"> <img alt="" src=images/Fasteners_Attached_Created.png  style="width   *200px;"> 
*Слева в посадочных местах выбрано две грани круглой формы. Справа крепёжные изделия установленны в указанные места.*

1.  Specify if the selected holes are tap holes or pass holes by selecting <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width   *16px;"> [Fasteners MatchTypeInner](Fasteners_MatchTypeInner.md) or <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width   *16px;"> [Fasteners MatchTypeOuter](Fasteners_MatchTypeOuter.md) respectively (not used for countersunk screws).
2.  Select one or more circular edges and/or faces with circular edges. For countersunk screws the top edge of the [chamfered hole](Fasteners_ChamferHole.md) must be selected.
3.  Select the desired fastener by clicking its button or by picking it from the menu.
4.  A fastener is attached to each of the selected circular edges.
5.  The default dimensions of each fastener depend on the radius of the circular edge it is attached to. Countersunk screws are matched by their head diameter, other fasteners are matched by their shaft diameter.
6.  Optionally change the dimensions and other properties of the fasteners. See above.
7.  Fasteners that appear upside-down can be inverted with the <img alt="" src=images/Fasteners_Flip.svg  style="width   *16px;"> [Fasteners Flip](Fasteners_Flip.md) command or by changing their **invert** property.
8.  Optionally change the **offset** property to create space between the fasteners and the edges they are attached to.

## Примечания

-   Если вы хотите, чтобы крепеж имел реалистичную резьбу (по умолчанию при добавлении крепежа резьба на нем не строится) его свойство **thread** должно быть установлено как `True`. Создание такой резьбы поглощает много ресурсов. Перерасчет трехмерного Вида (Recompute) занимает гораздо больше времени, если в документе много крепёжных изделий с реалистичной резьбой.
-   Свойства **invert** и **offset** игнорируются для крепёжных изделий которые не установлены в посадочные места.

## Команды

-   <img alt="" src=images/Fasteners_Flip.svg  style="width   *32px;"> [Перевернуть крепёж](Fasteners_Flip/ru.md)   * Обращает ориентацию уже установленного крепежа на противоположную.

-   <img alt="" src=images/Fasteners_Move.svg  style="width   *32px;"> [Переместить крепёж](Fasteners_Move/ru.md)   * Перемещает и устанавливает крепёж в указанную грань круглой формы. Может также использоваться для отсоединения крепёжа.

-   <img alt="" src=images/Fasteners_Shape.svg  style="width   *32px;"> [Создать непараметрическую копию](Fasteners_Shape/ru.md)   * Создает непараметрическую копию объекта (стандартного изделия).

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width   *32px;"> [Match for tap hole (Установить винты/болты в указанные места)](Fasteners_MatchTypeInner/ru.md)   * По диаметру выбранных ребер отверстий, автоматический подбирает крепёж по размеру в соответствии со стандартами и прикрепляет его к этим посадочным местам.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width   *32px;"> [Match screws by outer thread diameter (Pass hole)](Fasteners_MatchTypeOuter.md)   * подобрать резьбу по диаметру внутренний резьбы (отверстия под метчик).


</div>

-   <img alt="" src=images/Fasteners_BOM.svg  style="width   *32px;"> [Спецификация](Fasteners_BOM/ru.md)   * Создает электронную таблицу со спецификацией крепежных элементов имеющихся в документе.

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width   *32px;"> [Калькулятор отверстия под резьбу](Fasteners_ScrewCalculator/ru.md)   * Открывает калькулятор для определения размера отверстия под резьбу определенного диаметра.

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width   *32px;"> [Зенкование](Fasteners_ChamferHole/ru.md)   * Зенковать отверстия (добавить фаску) для крепежа с потайной головкой.

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width   *32px;"> [Изменить параметры крепежа](Fasteners_ChangeParameters/ru.md)   * Изменить параметры стандартных изделий.

## Крепёжные изделия 

Крепёжные изделия с метрическими размерами имеют оранжевые значки. Крепёжные изделия с дюймовыми размерами имеют зеленые значки.

### Запрессовочный крепёж и крепёж для Печатных Плат 

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width   *32px;"> (Self-clinching nut) Гайка запрессовочная.

-   <img alt="" src=images/Fasteners_PEMTHStandoff.svg  style="width   *32px;"> (Self-clinching standoff) Втулка запрессовочная полнопроходная резьбовая с шестигранным основанием.

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width   *32px;"> (Self-clinching stud) Шпилька резьбовая запрессовочная.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width   *32px;"> (PCB standoff Female/Male) Шестигранная стойка для печатных плат.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width   *32px;"> (PCB spacer Female/Female) Дистанцирующая стойка для печатных плат.

-   <img alt="" src=images/Fasteners_IUTHeatInsert.svg  style="width   *32px;"> (Heat staked insert) Резьбовая втулка под горячую запрессовку.

### Винты и болты с шестигранной головкой 

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width   *32px;"> 
**ISO 4017** **(ГОСТ Р ИСО 4017)** Винт с шестигранной головкой. *Классы точности А и В.*

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width   *32px;"> 
**ISO 4014** **(ГОСТ Р ИСО 4014)** Болт с шестигранной головкой. *Классы точности А и В.*

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width   *32px;"> **EN 1662** Болт с шестигранной головкой и фланцем, легкая серия.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width   *32px;"> **EN 1665** Болт с шестигранной головкой и фланцем, тяжёлая серия.

-   <img alt="" src=images/Fasteners_DIN571.svg  style="width   *32px;"> **DIN 571** **(Ближайший аналог ГОСТ 11473)** Шуруп с шестигранной головкой (для дерева).

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width   *32px;"> **ASME B18.2.1.6** UNC Винт с шестигранной головкой.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width   *32px;"> **ASME B18.2.1.8** UNC Винт с шестигранной головкой и фланцем.

### Винты шестигранным углублением под ключ 

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width   *32px;"> **ISO 4762** **(ГОСТ Р ИСО 4762)** Винт с цилиндрической головкой и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width   *32px;"> **DIN 7984** Винт с цилиндрической головкой уменьшенной высоты и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width   *32px;"> **DIN 6912** Винт с цилиндрической головкой уменьшенной высоты и шестигранным углублением под ключ с центрирующим отверстием.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width   *32px;"> **ISO 7380-1** **(ГОСТ Р ИСО 7380-1)** Винт с полукруглой головкой и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width   *32px;"> **ISO 7380-2** **(ГОСТ Р ИСО 7380-2)** Винт с полукруглой головкой с буртом и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width   *32px;"> **ISO 10642** **(ГОСТ Р ИСО 10642)** Винт с потайной головкой и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width   *32px;"> **ISO 7379** **(Ближайший аналог ГОСТ 28962)** Винт с внутренним шестигранником в головке и утолщенным стержнем.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width   *32px;"> **ISO 4026** **(ГОСТ Р ИСО 4026)** Винт установочный с шестигранным углублением и плоским концом.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width   *32px;"> **ISO 4027** **(ГОСТ Р ИСО 4027)** Винт установочный с шестигранным углублением и коническим концом.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width   *32px;"> **ISO 4028** **(ГОСТ Р ИСО 4028)** Винт установочный с шестигранным углублением и цилиндрическим концом.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width   *32px;"> **ISO 4029** **(ГОСТ Р ИСО 4029)** Винт установочный с шестигранным углублением и концом с лункой.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width   *32px;"> **ASME B18.3.1A** UNC Винт с цилиндрической головкой и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1G.svg  style="width   *32px;"> **ASME B18.3.1G** UNC Винт с цилиндрической головкой уменьшенной высоты и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width   *32px;"> **ASME B18.3.2** UNC Винт с потайной головкой и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width   *32px;"> **ASME B18.3.3A** UNC Винт с полукруглой головкой и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width   *32px;"> **ASME B18.3.3B** UNC Винт с полукруглой головкой с буртом и шестигранным углублением под ключ.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width   *32px;"> **ASME B18.3.4** UNC Винт с внутренним шестигранником в головке и утолщенным стержнем.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width   *32px;"> **ASME B18.3.5A** UNC Винт установочный с шестигранным углублением и плоским концом.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width   *32px;"> **ASME B18.3.5B** UNC Винт установочный с шестигранным углублением и коническим концом.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width   *32px;"> **ASME B18.3.5C** UNC Винт установочный с шестигранным углублением и цилиндрическим концом.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width   *32px;"> **ASME B18.3.5D** UNC Винт установочный с шестигранным углублением и концом с лункой.

### Винты звездообразным углублением под ключ 

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width   *32px;"> **ISO 14579** **(ГОСТ Р ИСО 14579)** Винт с цилиндрической головкой и звездообразным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width   *32px;"> **ISO 14580** **(ГОСТ Р ИСО 14580)** Винт с низкой цилиндрической головкой и звездообразным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width   *32px;"> **ISO 14582** **(ГОСТ Р ИСО 14582)** Винт с высокой потайной головкой и звездообразным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width   *32px;"> **ISO 14583** **(ГОСТ Р ИСО 14583)** Винт со скругленной головкой и звездообразным углублением под ключ.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width   *32px;"> **ISO 14584** **(ГОСТ Р ИСО 14584)** Винт с полупотайной головкой и звездообразным углублением под ключ.

### Винты с прямым шлицем 

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width   *32px;"> **ISO 2009** **(ГОСТ Р ИСО 2009)** Винт с потайной головкой и прямым шлицем. *Класс точности А*.

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width   *32px;"> 
**ISO 2010** **(ГОСТ Р ИСО 2010)** Винт с полупотайной головкой со шлицем. *Класс точности А.*

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width   *32px;"> 
**ISO 1580** **(ГОСТ Р ИСО 1580)** Винт с плоской головкой со шлицем. *Класс точности А.*

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width   *32px;"> 
**ISO 1207** **(ГОСТ Р ИСО 1580)** Винт с низкой цилиндрической головкой со шлицем. *Класс точности А.*

-   <img alt="" src=images/Fasteners_DIN96.svg  style="width   *32px;"> **DIN 96** Slotted half round head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-1.svg  style="width   *32px;"> **GOST 1144-1** Slotted half round head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-2.svg  style="width   *32px;"> **GOST 1144-2** Slotted half round head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width   *32px;"> **ASME B18.6.3.1A** UNC Винт с потайной головкой и прямым шлицем.

### Винты с крестообразным шлицем 

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width   *32px;"> **DIN 967** **(Ближайший аналог ГОСТ 11644)** Винт с полукруглой головкой, буртом и крестообразным шлицем.

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width   *32px;"> 
**ISO 7045** **(ГОСТ Р ИСО 7045)** Винт со скругленной головкой и крестообразным шлицем типа Н. *Класс точности А.*

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width   *32px;"> 
**ISO 7046** **(ГОСТ Р ИСО 7046 две части)** Винт с потайной головкой и крестообразным шлицем типа Н. *Класс точности А.*

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width   *32px;"> 
**ISO 7047** **(ГОСТ Р ИСО 7047)** Винт с полупотайной головкой и крестообразным шлицем типа H. *Класс точности А.*

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width   *32px;"> **ISO 7048** **(ГОСТ Р ИСО 7048)** Винт с низкой цилиндрической головкой и крестообразным шлицем.

### Болты с другими головками 

-   <img alt="" src=images/Fasteners_ASMEB18.5.2.svg  style="width   *32px;"> **ASME B18.5** UNC Болт с полукруглой головкой и квадратным подголовком.

### Гайки

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width   *32px;"> 
**ISO 4032** **(ГОСТ Р ИСО 4032)** Гайка шестигранная нормальная (тип 1). *Классы точности А и В.*

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width   *32px;"> 
**ISO 4033** **(ГОСТ Р ИСО 4033)** Гайка шестигранная высокая (тип 2). *Классы точности А и В.*

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width   *32px;"> 
**ISO 4035** **(ГОСТ Р ИСО 4033)** Гайка шестигранная низкая с фаской (тип 0). *Классы точности А и В.*

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width   *32px;"> **EN 1661** Гайка шестигранная с фланцем.

-   <img alt="" src=images/Fasteners_DIN917.svg  style="width   *32px;"> **DIN 917** **(Ближайший аналог ГОСТ 11860 Исполнение 2)** Гайка колпачковая, низкая.

-   <img alt="" src=images/Fasteners_DIN1587.svg  style="width   *32px;"> **DIN 1587** **(Ближайший аналог ГОСТ 11860 Исполнение 1)** Гайка колпачковая.

-   <img alt="" src=images/Fasteners_GOST11860-1.svg  style="width   *32px;"> **GOST 11860-1** Cap nut.

-   <img alt="" src=images/Fasteners_DIN508.svg  style="width   *32px;"> **DIN 508** T-slot nut.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width   *32px;"> **DIN 557** Гайка квадратная с фаской.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width   *32px;"> **DIN 562** Гайка квадратная низкая.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width   *32px;"> **DIN 985** **(Ближайший аналог ГОСТ 50273)** Гайка самоконтрящаяся со стопорным кольцом.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width   *32px;"> **ASME B18.2.2.1A** UNC Гайка шестигранная общего назначения.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width   *32px;"> **ASME B18.2.2.4A** UNC Гайка шестигранная.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width   *32px;"> **ASME B18.2.2.4B** UNC Гайка шестигранная низкая.

### Шайбы

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width   *32px;"> **ISO 7089** **(Ближайший аналог ГОСТ 11371 Исполнение 1)** Шайба плоская. Нормальная серия. *Класс точности А*.

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width   *32px;"> **ISO 7090** **(Ближайший аналог ГОСТ 11371 Исполнение 2)** Шайба плоская с фаской. Нормальная серия. *Класс точности А*.

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width   *32px;"> **ISO 7092** **(ГОСТ Р ИСО 7092)** Шайба плоская. Мелкая серия. *Класс точности А*.

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width   *32px;"> **ISO 7093-1** **(ГОСТ Р ИСО 7093-1)** Шайба плоская. Крупная серия. *Класс точности А*.

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width   *32px;"> **ISO 7094** Шайба плоская. Особо крупная серия. *Класс точности C*.

-   <img alt="" src=images/Fasteners_NFE27-619.svg  style="width   *32px;"> **NFE27-619** Шайба-розетка полнотелая для винтов с потайной головкой.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width   *32px;"> **ASME B18.21.1.12A** UN Шайба, уменьшенная серия.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width   *32px;"> **ASME B18.21.1.12B** UN Шайба, нормальная серия.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width   *32px;"> **ASME B18.21.1.12C** UN Шайба, увеличенная серия.

### Другие изделия 

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width   *32px;"> Метчик произвольного диаметра (с метрической резьбой).

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width   *32px;"> Метчик произвольного диаметра (с дюймовой резьбой).

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width   *32px;"> Плашка произвольного диаметра (с метрической резьбой).

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width   *32px;"> Плашка произвольного диаметра (с дюймовой резьбой).

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width   *32px;"> **DIN 975** шпилька произвольной длины (с метрической резьбой).

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width   *32px;"> **Дюймовая (UNC)** шпилька произвольной длины.

## Справочные данные 

-   Автор   * [shaise](http   *//theseger.com/projects/author/shaise/)
    -   ScrewMaker   * Ulrich Brammer
    -   Обертка (wrapper) верстака   * Shai Seger
-   Домашняя страница   * <http   *//theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Исходный код   * <https   *//github.com/shaise/FreeCAD_FastenersWB>
-   Сообщения об ошибках и запросы   * <https   *//github.com/shaise/FreeCAD_FastenersWB/issues>
-   Тема на форуме   * <https   *//forum.freecadweb.org/viewtopic.php?t=11429>

## Ссылки

-   [Создание отверстий для винтов с потайной головкой в freecad](http   *//theseger.com/projects/2015/07/generating-holes-for-countersunk-screws-in-freecad/)
-   [BOLTS](https   *//github.com/jreinhardt/BOLTS)   * Открытая библиотека технических спецификаций.
-   [Внешние верстаки](External_workbenches/ru.md)
-   [Сборник макросов](Macros_recipes/ru.md)



[Category   *Addons](Category_Addons.md) [Category   *External Command Reference](Category_External_Command_Reference.md) [Category   *External Workbenches](Category_External_Workbenches.md) [Category   *Fasteners](Category_Fasteners.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > [External Workbenches](Category_External Workbenches.md) > [Fasteners](Category_Fasteners.md) > Fasteners Workbench/ru
