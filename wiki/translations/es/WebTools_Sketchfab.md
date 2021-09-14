---
- GuiCommand:/es
   Name:WebTools Sketchfab
   Name/es:HerramientasWeb Sketchfab
   MenuLocation:HerramientasWeb → Sketchfab
   Workbenches:[HerramientasWeb](WebTools_Workbench/es.md)
---

## Descripción

Esta herramienta le permite exportar y subir objetos a su cuenta [SketchFab](http://www.sketchfab.com). {{Version/es|0.17}}

![](images/Sketchfab_exporter.jpg )

## Utilización

1.  Crea tú mismo una cuenta en [SketchFab](http://www.sketchfab.com) si aún no tienes una. Las cuentas gratuitas están bien, las cuentas de pago añaden más características como la posibilidad de tener modelos privados y mayores tamaños máximos de subida
2.  Prepara un modelo que quieras subir
3.  Haz clic en <img alt="" src=images/WebTools_Sketchfab.svg  style="width:32px;"> de la barra de herramientas principal en el [Ambiente de trabajo HerramientasWeb](WebTools_Workbench/es.md)
4.  Rellene los campos. El nombre y la clave API son obligatorios
5.  Haga clic en el botón \"Cargar\".

## Opciones

-   Necesitas una clave API de Sketchfab para que este exportador pueda conectarse a tu cuenta de Sketchfab. Al pulsar el botón \"Obtener\", serás dirigido a tu página de configuración de Sketchfab, donde se da esa clave API (que es única para tu cuenta). Copie la clave y péguela en el campo \"API key\" del exportador. Este valor será almacenado por FreeCAD así que sólo necesitas hacerlo una vez
-   El campo del nombre es obligatorio, los otros pueden dejarse en blanco.
-   El exportador propone varios formatos de exportación diferentes. El mejor para ti depende del tipo de modelo y resultado que desees obtener, se recomienda probar lo que mejor te funcione. Generalmente, OBJ + MTL te dará un mejor control sobre los materiales, mientras que IV (OpenInventor) dará un resultado más parecido a lo que se ve en la vista 3D de FreeCAD.
-   Una vez subido tu modelo, Sketchfab ofrece una interfaz bastante avanzada en la que puedes seguir configurando los materiales, la iluminación y el entorno.
-   Cuando pulses el \"botón de subir\", una vez terminada la subida, si todo ha ido bien, el botón se convertirá en un botón de \"Ver tu modelo online\", que, al pulsarlo, te llevará directamente a la página del modelo en Sketchfab.
-   Algunos formatos, como el OBJ, son interpretados de forma diferente por Sketchfab y FreeCAD. FreeCAD considera que el eje Z apunta hacia arriba, mientras que Sketchfab considera que apunta hacia la persona que está detrás de la pantalla. Para remediar esto, una vez finalizada la carga, el exportador utilizará la API de Sketchfab para rotar el modelo a su posición correcta. Si esta operación falla, recibirás un aviso, pero tu modelo seguirá siendo subido correctamente. Puedes rotarlo manualmente en la interfaz de Sketchfab, pulsando la flecha derecha junto al eje \"X\" en la pestaña de orientación del modelo.
