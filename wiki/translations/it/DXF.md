# DXF/it
## Storia

Il Drawing Exchange Format (DXF) è un formato di dati CAD proprietario sviluppato da Autodesk per consentire lo scambio di file tra il prodotto di punta AutoCAD e altri software. Esistono numerose buone librerie software per leggere/scrivere il formato DXF.

Esistono molte versioni del formato DXF. Si sentirà parlare di alcune versioni chiave, come R12 (del 1992) o R14 (del 1997 che aveva le spline). Le versioni successive di DXF hanno elementi 3D, ma questi vengono utilizzati o implementati raramente. Il modo in cui si utilizza DXF per condividere i dati CAD tra programmi dipende principalmente dalle limitazioni e dai bug nei corrispondenti lettori/importatori e scrittori/esportatori. Questi raramente sono completamente documentati e possono essere una grande fonte di frustrazione.

Se si sta modificando dei file DXF e si desidera che rimangano quasi gli stessi quando vengono salvati, consigliamo di utilizzare [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD) o [/wiki/QCad QCad](https://en.wikipedia.org) perché le strutture dati interne di questi programmi sono compatibili con gli oggetti nel file DXF.

In FreeCAD i lettori DXF devono tradurre la geometria (ad esempio una forma spline) dal file DXF nelle specifiche rappresentazioni interne dell\'ambiente di lavoro.



## Metodi per importare i DXF in FreeCAD 

Se avete intenzione di rivedere le impostazioni frequentemente, vi consigliamo di andare su Modifica → Preferenze → Import-Export → DXF e spuntare la casella \"\[\] Mostra questa finestra di dialogo durante l\'importazione e l\'esportazione\".

Maggiori informazioni si trovano sulle pagine [Draft - File DXF](Draft_DXF/it.md) e [Importare i file DXF in FreeCAD](FreeCAD_and_DXF_Import/it.md).

Se state utilizzando la geometria importata per creare forme 3D in Part Design, provate a [Convalidare lo schizzo](Sketcher_ValidateSketch/it.md) dopo aver importato il DXF in uno schizzo.



### Importatote DXF C++ 

Questa implementazione è un\'implementazione veloce, ma ignora le funzioni che non riconosce, come le spline DXF. Inoltre, può importare la geometria in Draft solo come singole voci nell\'albero del modello. Le geometrie possono avere i colori letti dal file se si attiva questa opzione. Per ulteriori informazioni, vedere [questo post nel forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=32493).



### Importatore DXF Python 

Questo importatore deve essere scaricato e installato prima di poter essere utilizzato. Usare l\'opzione \"\[\] Consenti a FreeCAD di scaricare e aggiornare automaticamente le librerie DXF\".

Questo importatore ha più funzioni (come l\'implementazione delle spline) e ha la possibilità di caricare le forme DXF nell\'Ambiente Sketcher. Tuttavia, tenere presente che tutti gli elementi dello schizzo vengono visualizzati singolarmente una seconda volta nell\'albero del modello, il che può creare confusione. È possibile eliminare tutti questi singoli oggetti e conservare il singolo schizzo (che appare come la seconda voce nell\'elenco di nuovi elementi).

Sfortunatamente, l\'Ambiente Sketcher non implementa i colori, quindi tutta la geometria appare sullo stesso livello, il che è un problema se il file contiene molte linee di costruzione. Una soluzione consiste nell\'aprire il disegno in LibreCAD ed eliminare tutte le geometrie che non si desidera visualizzare prima di salvare un file che contiene esattamente la geometria che si desidera caricare.



### Macro

Dare uno sguardo al forum di FreeCAD o alla [Raccolta di macro](Macros_recipes/it.md) per implementazioni alternative dell\'importazione e della pulizia dei DXF man mano che si sviluppano.



## Salvare in DXF 

Oltre alle opzioni di Modifica → Preferenze, l\'ambiente [TechDraw](TechDraw_Workbench/it.md) può anche esportare le pagine di disegno in DXF usando la funzione [Esporta pagina in DXF](TechDraw_ExportPageDXF/it.md).



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User%20Documentation.md) > [Draft](Category_Draft.md) > [TechDraw](Category_TechDraw.md) > [File_Formats](Category_File_Formats.md) > DXF/it
