import discord
from discord.ext import commands
import os
import math
import asyncio
from cogs.utils.dataIO import dataIO
import PIL
from PIL import Image
import glob, os
from PIL import ImageEnhance
from PIL import ImageColor
from PIL import ImageFilter
from PIL import ImageOps
from PIL import ImageFont
from PIL import ImageDraw
import requests
from io import BytesIO
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

WINDOWS_OS = os.name == 'nt'

class imagefilter:
    """Allows for various image filtering"""

    def __init__(self, bot):
        self.bot = bot
        if not os.path.exists("data/imagefilter"):
            os.makedirs("data/imagefilter")
        self.path = os.path.join("data", "imagefilter")

        
    @commands.command(pass_context=True)
    async def invert(self, ctx, link):
        """Inverts the given image."""

        if any(word in ".BMP .EPS .GIF .ICNS .IM .JPEG .MSP .PCX .PNG .PPM .SPIDER .TIFF .WebP .XBM .CUR .DCX .DDS .FLI .FLC .FPX .FTEX .GBR .GD .ICO .IMT .IPTC .NAA .MCIDAS .MIC .MPO .PCD .PIXAR .PSD .SGI .TGA .WAL .XPM .PALM .PDF .BUFR .FITS .GRIB .HDF5 .MPEG .WMF .bmp .eps .gif .icns .im .jpeg .msp .pcx .png .ppm .spider .tiff .webp .xbm .cur .dcx .dds .fli .flc .fpx .ftex .gbr .gd .ico .imt .iptc .naa .mcidas .mic .mpo .pcd .pixar .psd .sgi .tga .wal .xpm .palm .pdf .bufr .fits .grib .hdf5 .mpeg .wmf" for word in link):
        
            id = ctx.message.author.id
            channel = ctx.message.channel
            response = requests.get(link)
            image = Image.open (BytesIO(response.content))
        
            image = image.convert("RGB")
       	    image = ImageOps.invert(image)
            image.save(self.path + "/" + id + ".jpg", quality=100)
       	    await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
            os.remove(self.path + "/" + id + ".jpg")
        else:
            await self.bot.say("Sorry, but this image format is not supported.")
            
    @commands.command(pass_context=True)
    async def rotate(self, ctx, link, degrees):
        """Rotates the given image."""

        if any(word in ".BMP .EPS .GIF .ICNS .IM .JPEG .MSP .PCX .PNG .PPM .SPIDER .TIFF .WebP .XBM .CUR .DCX .DDS .FLI .FLC .FPX .FTEX .GBR .GD .ICO .IMT .IPTC .NAA .MCIDAS .MIC .MPO .PCD .PIXAR .PSD .SGI .TGA .WAL .XPM .PALM .PDF .BUFR .FITS .GRIB .HDF5 .MPEG .WMF .bmp .eps .gif .icns .im .jpeg .msp .pcx .png .ppm .spider .tiff .webp .xbm .cur .dcx .dds .fli .flc .fpx .ftex .gbr .gd .ico .imt .iptc .naa .mcidas .mic .mpo .pcd .pixar .psd .sgi .tga .wal .xpm .palm .pdf .bufr .fits .grib .hdf5 .mpeg .wmf" for word in link):
        
            id = ctx.message.author.id
            channel = ctx.message.channel
            response = requests.get(link)
            image = Image.open (BytesIO(response.content))
        
            image = image.convert("RGB")
       	    image = image.rotate(int(degrees), expand=true)
            image.save(self.path + "/" + id + ".jpg", quality=100)
       	    await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
            
    @commands.command(pass_context=True)
    async def crop(self, ctx, link, pixels):
        """crops the given image by however many pixels you specify."""

        if any(word in ".BMP .EPS .GIF .ICNS .IM .JPEG .MSP .PCX .PNG .PPM .SPIDER .TIFF .WebP .XBM .CUR .DCX .DDS .FLI .FLC .FPX .FTEX .GBR .GD .ICO .IMT .IPTC .NAA .MCIDAS .MIC .MPO .PCD .PIXAR .PSD .SGI .TGA .WAL .XPM .PALM .PDF .BUFR .FITS .GRIB .HDF5 .MPEG .WMF .bmp .eps .gif .icns .im .jpeg .msp .pcx .png .ppm .spider .tiff .webp .xbm .cur .dcx .dds .fli .flc .fpx .ftex .gbr .gd .ico .imt .iptc .naa .mcidas .mic .mpo .pcd .pixar .psd .sgi .tga .wal .xpm .palm .pdf .bufr .fits .grib .hdf5 .mpeg .wmf" for word in link):
        
            id = ctx.message.author.id
            channel = ctx.message.channel
            response = requests.get(link)
            image = Image.open (BytesIO(response.content))
        
            image = image.convert("RGB")
       	    image = ImageOps.crop(image, int(pixels))
            image.save(self.path + "/" + id + ".jpg", quality=100)
       	    await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
            os.remove(self.path + "/" + id + ".jpg")
            
    @commands.command(pass_context=True)
    async def expand(self, ctx, link, pixels, color):
        """expands the given image's border by however many pixels you specify."""

        if any(word in ".BMP .EPS .GIF .ICNS .IM .JPEG .MSP .PCX .PNG .PPM .SPIDER .TIFF .WebP .XBM .CUR .DCX .DDS .FLI .FLC .FPX .FTEX .GBR .GD .ICO .IMT .IPTC .NAA .MCIDAS .MIC .MPO .PCD .PIXAR .PSD .SGI .TGA .WAL .XPM .PALM .PDF .BUFR .FITS .GRIB .HDF5 .MPEG .WMF .bmp .eps .gif .icns .im .jpeg .msp .pcx .png .ppm .spider .tiff .webp .xbm .cur .dcx .dds .fli .flc .fpx .ftex .gbr .gd .ico .imt .iptc .naa .mcidas .mic .mpo .pcd .pixar .psd .sgi .tga .wal .xpm .palm .pdf .bufr .fits .grib .hdf5 .mpeg .wmf" for word in link):
        
            id = ctx.message.author.id
            channel = ctx.message.channel
            response = requests.get(link)
            image = Image.open (BytesIO(response.content))
        
            image = image.convert("RGB")
       	    image = ImageOps.expand(image, border=int(pixels), fill=int(color))
            image.save(self.path + "/" + id + ".jpg", quality=100)
       	    await self.bot.send_file(channel, self.path + "/" + id + ".jpg")
            os.remove(self.path + "/" + id + ".jpg")
            
    @commands.command(pass_context=True)
    @commands.cooldown(1, 5)
    async def ascii(self, ctx, *, text:str):
        """Convert text into ASCII"""
        asciitext = figlet_format(text, font='starwars')
        await self.bot.say("```" + asciitext + "```")
        
     
    @commands.command(pass_context=True)
    @commands.cooldown(1, 5)
    async def makememe(self, ctx, link, TopText, BottomText):
        """Makes memes from the image and text you specify. Make sure to surround the two text areas with quotes for it to work."""
        response = requests.get(link)
        img = Image.open (BytesIO(response.content))
        imageSize = img.size

	# find biggest font size that works
        fontSize = int(imageSize[1]/5)
        font = ImageFont.truetype("Impact.ttf", fontSize)
        topTextSize = font.getsize(TopText)
        bottomTextSize = font.getsize(BottomText)
        while topTextSize[0] > imageSize[0]-20 or bottomTextSize[0] > imageSize[0]-20:
            fontSize = fontSize - 1
            font = ImageFont.truetype("Impact.ttf", fontSize)
            topTextSize = font.getsize(TopText)
            bottomTextSize = font.getsize(BottomText)

        # find top centered position for top text
        topTextPositionX = (imageSize[0]/2) - (topTextSize[0]/2)
        topTextPositionY = 0
        topTextPosition = (topTextPositionX, topTextPositionY)

        # find bottom centered position for bottom text
        bottomTextPositionX = (imageSize[0]/2) - (bottomTextSize[0]/2)
        bottomTextPositionY = imageSize[1] - bottomTextSize[1] - 8
        bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)

        draw = ImageDraw.Draw(img)

	# draw outlines
	# there may be a better way
        outlineRange = int(fontSize/15)
        for x in range(-outlineRange, outlineRange+1):
            for y in range(-outlineRange, outlineRange+1):
                draw.text((topTextPosition[0]+x, topTextPosition[1]+y), TopText, (0,0,0), font=font)
                draw.text((bottomTextPosition[0]+x, bottomTextPosition[1]+y), BottomText, (0,0,0), font=font)

        draw.text(topTextPosition, TopText, (255,255,255), font=font)
        draw.text(bottomTextPosition, BottomText, (255,255,255), font=font)
        id = ctx.message.author.id

        img.save(self.path + "/" + id + "meme" + ".png")
        await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "meme" + ".png")
        os.remove(self.path + "/" + id + "meme" + ".png")
	
    @commands.command(pass_context=True)
    async def bean(self,ctx, user=None):
        """You just got BEANED"""
	
        url = None
        if user is None:
            user = ctx.message.author
        elif len(ctx.message.mentions):
            user = ctx.message.mentions[0]
        else:
            url = user
        if type(user) == discord.User or type(user) == discord.Member:
            if user.avatar:
                avatar = 'https://discordapp.com/api/users/' + user.id + '/avatars/' + user.avatar + '.jpg'
                response = requests.get(avatar)
                img = Image.open (BytesIO(response.content))
            else:
                avatar = user.default_avatar_url
                response = requests.get(avatar)
                img = Image.open (BytesIO(response.content))
        else:
            response = requests.get(url)
            img = Image.open (BytesIO(response.content))
	
        id = ctx.message.author.id
        channel = ctx.message.channel
	
        try:
            id = ctx.message.author.id
            W, H = (600,840)
            msg = "Uh oh! You friccin \nmoron. You just got"

            im = Image.new("RGBA",(W,H),"white")
            draw = ImageDraw.Draw(im)
            fnt = ImageFont.load('Verdana.ttf', 120)
            w, h = draw.textsize(msg, font=fnt)
            draw.text(((W-w)/2,(H-h)), msg, fill="black")

            im.save("hello.png", "PNG")
            bean_path = 'bean.png'
            bean = PIL.Image.open(bean_path)
            width, height = bean.size
            width2, height2 = img.size
            img = img.resize((334, 395))
            bean.paste(img, (math.floor(width/5), math.floor(height/3)))
            bean.save(self.path + "/" + id + "beaned" + ".png")
            await self.bot.send_file(ctx.message.channel, self.path + "/" + id + "beaned" + ".png")
            os.remove(self.path + "/" + id + "beaned" + ".png")
        except Exception as e:
            await self.bot.say(e)

def setup(bot):
    bot.add_cog(imagefilter(bot))
