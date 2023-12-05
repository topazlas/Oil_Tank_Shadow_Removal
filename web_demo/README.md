# Oil Tank Shadow Removal(OTSR) Web Demo

## Environment Configuration

Ensure you have the following environment set up:

- **Python:** 3.8.0
- **CUDA:** 11.1
- **PyTorch:** 1.8.0

You can create the environment using the provided YAML file:

```bash
conda env create -f environment.yaml
conda activate OTSR_Web_Demo
```
Navigate to the OTSR directory:

```bash
cd OTSR_Web_Demo
python web_demo.py
```
http://127.0.0.1:8000/index

Input and Output Paths
- **Input Image Path:** \static\uploads
- **Mask Image Path:** \static\mask
- **Output Image Path:** \static\output

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

[![test](http://img.youtube.com/vi/d4pCRPrmvK0/0.jpg)](https://youtu.be/d4pCRPrmvK0?t=0s) 

## References
1. [GuoLanqing/ShadowFormer](https://github.com/guolanqing/shadowformer#visual-results)
2. [YOLOv8](https://docs.ultralytics.com/ko/)
3. [kaggle/Oil Storage Tanks](https://www.kaggle.com/datasets/towardsentropy/oil-storage-tanks)
