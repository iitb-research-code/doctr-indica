import os
import torch
from enum import Enum

torch.cuda.empty_cache()


### Path to the Data and Results directories
INPUT_DATA_DIR = "../data/doctr-detection/Archive/val"  #'./../processed/docbank_100/'
RESULTS_DATA_DIR = "../results-dataprogramming"

### class for defining the format of the groundtruth
class GroundTruthFormat(Enum):
    DocBank = 1
    DocTR = 2


### Keep True if True labels are available, else False
GROUND_TRUTH_AVAILABLE = False #True

### Path to images and the ground truths
INPUT_IMG_DIR = "/media/ashatya/Data/work/iit-bombay/media/my_pictures/" #os.path.join(INPUT_DATA_DIR, "images/")
GROUND_TRUTH_DIR = "../csvs-dataprogramming/"  # os.path.join(INPUT_DATA_DIR, 'txt/')


### Directories for resultant predictions
RESULT_VALUE = 35
RESULTS_DIR = os.path.join(RESULTS_DATA_DIR, "cage/results" + str(RESULT_VALUE) + "/")
OUT_TXT_DIR = os.path.join(RESULTS_DATA_DIR, "txt/txt" + str(RESULT_VALUE) + "/")
PREDICTIONS_DIR = os.path.join(
    RESULTS_DATA_DIR, "predictions/predictions" + str(RESULT_VALUE) + "/"
)


# Create a new directory if it does not exist already
if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)
    os.makedirs(OUT_TXT_DIR)
    os.makedirs(PREDICTIONS_DIR)


### Hyperparameters for Shrinkage threshold on LF outputs
WIDTH_THRESHOLD = 0.90
HEIGHT_THRESHOLD = 0.75

### Hyperparameter for Contour thickness to generate bboxes
THICKNESS = 4

### This is used when already DL model results are present, to save time
ANN_DOCTR_DIR = "./../testing_sample/doctr_txt/"

### Used in MASK model LF to change intensity as hyperparameter
LUMINOSITY = 1.0

### Choose the Labeling Functions which should be run
lab_funcs = [ 
   "CONVEX_HULL_LABEL_PURE", 
   # "CONVEX_HULL_LABEL_NOISE", 
   # "EDGES_LABEL", 
   # "EDGES_LABEL_REVERSE", 
   # "PILLOW_EDGES_LABEL", 
   # "PILLOW_EDGES_LABEL_REVERSE",
   "DOCTR_LABEL",
   # "TESSERACT_LABEL",
   "CONTOUR_LABEL",
   # "MASK_HOLES_LABEL",
   # "MASK_OBJECTS_LABEL",
   # "SEGMENTATION_LABEL"
]



DICT_LAB_FUNCS = {
    
}

QUALITY_GUIDE = [0.85, 0.9, 0.95]