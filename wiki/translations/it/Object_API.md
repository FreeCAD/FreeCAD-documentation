# Object API/it
**(Ottobre 2019) Non modificare queste pagine. Le informazioni sono incomplete e obsolete. Per l'API più recente, consultare la [https://www.freecadweb.org/api documentazione API autogenerata] o generare la documentazione autonomamente. Vedere [Documentazione del codice sorgente](Source_documentation/it.md).**

Essendo parametrici, in FreeCAD gli oggetti del documento possono avere un sacco di altre proprietà. Queste sono quelle di base, presenti in ogni FreeCAD Document Object. Gli oggetti possono essere recuperati semplicemente con il loro nome. Esempio: 
```python
myObj = FreeCAD.ActiveDocument.myObjectName
print myObj.PropertiesList
```


{{APIProperty|Content|Una rappresentazione XML delle proprietà di un oggetto.}}


{{APIProperty|Label|Ottiene / imposta l'etichetta degli oggetti. La stringa può essere unicode.}}


{{APIProperty|Name|Il nome univoco di un oggetto.}}


{{APIProperty|Placement|Ottiene / imposta il posizionamento di un oggetto. Un posizionamento definisce un orientamento (rotazione) ed una posizione (base) nello spazio 3D. Viene utilizzato quando non è necessario alcun ridimensionamento o altro tipo di distorsione.}}


{{APIProperty|PropertiesList|Un elenco delle proprietà di un oggetto}}


{{APIProperty|State| Lo stato di FreeCAD di un oggetto (ad esempio se deve essere ricalcolato)}}


{{APIProperty|Type|Una stringa che descrive il tipo di oggetto}}


{{APIProperty|ViewObject|Il View Provider associato (oggetto FreeCADGUI) a un oggetto}}


{{APIFunction|getAllDerivedFrom| | |Tutti i discendenti di questo oggetto}}


{{APIFunction|getDocumentationOfProperty| | |La stringa di documentazione della proprietà di questa classe.}}


{{APIFunction|getGroupOfProperty| | |Il nome del gruppo a cui appartiene la proprietà in questa categoria. Le proprietà sono ordinate in gruppi diversi denominati secondo convenienza.}}


{{APIFunction|getPropertyByName| | |Il valore di una proprietà denominata.}}


{{APIFunction|getTypeOfProperty| | |Il tipo di una proprietà denominata. Questo può essere (Hidden,ReadOnly,Output) o qualsiasi combinazione.}}


{{APIFunction|isDerivedFrom| | |True se il tipo dato è un padre}}


{{APIFunction|purgeTouched| |Contrassegna l'oggetto come unchanged (invariato)| }}


{{APIFunction|touch| |Contrassegna l'oggetto come changed (modificato, toccato)| }}


 

[<img src="images/Property.png" style="width:16px"> API](Category_API.md) [<img src="images/Property.png" style="width:16px"> Poweruser Documentation](Category_Poweruser_Documentation.md)

---
[documentation index](../README.md) > [API](Category_API.md) > Object API/it
