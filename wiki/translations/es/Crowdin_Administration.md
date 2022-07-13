# Crowdin Administration/es
{{TOCright}}

## Roles

-   Traductor
    -   Abilidad para sugerir y votar traducciones en un idioma.
    -   Preguntar por más contexto; preguntar para más claridad; reportar errores en la cadena a traducir; disputa una entrada de traducción actual, etc\...

-   Corrector de textos
    -   Gestiona las traducciones que los traductores sugieren y/o votan. El corrector de textos luego acepta/rechaza la traducción.
    -   Se necesita un paso adicional para dar también la aprobación final de la cadena de traducción. Debido a que \'aprobar\' una traducción requiere leerla nuevamente y marcarla, proporciona un tipo de capa de \'garantía de calidad\'. Una vez que se aprueba una traducción, marcará la cadena verde y agregará más progreso a la barra de estado verde del idioma que se traduce. La barra de progreso verde puede indicar la \'salud\' del idioma que se traduce. También permite una flexibilidad adicional para que los desarrolladores fusionen las traducciones que solo se han aprobado.
    -   Aborda las cuestiones de los traductores dentro de la interfaz de Crowdin. Por ejemplo, si se necesita más contexto; o si hay un error en la cadena que se traduce, o una traducción que fue aceptada o aprobada es disputada, etc.
    -   Informa a los desarrolladores cualquier problema relevante que requiera cambios en el código fuente, etc.

## Filtrando cadenas 

<img alt="" src=images/Crowdin_Filter_Strings.png  style="width   *500px;">

Filtrar cadenas es una característica útil para correctores y gerentes. Le da a la persona la capacidad de clasificar de manera efectiva muchas cadenas de traducción para, por ejemplo, mostrar solo cadenas que se han marcado como \'falta más información contextual\' o \'cadena fuente incorrecta\'. Este servicio que los traductores están haciendo para FreeCAD proporciona una capa adicional de pruebas de control de calidad. Muchos errores tipográficos, problemas gramaticales e incluso bugs pueden ser expuestos mediante la verificación de las cadenas de traducción. Y así, los usuarios marcan estas dichas cuerdas problemáticas para que podamos responder y, finalmente, \'resolver\'.

## Atajos de teclado 

<img alt="" src=images/Crowdin_keyboard_shortcuts.png  style="width   *300px;">

Usar atajos de teclado es una gran tip de eficiencia y ahorra mucho tiempo. Vale la pena aprender si eres un traductor, corrector de pruebas o gerente. Es posible ver la lista de atajos de teclado presionando el icono del teclado en la parte superior derecha de la interfaz de usuario de Crowdin.

**Nota importante   *** Tenga en cuenta no introducir errores en las cadenas de traducción producidas por teclas presionadas que estaban destinados a ser un atajo de teclado.

**Atajos de teclado usados frecuentemente   ***

-   Copiar fuente de traducción   * **Alt**+**C**
-   Guardar traducción   * **Ctrl**+**Enter**
-   Aprovar traducción   * **Alt**+**L** (relevante para correctores)

## Corregir problemas con la traducción 

Si nota una cadena en la interfaz de usuario de FreeCAD que no ha sido traducida realice lo siguiente   *

1.  Si no está seguro de a que entorno de trabajo pertenece la cadena, primero localícela en el código fuente de FreeCAD. En Linux puede usar {{Incode|grep -r "English text" *}}.
2.  Por ejemplo, si la cadena es {{Incode|"Solver Calculix Standard"}} encontrará este archivo   * **src/Mod/Fem/femcommands/commands.py**, y podrá saber que la cadena pertenece al entorno de trabajo FEM.
3.  Ahora busque esta cadena en Crowdin. Si tu idioma es Español visita <https   *//crowdin.com/project/freecad/es>, vaya al entorno de trabajo FEM, y vea si s encuentra ahí y si está traducida.
4.  Hay dos posibilidades   *
    1.  La cadena no está en Crowdin porque no ha sido recolectada por el script que recolecta cadenas de el código fuente de FreeCAD y las empaca en archivos **.ts**. Puede haber dos razones para esto   *
        -   La cadena no está siendo manejada correctamente por el código {{Incode|translate()}} (o {{Incode|QT_TRANSLATE_NOOP()}} código para casos especiales como nombres de comandos), que significa que hay un problema que debe de ser corregido en el código fuente.
        -   Todo parece normal, pero el script de recolección tiene u problema con una cadena en específico, que puede pasar porque tiene muchos errores (bugs).
    2.  La cadena está en Crowdin. Hay muchas posibilidades   *
        -   Puede ser que las últimas cadenas de Crowdin no han sido agregadas. Puede revisar si es el caso buscando la cadena (vea arriba), y revisar si aparece en los archivos **.ts** traducidos. En nuestro ejemplo {{Incode|"Solver Calculix Standard"}} sería encontrada en **src/Mod/Fem/Gui/Resources/translations/Fem_es.ts**. Esto indica que la cadena traducida está en el código fuente de FreeCAD y todo debería de estar bien en la siguiente build.
        -   Si aún falta la cadena en la suiguiente build el problema es más complejo y necesitamos hacer un depurado   *
            1.  Verifique en el archivo fuente si la cadena original es majada por {{Incode|translate()}} o por {{Incode|QT_TRANSLATE_NOOP()}}.
            2.  Verifique que el contecto coincida con el de Crowdin.
            3.  En el caso de {{Incode|QT_TRANSLATE_NOOP()}}, hay muchos casos particulares. Para comandos, el contexto debe ser el nombre del comando exacto, lo mismo que se usa en {{Incode|FreeCADGui.runCommand()}}. Para propiedades debe ser {{Incode|"App   *   *Property"}}. Para los nombres de los menús y barras de herramientas debe de ser {{Incode|"Workbench"}}.

## Enlaces

-   [Localización](Localisation/es.md)
-   [Scripts de Crowdin](Crowdin_Scripts/es.md)
-   [Proceso de lanzamiento](Release_process.md)




[Category   *Administration](Category_Administration.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Administration](Category_Administration.md) > Crowdin Administration/es
