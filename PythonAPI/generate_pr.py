
# uses the repo with a pr to add analyze image
# gh pr checkout 233

# create the output directory and set the input files then run

from pycocotool.coco import COCO
from pycocotool.cocoeval import COCOeval
#from pycocotools.coco import COCO
#from pycocotools.cocoeval import COCOeval
#import numpy as np
#import skimage.io as io
#import matplotlib.pyplot as plt
#import pylab

#from matplotlib.collections import PatchCollection
#from matplotlib.patches import Polygon
#from google.cloud import storage
#import cv2
#import pprint

ground_truth_file = 'mscoco_ground_truth.json'
predictions_file = 'mscoco_predictions.json'
save_to_dir = 'output'

# initialize COCO ground truth api
cocoGt = COCO(ground_truth_file)

# initialize COCO detections api
cocoDt = cocoGt.loadRes(predictions_file)

imgIds=sorted(cocoGt.getImgIds())

annType = 'bbox'

# running evaluation
cocoEval = COCOeval(cocoGt, cocoDt, annType)
cocoEval.params.imgIds = imgIds
cocoEval.params.catIds = [1] # person only, see cocoGt.loadCats(cocoGt.getCatIds())
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()
print(cocoEval.stats)

cocoEval.analyze(save_to_dir=save_to_dir)
