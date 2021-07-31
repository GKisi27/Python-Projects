from PIL import Image
import os

#Logo destination
logo_dest = "C:\\Users\Promech-PC-5\Desktop" #Source path of your logo

#Change directory to the logo destination
os.chdir(logo_dest)

#Open logo image
logo = Image.open("firebird.png")

#Images destination (Images in which we are going to add logo)
img_source = "C:\\Users\Promech-PC-5\Desktop\WallpaperPC"

#Change directory to the images destination
os.chdir(img_source)

for i, img in enumerate(os.listdir()):
    #Open each image
    im = Image.open(img)
    #Resizing logo according to size of image
    basewidth = int(im.size[0]/10)
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int(float(logo.size[1])*float(wpercent))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    
    #Checking whethe all files are images or not.
    ext = img.split(".")[-1]
    valid_ext = ["jpg", "png", "svg", "jpeg", "gif"]
    if ext.lower() in valid_ext:
        #Area of image, where we add the logo. Here it is top right corner
        position = (int(im.size[0]-logo.size[0]),0)
        #Pasting logo over image
        im.paste(logo, position)
        #Saving the image with logo with new name in new folder
        im.save("C:\\Users\Promech-PC-5\Desktop\WallpaperPCwithLogo"+"/Image"+str(i)+"."+ ext)