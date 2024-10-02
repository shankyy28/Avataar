import numpy as np
import cv2
from models.sam_model import import_sam
from models.yolo_model import import_yolo
from segment_anything import SamPredictor

def fetch_class(image_bgr, class_name, yolo):
    predictions = yolo.predict(image_bgr)
    result = []

    # Fetching the bouning boxes of required class
    for prediction in predictions:
        names = prediction.names
        for bbox in prediction.boxes:
            name = names[int(bbox.cls[0])]
            if name == class_name:
                x1, y1, x2, y2 = bbox.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                result = [x1, y1, x2, y2]
    return result

def red_mask(image_bgr, bbox, sam):
    # Making a SAM model to segment the bounding box
    mask_predictor = SamPredictor(sam)
    
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    mask_predictor.set_image(image_rgb)

    box = np.array(bbox)

    masks, _, _ = mask_predictor.predict(box = box, multimask_output = False)

    # Making a red mask on same image size as input
    red_mask = np.zeros_like(image_rgb)
    red_mask[masks[0]] = [255, 0, 0]

    # Blending the red mask with image
    result = cv2.addWeighted(image_rgb, 1, red_mask, 0.5, 0)
    return result, red_mask

def create_mask(input_image_path, class_name, output_image_path):
    # Importing models and checking if they're loaded properly or not
    try:
        yolo = import_yolo()
        print("YOLO MODEL LOADED!")
    except Exception as e:
        print("YOLO model couldn't be loaded")

    try:
        sam = import_sam()
        print("SAM MODEL LOADED!")
    except Exception as e:
        print("SAM model couldn't be loaded")

    image_bgr = cv2.imread(input_image_path)

    # Fetching the bounding boxes of the required class
    bbox = fetch_class(image_bgr, class_name, yolo)

    if bbox == []:
        print("The required class could not be predicted by the model")
        return

    # Making a red masked image
    red_mask_image_rgb, masks = red_mask(image_bgr, bbox, sam)

    red_mask_image_bgr = cv2.cvtColor(red_mask_image_rgb, cv2.COLOR_RGB2BGR)

    # Previewing the red masked image
    cv2.imshow("Image", red_mask_image_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return image_bgr, masks