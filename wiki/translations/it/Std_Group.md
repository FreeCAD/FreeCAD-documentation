---
- GuiCommand:
   Name: Std_Group   Name/it: Crea Gruppo
   MenuLocation: Vista ad albero -> Cliccare col destro sul nome del documento -> Crea gruppo
   |Workbenches: Tutti
   Shortcut: 
   Version: 
   SeeAlso: Std_Part/it, Draft_SelectGroup/it, Draft_AddToGroup/it
---

# Std Group/it



## Descrizione

Un [Gruppo](Std_Group/it.md) (chiamato internamente [App DocumentObjectGroup](App_DocumentObjectGroup/it.md)) è un contenitore per scopi generici che consente di raggruppare diversi tipi di oggetti nella [Vista ad albero](Tree_view/it.md), indipendentemente dal tipo di dati. È usato come una semplice cartella per classificare e organizzare gli oggetti nel modello, al fine di mantenere una struttura logica. I gruppi possono essere nidificati all\'interno di altri gruppi.

Lo strumento Gruppo non è definito da un particolare ambiente di lavoro, ma dal sistema base; di conseguenza lo si ritrova nella **barra degli strumenti struttura**, che è disponibile in tutti gli [ambienti di lavoro](Workbenches/it.md).

Per raggruppare gli oggetti 3D come una singola unità, con l\'intenzione di creare degli assiemi, utilizzare [Parte](Std_Part/it.md).

![](images/Std_Group_example.png )



*Vari elementi all'interno di Gruppo nella vista ad albero.*



## Utilizzo

1.  Effettuare una delle seguenti operazioni:
    -   Fare clic con il pulsante destro del mouse sul nome del documento nella [Vista ad albero](Tree_view.md) e nel menu contestuale scegliere **Crea gruppo...**.
    -   Premere il pulsante **<img src="images/Std_Group.svg" width=16px> [Crea gruppo](Std_Group.md)**.
2.  Viene creato un gruppo vuoto.
3.  Per aggiungere oggetti al gruppo, selezionarli nella [Vista ad albero](Tree_view.md) e trascinarli e rilasciarli nel gruppo.
4.  Per rimuovere gli oggetti dal gruppo, trascinarli fuori dal gruppo e sull\'etichetta del documento nella parte superiore della [Vista ad albero](Tree_view.md).
5.  Gli oggetti possono anche essere aggiunti e rimossi modificando la proprietà **Group** del gruppo.



## Proprietà

Il [Gruppo](Std_Group/it.md) è internamente chiamato [App DocumentObjectGroup](App_DocumentObjectGroup/it.md) (`App::DocumentObjectGroup` class), è derivato dall\'oggetto base [App DocumentObject](App_DocumentObject/it.md) (`App::DocumentObject` class), pertanto eredita tutte le sue proprietà.

Il Gruppo ha le stesse proprietà di [App FeaturePython](App_FeaturePython/it#Proprietà.md), che è l\'istanza più semplice di un [App DocumentObject](App_DocumentObject/it.md). Ha anche le seguenti proprietà aggiuntive nell\'[editor di proprietà](Property_editor/it.md). Le proprietà nascoste possono essere visualizzate utilizzando il comando **Mostra tutto** nel menu contestuale dell\'[editor di proprietà](Property_editor/it.md).



### Dati


{{TitleProperty|Base}}

-    **Group|LinkList**: un elenco di oggetti referenziati. Per impostazione predefinita, è vuoto {{value|[]}}.

-    **_ Group Touched|Bool|Hidden**: se il gruppo è touched o meno.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](Scripted_objects/it.md).

Vedi [Funzione Part](Part_Feature/it.md) per le informazioni generali su come aggiungere oggetti al documento.

Un Gruppo ([App DocumentObjectGroup](App_DocumentObjectGroup.md)) è creato con il metodo del documento `addObject()`. Una volta che un Gruppo esiste, altri oggetti possono essere aggiunti ad esso con i metodi `addObject()` o `addObjects()`.


```python
import FreeCAD as App

doc = App.newDocument()
group = App.ActiveDocument.addObject("App::DocumentObjectGroup", "Group")

obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("Part::Box", "Box")

group.addObjects([obj1, obj2])
App.ActiveDocument.recompute()
```

Questo `App::DocumentObjectGroup` di base non ha un oggetto Proxy, quindi non può essere pienamente utilizzato per la sotto-classe.

Per la sottoclasse [Python](Python/it.md), è necessario creare un oggetto `App::DocumentObjectGroupPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "Name")
obj.Label = "Custom label"
```

Per esempio, un [Analisi FEM](FEM_Analysis/it.md) è un oggetto `App::DocumentObjectGroupPython` con un\'icona personalizzata e proprietà aggiuntive.



## Link

-   [Esempio di utilizzo in Arch Tutorial](Arch_tutorial/it#Organizzare_il_modello.md)
-   [Struttura del documento](Document_structure/it.md)
-   [Esempio di organizzazione del modello](http://www.freecadweb.org/wiki/index.php?title=Arch_tutorial#Organizing_your_model)





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std Group/it
