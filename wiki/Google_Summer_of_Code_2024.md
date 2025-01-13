# Google Summer of Code 2024
FreeCAD started participating to the Google student coding program (GSoC) in 2016. We participated through a combined effort of many CAx projects, under the BRL-CAD umbrella. Since 2023, we are applying as our own organization.

-   Main page of the program: <https://summerofcode.withgoogle.com/>
-   Timeline: <https://developers.google.com/open-source/gsoc/timeline>
-   FreeCAD in GSoC 2024: <https://summerofcode.withgoogle.com/programs/2024/organizations/freecad>

## How it works 

-   The student writes a project proposal for FreeCAD.
-   Students can choose to work on their own idea, or they can pick an idea suggested by the FreeCAD mentors team. There is no difference in how your project is reviewed or accepted, the important part is to work on something you like.
-   Proposals will be reviewed, evaluated, and ranked by FreeCAD mentors.
-   Google allocates a certain number of slots to each participating organization. Slots are allocated following the ranking order given by the project mentors.
-   If you are accepted, You will have two FreeCAD mentors assigned to you. there is a first period allocated to get to know FreeCAD, the community and your mentors, then the real coding period starts. Your work get reviewed at mid-term and at the end.

If you want to get involved, have a look at the [GSoC Checklist](GSoC_Checklist.md). Whether you\'re applying or accepted, we\'ve itemized everything you need to do in this list. We\'re here to help you become new open source developers, so don\'t be shy if you have any questions.

## Writing your proposal 

We are proposing a number of project ideas here. But you are in no way forced to follow our ideas. You can propose anything you would like to work on, that you thing would be an interesting project. Good places to hunt for ideas are the [list of feature requests](https://github.com/FreeCAD/FreeCAD/issues?q=is%3Aopen+is%3Aissue+label%3AFeature), the [FreeCAD forum](https://forum.freecad.org) or other FreeCAD communities, like [Facebook](https://www.facebook.com/FreeCAD), [Discord](https://discord.com/invite/w2cTKGzccC) or [Reddit](https://www.reddit.com/r/freecad).

You will find many templates and models on the internet, and on the [Google Summer of Code website](https://summerofcode.withgoogle.com/), but it does not need to be very elaborate. Again, what is important is that you choose a subject you like. It\'s more important to get interested in your idea and do some research about how you would achieve it than writing very long proposals.

What we expect to see in your proposal is what is explained on the [Google Summer of Code website](https://summerofcode.withgoogle.com/). Additionally, we want to see that you did your research, and that you explored FreeCAD enough so we can trust you know what you are going into.

## The Selection Process 

GSoC is about getting people involved and contributing to open source over the long-term. As such, we heavily weight our application selection process towards students that are interested in remaining involved in FreeCAD and open source software development after GSoC has ended. GSoC is not a summer job, although it happens during the Norther hemisphere summer months and requires some dedication and commitment, like a job.

Additionally, submissions are ranked based on perception of the submitter\'s abilities to complete the task within the program timeframe, general consensus on the technical approach being proposed, and overall interest in having such modifications made to FreeCAD. Particular notice is made of students that are responsive to questions and readily interactive with the FreeCAD community, mainly through the [FreeCAD forum](https://forum.freecad.org). Communication is a great thing. Having a forum account already, and having already discussed your idea there, for example under the [GSOC section](https://forum.freecad.org/viewforum.php?f=46&sid=c47dc0459f8be0c52e072a8de66c8738), is a great way to have people interested in your project.

Just about every GSoC organization receives considerably more project proposals than can be accepted. Every application gets read multiple times and reviewed in detail. Of those applications, only a small subset are selected so keep in mind that the selection process is rather competitive.

Whether or not you are accepted, contributing to open source outside of GSoC is one of the main goals of the program and is the best way to be noticed and get your proposal accepted. Keep that in mind. Thanks for your interest and we look forward to working with new FreeCAD developers!

And in case your proposal is not accepted but you would still like to work on it, nothing prevents that! Several FreeCAD GSoC students in the past have worked on their project outside the GSoC program.

## Possible Mentors 

[Bernd](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=2069), [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68), [Amritpal](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=9146), [Ickby](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=686), [Kkremitzki](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=7997), [Kunda1](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=12229), [WandererFan](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=1375), [Sliptonic](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=708), [Paddle](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=29478), [Adrianinsaval](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=19302) and others. The best way to contact us is through the [FreeCAD GSoC 2024 discussion thread](https://forum.freecad.org/viewtopic.php?t=84897).

## Implementation Ideas 

There are several sources for project ideas. The table below lists existing project ideas already documented on our wiki. FreeCAD also previously participated in an umbrella organization for GSoC, and there are [FreeCAD project ideas available in their GSoC repo](https://github.com/opencax/GSoC/issues?q=is%3Aissue+is%3Aopen+FreeCAD). Additionally, there is a [forum thread](https://forum.freecad.org/viewtopic.php?t=84897) calling for additional ideas which may be the basis of a project.

The ideas listed here or in the OpenCAx repo have a high chance of being accepted as project proposal. Note that for students with an established involvement in FreeCAD who have already contributed code, ideas in their own line of work are also welcome. Feel free to contact us on the [forum](https://forum.freecad.org/viewtopic.php?t=84897) for further discussions about the listed projects.

The topic\'s priority shows you how important the work on the ideas is for the mentors, and hence choosing a high priority topic will give you an advantage if there are more applications than slots for FreeCAD. The size column shows the estimated time frame to complete the project, but you are of course free to suggest otherwise if you see arguments for it.

  Topic                                                                                                                                                                                                                      Language         Size   Difficulty   Priority   Contact
       
  [FreeCAD-BRLCAD integration](https://github.com/FreeCAD/FreeCAD/issues/8557): Allow to open, edit and save BRL-CAD models in FreeCAD                                                                                       C++              350h   High         Medium     [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68), [Daniel Rossberg](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=23847)
  [Unified Measurement Facility](https://github.com/FreeCAD/FreeCAD/issues/8561): Create a generalized measurement tool that combines functionality from workbench-specific ones                                             Python/C++       175h   Medium       Low        [Kkremitzki](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=7997)
  [Improve Hidden Line Removal](https://github.com/opencax/GSoC/issues/69): Develop new code for projecting shapes and creating the geometry for technical drawings                                                          C++              350h   Hard         Low        [WandererFan](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=1375)
  [Improving Headless mode](https://github.com/opencax/GSoC/issues/68): Exposing more FreeCAD functionality to the console that can run with and without the GUI available                                                   C++              175h   Medium       Low        [Kunda1](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=12229)
  [Command-line preferences manipulation](https://github.com/opencax/GSoC/issues/38): Design a command-line tool that allows to create, modify or delete FreeCAD preference parameters                                       C++              175h   Medium       Low        [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)
  [Improve the API documentation](https://github.com/FreeCAD/FreeCAD/issues/12547): Work on the FreeCAD doxygen-generated documentation: Propose a better plan, document the modules better, make it clearer to read, etc.   C++ and Python   175h   Medium       Low        [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)
  [Cabinet tool](https://github.com/opencax/GSoC/issues/35): Design a tool for the Arch workbench that allows a user to easily create several kinds of cabinets                                                              Python           350h   Medium       Low        [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)
  [Direct Modeling tools](https://github.com/opencax/GSoC/issues/17): Study and implement direct modeling tools in FreeCAD                                                                                                   Python/C++       350h   Hard         Low        [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)
  [Rebuild the Start Workbench](https://github.com/FreeCAD/FreeCAD/issues/12565): Redo the Start workbench to avoid Web/HTML dependency                                                                                      Python/C++       175h   Medium       High       [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)
  [Integrate a client for the buildingSMART Data Dictionary web service](https://github.com/FreeCAD/FreeCAD/issues/5607): Extend the classification manager in the BIM workbench                                             Python/C++       350h   Medium       Low        [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)

Note also that any issue open on the [FreeCAD issues tracker](https://github.com/FreeCAD/FreeCAD/issues) could become a good GSoC proposal. Don\'t hesitate to browse the issues, there is a number of issues [marked as GSoC issues](https://github.com/FreeCAD/FreeCAD/labels/GSoC), of which most are in the list above, and the ones [marked as \"Feature\"](https://github.com/FreeCAD/FreeCAD/issues?q=is%3Aissue+is%3Aopen+label%3AFeature) are feature requests and might be especially interesting to you.

The ones marked as [good first issue](https://github.com/FreeCAD/FreeCAD/labels/Good%20first%20issue) are identified as interesting for new contributors. If any of them picks your brain, feel free to discuss it, either directly on the issue itself, or on the [forum thread](https://forum.freecad.org/viewtopic.php?t=84897).

## Schedule

See <https://developers.google.com/open-source/gsoc/timeline>

## Previous GSOCs 

-   [Google Summer of Code 2023](Google_Summer_of_Code_2023.md)
-   [Google Summer of Code 2022](Google_Summer_of_Code_2022.md)
-   [Google Summer of Code 2020](Google_Summer_of_Code_2020.md)
-   [Google Summer of Code 2019](Google_Summer_of_Code_2019.md)
-   [Google Summer of Code 2018](Google_Summer_of_Code_2018.md)
-   [Google Summer of Code 2017](Google_Summer_of_Code_2017.md)



---
⏵ [documentation index](../README.md) > Google Summer of Code 2024
