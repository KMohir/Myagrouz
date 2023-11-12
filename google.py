import sys
import os
import webbrowser
import pyimgur



GOOGLE_SEARCH_URL = "https://images.google.com/searchbyimage?image_url="

for p in sys.argv[1:]:
    absolute_image_path = os.path.join(os.getcwd(), p)

    uploaded_image = with open('111.jpg','r')
    webbrowser.open_new_tab(GOOGLE_SEARCH_URL + uploaded_image.link)