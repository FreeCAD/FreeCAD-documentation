# Macro StraightenObject/it
{{Macro/it
|Name=StraightenObject
|Name/it=StraightenObject
|Icon=Macro_StraightenObject.png
|Description=Questa macro allinea un oggetto con il sistema di coordinate FC secondo gli elementi di riferimento (faccia/bordo)<br/>Questa macro è stata scritta principalmente per riallineare gli oggetti importati (es. STEP) con i principali piani/assi di FreeCAD.<br/>A utilizzare la macro, selezionare gli elementi di riferimento, eventualmente altri oggetti, quindi eseguire la macro.
Se vuoi allineare il tuo oggetto con un altro piano/asse, usa la macro e poi la funzione Trasforma di FreeCAD.
Vedere il capitolo "Dettagli" per la selezione di più oggetti.
|Author=OpenBrain
|Date=2019-06-10
|Version=0.8
|FCVersion= 0.17+
|SeeAlso=[Macro PlacementAbsolufy](Macro_PlacementAbsolufy/it.md) <img src="images/Macro_PlacementAbsolufy.png" width=24px>
|Download=[https://www.freecadweb.org/wiki/images/c/c9/Macro_StraightenObject.png ToolBar Icon]
}}

## Descrizione

### Contento

Questa macro è stata scritta principalmente per riallineare gli oggetti importati (es. STEP) con i principali piani/assi di FreeCAD.

## Usare

Funzionalmente, la macro utilizzerà uno o entrambi i seguenti elementi di riferimento per raddrizzare (ruotare e spostare) gli oggetti:

-   Faccia: la faccia selezionata verrà impostata in modo complanare con il piano XY, con la massa centrale impostata sull\'origine
-   Bordo (o 2 vertici): il bordo selezionato verrà allineato con l\'asse Y.

Per utilizzare la macro, selezionare gli elementi di riferimento, eventualmente altri oggetti, quindi eseguire la macro. Se vuoi allineare il tuo oggetto con un altro piano/asse, usa la macro e poi la funzione Trasforma di FreeCAD. Vedere il capitolo \"Dettagli\" per la selezione di più oggetti.

## Installazione

La macro è disponibile tramite [Addon Manager](Std_AddonMgr/it.md). Il codice viene fornito in questa pagina per comodità nel caso in cui il sistema dell\'utente non abbia git-python. Anche se dovrebbe essere aggiornato, l\'ultima versione è sempre disponibile all\'indirizzo [FreeCAD-macro repository](https://github.com/FreeCAD/FreeCAD-macros/blob/master/Utility/StraightenObject.FCMacro)

Per spiegazioni più dettagliate, consultare la pagina [Come installare una macro](How_to_install_macros/it.md).

## Dettaglio

Di seguito una tabella che presenta i diversi casi gestiti dalla macro:

  Primi oggetti oggetto selezionato                                                  Oggetto/i successivo/i selezionato/i selezionato/i   Comportamento macro
    
  Una faccia di riferimento                                                          Qualsiasi (facoltativo)                              Il primo oggetto viene ruotato/spostato in modo che la faccia di riferimento si trovi sul piano XY, con il centro della massa all\'origine. Altri oggetti selezionati subiscono lo stesso movimento del primo oggetto
  Un bordo di riferimento (o 2 vertici di riferimento)                               Qualsiasi (facoltativo)                              Il primo oggetto viene ruotato attorno al suo centro di massa in modo che il bordo di riferimento sia parallelo all\'asse Y (non viene applicato alcuno spostamento). Altri oggetti selezionati subiscono lo stesso movimento del primo oggetto
  Una faccia di riferimento + un bordo di riferimento (o 2 vertici di riferimento)   Qualsiasi (facoltativo)                              Il primo oggetto viene ruotato/spostato, quindi la faccia di riferimento si trova sul piano XY (il suo centro di massa si trova all\'origine) e il bordo di riferimento è parallelo all\'asse Y. Altri oggetti selezionati subiscono lo stesso movimento del primo oggetto
  2+ facce + qualsiasi                                                               Qualsiasi (facoltativo)                              La macro non riesce
  2+ bordi (o 3+ vertici) + qualsiasi                                                Qualsiasi (facoltativo)                              La macro non riesce
  Qualsiasi altra combinazione                                                       Qualsiasi (facoltativo)                              La macro non riesce

La macro eseguirà i seguenti controlli:

-   Se la faccia di riferimento è perpendicolare al bordo di riferimento, quest\'ultima verrà ignorata (notifica di avviso nella barra di stato)
-   Se la faccia di riferimento non è piatta, potrebbe verificarsi uno strano risultato (avviso di avviso nella barra di stato)

Quando si selezionano più oggetti, la macro proporrà 2 opzioni per applicare il raddrizzamento:

-   Parent: la macro tenterà di trovare un parent comune a tutti gli oggetti selezionati:
    -   Se non viene trovato nessuno, la macro ha esito negativo con una notifica di errore nella barra di stato
    -   Se ne vengono trovati uno o più, la trasformazione viene applicata su quella gerarchicamente inferiore
-   Multiplo: la trasformazione viene applicata su ogni oggetto selezionato separatamente

Da completare con un esempio di immagine

## Script

### Limitazione

-   Gli elementi di riferimento devono appartenere tutti al primo oggetto selezionato. Le voci di riferimento tra più oggetti non sono attualmente supportate
-   Gli oggetti raddrizzati devono essere in un sistema di coordinate corrispondente a quello globale. Se hai usato i contenitori Parte per individuare i tuoi oggetti, dovresti prima usare [Macro PlacementAbsolufy](Macro_PlacementAbsolufy/it.md) <img alt="" src=images/_Macro_PlacementAbsolufy.png  style="width:24px;"> sul tuo modello. Se questa condizione non viene soddisfatta, possono accadere cose strane.

ToolBar Icon ![](images/Macro_StraightenObject.png )

**Macro_StraightenObject.FCMacro**


{{MacroCode|code=
#!/usr/bin/python
#####################################
# Copyright (c) openBrain 2019
# Licensed under LGPL v2
#
# This FreeCAD macro will straighten an object vs. root origin based on a selected face or/and a selected edge (or 2 selected vertices)
# * If only a face is selected -> Center of mass of the face is set at origin, and normal to face at this same point is aligned with Z axis
# * If only an edge is selected (or 2 vertices) -> Object is rotated around Z axis (centered at the bounding box center) so that the virtual line between the 2 edge endpoints (or between the 2 vertices) is aligned with X axis
# * If both a face and an edge (or 2 vertices) are selected, both previous effects are applied (at the difference that the Z rotation in centered on the face center of mass)
#
# Selected reference items shall belong to the same object
#
# Main use of the macro is to re-align imported objects with the FreeCAD origin
#
# Version history :
# *0.8 : some typo improvement + commenting for official PR
# *0.75 : adding transaction for correct undo management
# *0.7 : multiple objects support (LIMITATION : reference items shall all belong to first object)(LIMITATION : unexpected results may happen if selected objects are in different coordinate systems)
# *0.6 : change way of reaching PartDesign Body, older has trouble with objects contained in a part
# *0.51 : change reference face alignment so it is considered a bottom face rather than a top one
# *0.5 : beta release
#
#####################################

__Name__ = 'StraigthenObject'
__Comment__ = 'Straighten an object by a face and/or an edge (or 2 vertices)'
__Author__ = 'openBrain'
__Version__ = '0.8'
__Date__ = '2019-06-10'
__License__ = 'LGPL v2'
__Web__ = 'https://www.freecadweb.org/wiki/Macro_StraightenObject'
__Wiki__ = 'https://www.freecadweb.org/wiki/Macro_StraightenObject'
__Icon__ = ''
__Help__ = 'Select face and/or edge to guide object straightening then run the macro'
__Status__ = 'Beta'
__Requires__ = 'FreeCAD >= 0.17'
__Communication__ = 'https://forum.freecadweb.org/viewtopic.php?f=22&t=35191'

__dbg__ = False #True for debugging

from PySide import QtGui

def cslM(msg):
    FreeCAD.Console.PrintMessage('\n')
    FreeCAD.Console.PrintMessage(msg)

def cslW(msg):
    FreeCAD.Console.PrintMessage('\n')
    FreeCAD.Console.PrintWarning(msg)

def cslE(msg):
    FreeCAD.Console.PrintMessage('\n')
    FreeCAD.Console.PrintError(msg)

def cslD(msg):
    if __dbg__:
        FreeCAD.Console.PrintMessage('\n')
        FreeCAD.Console.PrintMessage("Debug : " + str(msg))

_0Vec_ = FreeCAD.Vector(0, 0, 0)
_XVec_ = FreeCAD.Vector(1, 0, 0)
_YVec_ = FreeCAD.Vector(0, 1, 0)
_ZVec_ = FreeCAD.Vector(0, 0, 1)

if __dbg__:  ##Clear report view in debug mode
    FreeCADGui.getMainWindow().findChild(QtGui.QTextEdit, "Report view").clear()

cslM("Starting Straighten Object macro")
cslD("Getting selected objects to define targets")

selError = False #true if incorrect selection made
cancelOp = False #true if operation canceled by user

if len(FreeCADGui.Selection.getSelection()) > 1: #if several objet selected
    cslD("Multiple objects selected, asking user what to do")
    msgb = QtGui.QMessageBox() ##create a message box to ask for user choice & populate it
    msgb.setWindowTitle("Multiple objects selected")
    msgb.setText("""You have selected multiple objects
        This is experimental feature, unexpected results may happen if objects are in different coordinate systems
        Click 'Parent' to try to find a common parent and apply transformation to it
        Click 'Multiple' to apply transformation on all objects individually
        Click 'Cancel' to cancel operation""")
    msgb.setInformativeText("!!! Reference face and/or line shall belong to the 1st selected object !!!")
    msgb.setIcon(QtGui.QMessageBox.Question)
    pbut = msgb.addButton("Parent", QtGui.QMessageBox.AcceptRole) #button for 'Parent' mode
    mbut = msgb.addButton("Multiple", QtGui.QMessageBox.AcceptRole) #button for "Multiple' mode
    cbut = msgb.addButton("Cancel", QtGui.QMessageBox.RejectRole) #button to cancel operation
    msgb.exec_() #display message box
    if msgb.clickedButton() == pbut: #if 'Parent' mode selected
        cslD("Parent mode selected, will search for a common one")
        plist = FreeCADGui.Selection.getSelection()[0].InListRecursive #initialize the parent list
        for obj in FreeCADGui.Selection.getSelection(): #for each object in selection
            plist = list(set(plist).intersection(obj.InListRecursive)) #search common parent with previous objects
        cslD("Found common parent(s) : " + str([str(p.Label) for p in plist]) + " / if several, choose the first one")
        if len(plist) == 0: #if no common parent found
            selError = True
            cslE("No common parent found")
        else: #if common parent found
            target = [plist[0]] #take the lowest level one as target
            cslD("Selected parent as target : " + str(target[0].Label))
    elif msgb.clickedButton() == mbut: #if 'Multiple' mode selected
        cslD("Multiple mode selected, will apply on all objects")
        target = FreeCADGui.Selection.getSelection() #take all selection as target
    else: #if operation canceled
        cancelOp = True
        cslD("Operation canceled by user")
elif len(FreeCADGui.Selection.getSelection()) == 1: #if only one object selected
    target = FreeCADGui.Selection.getSelection() #take it as target
else: #no object selected
    selError = True
    cslE("No object selected")

if not(selError or cancelOp): #if a valid selection is available
    cslD("Target(s) after mode application : " + str(target[0].Label))
    cslD("Checking if PartDesign feature selected")
    for cnt, t in enumerate(target): #going through the targets
        try:
            while str(t.TypeId)[:10] == 'PartDesign' and str(t.TypeId) != 'PartDesign::Body': #while object is in a PartDesign and is not the Body
                t = t.getParentGeoFeatureGroup() #try its parent as new target
        except: #if a PartDesign object has no containing Body
            selError = True
            cslE("Found a PartDesign object not in a Body")
            break
        target[cnt] = t #update target

    target = list(set(target).intersection(target)) #remove duplicates to prevent applying 2 times transformation on same object
    cslD("Final target(s) : " + str([str(t.Label) for t in target]))

    cslD("Getting reference items")

    refFaceDef = False #true if a reference face is selected
    refPt1Def = False #true if one reference point is found selected
    refPt2Def = False #true if another reference point is found selected

    cslD("Subobjects : " +str(FreeCADGui.Selection.getSelectionEx()[0].SubElementNames))
    for selItem in FreeCADGui.Selection.getSelectionEx()[0].SubObjects: #going through selected items of first object
        if isinstance(selItem, Part.Face): #if it's a face
            if not refFaceDef: #if reference face not yet defined
                refFace = selItem #define it
                refFaceDef = True #and remember
            else:
                selError = True #too much faces selected
                cslE("Too much reference faces selected")
        elif isinstance(selItem, Part.Edge): #if it's an edge
            if not refPt1Def and not refPt2Def: #if reference points not yet defined
                refPt1 = selItem.Vertexes[0] #define 1st reference point as first edge point
                refPt1Def = True #and remember
                refPt2 = selItem.Vertexes[len(selItem.Vertexes)-1] #define 2nd reference point as last edge point
                refPt2Def = True #and remember
            else:
                selError = True #too much points selected
                cslE("Too much reference points selected (vertices or edges)")
        elif isinstance(selItem, Part.Vertex): #if it's a vertex
            if not refPt1Def: #if 1st reference point not yet defined
                refPt1 = selItem #define it
                refPt1Def = True #and remember
            elif not refPt2Def: #if 2nd reference point not yet defined
                refPt2 = selItem #define it
                refPt2Def = True #and remember
            else:
                selError = True #too much points selected
                cslE("Too much reference points selected (vertices or edges)")
        else:
            selError = True #incorrect type of item selected
            cslE("Incorrect type of item selected")

if cancelOp:
    cslM("Operation canceled by user ... exiting")
elif selError or (bool(refPt1Def) != bool(refPt2Def)) or (not (refPt1Def or refPt2Def or refFaceDef)): #if selection error or only one reference point defined or no reference face/point defined
    cslE("Selection error : see report view & documentation for more details ... Exiting")
else:
    FreeCAD.ActiveDocument.openTransaction("Straighten objects") #open new transaction for undo management
    cslD("Starting Transformation")
    obj = FreeCADGui.Selection.getSelection()[0] # take as reference the first object selected for transformation
    shiftVec = _0Vec_ #no shift move by defaut
    faceRot = FreeCAD.Rotation(_ZVec_, _ZVec_) #no reference rotation by default
    lineRot = FreeCAD.Rotation(_ZVec_, _ZVec_) #no reference line by default
    normVec = _ZVec_ #normal is the Z axis by default
    rotCenter = obj.Shape.BoundBox.Center #center of rotation at object bounding box center by default
    warning = False #True if a warning appears

    if refFaceDef: #if a reference face has been defined
        cslD("A reference face is available")
        faceCurv = refFace.curvatureAt(refFace.Surface.parameter(refFace.CenterOfMass)[0], refFace.Surface.parameter(refFace.CenterOfMass)[1]) #calculating face curvature at center of mass
        cslD("Curvature : " + str(faceCurv))
        if faceCurv != (0, 0): #if reference face is not flat at its center of mass
            warning = True
            cslW("Reference face is not flat at its center of mass, unexpected results may happen") #warn user about it
        rotCenter = refFace.CenterOfMass #changing center of rotation to center of mass of reference face
        shiftVec -= refFace.CenterOfMass #the reference face will be centered
        normVec = refFace.normalAt(refFace.Surface.parameter(refFace.CenterOfMass)[0], refFace.Surface.parameter(refFace.CenterOfMass)[1]) #getting normal vector at face center of mass
        faceRot = FreeCAD.Rotation(normVec, -_ZVec_) #calculate needed rotation to align the reference face with Z axis
        for t in target:
            t.Placement = FreeCAD.Placement(_0Vec_, faceRot, rotCenter).multiply(t.Placement) #rotate targets to align reference face normal with Z axis
        cslD("Targets rotated to match reference face normal with Z axis")
    if refPt1Def: #if reference points have been defined
        cslD("Reference points are available")
        lineVec = refPt2.Point - refPt1.Point #calculate vector (reference line) defined by reference points
        lineVecMod = faceRot.multVec(lineVec) #reference line has maybe been modified by previous object rotation
        lineNorm = lineVecMod.projectToPlane(_0Vec_, _ZVec_) #calculate line projection on XY plane
        cslD("Normality : " + str(lineNorm))
        if lineNorm == _0Vec_: #if reference line is perpendicular to rotating plane
            warning = True
            cslW("Line reference is aligned with normal, line alignment will be ignored") #warn user about it
        else:
            lineRot = FreeCAD.Rotation(lineNorm, _XVec_) #calculate needed rotation to align with X axis
            for t in target:
                t.Placement = FreeCAD.Placement(_0Vec_, lineRot, rotCenter).multiply(t.Placement) #rotate targets to align reference line with X axis
            cslD("Targets rotated to match reference line with X axis")

    for t in target:
        t.Placement.move(shiftVec) #finally shift targets if needed
    cslD("Targets shift")
    FreeCAD.ActiveDocument.commitTransaction() #commit transaction
    if warning:
        cslW("Macro terminated with warning(s), see report view & documentation for more details")
    else :
        cslM("Macro terminated correctly")
      
}}

## Forum discussioni 

Per qualsiasi feedback (bug, richiesta di funzionalità, commenti, \...), utilizzare questo thread del forum : [(Macro) Straighten objects](https://forum.freecadweb.org/viewtopic.php?f=22&t=35191)



---
⏵ [documentation index](../README.md) > Macro StraightenObject/it
