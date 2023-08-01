# VRML Preparation for Robot Simulation/de
{{TutorialInfo/de
|Topic=Roboter Arbeitsbereich
|Level=Mittelschwer
|Time=
|Author=
|FCVersion=0.11.4252ppa1
|Files=
}}


**Der FreeCAD Roboter Arbeitsbereich wird nicht gewartet. Bitte erwähne im FreeCAD Forum, wenn du daran interessiert bist, diesen Arbeitsbereich zu warten.**

## Übersicht

Dieses Tutorium erklärt, wie man FreeCAD und den <img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Arbeitsbereich Roboter Simulation](Robot_Workbench/de.md) um die Bewegungen eines 6-achsigen Serienroboters zu simulieren. **Das Tutorium konzentriert sich auf die Erstellung der als Visualisierung verwendeten VRML Datei**. Die Basis der VRML Datei ist ein FreeCAD Modell. Die verwendete Version von FreeCAD ist 0.11.4252ppa1 auf Ubuntu 32bit.

## Öffne eine Datei oder erstelle eine mit FreeCAD 

Das Tutorium basiert auf einer STEP Datei eines Stäubli TX40 (TX40-HB.stp). Du kannst die Datei von [Stäubli](https://secure.staubli.com/Intranet_Applications/Robotics/Group/RobDoc.nsf/ea05b3f4b301f597c1256d5f005665e8/bc3707ec036c9f6bc12576c700327958/$FILE/page.html) herunterladen. Obwohl ich immer noch nicht die Zeit hatte, dies zu überprüfen, sollte die Methode auch auf ein vollständig in FreeCAD erstelltes Modell anwendbar sein. Nachdem du die Datei geöffnet hast, solltest du dies erhalten:

<img alt="" src=images/staeubli_step_import.png  style="width:1024px;">

Beachte, dass der Roboter beim Import aus 8 Formen besteht, die sich direkt an der Wurzel des Dokumentenbaums befinden. Die Struktur der exportierten VRML Datei kann sich ändern, wenn Gruppen verwendet werden. Die Formen sind von der Basis bis zum Werkzeug geordnet. Die letzte Form enthält die Drehachsen aller Roboterachsen. Die Korrelation Formname - Teilename Teilname wird erteilt durch (vorläufig (März 2011) importiert FreeCAD die in STEP Dateien enthaltenen Namen nicht):

  FreeCAD name   STEP name
   
  TX40_HB        HORIZONTAL BASE CABLE OUTLET
  TX40_HB001     SHOULDER
  TX40_HB002     ARM
  TX40_HB003     ELBOW
  TX40_HB004     FOREARM
  TX40_HB005     WRIST
  TX40_HB006     TOOL FLANGE
  TX40_HB007     ?

Ändere für diesen Import den \" Darstellungsmodus\" jeder Form, mit Ausnahme von TX40_HB007, von \"Flache Linien\" in \"Schattiert\", damit der VRML Export gut aussieht. Ich änderte auch die Farben in \[245, 196, 0\] und \[204, 204, 204\], um dem Gelb von Stäubli besser zu entsprechen. Blende TX40_HB007 aus, weil es die Achsen aller Gelenke enthält und nicht auseinandergenommen werden kann.

## Messen geometrischer Merkmale 

Um die Denavit-Hartenberg Tabelle zu erstellen (siehe [Roboter 6-Achsen](Robot_6-Axis/de.md)) und die vrml Datei vorzubereiten, musst du die Eigenschaften des Roboters ermitteln. Im Moment ist das Messwerkzeug von FreeCAD noch nicht fertig, du kannst die in TX40_HB007 enthaltenen Achsen verwenden (die Koordinaten werden unten links angezeigt, wenn du mit der Maus auf ein Objekt zeigst) oder du musst die Python Konsole verwenden, um einige Informationen über die Geometrie zu erhalten. Beachte, dass die DH-Tabelle nur erforderlich ist, wenn du die inverse Kinematik verwenden musst, d.h. bekomme die kartesischen Koordinaten oder steuere den Roboter mit kartesischen Koordinaten. Die DH-Tabelle für diesen Roboter ist die folgende (mm, Grad und Grad/s):

  i   d     θ         r     α     θmin   θmax    Achsgeschwindikeit
  ---       
  1   320   q1        0     -90   -180   180     555
  2   35    q2 - 90   225   0     -125   125     475
  3   0     q3 + 90   0     90    -138   138     585
  4   225   q4        0     -90   -270   270     1035
  5   0     q5        0     90    -120   133.5   1135
  6   65    q6        0     0     -270   270     1575

Die csv Datei ist dann:

a  , alpha, d  , theta, rotDir, maxWinkel, minWinkel, AchsGeschwindigkeit
0  ,   -90, 320,     0,      1,      180,     -180, 555
225,     0,  35,   -90,      1,      125,     -125, 475
0  ,    90,   0,    90,      1,      138,     -138, 585
0  ,   -90, 225,     0,      1,      270,     -270, 1035
0  ,    90,   0,     0,      1,    133.5,     -120, 1135
0  ,     0,  65,     0,      1,      270,     -270, 1575

## Export nach VRML 

Exportiere das Dokument in eine VRML Datei. Die Struktur der VRML Datei ist wie folgt: 

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



Du kannst feststellen, dass wir 8 unabhängige Gruppen haben, die den 8 Formen entsprechen.

## Vorbereitung der vrml Datei 

Alle Formen in der VRML Datei werden unabhängig voneinander im Grundrahmen ausgedrückt. Für den [Arbeitsbereich Roboter Simulation](Robot_Workbench/de.md) müssen wir eine Struktur erstellen, bei der eine Bewegung einer Form eine Bewegung aller danach in der Struktur befindlichen Formen auslöst. Die Platzierung der Formen erfolgt relativ zu der vorhergehenden Form, so dass wir einige Übersetzungen vom absoluten Bezugssystem in das relative System einbeziehen müssen. Die Übersetzungen sind in der folgenden Abbildung beschrieben:

![](images/staeubli_important_points.png )

Mit

:   A=(0, 0, 168)
:   B=(0, 107.8, 320)
:   C=(0, 104.15, 545)
:   D=(0, 35, 601)
:   E=(0, 35, 770)
:   F=(0, 35, 835).

Nehmen wir das Beispiel der Achse 4 zwischen ELLBOGEN und UNTERARM, die sich bei D=(xd, yd, zd) befindet. Der Anker für die FreeCAD Achse ist 

"DEF FREECAD_AXIS4 Transform { rotation 0 1 0 0 children ["

 Dies entspricht einer Drehung um die y-Achse. Im CAD Modell erfolgt die Drehung um die z-Achse. Wir benötigen also eine Drehung um die x-Achse von $\pi$ vor der FreeCAD Achsdefinition und von $-\pi$ danach. Ausserdem ist eine Translation von (-xd, -yd, -zd) unmittelbar vor der Gruppe erforderlich, die der Definition von UNTERARM entspricht, um sie im relativen Bezugssystem auszudrücken, das bei D zentriert ist. Dies bedeutet, dass eine Translation von (xd, yd, zd) vor der ersten Drehung eingefügt werden muss. Am Ende sieht die VRML Datei von der Definition von ELLBOGEN bis zur Definition von UNTERARM wie folgt aus: 

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



Am Ende des Dokuments müssen die entsprechenden schließenden Klammern eingefügt werden: 

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

 Hier ist eine Korrektur, um die für die Robotersimulation geeignete VRML Datei zu erhalten: 

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



---
![](images/Button_right.svg) [documentation index](../README.md) > [Robot](Category_Robot.md) > VRML Preparation for Robot Simulation/de
