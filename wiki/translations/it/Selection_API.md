# Selection API/it
**(Ottobre 2019) Non modificare queste pagine. Le informazioni sono incomplete e obsolete. Per l'API più recente, consultare la [https   *//www.freecadweb.org/api documentazione API autogenerata] o generare la documentazione autonomamente. Vedere [Documentazione del codice sorgente](Source_documentation/it.md).**

Il sottomodulo Selection fa parte del modulo FreeCADGui. Esempio   * 
```python
import FreeCADGui
sel = FreeCADGui.Selection.getSelection()
```


{{APIFunction|addSelection|FreeCAD.Object|Aggiunge un oggetto alla selezione| }}


{{APIFunction|clearSelection|[string]|Cancella dalla selezione il documento con un determinato nome. Se non viene fornito alcun documento viene cancellata la selezione completa.| }}


{{APIFunction|getSelection|[string]|Restituisce un elenco di oggetti documento selezionati per un dato nome di documento. Se non viene dato nessun documento restituisce la selezione completa. | Un elenco di oggetti del documento nell'ordine in cui sono stati selezionati.}}


{{APIFunction|getSelectionEx|[string]|Restituisce un elenco di SelectionObject per un dato nome di documento. Se non viene dato nessun documento restituisce la selezione completa. usato per selezionare sottoggetti (es alcuni Edges di una Face).|una lista di SelectionObjects nell'ordine in cui sono stati selezionati}}


{{APIFunction|isSelected|FreeCAD.Object|Controlla se un dato oggetto è selezionato| }}


{{APIFunction|removeSelection|FreeCAD.Object|Rimuove un oggetto dalla selezione| }}


 

[Category   *API](Category_API.md) [Category   *Poweruser Documentation](Category_Poweruser_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Selection API/it
