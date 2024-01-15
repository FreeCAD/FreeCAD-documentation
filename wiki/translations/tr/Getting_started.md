# Getting started/tr
## Önsöz


<div class="mw-translate-fuzzy">

FreeCad, bir 3D CAD/CAE [parametrik modelleme uygulamasıdır.](About_FreeCAD/tr.md) Öncelikle mekanik tasarım için üretilmiş olup, aynı zamanda hassasiyet isteyen 3D modelleme ile model kayıtları üzerinde ayarlama gerektiren tüm alanlarda kullanılabilir.


</div>


<div class="mw-translate-fuzzy">

FreeCAD geliştirme süreci devam etmekte olup, şu anda bir çok [özellik](Feature_list/tr.md) barındırmaktadır. Özellikle ücretli emsalleriyle karşılaştırıldığında halen yeterli araçlara sahip olmamasına karşın, hobi alanında ve küçük atölyelerde ihtiyaçları karşılayabilecek yetenektedir. Hızla büyüyen, gönüllü kullanıcıların bulunduğu [FreeCAD forum](http://forum.freecadweb.org/index.php)\'a katılarak, FreeCAD\'le hazırlanmış [birçok kaliteli projeyi](https://forum.freecadweb.org/viewforum.php?f=24) inceleyebilirsiniz.


</div>


<div class="mw-translate-fuzzy">

Tüm açık kaynak kodlu projelerde olduğu gibi, FreeCAD projesi de geliştiriciler tarafından size sunulan tek yönlü bir çalışma değildir. Gelişmesi, yeni özellikler kazanması ve kararlı(hataların düzeltilmesi) hale gelmesi kullanıcı topluluğuna bağlıdır. FreeCAD kullanırken unutmayın; eğer FreeCAD kullanmak hoşunuza gittiyse, sizde FreeCAD\'in geliştirilmesine katkı sağlayabilir ve [FreeCAD\'e yardım ](help_FreeCAD.md) edebilirsiniz!


</div>

See also:

-   [Migrating to FreeCAD from Fusion360](Migrating_to_FreeCAD_from_Fusion360.md)
-   [Which workbench should I choose?](Which_workbench_should_I_choose.md)
-   [Tutorials](Tutorials.md)
-   [Video tutorials](Video_tutorials.md)



## Yükleme


<div class="mw-translate-fuzzy">

Her şeyden önce, FreeCAD\'i indirin ve kurun. Güncel sürüm ve güncellemeler hakkında bilgi almak için [İndirme](Download.md) sayfasını ve Yükleme talimatları için [Yükleme](Installing.md) sayfasını ziyaret ediniz.Windows(.msi), Debian ve Ubuntu(.deb), openSUSE(.rpm) ve Mac OSX işletim sistemlerine yönelik Yükleme dosyaları mevcuttur. FreeCAD, diğer birçok Linux dağıtımında paket yöneticilerinden ulaşılabilir. Ayrıca güncel 64-bit Linux sistemlerde tek başına çalıştırılabilir [AppImage](https://appimage.org/) da bulunmaktadır. FreeCAD açık kaynak kodlu olduğu için, kaynak kodunu indirip, kendiniz de [derleyebilirsiniz.](Compiling.md)


</div>




<div class="mw-translate-fuzzy">

## FreeCAD\'i Keşfedin 


</div>

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_interface.png  style="width:1024px;">


</div>


<div class="mw-translate-fuzzy">

1.  3D görünüm alanı, belge içeriğini gösterir.
2.  Ağaç görünüm alanı, belge içeriğindeki tüm nesnelerin hiyerarşisini ve yapım aşamalarını gösterir.
3.  [Özellik editörü](property_editor.md), seçilen nesnenin özellikleri görüntülenebilir veya değişiklikler yapılabilir.
4.  Rapor görünüm alanı (veya çıktı penceresi), FreeCAD\'e ait mesajlar,uyarılar ve hata mesajları görüntülenir.
5.  Python konsolu(komut satırı), FreeCAD tarafından çalıştırılan tüm komutlar görüntülenir ve Python kodu yazılabilir.
6.  [Tezgah seçici](Workbenches.md), aktif tezgahın seçildiği yer.


</div>


<div class="mw-translate-fuzzy">

FreeCAD arayüzünün arkasındaki anlayış, onun çalışma tezgahlarına ayrılmasıdır.Bir çalışma tezgahı, [Mesh çizimi](Mesh_Workbench.md) veya [2D nesnelerin](Draft_Workbench.md) çizimi veya [limitli taslaklar](Sketcher_Workbench.md) gibi belirli işler için uygun araçlardan oluşan koleksiyondur.Aktif çalışma tezgahı, Tezgah seçiciden değiştirilebilir(6).Her tezgah içerisinde bulunan araçlar, diğer tezgahlardan ve [makro](macros.md) olarak adlandırılan kullanıcı tarafından oluşturulan araçlar da eklenerek [özelleştirilebilir](Interface_Customization.md). [Parça dizaynı tezgahı](PartDesign_Workbench.md) ve [Parça tezgahı](Part_Workbench.md), yaygın olarak kullanılan, çalışma başlangıç noktalarıdır.


</div>


<div class="mw-translate-fuzzy">

FreeCAD ilk çalıştırıldığında, karşılama ekranı olarak başlangıç merkezi açılır.Sürüm 0.16 \'ya ait karşılama ekranı görüntüdeki gibidir.


</div>

<img alt="" src=images/Start_center_0.19_screenshot.png  style="width:600px;">


<div class="mw-translate-fuzzy">

Başlangıç Merkezi ile yaygın olarak kullanılan tezgahları kolayca seçebilir, son kullanılan dosyaları açabilir veya FreeCAD dünyasından en son haberleri görebilirsiniz. Varsayılan çalışma tezgahını [tercih ayarlarından](Preferences_Editor.md) değiştirebilirsiniz.


</div>



## 3D alanında gezinme 


<div class="mw-translate-fuzzy">

FreeCAD\'in, farenizi, 3D görünümdeki nesnelerle ve görünümün kendisi ile etkileşimde bulunma şeklini değiştiren çeşitli [gezinme yöntemi](Mouse_Model.md) vardır. Bunlardan biri özellikle fare orta tuşunun kullanılmadığı [dokunmatik](Mouse_Model#Touchpad_Navigation.md) yüzeyler için üretilmiştir. Aşağıdaki tabloda, CAD Gezinme adı verilen, varsayılan mod açıklanmaktadır (3D görünümün boş bir alanına sağ tıklayarak mevcut gezinme modunu hızlı bir şekilde değiştirebilirsiniz):


</div>

Ayrıca Görünüm menüsünde, Görünüm araç çubuğunda ve sayı kısayol tuşlarıyla (**1**, **2**, vb\...). kullanılabilen ön tanımlı(üstten görünüm, önden görünüm vb.) görünümleri kullanabilirsiniz. Bir nesne üzerinde veya 3D görünümde boş alanda sağ tıklayarak, özel görünüm seçebilir veya Ağaç görünümünde bir nesnenin yerini bulma gibi bazı genel işlemlere hızlı bir şekilde ulaşabilirsiniz.



## FreeCAD\'le İlk Adımlar 


<div class="mw-translate-fuzzy">

FreeCAD\'in odak noktası, yüksek hassasiyete sahip 3D modeller yapmanız, bu modellerin üzerinde sıkı bir kontrole sahip olmanız (modelleme geçmişine geri dönebilme ve parametreleri değiştirebilme) ve sonuç olarak bu modelleri (3D baskı alma, CNC ile işleme ve hatta inşaat şantiyesinde kullanım) yapmanızdır. Bu nedenle, animasyon filmi veya oyun gibi başka amaçlar için yapılmış diğer 3D uygulamalardan çok farklıdır. İlk defa 3D modelleme yapmaya başlıyorsanız, programı kullanmayı öğrenmek biraz karmaşık gelebilir. Kafanız karıştığında veya zorlandığınızda, unutmayın, zaman kaybetmeden dostça karşılanacağınız kullanıcı topluluğundan oluşan [FreeCAD forum\'dan](http://forum.freecadweb.org/index.php) yardım isteyebilirsiniz.


</div>


<div class="mw-translate-fuzzy">

FreeCAD\'de kullanmaya başlayacağınız çalışma tezgahı, yapacağınız işin türüne bağlıdır: Eğer mekanik modeller veya daha genel olarak küçük ölçekli nesneler üzerinde çalışacaksanız, muhtemelen [Parça Dizaynı(PartDesign)](PartDesign_Workbench.md) çalışma tezgahını kullanmayı tercih edeceksiniz. 2D\'de çalışacaksanız, kısıtlamalara ihtiyacınız varsa , [Ön Taslak Tezgahına](Draft_Workbench.md) veya [Taslak(Eskiz) tezgahına](Sketcher_Workbench.md) geçin. Eğer BIM(Building information modelling -Yapı Bilgi Modelleme) yapacaksanız [Yapı Tezgahını](Arch_Workbench.md) kullanabilirsiniz.Eğer gemi tasarımıyla uğraşıyorsanız,bu işe özel olarak [Gemi tezgahı](Ship_Workbench.md) bulunmaktadır. Eğer OpenSCAD kullanıcı iseniz [OpenSCAD tezgahın](OpenSCAD_Workbench.md)ı kullanabilirsiniz. There are also many community-developed [external workbenches](External_workbenches.md) available.


</div>


<div class="mw-translate-fuzzy">

Çalışma tezgahlarını istediğiniz zaman değiştirebilir ve diğer çalışma tezgahlarından araç eklemek için favori çalışma tablasını da [özelleştirebilirsiniz](Interface_Customization.md).


</div>



## Parça Dizaynı ve Eskiz tezgahlarıyla çalışma 


<div class="mw-translate-fuzzy">

[Parça Dizayn Tezgahı](PartDesign_Workbench.md), yapmak istediğiniz nesneyi elde edene kadar, basit şekillerden başlayarak, bu şekillere eklemeler veya çıkarımlar yaparak(biz buna özellikler diyoruz) özellikle kompleks nesneler elde etmek için tasarlandı.Modelleme işlemi sırasında uyguladığınız tüm özellikler , belgenizdeki diğer nesneleri de içeren [Ağaç Görünümü](Document_structure.md) olarak adlandırılan ayrı bir görünümde kaydedilir. Parça Dizayn nesnesini, her biri bir öncekinin sonucuna uygulanan, büyük bir zincir oluşturan, birbirini takip eden işlemler olarak düşünebilirsiniz. Ağaç görünümünde, nesnenin son halini görürsünüz, ancak onu genişletebilir ve önceki tüm durumlara erişebilir ve son nesneyi otomatik olarak güncelleyen, herhangi bir parametreyi değiştirebilirsiniz.


</div>


<div class="mw-translate-fuzzy">

Parça Dizayn Tezgahı,diğer bir tezgahı,[Eskiz Tezgahın](Sketcher_Workbench.md)ı çok sık kullanır. Eskiz,2D çizilen şekilleri, ölçülendirilmiş 2D şekile çevirmenizi sağlar. Örneğin,bir dikdörtgen çizebilir ve kenarlardan birine uzunluk ölçüsü vererek diğer tarafın boyutunu ayarlayabilirsiniz. Ayarlanan tarafın ölçüsü (yapılan ayar değiştirilmedikçe) değiştirilemez.


</div>

Eskiz ile yapılan bu 2D şekiller, Parça Dizayn tezgahında çok fazla kullanılır, örneğin 3D nesne oluşturmak veya nesnenizin gövdesinden oyulacak alanların yüzeylerini çizmek gibi. Tipik bir Parça Dizayn tezgah iş akışı aşağıdaki gibidir:

1.  Yeni bir eskiz oluşturun
2.  Kapalı bir şekil çizin(tüm noktaların birleştirildiğinden emin olun)
3.  Eskizi kapatın
4.  Kalınlık ver aracıyla 3D katıya dönüştürün.
5.  Katı üzerinde bir yüz seçin
6.  İkinci bir eskiz oluşturun(Eskiz seçilen yüz üzerinde çizilmelidir)
7.  Kapalı bir şekil çizin
8.  Eskizi kapatın
9.  İlk nesne üzerinde, ikinci eskizden bir cep oluşturun.(Eskize derinlik vererek nesne üzerinde, eskiz kadar kısmı nesneden çıkarmış oluyoruz)

Yapılan işlemler sonucunda elde edilen nesne şuna benzer:

<img alt="" src=images/Partdesign_example.jpg  style="width:600px;">

İstediğiniz zaman, özgün eskizi seçerek ve yeniden şekillendirerek, kalınlık veya cep işlem parametrelerini değiştirerek, istenen nesneyi elde edilebilirsiniz.



## Taslak ve Yapı tezgahlarıyla çalışma 


<div class="mw-translate-fuzzy">

[Taslak Tezgahı](Draft_Workbench.md) ve [Yapı Tezgahı](Arch_Workbench.md) , FreeCAD\'de aynı temel kurallar çerçevesinde işlese de yukarıdaki tezgahlardan biraz farklıdırlar. Kısacası, Eskiz ve Parça Dizayn öncelikli olarak tek parça oluşturmak için kullanılırken; Taslak ve Yapı, işleri kolaylaştırmak için birçok basit nesneyle çalışmak için kullanılır.


</div>


<div class="mw-translate-fuzzy">

[Taslak tezgahı](Draft_Workbench.md), [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD) gibi 2D CAD uygulamalarında bulunan geleneksel 2D çizim araçlarına benzerdir. 2D çizim FreeCAD\'in kapsama alanında olmadığından, bu alana özel uygulamaların sunduğu araçların tamamını bulmayı beklemeyin. Taslak araçlarının çoğu sadece 2D düzlemde değil, aynı zamanda 3D alanında ve [ Work planes (Çalışma Yüzeyleri)](Draft_SelectPlane.md) ile [Nesne Yakalamada](Draft_Snap.md) kullanılmaktadır.


</div>


<div class="mw-translate-fuzzy">

[Yapı Tezgahı](Arch_Workbench.md),FreeCAD\'e eklediği [BIM(Yapı bilgi modelleme)](http://en.wikipedia.org/wiki/Building_Information_Modeling) araçlarla, parametreli nesnelerden oluşan mimari modeller yapmanızı sağlar. Yapı tezgahı, Taslak ve Eskiz gibi tezgahlarla birlikte sık kullanılır. Tüm Taslak araçları ayrıca Yapı tezgahında bulunur ve çoğu Yapı aracı Taslak yardımcı sistemlerini kullanır.


</div>

Tipik bir Yapı ve Taslak tezgahı iş akışı şu şekildedir:

1.  Taslak çizgi aracıyla birkaç çizgi çizin
2.  Çizgi seçerek ve Duvar aracına tıklayarak, her çizgiyi duvara çevirin
3.  Duvar seçerek ve Yapı araçlarını kullanarak düzenlemeye geçin
4.  Bir zemin nesnesi oluşturun ve Ağaç görünümünde duvarınızı onun içine taşıyın
5.  Bir bina nesnesi oluşturun ve Ağaç görünümünde zemininizi onun içine taşıyın
6.  Pencere aracını tıklayarak bir pencere oluşturun, panelinde ön ayarları seçin ve duvar yüzüne tıklayın
7.  Eğer gerekiyorsa ilk önce çalışma düzlemini ayarlayın ve Taslak ölçü aracıyla ölçülendirin

Buna benzer bir şekil elde edeceksiniz:

<img alt="" src=images/Arch_workflow_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

Daha fazlası için [Kullanım Kılavuzu](Tutorials/tr.md) sayfasına bakınız.


</div>




<div class="mw-translate-fuzzy">

## Betik


</div>

FreeCAD, as an open source software, offers the possibility to supplement its workbenches with addons.

The [Addon](Addon.md) principle is based on the development of a workbench complement. Any user can develop a function that he or she deems to be missing for her/his own needs or, ultimately, for the community. With the forum, the user can request an opinion, help on the forum. It can share, or not, the object of its development according to copyright rules to define. Free to her/him. To develop, the user has available [scripting](scripting.md) functions.

There are two types of addons:

1.  [Macros](Macros.md): short snippets of Python code that provide a new tool or functionality. Macros usually start as a way to simplify or automate the task of drawing or editing a particular object. If many of these macros are collected inside a directory, the entire directory may be distributed as a new workbench.
2.  [External workbenches](External_workbenches.md): collections of tools programmed in Python or C++ that extend FreeCAD in an important way. If a workbench is sufficiently developed and is well documented, it may be included as one of the base workbenches in FreeCAD. Under [External workbenches](External_workbenches.md), you\'ll find the principle and a list of existing library.

## Scripting


<div class="mw-translate-fuzzy">

Son olarak, FreeCAD\'in en güçlü özelliklerinden biri [betik](Power_users_hub/tr.md) ortamıdır.Entegre python konsolundan (veya diğer herhangi bir harici Python betiğinden), FreeCAD\'in hemen her bölümüne erişebilir, geometri oluşturabilir veya değiştirebilir, 3D sahnede bu nesnelerin temsilini değiştirebilir veya FreeCAD arayüzüne erişebilir ve değiştirebilirsiniz. Python komut dosyası, özel komutlar oluşturmak için kolay bir yöntem sağlayan makrolarda da kullanılabilir .


</div>




<div class="mw-translate-fuzzy">

## Yenilikler


</div>


<div class="mw-translate-fuzzy">

-   [Sürüm 0.17 Sürüm Notları](Release_notes_0.17.md) : FreeCAD\'in 0.17 sürümündeki yenilikler nelerdir?
-   [Sürüm 0.16 Sürüm Notları](Release_notes_0.16.md) : FreeCAD\'in 0.16 sürümündeki yenilikler nelerdir?
-   [Sürüm 0.15 Sürüm Notları](Release_notes_0.15.md) : FreeCAD\'in 0.15 sürümündeki yenilikler nelerdir?
-   [Sürüm 0.14 Sürüm Notları](Release_notes_0.14.md) : FreeCAD\'in 0.14 sürümündeki yenilikler nelerdir?
-   [Sürüm 0.13 Sürüm Notları](Release_notes_0.13.md) : FreeCAD\'in 0.13 sürümündeki yenilikler nelerdir?
-   [Sürüm 0.12 Sürüm Notları](Release_notes_0.12.md) : FreeCAD\'in 0.12 sürümündeki yenilikler nelerdir?
-   [Sürüm 0.11 Sürüm Notları](Release_notes_0.11.md) : FreeCAD\'in 0.11 sürümündeki yenilikler nelerdir?


</div>


<div class="mw-translate-fuzzy">


{{docnav/tr|[Mac icin Kurulum](Install_on_Mac/tr.md)|[Fare ile 3D Gezinme](Mouse_Model/tr.md)}}


</div>




[Kullanıcı Belgeleri](Category:User_Documentation/tr.md)



---
⏵ [documentation index](../README.md) > Getting started/tr
