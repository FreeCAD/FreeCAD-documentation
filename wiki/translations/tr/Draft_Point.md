---
- GuiCommand:/tr
   Name:Draft Point
   Name/tr:Nokta
   MenuLocation:Taslak → Nokta
   Workbenches:[Taslak](Draft_Workbench/tr.md), [Yapı](Arch_Workbench/tr.md)
   Shortcut:P T
   SeeAlso:[Çizgi](Draft_Line/tr.md), [Tel](Draft_Wire/tr.md)
   Version:0.17
---

# Draft Point/tr


</div>



## Tanım


<div class="mw-translate-fuzzy">

Nokta aracı, geçerli [Çalışma düzlemi](Draft_SelectPlane/tr.md) içinde basit bir nokta yaratır, daha sonra başka nesnelerin yerleştirilmesi için referans olarak kullanılmaya elverişlidir. [Taslak Tepsi](Draft_Tray/tr.md) \'de ayarlanan [Çizgi stili](Draft_Linestyle/tr.md) ayarlarını alır.


</div>

<img alt="" src=images/Draft_point_example.jpg  style="width:400px;">




<div class="mw-translate-fuzzy">

## Nasıl Kullanılır 


</div>

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  
    **<img src="images/Draft_Point.png" width=16px> Nokta**tuşuna veya **P** basın ardından **T** basın.

2.  3D görünümünde bir noktaya tıklayın veya bir koordinat yazın ve **<img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle** düğmesine basın.


</div>



## Seçenekler

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında **Enter** tuşuna basın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda **<img src="images/_Draft_AddPoint.svg" width=16px> Nokta ekle** düğmesine basabilirsiniz.
-   **Devam** moduna geçmek için **T** tuşuna basın veya onay kutusunu tıklayın. Devam modu açıksa, nokta aracı siz bir noktaya yerleştirdikten sonra yeniden başlatılır ve araç düğmesine tekrar basmadan bir tane daha yerleştirmenizi sağlar.
-   Geçerli komutu iptal etmek için **Esc** veya **Close** düğmesine basınız.


</div>

## Notes

-   Use <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [Draft Snap Near](Draft_Snap_Near.md) ({{VersionMinus|0.20}}) or <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:16px;"> [Draft Snap Endpoint](Draft_Snap_Endpoint.md) (<small>(v0.21)</small> ) to snap to Draft points.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.



## Özellikler

See also: [Property editor](Property_editor.md).

A Draft Point object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/tr|X}}: Noktanın X koordinatı

-    {{PropertyData/tr|Y}}: Noktanın Y koordinatı

-    {{PropertyData/tr|Z}}: Noktanın Z koordinatı


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Nokta aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


```python
point = make_point(X=0, Y=0, Z=0, color=None, name="Point", point_size=5)
point = make_point(point, Y=0, Z=0, color=None, name="Point", point_size=5)
```


<div class="mw-translate-fuzzy">

-   Belirtilen `X`, `Y` ve `Z` koordinatlarında, birimler milimetre cinsinden bir `Point` nesnesi oluşturur. Eğer koordinat verilmezse, başlangıç noktasında nokta oluşturulur (0,0,0). \*

-   Eğer `X` bir `FreeCAD.Vector` tarafından tanımlanan bir `point` ise, kullanılır.

-    `color`, `(R, G, B)` bir skaladır; nokta, RGB ölçeğindeki noktanın rengini gösterir; Bağlantıdaki her değer, `0` ila `1` aralığında olmalıdır.

-    `name`, nesnenin adıdır.

-    `point_size`, grafiksel kullanıcı arayüzü yüklendiğinde nesnenin piksel cinsinden boyutudur.


</div>

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

point1 = Draft.make_point(1600, 1400, 0)

p2 = App.Vector(-3200, 1800, 0)
point2 = Draft.make_point(p2, color=(0.5, 0.3, 0.6), point_size=10)

doc.recompute()
```

Örnek:

This code creates `N` random points within a square of side `2L`. It makes a loop creating `N` points, that may appear anywhere from `-L` to `+L` on both X and Y. It also chooses a random color and size for each point. Change `N` to change the number of points, and change `L` to change the area covered by the points.


```python
import random
import FreeCAD as App
import Draft

doc = App.newDocument()

L = 1000
centered = App.Placement(App.Vector(-L, -L, 0), App.Rotation())
rectangle = Draft.make_rectangle(2*L, 2*L, placement=centered)

N = 10
for i in range(N):
    x = 2*L*random.random() - L
    y = 2*L*random.random() - L
    z = 0
    r = random.random()
    g = random.random()
    b = random.random()
    size = 15*random.random() + 5
    Draft.make_point(x, y, z, color=(r, g, b), point_size=size)

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Point/tr
