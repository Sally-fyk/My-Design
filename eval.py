import sys
from utils import extract_classifiers 
from eval.captioner import * 
from eval.coco_eval import *
#from eval import eval_sentences
from dcc_transfer import transfer_weights
import argparse
import pdb 
from utils.config import *
import h5py

def generate(args):
  print "main"
  save_caps = '/root/noc/caption-eval/COCO_beam1.txt.json'
  gt_json = coco_annotations + 'captions_%s2014.json' %args.split
  gt_template_novel = coco_annotations + 'captions_split_set_%s_%s_novel2014.json'
  gt_template_train = coco_annotations + 'captions_split_set_%s_%s_train2014.json'

  print "Scores over entire dataset..."
#  score_generation(gt_json, save_caps)

  print "Scores over word splits..."
  new_words = ['bus', 'bottle', 'couch', 'microwave', 'pizza', 'racket', 'suitcase', 'zebra']
  score_dcc(gt_template_novel, gt_template_train, save_caps, new_words, 'val_test')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", type=str, default='val_test')
    args = parser.parse_args()
    generator = generate(args)