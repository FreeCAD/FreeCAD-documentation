---
 GuiCommand:
   Name/ru: Выдавливание
   Name: PartDesign_Pad
   MenuLocation: Part Design , Аддитивные преобразования , Выдавливание
   Workbenches: PartDesign_Workbench/ru
   SeeAlso: PartDesign_Pocket/ru
---

# PartDesign Pad/ru



## Описание

Инструмент **Выдавливание** вытягивает эскиз или грань твёрдого тела по прямой траектории.

![](images/PartDesign_Pad_example.svg )

*Эскиз (А) показан слева; конечный результат после операции выдавливания (B) справа.*



## Применение


<div class="mw-translate-fuzzy">

1.  Выберите один эскиз или грань для выдавливания. {{Version/ru|0.20}}: Можно также выбрать несколько эскизов или граней.
2.  Нажмите кнопку **<img src="images/PartDesign_Pad.svg" width=16px> [Выдавливание](PartDesign_Pad/ru.md)**.
3.  Установите параметры Выдавливания, смотрите [Опции](#Options.md) ниже.
4.  Нажмите **OK**.


</div>



## Опции


<div class="mw-translate-fuzzy">

Когда производится выдавливание, появляется диалоговое окно **Параметры выдавливания**. Оно предлагает следующие настройки:


</div>


<div class="mw-translate-fuzzy">

![](images/pad_parameters_cropped.png )


</div>



### Тип


<div class="mw-translate-fuzzy">

Тип предлагает пять различных способов задания протяжённости выдавливания:


</div>



#### Размер

Enter a numeric value for the **Length** of the pad. With the option **Symmetric to plane** the pad will extend half the given length to either side of the sketch or face.



#### К последнему 

The pad will extend up to the last face of the support it encounters in its direction. If there is no support, an error message will appear.



#### К первому 


<div class="mw-translate-fuzzy">

Контур будет выдавлен до первой встречной грани детали в направлении выдавливания. Если такая грань не будет обнаружена, появится сообщение об ошибке.


</div>



#### До грани 

The pad will extend up to a face. Press the **Select face** button and select a face or a [datum plane](PartDesign_Plane.md) from the Body.



#### Два размера 

This allows to enter a second length in which the pad should extend in the opposite direction. The directions can be switched by checking the **Reversed** option.

#### Up to shape 


<small>(v1.0)</small> 

: The pad will extend up to the selected shape. Optionally press the **Select shape** button and select a shape. Leave the **Select all faces** checkbox enabled or disable it, press the **Select faces** button and select the faces up to which the pad should be created.



### Смещение к грани 

Offset from face at which the pad will end. This option is only available if **Type** is **To last**, **To first** or **Up to face**.



### Длина

Defines the length of the pad. This option is only available if **Type** is **Dimension** or **Two dimensions**. The length is measured along the direction vector, or along the normal of the sketch or face. Negative values are not possible. Use the **Reversed** option instead.



### 2-я длина 

Defines the length of the pad in the opposite direction. This option is only available if **Type** is **Two dimensions**.



### Симметрично плоскости 

Check this option to extrude half the given length to either side of the sketch or face. This option is only available if **Type** is **Dimension**.



### В обратную сторону 

Меняет направление выдавливания на противоположное.



### Направление



#### Направление/ребро

Вы можете выбрать направление экструзии:

-   **Sketch normal** or **Face normal:** The sketch or face is extruded in the direction of its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used.
-   **Select reference\...:** The sketch or face is extruded in the direction of a straight edge or a [datum line](PartDesign_Line.md) selected from the Body.
-   **Custom direction:** The sketch or face is extruded in the direction of the specified vector.



#### Показать направление 

If checked, the pad direction will be shown. In case the pad uses a **Custom direction**, it can be changed.



#### Длина вдоль нормали эскиза 

If checked, the pad length is measured along the sketch or face normal, otherwise along the custom direction.



### Угол сужения 

Tapers the pad in the extrusion direction by the given angle. A positive angle means the outer pad border gets wider. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts. This option is only available if **Type** is **Dimension** or **Two dimensions**.



### 2-й угол сужения 

Tapers the pad in the opposite extrusion direction by the given angle. See **Taper angle**. This option is only available if **Type** is **Two dimensions**.



## Свойства

### Data


{{TitleProperty|Pad}}

-    **Type|Enumeration**: Defines how the pad will be extruded, see [Options](#Options.md).

-    **Length|Length**: Defines the length of the pad, see [Options](#Options.md).

-    **Length2|Length**: Second pad length in case the **Type** is **TwoLengths**, see [Options](#Options.md).

-    **Use Custom Vector|Bool**: If checked, the pad direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction|Vector**: Vector of the pad direction if **Use Custom Vector** is used.

-    **Reference Axis|LinkSub**
    

-    **Along Sketch Normal|Bool**: If *true*, the pad length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face|LinkSub**: A face the pad will extrude up to, see [Options](#Options.md).

-    **Offset|Length**: Offset from face in which the pad will end. This is only taken into account if the **Type** option **UpToLast**, **UpToFirst** or **UpToFace** is used.

-    **Taper Angle|Angle**
    

-    **Taper Angle2|Angle**
    


{{TitleProperty|Part Design}}

-    **Refine|Bool**: True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part Design → General → Model settings**).


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    



## Ограничения


<div class="mw-translate-fuzzy">

-   Как и все элементы Part Design, Выдавливание создает твёрдое тело, поэтому эскиз должен содержать замкнутый профиль, иначе произойдет сбой с ошибкой *Failed to validate broken face*.
-   Алгоритм, используемый для выдавливания **К первому** и **К последнему**:
    -   Создаёт линию через центр эскиза
    -   Находит все грани твёрдого тела, разрезанные этой линией.
    -   Выбирает грань, в которой точка пересечения находится ближе/дальше всего от эскиза

:   Это означает, что найденная грань может быть не всегда такой, которую вы ожидали. Если вы столкнулись с этой проблемой, используйте вместо этого тип **До грани** и выберите нужную грань.
:   Для особого случая выдавливания на вогнутую поверхность, где эскиз больше этой поверхности, выдавливание не выполняется. Это неразрешенная ошибка.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/ru
