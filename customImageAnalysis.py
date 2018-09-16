#!/usr/bin/env python
# coding: utf-8

# # Image Analysis Using Azure

# imports and Azure URL and subscription

# In[1]:


import requests

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "<subscription_key>"
assert subscription_key

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"


# Read local image

# In[5]:


def readImage(image_source, scope):
    if(scope == 'local'):
        data = open(image_source, "rb").read()
        return data
    elif(scope == 'remote'):
        image_url = image_source
        data    = {'url': image_url}
        return data
    else:
        print('kindly pass the scope parameter local or remote')
        return null


# Calling Azure Computer vision APIs

# In[6]:


def apiCall(serviceURL, params, data, scope):
    if(scope == 'local'):
        headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
                      'Content-Type': 'application/octet-stream'}
        response = requests.post(serviceURL, headers=headers, params=params, data=data)
    
    elif(scope == 'remote'):        
        headers = {'Ocp-Apim-Subscription-Key': subscription_key}
        response = requests.post(serviceURL, headers=headers, params=params, json=data)
    else:
        print('kindly pass the scope paramtere local or remote')
        return null
    
    response.raise_for_status()

    analysis = response.json()
    return analysis


# Main

# In[7]:


if __name__ == "__main__":
    ## set scope to 'local' or 'remote'
    scope = "local"
#     scope = "remote"
        
    ## set image source
    ## local source image sample
#     image_source = "a.jpeg" # red apple for object detection
    image_source = "theGreatPyramids.jpg" # the great pyramids for land mark

    ## remote source image sample
#     image_source = "https://images.all-free-download.com/images/graphicthumb/green_apple_03_hd_picture_167362.jpg" # green apple for object detection
#     image_source = "https://i.ytimg.com/vi/DCExvb-BJPw/hqdefault.jpg" # George Bernard Shaw for Celebrities Recognision
    
    ## Read image
    data = readImage(image_source, scope)
    
    ## General Object Detection
#     serviceURL = vision_base_url + "analyze"
#     params     = {'visualFeatures': 'Categories,Description,Color'}
    ## Landmark
    serviceURL = vision_base_url + "models/landmarks/analyze"
    params  = {'model': 'landmarks'}
    ## Celebrities Recognision
#     serviceURL = vision_base_url + "models/celebrities/analyze"
#     params     = {'model': 'celebrities'}
    analysis = apiCall(serviceURL, params, data, scope)    

    print(analysis)

