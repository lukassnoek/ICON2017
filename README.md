## Hi there!
Welcome to the website for the ICON 2017 hackathon "multivoxel pattern analysis (MVPA) of fMRI data in Python"! On this website, you'll find some general info about the hackathon, how to prepare for it (in terms of Python prerequisites and environment), and the slides/notebooks/data that will be used during the hackathon.

## Scope/learning goals
This "hackathon" (or rather *workshop*, really) assumes that participants are familiar with analyzing (f)MRI data and want to know how they would go about implementing a machine-learning ("decoding") analysis in Python. As such, it's definitely helpful if you have *some* knowledge about Python's syntax, but it's not strictly necessary. (We do provide a crash-course Python-for-fMRI in a separate notebook which we'll *won't* discuss during the workshop, but you can do on your own if you want!)

Also, we assume participants are relatively unfamiliar with machine learning (ML) concepts and their implementation. This workshop is based on material from the course "Neuroimaging: Pattern Analysis" taught at the University of Amsterdam for the Research Master Psychology, so it was designed with this in mind, resulting in a relatively "hands-on" approach, including lot's of "practice assignments" in the notebooks, which are optional for this workshop as it involves quite a bit of Python programming. Anyway, in short: if you're a ML guru, this is probably not the right workshop for you ... 

## How to prepare ...
To make sure that we are not going to spend half of the workshop fixing software dependencies and downloading data, we provide some instructions here to prepare for the workshop. 

### Set up Python
For this workshop, we'll obviously use the Python programming language. We expect participants to bring their own laptop. Given that you brought your own laptop, there are two options for working on the materials from the hackathon:

1. Install/configure Python on your own computer and download the materials (this is recommended!). Please follow [these](configure_python.md) instructions on how to download and set-up Python correctly.

2. Request an account on our analysis-server. In that case, please email me (lukassnoek [at] gmail [dot] com) in advance. You would need to download [X2go](http://wiki.x2go.org/doku.php/doc:installation:x2goclient) - a remote desktop client - to access our server.

If possible, try to install Python on your own computer (option 1), as this will not have the problem of "lag" caused by the remote desktop client. Following the tutorials should be doable on a laptop with decent specs (i.e., at least 4 GB of RAM). Once you set up Python and installed the necesary packages, you can download the data we are going to use for the workshop.

### Download the data
On top of this website, click the button "Download material (.zip)" to download the entire Github repository with the material. Unzip it and check out its contents. There are various files in this directory (most of them are used to generate this website), but the only relevant directory for you is the *tutorial* directory which contains the notebooks we'll use for the workshop. As you can see, the unzipped folder also contains a file named `download_data.py`, which is as its name suggests a script to download the data. Note: the data is 211 MB in total! Also, it assumes that you've installed Python already.

To start the download, open a terminal (or `cmd` tool in Windows) and type:

`python download_data.py`
  
This should create a folder "data" in the directory with the materials, which will include 15 folders starting with "pi". These comprise the data that we'll use in our tutorials.
 
If, for some reason, the `download_data.py` script doesn't work, you can manually download the data by going to [this URL](https://surfdrive.surf.nl/files/index.php/s/tosBy0KNb9BFUTC/download) (which points to the data repo). Download the zip-file and unzip it in the folder with the materials such that the unzipped folder ("data") is located here:

`Name_of_unzipped_materials_folder/`  
`├── code`  
`├── configure_python.md`  
`├── \_config.yml`  
├── **data**  
`├── download_data.py`  
`├── \_layouts`  
`├── LICENSE`  
`├── README.md`  
`└── tutorial`  

The location of the data is important because the tutorials assume that they're located in the same folder as the *tutorial* directory.
 
__Please download the data *before* the day of your workshop, because on the day itself wifi will probably be very slow!__

### Opening the notebooks


## ToDo:

- Lukas: run piop1 WM first-levels
- Lukas: data op surfdrive + download-script
- Lukas: python-refresher notebook
- Lukas: python installatie tutorial op website
- Steven: aanpassingen notebook

* design korter
* minder python programmeer dingetjes
* answer-notebook
* Figure out cell collapse

- Figure out IP van Beurs van Berlage (open zetten voor TUX)


