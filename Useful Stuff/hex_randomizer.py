import random

def rgb(hex):
    r = int(hex[:2], 16)
    g = int(hex[2:4], 16)
    b = int(hex[4:], 16)
    return r, g, b
def hsl(r, g, b):
    rP, gP, bP = r/255, g/255, b/255

    cMax = max(rP, gP, bP)
    cMin = min(rP, gP, bP)

    chroma = cMax - cMin
    lightness = ((cMax + cMin) / 2)

    if chroma == 0:
        return 0, 0, lightness * 100

    saturation = (chroma / (1 - abs((lightness * 2) - 1))) * 100
    lightness *= 100

    if cMax == rP:
        hue = 60 * (((gP - bP) / chroma) % 6)
    elif cMax == gP:
        hue = 60 * (((bP - rP) / chroma) + 2)
    else:
        hue = 60 * (((rP - gP) / chroma) + 4)

    return hue, saturation, lightness
def return_to_hex(hue, saturation, lightness):
    saturation /= 100
    lightness /= 100

    chroma = (1 - abs((lightness * 2) - 1)) * saturation
    intermediate = chroma * (1 - abs(((hue/60) % 2) - 1))
    light_match = lightness - (chroma / 2)

    if 0 <= hue < 60:
        r1, g1, b1 = chroma, intermediate, 0
    elif 60 <= hue < 120:
        r1, g1, b1 = intermediate, chroma, 0
    elif 120 <= hue < 180:
        r1, g1, b1 = 0, chroma, intermediate
    elif 180 <= hue < 240:
        r1, g1, b1 = 0, intermediate, chroma
    elif 240 <= hue < 300:
        r1, g1, b1 = intermediate, 0, chroma
    else:
        r1, g1, b1 = chroma, 0, intermediate

    r_new = max(min(int((r1 + light_match) * 255), 255), 0)
    g_new = max(min(int((g1 + light_match) * 255), 255), 0)
    b_new = max(min(int((b1 + light_match) * 255), 255), 0)

    return (f"{r_new:02x}{g_new:02x}{b_new:02x}")
def vary(h_vary, s_vary, l_vary, hue, saturation, lightness):
    new_hue = min(360, max(0, hue + random.randint(-h_vary, h_vary)))
    new_saturation = min(100, max(0, saturation + random.randint(-s_vary, s_vary)))
    new_lightness = min(100, max(0, lightness + random.randint(-l_vary, l_vary)))

    return new_hue, new_saturation, new_lightness

while True:
    hex = input("Type your color hex code:\n>").lower()

    if hex[0] in "# ":
        hex = hex[1:]

    if len(hex) != 6:
        print("Invalid hex code\n")
        continue

    for i in hex:
        if i not in "1234567890abcdef":
            print("Invalid hex code\n")
            break
    else:
        r, g, b = rgb(hex)
        hue, saturation, lightness = hsl(r, g, b)

        print(f"\nThe provided hex code converted to HSL is:\n\nHue: {round(hue)}\nSaturation: {round(saturation)}\nLightness: {round(lightness)}\n")

        while True:
            variation = input("How much would you like to vary each value? (H, S, L)\n> ")
            
            valid = True
            for i in variation:
                if i not in "0123456789, ":
                    print(f"Invalid character: {i}")
                    valid = False
                    break
            if valid:
                break

        parts = variation.split(",")

        h_vary = int(parts[0].strip())
        s_vary = int(parts[1].strip())
        l_vary = int(parts[2].strip())

        while True:
            count = input("How many hex codes?\n> ")

            if count.isdigit():
                count = int(count)
                break
            else:
                print("Must be a number.")

        for i in range(count):
            new_hue, new_saturation, new_lightness = vary(h_vary, s_vary, l_vary, hue, saturation, lightness)
            print(return_to_hex(new_hue, new_saturation, new_lightness))
        print()