---
- GuiCommand:
   Name:Std_ViewScreenShot
   Name/it:Cattura Schermata
   MenuLocation:Strumenti → Salva immagine...
   Workbenches:Tutti
   SeeAlso:[Stampa](Std_Print/it.md), [Esporta Pdf](Std_PrintPdf/it.md), [Macro Copia la vista 3D negli appunti](Macro_Copy3DViewToClipboard/it.md), [Macro Screen Wiki](Macro_Screen_Wiki/it.md), [Macro Snip](Macro_Snip/it.md)
---

# Std ViewScreenShot/it



## Descrizione

Il comando **Salva immagine** apre una finestra di dialogo per salvare il contenuto della [vista 3D](3D_view/it.md) attiva in un file.

<img alt="" src=images/Save_picture.png  style="width:800px;"> 
*La finestra di dialogo Salva immagine dopo aver premuto il pulsante Esteso*



## Utilizzo

1.  Selezionare l\'opzione **Strumenti → <img src="images/Std_ViewScreenShot.svg" width=16px> Salva immagine...** dal menu.
2.  Si apre la finestra di dialogo Salva immagine.
3.  Facoltativamente, premere il pulsante **Esteso** per visualizzare un pannello aggiuntivo nella finestra di dialogo. Per maggiori informazioni vedere [Opzioni](#Opzioni.md).
4.  Facoltativamente, sfogliare fino alla cartella corretta.
5.  Immettere un nome file e selezionare il tipo di file.
6.  Premere il pulsante **Salva** per creare il file immagine e chiudere la finestra di dialogo.



## Opzioni



### Dimensioni immagine 

1.  Selezionare una dimensione standard dall\'elenco a discesa **Dimensioni standard**. Oppure specificare **Larghezza** e **Altezza** per una dimensione personalizzata.
2.  Facoltativamente, premere un pulsante **Proporzioni** per impostare il rapporto larghezza-altezza dell\'immagine. Se la casella di input **Larghezza** ha il focus, l\'altezza dell\'immagine cambierà e viceversa.



### Proprietà immagine 

1.  Selezionare un\'opzione dall\'elenco a discesa **Sfondo**:
    -   
        {{Value|Corrente}}
        
        Questa opzione utilizza lo sfondo della vista 3D.

    -   
        {{Value|Bianco}}
        

    -   
        {{Value|Nero}}
        

    -   
        {{Value|Transparente}}
        
        Non tutti i formati immagine supportano la trasparenza.
2.  Selezionare un\'opzione dall\'elenco a discesa **Metodo di creazione**:
    -   
        {{Value|Offscreen (New)}}
        
        Questo è il metodo predefinito. Questo metodo supporta l\'[anti-aliasing](https://en.wikipedia.org/wiki/Multisample_anti-aliasing). *Informazioni tecniche: le classi più importanti per questo metodo sono QOffscreenSurface e QOpenGLFramebufferObject di Qt.*

    -   
        {{Value|Offscreen (Old)}}
        
        Questo metodo non funziona su molti sistemi Linux moderni in quanto si basa sul driver grafico. Questo metodo non supporta l\'anti-aliasing. *Informazioni tecniche: questo è un vero e proprio metodo di rendering off-screen che utilizza solo le funzioni della libreria Coin3d.*

    -   
        {{Value|Framebuffer (custom)}}
        
        Questo metodo supporta l\'anti-aliasing. *Informazioni tecniche: se l\'anti-aliasing è disattivato, questo metodo legge l\'immagine direttamente dal renderer grafico, altrimenti esegue il rendering in un framebuffer e ottiene l\'immagine da lì. La parte fondamentale di questo metodo è la classe QOpenGLFramebufferObject di Qt.*

    -   
        {{Value|Framebuffer (as is)}}
        
        Questo metodo usa le stesse tecniche di **Framebuffer (custom)**. Supporta anche l\'anti-aliasing ma presenta alcune limitazioni relative alle dimensioni personalizzate e utilizza sempre lo sfondo corrente della vista 3D.



### Commento immagine 

1.  Selezionare l\'opzione {{RadioButton|TRUE|Inserisci MIBA}} per aggiungere le informazioni [MIBA](MIBA/it.md) al file. Non tutti i formati immagine lo supportano.
2.  Oppure selezionare l\'opzione {{RadioButton|TRUE|Inserisci commento}} e digitare un commento nel campo di testo per incorporare un commento nel file. Non tutti i formati immagine lo supportano.
3.  Selezionare la casella di controllo {{CheckBox|TRUE|Aggiungi filigrana}} per aggiungere una filigrana. La filigrana si trova nell\'angolo in basso a sinistra dell\'immagine ed è costituita dal logo e dal nome di FreeCAD sopra l\'URL principale di FreeCAD: [www.freecadweb.org](http://www.freecadweb.org).



## Note

-   Il numero di formati di file immagine disponibili può variare a seconda del sistema operativo.
-   Alcuni driver OpenGL non consentono rendering al di sopra di una certa dimensione massima.



## Preferenze

-   Lo sfondo della vista 3D può essere modificato nelle preferenze: **Modifica → Preferenze... → Visualizzazione → Colori → Colore di sfondo**. Vedi [Editor delle preferenze](Preferences_Editor/it#Colori.md).
-   Per cambiare l\'anti-aliasing della vista 3D: **Modifica → Preferenze... → Visualizzazione → Vista 3D → Rendering → Anti-Aliasing**. Vedi [Editor delle preferenze](Preferences_Editor/it#Vista_3D.md).



## Script

È possibile creare screenshot con codice Python.


```python
Gui.ActiveDocument.ActiveView.saveImage('C:/temp/test.png',1656,783,'Current')
```

Questo script salva una serie di screenshot di diverse dimensioni e da diverse direzioni. Anche il tipo di fotocamera, ortogonale o prospettica, viene modificato.


```python
import Part, PartGui
# Loading test part
Part.open('C:/Documents and Settings/jriegel/My Documents/Projects/FreeCAD/data/Blade.stp')
OutDir = 'C:/temp/'
 
# Creating images with different Views, Cameras and sizes
for p in ['PerspectiveCamera','OrthographicCamera']:
    Gui.SendMsgToActiveView(p)
    for f in ['ViewAxo','ViewFront','ViewTop']:
        Gui.SendMsgToActiveView(f)
        for x,y in [[500,500],[1000,3000],[3000,1000],[3000,3000],[8000,8000]]:
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + 'Blade_' + p +'_' + f + '_' + x + '_' + y + '.jpg',x,y,'White')
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + 'Blade_' + p +'_' + f + '_' + x + '_' + y + '.png',x,y,'Transparent')

# Close active document
App.closeDocument(App.ActiveDocument.Name)
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewScreenShot/it
