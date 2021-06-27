from PIL import Image

images = []

hand = input("Please input hand: ")
hand_length = 0

folder = "hai"
filenames = []
kakan_idx = []
seperates = []

tiles = []
for c in hand.split()[0]:
    if c.isdigit():
        tiles.append(c)
        hand_length += 1
    elif c.isalpha():
        tiles = [num+c for num in tiles]
        for tile in tiles:
            filenames.append(f"{folder}/{tile}.png")
        tiles = []

seperates.append(hand_length-1)

for file in filenames:
    images.append(Image.open(file))

i = 0
tiles = []
call = " ".join(hand.split()[1:])
while i < len(call):
    c = call[i]
    if c == "p":
        from_whom = call[i+1]
        idx = 0
        if from_whom == "l":
            idx = 0
        elif from_whom == "m":
            idx = 1
        elif from_whom == "r":
            idx = 2
        i += 2

        name = call[i:i+2]
        name = f"{folder}/{name}.png"
        i += 2
        for j in range(0, 3):
            if j == idx:
                img = Image.open(name)
                rotated = Image.new("RGBA", (img.size[1], img.size[1]))
                rotated.paste(img.rotate(90, expand=True), (0, img.size[1]-img.size[0]))
                images.append(rotated)
            else:
                img = Image.open(name)
                images.append(img)
        seperates.append(seperates[-1]+3)
    elif c == "c":
        from_whom = call[i+1]
        idx = 0
        if from_whom == "l":
            idx = 0
        elif from_whom == "m":
            idx = 1
        elif from_whom == "r":
            idx = 2
        i += 2

        names = [call[i], call[i+1], call[i+2]]
        names = [f"{folder}/{name+call[i+3]}.png" for name in names]
        i += 3
        for j in range(0, 3):
            if j == idx:
                img = Image.open(names[j])
                rotated = Image.new("RGBA", (img.size[1], img.size[1]))
                rotated.paste(img.rotate(90, expand=True), (0, img.size[1]-img.size[0]))
                images.append(rotated)
            else:
                img = Image.open(names[j])
                images.append(img)
        seperates.append(seperates[-1]+3)
    elif c == "k":

        mode = call[i+1]
        i += 1

        idx = 0
        if mode != "a" or mode != "k":
            from_whom = call[i+1]
            if from_whom == "l":
                idx = 0
            elif from_whom == "m":
                idx = 1
            elif from_whom == "r":
                idx = 3
        if mode == "k":
            from_whom = call[i+1]
            if from_whom == "l":
                idx = 0
            elif from_whom == "m":
                idx = 1
            elif from_whom == "r":
                idx = 2
        if mode != "a":
            i += 2
        else:
            i += 1

        if mode == "a":
            name = call[i:i+2]
            name = f"{folder}/{name}.png"
            images.append(Image.open(f"{folder}/b.png"))
            images.append(Image.open(name))
            images.append(Image.open(name))
            images.append(Image.open(f"{folder}/b.png"))
            i += 1
            seperates.append(seperates[-1]+4)
        elif mode == "k":
            name = call[i:i+2]
            name = f"{folder}/{name}.png"
            for j in range(3):
                if j == idx:
                    kakan_idx.append(len(images))

                    img = Image.open(name)
                    rotated = Image.new("RGBA", (img.size[1], 2*img.size[0]))
                    rotated.paste(img.rotate(90, expand=True), (0, 0))
                    rotated.paste(img.rotate(90, expand=True), (0, img.size[0]))
                    images.append(rotated)
                else:
                    img = Image.open(name)
                    images.append(img)
            i += 2
            seperates.append(seperates[-1]+3)
        elif mode == "m":
            name = call[i:i+2]
            name = f"{folder}/{name}.png"
            i += 2
            for j in range(4):
                if j == idx:
                    img = Image.open(name)
                    rotated = Image.new("RGBA", (img.size[1], img.size[1]))
                    rotated.paste(img.rotate(90, expand=True), (0, img.size[1]-img.size[0]))
                    images.append(rotated)
                else:
                    img = Image.open(name)
                    images.append(img)
            seperates.append(seperates[-1]+4)

    i += 1

widths, heights = zip(*(img.size for img in images))
total_width = sum(widths)
if call != "":
    total_width += max(widths)*(len(seperates)-1)

max_height  = max(heights)

new_image = Image.new("RGBA", (total_width, max_height))

x_offset = 0
y_offset = max(heights)-max(widths) if len(kakan_idx) > 0 else 0

seperates.pop()
for i, img in enumerate(images):
    if i in kakan_idx:
        new_image.paste(img, (x_offset, 0))
    else:
        new_image.paste(img, (x_offset, y_offset))

    if i in seperates:
        x_offset += max(widths) + img.size[0]
    else:
        x_offset += img.size[0]

new_image.save(f"{hand}.png")