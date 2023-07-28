---
- GuiCommand:/it
   Name:Std_ProjectUtil
   Name/it:Utilità di progetto
   MenuLocation:Strumenti → Utilità di progetto...
   Workbenches:Tutti
---

# Std ProjectUtil/it



## Descrizione

Con il comando **Utilità di progetto** è possibile estrarre i file da un file di progetto FreeCAD (***.FCStd**), che in realtà è un file [ZIP](https://en.wikipedia.org/wiki/Zip_(file_format)) e, dopo le modifiche manuali, creare un nuovo file di progetto da essi.

![](images/Project_utility_en.png ) 
*La finestra di dialogo Utilità di progetto*



## Utilizzo



### Estrarre un progetto 

1.  Selezionare l\'opzione **Strumenti →  <img src="images/Std_ProjectUtil.svg" width=16px> Utilità di progetto...** dal menu.
2.  Viene visualizzata la finestra di dialogo Utilità di progetto.
3.  Premere il pulsante **...** alla destra di **Estrai progetto → Sorgente**.
4.  Selezionare il file ***.FCStd** che si vuole editare.
5.  Premere il pulsante **...** alla destra di **Estrai progetto → Destinazione**.
6.  Selezionare una cartella in cui estrarre il file del progetto. Si consiglia di selezionare una cartella vuota.
7.  Premere il pulsante **Estrai**.
8.  Premere il pulsante **Chiudi** per chiudere la finestra di dialogo.



### Modifiche manuali 

È importante ricordare che i file all\'interno di un file di progetto di FreeCAD sono interconnessi. Basta modificare un singolo file per ottenere degli errori. Per apportare modifiche coerenti su più file, utilizzare un buon editor di codice, come [Notepad++](http://notepad-plus-plus.org/) (per il sistema operativo Windows) o [Notepadqq](https://notepadqq.com/s/) (per il sistema operativo Linux).



### Creare un progetto 

1.  Selezionare l\'opzione **Strumenti →  <img src="images/Std_ProjectUtil.svg" width=16px> Utilità di progetto...** dal menu.
2.  Viene visualizzata la finestra di dialogo Utilità di progetto.
3.  Premere il pulsante **...** alla destra di **Crea progetto → Sorgente**.
4.  Selezionare un file **Document.xml**. Il comando trova automaticamente tutti i file collegati.
5.  Premere il pulsante **...** alla destra di **Crea progetto → Destinazione**.
6.  Selezionare una cartella in cui creare il nuovo file di progetto.
7.  Premere il pulsante **Crea**.
8.  Nella cartella selezionata viene creato un nuovo file di progetto **project.fcstd** con il nome stabilito. Non vi è alcun avviso se esiste già un file con quel nome.
9.  Facoltativamente, selezionare la casella di controllo {{CheckBox|TRUE|Carica il file di progetto dopo la creazione}}.
10. Premere il pulsante **Chiudi** per chiudere la finestra di dialogo.



## Note

-   Per ulteriori informazioni sul formato del file di progetto di FreeCAD, consultare [Formato dei file FCStd](File_Format_FCStd/it.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ProjectUtil/it
