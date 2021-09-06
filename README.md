# students-inclassroom-monitoring

![students-inclassroom-monitoring](https://socialify.git.ci/lunarwhite/students-inclassroom-monitoring/image?description=1&descriptionEditable=Monitoring%20of%20the%20number%20of%20students%20in%20classroom%2C%20YOLOv5-based.&font=Raleway&forks=1&issues=1&logo=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Fc%2Fc6%2FPyTorch_logo_black.svg%2F220px-PyTorch_logo_black.svg.png&owner=1&pulls=1&stargazers=1&theme=Light)

Monitoring of the number of students in classroom, YOLOv5-based. || 基于YOLOv5的教室人数监测统计系统，支持输入图片、视频和直播流等多种媒体格式，迁移学习

```
.
├── dataset # 数据集
│   ├── annotations # XML标签
│   ├── images # 图片
│   └── labels # txt标签
├── detect.sh # detect bash脚本
├── hellodata.py # 数据探索、预处理
├── LICENSE
├── README.md
├── res
│   ├── demo_picture1.png # 样例图片
│   └── demo_picture2.png
├── runs
│   ├── detect # 训练后的文件结果
│   └── train # 训练后的权重
├── train.sh # train bash脚本
├── xml2txt.py # 将xml转换为txt标签
└── yolov5 # 从 @ultralytics/yolov5 克隆
    ├── data
    │   ├── coco.yaml
    │   ├── headset.yaml # 自定义训练集
    │   ├── hyp.scratch.yaml
    │   ├── images # 存放detect输入数据
    │   │   ├── bus.jpg
    │   │   └── zidane.jpg
    │   └── videos # 存放detect输入数据
    ├── detect.py
    ├── Dockerfile
    ├── hubconf.py
    ├── models # 预训练模型yaml文件
    │   ├── common.py
    │   ├── experimental.py
    │   ├── export.py
    │   ├── hub # yaml
    │   ├── __init__.py
    │   ├── yolo.py
    │   ├── yolov5l.yaml
    │   ├── yolov5m.yaml
    │   ├── yolov5s.yaml
    │   └── yolov5x.yaml
    ├── requirements.txt # Python依赖库
    ├── test.py
    ├── train.py
    ├── utils
    │   ├── activations.py
    │   ├── autoanchor.py
    │   ├── aws
    │   │   ├── __init__.py
    │   │   ├── mime.sh
    │   │   ├── resume.py
    │   │   └── userdata.sh
    │   ├── datasets.py
    │   ├── flask_rest_api
    │   │   ├── example_request.py
    │   │   ├── README.md
    │   │   └── restapi.py
    │   ├── general.py
    │   ├── google_app_engine
    │   │   ├── additional_requirements.txt
    │   │   ├── app.yaml
    │   │   └── Dockerfile
    │   ├── google_utils.py
    │   ├── __init__.py
    │   ├── loss.py
    │   ├── metrics.py
    │   ├── plots.py
    │   ├── torch_utils.py
    │   └── wandb_logging
    │       ├── __init__.py
    │       ├── log_dataset.py
    │       └── wandb_utils.py
    └── weights # 预训练权重

20 directories, 65 files
```

## 1 概览

- object-detection
- 教室人数检测统计系统，支持输入图片、视频和直播流等多种媒体格式
- 先借助YOLOv5预训练模型对图片数据集进行训练，再测试多种输入流
- 数据集下载：[Classroom Monitoring Dataset - kaggle](https://www.kaggle.com/lunarwhite/classroom-monitoring-dataset)
  - images 图片
    - partA 2000张，格式：[PartA_编号].jpg
    - partB 2405张，格式：[PartB_编号].jpg
  - annotations 标签，标注了图片中 目标的类别和坐标位置
    - partA 2000条，格式：[PartA_编号].xml
    - partB 2405条，格式：[PartB_编号].xml
- 主要工具包版本为PyTorch1.7.1+cu110、和Python 3.8.5

## 2 部署

- 克隆repo：`git clone https://github.com/lunarwhite/students-inclassroom-monitoring.git`
- 更新pip：`pip3 install --upgrade pip`
- 为项目创建虚拟环境：`conda create --name <env_name> python=3.8`
- 激活env：`conda activate <env_name>`
- 安装python库依赖：`pip3 install -r yolov5/requirements.txt`
- 下载部署预训练权重：https://github.com/ultralytics/yolov5/releases，把下载的`.pt`文件 放在`yolov5/weights/`目录下

## 3 运行

- 为了方便执行，手动编写了运行脚本[detect.sh](https://github.com/lunarwhite/students-inclassroom-monitoring/blob/main/detect.sh)和[train.sh](https://github.com/lunarwhite/students-inclassroom-monitoring/blob/main/train.sh)，命令行直接运行`bash train.sh`进行训练，运行`bash detect.sh`进行预测测试。

- 在`train.sh`文件中修改常用参数，如下
  ```python
  --epochs：训练的epoch，默认值300
  --batch-size：默认值16
  --cfg yolov5s.yaml --weights ''：从头开始训练
  --cfg yolov5s.yaml --weights yolov5s.pt：从预训练模型开始训练
  --data：数据集的配置文件，默认为data/coco128.yaml
  --resume：是否从最新的last.pt中恢复训练，布尔值
  --evolve：进化超参数（evolve hyperparameters），布尔值
  --cache-images：缓存图片可以更快的开始训练，布尔值
  --weights：初始化参数路径，默认值''
  --adam：使用adam优化器，布尔值
  ```

- 一般只需改动这两个脚本文件就可，如需训练自定义的数据集，请看官方文档：[Train Custom Models - YOLOv5 Documentation](https://docs.ultralytics.com/tutorials/articles/train-custom-models/)

## 4 流程

- 自定义数据集

- 观察数据
  
  - 数据集大小
  - 数据集样本
  - 图像分辨率
  
- 数据预处理
  
  - 数据清洗，观察发现，有一些图像的label存在缺失，在`XML`转换`TXT`的过程中，一并丢弃
  - YOLOv5原生预处理
  
- 搭建模型，可视化分析

  - 分析与调整训练，提高模型泛化能力

  - demo的detect结果：

    ![demo_picture1.png](https://github.com/lunarwhite/students-inclassroom-monitoring/blob/main/res/demo_picture1.png)

    ![demo_picture2.png](https://github.com/lunarwhite/students-inclassroom-monitoring/blob/main/res/demo_picture2.png)

- 改进模型
  - todo：可视化图形界面
  - todo：优化目录结构，提高封装性

## 5 参考

- https://github.com/ultralytics/yolov5
- [Getting Started - YOLOv5 Documentation](https://docs.ultralytics.com/quick-start/)
- [Train Custom Models - YOLOv5 Documentation](https://docs.ultralytics.com/tutorials/articles/train-custom-models/)
- [Tips for Best Training Results - YOLOv5 Documentation]( https://github.com/ultralytics/yolov5/wiki/Tips-for-Best-Training-Results)
- [Transfer Learning with Frozen Layers - YOLOv5 Documentation](https://github.com/ultralytics/yolov5/issues/1314)
