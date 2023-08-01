# Document structure/tr
![](images/Screenshot_treeview.jpg ) Bir FreeCAD belgesi, sahnenizdeki tüm nesneleri içerir. Herhangi bir tezgah ile yapılan grupları ve nesneleri içerebilir. Bu nedenle tezgahlar arasında geçiş yapabilir ve hala aynı belge üzerinde çalışabilirsiniz. Çalışmanızı kaydettiğinizde belge diske kaydedilecek olandır. Ayrıca FreeCAD\'de aynı anda birkaç belge açabilir ve aynı belgenin birkaç görünümünü açabilirsiniz.


<div class="mw-translate-fuzzy">

Belgenin içinde nesneler gruplara taşınabilir ve benzersiz bir ad alabilirler. Grupları, nesneleri ve nesne adlarını yönetmek, genellikle Ağaç görünümünden yapılır. Elbette, FreeCAD içinde yapılabilen her şeyi [Python](Python.md) yorumlayıcıdan da yapabilirsiniz. Ağaç görünümünde, gruplar oluşturabilir, nesneleri gruplara taşıyabilir, nesneleri veya grupları silebilir, ağaç görünümünde veya bir nesneyi sağ tıklayarak, adlarını çift tıklatarak nesneleri yeniden adlandırabilir veya çalışılan tezgaha bağlı olarak diğer işlemleri yapabilirsiniz.


</div>


<div class="mw-translate-fuzzy">

FreeCAD belgesindeki nesneler farklı türlerde olabilir. Her tezgah kendi nesne türlerini yaratabilir, örneğin [Kafes tezgahı](Mesh_Workbench.md) kafes nesnelerini yaratır, [Parça tezgahı](Part_Workbench.md) Parça nesnelerini yaratır , [Taslak Tezgâhı](Draft_Workbench.md) ayrıca Parça nesnelerini yaratır vb.


</div>

FreeCAD\'de en az bir açık belge varsa, her zaman bir ve sadece bir aktif belge vardır. Geçerli 3D görünümünde görünen, üzerinde çalışmakta olduğunuz belge budur.

## Uygulama ve Kullanıcı Arayüzü 

FreeCAD\'deki hemen hemen her şey gibi, grafiksel kullanıcı arabirimi kısmı (GUI), temel uygulama bölümünden (App) ayrılmıştır. Bu aynı zamanda belgeler için de geçerlidir. Belgeler ayrıca iki bölümden oluşur: nesnelerimizi içeren Uygulama belgesi ve nesnelerimizin ekrandaki gösterimi içeren Görünüm belgesi.

Nesnelerin tanımlandığı iki alan olarak düşünün. Yapısal parametreleri (bu bir küp mü? Koni mi? Hangi ölçüler?) Uygulama belgesinde saklanırken, grafiksel gösterimleri (Mavi renkli yüzler? Siyah renkli çizgiler??) görünüm belgesinde saklanır. Neden? Çünkü FreeCAD ayrıca , örneğin diğer programların içinde grafik arayüzü olmadan da kullanılabilir ve ekranda herhangi bir şey çizilmemiş olsa bile nesnelerimizi değiştirebilmeliyiz.

Görünüm belgesinde bulunan bir başka şey 3D görünümlerdir. Bir belgede birkaç görünüm açılabilir, böylece belgenizi aynı anda birkaç bakış açısından inceleyebilirsiniz. Belki aynı anda çalışmanızın bir üst görünümünü ve ön görünümünü görmek istersiniz? Ardından, her ikisi de Görünüm belgesinde saklanan aynı belgenin iki görünümüne sahip olacaksınız. Yeni görünümler oluşturmak veya görünümleri kapatmak Görünüm menüsünden veya bir görünüm sekmesine sağ tıklayarak yapılabilir.

## Betik


<div class="mw-translate-fuzzy">

Python yorumlayıcısından belgeler kolayca oluşturulabilir, erişilebilir ve değiştirilebilir . Örneğin:


</div>


```python
FreeCAD.ActiveDocument
```

Geçerli (etkin) belgeyi döndürür 
```python
FreeCAD.ActiveDocument.Blob
``` Belgenizde \"Blob\" adlı bir nesneye erişir 
```python
FreeCADGui.ActiveDocument
``` Geçerli belgeyle ilişkili görüntüleme belgesini döndürür 
```python
FreeCADGui.ActiveDocument.Blob
``` Blob nesnesinin grafik gösterimi (görünümü) bölümüne erişir 
```python
FreeCADGui.ActiveDocument.ActiveView
``` Geçerli görünümü döndürür


<div class="mw-translate-fuzzy">


{{docnav/tr|[Fare ile 3D gezinme](Mouse_Model/tr.md)|[Seçenekler penceresi](Preferences_Editor/tr.md)}}


</div>



---
⏵ [documentation index](../README.md) > Document structure/tr
