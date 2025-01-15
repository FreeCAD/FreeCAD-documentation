# <img alt="Fasteners Workbench icon" src=images/Fasteners_workbench_icon.svg  style="width:64px;"> Fasteners Workbench/es






## Introducción

El <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Entorno de trabajo Elementos de sujeción](Fasteners_Workbench.md) es un [entorno de trabajo externo](External_workbenches.md) que puede agregar varios elementos de sujeción a partes.

<img alt="" src=images/Fasteners_Toolbars.png  style="width:500px;"> 
*El diseño de barra de herramientas única opcional del banco de trabajo.<br>
 Los elementos de sujeción con dimensiones métricas tienen íconos naranjas.<br>
 Los elementos de sujeción con dimensiones en pulgadas tienen íconos verdes.*



## Instalación

1.  Instale el entorno de trabajo Fasteners a través del <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Administrador de complementos](Std_AddonMgr/es.md). Para la instalación manual, consulte [Instalación de más entornos de trabajo](Installing_more_workbenches/es.md).
2.  Reinicie FreeCAD.
3.  Seleccione <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Elementos de sujeción](Fasteners_Workbench/es.md) de la [lista desplegable de entornos de trabajo](Std_Workbench/es.md).
4.  Opcionalmente, cambie la barra de herramientas y el diseño del menú:
    1.  Vaya a: **Editar → Preferencias... → Elementos de sujeción → Configuración general**.
    2.  Seleccione una de las opciones disponibles de **Agrupación de iconos de tornillos de barra de herramientas**:
        -   
            **Ninguno**
            
            : todos los sujetadores aparecen en una sola barra de herramientas. Para ver todos los botones disponibles, utilice el botón **>>** para expandirlo.

        -   
            **Barras de herramientas separadas**
            
            : los sujetadores se agrupan en varias barras de herramientas. Este es el diseño predeterminado.

        -   
            **Botones desplegables**
            
            : los sujetadores se agrupan en barras de herramientas con menús laterales.
    3.  Opcionalmente, desmarque una o más opciones de **Estándares de fijación mostrados en las barras de herramientas**. Los estándares no verificados todavía están disponibles en el menú.
    4.  Reinicie FreeCAD.



## Uso

Fasteners can be attached or unattached. Attached fasteners have a **Base Object**, a circular edge, and their **Placement** is dynamically linked to that object. The <img alt="" src=images/Fasteners_Move.svg  style="width:16px;"> [Fasteners Move](Fasteners_Move.md) command can be used to attach or detach a fastener.

### Unattached fasteners 

1.  Select the desired fastener by clicking its button or by picking it from the menu.
2.  A fastener is created at the origin.
3.  Optionally change the dimensions and other properties of the fastener:
    1.  Select the fastener.
    2.  Go to the **Data** tab of the [Property editor](Property_editor.md).
    3.  Change the required properties.

### Attached fasteners 

<img alt="" src=images/Fasteners_Attached_Selected.png  style="width:200px;"> <img alt="" src=images/Fasteners_Attached_Created.png  style="width:200px;"> 
*On the left two selected circular edges. On the right the attached fasteners.*

1.  Specify if the selected holes are tap holes or pass holes by selecting <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:16px;"> [Fasteners MatchTypeInner](Fasteners_MatchTypeInner.md) or <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:16px;"> [Fasteners MatchTypeOuter](Fasteners_MatchTypeOuter.md) respectively (not used for countersunk screws).
2.  Select one or more circular edges and/or faces with circular edges. For countersunk screws the top edge of the chamfered hole must be selected.
3.  Select the desired fastener by clicking its button or by picking it from the menu.
4.  A fastener is attached to each of the selected circular edges.
5.  The default dimensions of each fastener depend on the radius of the circular edge it is attached to. Countersunk screws are matched by their head diameter, other fasteners are matched by their shaft diameter.
6.  Optionally change the dimensions and other properties of the fasteners. See above.
7.  Fasteners that appear upside-down can be inverted with the <img alt="" src=images/Fasteners_Flip.svg  style="width:16px;"> [Fasteners Flip](Fasteners_Flip.md) command or by changing their **Invert** property.
8.  Optionally change the **Offset** property to create space between the fasteners and the edges they are attached to.



## Notas

-   To generate threads, the **Thread** property of a fastener must be changed to `True`. Generating threads is costly. Recomputes take much longer if there are many fasteners with threads in a document.
-   The **Invert** property and the **Offset** property are ignored for unattached fasteners.



### Commandos

-   <img alt="" src=images/Fasteners_Flip.svg  style="width:32px;"> [Invert fastener](Fasteners_Flip.md): Invert the orientation of attached fasteners.

-   <img alt="" src=images/Fasteners_Move.svg  style="width:32px;"> [Move fastener](Fasteners_Move.md): Move and attach a fastener to a circular edge. Can also be used to detach a fastener.

-   <img alt="" src=images/Fasteners_Simplify.svg  style="width:32px;"> [Simplify shape](Fasteners_Simplify.md): Create non-parametric copies of fasteners.

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:32px;"> [Match for tap hole](Fasteners_MatchTypeInner.md): Consider circular edges to be tap holes when new fasteners are attached to them.

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:32px;"> [Match for pass hole](Fasteners_MatchTypeOuter.md): Consider circular edges to be pass holes when new fasteners are attached to them.

-   <img alt="" src=images/Fasteners_BOM.svg  style="width:32px;"> [Generate BOM](Fasteners_BOM.md): Create a spreadsheet with a bill of materials for the fasteners in the document.

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:32px;"> [Screw calculator](Fasteners_ScrewCalculator.md): Show a calculator to determine the tap hole size of screws.

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width:32px;"> [Change fastener parameters](Fasteners_ChangeParameters.md): Change the parameters of fasteners.



## Elementos de sujeción 

Los elementos de sujeción con dimensiones métricas tienen íconos naranjas. Los elementos de sujeción con dimensiones en pulgadas tienen íconos verdes.

### Hexagon head screws and bolts 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width:32px;"> **ASME B18.2.1.6** UNC hexagon head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width:32px;"> **ASME B18.2.1.8** UNC hexagon head screw with flange.

-   <img alt="" src=images/Fasteners_DIN571.svg  style="width:32px;"> **DIN 571** Hexagon head wood screw.

-   <img alt="" src=images/Fasteners_DIN933.svg  style="width:32px;"> **DIN 933** Hexagon head screw.

-   <img alt="" src=images/Fasteners_DIN961.svg  style="width:32px;"> **DIN 961** Hexagon head screw.

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width:32px;"> **EN 1662** Hexagon head bolt with flange, small series.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width:32px;"> **EN 1665** Hexagon head bolt with flange, heavy series.

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width:32px;"> 
**ISO 4014** Hexagon head bolt. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO4015.svg  style="width:32px;"> **ISO 4015** Hexagon head bolt with reduced shank.

-   <img alt="" src=images/Fasteners_ISO4016.svg  style="width:32px;"> 
**ISO 4016** Hexagon head bolt. *Product grade C.*

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width:32px;"> 
**ISO 4017** Hexagon head screw. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO4018.svg  style="width:32px;"> 
**ISO 4018** Hexagon head screw. *Product grade C.*

-   <img alt="" src=images/Fasteners_ISO4162.svg  style="width:32px;"> 
**ISO 4162** Hexagon bolt with flange, small series. *Product grade A with driving feature of product grade B.*

-   <img alt="" src=images/Fasteners_ISO8676.svg  style="width:32px;"> 
**ISO 8676** Hexagon head screw with fine pitch thread. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO8765.svg  style="width:32px;"> **ISO 8765** Hexagon head bolt with fine pitch thread.

-   <img alt="" src=images/Fasteners_ISO15071.svg  style="width:32px;"> 
**ISO 15071** Hexagon bolt with flange, small series. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO15072.svg  style="width:32px;"> 
**ISO 15072** Hexagon bolt with flange and fine pitch thread, small series. *Product grade A.*

### Hexagon socket screws 

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width:32px;"> **ASME B18.3.1A** UNC hexagon socket head cap screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1G.svg  style="width:32px;"> **ASME B18.3.1G** UNC hexagon socket head cap screw with low head.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width:32px;"> **ASME B18.3.2** UNC hexagon socket countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width:32px;"> **ASME B18.3.3A** UNC hexagon socket button head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width:32px;"> **ASME B18.3.3B** UNC hexagon socket button head screw with flange.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width:32px;"> **ASME B18.3.4** UNC hexagon socket head shoulder screw.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width:32px;"> **DIN 6912** Hexagon socket head cap screw with low head with center.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width:32px;"> **DIN 7984** Hexagon socket head cap screw with low head.

-   <img alt="" src=images/Fasteners_ISO2936.svg  style="width:32px;"> **ISO 2936** Hexagon socket screw key.

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width:32px;"> **ISO 4762** Hexagon socket head cap screw.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width:32px;"> **ISO 7379** Hexagon socket head shoulder screw.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width:32px;"> **ISO 7380-1** Hexagon socket button head screw.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width:32px;"> **ISO 7380-2** Hexagon socket button head screw with flange.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width:32px;"> **ISO 10642** Hexagon socket countersunk head screw.

### Hexalobular socket head screws 

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width:32px;"> **ISO 14579** Hexalobular socket head cap screw.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width:32px;"> **ISO 14580** Hexalobular socket cheese head screw.

-   <img alt="" src=images/Fasteners_ISO14581.svg  style="width:32px;"> **ISO 14581** Hexalobular socket countersunk flat head screw.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width:32px;"> **ISO 14582** Hexalobular socket countersunk head screw, high head.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width:32px;"> **ISO 14583** Hexalobular socket pan head screw.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width:32px;"> **ISO 14584** Hexalobular socket raised countersunk head screw.

### Slotted head screws 

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.2.svg  style="width:32px;"> **ASME B18.6.1.2** Slotted flat countersunk head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.4.svg  style="width:32px;"> **ASME B18.6.1.4** Slotted oval countersunk head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width:32px;"> **ASME B18.6.3.1A** UNC slotted countersunk flat head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.4A.svg  style="width:32px;"> **ASME B18.6.3.4A** UNC slotted oval countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.9A.svg  style="width:32px;"> **ASME B18.6.3.9A** UNC slotted pan head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.10A.svg  style="width:32px;"> **ASME B18.6.3.10A** UNC Slotted fillister head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.12A.svg  style="width:32px;"> **ASME B18.6.3.12A** UNC Slotted truss head screws.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.16A.svg  style="width:32px;"> **ASME B18.6.3.16A** UNC Slotted round head screw.

-   <img alt="" src=images/Fasteners_DIN84.svg  style="width:32px;"> 
**DIN 84 (superseded by ISO 1207)** Slotted cheese head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_DIN96.svg  style="width:32px;"> **DIN 96** Slotted half round head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-1.svg  style="width:32px;"> **GOST 1144-1** Slotted half round head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-2.svg  style="width:32px;"> **GOST 1144-2** Slotted half round head wood screw.

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width:32px;"> 
**ISO 1207** Slotted cheese head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width:32px;"> 
**ISO 1580** Slotted pan head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width:32px;"> 
**ISO 2009** Slotted countersunk flat head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width:32px;"> 
**ISO 2010** Slotted raised countersunk head screw. *Product grade A.*

### H cross head screws 

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.3.svg  style="width:32px;"> **ASME B18.6.1.3** Flat countersunk head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.5.svg  style="width:32px;"> **ASME B18.6.1.5** Oval countersunk head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1B.svg  style="width:32px;"> **ASME B18.6.3.1B** UNC flat countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.4B.svg  style="width:32px;"> **ASME B18.6.3.4B** UNC oval countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.9B.svg  style="width:32px;"> **ASME B18.6.3.9B** UNC pan head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.10B.svg  style="width:32px;"> **ASME B18.6.3.10B** UNC fillister head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.12C.svg  style="width:32px;"> **ASME B18.6.3.12C** UNC truss head screws.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.16B.svg  style="width:32px;"> **ASME B18.6.3.16B** UNC round head screw.

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width:32px;"> **DIN 967** Pan head screw with collar.

-   <img alt="" src=images/Fasteners_DIN7996.svg  style="width:32px;"> **DIN 7996** Pan head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-3.svg  style="width:32px;"> **GOST 1144-3** Pan head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-4.svg  style="width:32px;"> **GOST 1144-4** Pan head wood screw.

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width:32px;"> 
**ISO 7045** Pan head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width:32px;"> 
**ISO 7046** Countersunk flat head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width:32px;"> 
**ISO 7047** Raised countersunk head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width:32px;"> **ISO 7048** Cheese head screw.

-   <img alt="" src=images/Fasteners_ISO7049-C.svg  style="width:32px;"> **ISO 7049-C** Pan head self tapping screws with conical point.

-   <img alt="" src=images/Fasteners_ISO7049-F.svg  style="width:32px;"> **ISO 7049-F** Pan head self tapping screws with flat point.

-   <img alt="" src=images/Fasteners_ISO7049-R.svg  style="width:32px;"> **ISO 7049-R** Pan head self tapping screws with rounded point.

### Other head bolts 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.1.svg  style="width:32px;"> **ASME B18.2.1.1** UNC square head bolt.

-   <img alt="" src=images/Fasteners_ASMEB18.5.2.svg  style="width:32px;"> **ASME B18.5** UNC Round head square neck bolt.

-   <img alt="" src=images/Fasteners_DIN478.svg  style="width:32px;"> **DIN 478** Square head bolt with collar.

-   <img alt="" src=images/Fasteners_DIN603.svg  style="width:32px;"> **DIN 603** Round head square neck bolt.

-   <img alt="" src=images/Fasteners_ISO2342.svg  style="width:32px;"> **ISO 2342** Headless screw with shank

### Set screws 

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width:32px;"> **ASME B18.3.5A** UNC hexagon socket set screw with flat point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width:32px;"> **ASME B18.3.5B** UNC hexagon socket set screw with cone point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width:32px;"> **ASME B18.3.5C** UNC hexagon socket set screw with dog point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width:32px;"> **ASME B18.3.5D** UNC hexagon socket set screw with cup point.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width:32px;"> **ISO 4026** Hexagon socket set screw with flat point.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width:32px;"> **ISO 4027** Hexagon socket set screw with cone point.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width:32px;"> **ISO 4028** Hexagon socket set screw with dog point.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width:32px;"> **ISO 4029** Hexagon socket set screw with cup point.

-   <img alt="" src=images/Fasteners_ISO4766.svg  style="width:32px;"> **ISO 4766** Slotted socket set screw with flat point.

-   <img alt="" src=images/Fasteners_ISO7434.svg  style="width:32px;"> **ISO 7434** Slotted socket set screw with cone point.

-   <img alt="" src=images/Fasteners_ISO7435.svg  style="width:32px;"> **ISO 7435** Slotted socket set screw with long dog point.

-   <img alt="" src=images/Fasteners_ISO7436.svg  style="width:32px;"> **ISO 7436** Slotted socket set screw with cup point.

### Thumb screws 

-   <img alt="" src=images/Fasteners_DIN464.svg  style="width:32px;"> **DIN 464** Knurled thumb screw, high type.

-   <img alt="" src=images/Fasteners_DIN465.svg  style="width:32px;"> **DIN 465** Slotted knurled thumb screw, high type.

-   <img alt="" src=images/Fasteners_DIN653.svg  style="width:32px;"> **DIN 653** Knurled thumb screw, low type.

### Nuts

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width:32px;"> **ASME B18.2.2.1A** UNC hexagon machine screw nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1B.svg  style="width:32px;"> **ASME B18.2.2.1B** UNC square machine screw nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.2.svg  style="width:32px;"> **ASME 18.2.2.2** UNC square nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width:32px;"> **ASME B18.2.2.4A** UNC hexagon nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width:32px;"> **ASME B18.2.2.4B** UNC hexagon thin nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.5.svg  style="width:32px;"> **ASME 18.2.2.5** UNC hexagon castle nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.12.svg  style="width:32px;"> **ASME 18.2.2.12** UNC hexagon nut with flange.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.13.svg  style="width:32px;"> **ASME 18.2.2.13** UNC hexagon coupling nut.

-   <img alt="" src=images/Fasteners_ASMEB18.6.9A.svg  style="width:32px;"> **ASME 18.6.9A** Wing nut, type A.

-   <img alt="" src=images/Fasteners_DIN315.svg  style="width:32px;"> **DIN 315** Wing nut.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width:32px;"> **DIN 557** Square nut.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width:32px;"> **DIN 562** Square nut.

-   <img alt="" src=images/Fasteners_DIN917.svg  style="width:32px;"> **DIN 917** Cap nut, low form.

-   <img alt="" src=images/Fasteners_DIN928.svg  style="width:32px;"> **DIN 928** Square weld nut.

-   <img alt="" src=images/Fasteners_DIN929.svg  style="width:32px;"> **DIN 929** Hexagon weld nut.

-   <img alt="" src=images/Fasteners_DIN934.svg  style="width:32px;"> 
**DIN 934 (superseded by ISO 4035 and ISO 8673)** Hexagon thin nut chamfered. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_DIN935.svg  style="width:32px;"> **DIN 935** Hexagon castle nut.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width:32px;"> **DIN 985** Nyloc nut.

-   <img alt="" src=images/Fasteners_DIN1587.svg  style="width:32px;"> **DIN 1587** Cap nut.

-   <img alt="" src=images/Fasteners_DIN6330.svg  style="width:32px;"> **DIN 6330** Hexagon nut 1.5d high.

-   <img alt="" src=images/Fasteners_DIN6331.svg  style="width:32px;"> **DIN 6331** Hexagon with collar 1.5d high.

-   <img alt="" src=images/Fasteners_DIN6334.svg  style="width:32px;"> **DIN 6334** Hexagon coupling nut.

-   <img alt="" src=images/Fasteners_DIN7967.svg  style="width:32px;"> **DIN 7967** Self-locking counter nut.

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width:32px;"> **EN 1661** Hexagon nut with flange.

-   <img alt="" src=images/Fasteners_GOST11860-1.svg  style="width:32px;"> **GOST 11860-1** Cap nut.

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width:32px;"> 
**ISO 4032** Hexagon nut, style 1. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width:32px;"> 
**ISO 4033** Hexagon high nut, style 2. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO4034.svg  style="width:32px;"> **ISO 4034** Hexagon nut, style 1.

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width:32px;"> 
**ISO 4035** Hexagon thin nut chamfered, style 0. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO4161.svg  style="width:32px;"> **ISO 4161** Hexagon nut with flange.

-   <img alt="" src=images/Fasteners_ISO7040.svg  style="width:32px;"> **ISO 7040** Prevailing torque type hexagon nut (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO7041.svg  style="width:32px;"> **ISO 7041** Prevailing torque type hexagon nut (with non-metallic insert), style 2.

-   <img alt="" src=images/Fasteners_ISO7043.svg  style="width:32px;"> **ISO 7043** Prevailing torque type hexagon nut with flange (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO7044.svg  style="width:32px;"> **ISO 7044** Prevailing torque type all-metal hexagon nut with flange.

-   <img alt="" src=images/Fasteners_ISO7719.svg  style="width:32px;"> **ISO 7719** Prevailing torque type all-metal hexagon nut.

-   <img alt="" src=images/Fasteners_ISO7720.svg  style="width:32px;"> **ISO 7720** Prevailing torque type all-metal hexagon nut, style 2.

-   <img alt="" src=images/Fasteners_ISO8673.svg  style="width:32px;"> 
**ISO 8673** Hexagon nut with fine pitch thread, style 1. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO8674.svg  style="width:32px;"> 
**ISO 8674** Hexagon high nut with fine pitch thread, style 2. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO8675.svg  style="width:32px;"> 
**ISO 8675** Hexagon thin nut with fine pitch thread, style 0. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO10511.svg  style="width:32px;"> **ISO 10511** Prevailing torque type hexagon thin nut (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO10512.svg  style="width:32px;"> **ISO 10512** Prevailing torque type hexagon nut with fine pitch thread (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO10513.svg  style="width:32px;"> **ISO 10513** Prevailing torque type all-metal hexagon nut with fine pitch thread.

-   <img alt="" src=images/Fasteners_ISO10663.svg  style="width:32px;"> **ISO 10663** Hexagon nut with flange and fine pitch thread.

-   <img alt="" src=images/Fasteners_ISO12125.svg  style="width:32px;"> **ISO 12125** Prevailing torque type hexagon nut with flange and fine pitch thread (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO12126.svg  style="width:32px;"> **ISO 12126** Prevailing torque type all-metal hexagon nut with flange and fine pitch thread.

-   <img alt="" src=images/Fasteners_ISO21670.svg  style="width:32px;"> **ISO 21670** Hexagon weld nut with flange.

-   <img alt="" src=images/Fasteners_SAEJ483a1.svg  style="width:32px;"> **SAE J483a 1** Low cap nut.

-   <img alt="" src=images/Fasteners_SAEJ483a2.svg  style="width:32px;"> **SAE J483a 2** High cap nut.

### T-slot fasteners 

-   <img alt="" src=images/Fasteners_DIN508.svg  style="width:32px;"> **DIN 508** T-slot nut.

-   <img alt="" src=images/Fasteners_GN505.svg  style="width:32px;"> **GN 505** Serrated quarter-turn T-slot nut.

-   <img alt="" src=images/Fasteners_GN505.4.svg  style="width:32px;"> **GN 505.4** Serrated T-slot bolt.

-   <img alt="" src=images/Fasteners_GN506.svg  style="width:32px;"> **GN 506** T-Slot swivel nut.

-   <img alt="" src=images/Fasteners_GN507.svg  style="width:32px;"> **GN 507** T-slot nut.

-   <img alt="" src=images/Fasteners_ISO299.svg  style="width:32px;"> **ISO 299** T-Slot nut.

### Washers

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width:32px;"> **ASME B18.21.1.12A** UN washer, narrow series.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width:32px;"> **ASME B18.21.1.12B** UN washer, regular series.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width:32px;"> **ASME B18.21.1.12C** UN washer, wide series.

-   <img alt="" src=images/Fasteners_DIN6319C.svg  style="width:32px;"> **DIN 6319C** Spherical washer.

-   <img alt="" src=images/Fasteners_DIN6319D.svg  style="width:32px;"> **DIN 6319D** Conical seat.

-   <img alt="" src=images/Fasteners_DIN6319G.svg  style="width:32px;"> **DIN 6319G** Conical seat.

-   <img alt="" src=images/Fasteners_DIN6340.svg  style="width:32px;"> **DIN 6340** Washer for clamping devices.

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width:32px;"> 
**ISO 7089** Plain washer, normal series. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width:32px;"> 
**ISO 7090** Plain washer chamfered, normal series. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width:32px;"> 
**ISO 7092** Plain washer, small series. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width:32px;"> 
**ISO 7093-1** Plain washer, large series. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width:32px;"> 
**ISO 7094** Plain washer, extra large series. *Product grade C.*

-   <img alt="" src=images/Fasteners_ISO8738.svg  style="width:32px;"> **ISO 8738** Plain washer for clevis pins.

-   <img alt="" src=images/Fasteners_NFE27-619.svg  style="width:32px;"> **NFE27-619** Countersunk washer.

### Rods, taps and dies 

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width:32px;"> Inch threaded rod for tapping holes.

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width:32px;"> Tool object for cutting external inch threads.

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width:32px;"> UNC inch threaded rod.

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width:32px;"> DIN 975 metric threaded rod.

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width:32px;"> Metric threaded rod for tapping holes.

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width:32px;"> Tool object for cutting external metric threads.

### Inserts

-   <img alt="" src=images/Fasteners_IUTHeatInsert.svg  style="width:32px;"> Heat staked insert.

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width:32px;"> Self-clinching nut.

-   <img alt="" src=images/Fasteners_PEMStandoff.svg  style="width:32px;"> Self-clinching standoff.

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width:32px;"> Self-clinching stud.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width:32px;"> PCB spacer female/female.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width:32px;"> PCB standoff female/male.

-   <img alt="" src=images/Fasteners_4PWTI.svg  style="width:32px;"> 4 prong threaded wood insert (DIN 1624 Tee nuts).

### Retaining rings 

-   <img alt="" src=images/Fasteners_DIN471.svg  style="width:32px;"> **DIN 471** External retaining ring.

-   <img alt="" src=images/Fasteners_DIN472.svg  style="width:32px;"> **DIN 472** Internal retaining ring.

-   <img alt="" src=images/Fasteners_DIN6799.svg  style="width:32px;"> **DIN 6799** E-clip retaining ring.

### Nails

-   <img alt="" src=images/Fasteners_DIN1143.svg  style="width:32px;"> **DIN 1143** Round plain head nail for use in automatic nailing machines.

-   <img alt="" src=images/Fasteners_DIN1144-A.svg  style="width:32px;"> **DIN 1144-A** Nail for the installation of wood wool composite panels, 20mm round head.

-   <img alt="" src=images/Fasteners_DIN1151-A.svg  style="width:32px;"> **DIN 1151-A** Round plain head wire nail.

-   <img alt="" src=images/Fasteners_DIN1151-B.svg  style="width:32px;"> **DIN 1151-B** Round countersunk head wire nail.

-   <img alt="" src=images/Fasteners_DIN1152.svg  style="width:32px;"> **DIN 1152** Round lost head wire nail.

-   <img alt="" src=images/Fasteners_DIN1160-A.svg  style="width:32px;"> **DIN 1160-A** Clout or slate nail.

-   <img alt="" src=images/Fasteners_DIN1160-B.svg  style="width:32px;"> **DIN 1160-B** Clout or slate wide head nail.

### Pins

-   <img alt="" src=images/Fasteners_ISO1234.svg  style="width:32px;"> **ISO 1234** Split pin.

-   <img alt="" src=images/Fasteners_ISO2338.svg  style="width:32px;"> **ISO 2338** Parallel pin.

-   <img alt="" src=images/Fasteners_ISO2339.svg  style="width:32px;"> **ISO 2339** Taper pin.

-   <img alt="" src=images/Fasteners_ISO2340A.svg  style="width:32px;"> **ISO 2340A** Clevis pin.

-   <img alt="" src=images/Fasteners_ISO2340B.svg  style="width:32px;"> **ISO 2340B** Clevis pin without head (with split pin holes).

-   <img alt="" src=images/Fasteners_ISO2341A.svg  style="width:32px;"> **ISO 2341A** Clevis pin with head.

-   <img alt="" src=images/Fasteners_ISO2341B.svg  style="width:32px;"> **ISO 2341B** Clevis pin with head (with split pin hole).

-   <img alt="" src=images/Fasteners_ISO8733.svg  style="width:32px;"> **ISO 8733** Parallel pin with internal thread, unhardened.

-   <img alt="" src=images/Fasteners_ISO8734.svg  style="width:32px;"> **ISO 8734** Dowel pin.

-   <img alt="" src=images/Fasteners_ISO8735.svg  style="width:32px;"> **ISO 8735** Parallel pin with internal thread, hardened.

-   <img alt="" src=images/Fasteners_ISO8736.svg  style="width:32px;"> **ISO 8736** Taper pin with internal thread, unhardened.

-   <img alt="" src=images/Fasteners_ISO8737.svg  style="width:32px;"> **ISO 8737** Taper pin with external thread, unhardened.

-   <img alt="" src=images/Fasteners_ISO8739.svg  style="width:32px;"> **ISO 8739** Full-length grooved pin with pilot.

-   <img alt="" src=images/Fasteners_ISO8740.svg  style="width:32px;"> **ISO 8740** Full-length grooved pin with chamfer.

-   <img alt="" src=images/Fasteners_ISO8741.svg  style="width:32px;"> **ISO 8741** Half-length reverse taper grooved pin.

-   <img alt="" src=images/Fasteners_ISO8742.svg  style="width:32px;"> **ISO 8742** Third-length center grooved pin.

-   <img alt="" src=images/Fasteners_ISO8743.svg  style="width:32px;"> **ISO 8743** Half-length center grooved pin.

-   <img alt="" src=images/Fasteners_ISO8744.svg  style="width:32px;"> **ISO 8744** Full-length taper grooved pin.

-   <img alt="" src=images/Fasteners_ISO8745.svg  style="width:32px;"> **ISO 8745** Half-length taper grooved pin.

-   <img alt="" src=images/Fasteners_ISO8746.svg  style="width:32px;"> **ISO 8746** Grooved pin with round head.

-   <img alt="" src=images/Fasteners_ISO8747.svg  style="width:32px;"> **ISO 8747** Grooved pin with countersunk head.

-   <img alt="" src=images/Fasteners_ISO8748.svg  style="width:32px;"> **ISO 8748** Coiled spring pin, heavy duty.

-   <img alt="" src=images/Fasteners_ISO8750.svg  style="width:32px;"> **ISO 8750** Coiled spring pin, standard duty.

-   <img alt="" src=images/Fasteners_ISO8751.svg  style="width:32px;"> **ISO 8751** Coiled spring pin, light duty.

-   <img alt="" src=images/Fasteners_ISO8752.svg  style="width:32px;"> **ISO 8752** Slotted spring pin, heavy duty.

-   <img alt="" src=images/Fasteners_ISO13337.svg  style="width:32px;"> **ISO 13337** Slotted spring pin, light duty.

## Obsolete

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:32px;"> [Make countersunk](Fasteners_ChamferHole.md): Chamfer holes for countersunk screws. Not available in <small>(v0.5.13)</small> .

## References

-   Author: [shaise](http://theseger.com/projects/author/shaise/)
    -   ScrewMaker: Ulrich Brammer
    -   Workbench wrapper: Shai Seger
-   Source code: <https://github.com/shaise/FreeCAD_FastenersWB>
-   Bug reports and feature requests: <https://github.com/shaise/FreeCAD_FastenersWB/issues>
-   Forum topic: <https://forum.freecadweb.org/viewtopic.php?t=11429>

## Links

-   [BOLTS](https://github.com/jreinhardt/BOLTS): An open library for technical specifications.


{{Fasteners_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [External_Workbenches](Category_External_Workbenches.md) > [Fasteners](Category_Fasteners.md) > Fasteners Workbench/es
