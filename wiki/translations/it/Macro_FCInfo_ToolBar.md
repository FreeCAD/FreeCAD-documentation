# Macro FCInfo ToolBar/it
{{Macro
|Name=Macro FCCInfo ToolBar
|Icon=FCInfoToolBar.png
|Description=Fornisce informazioni sulla forma selezionata e può visualizzare una conversione di raggio, diametro, lunghezza, area, volume ... in diverse unità (metriche e imperiali) in una barra degli strumenti in real tempo. Le informazioni da visualizzare sono parametrizzabili nel parametro di FreeCAD.
|Author=Mario52
|Version=00.04
|Date=2023/06/28
|FCVersion=0.18 and more
|Download=[https://wiki.freecadweb.org/images/9/9d/FCInfoToolBar.png The toolBar icon]
|SeeAlso=[Arch Survey](Arch_Survey.md) <img src="images/Arch_Survey.svg" width=32px></br>[Macro FCInfo](Macro_FCInfo.md) <img src="images/FCInfo.png" width=32px></br>[Macro FCInfoGlass](Macro_FCInfoGlass.md) <img src="images/Macro_FCInfoGlass.png" width=32px>
}}



## Descrizione

Fornisce informazioni sulla forma selezionata e può visualizzare una conversione di raggio, diametro, lunghezza, area, volume \... in diverse unità (metriche e imperiali) in una barra degli strumenti. Le informazioni da visualizzare sono parametrizzabili nel parametro di FreeCAD.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/e382adbe41747788ad15a18eb206a872/raw/40ca52f49edb1e29c70f0eaef42934aec19ca594/FCInfo_ToolBar.FCMacro}}

![FCInfo_ToolBar](images/Macro_FCInfo_ToolBar_00.png ) 
*FCInfo_ToolBar*



## Utilizzo

Dopo aver eseguito la macro, andare a Menu → Strumenti → Modifica parametri \... :BaseApp/Preferences/Macros/FCMmacros/FCInfo_ToolBar

e aggiungere le informazioni da visualizzare.

Le informazioni complete vengono visualizzate nella finestra ToolTip, l\'opzione selezionata è visibile se viene visualizzato di uno \"\*\".

Usate il pulsante reset dopo aver cambiato un\'opzione nella finestra dei parametri.

L\'unità delle dimensione può essere selezionata: km, hm, dam, m, dm, cm, mm, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.

![FCInfo_ToolBar the info toolTip](images/Macro_FCInfo_ToolBar_01.png ) 
*FCInfo_ToolBar the info toolTip*



## Opzioni

Le opzioni si trovano nel parametro di FreeCAD:

*Menu → Strumenti → Modifica parametri \... :BaseApp/Preferences/Macros/FCMmacros/FCInfo_ToolBar*

-   ***switch_User_ToolbarIconSize***
    -   se = `False`: l\'icona della barra degli strumenti rispetta il valore di FreeCAD per la dimensione dell\'icona
    -   se = `True`: l\'icona prende i valori della variabile **seT_User_sizeIconX** e **seT_User_sizeIconY**

-   ***seT_User_sizeIconX***
    -   imposta il valore X dell\'icona

-   ***seT_User_sizeIconY***
    -   imposta il valore Y dell\'icona

-   ***seT_User_setFixed_Tool_Bar_Width***
    -   imposta la lungunese del ToolBar

-   ***seT_User_setFixed_Tool_Bar_Height***
    -   imposta la altessa del ToolBar

-   ***switch_User_Work_With_Preselection***
    -   Lavora con la preselezione, i dati sono calcolate in tempo reale

-   ***seT_User_StyleSheetColorToolBar***
    -   imposta il colore della barra degli strumenti in formato HTML esempio: **#F8E6E0**\'.
    -   se il valore è **0**\' la barra degli strumenti prende il colore del sistema

-   ***seT_User_DecimalValue***
    -   dare il numero di decimali del numero (Default **2**)

-   ***seT_User_TextHeigthValue***
    -   dare l\'altezza del testo della barra degli strumenti

-   ***switch_User_Display_objectName***
    -   visualizza il Nome ()

-   ***switch_User_Display_SubElementName***
    -   visualizza il nome del sotto-elemento ()

-   ***switch_User_Display_ShapeType***
    -   visualizzare il Shape type (TyS:)

-   ***switch_User_Display_TypeId***
    -   visualizzare il TypeId (TyI:)

-   ***switch_User_Display_RadiusObject***
    -   visualizzare il raggio e il diametro (r:) \[D:\]

-   ***switch_User_Display_LengthObject***
    -   Visualizza la lunghezza del bordo selezionato o il perimetro della faccia selezionata
        -   (L:) visualizza la lunghezza del filo, linea, bordo selezionato
        -   (P:) visualizza il perimetro della fascia selezionata

-   ***switch_User_Display_SommeAllEdgesObject***
    -   visualizza la lunghezza totale dei bordi (edges) di l\'obietto selezionato (Se:)

-   ***switch_User_Display_NumberFacesMesh***
    -   visualizza il numero di facce dell\'oggetto Mesh (Nf:)

-   ***switch_User_Display_NumberPointsMeshPoints***
    -   visualizza il numero di punti dell\'oggetto Mesh (Np:)

-   ***switch_User_Display_NumberEdgesMesh***
    -   visualizza il numero di bordi dell\'oggetto Mesh (Ne:)

-   ***switch_User_Display_AreaObject***
    -   visualizza la superficie dell\'oggetto (A:)

-   ***switch_User_Display_AreaSubObject***
    -   visualizza la superficie della faccia selezionata (Af:)

-   ***switch_User_Display_VolumeObject***
    -   visualizza il volume dell\'oggetto (V:)

-   ***switch_User_Display_BsplineObject***
    -   visualizza il numero di nodi della Bspline selezionata
        -   (BSpline) visualizza i nodi del BSpline
        -   (BSrA) BSPline raggio approximativo del primo raggio del BSpline
        -   (BSS) BSPline Points Shape numero di punti del BSPline (caso Shape)
        -   (BSc) BSPline Points Sub Obbietto numero di punti del sub obbietto selezionato (case Edge)

-   ***switch_User_Display_CentreObject***
    -   visualizza il centro del cerchio (se viene rilevato un cerchio) o dell\'oggetto selezionato (Ce:)

-   ***switch_User_Display_CentreBoundBoxObject***
    -   visualizza il centro del boundingBox dell\'oggetto (BBCe:)

-   ***switch_User_Display_Position***
    -   visualizza le coordinate del punto puntato dal mouse (Pos:)

-   ***switch_User_NotInfoOnBeginning***
    -   se è `False` l\'informazione (questa informazione) viene visualizzata
    -   se è `True` l\'informazione non viene visualizzata

-   ***seT_User_UnitSymbolSquare***
    -   dare il simbolo quadrato (Predefinito **2**)

-   ***seT_User_UnitSymbolCube***
    -   datare il simbolo del cubo (Predefinito **3**)

-   ***seT_User_UnitSymbolMicro***
    -   dare il simbolo micro (Predefinito **u**)



## Per l\'esecuzione automatica 



#### in linea di comando 

Nella tua scorciatoia *verifica il tuo percorso giusto*.

\"Percorso_completo_di_FreeCAD\" \"Percorso_completo_della_macro.FCMacro\"

esempio:


```python
"C:/FreeCAD_0.20.26858_Win-LPv12.5.4_vc17.x-x86-64/bin/FreeCAD.exe" "C:/Users/User/AppData/Roaming/FreeCAD/Macro/FCInfo_ToolBar.FCMacro"
```



#### nella directory Mod 

1.  Dopo aver installato la macro con [Addon Manager](Std_AddonMgr/it.md)
2.  Creare la directory *FCInfo_ToolBar*.
3.  Copiare la macro FCInfo_ToolBar.FCMacro (copiare non spostare) nella directory *FCInfo_ToolBar* e rinominarla in FCInfo_ToolBar.py
4.  Creare un file chiamato InitGui.py
5.  Incolla il codice in InitGui.py:


```python
#### FC Version: 0.1 #16/02/2022
#### Mario52
#### FCInfo_ToolBar : mini FCInfo ####
#
import importlib
from importlib import reload
import FreeCAD, FreeCADGui
App = FreeCAD
Gui = FreeCADGui


switch_User_NotRunAuto = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/FCInfo_ToolBar").GetBool("switch_User_NotRunAuto")
## switch_User_NotRunAuto 0 (False) = run the macro in begin
## switch_User_NotRunAuto 1 (True)  = not run automatic the macro


if switch_User_NotRunAuto == False:
    import FCInfo_ToolBar
    #reload(FCInfo_ToolBar)
    FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macros/FCMmacros/FCInfo_ToolBar").SetBool("switch_User_NotRunAuto", False)
    #FreeCAD.Console.PrintMessage("InitGui Ok FCInfo_ToolBar" + "\n")
```

1.  salvare il file
2.  eseguire FreeCAD
3.  se la macro non viene eseguita (normale) eseguire la macro FCInfo_ToolBar.FCMacro come una normale macro
4.  al prossimo avvio di FreeCAD la macro deve partire automaticamente

enjoy



## Collegamento

Discussioni sul forum [Feature request: coordinates display](https://forum.freecadweb.org/viewtopic.php?f=8&t=66294)



## Versione

versione 00.04 28/06/2023 : correzione fogli di stile e:


```python
                        sommeEdgesSTR = str(sommeEdges)
```

sostituito da: 
```python
                        sommeEdgesSTR = str(round(sommeEdges * uniteM, seT_User_DecimalValue)) + " " + uniteMs
```

version: (00.02 +) 00.03 2022/03/22 : add somme all edges

version: 00.02 2022/03/14 : add calcul in real time (with preselection), dimension of toolBar, add info mesh and points

version: 00.01 2022/02/16 :



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCInfo ToolBar/it
