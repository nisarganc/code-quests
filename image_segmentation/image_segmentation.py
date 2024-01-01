"""
This program segments an areal image into two clusters (cloud and others) using KMeans clustering.
"""

from matplotlib.image import imread
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def segment_image():
    image = imread("ireland.png")
    height, width, channels = image.shape

    # Reshape image to be a list of pixels
    reshaped_image = image.reshape((height * width, channels))

    # Specify the number of clusters (2 for clouds and non-clouds)
    num_clusters = 2

    # Fit KMeans clusterer to the image
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    kmeans.fit(reshaped_image)

    # Get the labels assigned to each pixel
    labels = kmeans.labels_

    # stack cluster_centers_ horizontally according to labels
    segmented_image = kmeans.cluster_centers_[labels]

    # Reshape the segmented image back to the original shape
    segmented_image = segmented_image.reshape((height, width, channels))

    # Create the output dictionary
    out = {'segmented_image': segmented_image, 'clusterer': kmeans}

    return out

# Visualize the original and segmented images
result = segment_image()
segmented_image = result['segmented_image']
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(imread("ireland.png"))
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(segmented_image)
plt.title('Segmented Image')
plt.axis('off')
plt.show()

