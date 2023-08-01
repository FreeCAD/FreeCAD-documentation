---
- TutorialInfo:/it
   Topic:Disegno tecnico
   Level:Intermedio
   Time:60 minuti
   Author:[http://freecadweb.org/wiki/index.php?title=User:wandererfan wandererfan]
   FCVersion:0.17
---

# TechDraw TemplateHowTo/it







## Introduzione

Questo tutorial mostra come creare un file [SVG](SVG/it.md) da usare come [modello di squadratura](TechDraw_Templates/it.md) per le pagine di [TechDraw](TechDraw_Workbench/it.md).

Questa guida presume che si abbia una discreta familiarità con [Inkscape](https://en.wikipedia.org/wiki/Inkscape), [SVG](SVG/it.md) e l\'ambiente [TechDraw](TechDraw_Workbench/it.md) di FreeCAD.

Faremo un semplice modello in formato Letter americano con orientamento orizzontale.

Una copia del risultato di questo HowTo è disponibile nella directory dei modelli di FreeCAD: 
```python
$INSTALL_DIR/Mod/TechDraw/Templates/HowToExample.svg
```

Dove `$INSTALL_DIR` è la directory in cui è stato installato FreeCAD, per esempio 
```python
/usr/share/freecad/Mod/TechDraw/Templates/HowToExample.svg
```



## Creare un documento di base 

1\. Aprire un nuovo documento in Inkscape.

2\. Nelle Proprietà del documento

-   selezionare il formato \"US Letter\" o \"A4\" e l\'orientamento orizzontale
-   Impostare le unità predefinite su \"mm\" e le dimensioni della pagina su larghezza \"279.4\" e altezza \"215.9\". Per DIN-A4 impostare \"210\" e \"297\".

<img alt="" src=images/InkDocProp.png  style="width:800px;"> 
*align=center|Inkscape: il documento con dimensioni e orientamento della pagina* 

3\. Usare l\'editor XML (menu Modifica -\> Editor XML\...) per aggiungere una clausola \"freecad\" namespace a ogni elemento `<svg>`.

:   xmlns:freecad="[http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace](http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace)". Notare che i testi modificabili *non* funzioneranno se usi \"<https://>\...\", anche se il wiki viene raggiunto tramite https in questi giorni. Poiché SVG è un formato umanamente leggibile, si può anche inserire la riga sopra nel file con un editor di testo.

<img alt="" src=images/InkXMLNameSpace.png  style="width:800px;"> 
*align=center|Inkscape: editor XML che aggiunge la clausola "freecad" namespace all'elemento <svg>* 



## Creare il disegno del modello 

4\. Disegnare contorni, numeri di zona, linee centrali e altre geometrie.

5\. Disegnare le caselle e le linee per il cartiglio.

6\. Aggiungere e posizionare il testo statico.

7\. Aggiungere e posizionare il testo che sarà modificabile.

8\. Ora, il lavoro finito dovrebbe assomigliare a questo: <img alt="" src=images/InkFinishedArt.png  style="width:800px;"> 
*align=center|Inkscape: layout del modello provvisorio* 



## Creare i campi modificabili 

9\. Utilizzare l\'editor XML per aggiungere un tag `freecad:editable` a ogni elemento `<text>` editable.

-   Assegnare un nome di campo significativo a ogni testo modificabile.

<img alt="" src=images/InkXMLeditableTag.png  style="width:800px;"> 
*align=center|Inkscape: editor XML che aggiunge la proprietà "freecad:editable" a ogni elemento <text>* 



## Regolare le dimensioni del SVG 

10\. Utilizzare l\'editor XML per regolare l\'attributo `viewBox` in modo che corrisponda alle dimensioni della pagina in millimetri.

-   Sono quattro valori, nel formato `"0 0 larghezza altezza"`

<img alt="" src=images/InkXMLviewBox.png  style="width:800px;"> 
*align=center|Inkscape: editor XML che regola la viewbox in modo che corrisponda alle dimensioni della pagina in millimetri* 

11\. Ora il modello appare molto più grande di quanto desiderato. <img alt="" src=images/InkMuchTooBig.png  style="width:800px;"> 
*align=center|Inkscape: layout del modello provvisorio che supera la dimensione della pagina* 

12\. Bisogna ridurlo.

-    **Modifica → Seleziona tutto in ogni livello**, o box di selezione e selezionare tutto.

-   Adattare gli spinbox **W:** e **H:** per impostare le dimensioni del disegno in millimetri.

-   Impostare la dimensione della pagina meno eventuali margini applicabili, ad esempio {{Button | W: 250}} e {{Button | H: 200}}.

13\. Usare **Oggetto → Allinea e distrubuisci** o gli spinbox **X:** e **Y:** per posizionare il disegno entro i limiti della pagina, se necessario.

14\. Ora il modello dovrebbe apparire corretto, proprio come nella foto sopra del disegno finito.



## Rimuovere le trasformazioni nel file SVG 

15\. Assicurarsi che tutti i testi modificabili siano \"non raggruppati\" con **Maiusc**+**Ctrl**+**g**.

16\. Selezionare tutti gli elementi della pagina, **Modifica → Seleziona tutto**, e poi **Modifica → Copia** (**Ctrl**+**c**).

17\. Quindi eliminare il livello, layer corrente, **Livello → Elimina livello attuale**.: Nota: se si è già eliminato il livello (nel pannello dei livelli non è elencato alcun livello) questo passaggio non è necessario. In tal caso si dovrebbe selezionare tutto (**Ctrl**+**a**), tagliare la selezione (**Ctrl**+**x**) e incollarla con il comando nel passaggio successivo.

18\. Poi incollare, **Modifica → Incolla in origine**.

:   **Nota:** Questo comando impedisce che le posizioni del testo vengano memorizzate nei tag di trasformazione. È importante non utilizzare il normale comando incolla!

19\. Ora il modello dovrebbe apparire corretto e non dovrebbe avere trasformazioni indesiderate.

20\. Salvare il modello. Quando si usa Inkscape, salvarlo preferibilmente come **Plain SVG** perché FreeCAD può gestire solo le caratteristiche della specifica SVG 1.1. **Plain SVG** rimuoverà qualsiasi tag XML specifico di Inkscape.

21\. Provarlo in FreeCAD e [Ambiente TechDraw](TechDraw_Workbench/it.md) con [Nuovo disegno da modello](TechDraw_PageTemplate/it.md). ![](images/FCTemplateHow.png ) 
*align=center|FreeCAD: modello finito con un campo di testo modificabile modificato* 

## Note

Non utilizzare i livelli in Inkscape prima di aver imparato a creare il modello senza di essi. Livelli (e gruppi) possono inserire automaticamente trasformazioni indesiderate nel file [SVG](SVG/it.md) risultante.

Come ultimo passo prima di utilizzare il nuovo modello, assicursi di rimuovere eventuali clausole di trasformazione dal codice Svg. Le clausole di trasformazione **causano problemi**.

Vedere una discussione su StackOverflow [removing transform clauses in SVG files](https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files).

Se non si vedono le caselle verdi, per i tuoi testi modificabili, potrebbe esserci qualcosa che non va nella scala del tuo documento. Aprire di nuovo il file in Inkscape e verificare, che i valori di viewBox e le dimensioni corrispondano.

Se i testi appaiono sfalsati in FreeCAD, potrebbe essere necessario rimuovere gli attributi {{Incode|xml:space<nowiki>=</nowiki>"preserve"}} nel file SVG. Vedere: <https://www.forum.freecadweb.org/viewtopic.php?t=50897>.


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw TemplateHowTo/it
