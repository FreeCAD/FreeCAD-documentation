---
- GuiCommand:/tr
   Name:Draft ShapeString
   Name/tr:Şekil dizesi
   MenuLocation:Taslak → Şekil dizesi
   Workbenches:[Taslak](Draft_Workbench/tr.md), [Yapı](Arch_Workbench/tr.md)
   Shortcut:**S** **S**
   Version:0.14
   SeeAlso:[Metin](Draft_Text/tr.md), [Parça çıkarma](Part_Extrude/tr.md),<br /> [Macro Fonts Win10 PYMP](Macro_Fonts_Win10_PYMP/tr.md) <img src="images/Macro_Fonts_Win10_PYMP.png" width=24px>
---

# Draft ShapeString/tr


</div>

## Tanım


<div class="mw-translate-fuzzy">

Şekil dizesi aracı, bir metin dizesini temsil eden bir bileşik şekil ekler. Metin yüksekliği, ara boşluk ve yazı tipi belirtilebilir. Ortaya çıkan şekil, 3D harfler oluşturmak için [Parça çıkarma](Part_Extrude/tr.md) aracıyla kullanılabilir.


</div>


<div class="mw-translate-fuzzy">

Kapalı bir şekil olmadan daha basit bir metin elemanı eklemek için [Taslak Metin](Draft_Text/tr.md) kullanın. Bir yönlendirici ve bir ok içeren bir metin etiketi oluşturmak için [Taslak Etiket](Draft_Label/tr.md) kullanın.


</div>

![](images/Draft_ShapeString_Example400.png )


<div class="mw-translate-fuzzy">


{{Caption | Şekil dizesini konumlandırmak için tek nokta gerekli}}


</div>


<div class="mw-translate-fuzzy">

## Nasıl Kullanılır 


</div>

For Windows users: please read the [Font file selection on Windows](#Font_file_selection_on_Windows.md) paragraph first.

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_ShapeString.svg" width=16px> [Draft ShapeString](Draft_ShapeString.md)** button.
    -   Select the **Drafting → <img src="images/Draft_ShapeString.svg" width=16px> Shape from text** option from the menu.
2.  The **ShapeString** task panel opens.
3.  Click a point in the [3D view](3D_view.md), or type coordinates.
4.  Optionally press the **Reset Point** button to reset the point to the origin.
5.  Enter a **String**.
6.  Specify the **Height**.
7.  To select a font do one of the following:
    -   Enter a file path in the **Font file** input box.
    -   Press the **...** button and select a file.
8.  Press the **OK** button to finish the command.

## Seçenekler


<div class="mw-translate-fuzzy">

-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında {{KEY | Enter}} tuşuna basın. Noktayı eklemek istediğiniz değerlere sahipseniz {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basabilirsiniz.
-   Geçerli komutu iptal etmek için {{KEY | Esc}} veya {{Button | Close}} düğmesine basınız.


</div>

## Notes


<div class="mw-translate-fuzzy">

### Sınırlamalar

-   Çok küçük metin yükseklikleri, ölçeklemede ayrıntı kaybı nedeniyle deforme karakter şekillerine neden olabilir.
-   Mevcut sürüm, soldan sağa yazma ile sınırlıdır.
-   Dairesel biçimde düzenlenmiş metin oluşturmak için ![ 24px](images/_FCCircularTextButtom.png ) [Macro FCCircularText](Macro_FCCircularText/tr.md) kullanın.


</div>

## Font file selection on Windows 

On Windows access to the default font folder is restricted. This affects the font file selection for ShapeStrings. There are three cases in FreeCAD where a font file for ShapeStrings can be specified: in the ShapeString task panel, when changing the **Font File** property of a ShapeString, and when specifying the default font file in the [Draft Preferences](Draft_Preferences#Texts_and_dimensions.md).

Pressing the **...** button and then selecting a file from the default Windows font folder is not possible when using the native file dialog. There are a number of workarounds:

-   Make sure **DontUseNativeFontDialog** is set to {{True}}, which is the default value for this preference. This will only call a different, non-native, file dialog when pressing the **...** button in the ShapeString task panel. With this file dialog the default Windows font folder can be accessed.
-   Change **DontUseNativeDialog** to {{True}}. This instructs FreeCAD to always use the non-native file dialog.
-   Specify the font file in the input box. You can of course type the full path or copy-paste the path from the Windows File Explorer. But there is also another way to enter the path. If you enter {{Value|C:\}} a dropdown list will appear. Select {{Value|Windows}} from that list and add {{Value|\F}}. Select {{Value|Fonts}} from the new dropdown list. Finally add {{Value|\}} and the first letter(s) of the font file, and then select it from the dropdown list.
-   Create a custom folder for your font files.

See the [Preferences](#Preferences.md) paragraph below for the location of the mentioned preferences.


<div class="mw-translate-fuzzy">

## Kılavuzlar

-   [Taslak Şekil dizesi kılavuzu](Draft_ShapeString_tutorial/tr.md): Bir Şekil dizesi\'i çıkarın, 3D alanda yerleştirin ve başka bir gövdede bir gravür oluşturun.


</div>

-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md): extrude a ShapeString, position it in 3D space, and create an engraving in another body.
-   [How to use ShapeStrings in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623)

## Preferences

See also: [Preferences Editor](Preferences_Editor.md), [Draft Preferences](Draft_Preferences.md) and [Std DlgParameter](Std_DlgParameter.md).

-   The default font file can be changed in the preferences: **Edit → Preferences... → Draft → Texts and dimensions → Default ShapeString font file**.
-   For Windows users:
    -   Set **Tools → Edit parameters... → BaseApp → Preferences → Dialog → DontUseNativeFontDialog** to {{True}} to use the non-native file dialog when selecting a font file from the ShapeString task panel.
    -   Alternatively, set **Tools → Edit parameters... → BaseApp → Preferences → Dialog → DontUseNativeDialog** to {{True}} to always use the non-native file dialog.

## Özellikler

See also: [Property editor](Property_editor.md).

A Draft ShapeString object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    {{PropertyData | Position}}: bileşik şeklin taban noktasının konumunu belirtir.

-    {{PropertyData | Angle}}: şeklin taban çizgisinin dönüşünü belirtir.

-    {{PropertyData | Axis}}: döndürme için kullanılacak ekseni belirtir.

-    {{PropertyData | String}}: görüntülenecek metin dizesini belirtir; [Taslak Metin](Draft_Text/tr.md) aracından farklı olarak, [Taslak Şekil dizesi](Draft_ShapeString/tr.md) yalnızca tek bir satır görüntüleyebilir.

-    {{PropertyData | Size}}: harflerin genel yüksekliğini belirtir.

-    {{PropertyData | Tracking}}: dizedeki karakterler arası ek boşluğu belirtir.

-    {{PropertyData | Font File}}: dizeyi çizmek için kullanılan font dosyasının tam yolunu belirtir.


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the faces of the text. This property only works if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Şekil dizesi aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```


<div class="mw-translate-fuzzy">

-   Belirtilen {{incode | String}} ve desteklenen bir {{incode | FontFile}} tam yolunu kullanarak bir {{incode | ShapeString}} bileşik şekli oluşturur.

-    {{incode | Size}}sonuçta elde edilen metnin milimetre cinsinden yüksekliğidir.

-    {{incode | Tracking}}milimetre cinsinden karakterler arası ek boşluktır.


</div>

Şekil dizesi\'in yerleşimi, {{incode | Placement}} özniteliğinin üzerine yazarak veya {{incode | Placement.Base}} ve {{incode | Placement.Rotation}} özniteliklerinin üzerine yazılarak değiştirilebilir.

Örnek:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

font1 = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
font2 = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
font3 = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

S1 = Draft.make_shapestring("This is a sample text", font1, 200)

S2 = Draft.make_shapestring("Inclined text", font2, 200, 10)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(-1000, 500, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 45))
S2.Placement = place2

S3 = Draft.make_shapestring("Upside-down text", font3, 200, 10)
S3.Placement.Base = App.Vector(0, -1000, 0)
S3.Placement.Rotation = App.Rotation(zaxis, 180)

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ShapeString/tr
