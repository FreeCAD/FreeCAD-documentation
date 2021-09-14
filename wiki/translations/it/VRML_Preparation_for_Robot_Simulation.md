# VRML Preparation for Robot Simulation/it




<div class="mw-translate-fuzzy">


{{TutorialInfo/it
|Topic=Robot
|Level=Intermedio
|Time=
|Author=
|FCVersion=
|Files=
}}


</div>


{{VeryImportantMessage|The FreeCAD Robot Workbench is unmaintained. Please mention on the FreeCAD forum if you have an interest in maintaining this 
workbench.}}

## Overview


<div class="mw-translate-fuzzy">

Questo tutorial spiega come utilizzare FreeCAD e l\'ambiente **Simulazione Robot** per simulare i movimenti dei robot a 6 assi.
Il tutorial si concentra sulla creazione del file **VRML** utilizzato per la visualizzazione.
La base del file VRML è un modello di FreeCAD.
La versione di FreeCAD utilizzata è la 0.11.4252ppa1 in Ubuntu 32 bit.


</div>

## Aprire un file o crearne uno con FreeCAD 

Il tutorial si basa su un **file STEP** di un robot Stäubli TX40 (TX40-HB.stp).
È possibile scaricare il file file TX40-HB.stp da [Stäubli](https://secure.staubli.com/Intranet_Applications/Robotics/Group/RobDoc.nsf/ea05b3f4b301f597c1256d5f005665e8/bc3707ec036c9f6bc12576c700327958/$FILE/page.html).
Anche se non ho ancora avuto tempo di controllare, il metodo dovrebbe valere anche per un modello realizzato completamente in FreeCAD.
Dopo aver aperto il file, si dovrebbe ottenere questo:

<img alt="" src=images/staeubli_step_import.png  style="width:1024px;">


<div class="mw-translate-fuzzy">

Notare che, nell\'importazione, il robot è composto di 8 forme, direttamente sulla radice dell\'albero del documento.
La struttura del file VRML esportato può cambiare se sono utilizzati i gruppi. Le forme sono ordinate a partire dalla base allo strumento.
L\'ultima forma contiene gli assi di rotazione di tutti gli assi del robot.
I nomi delle forme sono attribuiti in modo correlativo da FreeCAD, (dato che per ora (marzo 2011) FreeCAD non importa i nomi inclusi nei file STEP):


</div>

  nome FreeCAD   nome STEP
  -------------- ------------------------------
  TX40\_HB       HORIZONTAL BASE CABLE OUTLET
  TX40\_HB001    SHOULDER
  TX40\_HB002    ARM
  TX40\_HB003    ELBOW
  TX40\_HB004    FOREARM
  TX40\_HB005    WRIST
  TX40\_HB006    TOOL FLANGE
  TX40\_HB007    ?


<div class="mw-translate-fuzzy">

In questa importazione, cambiare la modalità di visualizzazione, "Display Mode", di ogni forma, ad eccezione di TX40\_HB007, da \"Flat Lines\" a \"Shaded\" per dare un buon aspetto all\'esportazione VRML. Ho anche cambiato i colori in \[245, 196, 0\] e \[204, 204, 204\] per farli corrispondere meglio al giallo di Stäubli.
Nascondere TX40\_HB007 perché contiene gli assi di tutti i giunti e non può essere smontato.


</div>

## Misure delle caratteristiche geometriche 

Per costruire la tabella di [Denavit-Hartenberg](http://it.wikipedia.org/wiki/Denavit-Hartenberg) (vedere [6-Axis\_Robot](Robot_6-Axis/it.md) ) e per preparare il file [VRML](http://it.wikipedia.org/wiki/VRML), è necessario ottenere le caratteristiche del Robot.
Per ora, lo strumento di misurazione di FreeCAD non è ancora pronto, è possibile utilizzare gli assi inclusi in TX40\_HB007 (le coordinate sono indicate in basso a sinistra quando si punta un oggetto con il mouse), oppure si deve utilizzare la console Python per ottenere delle informazioni sulla geometria.
Notare che la **Tabella DH** è necessaria solo quando si ha bisogno di usare la cinematica inversa, ad esempio, per ottenere le coordinate cartesiane o guidare il robot con coordinate cartesiane.
La **Tabella DH** per questo robot è la seguente **(mm, gradi e gradi/s)** :

  i   d     θ         r     α     θmin   θmax    Axis velocity
  --- ----- --------- ----- ----- ------ ------- ---------------
  1   320   q1        0     -90   -180   180     555
  2   35    q2 - 90   225   0     -125   125     475
  3   0     q3 + 90   0     90    -138   138     585
  4   225   q4        0     -90   -270   270     1035
  5   0     q5        0     90    -120   133.5   1135
  6   65    q6        0     0     -270   270     1575

Il file csv è quindi:

 a  , alpha, d  , theta, rotDir, maxAngle, minAngle, AxisVelocity
0  ,   -90, 320,     0,      1,      180,     -180, 555
225,     0,  35,   -90,      1,      125,     -125, 475
0  ,    90,   0,    90,      1,      138,     -138, 585
0  ,   -90, 225,     0,      1,      270,     -270, 1035
0  ,    90,   0,     0,      1,    133.5,     -120, 1135
0  ,     0,  65,     0,      1,      270,     -270, 1575


<div class="mw-translate-fuzzy">

## Esportare in VRML 

Esportare il documento in un file VRML. La struttura del file VRML è la seguente:


</div>



#VRML V2.0 utf8
Group {
  children 
    Group {
      children [ 
        Group {
        …
        },
          
        Group {
        …
        },
          
        Group {
        …
        },
          
        Group {
        …
        },
          
        Group {
        …
        },
          
        Group {
        …
        },
          
        Group {
        …
        },
          
        Group {
        …
        } ]
    }
}



Si può notare che ci sono 8 gruppi indipendenti, corrispondenti alle 8 forme.


<div class="mw-translate-fuzzy">

## Preparazione del file VRML 

Tutte le forme nel file VRML sono espresse nella struttura di base, indipendentemente le une dalle altre.
Per l\'ambiente Simulazione Robot di FreeCAD, è necessario creare una struttura in cui un movimento di una forma induce un movimento di tutte le forme che sono situate successivamente nella struttura. Il posizionamento delle forme sarà relativo alla forma precedente, quindi è necessario includere alcune traduzioni dal sistema di riferimento assoluto a quello relativo.
Le traduzioni sono descritte nella figura seguente:


</div>

![](images/staeubli_important_points.png )

Con:

:   A=(0, 0, 168)
:   B=(0, 107.8, 320)
:   C=(0, 104.15, 545)
:   D=(0, 35, 601)
:   E=(0, 35, 770)
:   F=(0, 35, 835)

Prendiamo come esempio l\'asse 4 tra ELBOW e FOREARM, situato in D=(xd, yd, zd). Il punto di ancoraggio per l\'asse di FreeCAD è: 

"DEF FREECAD_AXIS4 Transform { rotation 0 1 0 0 children ["




<div class="mw-translate-fuzzy">

Questo corrisponde ad una rotazione intorno all\'asse Y. Nel modello CAD, la rotazione è intorno all\'asse Z.
Pertanto, è necessaria una rotazione intorno all\'asse X di $\pi$ prima della definizione dell\'asse di FreeCAD e di -$\pi$ dopo di essa.
Inoltre, è necessaria una translation di (-xd, yd-,-zd) immediatamente prima del gruppo corrispondente alla definizione di FOREARM e espressa nel frame di riferimento relativo centrato rispetto a D.
Ciò significa che la translation di (xd, yd, zd) deve essere inserita prima della prima rotazione.
Alla fine, il file VRML compreso tra la definizione di ELBOW e la definizione di FOREARM è simile al seguente:


</div>



      # ELBOW
      Group {
        … here comes the unmodified definition of ELBOW
  
      },
        
      Transform {
        translation 0 35 601
        rotation 1 0 0 1.5707963
        children
          DEF FREECAD_AXIS4 Transform { rotation 0 1 0 0 children
            Transform {
              rotation 1 0 0 -1.5707963
              children
                Transform {
                  translation 0 -35 -601
                  children [
      # FOREARM  
      Group {
        ... here comes the unmodified definition of FOREARM
  
      },



Alla fine del documento, si devono inserire le parentesi di chiusura appropriate: 

#VRML V2.0 utf8
  
  
Group {
  children
  Group {
    children [ 
      # HORIZONTAL BASE CABLE OUTLET 
      Group {
          ... here comes the unmodified definition of HORIZONTAL BASE CABLE OUTLET
   
      },
        
      Transform {
        translation 0 0 168
        rotation 1 0 0 1.5707963
        children
          DEF FREECAD_AXIS1 Transform { rotation 0 1 0 0 children
            Transform {
              rotation 1 0 0 -1.5707963
              children
                Transform {
                  translation 0 0 -168
                  children [
      # SHOULDER
      Group {
          ... here comes the unmodified definition of SHOULDER 
  
      },
        
      Transform {
        translation 0 107.8 320
        #rotation 0 0 1 0
        children
          DEF FREECAD_AXIS2 Transform { rotation 0 1 0 0 children
            Transform {
              #rotation 0 0 1 0
              children
                Transform {
                  translation 0 -107.8 -320
                  children [
      # ARM  
      Group {
          ... here comes the unmodified definition of ARM 
  
      },
        
      Transform {
        translation 0 104.15 545
        #rotation 0 0 1 0
        children
          DEF FREECAD_AXIS3 Transform { rotation 0 1 0 0 children
            Transform {
              #rotation 0 0 1 0
              children
                Transform {
                  translation 0 -104.15 -545
                  children [
      # ELBOW
      Group {
          ... here comes the unmodified definition of ELBOW
  
      },
        
      Transform {
        translation 0 35 601
        rotation 1 0 0 1.5707963
        children
          DEF FREECAD_AXIS4 Transform { rotation 0 1 0 0 children
            Transform {
              rotation 1 0 0 -1.5707963
              children
                Transform {
                  translation 0 -35 -601
                  children [
      # FOREARM  
      Group {
          ... here comes the unmodified definition of FOREARM
  
      },
        
      Transform {
        translation 0 35 770
        #rotation 0 0 1 0
        children
          DEF FREECAD_AXIS5 Transform { rotation 0 1 0 0 children
            Transform {
              #rotation 0 0 1 0
              children
                Transform {
                  translation 0 -35 -770
                  children [
      # WRIST
      Group {
          ... here comes the unmodified definition of WRIST
  
      },
        
      Transform {
        translation 0 35 835
        rotation 1 0 0 1.5707963
        children
          DEF FREECAD_AXIS6 Transform { rotation 0 1 0 0 children
            Transform {
              rotation 1 0 0 -1.5707963
              children
                Transform {
                  translation 0 -35 -835
                  children [
      # TOOL FLANGE
      Group {
          ... here comes the unmodified definition of TOOL FRAME
  
      },
        
      Group {
          ... here comes the unmodified definition of TX40_HB007
  
      } # "]" was deleted from this line
    ]}}}},
    ]}}}},
    ]}}}},
    ]}}}},
    ]}}}},
    ]}}}},
    ] # this is the "]" deleted from the line above
  }
}




<div class="mw-translate-fuzzy">

Ecco un patch per ottenere il file VRML adatto per la simulazione del robot:


</div>



7a8
>         # HORIZONTAL BASE CABLE OUTLET 
95968a95970,95981
>         Transform {
>           translation 0 0 168
>           rotation 1 0 0 1.5707963
>           children
>             DEF FREECAD_AXIS1 Transform { rotation 0 1 0 0 children
>               Transform {
>                 rotation 1 0 0 -1.5707963
>                 children
>                   Transform {
>                     translation 0 0 -168
>                     children [
>         # SHOULDER
128428a128442,128453
>         Transform {
>           translation 0 107.8 320
>           #rotation 0 0 1 0
>           children
>             DEF FREECAD_AXIS2 Transform { rotation 0 1 0 0 children
>               Transform {
>                 #rotation 0 0 1 0
>                 children
>                   Transform {
>                     translation 0 -107.8 -320
>                     children [
>         # ARM  
206503a206529,206540
>         Transform {
>           translation 0 104.15 545
>           #rotation 0 0 1 0
>           children
>             DEF FREECAD_AXIS3 Transform { rotation 0 1 0 0 children
>               Transform {
>                 #rotation 0 0 1 0
>                 children
>                   Transform {
>                     translation 0 -104.15 -545
>                     children [
>         # ELBOW
267111a267149,267160
>         Transform {
>           translation 0 35 601
>           rotation 1 0 0 1.5707963
>           children
>             DEF FREECAD_AXIS4 Transform { rotation 0 1 0 0 children
>               Transform {
>                 rotation 1 0 0 -1.5707963
>                 children
>                   Transform {
>                     translation 0 -35 -601
>                     children [
>         # FOREARM  
417854a417904,417915
>         Transform {
>           translation 0 35 770
>           #rotation 0 0 1 0
>           children
>             DEF FREECAD_AXIS5 Transform { rotation 0 1 0 0 children
>               Transform {
>                 #rotation 0 0 1 0
>                 children
>                   Transform {
>                     translation 0 -35 -770
>                     children [
>         # WRIST
422053a422115,422126
>         Transform {
>           translation 0 35 835
>           rotation 1 0 0 1.5707963
>           children
>             DEF FREECAD_AXIS6 Transform { rotation 0 1 0 0 children
>               Transform {
>                 rotation 1 0 0 -1.5707963
>                 children
>                   Transform {
>                     translation 0 -35 -835
>                     children [
>         # TOOL FLANGE
435627c435700,435707
<         } ]
---
>         } 
>       ]}}}},
>       ]}}}},
>       ]}}}},
>       ]}}}},
>       ]}}}},
>       ]}}}},
>       ]





[Category:Robot](Category:Robot.md)
