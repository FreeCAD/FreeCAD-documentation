# FreeCAD and DXF Import/tr
{{TOCright}}

## Background

DXF is a proprietary CAD data format for 2D drawings that originated with AutoCAD. More details can be found on the [DXF](DXF.md) wiki page.


<div class="mw-translate-fuzzy">

## Yasal Uyarı 

DXF Dosyalarını içe aktarabilmek için birkaç dosyayı manuel olarak yüklemeniz gerekir. Neden derseniz? Bu kütüphaneler, FreeCAD\'den başka bir lisansla yayınlanmaktadır, dolayısıyla FreeCAD geliştiricileri, FreeCAD-Uygulaması ile birlikte sunmayacaktır.


</div>

Since FreeCAD version 0.18 there is a new C++ DXF importer, and since version 0.19 also a new C++ DXF exporter. These new components are installed with FreeCAD.

To use the older, legacy, DXF importer and exporter you need to install several files. These files cannot be included with FreeCAD since they use libraries published under a license that is not compatible with FreeCAD.


<div class="mw-translate-fuzzy">

## Nasıl kurulur 

Draft-dxf-importer uygulamasını kurmak için:

1.  [Yorik\'in Github hesabına](Https://github.com/yorikvanhavre/Draft-dxf-importer) gidin ve bu dosyaları indirin (sağ tarafta \"ZIP olarak indir\" seçeneğini seçebilirsiniz).
2.  Dosyaları makro klasörünüze yerleştirin.

-   Ubuntu\'da bu normal

  /home/your_user_name/.FreeCAD Dizin gizlidir. Görünür hale getirmek için gizliliğini kaldırmanız gerekebilir.

-   Windows\'ta, (standart) makro dizininiz

  C:\\Users\\kullanıcı_adınız\\AppData\\Roaming\\FreeCAD


</div>

### Automatically

If the files are not already installed, go to the menu **Edit → Preferences → Import-Export → DXF** and enable the option **Allow FreeCAD to automatically download and update the DXF libraries** to make FreeCAD automatically download and install them.

For FreeCAD 0.14 or older you have to install manually:

### Manually

1.  Go to [Yorik\'s Github account](https://github.com/yorikvanhavre/Draft-dxf-importer) and download these files (on the right side you can choose \"download as ZIP\").
2.  Put the files in your macro folder.
3.  If you are unsure where this folder is, go to **Edit → Preferences → General → Macro** and check the field named **Macro Path**.

-   In Ubuntu your macro folder is normally (the folder is hidden, you may need to unhide it):

/home/your_user_name/.FreeCAD 

-   In Windows your macro folder is normally:

C:\Users\your_user_name\AppData\Roaming\FreeCAD


<div class="mw-translate-fuzzy">

Kılavuz: [Dxf Importer kurulumu](Dxf_Importer_Install/tr.md)


</div>


<div class="mw-translate-fuzzy">

## İpuçları ve Püf Noktaları 

Bazen DXF Dosyaları 2D-DXF-CAD Programlarında sorunsuz bir şekilde açılsa bile içe aktarılamıyor olabilir.
Şunları deneyebilirsiniz:
\# Düzenle → Seçenekler → İçe / Dışa Aktar → DXF / DWG seçeneğine gidin ve \"geometri birleştir\" seçeneğinin işaretini kaldırın ve tekrar deneyin.

1.  Unutmayın belki şimdi rastlantısal çizgi sonu noktalarına sahip olmayacaksınız. Onları kendin tayin etmek zorunda kalacaksın.
2.  Bunu, eskiz çalışma tezgahında \"Şekli Kapat\" komutuyla yapabilir (sürüm 0.15\'e ihtiyaç duyar) veya kısıtlamaları manuel olarak uygulayabilirsiniz.

Ayrıca şunu da deneyebilirsiniz:
\# Düzenle → Seçenekler → Taslak → Genel\'e gidin ve \"Tolerans\" değerini ayarlayın (varsayılan: 0,05)

1.  Tekrar deneyin


</div>

Sometimes DXF Files don\'t import although they open in other CAD-Programs without problems.

You can try:

1.  Go to **Edit → Preferences → Import-Export → DXF** and untick the option **Join geometry** and try again.
2.  Remember that maybe now you won\'t have coincident endpoints. You will have to make them coincident yourself.
3.  You can do this with the [Sketcher CloseShape](Sketcher_CloseShape.md) command <small>(v0.15)</small>  or you can apply the constraints manually.

You can also try:

1.  Go to **Edit → Preferences → Draft → General settings** and adjust the value of **Tolerance** (default: 0,05) and try again.

For an overview of all DXF related preferences see [Import Export Preferences](Import_Export_Preferences#DXF.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and DXF Import/tr
