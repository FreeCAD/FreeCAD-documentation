---
- GuiCommand:/es
   Name:Arch Component
‏‎‏‎   Name/es:Arch Componente
‏‎‏‎   MenuLocation:Arch → Utilities → Component
   Workbenches:[Arch](Arch_Workbench/es.md)
   Shortcut:**C** **M**
   SeeAlso:
---

# Arch Component/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

Crea un componente no paramétrico [ Arch](Arch_Workbench/es.md) de cualquier objeto [ Pieza](Part_Workbench/es.md). Esto le da al objeto basado en una Pieza los mismos atributos y propiedades que otros objetos Arch, y permite especificar cómo se debe exportar a IFC estableciendo su propiedad **Rol**.


</div>


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Seleccione un objeto basado en [ Part](Part_Workbench/es.md)
2.  Seleccione el menú Arch → Utilidades → {{KEY | <img src="images/_Arch_Component.png_" width= 16px> [ Componente](Arch_Component/es_.md)}}


</div>

## Propiedades de componentes Arch comunes 


<div class="mw-translate-fuzzy">

El objeto del Arch componente es también una base compartida por todos los demás Arch objetos ([ Muro](Arch_Wall/es.md), [ Estructura](Arch_Structure/es.md), etc.). Por lo tanto, algunas de sus propiedades y comportamientos son comunes a todos los objetos Arch (excepto las herramientas que no producen objetos sólidos, como [ Plano de sección](Arch_SectionPlane/es.md) o [ Eje](Arch_Axis/es.md)):


</div>


<div class="mw-translate-fuzzy">

-   **Forma de la base**: los componentes de Arch se basan siempre en un objeto base [ Forma](Part_Workbench/es.md). Algunos tipos de objetos de Arch simplemente usarán la forma de Base tal como está, otros (por ejemplo [ Wall](Arch_Wall/es.md)) realizarán algunas operaciones adicionales en él, como una extrusión. Para algunos tipos, tener un objeto base no es obligatorio ([ Estructura](Arch_Structure/es.md))


</div>


<div class="mw-translate-fuzzy">

-   **Adiciones**: los componentes de Arch tienen una propiedad de adición, que puede contener referencia a cualquier cantidad de otros objetos basados en [ Forma](Part_Workbench/es.md). La forma de estas adiciones se unirá con la forma de base del componente, para producir la forma final.


</div>


<div class="mw-translate-fuzzy">

-   **Sustracciones**: los componentes de Arch tienen una propiedad de sustraccion, que puede contener referencia a cualquier cantidad de otros objetos basados en [ Forma](Part_Workbench/es.md). La forma de estos objetos se restará de la forma base del componente, para producir la forma final.


</div>


<div class="mw-translate-fuzzy">

-   La colocación del componente de Arch se aplica después de realizar las adiciones y sustracciones, por lo que se realizan contra el objeto base en su ubicación base. Luego, el resultado se mueve a la ubicación de la Locación.


</div>


<div class="mw-translate-fuzzy">

-   Los objetos pueden agregarse o eliminarse a / desde las listas de Adiciones y Subtracciones de un Componente seleccionando tanto el objeto como el componente, y usando los comandos [Arch Add](Arch_Add/es.md) o [Arch Remove](Arch_Remove/es.md) , o desde el panel de tareas haciendo doble clic en el Componente en la vista de árbol. El panel de tareas también permite verificar qué objeto es actualmente parte de estas listas.


</div>


<div class="mw-translate-fuzzy">

-   **Role**: Each Arch Component, besides the function defined by its type (wall, window, etc), also has a Role property, that can define further which kind of function it performs. For example, an [Structure](Arch_Structure.md) can have a beam o column role. Generic Arch Components (as produced by this command) can have any role available in the whole Arch workbench. The role is what is used to define the type of IFC object to export to when [exporting to IFC](Arch_IFC.md).


</div>


<div class="mw-translate-fuzzy">

-   **Clon de**: cualquier componente de Arch puede ser un clon de otro componente de Arch del mismo tipo (un muro solo puede ser un clon de otro muro, etc.). La única excepción es el Componente Arch genérico (como lo produce este comando), que puede clonarse de cualquier otro tipo (Muro, estructura, ventana, etc.). Esto permite usar un Componente Arch genérico para sobreescribir el tipo de otro.


</div>

-   **Description**: All Arch Components have a Description field, that can contain any text. This is used when [exporting to IFC](Arch_IFC.md).

-   **Etiqueta**: la propiedad Etiqueta es otro campo de texto, que se puede usar para dar una identidad personalizada adicional a los objetos.


<div class="mw-translate-fuzzy">

-   **Material**: todos los componentes de Arch tienen una ranura de material, que puede contener un [ Material](Arch_SetMaterial.md) o un [ MultiMaterial](Arch_MultiMaterial.md) (no todos los tipos de objetos Arch admiten el uso MutiMateriales). Las propiedades DiffuseColor y Transparencia del material adjunto definirán el color de la forma y la transparencia del componente Arch. El material se importará y exportará a [ IFC](Arch_IFC.md), [ OBJ](Arch_OBJ.md) y [ DAE](Arch_DAE.md).


</div>


<div class="mw-translate-fuzzy">

-   **Move with Host**: cuando un componente está incrustado en otro (como una ventana dentro de un muro), al establecer esta propiedad en Verdadero, el objeto se mueve o gira con su objeto host cuando se mueve el objeto host o girado con los controles Mover o Girar borrador.


</div>


<div class="mw-translate-fuzzy">

-   **Hi Res**: Arch Components puede usar la forma de otro objeto como una versión de mayor resolución de ellos mismos. Para esto, se deben configurar tanto la propiedad de alta resolución como el modo de visualización de alta resolución. Esto permite, por ejemplo, hacer un muro simple y luego modelar cada ladrillo que compone el muro, por ejemplo con [ Part Box](Part_Box.md). Luego, usa un compond de esos ladrillos como una versión de alta resolución de la pared. La forma de la pared no se modifica agregando un objeto de alta resolución. Solo su representación en la vista 3D cambiará al adoptar la representación de la versión de alta resolución en lugar de la propia.


</div>

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Component/es
