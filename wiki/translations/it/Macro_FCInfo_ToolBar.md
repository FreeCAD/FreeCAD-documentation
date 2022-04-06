# Macro FCInfo ToolBar/it
{{Macro
|Name=Macro FCCInfo ToolBar
|Icon=FCInfoToolBar.png
|Description=Fornisce informazioni sulla forma selezionata e può visualizzare una conversione di raggio, diametro, lunghezza, area, volume ... in diverse unità (metriche e imperiali) in una barra degli strumenti in real tempo. Le informazioni da visualizzare sono parametrizzabili nel parametro di FreeCAD.
|Author=Mario52
|Version=00.03
|Date=2022/03/29
|FCVersion=0.18 and more
|Download= [https://wiki.freecadweb.org/images/9/9d/FCInfoToolBar.png The toolBar icon]
|SeeAlso = [Arch Survey](Arch_Survey/it.md) <img src="images/Arch_Survey.svg" width=32px></br>[Macro FCInfo](Macro_FCInfo/it.md) <img src="images/FCInfo.png" width=32px></br>[Macro FCInfoGlass](Macro_FCInfoGlass/it.md) <img src="images/Macro_FCInfoGlass.png" width=32px>
}}

## Descrizione

Fornisce informazioni sulla forma selezionata e può visualizzare una conversione di raggio, diametro, lunghezza, area, volume \... in diverse unità (metriche e imperiali) in una barra degli strumenti. Le informazioni da visualizzare sono parametrizzabili nel parametro di FreeCAD.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/e382adbe41747788ad15a18eb206a872/raw/45da6835214d570588244705d2c0f37f97320874/FCInfo_ToolBar.FCMacro}}

![FCInfo\_ToolBar](images/Macro_FCInfo_ToolBar_00.png ) 
*FCInfo_ToolBar*

## Usare

Dopo aver eseguito la macro, andare a Menu → Strumenti → Modifica parametri \... :BaseApp/Preferences/Macros/FCMmacros/FCInfo\_ToolBar

e aggiungere le informazioni da visualizzare.

Le informazioni complete vengono visualizzate nella finestra ToolTip, l\'opzione selezionata è visibile se viene visualizzato di uno \"\*\".

Usate il pulsante reset dopo aver cambiato un\'opzione nella finestra dei parametri.

L\'unità delle dimensione può essere selezionata: km, hm, dam, m, dm, cm, mm, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.

![FCInfo\_ToolBar the info toolTip](images/Macro_FCInfo_ToolBar_01.png ) 
*FCInfo_ToolBar the info toolTip*

## Opzioni

Le opzioni si trovano nel parametro di FreeCAD

*Menu → Strumenti → Modifica parametri \... :BaseApp/Preferences/Macros/FCMmacros/FCInfo\_ToolBar*

-   ***switch\_User\_ToolbarIconSize***
    -   se = `False`: l\'icona della barra degli strumenti rispetta il valore di FreeCAD per la dimensione dell\'icona
    -   se = `True`: l\'icona prende i valori della variabile **seT\_User\_sizeIconX** e **seT\_User\_sizeIconY**

-   ***seT\_User\_sizeIconX***
    -   imposta il valore X dell\'icona

-   ***seT\_User\_sizeIconY***
    -   imposta il valore Y dell\'icona

-   ***seT\_User\_setFixed\_Tool\_Bar\_Width***
    -   imposta la lungunese del ToolBar

-   ***seT\_User\_setFixed\_Tool\_Bar\_Height***
    -   imposta la altessa del ToolBar

-   ***switch\_User\_Work\_With\_Preselection***
    -   Lavora con la preselezione, i dati sono calcolate in tempo reale

-   ***seT\_User\_StyleSheetColorToolBar***
    -   imposta il colore della barra degli strumenti in formato HTML esempio: **\#F8E6E0**\'.
    -   se il valore è **0**\' la barra degli strumenti prende il colore del sistema

-   ***seT\_User\_DecimalValue***
    -   dare il numero di decimali del numero (Default **2**)

-   ***seT\_User\_TextHeigthValue***
    -   dare l\'altezza del testo della barra degli strumenti

-   ***switch\_User\_Display\_objectName***
    -   visualizza il Nome ()

-   ***switch\_User\_Display\_SubElementName***
    -   visualizza il nome del sotto-elemento ()

-   ***switch\_User\_Display\_ShapeType***
    -   visualizzare il Shape type (TyS:)

-   ***switch\_User\_Display\_TypeId***
    -   visualizzare il TypeId (TyI:)

-   ***switch\_User\_Display\_RadiusObject***
    -   visualizzare il raggio e il diametro (r:) \[D:\]

-   ***switch\_User\_Display\_LengthObject***
    -   Visualizza la lunghezza del bordo selezionato o il perimetro della faccia selezionata
        -   (L:) visualizza la lunghezza del filo, linea, bordo selezionato
        -   (P:) visualizza il perimetro della fascia selezionata

-   ***switch\_User\_Display\_SommeAllEdgesObject***
    -   visualizza la lunghezza totale dei bordi (edges) di l\'obietto selezionato (Se:)

-   ***switch\_User\_Display\_NumberFacesMesh***
    -   visualizza il numero di facce dell\'oggetto Mesh (Nf:)

-   ***switch\_User\_Display\_NumberPointsMeshPoints***
    -   visualizza il numero di punti dell\'oggetto Mesh (Np:)

-   ***switch\_User\_Display\_NumberEdgesMesh***
    -   visualizza il numero di bordi dell\'oggetto Mesh (Ne:)

-   ***switch\_User\_Display\_AreaObject***
    -   visualizza la superficie dell\'oggetto (A:)

-   ***switch\_User\_Display\_AreaSubObject***
    -   visualizza la superficie della faccia selezionata (Af:)

-   ***switch\_User\_Display\_VolumeObject***
    -   visualizza il volume dell\'oggetto (V:)

-   ***switch\_User\_Display\_BsplineObject***
    -   visualizza il numero di nodi della Bspline selezionata
        -   (BSpline) visualizza i nodi del BSpline
        -   (BSrA) BSPline raggio approximativo del primo raggio del BSpline
        -   (BSS) BSPline Points Shape numero di punti del BSPline (caso Shape)
        -   (BSc) BSPline Points Sub Obbietto numero di punti del sub obbietto selezionato (case Edge)

-   ***switch\_User\_Display\_CentreObject***
    -   visualizza il centro del cerchio (se viene rilevato un cerchio) o dell\'oggetto selezionato (Ce:)

-   ***switch\_User\_Display\_CentreBoundBoxObject***
    -   visualizza il centro del boundingBox dell\'oggetto (BBCe:)

-   ***switch\_User\_Display\_Position***
    -   visualizza le coordinate del punto puntato dal mouse (Pos:)

-   ***switch\_User\_NotInfoOnBeginning***
    -   se è `False` l\'informazione (questa informazione) viene visualizzata
    -   se è `True` l\'informazione non viene visualizzata

-   ***seT\_User\_UnitSymbolSquare***
    -   dare il simbolo quadrato (Predefinito **2**)

-   ***seT\_User\_UnitSymbolCube***
    -   datare il simbolo del cubo (Predefinito **3**)

-   ***seT\_User\_UnitSymbolMicro***
    -   dare il simbolo micro (Predefinito **u**)

## Per l\'esecuzione automatica 

#### in linea di comando 

Nella tua scorciatoia *verifica il tuo percorso giusto*.

\"Percorso\_completo\_di\_FreeCAD\" \"Percorso\_completo\_della\_macro.FCMacro\"

esempio:


```python
"C:/FreeCAD_0.20.26858_Win-LPv12.5.4_vc17.x-x86-64/bin/FreeCAD.exe" "C:/Users/User/AppData/Roaming/FreeCAD/Macro/FCInfo_ToolBar.FCMacro"
```

#### nella directory Mod 

1.  Dopo aver installato la macro con AddonManager
2.  Creare la directory *FCInfo\_ToolBar*.
3.  Copiare la macro FCInfo\_ToolBar.FCMacro (copiare non spostare) nella directory *FCInfo\_ToolBar* e rinominarla in FCInfo\_ToolBar.py
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
3.  se la macro non viene eseguita (normale) eseguire la macro FCInfo\_ToolBar.FCMacro come una normale macro
4.  al prossimo avvio di FreeCAD la macro deve partire automaticamente

enjoy

## Collegamento

Discussioni sul forum [Feature request: coordinates display](https://forum.freecadweb.org/viewtopic.php?f=8&t=66294)

## Versione

version: (00.02 +) 00.03 2022/03/22 : add somme all edges

version: 00.02 2022/03/14 : add calcul in real time (with preselection), dimension of toolBar, add info mesh and points

version: 00.01 2022/02/16 :



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FCInfo ToolBar/it
