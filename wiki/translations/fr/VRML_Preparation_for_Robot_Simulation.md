


<div class="mw-translate-fuzzy">


{{TutorialInfo/fr
|Topic=Robot Workbench
|Level=Intermediate
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

Ce tutoriel explique comment utiliser FreeCAD et le **Workbench Simulation Robot** pour simuler les mouvements du robot sur **6 axes**.
Le tutoriel se concentre sur la création du fichier **VRML** utilisé pour la visualisation. La base du fichier **VRML** est un modèle FreeCAD. La version de FreeCAD utilisée est **0.11.4252ppa1** sur Ubuntu 32 bits.


</div>

## Ouvrir un fichier, ou en créer un avec FreeCAD 

Le tutoriel est basé sur un **fichier-STEP** d\'un **[Stäubli TX40](http://www.staubli.com/fr/robotique/robots-4-et-6-axes/robots-petits-porteurs/tx40/)**, vous pouvez télécharger le fichier [fichier TX40-HB.stp](https://secure.staubli.com/Intranet_Applications/Robotics/Group/RobDoc.nsf/ea05b3f4b301f597c1256d5f005665e8/bc3707ec036c9f6bc12576c700327958/$FILE/page.html), la méthode, devrait également s\'appliquer à un modèle entièrement réalisé dans FreeCAD, cependant, je n\'ai pas encore eu le temps de vérifier ce point.
Après l\'ouverture du fichier, vous devriez obtenir ceci :

<img alt="" src=images/staeubli_step_import.png  style="width:1024px;">


<div class="mw-translate-fuzzy">

On notera que pour l\'importation, le robot est composé de 8 formes, directement sur la racine de l\'arbre du document.
La structure du fichier **VRML** exporté peut changer si des groupes sont utilisés. Les formes sont commandées à partir de la base de l\'outil.
La dernière forme contient les axes de rotation de tous les axes du robot.
Le nom de forme de corrélation, le nom de la pièce est donné (pour l\'instant (Mars 2011) par FreeCAD, FreeCAD n\'importe pas encore les noms inclus dans les fichiers STEP) :


</div>

  FreeCAD name   STEP name
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

Pour cette importation, changez le \"Mode d\'affichage\" de chaque forme, à l\'exception **TX40\_HB007**, de \"**lisser**\" les lignes en \"**Ombrage**\" pour l\'exportation **VRML** pour faire bonne figure. J\'ai aussi changé les couleurs de **\[245, 196, 0\]** et **\[204, 204, 204\]** afin de mieux correspondre au jaune Stäubli.
Masquer **TX40\_HB007** car il contient les axes de tous les joints et ne peut pas être démonté.


</div>

## Mesure des caractéristiques géométriques 

Afin de construire la table [Denavit-Hartenberg](http://fr.wikipedia.org/wiki/Denavit-Hartenberg) (voir [6-Axis\_Robot](Robot_6-Axis/fr.md) ) et de préparer le fichier [VRML](http://fr.wikipedia.org/wiki/Virtual_Reality_Markup_Language), que vous avez besoin pour obtenir des caractéristiques du Robot. Pour l\'instant, l\'outil de mesure de FreeCAD n\'est pas prêt, vous pouvez utiliser les axes inclus dans **TX40\_HB007** (les coordonnées sont indiquées en bas à gauche lorsque vous pointez un objet avec la souris) ou vous devez utiliser la [console Python](Introduction_to_Python/fr.md) pour obtenir des informations sur la forme géométrique.
Notez que, le **DH-tableau** n\'est nécessaire que si vous avez besoin d\'utiliser la cinématique inverse, c\'est à dire obtenir les coordonnées cartésiennes ou de commander le robot en coordonnées cartésiennes.
La **DH-table** pour ce robot est le suivant **(mm, degrés et deg/s)** :

  i   d     θ         r     α     θmin   θmax    Axis velocity
  --- ----- --------- ----- ----- ------ ------- ---------------
  1   320   q1        0     -90   -180   180     555
  2   35    q2 - 90   225   0     -125   125     475
  3   0     q3 + 90   0     90    -138   138     585
  4   225   q4        0     -90   -270   270     1035
  5   0     q5        0     90    -120   133.5   1135
  6   65    q6        0     0     -270   270     1575

Le fichier **csv** est :

 a  , alpha, d  , theta, rotDir, maxAngle, minAngle, AxisVelocity
0  ,   -90, 320,     0,      1,      180,     -180, 555
225,     0,  35,   -90,      1,      125,     -125, 475
0  ,    90,   0,    90,      1,      138,     -138, 585
0  ,   -90, 225,     0,      1,      270,     -270, 1035
0  ,    90,   0,     0,      1,    133.5,     -120, 1135
0  ,     0,  65,     0,      1,      270,     -270, 1575


<div class="mw-translate-fuzzy">

## Exporter en VRML 

Exporter le document dans un fichier VRML.
La structure du fichier VRML est la suivante :


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



Vous pouvez remarquer que nous avons 8 groupes indépendants, correspondants aux 8 formes.


<div class="mw-translate-fuzzy">

## Préparation du dossier de vrml 

Toutes les formes dans le fichier **vrml** sont exprimées dans le cadre de base, indépendamment les uns des autres. Pour le **Workbench Simulation Robot**, nous avons besoin de créer une structure où, un mouvement de formes induit un mouvement de toutes les formes qui se trouveront ensuite dans la structure. Le placement des formes sera relatif à la forme précédente, nous avons donc besoin d\'inclure quelques modifications à partir du système de référence absolu vers le système relatif.
Les traductions sont décrites dans le tableau suivant :


</div>

![](images/staeubli_important_points.png )

With

:   A=(0, 0, 168)
:   B=(0, 107.8, 320)
:   C=(0, 104.15, 545)
:   D=(0, 35, 601)
:   E=(0, 35, 770)
:   F=(0, 35, 835).

Prenons l\'exemple de l\'axe **4** entre le coude et avant-bras, située à **D = (xd, yd, zd)**.
Le point d\'ancrage pour l\'axe de FreeCAD est : 

"DEF FREECAD_AXIS4 Transform { rotation 0 1 0 0 children ["




<div class="mw-translate-fuzzy">

Cela correspond à une rotation autour de l\'axe **y**. Dans le modèle CAO, la rotation se fait sur l\'axe **z**. Ainsi, nous avons besoin d\'une rotation autour de l\'axe **x** de **$\pi$** avant la définition des axes de FreeCAD et de **-$\pi$** après. En outre, une traduction de **(-xd, yd-,-zd)** est nécessaire juste avant le groupe correspondant à la définition de l\'avant bras, et de l\'exprimer dans le cadre de référence centré par rapport à **D**.
Cela signifie que la traduction de **(xd, yd, zd)** doit être insérée avant la première rotation.
A la fin, le **fichier vrml** à partir de la définition du **COUDE** (ELBOW) vers la définition de l**\'avant bras** (FOREARM) ressemble à ceci :


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



En fin de document, les crochets de fermeture appropriés doivent être insérés: 

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

Voici un **patch** pour obtenir un fichier **vrml** convenant à la simulation du robot :


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





[Category:Robot{{\#translation:}}](Category:Robot.md)
