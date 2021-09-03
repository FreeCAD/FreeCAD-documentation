

## Introduzione


{{TOCright}}


<div class="mw-translate-fuzzy">

L\'ambiente OSE Piping crea tubi e raccordi. Supporta l\'ambiente [Flamingo](Flamingo_Workbench/it.md). È una parte di [Open Source Ecology](https://www.opensourceecology.org/).


</div>

![ 512px](images/OSE_Piping_workbench_screenshot.png )

# Customization

OSE Piping stores dimensions in CSV-files in the *table* directory in the workbench directory. Edit these CSV files if you want to add new or to change dimensions of the fitting.

# Pipe

A pipe is described by its outer diameter **OD**, its wall thickness **Thk** and its height **H**.

To create a pipe, click ![](images/OSE_Piping_create_pipe_icon.svg ) in OSE piping workbench. Select pipe dimensions and click \"OK\".

![ 512px](images/OSE_Pining_create_pipe_screenshot.png )

To add new dimensions adjust CSV **pipe.csv** file.

Wikipedia on Nominal Pipe Size (NPS) [1](https://en.wikipedia.org/wiki/Nominal_Pipe_Size).

# Elbow

An elbow is described by an angle alpha, outer pipe diameter **POD**, inner pipe diameter **PID**, **H**, **J**, and **M**.

To create an elbow, click ![](images/OSE_Piping_create_elbow_icon.svg ).

<img alt="" src=images/OSE_Piping_create_elbow_screenshot.png  style="width:512px;"> ![](images/OSE_Piping_elbow_CAD_screenshot.png )  To add new elbows, adjust **elbow.csv** file.

# Sweep Elbow {#sweep_elbow}

A sweep elbow is a special elbow with larger radius of the bent part. It is described by outer pipe diameter POD, pipe thickness **PThk**, **G**, **H**, and **M**. To create a sweep elbow, click ![](images/OSE_Piping_create_sweep_elbow_icon.svg ).

<img alt="" src=images/OSE_Piping_create_sweep_elbow_screenshot.png  style="width:512px;"> ![](images/OSE_Piping_sweep_elbow_CAD_screenshot.png )  To add new sweep elbows, adjust **sweep-elbow.csv** file.



[Category:User Documentation{{\#translation:}}](Category:User_Documentation.md) [Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Workbenches{{\#translation:}}](Category:External_Workbenches.md)
