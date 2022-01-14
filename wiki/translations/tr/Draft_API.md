# Draft API/tr
<div class="mw-translate-fuzzy">

Bu işlevler Taslak modülünün bir parçasıdır ve Taslak modülü alındıktan sonra komut dosyalarında ve makrolarda veya python yorumlayıcısında kullanılabilir.


</div>

These functions are part of the [Draft Workbench](Draft_Workbench.md) and can be used in [macros](macros.md) and from the [Python](Python.md) console once the `Draft` module has been imported.

Örnek: 
```python
import FreeCAD, Draft

myrect = Draft.makeRectangle(4, 3)
mydistance = FreeCAD.Vector(2, 2, 0)
Draft.move(myrect, mydistance)
```


{{APIFunction | cut | FreeCAD.Object, FreeCAD.Object | Verilen 2 nesnenin farkından yapılan bir kesim nesnesi döndürür. Orijinal nesneler gizlenir. | Yeni oluşturulan nesne}}


{{APIFunction | extrude | FreeCAD.Object, Vector | Verilen nesneyi vektör tarafından verilen yönde çıkarır. Orijinal nesne gizlenir. | Yeni oluşturulan nesne}}


{{APIFunction | formatObject | FreeCAD.Object, [FreeCAD.Object] | Bu işlev, Taslak araç çubuğundaki geçerli özellikleri verilen hedef nesneye uygular (çizgi rengi ve çizgi genişliği) veya verilirse ikinci bir nesnenin özelliklerini kopyalar. Ayrıca inşaat düğmesine basıldığında nesneyi inşaat grubuna yerleştirir. | Nothing}}


{{APIFunction | fuse | FreeCAD.Object, FreeCAD.Object | Verilen 2 nesnenin birleşiminden yapılan nesneyi döndürür. Nesneler düzlemsel ise, özel bir Taslak Teli kullanılır, aksi takdirde nihai nesne standart bir Kısım sigortasıdır. | Yeni oluşturulan nesne}}


{{APIFunction | getDraftPath | [string] | Taslak modülünün bulunduğu kullanıcıyı veya sistem yolunu döndürür den çalışıyor. Bir alt yol veya bir dosya adı verilirse, Taslak modülündeki alt yolun tam yolu döndürülür. | Bir dosya yolu}}


{{APIFunction | getGroupContents | list | Gruplar için verilen listeyi tekrar tekrar tarar. Gruplarla karşılaşılırsa, içerikleri listeye eklenir. | FreeCAD Nesnelerinin bir listesi}}


{{APIFunction | getRealName | string | Bir takip eden sayıları bir nesne adından soyar. | Soyulmuş nesne adı}}


{{APIFunction | getSelection | | Geçerli FreeCAD seçimini döndürür. | Geçerli FreeCAD seçimidir.}}

{{APIFunction | makeCircle | radius, [yerleşim], [facemode], [startangle], [endangle] | Verilen yarıçapı olan bir daire nesnesi oluşturur. Yerleşim verilirse kullanılır. Yüz modu Yanlış ise, daire bir tel kafes olarak gösterilir, aksi halde yüz olarak gösterilir. Startangle ve endangle verilirse (derece cinsinden) kullanılırlar ve nesne bir yay gibi görünür. | Yeni oluşturulan nesne.}} {{APIFunction | makeDimension | Vector, Vector, [Vector] veya FreeCAD.Object, int, int, [Vector] | İlk ve ikinci vektörler arasındaki mesafeyi ölçen bir Ölçümlendirme nesnesi oluşturur, eğer varsa boyut çizgisi üçüncü vektörden geçer. Taslak araç çubuğundan geçerli çizgi genişliği ve rengi kullanılacaktır. 2 vektör yerine, bir FreeCAD nesnesini ve iki tam sayıyı (ve isteğe bağlı olarak boyut çizgisinin geçmesi gereken bir vektör) geçirebilirsiniz. Bu durumda boyut, nesneyle ilişkilendirilir ve verilen iki indeks numarası ile gösterilen iki köşesini ölçer. | Yeni oluşturulan nesne.}} {{APIFunction | makeLine | Vector, Vector | Arasında bir çizgi oluşturur. verilen iki vektör. Taslak araç çubuğundan geçerli çizgi genişliği ve rengi kullanılacaktır. | Yeni oluşturulan nesne.}} {{APIFunction | makeRectangle | uzunluk, genişlik, [yerleştirme], [facemode] | X yönünde ve uzunluğunda bir Dikdörtgen nesnesi oluşturur. Y yönünde yükseklik. Yerleşim verilirse kullanılır. Yüz modu Yanlış ise, dikdörtgen bir tel kafes, aksi halde yüz olarak gösterilir. Taslak araç çubuğundan geçerli çizgi genişliği ve rengi kullanılacaktır. | Yeni oluşturulan nesne.}} {{APIFunction | makeText | string veya list, [Vector], [screenmode] | Belirtilen noktada bir Text nesnesi oluşturur dize veya listede verilen dizeleri, bir dizgiyi içeren bir vektör sağlanır. Taslak araç çubuğundan geçerli renk ve tercihlerde belirtilen metin yüksekliği ve yazı tipi kullanılır. Ekran modu True ise, metin her zaman görünüm yönüne bakar, aksi takdirde XY düzleminde kalır. | Yeni oluşturulan nesne.}} {{APIFunction | makeWire | list veya Part.Wire, [kapalı], [yerleşim], [ facemode] | Verilen vektör listesinden veya verilen Wire'dan bir DWire nesnesi oluşturur. Kapalı Doğru ise veya ilk ve son noktalar aynıysa, tel kapalıdır. Yüz modu Doğru ise (ve kablo kapalıysa), tel dolu görünecektir. Taslak araç çubuğundan geçerli çizgi genişliği ve rengi kullanılacaktır. | Yeni bir Taslak DWire (Parça Tel değil).}} {{APIFunction | move | FreeCAD.Object veya list, Vector, [copymode] | Verilen nesneyi taşır veya verilen listede yer alan ve belirtilen vektör tarafından belirtilen doğrultuda ve mesafedeki nesneler. Copymode True ise, gerçek nesneler taşınmaz, ancak kopyalar bunun yerine oluşturulur. | Nesneler (veya copymode True ise kopyaları).}} {{APIFunction | precision | | Taslak kullanıcı ayarlarından hassas değeri döndürür. | Bir tamsayı.}} {{APIFunction | rotate | FreeCAD.Object veya list, angle, [center], [axis], [copymode] | Verilen nesneyi veya içerdiği nesneleri döndürür Verilen listede, verilen merkez etrafında verilen açı ile, ekseni dönme ekseni olarak kullanma. Eksen ihmal edilirse, dönüş dikey Z ekseni etrafında olacaktır. Copymode True ise, gerçek nesneler taşınmaz, ancak kopyalar bunun yerine oluşturulur. | Nesneler (veya kopyaları).}} {{APIFunction | scale | FreeCAD.Object veya list, vector, [center], [copymode] | Verilen nesneyi veya verilen listede yer alan nesneleri verilen vektör tarafından tanımlanan ölçek faktörleriyle ölçeklendirir (X, Y ve Z dizinlerinde)}}


 




[<img src="images/Property.png" style="width:16px"> API](Category_API.md) [<img src="images/Property.png" style="width:16px"> Poweruser Documentation](Category_Poweruser_Documentation.md)

---
[documentation index](../README.md) > [API](Category_API.md) > [Draft](Draft_Workbench.md) > Draft API/tr
