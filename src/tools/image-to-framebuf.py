from PIL import Image

def convert_image_to_framebuffer(image_path):
    image = Image.open(image_path).convert('1')  # Convert to 1-bit pixels, black and white
    image = image.resize((128, 64))  # Resize to 128x64 pixels
    pixels = image.load()

    framebuffer = []
    for y in range(64):
        byte = 0
        for x in range(128):
            if pixels[x, y] == 0:  # Black pixel
                byte |= (1 << (x % 8))
            if (x % 8) == 7 or x == 127:
                framebuffer.append(byte)
                byte = 0

    return framebuffer

image_path = 'path_to_your_image.png'
framebuffer = convert_image_to_framebuffer(image_path)
print(framebuffer)
