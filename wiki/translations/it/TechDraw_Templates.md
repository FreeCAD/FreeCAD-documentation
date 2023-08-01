# TechDraw Templates/it
<div class="mw-translate-fuzzy">





</div>







<div class="mw-translate-fuzzy">

## Presentazione


</div>


<div class="mw-translate-fuzzy">

Ogni pagina TechDraw è basata su un oggetto Template. Il modello controlla la dimensione della carta e contiene degli elementi grafici e dei testi fissi, ad esempio una cornice di pagina o un bordo.


</div>

Il modello può anche contenere campi di testo modificabili per attributi come *Title*, *Subtitle*, *Author*, *Date*, *Scale*, *Weight*, *Drawing number*, e *Sheet*.


<div class="mw-translate-fuzzy">

I modelli sono file [SVG](SVG/it.md) che possono essere creati e modificati al di fuori di FreeCAD, con un\'applicazione come [Inkscape](https://en.wikipedia.org/wiki/Inkscape).


</div>



## Proprietà


<div class="mw-translate-fuzzy">

-    **Orientation**: Verticale o Orizzontale - Ritratto o Paesaggio.

-    **Width**: Larghezza della carta in mm.

-    **Height**: Altezza della carta in mm

-    **Page Result**: Una copia del file di modello originale che include tutte le modifiche fatte ai testi modificabili. Ciò consente agli utenti che non hanno una copia del file Modello di vedere la Pagina come prevista in originale. Non tipicamente utile per gli utenti finali.

-    **Template**: a) Un puntatore alla copia del file di Modello originale incorporato in questo file \*.FCSTD, o b) un percorso a un file di modello accessibile sul computer corrente. Utilizzare i puntini di sospensione (\...) per passare a selezionare un file modello diverso.


</div>

## Select a different template file 

To select a different template for a drawing:

1.  Locate the desired Page object in the [Tree view](Tree_view.md).
2.  Expand the Page node if necessary.
3.  Select the Template object.
4.  In the [Property editor](Property_editor.md) click in the **Template** property field.
5.  Press the **...** (ellipsis) button that appears.
6.  A file dialog opens the folder the current template is located in. If the Page was created in the current FreeCAD session this will be the default template folder (as set in the [TechDraw Preferences](TechDraw_Preferences#Files.md)).
7.  Optionally browse to another folder.
8.  Select a different template file.
9.  Press the **OK** button.

If you have modified a template file and want to update a Page created in the current FreeCAD session that uses this template, temporarily select a different file first, and then select the modified file again.



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


<div class="mw-translate-fuzzy">

Vedere anche [Come creare un modello TechDraw personalizzato](TechDraw_TemplateHowTo/it.md).


</div>



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



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Templates/it
