# VRML Preparation for Robot Simulation/pl
{{TutorialInfo/pl
|Topic=środowisko pracy Robot
|Level=średnio zaawansowany
|Time=dowolny
|Author=
|FCVersion=0.11.4252ppa1
|Files=
}}


**Środowisko pracy FreeCAD Robot nie jest utrzymywane. Prosimy o wzmiankę na forum FreeCAD, jeśli jesteś zainteresowany utrzymaniem tego środowiska pracy.**



## Informacje ogólne 

Ten samouczek wyjaśnia, jak korzystać z FreeCAD i środowiska symulacji <img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Robot](Robot_Workbench/pl.md) do symulacji ruchów 6-osiowego robota szeregowego. **Samouczek skupia się na tworzeniu pliku VRML** używanego jako wizualizacja. Podstawą pliku VRML jest model FreeCAD. Użyta wersja FreeCAD to 0.11.4252ppa1 na Ubuntu 32bit.

## Otwórz plik lub utwórz go za pomocą FreeCAD 

Samouczek opiera się na pliku STEP urządzenia Stäubli TX40 (TX40-HB.stp). Plik można pobrać ze strony [Stäubli](https://secure.staubli.com/Intranet_Applications/Robotics/Group/RobDoc.nsf/ea05b3f4b301f597c1256d5f005665e8/bc3707ec036c9f6bc12576c700327958/$FILE/page.html). Jednak, choć wciąż nie miałem czasu, aby to sprawdzić, metoda ta powinna mieć również zastosowanie do modelu wykonanego w całości w programie FreeCAD. Po otwarciu pliku powinieneś otrzymać:

<img alt="" src=images/staeubli_step_import.png  style="width:1024px;">

Zauważ, że po zaimportowaniu obiekt robot składa się z 8 kształtów, bezpośrednio na korzeniu drzewa dokumentu. Struktura wyeksportowanego pliku VRML może ulec zmianie, jeśli używane są grupy. Kształty są uporządkowane od podstawy do narzędzia. Ostatni kształt zawiera osie obrotu wszystkich osi robota. Nazwa kształtu korelacji - nazwa części jest podana przez *(na chwilę obecną (marzec 2011) FreeCAD nie importuje nazw zawartych w plikach STEP)*:

  nazwa FreeCAD   nazwa STEP
   
  TX40_HB         HORIZONTAL BASE CABLE OUTLET
  TX40_HB001      SHOULDER
  TX40_HB002      ARM
  TX40_HB003      ELBOW
  TX40_HB004      FOREARM
  TX40_HB005      WRIST
  TX40_HB006      TOOL FLANGE
  TX40_HB007      ?

W przypadku tego importu należy zmienić \"Tryb wyświetlania\" każdego kształtu, z wyjątkiem TX40_HB007, z \"Cieniowany z krawędziami\" na \"Cieniowane\", aby eksport VRML wyglądał dobrze. Zmieniłem również kolory na \[245, 196, 0\] i \[204, 204, 204\], aby lepiej odpowiadały żółtemu kolorowi Stäubli. Ukryj TX40_HB007, ponieważ zawiera on osie wszystkich połączeń i nie można go rozdzielić.

## Pomiar charakterystyk geometrycznych 

Aby zbudować tabelę Denavita-Hartenberga *(patrz [Robot: 6-osi](Robot_6-Axis/pl.md))* i przygotować plik vrml, musisz uzyskać charakterystykę robota. Na razie narzędzie pomiarowe FreeCAD nie jest gotowe, możesz użyć osi zawartych w TX40_HB007 (współrzędne są wskazywane w lewym dolnym rogu po wskazaniu obiektu myszą) lub musisz użyć konsoli Python, aby uzyskać informacje o geometrii. Należy pamiętać, że tabela DH jest wymagana tylko wtedy, gdy trzeba użyć kinematyki odwrotnej, tj. uzyskać współrzędne kartezjańskie lub sterować robotem za pomocą współrzędnych kartezjańskich. Tabela DH dla tego robota jest następująca *(mm, stopnie i stopnie/s)*:

  i   d     θ         r     α     θmin   θmax    Prędkość osi
  ---       
  1   320   q1        0     -90   -180   180     555
  2   35    q2 - 90   225   0     -125   125     475
  3   0     q3 + 90   0     90    -138   138     585
  4   225   q4        0     -90   -270   270     1035
  5   0     q5        0     90    -120   133.5   1135
  6   65    q6        0     0     -270   270     1575

Plik csv to:

a  , alpha, d  , theta, rotDir, maxAngle, minAngle, Prędkość osi
0  ,   -90, 320,     0,      1,      180,     -180, 555
225,     0,  35,   -90,      1,      125,     -125, 475
0  ,    90,   0,    90,      1,      138,     -138, 585
0  ,   -90, 225,     0,      1,      270,     -270, 1035
0  ,    90,   0,     0,      1,    133.5,     -120, 1135
0  ,     0,  65,     0,      1,      270,     -270, 1575

## Eksport do VRML 

Eksport dokumentu do pliku VRML. Struktura pliku VRML jest następująca: 

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



Można zauważyć, że mamy 8 niezależnych grup odpowiadających 8 kształtom.

## Przygotowanie pliku vrml 

Wszystkie kształty w pliku VRML są wyrażone w ramce bazowej, niezależnie od siebie. Dla środowiska [symulacji Robot](Robot_Workbench.md) musimy stworzyć strukturę, w której ruch kształtu wywołuje ruch wszystkich kształtów znajdujących się po nim w strukturze. Umieszczenie kształtów będzie względne w stosunku do poprzedniego kształtu, więc musimy uwzględnić pewne translacje z bezwzględnego układu odniesienia do względnego. Przesunięcia te zostały opisane na poniższym rysunku:

![](images/staeubli_important_points.png )

Przy

:   A=(0, 0, 168)
:   B=(0, 107.8, 320)
:   C=(0, 104.15, 545)
:   D=(0, 35, 601)
:   E=(0, 35, 770)
:   F=(0, 35, 835).

Weźmy przykład osi 4 między ELBOW i FOREARM, znajdującej się w D=(xd, yd, zd). Kotwica dla osi FreeCAD to 

"DEF FREECAD_AXIS4 Transform { rotation 0 1 0 0 children ["

 Odpowiada to obrotowi wokół osi y. W modelu CAD obrót dotyczy osi z. Dlatego potrzebujemy obrotu wokół osi x $\pi$ przed definicją osi FreeCAD i $-\pi$ po niej. Ponadto translacja (-xd, -yd, -zd) jest potrzebna tuż przed grupą odpowiadającą definicji FOREARM, aby wyrazić ją we względnym układzie odniesienia wyśrodkowanym w D. Oznacza to, że przesunięcie (xd, yd, zd) musi zostać wstawione przed pierwszym obrotem. Na koniec plik VRML od definicji ELBOW do definicji FOREARM wygląda następująco: 

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



Na końcu dokumentu należy wstawić odpowiednie nawiasy zamykające: 

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

 Oto łatka pozwalająca uzyskać plik VRML odpowiedni do symulacji robota: 

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
⏵ [documentation index](../README.md) > [Robot](Category_Robot.md) > VRML Preparation for Robot Simulation/pl
