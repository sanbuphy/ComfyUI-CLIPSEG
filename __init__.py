import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from clipseg_model.clipseg import CLIPSeg, CombineMasks

NODE_CLASS_MAPPINGS = {
    "CLIPSeg": CLIPSeg,"CombineSegMasks": CombineMasks,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "CLIPSeg": "CLIPSeg", "CombineSegMasks": "CombineSegMasks",
}

all = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']