# ViewObject API/it
 **(Ottobre 2019) Non modificare queste pagine. Le informazioni sono incomplete e obsolete. Per l'API più recente, consultare la [https://www.freecadweb.org/api documentazione API autogenerata] o generare la documentazione autonomamente. Vedere [Documentazione del codice sorgente](Source_documentation/it.md).**

Quando la GUI è attiva, a ogni oggetto del documento FreeCAD è associato un ViewObject, che risiede nella controparte FreeCADGui del documento. Un oggetto della vista può essere recuperato in due modi. Esempio: 
```python
myViewObj = FreeCAD.ActiveDocument.myObjectName.ViewObject
myViewObj = FreeCADGui.ActiveDocument.myObjectName
print myViewObj.IV
```


{{APIProperty|Annotation|il nodo della annotazione di un oggetto della vista ViewObject}}


{{APIProperty|BoundingBox|Il contenitore}}


{{APIProperty|Content|una rappresentazione XML delle proprietà di un ViewObject}}


{{APIProperty|DisplayMode|la modalità di visualizzazione corrente}}


{{APIProperty|IV|una rappresentazione Inventor del ViewObject}}


{{APIProperty|Object|il FreeCAD Document Object associato a questo ViewObject}}


{{APIProperty|PropertiesList|un elenco di proprietà di questo ViewObject}}


{{APIProperty|RootNode|il nodo di Inventor di questo ViewObject (pivy.coin object)}}


{{APIProperty|Selectable|True se l'oggetto è selezionabile}}


{{APIProperty|Type|il tipo di questo ViewObject}}


{{APIProperty|Visibility|True se il viewObject è visibile}}


{{APIFunction|getAllDerivedFrom| | |tutti i discendenti di questo oggetto}}


{{APIFunction|getDocumentationOfProperty| | |la stringa di documentazione della proprietà di questa classe.}}


{{APIFunction|getGroupOfProperty| | |il nome del gruppo al quale appartiene la proprietà in questa classe. Per comodità, le proprietà sono ordinate in gruppi con nomi diversi.}}


{{APIFunction|getPropertyByName| | |il valore di una proprietà denominata.}}


{{APIFunction|getTypeOfProperty| | |il tipo di una proprietà denominata. Questo può essere(Hidden,ReadOnly,Output) o qualsiasi combinazione.}}


{{APIFunction|hide| |Nasconde l'oggetto.| }}


{{APIFunction|isDerivedFrom|string|Controlla se questo oggetto è derivato dal dato tipo di oggetto | True se il tipo dato è suo genitore}}


{{APIFunction|isVisible| |Controlla se l'oggetto è visibile | un valore booleano}}


{{APIFunction|listDisplayModes| |Mostra un elenco di tutte le modalità di visualizzazione |una lista}}


{{APIFunction|setTransformation|coin.SoTransform|Imposta una trasformazione sul nodo Inventor |nulla}}


{{APIFunction|show| |Mostra l'oggetto, se è nascosto |nulla}}


{{APIFunction|toString| | |una rappresentazione in stringa del nodo Inventor}}


{{APIFunction|update| |Aggiorna la rappresentazione della vista dell'oggetto| }}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
