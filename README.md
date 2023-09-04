# Panoramic Image Stitching
Introduction - The input to the algorithm are pairs of images that are related by a unknown translation and scale(tx, ty, s).Your goal is to estimate this transformation using local feature matching and RANSAC to produce a combined image.

1. detectCorners.py - includes implementations of 2 types of corner detection algorithms.

2. extractFeatures.py -  extracts a vector of raw-pixel values from image centered at each corner in c. 

3. computeMatches.py - compute matches between the two sets of features. Implement thefunction computeMatches(f1,f2) that returns the best match of each feature f1 to f2 using the smallest sum-of-squared-differences as the distance measure.

4. ransac.py - RANSAC algorithm implementation returning a transformation that has the highest number of inliers.

5. stitchImages.py - Used to merge images

Example Output - 

<img width="468" alt="image" src="https://github.com/rohanraghuram/panoramic_image_stitching/assets/67184059/64f31010-48f4-4595-a7f9-ef48ee9506a7">

<img width="468" alt="image" src="https://github.com/rohanraghuram/panoramic_image_stitching/assets/67184059/963276c1-5224-44a6-a2c5-4fcffc7c6573">

