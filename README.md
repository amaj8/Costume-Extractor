# Costume-Extractor
Extracts the dresses and hats worn by Miss Lemon in the series Agatha Christie's Poirot

# How I approached this? 
* *Get the images*: First I needed the images of the character. I scraped Google Images using Selenium to get 42 images with Miss Lemon in it. 
* *Annotation*: Manually annotated the images (made 2 classes: dress and hat) using Roboflow Annotate. Made bounding boxes around the dresses and hats worn.

![Images after annotation - tagged dresses and hats](https://github.com/amaj8/Costume-Extractor/blob/main/miss_lemon_costumes_annotated.jpeg)

* *Data Augmentation*: Applied data augmentation such as flip, shear and blur to make the model more robust

* *Train the model*: Trained YOLOv5 on these annotations.
* *Results after 1000 epochs*
<br/> Results on test images
![Results on test images](https://github.com/amaj8/Costume-Extractor/blob/main/results_1000_epochs.jpeg)
<br/> Training plots after 1000 epochs
![Training plots after 1000 epochs](https://github.com/amaj8/Costume-Extractor/blob/main/plots_1000_epochs.png)


# Problems faced 
* Very small dataset - this could increase overfitting 
