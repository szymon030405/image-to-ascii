from PIL import Image

file = open("image_ascii.txt", 'w')

with Image.open("lebron.jpg") as image:
    for y in range(image.height):
        line = ""

        print(image.size)

        for x in range(image.width):
            rgb = image.getpixel((x,y))
            sum = rgb[0] + rgb[1] + rgb[2]

            if sum < 100:
                char = '! '
            elif sum < 200:
                char = '? '
            elif sum < 300:
                char = '/ '
            elif sum < 400:
                char = '£ '
            elif sum < 500:
                char = '@ '
            elif sum < 600:
                char = '$ '
            elif sum < 800:
                char = '# '

            line += char

        file.write(f'{line}\n')