 <img alt="3Dconnexion SpaceNavigator" src=images/SpaceNavigator.jpg  style="width:200px;"> {{TOCright}}


<div class="mw-translate-fuzzy">

## Sürücü kurulumu {#sürücü_kurulumu}

### Linux

FreeCAD [Spacenav](http://spacenav.sourceforge.net/) projesinden sürücüleri destekliyor. Bu, 3Dconnexion\'un özel sürücüleri ile uyumlu açık kaynaklı bir sürücü oluşturmayı amaçlayan bir projedir.


</div>

### Linux {#linux_1}

FreeCAD supports drivers from project [Spacenav](http://spacenav.sourceforge.net/). This is a project aiming to create an open-sourced driver which is compatible with the proprietary drivers from 3Dconnexion.


<div class="mw-translate-fuzzy">

#### Depodan yükleyin {#depodan_yükleyin}

##### Ubuntu


</div>

##### Ubuntu {#ubuntu_1}


```python
sudo apt-get install spacenavd
```

Note, however, that version 0.6 available on Ubuntu 20.04 (and probably older ones) does not seem to work. You then have to compile spacenavd from source as explained below.

##### Fedora


```python
sudo yum install spacenavd
```

##### Debian


```python
apt-get install spacenavd libspnav-dev
```


:   spacenav needs these permissions:





:   
    
```python
    cp ~/.Xauthority /root/
    
```
    





:   Restart spnavd and FreeCAD





:   
    
```python
    /usr/bin/spnavd_ctl x11 stop
    /usr/bin/spnavd_ctl x11 start
    
```
    

##### openSUSE


```python
sudo zypper install spacenavd
```


<div class="mw-translate-fuzzy">

#### Spacenav\'ı kaynaktan derle {#spacenavı_kaynaktan_derle}

Dağıtımınız eski bir sürüm sağlayabilirse, bu önerilir.


</div>

This is recommended if your distribution might provide an outdated version.


<div class="mw-translate-fuzzy">

Aşağıdaki dosyaları indirin:

-   -   [spacenavd-0.5.tar.gz](http://sourceforge.net/projects/spacenav/files/spacenav%20daemon/spacenavd%200.5/spacenavd-0.5.tar.gz/download)
    -   [libspnav-0.2.2.tar.gz](http://sourceforge.net/projects/spacenav/files/spacenav%20library%20%28SDK%29/libspnav%200.2.2/libspnav-0.2.2.tar.gz/download)
    -   [spnavcfg-0.2.1.tar.gz](http://sourceforge.net/projects/spacenav/files/spacenavd%20config%20gui/spnavcfg%200.2.1/spnavcfg-0.2.1.tar.gz/download)

-   Arşivleri, ana dizininizdeki bir klasöre yerleştirin.

-   Spacenavd-0.5 dizinine girin ve aşağıdaki komutları çalıştırın:


</div>


:   
    
```python
    ./configure
    make
    
```
    


<div class="mw-translate-fuzzy">

-   Bu başarılı olursa, aşağıdaki \'\' \'root\' \'\' (veya sudo ile öneki) komutlarını çalıştırın.


</div>


:   
    
```python
    make install
    ./setup_init
    /etc/init.d/spacenavd start
    
```
    

-   Bu, spacenav arka planını yükler, otomatik olarak sistem önyüklemesine yüklenecek şekilde yapılandırır ve yeniden başlatmaya gerek kalmadan arka plan programı başlatır.
-   Şimdi cihazınızın doğru bir şekilde algılandığını kontrol etmenin zamanı geldi. Cihazınız fişe takılı durumdayken, aşağıdaki komutu çalıştırın ve ardından takın.

:   
    
```python
    tail -n100 -f /var/log/spnavd.log 
    
```
    

-   Çıktı böyle görünüyorsa, devam edebilirsiniz.

:   
    
```python
    Device detection, parsing /proc/bus/input/devices
    trying alternative detection, querying /dev/input/eventX device names...
      trying "/dev/input/event1" ... Power Button
      trying "/dev/input/event2" ... 3Dconnexion SpaceNavigator
    using device: /dev/input/event2
    device name: 3Dconnexion SpaceNavigator
    
```
    


<div class="mw-translate-fuzzy">

-   Şimdi libspnav-0.2.2 adlı dizine girin ve aşağıdaki komutları çalıştırın:


</div>


:   
    
```python
    ./configure
    make
    
```
    

-   Aşağıdaki hatayı vererek başarısız olursa: \...

:   
    
```python
    fatal error: gtk/gtk.h: No such file or directory
    
```
    

-   \... sonra libgtkmm-2.4-dev\'i kurmanız gerekir. Ubuntu altında, bu şekilde yapılır:

:   
    
```python
    sudo apt-get install libgtkmm-2.4-dev
    
```
    

-   Make başarıyla tamamlandığında, aşağıdaki **root** (veya sudo ile) komutunu çalıştırın.

:   
    
```python
    make install
    
```
    


<div class="mw-translate-fuzzy">

-   Libspnav-0.2.2/samples/dizinine bakınız. Cihazınızı test etmek istiyorsanız, iki örnekten birini derleyin ve çalıştırın.


</div>

-   Spnavcfg\'yi derlemek ve kurmak için aynı işlemleri takip edin. Spnavcfg dosyasını root olarak çalıştırdığınızdan emin olun, aksi takdirde hiçbir ayar kaydedilmez!

#### Starting spacenavd as a systemd service at boot {#starting_spacenavd_as_a_systemd_service_at_boot}

If you want to start spacenavd at boot using systemd, do the following:

-   Go to the directory where you clone the spacenavd repository (to the root of the repository)
-   \"sudo cp contrib/systemd/spacenavd.service /usr/lib/systemd/system/spacenavd-local.service\".
-   \"sudo systemctl enable spacenavd-local.service\".
-   \"sudo systemctl start spacenavd-local.service\", if you want to start it right away.

This is only necessary for the installation from source.


<div class="mw-translate-fuzzy">

#### Yeniden başlatın {#yeniden_başlatın}

Bazen navigatör çalışmayı durdurursa, sürücüyü yeniden başlatmak iyidir. Yeniden başlatmak için Terminal\'e gidin ve yürütün:


</div>

If sometimes navigator stops working, it is good to restart driver. To restart it, go to Terminal and execute:


```python
sudo xhost +
sudo /etc/init.d/spacenavd restart
```

Bundan sonra FreeCAD\'i yeniden başlatın. Bazı dağıtımlarda, her açılışta bu gereklidir.

### Known Issues {#known_issues}

A user reported on the [forum](https://forum.freecadweb.org/viewtopic.php?p=341327#p341327) they saw the following:

 Spacenav daemon 0.6
 failed to open config file /etc/spnavrc: No such file or directory. using defaults.
 adding device.
 device name: 3Dconnexion SpacePilot
 using device: /dev/input/event5
 No protocol specified
 failed to open X11 display ":0.0" 

The workaround that worked for them:


```python 
sudo cp ~/.Xauthority /root/
sudo spnavd_ctl x11 start
sudo systemctl restart spacenavd 
```


<div class="mw-translate-fuzzy">

### OSX

3Dconnexion giriş cihazları, FreeCAD\'in kurulu olan 3Dconnexion sürücüleri olan bir sistemde oluşturulması ve kullanılması şartıyla OS X\'de desteklenir.


</div>

3Dconnexion input devices are supported on OS X, provided that FreeCAD is built and used on a system with the 3Dconnexion drivers installed.


<div class="mw-translate-fuzzy">

### Windows

0.13 sürümünden itibaren, 3D fare Windows altında desteklenmektedir. Özel sürücüleri kurmanız gerekir, ancak destek daha düşük seviyede geliştirildiğinden, 3D Connexion kontrol panelinde ayarladığınız ayarları geçersiz kılar. Ancak, bu ayarların çoğu Spaceball sekmeleri altındaki Araçlar \>\> Özelleştir iletişim kutusundan ayarlanabilir.


</div>

As of version 0.13, 3D mouse is supported under Windows. You need to have 3Dconnexion drivers installed.

#### Known Issue {#known_issue}

There is an issue where 3Dconnexion sends duplicate scroll events to FreeCAD, which causes the view to jump. To fix it:

1.  Open 3Dconnexion Properties. You can double-click its icon in the Taskbar, next to the Windows clock.
2.  Click on the Advanced Settings button.
3.  Open FreeCAD or switch to an already-open FreeCAD window.
4.  Switch back to 3Dconnexion Advanced Settings. Confirm that it says \"FreeCAD\" in the heading.
5.  Uncheck all boxes on the page.

ref: <https://freecadweb.org/tracker/view.php?id=1893>


<div class="mw-translate-fuzzy">

## FreeCAD\'i kurma {#freecadi_kurma}

Linux\'ta spnav projesiyle ve Windows\'ta çok düşük düzeyde 3D fare desteği verildi. Bu, bir aygıt için herhangi bir ayar için destek olmadığı, çünkü Linux\'ta bunun için iyi bir destek olmadığı ve Windows\'ta geçersiz kılındığı anlamına gelir. Bu nedenle \"Özelleştir\" iletişim kutusuna iki ek sayfa eklendi.


</div>

3D mouse support was made with spnav project on Linux, and on a very low level on Windows. This means there was no support for any settings for a device, since on Linux there is no good support for this, and on Windows it is overridden. This is why two additional pages were added to \"Customize\" dialog.

<img alt="" src=images/Spaceball_Motion.png  style="width:450px;"> <img alt="" src=images/Spaceball_Buttons.png  style="width:450px;">


<div class="mw-translate-fuzzy">

### Spaceball Hareketi {#spaceball_hareketi}

Bu sekmede, bazı genel uzay fare ayarlarının kurulumunu yapabilirsiniz. İçeriği:

-   Global Duyarlılık - Global duyarlılığı ayarlama özelliğine sahip kaydırıcı
-   Baskın - baskın modu etkinleştirirseniz, yalnızca en yüksek hareketi olan eksenler dikkate alınır.
-   YZ Çevir - Bu seçenek, 3D farede Y ve Z eksenlerini çevirmenizi sağlar
-   Çevirileri Etkinleştir - çevirileri etkinleştirmenin / devre dışı bırakmanın kolay yolu
-   Rotasyonları Etkinleştir - rotasyonları etkinleştirmenin / devre dışı bırakmanın kolay yolu
-   Kalibre Et - Boşluk yönlendiricisini ayarlamanızı sağlar. Uzay gezgini taşınmazken basılır.
-   Varsayılana Ayarla - tüm ayarları kaldırır ve varsayılanlara ayarlar.


</div>

In this tab you have ability to set up some of general space mouse settings. They include:

-   Global Sensitivity - Slider with ability to set global sensitivity
-   Dominant - if you enable dominant mode, only axes with highest move will be considered
-   Flip YZ - This option enables you to flip Y and Z axes on 3D mouse
-   Enable Translations - easy way to enable/disable translations
-   Enable Rotations - easy way to enable/disable rotations
-   Calibrate - enables you to calibrate space navigator. It is pressed while space navigator is not moved.
-   Set To Default - removes all settings and sets them to default.

Bunun dışında, her eksen için ayarlayabileceğiniz yetenekler:

-   Etkin - Eksenleri Etkinleştir / Devre Dışı Bırak
-   Ters - Eksenlerde ters hareket
-   Hassasiyet - hassasiyeti ayarlama yeteneğine sahip kaydırıcı


<div class="mw-translate-fuzzy">

### Spaceball Düğmeleri {#spaceball_düğmeleri}

Bu sekmeyi ilk kez açtığınızda, boş ve kullanılamayacak. Etkinleştirmek için boşluk fare düğmelerinden birine basmanız gerekir. Bunu yaptıktan sonra, sol tarafta düğmelerin listesi görünecek ve sağ tarafta komutların listesi bulunacaktır.


</div>

When you open this tab for the first time, it will be empty and unavailable. To activate it, you must press one of your space mouse buttons. After you do, list of buttons will appear on the left side, and list of commands will be available on the right side.

Belirli bir komutu bir düğmeyle bağlamak için, sol taraftaki düğmeyi seçin ve sağ taraftaki komutu seçin. Komutları düğmeden silmek için \"Sil\" e basın.

## Related

-   Forum thread [spacenav on windows](https://forum.freecadweb.org/viewtopic.php?f=3&t=51023)
-   Forum thread [Space navigator axis confusion](https://forum.freecadweb.org/viewtopic.php?f=8&t=57188)

[Category:User Documentation{{\#translation:}}](Category:User_Documentation.md) [Category:3rd Party{{\#translation:}}](Category:3rd_Party.md)
