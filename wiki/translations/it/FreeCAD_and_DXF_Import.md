# FreeCAD and DXF Import/it
{{TOCright}}

## Background

DXF is a proprietary CAD data format for 2D drawings that originated with AutoCAD. More details can be found on the [DXF](DXF.md) wiki page.


<div class="mw-translate-fuzzy">

## Note Legali 

Per essere in grado di importare dei file DXF è necessario installare manualmente alcuni file. Perché questo? Queste librerie sono pubblicate con un\'altra licenza di FreeCAD, così gli sviluppatori di FreeCAD non devono impacchettarle con l\'applicazione FreeCAD.


</div>

Since FreeCAD version 0.18 there is a new C++ DXF importer, and since version 0.19 also a new C++ DXF exporter. These new components are installed with FreeCAD.

To use the older, legacy, DXF importer and exporter you need to install several files. These files cannot be included with FreeCAD since they use libraries published under a license that is not compatible with FreeCAD.


<div class="mw-translate-fuzzy">

## Come installarle 


</div>

### Installazione automatica 


<div class="mw-translate-fuzzy">

Se non è ancora installato, andare al menu **Modifica → Preferenze → Importa/Esporta → DXF** e attivare l\'opzione **Consenti a FreeCAD di scaricare automaticamente le librerie DXF** per consentire a FreeCAD di scaricare e installare automaticamente queste librerie.


</div>


<div class="mw-translate-fuzzy">

Per FreeCAD 0.14 o versione più vecchie è necessario installarle manualmente   *


</div>

### Installazione manuale 


<div class="mw-translate-fuzzy">

1.  Andare a [Yorik\'s Github account](https   *//github.com/yorikvanhavre/Draft-dxf-importer) e scaricare questi file (sul lato destro si può scegliere \"download as ZIP\").
2.  Mettere i file nella cartella delle macro.

-   In Ubuntu, normalmente la cartella si trova in

/home/your_user_name/.FreeCAD 

La directory è nascosta. Potrebbe essere necessario renderla visibile.

-   In Windows, la directory standard delle macro è

C   *Users\your_user_name\AppData\Roaming\FreeCAD


</div>


<div class="mw-translate-fuzzy">

Tutorial   * [Installare l\'importatore DXF](Dxf_Importer_Install/it.md)


</div>


<div class="mw-translate-fuzzy">

## Trucchi e consigli 

A volte sembra che i file DXF non importino nulla anche se in programmi CAD 2D-DXF si aprono senza problemi. In questo caso, si può provare   *

1.  andare in Modifica → Preferenze → Import/Export → DXF/DWG e deselezionare l\'opzione \"Unisci geometria\" e riprovare.
2.  Ricordate che forse ora non avrete i punti finali delle linee coincidenti. Si dovrà farli coincidere da soli.
3.  Potete farlo con il comando \"Close Shape\" nel workbench Sketcher (con la versione 0.15) oppure è possibile applicare i vincoli manualmente

Potete anche provare   *

1.  andare in Modifica → Preferenze → Draft → Generali e regolare il valore di \"Tolerance\" (default   * 0,05)
2.  Riprovare


</div>

Sometimes DXF Files don\'t import although they open in other CAD-Programs without problems.

You can try   *

1.  Go to **Edit → Preferences → Import-Export → DXF** and untick the option **Join geometry** and try again.
2.  Remember that maybe now you won\'t have coincident endpoints. You will have to make them coincident yourself.
3.  You can do this with the [Sketcher CloseShape](Sketcher_CloseShape.md) command <small>(v0.15)</small>  or you can apply the constraints manually.

You can also try   *

1.  Go to **Edit → Preferences → Draft → General settings** and adjust the value of **Tolerance** (default   * 0,05) and try again.

For an overview of all DXF related preferences see [Import Export Preferences](Import_Export_Preferences#DXF.md).

[Category   *User_Documentation](Category_User_Documentation.md) [Category   *File_Formats](Category_File_Formats.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and DXF Import/it
