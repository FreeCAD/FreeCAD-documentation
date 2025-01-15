---
 GuiCommand:
   Name: Arch Project
   Name/es: Arquitectura Proyecto
   MenuLocation: Arquitectura , Proyecto
   Workbenches: Arch_Workbench/es
   Shortcut: **P** **O**
   SeeAlso: Arch_Site/es, Arch_Building/es
---

# Arch Project/es


</div>



## Descripción

El Arquitectura Proyecto es un objeto especial adecuado para añadir una mejor compatibilidad con los archivos [IFC](Arch_IFC/es.md). Cada archivo IFC debe contener una entidad [IfcProject](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_1/FINAL/HTML/schema/ifckernel/lexical/ifcproject.htm). El IfcProject se utiliza sobre todo para definir la configuración general del proyecto, como los sistemas de proyección, para la compatibilidad con los SIG, o los sistemas de unidades.

Al exportar un modelo de FreeCAD al formato de archivo IFC, si tu modelo no contiene ningún objeto de Proyecto, se creará automáticamente uno por defecto, que en la mayoría de los casos será suficiente. Sin embargo, es posible que desees poder ajustar la configuración del proyecto, en cuyo caso puede ser útil añadir un objeto de proyecto. Al importar un archivo IFC, siempre se creará un objeto de proyecto. Sin embargo, si no lo utiliza específicamente, puede simplemente eliminarlo después de la importación.

Tenga en cuenta que, aunque se puede añadir cualquier otro objeto BIM a un proyecto, algo que el estándar IFC no prohíbe, lo habitual es tener siempre sólo [Sitios](Arch_Site/es.md) o [edificios](Arch_Building/es.md) como hijos directos de un proyecto. Todos los demás objetos BIM deben estar dentro de estos sitios o edificios. El proyecto en sí debe estar siempre en la parte superior de la estructura de su modelo, es decir, no debe estar incluido en ningún otro objeto.



## Utilización

1.  Pulse el **<img src="images/Arch_Project.svg" width=16px> [Arquitectura Proyecto](Arch_Project/es.md)**, o pulse las teclas **P** y luego **O**.
2.  Añade cualquier objeto a tu proyecto arrastrándolo y soltándolo sobre el proyecto en la [Vista de árbol](Tree_view/es.md).


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Project/es
