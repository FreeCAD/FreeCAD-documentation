# Localisation Sidebar/tr
<div class="mw-translate-fuzzy">

[Yerelleştirme](Localisation/tr.md), çoklu dil kullanıcı arabirimiyle yazılım sağlama işlemidir. wiki Dokümantasyonu, [Localisation \# Wiki\'nin çevrilmesi](Localisation_#_Wiki'nin_çevrilmesi.md) bölümünde açıklandığı gibi yerelleştirilebilir.


</div>

Kenar çubuğu wiki dünyasında önemli bir gezinme aracıdır, daha fazla bilgi için [Manual: Interface / Sidebar](http://www.mediawiki.org/wiki/Manual:Interface/Sidebar) bölümüne bakın.

## Kenar çubuğunu çevir 

Kenar çubuğu artık wiki\'nin tüm sayfalarında bulunan [Translation extension](http://www.mediawiki.org/wiki/Help:Extension:Translate) ile tamamen çevrilebilir.

FreeCAD wiki\'de, kenar çubuğu seçilen dile bağlı olarak metni değiştiren şablonlar kullanılarak uygulanır. Bu özelliğin nasıl uygulandığına dair teknik detaylar forum başlığında [Wiki navigasyon / çeviri](http://forum.freecadweb.org/viewtopic.php?f=21&t=9687&start=10#p80441) açıklanmaktadır.

### Talimatlar

Çeviriye başlamak için özel [Special:Translate/wiki-sidebar](Special:Translate/wiki-sidebar.md) özel sayfasına gidebilirsiniz.

İndirme sayfasında bir hata var. Bağlantıyı \"Download/fr\" veya \"Download/de\" vb. Sayfalarına yönlendiremezsiniz. Bunun yerine, bağlantı kendi dilinizde \"İndirme\" gerçek çevirisini gösterecektir. Başa çıkmanın en iyi yolu bu yeni sayfayı oluşturmak ve doğru sayfaya yönlendirme yapmaktır. Yönlendirme hakkında daha fazlası [Yardım: Düzenleme](Help:Editing/tr.md).

### Önemli notlar 

Çoğu zaman kenar çubuğundaki her öğe için iki dize olacaktır.

** {{int:sidebar-faq-target}}|sidebar-faq

Soldaki link bağlantının hedefini, sağdaki ise kenar çubuğunda görüntülenecek metni temsil eder.

İkisi arasındaki farkı, değişkenin adının görüntülendiği çeviri kutusunun üstüne bakarak görebilirsiniz. Değişken ismi \"-target\" ile bitiyorsa, bu bir hedef link çevireceğiniz anlamına gelir. Tercümana izin vermek için yapıldı öğeleri çevrilmiş sayfalara yönlendirmek, diğer bir deyişle sayfa adının sonuna bir dil kodu ekleyerek, örneğin bir Fransızca çeviri için \"/ fr\".

\"/ fr\", \"/ de\", \"/ es\", \"/ ru\" dil kodlarını eklemeyin, eğer çevrilen sayfa bu dilde mevcut değilse, bağlantıyı kesecektir. Bu durumda, sayfanın adından başka bir şey yazmayın, aksi takdirde bağlantı kopar.

![Where to look](images/Translate-sidebar-instruction.png )



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Wiki](Category_Wiki.md) > Localisation Sidebar/tr
