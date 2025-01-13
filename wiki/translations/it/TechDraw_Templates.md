# TechDraw Templates/it
## Descrizione

Ogni pagina TechDraw è basata su un oggetto Modello (Template). Il Modello fornisce un\'area sullo sfondo della pagina per inserire viste, simboli e altri oggetti di annotazione e ne definisce le dimensioni del foglio. Verrà eseguito il rendering per l\'esportazione o la stampa solo degli elementi all\'interno dell\'area di disegno.

Il modello può anche contenere elementi grafici come una cornice che definisce l\'area di disegno, compresi campi indicizzati, segni di piegatura e, facoltativamente, un cartiglio che a sua volta contiene testi fissi e [modificabili](Svg_Namespace#freecad_editable.md). Il cartiglio può anche essere inserito separatamente come [simbolo](TechDraw_Symbol/it.md).

I Modelli, come i simboli, sono file [SVG](SVG/it.md) che possono essere creati e modificati all\'esterno di FreeCAD, sia con un\'applicazione come [Inkscape](https://en.wikipedia.org/wiki/Inkscape), sia con un semplice editor di testo. Entrambi possono contenere campi di testo modificabili ma utilizzano strumenti di modifica diversi.

Un nuovo strumento di compilazione automatica ({{Version/it|1.0}}) può riempire automaticamente i campi di testo modificabili di un modello nel momento in cui viene inserito. Ciò richiede modelli che utilizzano il nuovo attributo [freecad:autofill](Svg_Namespace#freecad_autofill.md). I seguenti nomi di attributi sono validi per la compilazione automatica: \"author\", \"date\", \"organization\", \"scale\", \"sheet\", \"title\", \"page_number\", e \"page_count\".



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Modello ha le seguenti proprietà:


{{TitleProperty|Base}}

-    **Orientation|Enumeration**: {{Value|Portrait}} o {{Value|Landscape}}.


{{TitleProperty|Page Properties}}

-    **Width|Length**: Larghezza della carta in mm.

-    **Height|Length**: Altezza della carta in mm.

-    **Editable Texts|Map|Hidden**: Key:Value elenco dei testi modificabili nel modello.


{{TitleProperty|Template}}

-    **Page Result|FileIncluded**: Una copia del file Modello originale che include tutte le modifiche ai testi modificabili. Ciò consente agli utenti che potrebbero non disporre di una copia del file modello di visualizzare la Pagina come previsto. In genere non è utile per gli utenti finali.

-    **Template|File**: Un puntatore alla copia del file modello originale incorporato in questo file ***.FCStd** o un percorso file a un Modello accessibile sul dispositivo corrente. Consultare il [paragrafo successivo](#Selezionare_un_file_Modello_diverso.md) per informazioni su come modificare il Modello.



## Selezionare un file Modello diverso 

Per selezionare un Modello diverso per un disegno:

1.  Individuare l\'oggetto Pagina desiderato nella [Vista ad albero](Tree_view/it.md).
2.  Espandere il nodo Pagina se necessario.
3.  Selezionare l\'oggetto Modello.
4.  Nell\'[Editor delle proprietà](Property_editor.md) fare clic sul campo della proprietà **Template**.
5.  Premere il pulsante **...** (puntini di sospensione) visualizzato.
6.  Una finestra di dialogo apre la cartella in cui si trova il modello corrente. Se la pagina è stata creata nella sessione corrente di FreeCAD, questa sarà la cartella del modello predefinita (come impostata in [Preferenze di TechDraw](TechDraw_Preferences/it#Files.md)).
7.  Facoltativamente passare a un\'altra cartella.
8.  Selezionare un file modello diverso.
9.  Premere il pulsante **OK**.

Se si ha modificato un file modello e si desidera aggiornare una pagina creata nella sessione corrente di FreeCAD che utilizza questo modello, selezionare prima temporaneamente un file diverso, quindi seleziona nuovamente il file modificato.



## Modelli personalizzati 

In FreeCAD è incluso un numero limitato di modelli preformattati in vari formati di pagine standard. Questi si trovano in


```python
$INSTALL_DIR/Mod/TechDraw/Templates/
```

dove `$INSTALL_DIR` è la directory in cui è stato installato FreeCAD, per esempio


```python
/usr/share/freecad/Mod/TechDraw/Templates/
```

I modelli personalizzati possono anche essere specificati come predefiniti nelle [Preferenze di TechDraw](TechDraw_Preferences/it.md).

Vedere anche [Come creare un modello TechDraw personalizzato](TechDraw_TemplateHowTo/it.md) oppure, se si preferiscono i modelli generati da script, [TechDraw TemplateGenerator](TechDraw_TemplateGenerator/it.md) e [Macro TemplateHelper](Macro_TemplateHelper/it.md).



## Note

-   La libreria che FreeCAD utilizza per elaborare SVG **supporta solo la specifica svg-tiny**. In particolare: \"SVG Tiny non supporta sfumature, trasparenza, ritaglio, maschere, simboli, motivi, testo sottolineato, testo barrato, testo verticale o effetti filtro SVG.\" (dalla Guida di Adobe Illustrator). L\'utilizzo di queste funzionalità nel modello personalizzato causerà problemi di rendering.

-   Le clausole di trasformazione Svg possono causare dei problemi nei modelli personalizzati. Vedere la [Stackoverflow](https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files) discussione sulla rimozione delle clausole di trasformazione nei file SVG, soprattutto se Inkscape ne ha usati troppi. Ma non possono essere evitati se si ha bisogno di testo ruotato nel proprio modello.

La clausola **xml:space=\"preserve\"** causa a volte problemi di dimensioni e posizionamento del testo. È meglio evitare o rimuovere questa clausola dal codice SVG del proprio modello personalizzato.

-   I modelli funzionano meglio quando non contengono codice SVG superfluo (da alcuni chiamato \"spazzatura SVG\"). C\'è un buon articolo su [removing garbage from SVG here](https://freecad-gost.ru/news/gost-templates-techdraw-09-01-2020/). L\'articolo è in russo.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Templates/it
