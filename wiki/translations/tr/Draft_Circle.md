---
- GuiCommand:/tr
   Name:Draft Circle
   Name/tr:Çember
   MenuLocation:Taslak → Çember
   Workbenches:[Çember](Draft_Workbench/tr.md), [Yapı](Arch_Workbench/tr.md)
   Shortcut:**C** **I**
   SeeAlso:[Yay](Draft_Arc/tr.md), [Elips](Draft_Ellipse/tr.md)
   Version:0.7
---

# Draft Circle/tr


</div>

## Description


<div class="mw-translate-fuzzy">

## Açıklama

Çember aracı, geçerli [Çalışma düzlemi](Draft_SelectPlane/tr.md) içinde iki nokta girerek, merkez ve yarıçapı girerek veya teğetleri veya bunların herhangi bir kombinasyonunu alarak bir çember oluşturur. [Tepsi](Draft_Tray/tr.md) de önceden ayarlanmış olan [Çizgi stili](Draft_Linestyle/tr.md) alır.


</div>


<div class="mw-translate-fuzzy">

Bu araç, tam bir yay oluşturması dışında, [Yay](Draft_Arc/tr.md) aracıyla aynı şekilde çalışır. Bir elips çizmek için [Elips](Draft_Ellipse/tr.md) kullanın.


</div>

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Çember, iki noktayla tanımlanır*


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Nasıl kullanılır 

1.  
    **<img src="images/_Draft_Circle.png" width=16px> [Çember](Draft_Circle/tr.md)**düğmesine basın veya **C** ardından **I** tuşlarına basın .

2.  3D görünümde bir ilk noktaya tıklayın veya bir koordinat yazın ve **<img src="images/_Draft_AddPoint.svg" width=16px> Nokta ekle** düğmesine basın.

3.  3D görünümünde ikinci bir noktaya tıklayın veya bir yarıçap değeri girin.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Seçenekler

-   Daire aletinin birincil kullanımı, merkez ve çevre üzerindeki bir nokta olmak üzere iki nokta seçmektir.
    -   
        **Alt**
        
        tuşuna basarak, bir nokta seçmek yerine bir teğet seçebilirsiniz. Bu nedenle, bir, iki veya üç teğet seçerek birkaç daire tipi oluşturabilirsiniz.
-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında **Enter** tuşuna basın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda **<img src="images/_Draft_AddPoint.svg" width=16px> Nokta ekle** düğmesine basabilirsiniz.
-   **Devam** moduna geçmek için **T** tuşuna basın veya onay kutusunu tıklayın. Devam modu açıksa, daireyi tamamladıktan sonra Daire aracı yeniden başlatılır ve araç düğmesine tekrar basmadan bir tane daha çizmenize olanak sağlar.
-   **Dolgu** moduna geçmek için **L** tuşuna basın veya onay kutusunu tıklayın. Dolgu modu açıksa, daire dolgulu bir yüz oluşturur ({{PropertyData/tr|Make Face}} `True`); değilse, daire bir yüz oluşturmaz ({{PropertyData/tr|Make Face}} `False`).
-   [snapping](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak, en yakın çeki konumuna yönlendirmek için çizim yaparken **Ctrl** tuşunu basılı tutun.
-   İlk noktanıza göre ikinci noktanızı yatay veya dikey olarak [constrain](Draft_Constrain/tr.md) çizerken **Shift** tuşunu basılı tutun.
-   Geçerli komutu iptal etmek için **Esc** veya **Kapat** düğmesine basınız.


</div>

## Notes


<div class="mw-translate-fuzzy">

Ağaç görünümündeki öğeye çift tıklayarak veya **<img src="images/_Draft_Edit.svg" width=16px> [Düzenle](Draft_Edit/tr.md)** düğmesine basılarak daire düzenlenebilir. Ardından merkez ve yarıçap noktalarını yeni bir konuma getirebilirsiniz.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and radii: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Circle object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Veri

-    {{PropertyData/tr|Başlangıç açısı}}: Çemberin başlangıç açısını belirtir; normalde 0 °.

-    {{PropertyData/tr|Bitiş açısı}}: Çemberin bitiş açısını belirtir; normalde 0 °.

-    {{PropertyData/tr|Yarıçap}}: Çemberin yarıçapını belirtir.

-    {{PropertyData/tr|Yüzey oluştur}}: Çemberin bir yüzey yapıp yapmayacağını belirtir. `True` ise bir yüz yaratılır, aksi takdirde sadece çevre nesnenin bir parçası olarak kabul edilir. Bu özellik yalnızca şekil tam bir çevre ise işe yarar.

-    {{PropertyData/tr|Başlangıç açısı}}: ve tam daire olması için {{PropertyData/tr|Bitiş açısı}} aynı değere sahip olmalıdır; Aksi takdirde, bir [Yay](Draft_Arc/tr.md) görüntülenir. 0 ° ve 360 ° değerleri aynı sayılmaz, bu nedenle bu iki değer kullanılırsa, daire bir yüzey oluşturmaz.


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Görünüm

-    {{PropertyView/tr|Desen}}: Çemberin yüzünü doldurmak için bir [Desen](Draft_Pattern/tr.md) belirtir. Bu özellik yalnızca {{PropertyData/tr|Yüzey oluştur}} `True` ise ve {{PropertyView/tr|Görüntüle modu}} \"Düz Çizgiler\" ise çalışır.

-    {{PropertyView/tr|Desen}}: [Desen](Draft_Pattern/tr.md) \'nin boyutunu belirtir.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Çember aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


```python
circle = make_circle(radius, placement=None, face=None, startangle=None, endangle=None, support=None)
circle = make_circle(Part.Edge, placement=None, face=None, startangle=None, endangle=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Milimetre cinsinden `radius` verilen bir `Circle` nesnesi oluşturur.
    -   
        `radius`
        
        ayrıca `Curve` özniteliğinin bir `Part.Circle` olması gereken bir `Part.Edge` de olabilir.

-   Bir `placement` verilirse kullanılır; Aksi halde, şekil başlangıçta oluşturulur.

-    `face``True` ise, daire bir yüz yapacaktır, yani dolu görünecektir.

-   Eğer `startangle` ve `endangle` derece cinsinden verilirse ve farklı değerler varsa, bunlar kullanılır ve nesne [Draft Arc](Draft_Arc/tr.md) olarak görünür.


</div>

Örnek: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle1 = Draft.make_circle(200)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(1000, 1000, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 0))
circle2 = Draft.make_circle(500, placement=place2)

p3 = App.Vector(-1000, -1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 0))
circle3 = Draft.make_circle(750, placement=place3)

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Circle/tr
