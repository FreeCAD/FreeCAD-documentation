# DXF/it
{{TOCright}}



## Storia


<div class="mw-translate-fuzzy">

DXF è un formato di dati CAD proprietario per disegni 2D originato con AutoCAD, ma che è compreso dalla maggior parte dei pacchetti di disegno e di plotting, poiché non era disponibile uno standard aperto alternativo durante gli anni in cui AutoCAD era dominante.


</div>


<div class="mw-translate-fuzzy">

Lo stesso vale per i DXF. Sentirete parlare di alcune versioni chiave di DXF, come R12 (dal 1992) o R14 (dal 1997 che aveva le spline). Versioni successive di DXF hanno elementi 3D, ma questi sono usati o implementati raramente. Il modo in cui si utilizza DXF per condividere i dati CAD tra due programmi dipende principalmente dalle limitazioni e dai bug nei lettori / importatori e scrittori / esportatori corrispondenti. Non sorprende che raramente vi sia una documentazione completa delle limitazioni e degli errori del programma, il che è una grande fonte di frustrazione.


</div>


<div class="mw-translate-fuzzy">

Se state modificando dei file DXF e vi aspettate che rimangano quasi gli stessi quando li salvate, vi consigliamo di utilizzarli con [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD) o [QCad](https://en.wikipedia.org/wiki/QCad) perché le strutture dati interne di questi programmi sono compatibili con gli oggetti del file DXF.


</div>


<div class="mw-translate-fuzzy">

In FreeCAD i lettori DXF devono interpretare la geometria (ad esempio una forma spline) dal file DXF nelle specifiche forme interne dell\'ambiente di lavoro.


</div>



## Metodi per importare i DXF in FreeCAD 


<div class="mw-translate-fuzzy">

Se avete intenzione di rivedere le impostazioni frequentemente, vi consigliamo di andare su Modifica → Preferenze → Import-Export → DXF e spuntare la casella \"\[\] Mostra questa finestra di dialogo durante l\'importazione e l\'esportazione\".


</div>


<div class="mw-translate-fuzzy">

Maggiori informazioni sono sulle pagine [Draft - File DXF](Draft_DXF/it.md) e [Importare i file DXF in FreeCAD](FreeCAD_and_DXF_Import/it.md).


</div>

Se state utilizzando la geometria importata per creare forme 3D in Part Design, provate a [Convalidare lo schizzo](Sketcher_ValidateSketch/it.md) dopo aver importato il DXF in uno schizzo.



### Importatote DXF C++ 


<div class="mw-translate-fuzzy">

Questa implementazione è un\'implementazione veloce, ma ignora le funzioni che non riconosce, come le spline DXF. Inoltre, può importare la geometria in Draft solo come singole voci nell\'albero del modello. Le geometrie possono avere i colori letti dal file se si attiva questa opzione. Per ulteriori informazioni, vedere [questo post nel forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=32493).


</div>



### Importatore DXF Python 


<div class="mw-translate-fuzzy">

Questo importatore deve essere scaricato e installato prima di poter essere utilizzato. Vedere [Installare l\'importatore DXF](Dxf_Importer_Install/it.md), oppure usare l\'opzione \"\[\] Consenti a FreeCAD di scaricare e aggiornare automaticamente le librerie DXF\".


</div>


<div class="mw-translate-fuzzy">

Questo importatore ha più funzioni (come l\'implementazione delle spline) e ha la possibilità di caricare le forme DXF nello Sketcher. Tuttavia, tenere presente che tutti gli elementi dello schizzo vengono visualizzati singolarmente una seconda volta nell\'albero del modello, il che può creare confusione. È possibile eliminare tutti questi singoli oggetti e conservare il singolo schizzo (che appare come la seconda voce nell\'elenco di nuovi elementi).


</div>


<div class="mw-translate-fuzzy">

Sfortunatamente, Sketcher non implementa i colori, quindi tutta la geometria appare sullo stesso livello, il che è un problema se il file contiene molte linee di costruzione. Una soluzione consiste nell\'aprire il disegno in LibreCAD ed eliminare tutte le geometrie che non si desidera visualizzare prima di salvare un file che contiene esattamente la geometria che si desidera caricare.


</div>



### Macro


<div class="mw-translate-fuzzy">

Dare uno sguardo al forum di FreeCAD o alla [Raccolta di macro](Macros_recipes/it.md) per implementazioni alternative dell\'importazione e della pulizia dei DXF man mano che si sviluppano.


</div>



## Salvare in DXF 


<div class="mw-translate-fuzzy">

Oltre alle opzioni di Modifica → Preferenze, l\'ambiente [TechDraw](TechDraw_Workbench/it.md) può anche esportare le pagine di disegno in DXF usando la funzione [Esporta pagina in DXF](TechDraw_ExportPageDXF/it.md).


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Draft](Category_Draft.md) > [TechDraw](Category_TechDraw.md) > [File_Formats](Category_File_Formats.md) > DXF/it
