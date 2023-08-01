---
- GuiCommand:
   Name:Draft Polygon
   Name/tr:Çokgen
   MenuLocation:Taslak - Çokgen
   Workbenches:[Taslak](Draft_Workbench/tr.md), [Mimari](Arch_Workbench/tr.md)
   Shortcut:**P** **G**
   SeeAlso:[Çember](Draft_Circle/tr.md)
   Version:0.7
---

# Draft Polygon/tr


</div>

## Description


<div class="mw-translate-fuzzy">

## Açıklama

Çokgen aracı, merkez ve yarıçapı olmak üzere iki nokta toplayarak bir çevreye yerleştirilmiş düzenli bir çokgen oluşturur. [Draft Tray](Draft_Tray.md) \'de ayarlanan [Çizgi stili](Draft_Linestyle/tr.md) alır.


</div>


<div class="mw-translate-fuzzy">

Çokgen, yarıçapı belirtilen bir dairede oluşturulmuştur; çizme modu özelliğini değiştirerek oluşturulduktan sonra sınırlandırılabilir.


</div>

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


{{Caption | Merkez nokta ve yarıçap tarafından tanımlanan normal çokgen}}


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Nasıl kullanılır 

1.  
    {{Button | <img src="images/_Draft_Polygon.png_" width= 16px> [Çokgen](Draft_Polygon/tr.md)}}düğmesine veya {{KEY | P}} ve {{KEY | G}} tuşlarına basın.

2.  Seçenekler diyalog penceresinde istediğiniz kenar sayısını ayarlayın.

3.  3D görünümde bir ilk noktaya tıklayın veya bir koordinat yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basın.

4.  3D görünümünde başka bir noktaya tıklayın veya poligon yarıçapını tanımlamak için bir yarıçap değeri yazın.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Seçenekler

-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında {{KEY | Enter}} tuşuna basın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basabilirsiniz.
-   **Devam** moduna geçmek için {{KEY | T}} tuşuna basın veya onay kutusunu tıklayın. Devam modu açıksa, Çokgen aracı işlemi tamamladıktan sonra yeniden başlatılır ve araç düğmesine tekrar basmadan bir tane daha çizmenize olanak sağlar.
-   **Dolu** moduna geçmek için {{KEY | L}} tuşuna basın veya onay kutusunu tıklayın. Dolgu modu açıksa, çokgen dolgulu bir yüz oluşturur ({{PropertyData | Make Face}} `True`); değilse, çokgen bir yüz oluşturmayacak ({{PropertyData | Make Face}} `False`).
-   [ Yakalama](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak, en yakın çeki konumuna yönlendirmek için çizim yaparken {{KEY | Ctrl}} tuşunu basılı tutun.
-   İlk noktanıza göre ikinci noktanızı yatay veya dikey olarak [Kısıtlama](Draft_Constrain/tr.md) çizerken {{KEY | Shift}} tuşunu basılı tutun.
-   Geçerli komutu iptal etmek için {{KEY | Esc}} veya {{Button | Close}} düğmesine basınız.


</div>

## Notes


<div class="mw-translate-fuzzy">

Çokgen, ağaç görünümündeki öğeye çift tıklayarak veya {{Button | <img src="images/_Draft_Edit.svg_" width= 16px> [Düzenle](Draft_Edit/tr.md)}} düğmesine basılarak düzenlenebilir. Ardından merkez ve yarıçap noktalarını yeni bir konuma getirebilirsiniz.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and radii: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part RegularPolygon](Part_RegularPolygon.md) instead of a Draft Polygon.

## Özellikler

See also: [Property editor](Property_editor.md).

A Draft Polygon object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Veri

-    {{PropertyData/tr|Radius}}: Çokgeni tanımlayan dairenin yarıçapını belirtir.

-    {{PropertyData/tr|Draw Mode}}: Çokgenin bir daire içine mi yazıldığını yoksa bir daire içine mi yazıldığını belirtir.

-    {{PropertyData/tr|Faces Number}}: Çokgenin kenar sayısını belirtir.

-    {{PropertyData/tr|Chamfer Size}}: Çokgenin köşelerinde oluşturulan olukların (düz bölümler) boyutunu belirtir.

-    {{PropertyData/tr|Fillet Radius}}: Çokgenin köşelerinde oluşturulan filetoların (yay parçaları) yarıçapını belirtir.

-    {{PropertyData/tr|Make Face}}: şeklin bir yüz yapıp yapmamasını belirtir. Eğer `True` ise bir yüz yaratılır, aksi takdirde sadece çevre nesnenin bir parçası olarak kabul edilir.


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Görünüm

-    {{PropertyView/tr|Pattern}}: Çokgenin yüzünü doldurmak için bir [Taslak Deseni](Draft_Pattern.md) belirtir. Bu özellik yalnızca {{PropertyData/tr|Make Face}} `True` ise ve {{PropertyView/tr|Display Mode}} \"Düz Çizgiler\" ise çalışır.

-    {{PropertyView/tr|Pattern Size}}: [Desen](Draft_Pattern/tr.md) \'nin boyutunu belirtir.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Çokgen aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


```python
polygon = make_polygon(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Belirtilen yüz sayısıyla ({{incode | nfaces}}) bir {{incode | Polygon}} nesnesi oluşturur ve milimetre cinsinden bir {{incode | radius}} dairesine dayanır.

-   Eğer {{incode | inscribed}} {{incode | True}} ise, çokgen daireye yazılır, aksi takdirde sınırlandırılır.
    -   Başka bir yerleştirme yapılmazsa, çokgenin köşelerinden biri X ekseninde uzanır.

-   Bir {{incode | placement}} verilirse kullanılır; Aksi halde, şekil başlangıçta oluşturulur.

-    {{incode | face}}{{incode | True}} ise, şekil bir yüz yapacaktır, yani dolu görünecektir.


</div>

Örnek: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(4, radius=500)
polygon2 = Draft.make_polygon(5, radius=750)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

Polygon3 = Draft.make_polygon(6, radius=1450, placement=place3)

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Polygon/tr
