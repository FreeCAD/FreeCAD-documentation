# Installing on Windows/tr
<div class="mw-translate-fuzzy">


{{docnav/tr
|[Özellik listesi](Feature_list/tr.md)
|[Unix'te kurulum](Install_on_Unix/tr.md)
}}


</div>

FreeCAD\'i Windows\'a kurmanın en kolay yolu aşağıdaki kurulum dosyalarından, işletim sisteminize uygun olanı indirmektir.


{{DownloadWindowsStable}}

.Msi (Microsoft Installer) dosyasını indirdikten sonra, kurulum işlemini başlatmak için üzerine çift tıklayın.

Aşağıda kurulum hakkında daha fazla bilgi bulunmaktadır. Size zor gibi görünüyorsa, endişelenmeyin! Çoğu Windows kullanıcısı, FreeCAD\'i kurmak ve çalışmaya başlamak için .msi\'den daha fazlasına ihtiyaç duymaz !

### Basit Microsoft Yükleyici Kurulumu 

FreeCAD\'i Windows\'a kurmanın en kolay yolu yukarıda indirebileceğiniz kurulum dosyasıdır. Bu sayfada, daha fazla kurulum seçeneği için Microsoft Installer\'ın kullanımı ve özellikleri açıklanmaktadır.

The easiest way to **install FreeCAD on Windows** is by using the downloadable installer bundle above. This page describes the usage and features of the *NSIS Installer* for more installation options.

Kararsız bir geliştirme sürümü indirmek istiyorsanız, [İndirme sayfasına](Download/tr.md) bakın.

## Chocolatey

However, it is highly recommended that you use a package manager such as Chocolatey to keep your software updated. You can installed Chocolatey following [these instructions](https://chocolatey.org/install) and then open a PowerShell terminal as admin and run:


```python
choco install freecad
```

every once in a while you can update your software with


```python
choco upgrade freecad
```

to get the latest version available on Chocolatey repository. If there are any issues with the chocolatey package, you may contact maintainers on [this page](https://chocolatey.org/packages/freecad).

### Komut Satırı Kurulumu 

msiexec.exe komut satırı yardımcı programı ile birlikte ek özellikler, etkileşimsiz kurulum ve Yönetici yüklemesi gibi özellikler bulunur.Aşağıdaki örneklere bakınız.

With the *msiexec.exe* command line utility, additional features such as non-interactive installation and administrative installation are available. See examples below.

### Etkileşimsiz Kurulum 

Komut satırı ile

With the command line


```python
msiexec /i FreeCAD<version>.msi
```

Kurulum programlı olarak başlatılabilir. Bu komut satırının sonunda ek parametreler geçilebilir.


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

#### Sınırlı kullanıcı arayüzü 

Yükleyici tarafından izin verilen kullanıcı kontrolü miktarı / q seçenekleriyle kontrol edilebilir:

The amount of user control permitted by the installer can be controlled with /q options:


<div class="mw-translate-fuzzy">

-   /qn - Arayüz yok
-   /qb - Temel arayüz - İptal butonu ile sadece bir ilerleme diyalogu göster
-   /qb! - /qb gibi, ancak İptal düğmesini gizle
-   /qr - Azaltılmış arayüz - kullanıcı etkileşimi gerektirmeyen tüm iletişim

       kutularını görüntüler (tüm mod iletişim kutularını atla)

-   /qn+ -/qn gibi, ancak sonunda \"Tamamlandı\" iletişim kutusunu görüntüle
-   /qb+ -/qb gibi, ancak sonunda \"Tamamlandı\" iletişim kutusunu görüntüle


</div>

#### Hedef dizin 

TARGETDIR özelliği, FreeCAD kurulumunun kök dizinini belirler. Örneğin, farklı bir yükleme sürücüsü ile belirtilebilir.

The property TARGETDIR determines the root directory of the FreeCAD installation. For example, a different installation drive can be specified with


```python
TARGETDIR=R:\FreeCAD25
```

Varsayılan TARGETDIR \[WindowsVolume \\ Programm Files \\\] FreeCAD \<sürümdür.

#### Tüm Kullanıcılar için Kurulum 

Eklenen

Adding


```python
ALLUSERS=1
```

Tüm kullanıcılar tarafından kullanılabilen bir yüklemeye neden olur. Varsayılan olarak, etkileşimli olmayan (/i) bir yükleme, paketi geçerli kullanıcı (yalnızca yükleme işlemini gerçekleştiren) tarafından kullanılabilir hale getirir; Etkileşimli bir kurulum, kurulumu gerçekleştiren kullanıcı yeterince ayrıcalıklıysa, \"tüm kullanıcılar\" için varsayılan olan bir iletişim kutusu sunar.

#### Özellik Seçimi 

Bazı özellikler, özelliklerin kurulmasına, yeniden kurulmasına veya kaldırılmasına olanak sağlar. FreeCAD yükleyici için bir dizi özellik;

A number of properties allow selection of features to be installed, reinstalled, or removed. The set of features for the FreeCAD installer is

-   Varsayılan özellikler - yazılımı ve çekirdek kütüphaneleri uygun bir şekilde yükleyin,
-   Belgeler - belgeleri yükleyin
-   Kaynak kodu - kaynakları yükleyin
-   \... Yapılacaklar

Ek olarak, ALL tüm özellikleri belirtir.Tüm özellikler DefaultFeature\'a bağlıdır, bu nedenle herhangi bir özelliğin kurulması, varsayılan özelliği de otomatik olarak yükler. Aşağıdaki özellikler yüklenecek veya kaldırılacak özellikleri kontrol ediyor

-   ADDLOCAL - yerel makineye yüklenecek özelliklerin listesi
-   REMOVE - Bilgisayardan kaldırılacak özelliklerin listesi
-   ADDDEFAULT - Varsayılan yapılandırmasına eklenen özelliklerin listesi (tüm FreeCAD özellikleri için yereldir)
-   REINSTALL - yeniden yüklenecek / onarılacak özelliklerin listesi
-   ADVERTISE - Bir kısayol yüklemesi gerçekleştirmek için özellikler listesi

Bunların dışında ki özellikler için MSDN belgelerine bakın.

Bu seçeneklerle


```python
ADDLOCAL=Extensions
```

yorumlayıcıyı kendisi yükler ve uzantıları kaydeder, ancak başka bir şey yüklemez.

### Kaldırma

With


```python
msiexec /x FreeCAD<version>.msi
```

Bu komutla, FreeCAD kaldırılabilir.MSI dosyasının kaldırma için bulunması gerekmez; alternatif olarak, paket veya ürün kodu da belirtilebilir. Ürün kodunu, FreeCAD\'in başlat menüsünde yüklediği Kaldır kısayolunun özelliklerine bakarak bulabilirsiniz.

### Yetkili Kurulum 

With


```python
msiexec /a FreeCAD<version>.msi
```

Bu kodla, Yetkili(ağ) kurulumu yapılabilir.Dosyalar hedef dizine açılır (bu bir ağ dizini olmalıdır), ancak yerel sistemde başka bir değişiklik yapılmaz. Ek olarak, hedef dizinde başka bir (daha küçük) msi dosyası oluşturulur ve istemciler daha sonra yerel bir yükleme gerçekleştirmek için kullanabilirler (gelecekteki sürümler ayrıca bazı özellikleri ağ sürücüsünde bir arada bulundurmayı da önerebilir).

Şu anda, yönetimsel kurulumlar için kullanıcı arayüzü yoktur, bu nedenle hedef dizine komut satırından geçilmesi gerekir.

Bir yönetimsel kurulum için belirli bir kaldırma prosedürü yoktur - Basitçe hiç bir kullanıcı kullanmıyorsa hedef dizini silin.

### Kısayol

With


```python
msiexec /jm FreeCAD<version>.msi
```

Prensipte, FreeCAD\'i bir makineye \"tanıtmak\" mümkün olacaktır (bir kullanıcıya /ju ile). Bu, yazılımın yüklenmeden simgeleri başlangıç ​​menüsünde görünmesine ve uzantıların kaydedilmesine neden olur. Bir özelliğin ilk kullanımı bu özelliğin kurulmasına neden olur.

FreeCAD yükleyicisi şu anda,sadece başlangıç ​​menüsüne eklemeleri destekliyor, ancak kısayolları desteklemiyor.

### Makine gruplarına otomatik kurulum 

Windows Grup İlkesi ile, FreeCAD\'i bir grup makineye otomatik olarak kurmak mümkündür. Bunu yapmak için aşağıdaki adımları izleyin:

1.  Etki alanı denetleyicisinde oturum açın
2.  MSI dosyasını, tüm hedef makinelere verilen erişim ile paylaşılan bir klasöre kopyalayın.
3.  MMC ek bileşenini açın \"Active Directory kullanıcıları ve bilgisayarları\"
4.  FreeCAD kurulacak bilgisayar grubuna gidin
5.  Özellikleri açın
6.  Grup İlkelerini açın
7.  Yeni bir ilke ekle ve düzenle
8.  Bilgisayar Yapılandırması/Yazılım Kurulumu\'nda Yeni/Paket\'i seçin
9.  Ağ yolu üzerinden MSI dosyasını seçin
10. İsteğe bağlı olarak, bilgisayar ilkenin kapsamından çıkarsa, FreeCAD\'in kaldırılmasını istediğinizi seçin.

With Windows Group Policy, it is possible to automatically install FreeCAD on a group of machines. To do so, perform the following steps:

1.  Log on to the domain controller
2.  Copy the MSI file into a folder that is shared with access granted to all target machines.
3.  Open the MMC snapin \"Active Directory users and computers\"
4.  Navigate to the group of computers that need FreeCAD
5.  Open Properties
6.  Open Group Policies
7.  Add a new policy, and edit it
8.  In Computer Configuration/Software Installation, choose New/Package
9.  Select the MSI file through the network path
10. Optionally, select that you want FreeCAD to be de-installed if the computer leaves the scope of the policy.

Grup ilkesi yayılması genellikle biraz zaman alır - paketi güvenilir bir şekilde dağıtmak için tüm makineler yeniden başlatılmalıdır.

### Crossover Office kullanarak Linux\'ta kurulum 

FreeCAD\'in Windows sürümünü CXOffice 5.0.1 kullanarak bir Linux sistemine kurabilirsiniz . Yükleme paketinin \"Y:\" sürücü harfiyle eşlenen \"yazılım\" dizinine yerleştirildiğini varsayarak, CXOffice komut satırından msiexec komutunu çalıştırın : 
```pythonmsiexec /i Y:\\software\\FreeCAD<version>.msi
``` FreeCAD çalışıyor, ancak [Wine](wikipedia:Wine_(software).md), Google [SketchUp](wikipedia:SketchUp.md) altında çalışan diğer programlar gibi OpenGL ekranının çalışmadığı bildirildi .


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD çalışıyor ancak OpenGL ekranının çalışmadığı, [ Wine](wikipedia:Wine(software).md), yani Google [ SketchUp](wikipedia:_SketchUp.md) altında çalışan diğer programlar gibi çalışmadığı bildirildi.


<div class="mw-translate-fuzzy">


{{docnav/tr
|[Özellik listesi](Feature_list/tr.md)
|[Unix'te kurulum](Install_on_Unix/tr.md)
}}


</div>

---
[documentation index](../README.md) > Installing on Windows/tr
