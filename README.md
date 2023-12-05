# Oil Tank Shadow Removal(OTSR)

## Overview
Python script that uses the yolov8 model to detect shadows in crude oil storage tanks from satellite or aerial photographs and extract shadow masks to remove only shadows in crude oil storage tanks using shadow removal models

## Environment Configuration

Ensure you have the following environment set up:

- **Python:** 3.8.0
- **CUDA:** 11.1
- **PyTorch:** 1.8.0

You can create the environment using the provided YAML file:

```bash
conda env create -f environment.yaml
conda activate OTSR
```
Navigate to the OTSR directory:

```bash
cd OTSR
python final_main.py
```

Input and Output Paths
- **Input Image Path:** /Dataset/test/test_A
- **Mask Image Path:** /Dataset/test/test_B
- **Output Image Path:** /results

**Note**: The input image should be a 512x512 PNG file.

### Download the Model File

Download the required model file from the following link: [OTSR Model](https://drive.google.com/file/d/1FzcBA5OUFJO3LeUpQDlu-LFemi3totcK/view?usp=sharing)


### For additional development information, please refer to this [link](https://corbinyim.notion.site/Oil-Storage-Tank-Shadow-Removal-acf15dd4a47649c6a0df93ce72d76c58?pvs=4).


## Inference Results

### Source Image
<img src="/Dataset/test/test_A/99_3_7.png" width="512px" height="512px" title="A" alt="Source Image"></img><br/>

### Inferred Image
<img src="/results/99_3_7.png" width="512px" height="512px" title="B" alt="Result Image"></img><br/>

## Video Demonstration
Check out the implementation in action in the following video:

[![test](http://img.youtube.com/vi/2AyVU8FcxNs/0.jpg)](https://youtu.be/2AyVU8FcxNs?t=0s) 

## References
1. [GuoLanqing/ShadowFormer](https://github.com/guolanqing/shadowformer#visual-results)
2. [YOLOv8](https://docs.ultralytics.com/ko/)
3. [kaggle/Oil Storage Tanks](https://www.kaggle.com/datasets/towardsentropy/oil-storage-tanks)


## License
All code and documentation in this project are available under the [MIT License](https://opensource.org/licenses/MIT).
See the [LICENSE file](./LICENSE) for details.
