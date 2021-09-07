
{{UnfinishedDocu

}}  Esta página da una visión general de cómo las diferentes herramientas y conceptos que se encuentran en otras aplicaciones BIM convencionales se comparan con FreeCAD, específicamente su [BIM ambiente de trabajo](BIM_Workbench/es.md).

**HACER:** Añadir otras aplicaciones BIM: Allplan, Tekla, Vectorworks, BricsCAD, ¿qué más?

                                                           FreeCAD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Revit                                                                                                                                                                                                                              ArchiCAD
  -------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Precio y licencia**                                    Uso gratuito para cualquier persona, sin necesidad de registrarse.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Gratuito para los estudiantes previa inscripción, se necesita inscripción y pago para los demás usuarios                                                                                                                           Registro y pago
  **Formato de archivo estándar y versiones**              Los archivos de FreeCAD por defecto utilizan la extensión **.FCStd**. Puede ser abierto por FreeCAD y Blender (usando un plugin), pero también puede ser [unzipped](Fcstd_file_format.md). Cualquier archivo de FreeCAD, creado en cualquier versión, se abrirá en cualquier otra versión, más nueva o más antigua. Sin embargo, algunos objetos complejos creados con una versión más reciente pueden no ser editables cuando se abren en versiones más antiguas.                                                                                                                                                             Los archivos de Revit utilizan por defecto la extensión **.rvt**. Sólo se pueden abrir con Revit. Los archivos creados con cualquier versión anterior se abrirán. Los archivos creados con una versión más reciente no lo harán.   Los archivos de ArchiCAD utilizan por defecto la extensión **.pln**. Sólo se pueden abrir con ArchiCAD. Los archivos creados con cualquier versión anterior se abrirán. Los archivos creados con una versión más reciente no lo harán.
  **Intercambio de modelos y formatos de datos BIM**       [IFC](https://es.wikipedia.org/wiki/Industry_Foundation_Classes), [DXF](https://es.wikipedia.org/wiki/DXF) (sólo en 2D), [DWG](https://es.wikipedia.org/wiki/DWG) (sólo en 2D), [ACIS/SAT](https://es.wikipedia.org/wiki/ACIS) (Utilizando el complemento CadExchanger o InventoLoader), [STEP](https://en.wikipedia.org/wiki/ISO_10303-21)                                                                                                                                                                                                                                                                                            [IFC](https://es.wikipedia.org/wiki/Industry_Foundation_Classes), [DXF](https://es.wikipedia.org/wiki/AutoCAD_DXF), [DWG](https://es.wikipedia.org/wiki/.dwg), [ACIS/SAT](https://es.wikipedia.org/wiki/ACIS)                      [IFC](https://es.wikipedia.org/wiki/Industry_Foundation_Classes), [DXF](https://es.wikipedia.org/wiki/AutoCAD_DXF), [DWG](https://es.wikipedia.org/wiki/.dwg)
  **Creación de unidades de proyecto**                     En FreeCAD, todos los modelos aceptan cualquier unidad. La unidad con la que prefieres trabajar se puede establecer en el menú **Edición -\> Preferencias -\> General -\> Unidades**. Cambiar la unidad no afecta al modelo.                                                                                                                                                                                                                                                                                                                                                                                                           Seleccione el modelo correcto (Métrico o Imperial), luego modifique el aspecto de la unidad en el menú **Gestionar -\> Proyecto**. Cambiar la unidad no afecta al modelo.                                                          Seleccione la plantilla correcta, luego establezca la unidad en el menú **Opciones -\> Preferencias del proyecto -\> Unidades de trabajo**. El cambio de la unidad afecta al modelo.
  **Organizar los elementos de su proyecto**               Puedes usar [Sitios](Arch_Site/es.md), [Edificios](Arch_Building/es.md) y [contruir edificios](Arch_BuildingPart/es.md) (pisos/niveles), o el estándar [grupos](Std_Group/es.md) para agrupar y organizar objetos, y otros bancos de trabajo de FreeCAD ofrecen opciones adicionales de agrupación. Las partes del edificio pueden activarse haciendo doble clic en ellas, lo que automáticamente añade los siguientes objetos.                                                                                                                                                                        Los objetos se organizan automáticamente en planos de planta. También se pueden agrupar los objetos en Grupos.                                                                                                                     Los objetos se organizan automáticamente en planos de planta. Los objetos se organizan automáticamente en planos de planta.
  **Familias de objetos**                                  No existe el concepto de familia en FreeCAD. La misma idea se consigue mediante [clonación](Draft_Clone/es.md) de otro objeto, en cuyo caso adopta su forma y todas sus propiedades, o construyendo otro objeto similar como un [muro](Arch_Wall/es.md) o [estructura (columna, viga)](Arch_Structure/es.md) sobre el mismo perfil base, en cuyo caso el perfil es común pero el resto de propiedades (altura, etc) son independientes. La composición de los muros depende del [multimaterial](Arch_MultiMaterial/es.md) utilizado, que también puede ser compartido por varias instancias de muro.   Cada objeto pertenece a una familia determinada.                                                                                                                                                                                   Cada objeto pertenece a un tipo determinado.
  **Agrupación de objetos en componentes reutilizables**   Los grupos de FreeCAD no pueden ser instanciados (copias independientes), pero los objetos agrupados en [compuestos](Part_Compound/es.md) o [partes de edificios](Arch_BuildingPart.md) pueden ser clonados (copias dependientes) o copiados (copias independientes).                                                                                                                                                                                                                                                                                                                                                  Los grupos de Revit pueden ser instanciados (copias dependientes).                                                                                                                                                                 Los grupos de ArchiCAD no pueden ser instanciados (copias independientes).
  **Elementos BIM estándar**                               Paredes, estructuras (vigas, columnas y forjados), ventanas (puertas y ventanas), techos, escaleras, armazones (barandillas), componentes (muebles, aparatos, etc.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Paredes, vigas, columnas, pisos, techos, ventanas, puertas, techos, escaleras, barandas, componentes (muebles, aparatos, etc)                                                                                                      Paredes, vigas, columnas, forjados, ventanas, puertas, techos, escaleras, barandillas, muros cortina, objetos (muebles, electrodomésticos, etc)

[Category:BIM{{\#translation:}}](Category:BIM.md)