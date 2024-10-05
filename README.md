# Object Pose Editing in Scene Images

This project aims to develop a user-friendly tool for editing the pose of objects in scene images using generative AI techniques. It's particularly useful for post-production editing of product photographs, such as polishing scenes for e-commerce websites.

## Project Overview

The project consists of two main tasks:

1. **Object Segmentation**: Segment a user-specified object in a given scene using a class prompt.
2. **Pose Editing**: Edit the pose of the segmented object based on user-defined parameters (e.g., Azimuth and Polar angles).


## Features

- Object segmentation using YOLO and SAM (Segment Anything Model)
- Command-line interface for easy use
- Visualization of segmented objects

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/shankyy28/Avataar.git
   cd object-pose-editing
   ```

2. Install the required dependencies:
   ```
   pip install requirements.txt
   ```

3. Download the necessary model weights for YOLO and SAM.
-> YOLO will download the weights on its own and SAM can be downloaded from hugging face

## Usage

Run the main script with the following command:

```
python run.py --image <path_to_input_image> --class <object_class> --azimuth <degrees> --polar <degrees> --output <path_to_output_image>
```

Example:
```
python run.py --input_image.jpg --class "chair" --azimuth +10 --polar -5 --output generated.jpg
```

## Project Structure

- `run.py`: Main script to run the project
- `parse_input.py`: Handles command-line argument parsing
- `create_mask.py`: Contains functions for object segmentation
- `view_rotation.py`: Will handle pose editing

## Acknowledgements

- YOLO (You Only Look Once) for object detection
- SAM (Segment Anything Model) for image segmentation

## Input_image

- ![chair](https://github.com/user-attachments/assets/70afe8bd-eb73-49d5-9d18-0aa662bba41c)

## Red Masked output

- ![generated](https://github.com/user-attachments/assets/dbe58860-2a1d-4817-b2f9-e65e4a007cdb)

