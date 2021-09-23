# Feature list/tr
<div class="mw-translate-fuzzy">

FreeCAD\'in uyguladığı özelliklerin kapsamlı bir listesidir, dolayısıyla tam değildir. Gelecek dönemler için [Geliştirme yol haritasına](Development_roadmap.md) bakın veya hızlı bir şekilde göz gezdirmek için [Ekran görüntülerine](Screenshots.md) bir göz atın.


</div>


{{TOCright}}

## Sürüm Notları 


<div class="mw-translate-fuzzy">

-   [Sürüm 0.11](Release_notes_0.11.md) - Mart 2011
-   [Sürüm 0.12](Release_notes_0.12.md) - Aralık 2011
-   [Sürüm 0.13](Release_notes_0.13.md) - Ocak 2013
-   [Sürüm 0.14](Release_notes_0.14.md) - Mart 2014
-   [Sürüm 0.15](Release_notes_0.15.md) - Mart 2015
-   [Sürüm 0.16](Release_notes_0.16.md) - Nisan 2016
-   [Sürüm 0.17](Release_notes_0.17.md) - Nisan 2018


</div>

## Genel Özellikler 

### Temel Uygulama 


<div class="mw-translate-fuzzy">

-   ![](images/Feature1.jpg ) [Open CASCADE Technology](http://en.wikipedia.org/wiki/Open_CASCADE)-tabanlı **geometri çekirdeği**, karmaşık şekiller üzerinde, brep , eğriler ve yüzeyler, çeşitli geometrik şekiller, boolean işlemler ve dolgular, yerel destekli STEP ve IGES formatları gibi çeşitli yerel konseptlerle, karmaşık 3D işlemler yapmanıza olanak tanır.
-   ![](images/Feature3.jpg ) **Tam parametrik bir model**. Tüm FreeCAD objeleri doğal olarak parametriktir, yani şekilleri [özelliklere dayalı](Property.md) olabilir veya hatta diğer nesnelere bağlı olabilir, tüm değişiklikler talep üzerine yeniden hesaplanır ve geri al/yenile yığınıyla kaydedilir. [Tamamıyla Python\'da kodlanan](Scripted_objects.md) yeni nesne türleri kolayca eklenebilir.
-   ![](images/Feature4.jpg ) **Modüler mimari** eklentiler (modüller) sayesinde ana uygulamaya işlevsellik ekler. Bu uzantılar C ++ \'da programlanan tüm yeni uygulamalar kadar karmaşık veya [Python betikleri](Power_users_hub.md) veya kendi kendine kaydedilen [makrolar](macros.md) kadar basit olabilir. **Python** yerleşik yorumlayıcısından; [geometri oluşturma ve dönüştürme](Topological_data_scripting.md),bu geometrinin 2D veya 3D gösterimi([sahne grafiği](scenegraph.md)) hatta [FreeCAD arayüzüne](PySide.md) , makrolar veya harici komut dosyalarından FreeCAD\'in hemen hemen tüm kısımlarına erişebilirsiniz.
-   ![](images/Feature5.jpg ) FreeCAD\'in [Fcstd dosya formatına](Fcstd_file_format.md) ek olarak [STEP](http://en.wikipedia.org/wiki/ISO_10303), [IGES](http://en.wikipedia.org/wiki/IGES), [OBJ](http://en.wikipedia.org/wiki/Obj), [STL](http://en.wikipedia.org/wiki/STL_%28file_format%29), [DXF](http://en.wikipedia.org/wiki/Dxf), [SVG](http://en.wikipedia.org/wiki/Svg), [STL](http://en.wikipedia.org/wiki/STL_(file_format)), [DAE](http://en.wikipedia.org/wiki/COLLADA), [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) veya [OFF](http://people.sc.fsu.edu/~jburkardt/data/off/off.html), [NASTRAN](http://en.wikipedia.org/wiki/NASTRAN), [VRML](http://en.wikipedia.org/wiki/VRML) gibi dosya formatları da desteklenmektedir ve Dosya al/Dosya ver ile kullanılabilmektedir. FreeCAD ve verilen bir dosya formatı arasındaki uyumluluk seviyesi, onu uygulayan modüle bağlı olduğu için değişebilir.
-   ![](images/Feature7.jpg ) Geometri kısıtlı 2D şekillerin çizilmesine izin veren kısıtlayıcı-çözücülü bir [Eskiz](Sketcher_Workbench.md) . Eskiz, şu anda birkaç tip sınırlı geometri oluşturmanıza ve bunları FreeCAD boyunca başka nesneler oluşturmak için bir temel olarak kullanmanıza izin vermektedir.
-   ![](images/Feature9.jpg ) [Robot simülasyon](Robot_Workbench.md) modülü Robot hareketlerini incelemek için kullanılır. Robot modülünde, yalnızca GUI iş akışına izin veren genişletilmiş bir grafik arabirim vardır.
-   ![](images/Feature8.jpg )[Teknik resim modülü](TechDraw_Workbench.md) Ayrıntı görünümü, kesitler, boyutlandırma ve benzeri seçeneklerle geleneksel çizim sayfaları oluşturmak için 3 boyutlu modellerin 2D görünümlerini bir sayfaya koymanıza olanak veren yeni ve kolay bir modül. Bu modülle SVG veya PDF şeklinde kaydedilebilecek sayfalar üretilir.Eski [Çizim modülü](Drawing_Workbench.md) Arayüzde çok az araç bulundurur ancak Pythonla işlevselliği yüksektir.
-   ![](images/Feature-raytracing.jpg ) [Rendering](Raytracing_Workbench.md) modülü,başka render uygulamalarında kullanılmak üzere 3D nesneleri farklı formatlarda dosyalara kaydedebiliyorsunuz. Şu anda sadece [povray](http://en.wikipedia.org/wiki/POV-Ray) ve [LuxRender](http://en.wikipedia.org/wiki/LuxRender) uygulamalrını desteklemektedir. Ancak gelecekte daha fazla renderer uygulamasını destekleyeceğini umuyoruz.
-   ![](images/Feature-arch.jpg ) [Mimari(yapı)](Arch_Workbench.md) modülü, [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) benzeri iş akışı ve [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) uyumluluğuna sahiptir..
-   ![](images/Feature-CAM.jpg ) [Path modülü](Path_Workbench.md) Frezeleme gibi (CAM) mekanik işlemler içindir ve [G code](http://en.wikipedia.org/wiki/G-code) çıktısını alabilir, gösterebilir ve ayarlayabilir ..
-   ![](images/Feature_spreadsheet.png ) [Entegre Elektronik Tablo](Spreadsheet_Workbench.md) ve [ifade ayrıştırıcı](Expressions.md) Formül tabanlı modelleri oluşturmak veya modellerden veri almak için kullanılırlar.


</div>


<div class="mw-translate-fuzzy">

## Genel Özellikler: 


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD, multi-platform bir uygulamadır**. Windows,Linux ve macOS platformlarında da aynı şekilde çalışır ve davranır.


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD tam bir GUI uygulamasıdır**. FreeCAD, ünlü [Qt](http://www.qtsoftware.com/) framework\'e dayanan, tam bir Grafiksel Kullanıcı Arayüzüne sahiptir ve 3D görüntüleyici [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) ile 3D sahnelerin hızlı bir şekilde oluşturulmasını ve erişilebilir bir sahne grafiği sunumunu sağlar.


</div>


<div class="mw-translate-fuzzy">

-   **FreeCAD ayrıca bir komut satırı uygulaması olarak da çalışır**. Bellek kullanımı çok azdır.Komut satırı modunda, FreeCAD arayüzü olmadan ancak tüm geometri araçları ile çalışır. Örneğin, diğer uygulamalara içerik üretmek için sunucu olarak kullanılabilir.


</div>


<div class="mw-translate-fuzzy">

-   \'\'\'FreeCAD, [Python modülü](Embedding_FreeCAD.md) olarak \'\'\', Python komut dosyalarını çalıştırabilen diğer uygulamaların içine veya bir Python konsoluna alınabilir. Konsol kipinde olduğu gibi, FreeCAD\'in arayüz kısmı kullanılamaz, ancak tüm geometri araçlarına erişilebilir.


</div>


<div class="mw-translate-fuzzy">

-   **Tezgah konsepti**: FreeCAD arayüzünde, aletler [tezgahlar](workbenches.md) şeklinde gruplanır . Bu, çalışma alanını düzenli,işlevsel ve uygulamayı hızlı bir şekilde yükleyerek, yalnızca belirli bir görevi gerçekleştirmek için kullanılan araçları görüntülemenizi sağlar.


</div>


<div class="mw-translate-fuzzy">

-   **Özelliklerin/veri türlerinin sonradan yüklenebilmesi için Eklenti/Modül framework\'ü**. FreeCAD, yalnızca ihtiyaç duyulduğunda yüklenen çekirdek bir uygulamaya ve modüllere ayrılmıştır. Hemen hemen tüm aletler ve geometri türleri modüllerde depolanır. Modüller eklentiler gibi davranır ve mevcut bir FreeCAD kurulumuna eklenebilir veya kaldırılabilir.


</div>


<div class="mw-translate-fuzzy">

-   **Parametrik ilişkisel belge nesneleri**: Bir FreeCAD belgesindeki tüm nesneler parametrelerle tanımlanabilir. Bu parametreler anında değiştirilebilir ve her zaman yeniden hesaplanabilir. Nesneler arasındaki ilişki de depolanır, dolayısıyla bir nesneyi değiştirmek aynı zamanda bağımlı nesnelerini de değiştirir.


</div>


<div class="mw-translate-fuzzy">

-   **Parametrik ilkel oluşturma** (kutu, küre, silindir vb.)


</div>


<div class="mw-translate-fuzzy">

-   3D alanın herhangi bir düzleminde çeviri, döndürme, ölçekleme, yansıtma, ofset (önemsiz veya [Jung/Shin/Choi](https://www.researchgate.net/publication/240754626_Self-intersection_Removal_in_Triangular_Mesh_Offsetting) sonrası ) veya şekil dönüştürme gibi grafiksel **modifikasyon işlemleri**


</div>


<div class="mw-translate-fuzzy">

-   **[Boole işlemleri](http://en.wikipedia.org/wiki/Constructive_solid_geometry)**(birleşme, fark , kesişme)


</div>


<div class="mw-translate-fuzzy">

-   3D uzayın herhangi bir düzleminde çizgiler, teller, dikdörtgenler, b-splinelar, dairesel veya eliptik yaylar gibi **düzlemsel geometrik** şekillerin grafiksel olarak oluşturulması


</div>


<div class="mw-translate-fuzzy">

-   Düz veya devirli **ekstrüzyon** , **kesit** ve **dolgu** modellemesi.


</div>


<div class="mw-translate-fuzzy">

-   **Köşeler , kenarlar, teller ve düzlemler** gibi topolojik bileşenler (ayrıca Python komut dosyası aracılığıyla).


</div>


<div class="mw-translate-fuzzy">

-   Kafesler için **test ve tamir araçları**: katı testi, iki manifoldlu olmayan test, kendinden kesişim testi, delik doldurma ve düzgün yönlendirme.


</div>


<div class="mw-translate-fuzzy">

-   Metin veya boyut gibi **ek açıklamalar**


</div>


<div class="mw-translate-fuzzy">

-   **Geri Al/Yinele framework\'u**: geri alma yığın erişimi ile her şey geri alınabilir/yinelenebilir, bu nedenle bir kerede birden fazla adım geri alınabilir.


</div>


<div class="mw-translate-fuzzy">

-   **İşlem yönetimi**: Geri alma/yinele yığını, her bir aracın tam olarak ne yapılması gerektiğini veya yeniden yapılması gerektiğini tanımlamasına olanak tanıyan tek işlemleri değil, belge işlemlerini saklar.


</div>


<div class="mw-translate-fuzzy">

-   **Yerleşik [betik](Scripting.md) framework\'u** : FreeCAD, yerleşik bir [Python](http://www.python.org/) yorumlayıcısı ve uygulamanın hemen hemen her bölümünü, arayüzü, geometriyi ve bu geometrinin 3D görüntüleyicideki temsilini kapsayan bir API\'ye sahiptir. Yorumlayıcı, karmaşık komut dosyalarına kadar tek bir komut çalıştırabilir, hatta tüm modüller Python\'da bile tamamen programlanabilir.


</div>


<div class="mw-translate-fuzzy">

-   **Yerleşik Python konsolu** söz dizim vurgulaması, otomatik tamamlama ve sınıf tarayıcısına sahip: Python komutları doğrudan FreeCAD\'e verilebilir ve anında sonuç döndürür, anında kod yazarlarının işlevselliği test etmesine, modüllerin içeriğini keşfetmesine ve FreeCAD içindekileri kolayca öğrenmesine izin verir.


</div>


<div class="mw-translate-fuzzy">

-   **Konsolda kullanıcı etkileşimi yansıtma**: Kullanıcının FreeCAD arayüzünde yaptığı her şey, konsolda basılabilen ve makrolara kaydedilebilen Python kodunu çalıştırır.


</div>


<div class="mw-translate-fuzzy">

-   **Tam makro kayıt ve düzenleme** : Kullanıcı, arayüzü kullandığında, verilen Python komutları daha sonra kaydedilebilir, gerekirse düzenlenebilir ve daha sonra yeniden üretilmek üzere kaydedilebilir.


</div>


<div class="mw-translate-fuzzy">

-   **Bileşik (ZIP tabanlı) belge kaydetme formatı** : FreeCAD belgeleri [fcstd](fcstd_file_format.md) uzantısı ile kaydedilir ve içeriğinde geometri, komut dosyaları veya küçük resim simgeleri gibi birçok farklı türde bilgi bulunabilir. .Fcstd dosyasının kendisi bir zip konteyneridir, bu nedenle kaydedilmiş bir FreeCAD dosyası zaten sıkıştırılmıştır.


</div>


<div class="mw-translate-fuzzy">

-   **Tamamen özelleştirilebilir/betik Grafik Kullanıcı Arayüzü** . [Qt](http://www.qtsoftware.com) tabanlı FreeCAD arayüzü, Python yorumlayıcısı aracılığıyla tamamen erişilebilir. FreeCAD\'in çalışma tezgahlarına sağladığı basit fonksiyonların yanı sıra, tüm Qt framework\' te erişilebilir, böylece GUI üzerinde widget\'lar ve araç çubukları oluşturma, ekleme, yerleştirme, değiştirme veya kaldırma gibi herhangi bir işlem yapılabilir.


</div>


<div class="mw-translate-fuzzy">

-   **Simge**(şu anda yalnızca Linux sistemleri): FreeCAD belge simgeleri, Gnome\'s Nautilus gibi çoğu dosya yöneticisi uygulamasında dosyanın içeriğini gösterir.


</div>


<div class="mw-translate-fuzzy">

-   **Modüler bir MSI kurulum programı**, Windows sistemlerinde esnek kurulumlara izin verir. Ubuntu sistemleri için paketler de yapılmaktadır.


</div>

## Geliştirme aşamasında 


<div class="mw-translate-fuzzy">

-   ![](images/Feature-assembly.jpg ) Birden fazla proje, birden fazla şekil, birden fazla belge, birden fazla dosya, birden fazla ilişkiyle çalışmanıza izin veren bir [Montaj](Assembly_project.md) modülü \... Bu modül şu anda planlama aşamasındadır.


</div>


<div class="mw-translate-fuzzy">

## Ekstra Tezgahlar 

Uzman kullanıcılar, çeşitli özel [dış tezgahlar](external_workbenches.md) oluşturuyorlar.


</div>


<div class="mw-translate-fuzzy">


{{docnav/tr|[FreeCAD Hakkında](About_FreeCAD/tr.md)|[Windows'ta Kurulum](Install_on_Windows/tr.md)}}


</div>




[Category:User Documentation](Category:User_Documentation.md)

---
[documentation index](../README.md) > [User Documentation](Category:User Documentation.md) > Feature list/tr
