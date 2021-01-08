COCO API - http://cocodataset.org/

COCO is a large image dataset designed for object detection, segmentation, person keypoints detection, stuff segmentation, and caption generation. This package provides Matlab, Python, and Lua APIs that assists in loading, parsing, and visualizing the annotations in COCO. Please visit http://cocodataset.org/ for more information on COCO, including for the data, paper, and tutorials. The exact format of the annotations is also described on the COCO website. The Matlab and Python APIs are complete, the Lua API provides only basic functionality.

In addition to this API, please download both the COCO images and annotations in order to run the demos and use the API. Both are available on the project website.
-Please download, unzip, and place the images in: coco/images/
-Please download and place the annotations in: coco/annotations/
For substantially more details on the API please see http://cocodataset.org/#download.

After downloading the images and annotations, run the Matlab, Python, or Lua demos for example usage.

To install:
-For Matlab, add coco/MatlabApi to the Matlab path (OSX/Linux binaries provided)
-For Python, run "make" under coco/PythonAPI
-For Lua, run “luarocks make LuaAPI/rocks/coco-scm-1.rockspec” under coco/

Alternatively you can install with pip from the gitlab repo:
```
# first satisfy the requirements
dnf update -y
dnf install git gcc python3-devel -y
pip install numpy
# if your git user.name is set and ssh key are available you should be able to clone as follows:
# git config --global user.name "username"
# git clone git@gitlab.com:vivint/cv/cocoapi.git
python -m pip install -e "git+git@gitlab.com:vivint/cv/cocoapi.git@add_analyze_func#egg=pycocotools&subdirectory=PythonAPI"
```
