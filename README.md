[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/openpathsampling/ops_tutorial/HEAD?urlpath=lab)
![Tests](https://github.com/openpathsampling/ops_tutorial/workflows/Tests/badge.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/openpathsampling/ops_tutorial)

# OpenPathSampling Alanine Dipeptide Tutorial

This is an introductory tutorial for OpenPathSampling, and is generally the
tutorial that we recommend as a starting place for new users.  It is primarily
focused on basic transition path sampling, using the OpenMM engine. It also
includes analysis of a committor simulation. Although the OpenMM engine is
used, most of the setup and analysis is valid for other engines, as well.

This tutorial also introduces several other packages, both from the domain of
(bio)molecular simulation specifically, and from scientific Python generally.
Tools we will use that focus on molecular simulation include
[OpenPathSampling](http://openpathsampling.org), 
[OpenMM](http://openmm.org/), 
[OpenMMTools](https://github.com/choderalab/openmmtools), 
[NGLView](https://github.com/arose/nglview),
and 
[MDTraj](http://mdtraj.org/).
More generic Python tools that will be used include
[Jupyter notebooks](https://jupyter.org/),
[matplotlib](https://matplotlib.org/),
and
[pandas](https://pandas.pydata.org/).

## Requirements

If you'd prefer not to install things locally, you can try out the tutorial
using [this Binder
link](https://mybinder.org/v2/gh/openpathsampling/ops_tutorial/HEAD?urlpath=lab).
Performance is likely to be better on your own computer than on Binder, but
Binder is useful if you can't/don't want to install the software.

### Software

Note that OpenPathSampling does not support Windows; if you're using a Windows
machine, you should use the Windows Subsystem for Linux.

We strongly recommend installing the requirements using conda. Once you have
installed conda, the following commands will install OpenPathSampling and the
extras that are required for this tutorial:

```text
conda install -c conda-forge openpathsampling
conda install -c conda-forge -c omnia openmm openmmtools
conda install -c conda-forge jupyter tqdm
conda install -c conda-forge nglview
jupyter-nbextension enable nglview --py --sys-prefix
```

### Space and time

In addition to software installation, we recommend ensuring that you have
approximately 2GB of disk space free. The majority of the space needed will be
used by precomputed files, which can be downloaded from
https://figshare.com/s/01302bc7a39ec7648ea1, and which provide data for
detailed analysis.

Most people complete the three main parts of the tutorial in less than 90
minutes.  The most time-consuming step is the analysis of the committor
simulation, in notebook 3 (`analyzer = paths.ShootingPointAnalysis(...)`).  To
save time, you can start that analysis (running the cells up to and including
that one) before starting the tutorial (but after downloading the precomputed
files from figshare) and let that analysis run while you work through the
earlier parts.


## Using the tutorial

Each notebook has a numeric prefix, and they should be run in that order.
Notebook 0 is optional; it teaches some basics of working with Jupyter
notebooks for those who are not familiar with them.

To start the notebook server, switch to the directory with this tutorial and
type `jupyter notebook` at the command prompt.  This may immediately launch
your browser; if not, you should see text like:
```text
The Jupyter Notebook is running at:
http://localhost:8888/?token={LONG_HEXIDECIMAL_TOKEN_HERE}
 or http://127.0.0.1:8888/?token={LONG_HEXIDECIMAL_TOKEN_HERE}
```
You can copy-paste that link into your web browser.

You should see a directory listing in your browser. Clicking on a filename
should open a new tab with that notebook. Open notebook
`0_jupyter_intro.ipynb`, and start the tutorial!

During the tutorial, you'll see several cells marked with the words "YOUR TURN"
in comments. In these cells, you will need to add code. Frequently, this just
involves a slight modification to a previous cell. There are also a few
optional tasks that more advanced students might attempt, marked as advanced
exercises.

Cells marked with the cell magic `%%time` may take a few minutes to complete,
so don't worry if they don't complete immediately.

Notebook 4 is optional, and has no exercises in it. It provides setup for a
very different kind of system (a 2D toy model), and illustrates that the
overall setup process is the same, regardless of the underlying engine.

Notebook 5 contains some more advanced exercises related to TIS, and also shows
how to use the OPS command line interface. In addition to the requirements
listed above, it requires installation of `openpathsampling-cli`.

## History

This tutorial has been used in multiple classes and workshops, including
several E-CAM Extended Software Development Workshops (Leiden, The Netherlands,
2017; Lyon, France, 2019), Master's-level courses in Biomolecular Simulation at
the University of Amsterdam (since 2017), and the CECAM flagship school MolSim
(2021).

This tutorial was developed with financial support from the European Union's
Horizon 2020 research and innovation program, under grant agreement No. 676531
(project E-CAM).
