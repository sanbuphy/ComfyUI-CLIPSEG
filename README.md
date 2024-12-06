[中文版](README_zh.md)
[English](README.md)

# Custom Nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI): CLIPSeg and CombineSegMasks

##  utilize [CLIPSeg model](https://huggingface.co/docs/transformers/main/en/model_doc/clipseg) to generate masks for image inpainting tasks based on text prompts.


### 1. CLIPSeg
The CLIPSeg node generates a binary mask for a given input image and text prompt.

**Inputs:**

- image: A torch.Tensor representing the input image.
- text: A string representing the text prompt.
- blur: A float value to control the amount of Gaussian blur applied to the mask (0-15, default: 7).
- threshold: A float value to control the threshold for creating the binary mask (0-1, default: 0.4).
- dilation_factor: An integer value to control the dilation of the binary mask (0-10, default: 4).

**Outputs:**

- mask: A torch.Tensor representing the soft mask with smooth edges.
- hard_mask: A torch.Tensor representing the binary mask with hard edges.

### 2. CombineSegMasks
The CombineSegMasks node combines two masks into a single mask.

**Inputs:**

- mask1: A torch.Tensor representing the first mask.
- mask2: A torch.Tensor representing the second mask.

**Outputs:**

- mask: A torch.Tensor representing the combined mask.


## Installation
To use these custom nodes in your ComfyUI project, follow these steps:

1. Clone this repository to ComfyUI/custom_nodes/
2. Ready to use

## Usage
Below is an example for the intended workflow. 
The [json file](workflow/workflow_clipseg.json) for the example can be found inside the 'workflow' directory. 
![](workflow/workflow_clipseg.png)

## Reference

Thanks to https://github.com/biegert/ComfyUI-CLIPSeg