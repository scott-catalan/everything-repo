'''
# Project Creation Date: 6:21:32 PM, 2/6/2026
'''

import colorsys, random

def validate_hex(hex):
    if len(hex) not in (6, 7):
        return False
    
    if hex[0] in "#":
        hex = hex[1:]

    hex = hex.lower()

    for i in hex:
        if i not in "1234567890abcdef":
            return False

    return True

def hex_to_hsl(hex):
    r = int(hex[:2], 16)
    g = int(hex[2:4], 16)
    b = int(hex[4:], 16)

    h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
    h, l, s = round(h*360, 1), round(l*100, 1), round(s*100, 1)

    return h, s, l

def scatter_color(hex, h_pos, h_neg, l_pos, l_neg, s_pos, s_neg):
    r = int(hex[:2], 16)
    g = int(hex[2:4], 16)
    b = int(hex[4:], 16)
    
    h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
    
    h, l, s = h*360, l*100, s*100
    count = 9
    results = []
    
    for i in range(count):
        h_new = (h + random.uniform(-h_neg, h_pos)) % 360
        l_new = max(0, min(100, l + random.uniform(-l_neg, l_pos)))
        s_new = max(0, min(100, s + random.uniform(-s_neg, s_pos)))
        
        r, g, b = colorsys.hls_to_rgb(h_new/360, l_new/100, s_new/100)
        r, g, b = int(r * 255), int(g * 255), int(b * 255)
        
        results.append(f"{r:02x}{g:02x}{b:02x}")
    
    return results