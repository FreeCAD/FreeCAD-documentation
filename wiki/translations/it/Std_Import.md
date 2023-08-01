---
- GuiCommand:/it
   Name:Std_Import
   Name/it:Importa
   MenuLocation:File → Importa...
   Workbenches:All
   Shortcut:**Ctrl**+**I**
   SeeAlso:[Apri](Std_Open/it.md), [Importazione e Esportazione](Import_Export/it.md), [Preferenze di Importa/Esporta](Import_Export_Preferences/it.md)
---

# Std Import/it



## Descrizione

Il comando **Importa** importa la geometria da un diverso formato di file nel documento attivo. Sono supportati molti formati di file e per alcuni formati esistono più opzioni di importazione. Per ulteriori informazioni vedere [Importazione e esportazione](Import_Export/it.md).


{{Version/it|0.21}}

: se viene selezionato un formato immagine, il comando creerà un [Piano Immagine](#Piano_Immagine.md).



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **File →  <img src="images/Std_Import.svg" width=16px> Importa...** dal menu.
    -   Usare la scorciatoia da tastiera: **Ctrl**+**I**.
2.  Facoltativamente, selezionare il formato file corretto nella finestra di dialogo.
3.  Selezionare un file.
4.  Premere il pulsante **Apri**.



## Opzioni

-   Premere il tasto **Esc** o il pulsante **Annulla** per annullare il comando.



## Note

-   Per convertire in un solido un [oggetto mesh](Mesh_Workbench/it.md) importato, vedere il tutorial [Importare da STL o OBJ](Import_from_STL_or_OBJ/it.md).
-   Per importare in un nuovo documento è possibile utilizzare il comando [Apri](Std_Open/it.md).
-   Alcuni ambienti hanno comandi di importazione aggiuntivi. Vedere [Importazione e esportazione](Import_Export/it.md).



## Preferenze

-   Vedere [Preferenze di Importa e esporta](Import_Export_Preferences/it.md).
-   L\'ultima posizione del file utilizzato è memorizzata in: {{MenuCommand | Strumenti → Modifica parametri ... → BaseApp → Preferenze → Generale → FileOpenSavePath}}.
-   L\'ultimo filtro di importazione utilizzato è memorizzato in: {{MenuCommand | Strumenti → Modifica parametri ... → BaseApp → Preferenze → Generale → FileImportFilter}}.



## Piano Immagine 

Un Piano Immagine è una rappresentazione planare di un\'immagine nella [Vista 3D](3D_view/it.md). Ad esempio, può essere utilizzato durante la creazione di un modello basato su fotografie di un oggetto esistente.

Per impostazione predefinita, un piano immagine viene posizionato sul piano XY globale. La dimensione iniziale di un piano immagine viene calcolata utilizzando una risoluzione di 96 px/pollice.



### Modifica

1.  Per modificare un Piano Immagine, eseguire una delle seguenti operazioni:
    -   Fare doppio clic sul piano dell\'immagine nella [Vista albero](Tree_view/it.md).
    -   Fare clic con il pulsante destro del mouse sul piano dell\'immagine nella vista ad albero e selezionare **<img src="images/Image-scaling.svg" width=16px> Cambia immagine...** dal menu contestuale.

2.  Se il piano dell\'immagine non è piano-parallelo al piano XY, XZ o YZ del sistema di coordinate globali, viene riallineato in modo che sia piano-parallelo al piano XY.

3.  Si apre il pannello attività **Impostazioni piano immagine**.

4.  Opzionalmente selezionare **Piano XY**, **Piano XZ** o **Piano YZ** del sistema di coordinate globale.

5.  Selezionare **Direzione inversa** per ruotare il piano dell\'immagine di 180°. L\'asse di rotazione dipende dal piano selezionato. Per il piano XY è l\'asse X globale. Per il piano XZ e YZ è l\'asse Z globale.

6.  
    **Offset**, **Distanza X** e **Distanza Y** sono relativi al sistema di coordinate del Piano immagine. Un piccolo offset negativo può essere utile quando si traccia l\'immagine con una geometria [Sketch](Sketcher_Workbench/it.md) o [Draft](Draft_Workbench/it.md).

7.  Opzionalmente cambiare **Trasparenza**.

8.  
    **Dimensione immagine**opzioni:

    -   Scala tramite input numerico:
        1.  Facoltativamente deselezionare **Mantieni proporzioni** per ridimensionamento non uniforme.
        2.  Inserire **Larghezza** e/o **Altezza**.
    -   Scalare selezionando i punti:
        1.  Premiere il pulsante **Calibra**.
        2.  Scegliere due punti all\'interno dell\'immagine.
        3.  Viene visualizzata una linea di quota.
        4.  Inserire la dimensione desiderata.
        5.  Premere **Enter** o il pulsante **Applica**.

9.  Premere il pulsante **OK** per confermare le modifiche e chiudere il pannello delle attività.



### Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Image Plane deriva da un oggetto [App GeoFeature](App_GeoFeature/it.md) e ne eredita tutte le proprietà. Ha anche le seguenti proprietà aggiuntive:



#### Dati


{{TitleProperty|Image Plane}}

-    **Image File|FileIncluded**: il file immagine utilizzato per il piano immagine. Questo file è memorizzato nel file **.FCStd**.

-    **XSize|Length**: la larghezza del piano dell\'immagine.

-    **YSize|Length**: l\'altezza del piano dell\'immagine.



#### Vista


{{TitleProperty|Object Style}}

-    **Lighting|Enumeration**: come viene illuminato il piano dell\'immagine nella [Vista 3D](3D_view/it.md). Può essere {{value|Two side}} o {{value|One side}}.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Import/it
