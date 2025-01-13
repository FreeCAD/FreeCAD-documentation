# FeaturePython methods/it
## Introduzione

Questa pagina funge da riferimento per i metodi sovrascrivibili disponibili negli [Creare oggetti FeaturePython parte I](Create_a_FeaturePython_object_part_I/it.md) o [Oggetti creati da script](Scripted_objects/it.md).

## Riferimento primario 

I metodi seguenti rappresentano circa il 99% dei casi d\'uso che gli utenti esperti possono avere per le classi proxy Python.

++++
|                             | Chiamato durante il ricalcolo del documento                                         | Non chiamare `recompute()` da questo metodo (o qualsiasi metodo chiamato da `execute()`) poiché ciò provoca un ricalcolo nidificato.                                                                                                                                                                                                                                                               |
| `execute(self, obj)`              |                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                         |                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
++++
|                             | Chiamato prima che il valore di una proprietà venga modificato                      |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `onBeforeChange(self, obj, prop)` |                                                                                     | `prop`                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                         |                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                            |                                                                                     | è il nome della proprietà da modificare, non l\'oggetto proprietà stesso. Le modifiche alla proprietà non possono essere annullate. I valori delle proprietà precedente/successiva non sono disponibili contemporaneamente per il confronto.                                                                                                                                                                                                     |
++++
|                             | Chiamato dopo la modifica di una proprietà                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `onChanged(self, obj, prop)`      |                                                                                     | `prop`                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                         |                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                            |                                                                                     | è il nome della proprietà da modificare, non l\'oggetto proprietà stesso.                                                                                                                                                                                                                                                                                                                                                                        |
++++
|                             | Chiamato dopo il ripristino di un documento o la copia di un oggetto FeaturePython. | Occasionalmente, i riferimenti all\'oggetto FeaturePython dalla classe o alla classe dall\'oggetto FeaturePython potrebbero essere interrotti, poiché il metodo della classe `__init__()` non viene chiamato quando l\'oggetto viene ricostruito. L\'aggiunta di `self.Object <nowiki>=</nowiki> obj` o `obj.Proxy <nowiki>=</nowiki> self` spesso risolve questi problemi. |
| {{Incode|onDocumentRestored(self, obj)}}   |                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                         |                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
++++

Non è raro incontrare una situazione in cui i callback Python non vengono attivati ​​come dovrebbero. I principianti in questa situazione possono essere certi che il sistema di callback FeaturePython non è fragile o corrotto. Invariabilmente quando i callback non vengono eseguiti è perché un riferimento è perso o non è definito nel codice sottostante. Se, tuttavia, i callback sembrano non funzionare senza alcuna spiegazione, fornire riferimenti a oggetti/proxy nel callback `onDocumentRestored()` (come indicato nella prima tabella sopra) può alleviare questi problemi. Finché non ci si sente a proprio agio con il sistema di callback, potrebbe essere utile aggiungere istruzioni print in ogni callback per stampare messaggi sulla console durante lo sviluppo.

## Metodi aggiuntivi 

I metodi seguenti sono per l\'uso **avanzato** delle classi proxy Python e normalmente non ci sarà bisogno di usarli.

-   mustExecute
-   getViewProviderName
-   getSubObject
-   getSubObjects
-   getLinkedObject
-   hasChildElement
-   isElementVisible
-   canLinkProperties
-   allowDuplicateLabel
-   redirectSubName
-   canLoadPartial
-   onBeforeChangeLabel

## Determinazione dei metodi Python disponibili 

All\'interno della [FeaturePython Template Class](https://github.com/FreeCAD/FreeCAD/blob/76e74294894bbce46d006e149315c6274d206278/src/App/FeaturePython.h#L161-L351) esistono varie () chiamate.

Ognuna di queste corrisponde a un metodo Python associato disponibile.

Ad esempio, imp->execute() [alla riga 193](https://github.com/FreeCAD/FreeCAD/blob/76e74294894bbce46d006e149315c6274d206278/src/App/FeaturePython.h#L193) indica che il metodo execute è disponibile.

Nota, getPyObject() e init() sono casi speciali e non seguono l\'euristica di cui sopra.



## Vedere anche 

-   [FreeCAD GitHub: FeaturePython.h - public API](https://github.com/FreeCAD/FreeCAD/blob/76e74294894bbce46d006e149315c6274d206278/src/App/FeaturePython.h#L44-L86)
-   [FreeCAD GitHub: FeaturePythonT template class](https://github.com/FreeCAD/FreeCAD/blob/76e74294894bbce46d006e149315c6274d206278/src/App/FeaturePython.h#L167)
-   [FreeCAD Forum Discussion: Scripted Objects Complete Method Reference](https://forum.freecadweb.org/viewtopic.php?f=22&t=49194)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > FeaturePython methods/it
