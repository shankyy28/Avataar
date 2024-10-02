from parse_input import parse_input
from create_mask import create_mask
from view_rotation import view_rotation

def main():
    # Fetching the inputs
    input_image_path, class_name, output_image_path, azimuth, polar = parse_input()

    image_bgr, masks = create_mask(input_image_path = input_image_path,
                                   class_name = class_name,
                                   output_image_path = output_image_path)
    
    view_rotation(image_bgr, masks, azimuth, polar)
    
if __name__ == "__main__":
    main()