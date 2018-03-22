---
title: "Reproducibility in Network Experiments with a Simulator"
shorttitle: _portableExperiments_
author:
- name: Mariette Souppe
  affiliation: UC Santa Cruz
  email: msouppe@ucsc.edu
- name: Kerry Veenstra 
  affiliation: UC Santa Cruz
  email: veenstra@ucsc.edu
- name: Ivo Jimenez
  affiliation: UC Santa Cruz
  email: ivo.jimenez@ucsc.edu
- name: Katia Obraczka
  affiliation: UC Santa Cruz
  email: katia@soe.ucsc.edu
abstract: |
  In the mobile and wireless network domain there are a lot of simulations 
  and domain tools that are required to be produce results of an experiment. 
  Our approach is to minimize the amount of time spent to   set up experiments 
  and assumptions for experiments and be able to reproduce experiments with 
  available tools for any user to conduct an experiment on their own environment 
  with no clashing dependencies. Using Popper, a convention and CLI tool, and 
  Docker, a container image, allows any user to reproduce experiments from their 
  peers or a research paper with the exact parameters and assumptions has the 
  author made allowing for easy replication and reproducibility.
  This methodology is used on the 
---

# Introduction

Reruning an original experiment can be a lot of work since a lot configurations and downloading software are needed in order reproduce that experiment.

The approach that *Reproducible Network Experiments Using Container-Based Emulation* by Handigol, Heller [@handigol_emulator_2012] uses a container based solution. However, since it using a container-based emulation this method of reproducibility is using an emulator and not the actual simulator that was originally used to conduct the experiments. Conducting an experiment on an emulator does not have all of the bells and whistles compared to using the actual simulator. As a result, using an emulator to rerun an experiment would have some limitations.

Another the tool that is commonly used to rerun experiments is using a virtual machine. Virtual machines are also capable of running the appropriate software and operating system without having to use an emulator which means that there are no probable experiment limitations as in [@handigol_emulator_2012]. However, in order configure a virtual machine with all of the correct dependencies and environments to replicate an experiment, there is still some ambiguity in terms of the exact settings of the original experiment. Using Docker, which is a container that packages an environment and modules, takes away this ambiguity. 

![figure caption goes in here
](figures/dockerVm.png){#fig:dockerVm}

As you can see in the @Fig:dockerVm there is a difference between the virtual machine and the docker infrastructure. In a Docker container, it only contains the application itself and libraries for that experiment since the Docker layer takes care of the experiment environment. In a virtual machine an operating system has to first be defined before running the application.


The rest of the paper is outlined to show the methodology and tools that are used to reproduce this experiment, an example where this methodology is used in an actual experiment, and lastly our results of reproducing exact results from the original author's results.

# Methodology
![figure caption goes in here
](figures/workflow.png){#fig:workflow}

## Popper
Popper 

## Docker
In order to achieve a reproducibility model for experiments so that an experiment can truly run on any personal machine the technology tool called Docker is used to help accomplish this goal. Docker, a technology container, creates an environment which packages an application with all of the application's dependencies. In the experiment, which is further explained [in section], this tool is used the experiment needs Java and Python installed on a machine in order for the whole experiment to run properly. Normally, one would have to make sure that both of these dependencies are installed on one's personal machine, however with the use of Docker an environment is created with those dependencies 


This enables the portability of an experiment which further helps achieve reproducibility. 
  

## Cooja
For the experiment, to be described in the next section, uses Cooja to conduct the main experiment. Cooja is a network simulator that is used in wireless sensor networks which allows to simulate small or large networks.

# Example

## Background

The experiment where this methodology is used on the paper *Guiding Sensor-Node Deployment Over 2.5D Terrain* by Veenstra [@veenstra_terrain_2015]. The idea of this experiment is to initially place nodes on a specified terrain map with a given range. Then using the algorithm [@veenstra_terrain_2015] continually moves the nodes around the given terrain until a final cumulative visibility value has been computed. As a result, the output of the experiment is the final cumulative visibility value where of all of the nodes are placed in a way that maximizes the coverage a given terrain. 

In order for this experiment to run there are certain parameters that need to be defined. The first parameter in the configuration file is a file name for different simulations. This enables to differentiate between the different simulations. The second parameter is the allows the user to choose if they would like to use a random seed which enables to produce the same sequence of random numbers for testing purposes. This parameter is a boolean where *random* can be turned on or off. Depending on whether a random seed has been initialized to True or False, if True was chosen then a random seed value will need to be initialized. If the random is set to False, then is random seed parameter will be ignored. The last parameter that needs to be defined is the number of nodes desired to put on a terrain which can range from 1 - 50 nodes. As of right now the algorithm can handle a maximum of 50 nodes. 

## Pipeline
![figure caption goes in here
](figures/pipeline_docker.png){#fig:pipeline}

@Fig:pipeline, we show the pipeline 

  * **.popper.yaml**

    This file consists the ordering in which popper executes the main scripts; setup.sh, run.sh, post-run.sh to run the entire experiment with out extra input.

  * **.git**

    Currently the full experiment is not on Git, which it will be soon, however having the whole pipeline on Git will achieve the portable and reproducibility goal. Any user will be able to clone the repository and be able to reproduce the experiment with out having to individually download dependecies.

  * **Dockerfile**

    Retrieves the docker image with Java and installs Python, pip, java-random, pyyaml, and jinja2

  * **setup.sh**

    Builds a docker container with the environmnents, dependencies, and packages that are needed to run the pipeline.

  * **run.sh**

    Will run the simulations in the environment that has been previously defined.

  * **sim_config.yaml**

    The simulation configration file allows the user to run multiple experiments with different values for the parameters. The parameters that the user can define are the filename, decide to use a random generator true/false for nodes placement, random seed, and number of nodes (maximum of 50). The filename is used to name the different experiments so when looking at the final output it will be evident which experiment produce certain results. As of right now the algorithm has hard coded values for the initial placement of the nodes, but as the experiment is further developed the random generator will radomly generator the node placement. [Add in about random seed and point of that] The user can also define the amount of nodes desired for the experiment with a maximum of 50 nodes, since that is the maximum the algorithm of the experiment can handle.

  * **sim_template.csc**

    The template file consists of how the simulator reads in script to create the simulations based on the defined parameters for each experiment.

  * **create_sim_files.py**

    For the N amount of simulations defined in the sim_config.yaml, this file will merge the parameters with the template to create N amount of simlations.

  * **simulations directory**

    All of the simulation files that were produced from create_sim_files.py which are then run in run.sh.

  * **output directory**

    The output for each of the simulations containing the final visability value between the nodes [Need better wording and explain that a bit more]

  * **contiki/tools/cooja**

    The main experiment files are located, where Cooja is the simulator used for the experiment.
    




# Results {#sec:result}

# Conclusion {#sec:conclusion}



**Acknowledgments**: We would like to thank Bernardo Gonzalez for his 
feedback on a preliminary version of this paper, as well as all the 
anonymous reviewers. Special thanks go to our ICPE shepherd. This work 
was partially funded by the Center for Research in Open Source 
Software[^cross], Sandia National Laboratories, NSF Award #1450488 and 
DOE Award #DE-SC0016074. Sandia National Laboratories is a 
multimission laboratory managed and operated by National Technology 
and Engineering Solutions of Sandia, LLC, a wholly owned subsidiary of 
Honeywell International, Inc., for the U.S. Department of Energy’s 
National Nuclear Security Administration under contract DE-NA0003525.

@inproceedings{veenstra_terrain_2015,
  title = {Guiding Sensor-Node Deployment Over 2.5D Terrain},
  booktitle = {IEEE International Conference} on {{Communications}},
  date = {2015},
  author = {Veenstra, Kerry and Obraczka, Katia}
}


# References {.unnumbered}

http://tiny-tera.stanford.edu/~nickm/papers/p253.pdf
https://inrg.soe.ucsc.edu/wp-content/uploads/2015/09/icc-2015.pdf

\noindent
\vspace{-1em}
\setlength{\parindent}{-0.18in}
\setlength{\leftskip}{0.2in}
\setlength{\parskip}{0.5pt}
\fontsize{7pt}{8pt}\selectfont
