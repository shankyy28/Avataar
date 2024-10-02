import argparse

def parse_input():
    parser = argparse.ArgumentParser(description="Process an image with a specified class and generate output.")

    parser.add_argument('--image', type=str, required=True, help="Path to the input image file")
    parser.add_argument('--class', type=str, required=True, help="Class to process the image with")
    parser.add_argument('--azimuth', type=int, required=True, help="Horizontal shift in degrees to the image")
    parser.add_argument('--polar', type=int, required=True, help="Vertical shift in degrees to the image")
    parser.add_argument('--output', type=str, required=True, help="Path to save the generated output image")

    args = parser.parse_args()

    input_image_path = args.image
    class_name = getattr(args, 'class')  # 'class' is a reserved keyword, so we use getattr
    output_image_path = args.output
    azimuth = args.azimuth
    polar = args.polar

    return input_image_path, class_name, output_image_path, azimuth, polar