## Hi there!
This is the website for the **multivoxel pattern analysis (MVPA) of fMRI data in Python** workshop which was originally
given at [ICON](http://www.icon2017.org/) 2017. The materials and data will remain online so that everyone who's interested
can follow the workshop. Also, all the material is *fully open-source*, so feel free the re-use and modify this workshop's materials to fit your own educational activities! If you find mistakes or have suggestions for improvements of this workshop, please let me know by email (see [Github](https://github.com/lukassnoek)) or, even better, submit a "Pull Request" (PR) to this workshop's [Github repository](https://github.com/lukassnoek/ICON2017) - this is greatly appreciated! That said, on this website, you'll find some general info about the workshop, how to prepare for it (in terms of Python prerequisites and environment), and the slides/notebooks/data that will be used during the workshop.

Also, check out the slides from the introductory lecture below:

<style>
.responsive-wrap iframe{ max-width: 100%;}
</style>
<div class="responsive-wrap">
<!-- this is the embed code provided by Google -->
<iframe src="https://docs.google.com/presentation/d/1bgK1sv-VmnvAR_HgTiWsU0vQkyjz6oO1zQ5ly4laPkw/embed?start=false&loop=false&delayms=3000" frameborder="0" width="900" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
<!-- Google embed ends -->
</div>

### Scope/learning goals
Originally, this notebook was developed for the Research Master Psychology course [Neuroimaging: Pattern Analysis](http://studiegids.uva.nl/xmlpages/page/2017-2018/zoek-vak/vak/39531) at the University of Amsterdam, but it was adapted and extended for this ICON workshop. As such, this workshop was designed for people who are relatively *unfamiliar* with MVPA and/or its implementation in Python. We *do* assume that you are familiar with analyzing (f)MRI data; the purpose of this workshop is to "extend your analysis toolbox", so to say. As such, it’s definitely helpful if you have some knowledge about Python’s syntax, but it’s not strictly necessary. Also, we assume participants are relatively unfamiliar with machine learning (ML) concepts and their implementation; if you’re a ML guru, this is probably not the right workshop for you...

Also, there is actually no single "multivoxel pattern analysis"; rather, MVPA is a bucket-term referring to several kinds of pattern-based analyses. As this workshop cannot cover all such analyses, we limit the scope to machine learning (*classification-based*) analyses of fMRI data. We hope to cover these grounds sufficiently well for you to be able to explore other kinds of analyses on your own. 

### Learning goals of this workshop
In this workshop, we cover the basics and implementation of multivoxel pattern analysis (MVPA) to analyze (functional) MRI data in Python. After this tutorial, you are able to:

- Understand the differences between within-subject and between-subject pattern analysis;
- Know how to extract/estimate patterns from fMRI data;
- Implement different feature extraction and selection methods using scikit-learn;
- Build cross-validated MVPA pipelines using scikit-learn;
- Evaluate your models

In short, this tutorial will show how to build your own complete, cross-validated MVPA pipeline for fMRI data.

Note: if you're interested in the original course materials, check out the corresponding [github](https://github.com/lukassnoek/PatternAnalysis). The slides from the course corresponding to the material of this workshop can be viewed [here](lecture_slides/PatternAnalysis_week_1_intro.pdf) (intro/pattern estimation) and [here](lecture_slides/PatternAnalysis_week_2_decoding.pdf) (decoding/ML).

## How to prepare ...
To make sure that we are not going to spend half of the workshop fixing software dependencies and downloading data, we provide some instructions here to prepare for the workshop. 

### Python set-up
For this workshop, we'll obviously use the Python programming language. We expect participants to bring their own laptop. Given that you brought your own laptop, there are two options for working on the materials from the hackathon:

1. Install/configure Python on your own computer and download the materials (this is recommended!). Please follow **[these instructions](configure_python.md)** on how to download and set-up Python correctly.

2. Request an account on our analysis-server. In that case, please email me (lukassnoek [at] gmail [dot] com) in advance. You can only log in at the day of the workshop at the
Beurs van Berlage. See **[this manual](log_in_server.md)** for instructions on how to log in/access our server.

If possible, try to install Python on your own computer (**[option 1](configure_python.md)**), as this will not have the problem of "lag" caused by the remote desktop client. Following the tutorials should be doable on a laptop with decent specs (i.e., at least 4 GB of RAM). Once you set up Python and installed the necesary packages, you should download the data we are going to use for the workshop.

### Download the data
At the top of this website, click the button [Download material (.zip)](https://github.com/lukassnoek/ICON2017/zipball/master) to download the entire Github repository with the material. Unzip it and check out its contents. There are various files in this directory (some of them are used to generate this website), but the only relevant directory for you is the **tutorial** directory which contains the notebooks we'll use for the workshop. As you can see, the unzipped folder also contains a file named `download_data.py`, which is as its name suggests a script to download the data. Note: the data is about 400MB in total! Also, *it assumes that you've installed Python already*.

To start the download, open a terminal (or `cmd` tool in Windows) and type:

`python download_data.py`
  
This should create a folder "data" in the directory with the materials, which will include 16 folders starting with *pi*. This het data that we'll use in our tutorials.
 
If, for some reason, the `download_data.py` script doesn't work, you can manually download the data by going to [this URL](https://surfdrive.surf.nl/files/index.php/s/Iv5tNOAMZTJ0WiS/download) (which points to the data repo). Download the zip-file and unzip it in the folder with the materials such that the unzipped folder ("data") is located here:

`Name_of_unzipped_materials_folder/`  
`├── code`  
`├── configure_python.md`  
`├── \_config.yml`  
├── **data**  
`├── download_data.py`  
`├── \_layouts`  
`├── lecture_slides`  
`├── LICENSE`  
`├── README.md`  
`└── tutorial`  

The location of the data is important because the tutorials assume that they're located in the same folder as the *tutorial* directory.

__Please download the data *before* the day of your workshop, because on the day itself wifi will probably be slow!__

### Opening the notebooks
To open the tutorial notebook, use your terminal to navigate to the "tutorial" directory. Then, start the notebook by typing:

    $ jupyter notebook ICON2017_tutorial.ipynb

(Do not actually type the `$`; this represents the prompt of your terminal!)
Now, a browser should open with the notebook!

### Do the Python tutorial (*optional*)
For the course on which this workshop is based, we included short Python refresher/tutorial. For those who
want to brush up their Python skills, or don't have any experience with Python at all, we included the 
notebook in the workshop's materials. Like the main `ICON2017_tutorial`, you can start the `python_tutorial.ipynb`  as follows:

    $ jupyter notebook python_tutorial.ipynb

## Questions
If you have questions about the workshop, you can send an email to *lukassnoek [at] gmail [dot] com*.
We're looking forward to meeting you in Amsterdam!

Best,

Lukas & Steven