


<div class="mw-translate-fuzzy">


{{docnav|[Markalama](Branding/tr.md)|[Ekstra python modülleri](Extra_python_modules/tr.md)}}


</div>


{{TOCright}}


<div class="mw-translate-fuzzy">

**Yerelleştirme** genel olarak bir Yazılımın çok dilli bir kullanıcı arayüzüne sahip olma sürecidir. FreeCAD\'de kullanıcı arayüzünün dilini *Düzenle → Seçenekler → Uygulama* altında ayarlayabilirsiniz. FreeCAD çoklu dil desteğini etkinleştirmek için [Qt](wikipedia:Qt(toolkit).md) kullanır. Unix / Linux sistemlerinde, FreeCAD sisteminizin mevcut yerel ayarlarını varsayılan olarak kullanır.


</div>

**Localisation** is in general the process of providing a Software with a multiple language user interface. In FreeCAD you can set the language of the user interface under **Edit → Preferences → General**. FreeCAD uses [Qt](wikipedia:Qt_(toolkit).md) to enable multiple language support. On Unix/Linux systems, FreeCAD uses the current locale settings of your system by default.

## FreeCAD\'i çevirme de yardım 

Kullanıcıların FreeCAD\'e katkıda bulunabilecekleri çok önemli şeylerden biri (örneğin programlama becerileri yoksa), farklı yönlerini (kaynak kodu, wiki, web sitesi, dokümantasyon vb.) Başka bir dile çevirmeye yardımcı olmaktır. İşte bunu yapmanın yolları


<div class="mw-translate-fuzzy">

## FreeCAD kaynak kodunu çevirin 

FreeCAD, [Crowdin](https://crowdin.net) adlı üçüncü taraf işbirlikçi çevrimiçi çeviri sistemini kullanmaktadır. Crowdin, özel bir yazılımdır ancak FOSS(Free and Open Source Software, Ücretsiz ve açık kaynak yazılım) projelerine ücretsizdir. Aşağıda nasıl kullanılacağına ilişkin talimatlar verilmiştir:


</div>

FreeCAD utilizes a third party collaborative on-line translation system called [Crowdin](https://crowdin.net).

<img alt="" src=images/Logo-crowdin.png  style="width:320px;">

It is proprietary software but free to FOSS projects. Below are instructions on how to use it:


<div class="mw-translate-fuzzy">

-   Crowdin\'deki [FreeCAD çeviri projesi sayfasına](http://crowdin.net/project/freecad) gidin.
-   Yeni bir profil oluşturarak veya bir üçüncü taraf hesabı kullanarak giriş yapın (GitHub, GitLab, GMail vb \...)
-   Tercüme etmek istediğiniz dile tıklayın
-   Dosyalardan birinin yanındaki Çevir düğmesine tıklayarak çeviri işlemine başlayın. Örneğin, *FreeCAD.ts*, FreeCAD ana GUI\'sinin metin dizelerini içerir.
-   Mevcut çeviriler için oy kullanabilir veya kendinizinkini oluşturabilirsiniz.


</div>

{{Message| FreeCAD çevirisinde aktif olarak yer alıyorsanız ve bir sonraki sürüm başlatılmaya hazır olmadan önce bilgilendirilmek istiyorsanız, çevirinizi incelemek için zamanınız varsa, lütfen Crowdin FreeCAD çeviri ekiplerinden birine abone olun.}}


**Note:**

Details on how to use crowdin can be found on the [Crowdin Administration](Crowdin_Administration.md) page.

## Translating external workbenches 

Visit [Translating an external workbench](Translating_an_external_workbench.md).

## FreeCAD wiki\'sini çevirin 


<div class="mw-translate-fuzzy">

Bu wiki, çoğu el kitabından oluşan birçok içeriğe ev sahipliği yapıyor. [Ana Sayfa](Main_Page/tr.md) \'dan başlayarak belgelere göz atabilir veya [Kullanım kılavuzuna](Online_Help_Toc/tr.md) göz atabilirsiniz.


</div>


<div class="mw-translate-fuzzy">

Wikiyi çevirmek için, wiki düzenleme izninizin olması gerekir; bkz. [ Wiki\'de nasıl düzenleme iznini alabilirim?](FAQ#How_can_I_get_edit_permission_on_the_wiki?.md).


</div>


<div class="mw-translate-fuzzy">

Ayrıca, wiki işaretlemesi hakkında yeterli bilgiye sahip olmalı ve [WikiPages](WikiPages.md) bölümünde açıklanan genel şekillendirme kurallarına uymalısınız.


</div>

### Mediawiki Çeviri Uzantısı 

Wiki SourceForge\'dan uzaklaştığında, [Yorik](User:Yorik.md), sayfaların çevrilmesini kolaylaştıran [MediaWiki\'nin Çeviri eklentisini](http://www.mediawiki.org/wiki/Help:Extension:Translate) kurdu. Çeviri uzantısının avantajları, sayfa başlığının artık çevrilebilmesi, çevirilerin kaydını tutması, orijinal sayfanın güncellendiğini bildirmesi ve çevirileri orijinal İngilizce sayfasıyla senkronize olarak tutmasıdır.

Bu araç [Help: Extension: Translate](http://www.mediawiki.org/wiki/Help:Extension:Translate) bölümünde belgelenmiştir ve [MediaWiki Dilinin Uzatma Paketi](http://www.mediawiki.org/wiki/MediaWiki_Language_Extension_Bundle)nin bir parçasıdır.

Çeviri için bir sayfa hazırlamaya hemen başlamak için, lütfen [Sayfa çeviri örneğini](http://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example) okuyun. Temel olarak, çeviri sistemini etkinleştirmek için tüm sayfayı çevreleyen bir çift

    &lt;translate&gt; ... &lt;/translate&gt;

etiketi olmalı ve sayfanın çeviri için işaretlenmesi gerekir.


<div class="mw-translate-fuzzy">

Çeviri aracının nasıl çalıştığına dair bir örnek görmek için [Ana Sayfa](Main_Page/tr.md) sayfasını ziyaret edin. En üstte otomatik olarak oluşturulan bir dil çubuğu göreceksiniz. [Türkçe](Main_Page/tr.md) üzerine tıkladığınızda [Main Page/tr](Main_Page/tr.md) bölümüne ulaşacaksınız. Başlığın hemen altında, \"Bu sayfa, sayfanın çevrilmiş bir sürümüdür ve çeviri% XX tamamlandı.\" Yazısını, XX\'nin geçerli çeviri yüzdesi olduğunu görebilirsiniz. Mevcut çeviriyi güncellemek, düzeltmek ve incelemek üzere çeviri yardımcı programını başlatmak için sayfanın üstündeki \"Çevir\" düğmesini tıklayın.


</div>


<div class="mw-translate-fuzzy">

[Main Page/tr](Main_Page/tr.md) \'ye giderseniz, \"Düzenle\" etiketine tıklayarak düzenleme yapamayacağınızı farkedersiniz, çünkü \"Düzenle\" etiketi yerine \"Çevir\" etiketi ile çeviri aracı açılacaktır.


</div>

Yeni içerik eklerken, önce İngilizce sayfa oluşturulmalı, sonra başka bir dile çevrilmelidir. Birisi bir sayfaya içerik değiştirmek veya eklemek isterse, önce İngilizce sayfanın değiştirilmesi gerekir.


<div class="mw-translate-fuzzy">

Çevirilere nasıl devam edeceğiniz konusunda emin değilseniz, Geliştirme/Wiki alt forumunda veya [FreeCAD forumundaki](http://forum.freecadweb.org) belirli bir dil alt forumunda yardım almaktan çekinmeyin.


</div>

### Önemli notlar 


<div class="mw-translate-fuzzy">

\"Editör\" izinlerine sahip her wiki kullanıcısı, çeviri aracını başlatabilir ve çevirileri yazabilir, kaydedebilir ve inceleyebilir.


</div>

Ancak, yalnızca \"Yönetici\" izinlerine sahip kullanıcılar çeviri için sayfaları işaretleyebilir. Çeviri için işaretlenmemiş bir sayfa çeviri uzantısını kullanmaz ve İngilizce bilgilerle doğru bir şekilde senkronize edilmez.


<div class="mw-translate-fuzzy">

Sol kenar çubuğu da çevrilebilir ancak sitenin bu öğesini yalnızca Yöneticiler değiştirebilir. Lütfen [Yerelleştirme Kenar Çubuğu](Localisation_Sidebar/tr.md) ile ilgili talimatları izleyin.


</div>

Bir sayfayı yeni çeviri sistemine ilk kez çevirdiğinizde, eski \"manuel\" çevirilerinin tümünü kaybeder. Bir çeviriyi kurtarmak için, eski metnin çevrimdışı bir kopyasını geçiş yapmadan önce kaydetmelisiniz. Daha sonra bu eski çevrilmiş metni, yeni sistemdeki çeviri birimlerini doldurmak için kullanabilirsiniz. Ayrıca tarihin önceki bir sürümünü açabilir ve eski metni bu şekilde alabilirsiniz. Bu, çevrilmiş bir sayfa olan her dil için yapılmalıdır.


<div class="mw-translate-fuzzy">

## FreeCAD belgelerini çevirin 


</div>

As per general consensus, the reference page in the wiki is the English page, which should be created first. If you want to change or add content to a page, you should do it to the English page first, and only once the update is completed, port the modification to the translated page.

### Eski çeviri talimatları 


<div class="mw-translate-fuzzy">

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| These instructions are for historical background only. Translations should use the new system with the [\#Mediawiki Translation Extension](#Mediawiki_Translation_Extension.md) described above.                                                                                                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| So the first step is to **check if the manual translation has already been started for your language** (look in the left sidebar, under \"manual\").                                                                                                                                                                                                                                                                                                                                                                                                                     |
| If not, head to the [forum](http://forum.freecadweb.org/) and say that you want to start a new translation, we\'ll create the basic setup for the language you want to work on.                                                                                                                                                                                                                                                                                                                                                                                          |
| You must then [gain wiki edit permission](FAQ#How_can_I_get_edit_permission_on_the_wiki.3F.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| If your language is already listed, see what pages are still missing a translation (they will be listed in red). The technique is simple: **go into a red page, and copy/paste the contents of the corresponding English page, and start translating**.                                                                                                                                                                                                                                                                                                                  |
| Do not forget to include all the tags and templates from the original English page. Some of those templates will have an equivalent in your language (for example, there is a French Docnav template called Docnav/fr). You should use **a slash and your language code** in almost all the links. Look at other already translated pages to see how they did it.                                                                                                                                                                                                        |
| Add a slash and your language code in the categories, like \[\[Category:Developer Documentation/fr\]\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| And if you are unsure, head to the forums and ask people to check what you did and tell you if it\'s right or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Four templates are commonly used in manual pages. These 4 templates have localized versions (Template:Docnav/fr, Template:fr, etc\...)                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -   [Template:GuiCommand](Template:GuiCommand.md) : is the Gui Command information block in upper-right of command documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -   [Template:Docnav](Template:Docnav.md) : it is the navigation bar at the bottom of the pages, showing previous and next pages.                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| \'\'\' Page Naming Convention \'\'\'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Please take note that, due to limitations in the Sourceforge implementation of the MediaWiki engine, we require that your pages all keep their original English counterpart\'s name, appending a slash and your language code. For example, the translated page for About FreeCAD should be About Freecad/es for Spanish, About FreeCAD/pl for polish, etc. The reason is simple: so that if translators go away, the wiki\'s administrators, who do not speak all languages, will know what these pages are for. This will facilitate maintenance and avoid lost pages. |
| If you want the Docnav template to show linked pages in your language, you can use **redirect pages**. They are basically shortcut links to the actual page. Here is an example with the French page for About FreeCAD.                                                                                                                                                                                                                                                                                                                                                  |
| \* The page About FreeCAD/fr is the page with content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -   The page À propos de FreeCAD contains this code:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| #REDIRECT [[About FreeCAD/fr]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -   In the About FreeCAD/fr page, the Docnav code will look like this:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| {{docnav/fr|Bienvenue sur l'aide en ligne|Fonctionnalités}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| The page \"Bienvenue sur l\'aide en ligne\" redirects to Online Help Startpage/fr, and the page \"Fonctionnalités\" redirects to Feature list/fr.                                                                                                                                                                                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


</div>


<div class="mw-translate-fuzzy">

## FreeCAD web sitesini çevirin 

FreeCAD web sitesinin çevirisi şimdi [Crowdin](https://crowdin.com/translate/freecad/561/en-en) üzerinden yapılıyor. Dosya **homepage.po** olarak adlandırıldı.


</div>

Translation of the FreeCAD website is now done through [Crowdin](https://crowdin.com/translate/freecad/561/en-en). The file is named {{FileName|homepage.po}}.


<div class="mw-translate-fuzzy">

## Geliştirme - Yerelleştirme Ekleme 

Bu bölüm, kodlarına yerelleştirme eklemek isteyen geliştiriciler içindir.


</div>

This section is for developers who want to add localisation to their code.


<div class="mw-translate-fuzzy">

### FreeCAD / master modüllerinizi çeviri için hazırlama 

Bunlar FreeCAD çeviri sürecinin parçalarıdır:

-   Kaynak koddan metin dizeleri \* .ts dosyaları içine ayıklamak
-   \* .ts dosyalarını [FreeCAD Crowdin](http://crowdin.net/project/freecad) \'e yükleyin.
-   Crowdin içindeki karakterlerin çevirisi
-   Crowdin\'den değiştirilmiş / yeni \* .ts dosyaları çıkartma
-   convert \* .ts dosyaları \* .qm dosyalarına ve her modülün \* .qrc dosyasını güncelleyin
-   FreeCAD master\'ı güncelle


</div>

These are the parts to the FreeCAD translation process:

-   extract text strings from source code into \*.ts files
-   load \*.ts files into [FreeCAD Crowdin](http://crowdin.net/project/freecad).
-   translation of strings within Crowdin
-   extract modified/new \*.ts files from Crowdin
-   convert \*.ts files into \*.qm files and update each module\'s \*.qrc file
-   update FreeCAD master

Yukarıdaki adımların tümü, periyodik olarak bir yönetici tarafından çalıştırılan \"çeviri komut dosyaları\" tarafından gerçekleştirilir.


<div class="mw-translate-fuzzy">

Modülünüzü çeviri için hazırlamak oldukça kolaydır. Öncelikle, myModule / Gui / Resources\'ta bir \"çeviriler\" dizini olduğundan emin olmalısınız. Ardından \"çeviriler\" dizininizde bir terminal penceresi (veya Windows / OSX eşdeğeri) açın ve aşağıdaki komutu girin: {{Code | code = lupdate -ts myModule.ts}}


</div>


<div class="mw-translate-fuzzy">

Bu boş bir çeviri dosyası oluşturur. Bu yapıldıktan sonra, çeviri komut dosyalarının bu gibi güncellenmesini sağlamalısınız [çekme isteği](https://github.com/FreeCAD/FreeCAD/pull/810).


</div>


<div class="mw-translate-fuzzy">

Bundan sonraki her şey bir geliştirici için otomatiktir. Yönetici metin dizelerini çıkaracak, çevirmenler onları çevirecek, daha sonra yönetici çevirileri çıkaracak ve FreeCAD / master\'ı güncelleyecektir.


</div>


<div class="mw-translate-fuzzy">

### 3. parti modülünüzü veya makronuzu çeviri için hazırlama 

3\. parti modüller veya makrolar, işin bir kısmını kendiniz yapmanız dışında, aynı şekilde tercüme edilir. Bu [forum tartışma](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) ayrıntılarını açıklar.


</div>

3rd party modules or macros are translated in much the same fashion, except that you must do some of the work yourself. This [forum discussion](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=25180) describes the details.

Update: see [Translating an external workbench](Translating_an_external_workbench.md)


<div class="mw-translate-fuzzy">

### Eski modül çeviri teknikleri 

[Yerelleştirme Eski Yöntemler](Localization_Older_Methods/tr.md), Qt Linguist, lupdate, lrelease, pylupdate4 gibi çeviri araçlarının kullanımını ayrıntılı olarak açıklar. Bunun çoğu artık FreeCAD / master modülleri için gerekli değildir, ancak 3. parti modülleri hazırlamak ve güncellemek için yardımcı olabilir.


</div>

[Localization Older Methods](Localization_Older_Methods.md) describes the use of translation tools such as Qt Linguist, lupdate, lrelease, pylupdate4, etc in detail. Most of this is no longer required for FreeCAD/master modules, but may be helpful preparing and updating 3rd party modules.


<div class="mw-translate-fuzzy">

## Crowdin Çeviri Güncellemelerini Otomatikleştirme 

Şu anda FreeCAD çalışanları, çevirileri alıp Crowdin\'e göndermek ve Github deposuna geri göndermek için Crowdin API\'sini [Crowdin Scripts](Crowdin_Scripts.md) üzerinden kullanıyorlar. Crowdin API, FreeCAD bakımcılarına projenin çeviri iş akışının özelliklerini otomatikleştirme yeteneği verir, daha fazla bilgi için [Crowdin API belgelerine](https://support.crowdin.com/api/api-integration-setup/) bakın.


</div>

Currently FreeCAD maintainers use the Crowdin API via [Crowdin Scripts](Crowdin_Scripts.md) to pull and push translations in to Crowdin and back in to the Github repo. The Crowdin API gives FreeCAD maintainers the ability to automate aspects of the project\'s translation workflow, for more info refer to the [Crowdin API documentation](https://support.crowdin.com/api/api-integration-setup/).


<div class="mw-translate-fuzzy">

## İlgili Sayfalar 

-   [Crowdin Yönetici](Crowdin_Administration/tr.md)
-   [Crowdin Scriptleri](Crowdin_Scripts/tr.md)


</div>

-   [Crowdin Administration](Crowdin_Administration.md)
-   [Crowdin Scripts](Crowdin_Scripts.md)


<div class="mw-translate-fuzzy">


{{docnav|[Markalama](Branding/tr.md)|[Ekstra python modülleri](Extra_python_modules/tr.md)}}


</div>


 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Wiki{{\#translation:}}](Category:Wiki.md)
