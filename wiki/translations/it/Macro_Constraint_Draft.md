# Macro Constraint Draft/it
{{Macro/it
|Name=Constraint Draft
|Icon=Macro_Constraint_Draft.png
|Translate=Constraint Draft
|Description=Crea una simulazione utilizando le [espressioni](Expressions/it.md) per legare gli oggetti (Questa macro funziona con FreeCAD versione 16).
|Author=Mario52
|Version=1.0
|Date=2017-04-19
|FCVersion=0.16
|Download=Il file esempio [http://forum.freecadweb.org/download/file.php?id=36559 Constraint_Draft00.FCStd]<br />[https://www.freecadweb.org/wiki/images/d/d8/Macro_Constraint_Draft.png Icona]
}}

## Descrizione

Semplice esempio di animazione dentro l\'ambiente Draft utilizzando le [espressioni](Expressions/it.md) per associare vari contorni e simulare o verificare la cinematica del complessivo.

![](images/Constraint_Draft00.gif ) *Animazione utilizzando il vincolo espressioni*

## Utilizzo

Caricare il file di esempio [Constraint\_Draft00.FCStd](http://forum.freecadweb.org/download/file.php?id=36559), e aprirlo con FreeCAD

## Codice

Selezionare la **Line005\_with\_Code** dentro la Vista combinata Seleziona Dati tab → Memo code → Code for rotation → ** ... ** (Questa macro funziona con FreeCAD versione 16 )

Selezionare il codice completo e copiarlo dentro la console Python

Se la console Python non è visibile fare : Menu → Visualizza → Pannelli → attiva Console Python

Un piccolo video di come copiare il codice

![Come copiare il codice](images/Constraint_Draft_Code01.gif )

ToolBar Icon ![](images/Macro_Constraint_Draft.png )

**Macro\_Constraint\_Draft.FCMacro**


{{MacroCode|code=

# Copy and pate this snippet in the FreeCAD console Python 
# mario52 19/04/2017

import FreeCADGui
import FreeCAD

#FreeCAD.Console.PrintMessage(str(FreeCAD.Version()) + "\n")
if int(FreeCAD.Version()[1]) == 16:    # Version de FreeCAD
    try:
        for i in range(0,360,5):
            App.getDocument("Constraint_Draft00").Circle.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(i,0,0), App.Vector(0,0,0))
            FreeCADGui.updateGui()
            FreeCAD.ActiveDocument.recompute()
    except Exception:
        FreeCAD.Console.PrintMessage("You must download the Constraint_Draft00.FCStd file for run this macro" + "\n")
        import webbrowser 
        webbrowser.open("http://forum.freecadweb.org/download/file.php?id=36559")

else:
    FreeCAD.Console.PrintError("This macro run with the FreeCAD.Version 16 " + "\n")

}}

## Rotazione con gli strumenti di FreeCAD 

![Ruotare con gli strumenti FreeCAD](images/Constraint_Draft01.gif )

## Link

Il forum [Sketch Feature to create linkage mechanism simulator](https://www.forum.freecadweb.org/viewtopic.php?f=22&t=21778&sid=28247565010ecdef0aa4f5c69e58f672)

---
[documentation index](../README.md) > Macro Constraint Draft/it
