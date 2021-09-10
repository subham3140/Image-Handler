from django.db import models
from PIL import Image, ImageEnhance
FLIP_TO = [
    ("flip left right", "FLIP LEFT RIGHT"),
    ("flip top bottom", "FLIP TOP BOTTOM")
]

ROTATE_TO = [
    ("rotate 90", "ROTATE 90"),
    ("rotate 180", "ROTATE 180"),
    ("rotate 270", "ROTATE 270"),
]

COLOR_TRANSFORM = [
    ("l", "L"),
    ("rbg", "RBG"),
    ("cmyk", "CMYK (cyan, magenta, yellow, black)")
]

class ImagePro(models.Model):
   imagetitle = models.CharField(max_length=500, blank=True, null=True, default="new image")
   image = models.ImageField(upload_to="images")
   rotate_by = models.CharField(max_length=500, choices=ROTATE_TO, null=True, blank=True)
   flip_to = models.CharField(max_length=500, choices=FLIP_TO, blank=True, null=True)
   color_transform = models.CharField(max_length=500, choices=COLOR_TRANSFORM, null=True, blank=True)
   created = models.DateField(auto_now_add=True)

   def __str__(self):
       return f'{self.imagetitle} - {self.pk}'

   def resize(self, width, height):
       if(width == 0 or height == 0):
           return
       img = Image.open(self.image.path)
       img = img.resize((width, height))
       img.save(self.image.path)

   def rotate(self, rotateval):
       if rotateval == 0:
           return
       img = Image.open(self.image.path)
       img = img.rotate(rotateval)
       img.save(self.image.path)

   def flip(self, flipto):
       if flipto == "":
           return
       flip = ""   
       if flipto == "flip left right":
            flip = Image.FLIP_LEFT_RIGHT
       elif flipto == "flip top bottom":
            flip = Image.FLIP_TOP_BOTTOM
       image = Image.open(self.image.path)
       image = image.transpose(flip)
       image.save(self.image.path)

   def enhance(self, enhance_val):
       if enhance_val == 0:
           return
       image = Image.open(self.image.path)
       image = ImageEnhance.Contrast(image)
       image.enhance(enhance_val).save(self.image.path)

   def colorTransform(self, transform_to):
       if transform_to == "":
           return
       col_trans = ""
       if transform_to == "l":
           col_trans = "L"
       elif transform_to == "rbg":
           return
       elif transform_to == "cmyk":
           col_trans = "CMYK"            
       image = Image.open(self.image.path)
       image = image.convert(col_trans)
       image.save(self.image.path)

   def quality(self, quality):
       if quality == 0:
           return
       image = Image.open(self.image.path)
       image.save(self.image.path, quality=quality)


