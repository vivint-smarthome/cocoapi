
#%% Generate graphs with the operating points
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

ground_truth_file = 'mscoco_ground_truth.json'
predictions_file = 'mscoco_predictions.json'

# initialize COCO ground truth api
cocoGt = COCO(ground_truth_file)

# initialize COCO detections api
cocoDt = cocoGt.loadRes(predictions_file)

imgIds=sorted(cocoGt.getImgIds())

annType = 'bbox'

# running evaluation
cocoEval = COCOeval(cocoGt, cocoDt, annType)
cocoEval.params.imgIds = imgIds
cocoEval.params.catIds = [1]
cocoEval.analyze_thresholds(save_to_dir='.', confidence_thresholds=[0.5, 0.6, 0.7], catIds=[1])
