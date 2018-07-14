# Parallelizing-Image-Processing-Tasks

## Intro

Pre-processing images is a neccesary task for almost any deep learning task. It helps highlight certain areas and also normalizes the image making it easier for the training model to look at the important regions. This is a time consuming task especially when you have a large dataset set in hand. It becomes exponentially harder when incorporating various augmentations as well.

Parallelizing this task saves a lot of time in this aspect. Here I have used the joblib library which I came across after reading a page from their documentation titled [Embarrassingly parallel for loops](https://pythonhosted.org/joblib/parallel.html). The page demonstrates examples of mathematical tasks being executed in parallel for elements in an array or a list. According to what they have mentioned, *"the core idea is to write the code to be executed as a generator expression and convert it to parallel computing"*.

## My Contribution

I extended this idea to perform image processing tasks on a collection of images on my desktop. The pre-processing task I decided to use was [addWeighted from OpenCV](https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html#addweighted). Technically speaking, it finds a weighted sum of two image arrays. In layman terms, it simply adds two images together assigning a different weight to each one, offering a blending or transpareny effect. See how it is used [here](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html#image-blending).

I performed this function with and without joblib for a bunch of images on my desktop and compared their performances. I have also mentioned the number of images and the collective size of those images used.

**Getting your image statistics**

Using `image_statistics.py` I passed in the path pointing to my desktop and calculated the number of images present along with the toal size. I had 14 images of all formats with a size of 58Mb:

`Collective size of all 14 images in the predefined path is 58 MB`

**Performance Comparison**

Using the file `parallelizing_loops.py` you can compare how using `joblib` makes a difference. I have shown my results below. It has made a big impact. I am sure its use will be felt tremendously when used with large datasets.

The result of this script on my console:

    Using Joblib : 0.0940001011 seconds
    Without Joblib : 15.3860001564 seconds
