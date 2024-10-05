import numpy as np
from zero123 import zero123

def view_rotation(image, mask, azimuth, polar):

    input_image = image
    input_mask = mask

    camera_pose = Camera(
        azimuth = azimuth,
        polar = polar,
    )

    output = model(
        image=input_image,
        mask=input_mask,
        num_inference_steps = 50,
        guidance_scale = 7.5,
        camera_pose = camera_pose)

    generated_image = output.images[0]