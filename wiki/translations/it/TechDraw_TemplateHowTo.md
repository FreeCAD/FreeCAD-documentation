# TechDraw TemplateHowTo/it




{{TutorialInfo/it
|Topic=Disegno tecnico
|Level=Intermedio
|Time=60 minuti
|Author=[http://freecadweb.org/wiki/index.php?title=User:wandererfan wandererfan]
|FCVersion=0.17
}}

## Introduzione


<div class="mw-translate-fuzzy">

Questo tutorial mostra come creare un file [SVG](SVG/it.md) da usare come [modello di squadratura](TechDraw_Templates/it.md) per le pagine di [TechDraw](TechDraw_Workbench/it.md).


</div>


<div class="mw-translate-fuzzy">

Questa guida presume che si abbia una discreta familiarità con [Inkscape](https://en.wikipedia.org/wiki/Inkscape), [SVG](SVG/it.md) e l\'ambiente [TechDraw](TechDraw_Workbench/it.md) di FreeCAD.


</div>

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


<div class="mw-translate-fuzzy">

2\. Nelle Proprietà del documento

-   selezionare il formato (US Letter) e l\'orientamento orizzontale
-   Impostare le unità predefinite su \"mm\" e le dimensioni della pagina su larghezza \"279.4\" e altezza \"215.9\".

<img alt="" src=images/InkDocProp.png  style="width:800px;"> *align=center|Inskcape: il documento con dimensioni e orientamento della pagina* 


</div>


<div class="mw-translate-fuzzy">

3\. Usare l\'editor XML (menu Modifica -\> Editor XML\...) per aggiungere una clausola \"freecad\" namespace a ogni elemento `<svg>`.

-   xmlns:freecad="[http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace](http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace)".

<img alt="" src=images/InkXMLNameSpace.png  style="width:800px;"> *align=center|Inkscape: editor XML che aggiunge la clausola "freecad" namespace all'elemento <svg>* 


</div>

## Creare il disegno del modello 

4\. Disegnare contorni, numeri di zona, linee centrali e altre geometrie.

5\. Disegnare le caselle e le linee per il cartiglio.

6\. Aggiungere e posizionare il testo statico.

7\. Aggiungere e posizionare il testo che sarà modificabile.

8\. Ora, il lavoro finito dovrebbe assomigliare a questo: <img alt="" src=images/InkFinishedArt.png  style="width:800px;"> *align=center|Inkscape: layout del modello provvisorio* 

## Creare i campi modificabili 

9\. Utilizzare l\'editor XML per aggiungere un tag `freecad:editable` a ogni elemento `<text>` editable.

-   Assegnare un nome di campo significativo a ogni testo modificabile.

<img alt="" src=images/InkXMLeditableTag.png  style="width:800px;"> *align=center|Inkscape: editor XML che aggiunge la proprietà "freecad:editable" a ogni elemento <text>* 

## Regolare le dimensioni del SVG 

10\. Utilizzare l\'editor XML per regolare l\'attributo `viewBox` in modo che corrisponda alle dimensioni della pagina in millimetri.

-   Sono quattro valori, nel formato `"0 0 larghezza altezza"`

<img alt="" src=images/InkXMLviewBox.png  style="width:800px;"> *align=center|Inkscape: editor XML che regola la viewbox in modo che corrisponda alle dimensioni della pagina in millimetri* 

11\. Ora il modello appare molto più grande di quanto desiderato. <img alt="" src=images/InkMuchTooBig.png  style="width:800px;"> *align=center|Inkscape: layout del modello provvisorio che supera la dimensione della pagina* 

12\. Bisogna ridurlo.

-    **Modifica → Seleziona tutto in ogni livello**, o box di selezione e selezionare tutto.

-   Adattare gli spinbox **W:** e **H:** per impostare le dimensioni del disegno in millimetri.

-   Impostare la dimensione della pagina meno eventuali margini applicabili, ad esempio {{Button | W: 250}} e {{Button | H: 200}}.

13\. Usare **Oggetto → Allinea e distrubuisci** o gli spinbox **X:** e **Y:** per posizionare il disegno entro i limiti della pagina, se necessario.

14\. Ora il modello dovrebbe apparire corretto, proprio come nella foto sopra del disegno finito.

## Rimuovere le trasformazioni nel file SVG 

15\. Assicurarsi che tutti i testi modificabili siano \"non raggruppati\" con **Maiusc**+**Ctrl**+**g**.


<div class="mw-translate-fuzzy">

16\. Selezionare tutti gli elementi della pagina, **Modifica → Seleziona tutto**, e poi **Modifica → Copia**.


</div>


<div class="mw-translate-fuzzy">

17\. Quindi eliminare il livello, layer corrente, **Livello → Elimina livello attuale**.


</div>


<div class="mw-translate-fuzzy">

18\. Poi incollare, **Modifica → Incolla in origine**.


</div>

19\. Ora il modello dovrebbe apparire corretto e non dovrebbe avere trasformazioni indesiderate.


<div class="mw-translate-fuzzy">

20\. Salvare il modello.


</div>


<div class="mw-translate-fuzzy">

21\. Provarlo in FreeCAD e [TechDraw](TechDraw_Workbench/it.md) con [Nuovo disegno da modello](TechDraw_New_Pick/it.md). ![](images/FCTemplateHow.png ) *align=center|FreeCAD: modello finito con un campo di testo modificabile modificato* 


</div>


<div class="mw-translate-fuzzy">

## Note

Non utilizzare i livelli in Inkscape prima di aver imparato a creare il modello senza di essi. Livelli (e gruppi) possono inserire automaticamente trasformazioni indesiderate nel file [SVG](SVG/it.md) risultante.


</div>

Come ultimo passo prima di utilizzare il nuovo modello, assicursi di rimuovere eventuali clausole di trasformazione dal codice Svg. Le clausole di trasformazione **causano problemi**.

Vedere una discussione su StackOverflow [removing transform clauses in SVG files](https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files).

If you do not see the green boxes for your editable texts, there might be something wrong with your document scale. Open your file in Inkscape again and confirm the values of the viewBox and the sizes are matching.


{{Tutorials navi

}} {{TechDraw Tools navi}} 
