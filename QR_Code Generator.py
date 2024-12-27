'''
    basic script for generating a QR Code that will direct you to a website
                                                                            '''

import qrcode # import the library

website = "https://www.google.com" # assign a URL to the website variable
image = qrcode.make(website) # declare a variable for the QR Code, then call the make method, pass your website variable in
image.save("my_qrcode.png") # call the save method, this allows the generated QR Code to be saved as your preferred file name
