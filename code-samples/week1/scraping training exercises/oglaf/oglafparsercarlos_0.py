'''
Written by Antonio Carlos L. Ortiz 02/25/2015
Input: website - 'http://oglaf.com/archive/'
Output: scraped images of the comics with the title and alt description appendend at the
top of the photo.
'''

import requests
from bs4 import BeautifulSoup
import os
import string #for zfill
from PIL import ImageFont, Image, ImageDraw, ImageOps
import os
import sys
from image_utils import ImageText


def download(src, localname):
    '''
    takes in the image source, and local filename then downloads the image to out/localname.
    '''
    image = get_page(src, 5)
    if not image:
        return False

    f = open('out/' + localname, 'wb')
    f.write(image)
    f.close()

    return True

def make_page(infile, outfile, text = "", text2 = ""):
    '''takes the inputfilename, outputfilename and text to put it in at the bottom'''

    font = 'Aller_Rg.ttf' #some random font, just fine one that is legible enough
    color = (50, 50, 50) # color of the text box
    page = Image.open(infile) # opening original image
    width, original_height = page.size # size of original image

    temp = ImageText((1000, 500), background=(255, 255, 255, 200))
    
    # +20 y offset writer leaves that much space at the top
    height = temp.write_text_box((0, 0), text,
                                 box_width=width, font_filename=font,
                                 font_size=16, color=color)[1] + 20
    
    textbox = temp.image.crop((0, 0, width, height)) #crop text
    #making a large temp Image text object to put  the text in.
    temp = ImageText((1000, 500), background=(255, 255, 255, 200)) 
    
    # +20 y offset writer leaves that much space at the top
    height2 = temp.write_text_box((0, 0), text2,
                                  box_width=width, font_filename=font,
                                  font_size=16, color=color)[1] + 20
    
    textbox2 = temp.image.crop((0, 0, width, height)) #crop textbox
    
    output = Image.new("RGBA", (width, original_height + height + height2),
                      (120, 20, 20)) # make new blank image with computed dimensions
    output.paste(textbox2, (0,0))
    output.paste(page, (0,height2)) # paste original
    output.paste(textbox, (0, original_height + height2)) # paste textbox
    output.save(outfile) # save file

def get_page(url, max_attempts):
    '''
    Function to check if the requested page returns the correct page and did not
    time out.
    '''
    for i in xrange(max_attempts):
        print "attempt no.", i + 1
        r = requests.get(url)
        
        if r.status_code == 200:
            return r.content

    print r.status_code
    return False

def extract_archive(url1, url2):
    '''extract links on the archive page'''
    html = get_page(url1, 5)
 
    if html:
        soup = BeautifulSoup(html)
        comic = soup.findAll('a')   #find all tags <a href= ..
        
        for i in comic:
            #method 'get()'' can obtain data with a var=data format
            address = i.get('href')        
            new_addr = "".join((url2,address[1:]))
            
            html_inner = get_page(new_addr, 5)
            
            extract_comic(html_inner, address, new_addr)

def extract_comic(html_inner,address, new_addr, count=1):
    '''
    find the element with an id of 'strip' as this contains details of the comic in html_inner
    '''
    if html_inner:
        soup_inner = BeautifulSoup(html_inner)
        comic = soup_inner.find(id = 'strip')

        src = comic.get('src')
        alt = comic.get('alt')
        title = comic.get('title')

        #create the filename for the comic
        filename = address[1:][:-1] + '-' + string.zfill(1, 3) + '.' + \ 
            src[-3:].lower()

        # save the picture to local.
        download(src, filename)
        
        try:
            make_page(os.path.join('out', filename), os.path.join(outpath,
                os.path.basename(filename)), title, alt) # process the page
        except Exception, e:
            print e
        
        #printing is buffered by default and this makes the display  as soon as it is encountered
        sys.stdout.flush()

        
        count += 1
        html_inner = soup_inner.find(href = address + str(count) + '/')
        
        #this is for the comic segments with multiple pages.
        extract_comic(html_inner,address,new_addr,count)

if __name__ == "__main__":
    '''create directory if it is not yet existing'''
    for directory in ['out', 'final']:
        if not os.path.exists(directory):
            os.makedirs(directory)

    outpath = os.path.join(os.getcwd(), 'final')

    url1 = 'http://oglaf.com/archive/'
    url2 = 'http://oglaf.com/'
    extract_archive(url1, url2)