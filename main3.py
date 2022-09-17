from imageai.Detection import VideoObjectDetection
import os
import csv
import sys

ext = ["mp4", "mkv", "avi", "mov"]


def all():
    fl = []
    ld = os.listdir()

    for i in ld:

        j = i.substring('.')

        if j[2] in ext:
            v = r"" + i
        a = i + ","

        def forFrame(frame_number, output_array, output_count):
            global a
            for i in output_array:
                if i['name'] in a:
                    continue
                else:
                    a = a + i['name'] + ";"

        vid_obj_detect = VideoObjectDetection()

        vid_obj_detect.setModelTypeAsYOLOv3()

        vid_obj_detect.setModelPath(r"yolo.h5")

        vid_obj_detect.loadModel(detection_speed="flash")

        detected_vid_obj = vid_obj_detect.detectObjectsFromVideo(
            input_file_path=v,
            save_detected_video=False,
            display_object_name=True,
            per_frame_function=forFrame,
            log_progress=True
        )

        fl.append(a)

    with open('myfile.csv', 'w', newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerows(fl)


def singlerun(v):
    global a
    v = r"" +v
    a = []
    a.append(v)

    def forFrame(frame_number, output_array, output_count):
        d=[]
        for i in output_array:
            if i['name'] not in a:
                a.append(i['name'])
            else:
                continue

    vid_obj_detect = VideoObjectDetection()

    vid_obj_detect.setModelTypeAsYOLOv3()

    vid_obj_detect.setModelPath(r"yolo.h5")

    vid_obj_detect.loadModel(detection_speed="flash")

    detected_vid_obj = vid_obj_detect.detectObjectsFromVideo(
        input_file_path=v,
        output_file_path="/output.mp4",
        save_detected_video=True,
        display_object_name=True,
        per_frame_function=forFrame,
        log_progress=True
    )
    with open('final.csv', 'w', newline='') as file:
        mywriter = csv.writer(file)
        mywriter.writerow(a)
    print(a)




def count():
    def forFull(output_arrays, count_arrays, average_output_count):
        print("hi")
        print("output", output_arrays)
        print(" count arrays", count_arrays)
        print("average", average_output_count)

        #     print("Output count for unique objects : ", output_count)
        #     print("------------END OF A FRAME --------------")
        #     print("FOR FRAME ", frame_number)
        #     print("Output for each object : ", output_array)

    vid_obj_detect = VideoObjectDetection()
    vid_obj_detect.setModelTypeAsYOLOv3()
    vid_obj_detect.setModelPath(r"yolo.h5")
    vid_obj_detect.loadModel(detection_speed="flash")
    detected_vid_obj = vid_obj_detect.detectObjectsFromVideo(
        input_file_path=r"input_video.mp4",
        # frames_per_second=30,
        save_detected_video=False,
        display_object_name=True,
        video_complete_function=forFull,
        # per_minute_function=forFrame1,
        log_progress=True
    )


def custom(v,o):
    global a
    v = r"" + v
    a = []
    a.append(v)

    def forFrame(frame_number, output_array, output_count):
        d = []
        for i in output_array:
            if i['name'] not in a:
                a.append(i['name'])
            else:
                continue

    vid_obj_detect = VideoObjectDetection()

    vid_obj_detect.setModelTypeAsYOLOv3()

    vid_obj_detect.setModelPath(r"yolo.h5")

    vid_obj_detect.loadModel(detection_speed="flash")

    detected_vid_obj = vid_obj_detect.detectCustomObjectsFromVideo(
        input_file_path=v,
        output_file_path=r"output",
        save_detected_video=True,
        display_object_name=True,
        per_frame_function=forFrame,
        log_progress=True,
        custom_objects=o
    )
    with open('final.csv', 'w', newline='') as file:
        mywriter = csv.writer(file)
        mywriter.writerow(a)
    print(a)

if sys.argv[1]=="custom":
    videoName = sys.argv[2]
    objectName = sys.argv[3]
    custom(videoName,objectName)
elif sys.argv[1] == "all":
    videoName = sys.argv[2]
    singlerun(videoName);
else:
    print("Unexpected error")