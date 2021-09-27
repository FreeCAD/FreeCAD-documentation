# Importing From Sketchup/it
{{Fake heading|sub=4|< Torna a [[FreeCAD Howto Import Export]]}}

## Il metodo migliore 


{{TOCright}}

Per esperienza, attualmente il metodo migliore per importare un file da SketchUp è quello di utilizzare il formato Collada (\*.dae).FreeCAD non supporta nativamente il formato Collada. Per avere questa funzionalità in FreeCAD, l\'utente deve installare un modulo Python per l\'importazione e l\'esportazione del formato. Si tratta di un compito relativamente facile da eseguire e le istruzioni si possono trovare nella pagina [Moduli python aggiuntivi](Extra_python_modules/it.md). Il link diretto alle istruzioni è: [Extra python modules: pyCollada](http://www.freecadweb.org/wiki/index.php?title=Extra_python_modules#pyCollada).

## Importare i file Collada (\*.dae) 

Se il modulo pyCollada è stato installato, è possibile aprire o importare un file Collada nello stesso modo di qualsiasi altro. Selezionare il menu File e quindi selezionare Apri o Importa. Selezionare il file Collada e fare clic su Apri. È possibile filtrare il tipo di file, selezionando Tipo di file nella finestra di dialogo pull down Apri o Importa e selezionando poi Collada (\*.dae) nella lista.

## Alternative

Utilizzando il plugin esportazione STL di Sketchup, si può anche scegliere di utilizzare tale formato che FreeCAD supporta in modo nativo. Ci sono un certo numero di questi plugin disponibili per Sketchup e alcuni funzionano meglio di altri. È possibile che l\'utente debba fare alcune ricerche per stabilire quale si adatta meglio alle proprie esgenze.

## Note

Sia Collada (\*.dae) che STL sono formati mesh. Per utilizzare questi file all\'interno di FreeCAD, che lavora principalmente con i solidi, e usando questi formati può essere necessario fare del lavoro aggiuntivo sugli oggetti importati.

## Relazioni

-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)
-   [Importazione e esportazione](Import_Export/it.md)
-   [Preferenze di Importa/Esporta](Import_Export_Preferences/it.md)




_ _

---
[documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > Importing From Sketchup/it
