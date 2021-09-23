---
- GuiCommand:/es
   Name:PartDesign InvoluteGear
   Name/es:DiseñoPiezas EngranajeEvolvente
   MenuLocation:DiseñoPiezas → Engranaje Evolvente...
   Workbenches:[DiseñoPiezas](PartDesign_Workbench/es.md)
   SeeAlso:[Ambiente de trabajo FCEngranaje](FCGear_Workbench/es.md)
---

# PartDesign InvoluteGear/es

## Descripción

Esta herramienta permite crear un perfil 2D de un engranaje evolvente. Este perfil 2D es totalmente paramétrico, y puede ser rellenado con la función [DiseñoPiezas Pad](PartDesign_Pad/es.md).
Para una información más detallada ver las entradas de Wikipedia para: [Gear](https://en.wikipedia.org/wiki/Gear) y [Involute Gear](https://en.wikipedia.org/wiki/Involute_gear)

![](images/PartDesign_Involute_Gear_01.png ) 

## Uso

1.  Ir al menú **DiseñoPiezas → <img src=images/PartDesign_InternalExternalGear.svg style="width:24px"> Engranaje evolvente...**.
2.  Establezca los parámetros de evolvente.
3.  Haga clic en **OK**
4.  El engranaje evolvente se crea fuera del cuerpo activo. Arrastre y suéltelo en un cuerpo para la aplicación de otras características como el relleno.

## Parámetros

-   Número de dientes: Establece el número de dientes.

-   Módulos: Diámetro del paso dividido por el número de dientes.

-   Ángulo de presión: Ángulo agudo entre la línea de acción y una normal a la línea que une los centros de los engranajes. Por defecto es de 20 grados. ([Más información](http://en.wikipedia.org/wiki/Involute_gear))

-   Alta precisión: Verdadero o falso

-   Engranaje externo: Verdadero o falso

## Relacionados

-   [FCGear Ambiente de trabajo](FCGear_Workbench/es.md)





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign InvoluteGear/es
