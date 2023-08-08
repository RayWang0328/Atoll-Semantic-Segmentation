
# 🏝️ Atoll Segmentation Web App Demo ⚙️ 

Climate change poses significanrt threats to the stability and sustainability of atoll ecosystems worldwide. To effectively monitor and quantify the impacts of climate change on atoll morphometrics, this study employs an unique approach using semantic segmentation, a deep learning based image analysis technique. High-resolution satellite imagery is processed and classified into distinct features of reef, island, and ocean components.

This is a web application that allows for easy segmentation of Atoll Morphometrics. The backend supports four models, each of a different image type that was all trained from scratch. The four image types are: RGB, NIR, SpecInd, and SSR.  

## 🌟 Project Overview : 
* Dataset: 288 distnct Atoll Images provided by Dr. Alejandra Geiger-Ortiz
* Model Training: Tensorflow and [Segmentation Gym](https://github.com/Doodleverse/segmentation_gym)
* Web App: HTML/CSS, Javascript, Flask

For more information, refer to this [presentation](https://docs.google.com/presentation/d/1EEPi7M9ejf25oRwZPkbJS6nphWAbFXE6plbLAS6Srk4/edit?usp=sharing). Paper coming soon... 

[Original Project](https://github.com/Tahiya31/colby_atoll)

## 🎬 Web Demo 

https://github.com/RayWang0328/Atoll-Semantic-Segmentation/assets/19866871/10eb4fb0-96d7-429e-b3b5-8b92da9be6dc


## 🛠️ Installation 

For Windows Users: 

Change Directory and activate virtual environment
```
cd myproject
py -3 -m venv .venv
.venv\Scripts\activate
```

Install Required libraries:
```
pip3 install -r requirements.txt
```

Run Application: 
```
python app.py
```


For Mac Users: 

Change Directory and activate virtual environment
```
cd myproject
python3 -m venv .venv
. .venv/bin/activate
```

Install Required Libraries 
```
pip3 install -r requirements.txt
```

Run Application: 
```
python app.py
```
