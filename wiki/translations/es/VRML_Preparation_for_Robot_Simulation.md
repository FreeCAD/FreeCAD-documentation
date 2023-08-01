# VRML Preparation for Robot Simulation/es
{{TutorialInfo/es
|Topic=Ambiente de trabajo Robot
|Level=Intermedio
|Time=
|Author=
|FCVersion=
|Files=
}}


**The FreeCAD Robot Workbench is unmaintained. Please mention on the FreeCAD forum if you have an interest in maintaining this 
workbench.**

## Vista general 


<div class="mw-translate-fuzzy">

Este tutorial explica como utilizar FreeCAD y el entorno de simulación de Robots para simular los movimientos de un robot de 6 ejes. **El tutorial se centra en la creación de un archivo VRML** utilizado como visualización. La base del archivo VRML es el modelo de FreeCAD. La versión de FreeCAD utilizada es 0.11.4252ppa1 en Ubuntu 32bit.


</div>

## Abrir un archivo o crear uno con FreeCAD 

El tutorial está basado en un archivo STEP de un Stäubli TX40 (TX40-HB.stp). Puedes descargar el archivo de <https://secure.staubli.com/Intranet_Applications/Robotics/Group/RobDoc.nsf/ea05b3f4b301f597c1256d5f005665e8/bc3707ec036c9f6bc12576c700327958/$FILE/page.html>. Sin embargo, aunque aún no he tenido tiempo para comprobarlo, el método debería también aplicarse a un modelo creado completamente en FreeCAD. Después de abrir el archivo deberías tener esto:

<img alt="" src=images/staeubli_step_import.png  style="width:1024px;">


<div class="mw-translate-fuzzy">

Observa, que en la importación, el robot es creado en 8 formas, directamente en la raíz del árbol del documento. La estructura del archivo VRML exportado debe cambiarse si se utilizan grupos. Las formas están ordenadas desde la base a la herramienta. La última forma contiene los ejes de rotación de todos los ejes del robot. Los nombres de las formas son dados de forma correlativa (de momento, marzo de 2011, FreeCAD no importa los nombres incluidos en los archivos STEP):


</div>

  FreeCAD name   STEP name
   
  TX40_HB        HORIZONTAL BASE CABLE OUTLET
  TX40_HB001     SHOULDER
  TX40_HB002     ARM
  TX40_HB003     ELBOW
  TX40_HB004     FOREARM
  TX40_HB005     WRIST
  TX40_HB006     TOOL FLANGE
  TX40_HB007     ?


<div class="mw-translate-fuzzy">

Cambia el "modo de visualización" de cada forma, excepto TX40_HB007, de "líneas planas" a "sombreado" para que la exportación a VRML tenga un buen aspecto. Yo también he cambiado el color a \[245, 196, 0\] y \[204, 204, 204\] para corresponderse mejor con el amarillo de Stäubli. Oculta TX40_HB007 porque contiene los ejes de todas las uniones y no puede cogerse aparte.


</div>


<div class="mw-translate-fuzzy">

## Medición de características geométricas 

Para construir la tabla Denavit-Hartenberg (mira <http://www.freecadweb.org/wiki/index.php?title=6-Axis_Robot>) y preparar el archivo VRML, necesitas obtener las características del robot. De momento, la herramienta de medición de FreeCAD aún no está disponible, puedes utilizar los ejes incluidos en TX40_HB007 (las coordenadas son indicadas en la parte inferior izquierda cuando apuntas un objeto con el ratón) o tienes que utilizar la consola de Python para obtener algo de información sobre la geometría. Observa que la tabla DH-table sólo es requerida si necesitas utilizar cinemática inversa, por ejemplo obtener las coordenadas cartesianas o conducir el robot con coordenadas cartesianas. La tabla DH-table para este robot es la siguiente (mm, deg y deg/s):


</div>

  i   d     θ         r     α     θmin   θmax    Axis velocity
  ---       
  1   320   q1        0     -90   -180   180     555
  2   35    q2 - 90   225   0     -125   125     475
  3   0     q3 + 90   0     90    -138   138     585
  4   225   q4        0     -90   -270   270     1035
  5   0     q5        0     90    -120   133.5   1135
  6   65    q6        0     0     -270   270     1575

El archivo CSV es entonces:

 a  , alpha, d  , theta, rotDir, maxAngle, minAngle, AxisVelocity
0  ,   -90, 320,     0,      1,      180,     -180, 555
225,     0,  35,   -90,      1,      125,     -125, 475
0  ,    90,   0,    90,      1,      138,     -138, 585
0  ,   -90, 225,     0,      1,      270,     -270, 1035
0  ,    90,   0,     0,      1,    133.5,     -120, 1135
0  ,     0,  65,     0,      1,      270,     -270, 1575


<div class="mw-translate-fuzzy">

## Exportar a VRML 

Exportar el documento a un archivo VRML. La estructura del archivo VRML es la siguiente:


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



Puedes observar que tenemos 8 grupos independientes correspondientes a las 8 formas.


<div class="mw-translate-fuzzy">

## Preparación del archivo VRML 

Todas las formas en el archivo VRML son expresadas en el cuadro base, independientemente de cada otra. Para el entorno de simulación de Robots, necesitamos crear una estructura donde un movimiento de una forma induzca un movimiento de todas las formas situadas después en la estructura. La ubicación de las formas será relativa a la forma precedente, así necesitamos incluir algunas traducciones desde el sistema de referencia absoluto a los relativos. Las traducciones se describen en la siguiente imagen:


</div>

![](images/staeubli_important_points.png )

Con

:   A=(0, 0, 168)
:   B=(0, 107.8, 320)
:   C=(0, 104.15, 545)
:   D=(0, 35, 601)
:   E=(0, 35, 770)
:   F=(0, 35, 835)

Cojamos el ejemplo de el eje 4 entre ELBOW y FOREARM, situado en D=(xd, yd, zd). El anclaje para el eje de FreeCAD es 

"DEF FREECAD_AXIS4 Transform { rotation 0 1 0 0 children ["




<div class="mw-translate-fuzzy">

Este corresponde a la rotación alrededor del eje Y. En el modelo de CAD, la rotación es alrededor del eje Z. Así, necesitamos una rotación alrededor del eje X de $\pi$ antes de la definición del eje en FreeCAD y de $-\pi$ después de ella. También, se necesita una traslación de (-xd, -yd, -zd) antes de la correspondencia del grupo a la definición de FOREARM para expresarlo centrado en el cuadro de referencia relativa en D. Esto significa que la traslación de (xd, yd, zd) debe insertarse antes de la primera rotación. Al final, el archivo VRML de la definición de ELBOW a la definición de FOREARM se parecerá a esto:


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




<div class="mw-translate-fuzzy">

Al final del documento, deben insertarse los corchetes de cierre apropiados: " \]}}}}," para cada uno de los 6 ejes. Al final, el documento se parecerá a esto (No sé si puedo vincular el archivo aquí debido al copyright):


</div>



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

Aquí está un parche para conseguir el archivo VRML adecuado para la simulación del robot:


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



---
⏵ [documentation index](../README.md) > [Robot](Category_Robot.md) > VRML Preparation for Robot Simulation/es
