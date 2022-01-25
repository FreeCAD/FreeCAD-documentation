---
- GuiCommand:Addon/es
   Name:BIM Library
   Name/es:BIM Library
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench/es.md)
   Addon:BIM
   MenuLocation:3D Modeling → Library
   SeeAlso:[Arch Equipment](Arch_Equipment/es.md)
---

# BIM Library/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta de biblioteca le permite colocar, en el modelo actual, un objeto de la [FreeCAD Parts Library](Parts_Library.md), que debe instalarse a través del [Addon Manager](Std_AddonMgr.md) para que esta herramienta esté disponible.


</div>

<img alt="" src=images/BIM_Library_screenshot.png  style="width:800px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/BIM_Library_screenshot.png  style="width:800px;">


</div>


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Presione el botón **<img src="images/BIM_Library.png" width=16px> '''BIM Library'''
**
2.  Haga clic en un archivo de la biblioteca
3.  Haga doble clic en él o presione el botón **Insert**
4.  Haga clic en un punto en la vista 3D o ingrese una coordenada manualmente para colocar el objeto


</div>

## Opciones


<div class="mw-translate-fuzzy">

-   Los archivos FCStd, STEP y BREP son compatibles. Sólo los archivos STEP y BREP son colocables. Los archivos FCStd no le permitirán elegir una ubicación, ya que podrían estar compuestos por una serie compleja de objetos con posiciones significativas. Al elegir un archivo FCStd, su contenido se insertará en la posición que se define en el archivo.
-   Los objetos PASO y BREP se insertan como [Equipments](Arch_Equipment.md) sin forma de base separada. Agregar una forma de base a estos objetos después destruirá su forma actual.
-   Al colocar un objeto, puede elegir su punto de inserción entre el original (el (0,0,0) punto definido en el archivo), superior, medio, inferior e izquierdo, central y derecho.


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [BIM](Category_BIM.md) > [Arch](Category_Arch.md) > BIM Library/es
