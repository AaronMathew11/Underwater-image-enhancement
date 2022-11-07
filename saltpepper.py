# Importing Image and ImageFilter module from PIL package  
from PIL import Image, ImageFilter 
     
# creating a image object 
im1 = Image.open(r"./erock_gray.jpg") 
     
# applying the mode filter 
im2 = im1.filter(ImageFilter.ModeFilter(size = 3)) 
     
im2.show() 