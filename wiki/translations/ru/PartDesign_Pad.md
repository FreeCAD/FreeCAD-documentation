---
- GuiCommand   */ru
   Name/ru   *Выдавливание
   Name   *PartDesign_Pad
   MenuLocation   *Part Design → Аддитивные преобразования → Выдавливание
   Workbenches   *[PartDesign](PartDesign_Workbench/ru.md)
   SeeAlso   *[Вырез](PartDesign_Pocket/ru.md)
---

# PartDesign Pad/ru

## Описание

Инструмент **Выдавливание** вытягивает эскиз или грань твёрдого тела по прямой траектории.

![](images/PartDesign_Pad_example.svg )

*Эскиз (А) показан слева; конечный результат после операции выдавливания (B) справа.*

## Применение

1.  Выберите один эскиз или грань для выдавливания. {{Version/ru|0.20}}   * Можно также выбрать несколько эскизов или граней.
2.  Нажмите кнопку **<img src="images/PartDesign_Pad.svg" width=16px> [Выдавливание](PartDesign_Pad/ru.md)**.
3.  Установите параметры Выдавливания, смотрите [Опции](#Options.md) ниже.
4.  Нажмите **OK**.

При выборе одного эскиза он может иметь несколько замкнутых профилей внутри большего, например прямоугольник с двумя окружностями внутри. Но профили могут не пересекаться друг с другом. {{Version/ru|0.20}}

## Опции

When creating a pad, the **Pad parameters** dialog will be shown. It offers the following settings   *

![](images/pad_parameters_cropped.png )

### Тип

Тип предлагает пять различных способов задания протяжённости выдавливания   *

#### Размер

Enter a numeric value for the length of the pad. The default direction for extrusion is away (outside of) the support, but it can be changed by ticking the **Reversed** option. Extrusions occur by default [normal](http   *//en.wikipedia.org/wiki/Surface_normal) to the defining sketch plane. This can be changed by specifying another **Direction**. With the option **Symmetric to plane** the pad will extend half of the given length to either side of the plane. Negative dimensions are not possible. Use the **Reversed** option instead.

#### К последнему 

The pad will extrude up to the last face of the support in the extrusion direction. If there is no support, an error message will appear.

#### К первому 

Контур будет выдавлен до первой встречной грани детали в направлении выдавливания. Если такая грань не будет обнаружена, появится сообщение об ошибке.

#### До грани 

The pad will extrude up to a face in the model that can be chosen by clicking on it.

#### Два размера 

This allows to enter a second length in which the pad should extend in the opposite direction (into the support). The directions can be switched by ticking the **Reversed** option.

### Длина

Defines the length of the pad. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available when **Type** is either **Dimension** or **Two dimensions**.

### Смещение к грани 

Offset from face at which the pad will end. This option is only available when **Type** is either **To last**, **To first** or **Up to face**.

### Направление

#### Direction/edge

You can select the direction of the extrusion   *

-   **Sketch normal** The sketch or face is extruded along its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used. <small>(v0.20)</small> 
-   **Select reference\...** The sketch is extruded along an edge of the 3D model. When this is method selected, you can click on any edge in the 3D model and it becomes the direction vector for the extrusion. <small>(v0.20)</small> 
-   **Custom direction** The sketch is extruded along a direction that can be specified via vector values. <small>(v0.19)</small> 

#### Show direction 

If checked, the pad direction will be shown. In case the pad uses a **Custom direction**, it can be changed. <small>(v0.20)</small> 

#### Length along sketch normal 

If checked, the pad length is measured along the sketch normal, otherwise along the custom direction. <small>(v0.20)</small> 

### Симметрично плоскости 

Tick the checkbox to extrude half of the given length to either side of the sketch or plane.

### Reversed

Reverses the direction of the pad.

### Taper angle 


<small>(v0.20)</small> 

Tapers the pad in the extrusion direction by the given angle. A positive angle means the outer pad border gets wider. This option is only available if **Type** is either **Dimension** or **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

Limitations   *

-   Sketches containing [B-Splines](B-Splines.md) often cannot be properly tapered. This is a limitation of the [OpenCASCADE](OpenCASCADE.md) kernel that FreeCAD uses.
-   For larger angles tapering will fail if the end face of the pad would have fewer edges than the start face/sketch.

### 2nd length 

Defines the length of the pad in the opposite extrusion direction. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available if **Type** is **Two dimensions**.

### 2nd taper angle 


{{Version/ru|0.20}}

Tapers the pad in the opposite extrusion direction by the given angle. A positive angle means the outer pad border gets wider. This option is only available if **Type** is **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

## Свойства

-    **Type**   * Type of ways how the pad will be extruded, see [Options](#Options.md).

-    **Length**   * Defines the length of the pad, see [Options](#Options.md).

-    **Length2**   * Second pad length in case the **Type** is **TwoLengths**, see [Options](#Options.md).

-    **Use Custom Vector**   * <small>(v0.19)</small>  If checked, the pad direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction**   * <small>(v0.19)</small>  Vector of the pad direction if **Use Custom Vector** is used.

-    **Along Sketch Normal**   * <small>(v0.20)</small>  If *true*, the pad length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face**   * A face the pad will extrude up to, see [Options](#Options.md).

-    **Offset**   * Offset from face in which the pad will end. This is only taken into account if the **Type** option **UpToLast**, **UpToFirst** or **UpToFace** is used.

-    **Refine**   * True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part design → General → Model settings**). It can be manually changed afterwards. This property will be saved with the FreeCAD document.

## Ограничения

-   Как и все элементы Part Design, Выдавливание создает твёрдое тело, поэтому эскиз должен содержать замкнутый профиль, иначе произойдет сбой с ошибкой *Failed to validate broken face*.
-   Алгоритм, используемый для **К первому** и **К Последнему**   *
    -   Создаёт линию через центр эскиза
    -   Находит все грани твёрдого тела, разрезанные этой линией.
    -   Выбирает грань, в которой точка пересечения находится ближе/дальше всего от эскиза

   *   Это означает, что найденная грань может быть не всегда такой, которую вы ожидали. Если вы столкнулись с этой проблемой, используйте вместо этого тип **До грани** и выберите нужную грань.
   *   Для особого случая выдавливания на вогнутую поверхность, где эскиз больше этой поверхности, выдавливание не выполняется. Это неразрешенная ошибка.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/ru
