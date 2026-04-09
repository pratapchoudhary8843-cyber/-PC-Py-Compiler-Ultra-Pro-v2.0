from PIL import Image, ImageDraw, ImageFont
import math

# Create a 512x512 image
size = 512
img = Image.new('RGBA', (size, size), (10, 14, 39, 255))
draw = ImageDraw.Draw(img)

# Draw gradient background circles for glow effect
for i in range(5, 0, -1):
    radius = 180 + (i * 20)
    alpha = int(30 / i)
    draw.ellipse([size//2 - radius, size//2 - radius, 
                  size//2 + radius, size//2 + radius], 
                 fill=(0, 243, 255, alpha))

# Draw Python snake-like design
# Top snake (cyan)
draw.arc([100, 80, 412, 280], start=180, end=0, 
         fill=(0, 243, 255, 255), width=45)
draw.line([100, 180, 100, 320], fill=(0, 243, 255, 255), width=45)

# Bottom snake (pink)  
draw.arc([100, 232, 412, 432], start=0, end=180,
         fill=(255, 0, 110, 255), width=45)
draw.line([412, 332, 412, 192], fill=(255, 0, 110, 255), width=45)

# Draw eyes
draw.ellipse([130, 140, 160, 170], fill=(10, 14, 39, 255))
draw.ellipse([352, 342, 382, 372], fill=(10, 14, 39, 255))

# Draw code brackets
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 80)
except:
    font = ImageFont.load_default()

draw.text((120, 400), "</>",(0, 243, 255, 150), font=font)

# Draw border
draw.rectangle([5, 5, size-5, size-5], outline=(139, 92, 246, 180), width=6)

# Save the image
img.save('/home/claude/pc-py-compiler-app/assets/icon.png')
print("Icon created successfully!")
