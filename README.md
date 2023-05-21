# pyqt-dreamstudio
Using DreamStudio API in Python desktop application

You can make a bunch of image without installing heavy resources like CUDA, torch, etc. But it's not free.

This is separated from <a href="https://github.com/yjg30737/pyqt-openai">pyqt-openai</a> package to people who only wants to use stable diffusion api

and who wants to fork this only.

## Prerequisite 
You have to get the DreamStudio api key from <a href="https://platform.stability.ai/docs/getting-started/authentication">here</a>.

Using DreamStudio or the API requires credits. Take a look at <a href="https://platform.stability.ai/docs/getting-started/credits-and-billing#sdxl-pricing-table">pricing</a> about this.

Make your image in <a href="https://beta.dreamstudio.ai/generate">here</a> before doing with this app.

## How to Install
1. pip clone
2. cd pyqt_dreamstudio
3. pip install -r requirements.txt
4. python main.py

## Result
![image](https://github.com/yjg30737/pyqt-dreamstudio/assets/55078043/80101faf-fb0e-43e2-acb9-2cf51a9ff3b1)

## Note
As far as i know, Using Stable Diffusion with API doesn't support disable safety filter. Shame!!

So if you type any words which is considered as NSFW, toast containing error message will show up
