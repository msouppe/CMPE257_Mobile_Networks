---
title: "Reproducing Network Experiments With Popper"
shorttitle: _portableExperiments_
author:
- name: Andrea David
  affiliation: UC Santa Cruz
  email: andavid@ucsc.edu
- name: Mariette Souppe
  affiliation: UC Santa Cruz
  email: msouppe@ucsc.edu
- name: Katia Obraczka
  affiliation: UC Santa Cruz
  email: katia@soe.ucsc.edu
- name: Ivo Jimenez
  affiliation: UC Santa Cruz
  email: ivo.jimenez@ucsc.edu
- name: Sam Mansfield 
  affiliation: UC Santa Cruz
  email: smansfie@ucsc.edu
- name: Kerry Veenstra 
  affiliation: UC Santa Cruz
  email: veenstra@ucsc.edu
abstract: |
  Need abstract
---

# Introduction
The ability to reproduce previous experiments is one of the most important aspects in scientific research. However, as scientific discovery is rapidly advancing, researchers are pressured to rush publication of new findings and present these breakthrough discoveries at conferences. Lately, there has been a growing concern in the research community about results that cannot be reproduced and thus cannot be verified. This is partially due to the lack of incentive for researchers to revoke experiments that were unable to be reproduced [??]. Moreover, replicating scientific experiments in the field of Computer Science and Computer Engineering is a challenging task. One of the biggest setbacks of reproducibility is the complexity that comes with rebuilding the same environment in which the original experiment was conducted [??]. Rerunning an original experiment can be strenuous since a lot configuration and downloading software are needed in order to reproduce any experiment. In the scientific community, it is important to be able to reproduce existing research paper results to further improve upon and understand conveyed ideas.

Network simulators were not designed with the concept of reproducibility which makes the automation and configuration of simulations more difficult especially with trying to automate without a GUI.




# Related Work
ReproZip is another tool that allows for easy reproduction of experiments from command-line executions. While executing the experiment in its original environment, ReproZip tracks operating system calls and packs necessary components of the experiment into a file. In the unpacking step, ReproZip reproduces the experiment form that file. ReproZip, however, can only package experiments that are executed on Linux.


# Popper Versus Exisiting Tools 
![As you can see there is a difference between the virtual machine and the docker infrastructure. In a Docker container, it only contains the application itself and libraries for that experiment since the Docker layer takes care of the experiment environment. In a virtual machine an operating system has to first be defined before running the application.
](figures/dockerVm.png){#fig:dockerVm}
	
A tool that is commonly used to rerun experiments is a virtual machine. The base functionality between a virtual machine and using Docker are similar in the ability to create an environment for
an application. However, these two tools use their own approaches. In a virtual machine you must define an environment per application, whereas in Docker an environment can be shared among other applications where the applications are run in a container. This allows for sharing resources on your host operating system since Docker dynamically allocate memory. Another added feature to
Docker is that modules and packages can also be defined when building the environment which prevents having to be careful of how each operating system handles downloading modules such as *pip* for example.

However, in order configure a virtual machine with all of the correct dependencies and environments to replicate an experiment, there is still some ambiguity in terms of the exact settings of the original experiment. Using Docker and packaging an environment and extra modules, eliminates this ambiguity. @Fig:dockerVm shows the infrastructure of these tools.

# Experiment Examples

## Cooja Simulator
Cooja is used to conduct the main experiments. Cooja is a network simulator that is used in wireless sensor networks which allows simulations of small or large networks. Contiki is also used in the experiment but only used for its thin layer operating system to run Cooja. Cooja is a tool of Contiki as you can see in the file directory where the experiment is run. 

## TerrainLOS
One of the experiments that are reproduced in this paper is based on Sam Mansfield’s paper “Modeling Communication Over Terrain for Realistic Simulation of Outdoor Sensor Network Deployments” [??]. TerrainLOS is an outdoor terrain propagation model that aims to create a more accurate simulation of outdoor sensor network communication. When it comes to simulating sensor networks, terrain plays a significant role in evaluating the performance of network functions. Most simulation platforms, however, either assume a completely flat terrain or tend to use very simplistic channel propagation models that do not represent realistic outdoor terrain conditions. To present a more accurate outdoor simulation model, TerrainLOS uses common geographical height maps, called Digital Elevation Models (DEMs). These data files are used in experimental evaluations to investigate communication between nodes under realistic conditions. TerrainLOS describes the Average Cumulative Visibility (ACV) as a metric to characterize network connectivity over the terrain classified in the DEMs. ACV denotes the percentage of sensor nodes that are visible in an area from all locations on a given map. For example, 100% ACV means that every node is visible from all locations, which further implies the presence of a flat terrain. In the experimental methodology, the authors of TerrainLOS refer to the average number of nodes in an area as the average population, and the average number of nodes that a given node can communicate with is referred to as the average node density. These two metrics are used in determining network connectivity. This experiment focuses on automating the execution and re-execution of one of the experimental simulations performed in the paper, called Experimental Connectivity. This experiment focuses on experimentally evaluating the accuracy of connectivity results based on the models presented in the paper. The connectivity results are plotted using the average cumulative visibility metric and population size. 


## 2.5D Deployment on TerrainLOS
The experiment where this methodology is used on is based on the paper Guiding Sensor-Node Deployment Over 2.5D Terrain by Veenstra. The idea of this experiment is to initially place nodes on a specified terrain map within a predetermined range. Then using the algorithm from the paper, nodes continually move around the given terrain until a final cumulative visibility value has been computed. As a result, the output of the experiment is a final cvis value where of all of the nodes are placed in a way that maximizes the coverage a given terrain.

The old way Kerry’s experiment was conducted was that he would have to start the GUI, configure a few parameters such as the number of nodes, terrain, and transmitting range, then initial a script, run the script, and wait for final results. For each simulation these manual steps had to done. 

# Popperization

## Background

## TerrainLOS
To run TerrainLOS in COOJA, without using Popper, a user would have to go through the same steps I did when I tried replicating Sam’s results on my computer. First, they would have to download Instant Contiki, install a Virtual Machine to start Contiki. Then, they would have to download all the necessary files and dependencies from Sam’s GitHub page, create a jar file of TerrainLOS, run the simulator, and load it into COOJA. This is a very time-consuming task and the user might even receive error messages when they try to run the project the first time. Using Popper is a much more effortless way to re-execute someone’s experiment without the need to have the original author explain the steps they need to take to run the project. 

In my Popper pipeline, I had two stages – the run stage and the post-run stage. My setup stage was done using Docker, by creating an image of the Contiki operating system including the COOJA simulator in a Dockerfile. In the run stage, I ran Sam’s python script called calc_experimental_connectivity.py that takes ACV and population as it’s input. The run stage runs the experiment with population of 1, 10, 30, and 80, and ACV of 10-100 in increments of ten. The results of these runs will be put into log files. These log files are then read with the graph_max_density_connectivity.py script in the post-run stage. At the end of the run the graph of the experiment will be saved as “Connectivity.png” file under Connectivity. This 3 “popperized” experiment can be now run by just simply using the command “popper check” inside the pipeline.


## 2.5D Deployment on TerrainLOS
With the popper version, the user only has to configure one file for multiple simulations where popper will run each simulation individually and then output the final results.

Workflow of automation of experiment: First, the values of the parameters of the experiment have to be defined by the user. Second, a Docker container is created with the entire environment, modules, and packages for the experiment to run. In the third step, the simulation template gets pulled in to the fourth step when creates N amount of simulations that the user has defined. Fifth, those N simulations are run and lastly the Cooja.testlog are outputted into the output folder to further evaluate the final result.


# Conclusion {#sec:conclusion}
Researchers usually don’t have the opportunity to reach out to the author of an experiment when rebuilding their work in the environment the original project was built in. This process can be time-consuming and often impossible. The Popper convention offers a very straight forward way to implement reproducibility for scientific research articles.

It is harder to try to make a fully finished experiment reproducible, especially if the person trying to reproduce the experiment is not the original author of that experiment. Reproducibility should be kept in mind at the start of an experiment. Reproducing small sections of the code is easier than trying to reproduce code that has already been completed. 




\noindent
\vspace{-1em}
\setlength{\parindent}{-0.18in}
\setlength{\leftskip}{0.2in}
\setlength{\parskip}{0.5pt}
\fontsize{7pt}{8pt}\selectfont

