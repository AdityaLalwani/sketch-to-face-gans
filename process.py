import os
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from numpy import vstack
from matplotlib import pyplot


def predict_img(filename):
    target=os.path.join('./temp/'+filename) #location of image present in temp directory
    img_array = []
    image = cv2.imread(target)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (256, 256))
    image = image.astype('float32') / 255.0
    img_array.append(img_to_array(image))
    test_image = np.reshape(img_array,(len(img_array),256,256,3))
    model=load_model("./stf_model.h5")
    gen_image = model.predict(test_image)
    def plot_images(src_img, gen_img):
	    images = vstack((src_img, gen_img))
	    pyplot.figure(figsize=(10,10))
	    titles = ['Source', 'Generated']
	# plot images row by row
	    for i in range(len(images)):
		# define subplot
		    pyplot.subplot(1, 2, 1 + i)
		# turn off axis
		    pyplot.axis('off')
		# plot raw pixel data
		    pyplot.imshow(images[i])
		# show title
		    pyplot.title(titles[i])
	    pyplot.savefig('./static/'+filename)
    plot_images(test_image, gen_image)
    # random_array = np.random.random_sample(gen_image.shape) * 255
    # random_array = random_array.astype(np.uint8)
    # img = np.reshape(random_array,(len(random_array),256,256,3))
    # random_image = im.fromarray(img)    
    # random_image.save('./temp/'+'gfg_dummy_pic.png') 
    # d={} #dictionary that will save results
    # for eachPrediction, eachProbability in zip(predictions, probabilities):
    #     d[eachPrediction]=eachProbability #prediction output
        #print(eachPrediction , " : " , eachProbability)
    tar = os.path.join('./static/'+filename)

    os.remove(target) #delete temporary file

    return tar