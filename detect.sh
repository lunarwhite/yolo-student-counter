# $ python detect.py --source 0  # webcam
#                             file.jpg  # image 图片
#                             file.mp4  # video 视频
#                             path/  # directory 
#                             path/*.jpg  # glob
#                             'https://youtu.be/NUsoVlDFqZg'  # YouTube video
#                             'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream 直播流
python yolov5/detect.py --weights runs/train/exp/weights/best.pt

# saving results to runs/detect/
# bash detec