# $ python train.py --data coco.yaml --cfg yolov5s.yaml --weights '' --batch-size 64
#                                          yolov5m                                40
#                                          yolov5l                                24
#                                          yolov5x                                16
# Train YOLOv5s on headset for 50 epochs
python yolov5/train.py --batch 32 --epochs 50

# saving results to runs/train/
# bash train.sh