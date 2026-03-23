from ultralytics import YOLO

class IDDetector:

    def __init__(self, model_path, conf=0.5):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect(self, frame):

        results = self.model(frame)[0]

        detections = []

        for box in results.boxes:
            confidence = float(box.conf[0])

            if confidence >= self.conf:
                x1,y1,x2,y2 = map(int, box.xyxy[0])
                detections.append((x1,y1,x2,y2,confidence))

        return detections
