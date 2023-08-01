---
- GuiCommand:
   Name:PartDesign Sprocket
   Name/es:DiseñoPieza Rueda Dentada
   MenuLocation:DiseñoPieza → Rueda Dentada...
   Workbenches:[DiseñoPieza](PartDesign_Workbench/es.md)
   Version:0.19
---

# PartDesign Sprocket/es

## Description

## Descripción

Esta herramienta permite crear un perfil 2D de una rueda dentada. Se puede acolchado con la función [DiseñoPieza Pastilla](PartDesign_Pad/es.md).

## Usage

## Uso

1.  Ir al menú **DiseñoPieza → [<img src=images/PartDesign_Sprocket.svg style="width:24px"> Rueda dentada...**.
2.  Establezca la **Número de dientes** y la **Referencia de la rueda dentada**.
3.  Haga clic en **Aceptar**
4.  Si la rueda dentada se crea fuera del cuerpo activo, arrástrela y suéltela en un cuerpo para aplicar otras características como el acolchado.

## Propiedades

-    **Número de dientes**: Número de dientes

-    **Referencia del rueda**: El tipo de rueda. Una lista de definiciones de ruedas. {{Version/es|0.20}} La lista incluye las normas ANSI e ISO, así como algunas definiciones de ruedas para bicicletas y motocicletas.

-    **Paso**: Distancia entre dos dientes

-    **Diámetro de los rodillos**: Diámetro de los rodillos de la cadena para los que está diseñado el rueda.

-    **Grosor**: El grosor principal del rueda. **Nota:** El rueda no puede limitarse a rellenar este grosor porque los dientes tienen chaflanes laterales. Por lo tanto, mira la definición de la rueda dentada para modelar una rueda dentada 3D válida. {{Version/es|0.20}}





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Sprocket/es
