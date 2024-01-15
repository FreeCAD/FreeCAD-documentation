# FreeCAD and DXF Import/it
## Antefatto

DXF è un formato dati CAD proprietario per disegni 2D originati da AutoCAD. Maggiori dettagli possono essere trovati sulla pagina wiki [DXF](DXF/it.md).



## Introduzione

A partire dalla versione 0.18 di FreeCAD è presente un nuovo importatore DXF C++ e dalla versione 0.19 anche un nuovo esportatore DXF C++. Questi nuovi componenti vengono installati con FreeCAD.

Per utilizzare il vecchio importatore ed esportatore DXF è necessario installare diversi file. Questi file non possono essere inclusi con FreeCAD poiché utilizzano librerie pubblicate con una licenza non compatibile con FreeCAD.



## Come installare l\'importatore ed esportatore DXF legacy 



### Installazione automatica 

Se questi file non sono ancora stati installati, andare al menu **Modifica → Preferenze → Importa/Esporta → DXF** e attivare l\'opzione **Consenti a FreeCAD di scaricare e aggiornare automaticamente le librerie DXF** per consentire a FreeCAD di scaricare e installare automaticamente queste librerie.

Per FreeCAD 0.14 o versioni precedenti è necessario installarle manualmente:



### Installazione manuale 

1.  Andare a [Yorik\'s Github account](https://github.com/yorikvanhavre/Draft-dxf-importer) e scaricare i file (sul lato destro si può selezionare \"download as ZIP\").
2.  Mettere i file nella cartella delle macro.
3.  Se non si è sicuri di dove sia questa cartella, andare su **Modifica → Preferenze → Python → Macro** e controllare il campo denominato **Percorso macro**.

-   In Ubuntu la cartella macro è normalmente: /home/your_user_name/.FreeCAD (la cartella è nascosta, potrebbe essere necessario mostrarla)
-   In Windows la cartella delle macro è normalmente: C:\\Users\\your_user_name\\AppData\\Roaming\\FreeCAD



## Trucchi e consigli 

A volte i file DXF non vengono importati anche se si aprono senza problemi in altri programmi CAD.

Si può provare quanto segue:

1.  Andare su **Modifica → Preferenze → Importa/Esporta → DXF** e deselezionare l\'opzione **Unisci la geometria** e riprovare.
2.  Ricordare che forse ora non si avranno endpoint coincidenti. Si possono renderli coincidenti con [Convalida lo schizzo](Sketcher_ValidateSketch/it.md)

Si può anche provare:

1.  Su **Modifica → Preferenze → Draft → Impostazioni generali** e modificare il valore di **Tolleranza** (valore predefinito: 0,05) e quindi riprovare.

Per una panoramica di tutte le preferenze relative a DXF vedere [Preferenze di Importa/Esporta](Import_Export_Preferences/it#DXF.md).



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and DXF Import/it
