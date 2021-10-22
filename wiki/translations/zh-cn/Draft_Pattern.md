# Draft Pattern/zh-cn
{{TOCright}}

## Description


<div class="mw-translate-fuzzy">

所有的闭合的底图对象，如[矩形](Draft_Rectangle.md)、[圆形](Draft_Circle.md)、[椭圆形](Draft_Ellipse.md)、[连线或](Draft_Wire.md)[多边形](Draft_Polygon.md), 当它们绘制出的是闭合图形并处于\"Flat Lines\"显示模式时，便可以通过设置\"Pattern（图案）\"属性，令指定的图案取代表面颜色填充图形。


</div>

![](images/DraftPatternSample.png ) 
*An ellipse and a polygon with an SVG pattern*

## Usage


<div class="mw-translate-fuzzy">

## 如何使用

1.  选中对象
2.  在Combo View → Data中: 将Make Face项设置为 true，从而确保存在可填充图案的对象面
3.  在Combo View → View → Pattern中: 指定一种待填充的图案
4.  在Combo View → View → Pattern Size中: 指定填充图案的大小


</div>

## Available patterns 

Image:Aluminium.svg\|aluminium Image:Brick01.svg\|brick01 Image:Concrete.svg\|concrete Image:Cross.svg\|cross Image:Cuprous.svg\|cuprous Image:Diagonal1.svg\|diagonal1 Image:Diagonal2.svg\|diagonal2 Image:Earth.svg\|earth Image:General\_steel.svg\|general\_steel Image:Glass.svg\|glass Image:Hatch45L.svg\|hatch45L Image:Hatch45R.svg\|hatch45R Image:Hbone.svg\|hbone Image:Line.svg\|line Image:Plastic.svg\|plastic Image:Plus.svg\|plus Image:Simple.svg\|simple Image:Solid.svg\|solid Image:Square.svg\|square Image:Steel.svg\|steel Image:Titanium.svg\|titanium Image:Wood.svg\|wood Image:Woodgrain.svg\|woodgrain Image:Zinc.svg\|zinc

## Notes

-   SVG patterns are stored in {{FileName|.SVG}} files. It is possible to use your own custom patterns. See [Preferences](#Preferences.md).
-   The patterns themselves are not saved in the FreeCAD document. Objects whose **Pattern** cannot be found are displayed with a solid face color instead.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To specify a directory with addition SVG patterns: **Edit → Preferences... → Draft → Visual settings → Alternate SVG patterns location**. Select a file in the directory and then remove the filename in the preferences input box, leaving only the path. After changing this preference you must restart FreeCAD.
-   The **Edit → Preferences... → Draft → Visual settings → SVG pattern resolution** preference is not used.
-   To change the **Pattern Size** used for new objects: **Edit → Preferences... → Draft → Visual settings → SVG pattern default size**.

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Pattern/zh-cn
