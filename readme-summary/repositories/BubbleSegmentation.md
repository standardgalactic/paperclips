# BubbleSegmentation

Summary:

BubbleSegmentation is a software tool designed to identify bubbles within image data using a scale-equivariant convolutional kernel. This approach generates a bubble heatmap for various radii, from which a 'constellation' of points representing bubble centers is extracted. The thresholding process varies based on radius and bubble volume fraction, values empirically derived from sample datasets.

Key components include:
- **bubbles.py**: Contains the primary functions.
- **utils_visualisation.py**: Provides utility and visualization tools.
- **bubble_processing.ipynb**: A guided notebook for software usage.
- **bubble_test_notebook.ipynb**: A test notebook demonstrating functionality.
- **bubble_data**: Directory for saving computed bubble data from processing.
- **threshold_testing.py**: Contains empirical measurements used to develop the thresholding model.

Usage instructions:
1. Clone the repository and create a 'data' folder within it, organizing images into subfolders (e.g., 'data/05.17_0.37/230517_AR_1632.jpg').
2. Install OpenCV if not already available; other dependencies are standard.
3. Follow the steps in bubble_processing.ipynb to utilize the software, experimenting with data in separate folders.

KEYWORDS:
BubbleSegmentation, image processing, convolutional kernel, scale-equivariant, bubble heatmap, thresholding model, empirical measurements, openCV, guided notebook, test notebook.
