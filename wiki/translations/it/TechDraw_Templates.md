# TechDraw Templates/it




<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Presentazione

Ogni pagina TechDraw è basata su un oggetto Template. Il modello controlla la dimensione della carta e contiene degli elementi grafici e dei testi fissi, ad esempio una cornice di pagina o un bordo.

Il modello può anche contenere campi di testo modificabili per attributi come *Title*, *Subtitle*, *Author*, *Date*, *Scale*, *Weight*, *Drawing number*, e *Sheet*.

I modelli sono file [SVG](SVG/it.md) che possono essere creati e modificati al di fuori di FreeCAD, con un\'applicazione come [Inkscape](https://en.wikipedia.org/wiki/Inkscape).

## Proprietà


<div class="mw-translate-fuzzy">

-    **Orientation**: Verticale o Orizzontale - Ritratto o Paesaggio.

-    **Width**: Larghezza della carta in mm.

-    **Height**: Altezza della carta in mm

-    **Page Result**: Una copia del file di modello originale che include tutte le modifiche fatte ai testi modificabili. Ciò consente agli utenti che non hanno una copia del file Modello di vedere la Pagina come prevista in originale. Non tipicamente utile per gli utenti finali.

-    **Template**: a) Un puntatore alla copia del file di Modello originale incorporato in questo file \*.FCSTD, o b) un percorso a un file di modello accessibile sul computer corrente. Utilizzare i puntini di sospensione (\...) per passare a selezionare un file modello diverso.


</div>

## Changing Template File 

To change the template of a drawing

1.  click the desired page in the tree
2.  if not already open the tree should open a small sub-tree with several leaves
3.  Select the Template leaf
4.  in the property panel/Data Tab/Template is the path to the template file. To change the file press the ellipsis button (\'\...\'). This will open your default template folder (as set in Preferences/TechDraw).
5.  select another template file.

The new file will be opened directly.

When you want to update a changed template file note that you have to load another file before you can select the same file again. This is because the selection of the same file is ignored.

## Modelli personalizzati 

In FreeCAD è incluso un numero limitato di modelli preformattati in vari formati di pagine standard. Questi si trovano in


```python
$INSTALL_DIR/Mod/TechDraw/Templates/
```

dove `$INSTALL_DIR` è la directory in cui è stato installato FreeCAD, per esempio


```python
/usr/share/freecad/Mod/TechDraw/Templates/
```


<div class="mw-translate-fuzzy">

I modelli personalizzati possono anche essere specificati come predefiniti nelle [Preferenze di TechDraw](TechDraw_Preferences/it.md).


</div>

Vedere anche [Come creare un modello TechDraw personalizzato](TechDraw_TemplateHowTo/it.md).

## Note

-   I modelli TechDraw non sono interamente intercambiabili con i [Modelli Drawing](Drawing_templates/it.md). In generale, i modelli di Drawing funzionano anche in TechDraw, ma possono esserci dei problemi con il testo modificabile.

-   Le clausole di trasformazione Svg causano dei problemi nei modelli personalizzati. Vedere la [Stackoverflow](https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files) discussione sulla rimozione delle clausole di trasformazione nei file SVG.


<div class="mw-translate-fuzzy">

La clausola **xml:space=\"preserve\"** causa a volte problemi di dimensioni e posizionamento del testo. È meglio evitare o rimuovere questa clausola dal codice SVG del modello personalizzato.


</div>


<div class="mw-translate-fuzzy">

-   I modelli funzionano meglio quando non contengono codice SVG superfluo (da alcuni chiamato \"spazzatura SVG\"). C\'è un buon articolo su [removing garbage from SVG here](https://freecad-gost.ru/news/gost-templates-techdraw-09-01-2020/). L\'articolo è in russo.


</div>


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
