 {{TOCright}}

## Importar

### Elementos soportados 

-   primitivas: cubo, esfera, cilindro, cuadrado, circunferencia, polígono, poliedro
-   booleanas: unión, diferencia, intersección
-   extrusión lineal, revolución
-   importar (dxf, stl, off) (sin escalado o transformación del origen)
-   matriz múltiple
-   color

### Elementos no soportados 

-   proyección
-   superficie
-   render (ignorado)
-   operaciones en general: minkowski, deslizar, ruta, subdivisión, cáscara

## Exportar

### Elementos soportados 

-   primitivas: Caja, cilindro, Cono, Toro
-   booleanas: corte, fusión, común

### Recursos

Todo objeto derivado de Part::Feature que aún no es soportado será mallado y exportado como un elemento poliédrico

## Related

-   [OpenSCAD Workbench](OpenSCAD_Workbench.md)
-   [Import Export](Import_Export.md)
-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)


 {{OpenSCAD Tools navi}}

[Category:File\_Formats{{\#translation:}}](Category:File_Formats.md)
