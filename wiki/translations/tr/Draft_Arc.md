---
- GuiCommand:
   Name: Draft Arc
   Name/tr: Yay
   Workbenches: [Taslak](Draft_Workbench/tr.md), [Mimari](Arch_Workbench/tr.md)
   MenuLocation: Taslak - Yay
   Shortcut: **A** **R**
   Version: 0.17
   SeeAlso: [Çember](Draft_Circle/tr.md),[Elips](Draft_Ellipse/tr.md)
---

# Draft Arc/tr


</div>

## Açıklama


<div class="mw-translate-fuzzy">

Yay aracı, geçerli [Çalışma düzlemi](Draft_SelectPlane/tr.md) içinde dört nokta, merkez, yarıçap, ilk nokta ve son nokta girerek ya da teğetleri toplayarak ya da bunların herhangi bir bileşimini girerek bir yay oluşturur. Görevler sekmesinde önceden ayarlanmış olan [Çizgi stili](Draft_Linestyle/tr.md) alır. Bu araç, [Çember](Draft_Circle/tr.md) aracıyla aynı şekilde çalışır, ancak başlangıç ve bitiş açılarını ekler.


</div>

A Draft Arc is in fact a [Draft Circle](Draft_Circle.md) with a **First Angle** that is not the same as its **Last Angle**.

<img alt="" src=images/Draft_Arc_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Yay; merkez, yarıçap,  ​​yay başlangıç noktası ve  yay son noktasıolarak dört noktada tanımlanır.
*


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Nasıl kullanılır 

1.  
    **<img src="images/Draft_Arc.png" width=16px> [Yay](Draft_Arc/tr.md)**düğmesine basınız veya **A** ve **R** tuşlarına basınız.

2.  3D görünümünde bir ilk noktaya tıklayın veya bir Koordinat yazın ve **<img src="images/Draft_AddPoint.svg" width=16px> add point** basın

3.  3D görünümünde ikinci bir noktaya tıklayın veya bir yarıçap değeri girin

4.  3D görünümünde üçüncü bir noktaya tıklayın veya bir başlangıç açısı girin

5.  3D Görünümünde dördüncü bir noktaya tıklayın veya bitiş sonunu girin


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Seçenekler

-   Yay aracının birincil kullanımı dört nokta seçmektir: merkez, çevre üzerinde bir nokta, yayın başlangıcı ve bitişi.
    -   
        **Alt**
        
        tuşuna basarak arkın temel çemberini tanımlamak için toplama noktası yerine bir teğet seçebilirsiniz. Bu nedenle, bir, iki veya üç teğet seçerek birkaç daire tipi oluşturabilirsiniz.
-   Yay yönü, farenizle yaptığınız harekete bağlıdır. Üçüncü nokta girildikten sonra saat yönünde hareket etmeye başlarsanız, yayınız saat yönünde gider. Saat yönünün tersine gitmek için, farenizi yay diğer yöne çekmeye başlayana kadar üçüncü noktanın üzerine getirin.
-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında **Enter** tuşuna basın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda **<img src="images/_Draft_AddPoint.svg" width=16px> Nokta ekle** düğmesine basabilirsiniz.
-   *Devam* moduna geçmek için **T** tuşuna basın veya onay kutusunu tıklayın. Devam modu açıksa, yay aracı, yayı bitirdikten sonra yeniden başlatılır ve takım düğmesine tekrar basmadan bir tane daha çizmenize olanak sağlar.
-   [snapping](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak, en yakın çeki konumuna yönlendirmek için çizim yaparken **Ctrl** tuşunu basılı tutun.
-   Ortaya göre noktanızı yatay veya dikey olarak [constrain](Draft_Constrain/fr.md) öğesine çizerken **Shift** tuşunu basılı tutun.
-   Geçerli komutu iptal etmek için **Esc** veya **Kapat** düğmesine basınız.


</div>

## Notes


<div class="mw-translate-fuzzy">

Ağaç görünümündeki öğeye çift tıklayarak veya **<img src="images/_Draft_Edit.svg" width=16px> [Düzenle](Draft_Edit/tr.md)** düğmesine basılarak ark düzenlenebilir. Ardından merkez noktasını yeni bir konuma taşıyabilirsiniz.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, radii and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Properties


<div class="mw-translate-fuzzy">

## Özellikleri

Bir yay nesnesi [Çember](Draft_Circle/tr.md) \'in tüm özelliklerini paylaşır, ancak bazı özellikler sadece çember için geçerlidir.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Yay aracı, [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan ek argümanlarla çember oluşturmak için aynı işlevle kullanılabilir. İçindeki bilgilere bakın [Daire](Draft_Circle/tr.md).


</div>

Örnek:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

arc1 = Draft.make_circle(200, startangle=0, endangle=90)
arc2 = Draft.make_circle(500, startangle=20, endangle=160)
arc3 = Draft.make_circle(750, startangle=-30, endangle=-150)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Arc/tr
