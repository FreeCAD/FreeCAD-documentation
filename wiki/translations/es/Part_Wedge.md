---
- GuiCommand:/es   Name:Part Wedge   Name/es:Part Wedge   MenuLocation:Part -> [|Workbenches:[[Part_Workbench/es   Part](Part_CreatePrimitives/es___Part_CreatePrimitives]]_->_Cuña.md)|SeeAlso:[Part CreatePrimitives](Part_CreatePrimitives/es.md)---


</div>

## Description

Crea un objeto paramétrico Cuña. Esta Cuña se predetermina a un cuadrado más grande como base y un cuadrado más pequeño arriba.

## Usage

### Default Size and Placement {#default_size_and_placement}

**Placement:** The default orientation places the base in the XZ plane and the top outward in the Y axis direction. The default base corner is the 0,0,0 origin.

**Base Face:**

-   X : 10 mm
-   Z : 10 mm

**Height:**

-   Y : 0-10 mm

**Top Face:**

-   X : 2-8 mm
-   Z : 2-8 mm

![](images/PartWedgeProperty.png ) 

### Parametric Inputs {#parametric_inputs}

+------------------------------------------------------------------+----------------------------------------------------+
| ![](images/PartWedgeProperty_Inputs.png ) | Using the default placement, the below inputs are: |
|                                                                  |                                                    |
|                                                                  | -                                   |
|                                                                  |     **X min/max**                     |
|                                                                  |                                                 |
|                                                                  |     : Base face X axis span                        |
|                                                                  |                                                    |
|                                                                  | -                                   |
|                                                                  |     **Y min/max**                     |
|                                                                  |                                                 |
|                                                                  |     : Wedge height span                            |
|                                                                  |                                                    |
|                                                                  | -                                   |
|                                                                  |     **Z min/max**                     |
|                                                                  |                                                 |
|                                                                  |     : Base face Z axis span                        |
|                                                                  |                                                    |
|                                                                  | -                                   |
|                                                                  |     **X2 min/max**                    |
|                                                                  |                                                 |
|                                                                  |     : Top face X axis span                         |
|                                                                  |                                                    |
|                                                                  | -                                   |
|                                                                  |     **Z2 min/max**                    |
|                                                                  |                                                 |
|                                                                  |     : Top face Z axis span                         |
+------------------------------------------------------------------+----------------------------------------------------+

### More examples for wedges {#more_examples_for_wedges}

![](images/Wedge_examples.png )





 
