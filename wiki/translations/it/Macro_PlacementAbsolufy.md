# Macro PlacementAbsolufy/it




{{Macro/it
|Name=PlacementAbsolufy
|Name/it=PlacementAbsolufy
|Icon=Macro_PlacementAbsolufy.png
|Description=Questa macro ripristina la posizione di tutti i contenitori di parti per documentare l'origine mantenendo le posizioni assolute dell'oggetto.<br/>Questa macro è stata scritta principalmente per eludere l'implementazione incompleta del contenitore di parti che può portare a uno spostamento di posizione assoluto, principalmente durante l'esportazione di parti. Ciò è dovuto al fatto che i contenitori di parti creano un sistema di coordinate locale che può essere spostato da quello globale. Questo riferimento locale viene quindi utilizzato dagli oggetti successivi ma non è gestito correttamente da diverse funzioni (ad es. Esportazione).
|Author=OpenBrain
|Date=2019-06-10
|Version=0.2
|FCVersion= 0.17+
|SeeAlso=[Macro StraightenObject](Macro_StraightenObject/it.md) <img src="images/Macro_StraightenObject.png" width=24px>
|Download=[https://www.freecadweb.org/wiki/images/9/92/Macro_PlacementAbsolufy.png ToolBar Icon]
}}

## Descrizione

### Contento

Questa macro è stata scritta principalmente per eludere l\'implementazione incompleta del contenitore delle parti che può portare a uno spostamento assoluto della posizione, principalmente durante l\'esportazione delle parti. Ciò è dovuto al fatto che i contenitori di parti creano un sistema di coordinate locale che può essere spostato da quello globale. Questo riferimento locale viene quindi utilizzato dagli oggetti successivi ma non è gestito correttamente da diverse funzioni (ad es. Esportazione).

## Usare

Funzionalmente, la macro reimposterà il posizionamento dei contenitori Parte su origine globale preservando la posizione assoluta degli oggetti. Si noti che la macro PlacementAbsolufy si applica all\'intero documento attivo.

Per utilizzare la macro, basta eseguirla quando il documento su cui deve essere applicato è aperto.

## Installazione

La macro è disponibile tramite [Addon Manager](Std_AddonMgr/fr.md). Il codice viene fornito in questa pagina per comodità nel caso in cui il sistema dell\'utente non abbia git-python. Anche se dovrebbe essere aggiornato, l\'ultima versione è sempre disponibile all\'indirizzo [FreeCAD-macro repository](https://github.com/FreeCAD/FreeCAD-macros/blob/master/Utility/PlacementAbsolufy.FCMacro)

Per spiegazioni più dettagliate, vedere la pagina [Come installare le macro](How_to_install_macros/it.md).

## Script

ToolBar Icon ![](images/Macro_PlacementAbsolufy.png )

**Macro\_PlacementAbsolufy.FCMacro**


{{MacroCode|code=
#!/usr/bin/python
#####################################
# Copyright (c) openBrain 2019
# Licensed under LGPL v2
#
# This macro will reset position of all part containers to document origin while keeping the absolute object positions
#
# Version history :
# *0.2 : some typo improvement + commenting for official PR
# *0.1 : alpha release, almost no test performed
#
#####################################

__Name__ = 'PlacementAbsolufy'
__Comment__ = 'Reset part containers to global origin while keeping object positions'
__Author__ = 'openBrain'
__Version__ = '0.2'
__Date__ = '2019-06-10'
__License__ = 'LGPL v2'
__Web__ = 'https://www.freecadweb.org/wiki/Macro_PlacementAbsolufy'
__Wiki__ = 'https://www.freecadweb.org/wiki/Macro_PlacementAbsolufy'
__Icon__ = ''
__Help__ = 'Run the macro with model active in the GUI'
__Status__ = 'Alpha'
__Requires__ = 'FreeCAD >= 0.17'
__Communication__ = 'https://forum.freecadweb.org/viewtopic.php?f=3&t=36869'
__Files__ = ''

currState = {} #initialize a dictionary to store current object placements

for obj in App.ActiveDocument.Objects: #going through active document objects
    if "Placement" in obj.PropertiesList: #if object has a Placement property
        currState[obj] = obj.getGlobalPlacement() #store the object pointer with its global placement

App.ActiveDocument.openTransaction("Absolufy") #open a transaction for undo management

for obj, plac in currState.items(): #going through all moveable objects
    if obj.isDerivedFrom("App::Part"): #if object is a part container
        obj.Placement = App.Placement(App.Vector(0,0,0),App.Rotation(0,0,0)) #reset its placement to global document origin
    elif obj.TypeId[:5] == "App::": #if object is another App type (typically an origin axis or plane)
        None #do nothing
    else: #for all other objects
        obj.Placement = plac #replace them at their global (absolute) placement

App.ActiveDocument.commitTransaction() #commit transaction
}}

## Limitativo

-   Tratta l\'intero documento aperto

## Forum discussione 

Per qualsiasi feedback (bug, richiesta di funzionalità, commenti, \...), utilizzare questo thread del forum : [Preserving global position of Parts during export](https://forum.freecadweb.org/viewtopic.php?f=3&t=36869)
