# 📊 Data Augmentation Code

This directory contains the data augmentation script used to enhance the original dataset of floor plan images. The goal of this augmentation process is to increase the dataset's size and diversity, thereby improving the performance and robustness of our generative model.

## 📄 Description

The provided script applies 10 different augmentation techniques on each image in the dataset. These include:

1. Horizontal Flip
2. 90° Clockwise Rotation
3. Gaussian Blur
4. Grayscale Conversion
5. HSV Color Space Conversion
6. Brightness Increase
7. Brightness Decrease
8. 90° Counterclockwise Rotation
9. Vertical Flip
10. Random Noise Addition

All augmented images are saved to a designated Google Drive folder, preserving the format and ensuring seamless access for model training.

## 📂 Directory Structure

```
Data Augmentation Code/
├── Image_Augmentation.ipynb
└── README.md
```

## 🚀 Steps to Run on Google Colab

Follow these steps to execute the augmentation code in Google Colab:

**1.** **Upload the original dataset** to your Google Drive.
   Recommended location:
   `/My Drive/Datasets/ROBIN/Dataset_3rooms`

**2.** **Open the notebook** (`image_augmentation.ipynb`) in Google Colab.

**3.** **Mount your Google Drive** using:

   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

**4.** **Set the paths** in the code to point to your dataset and desired output location:

   ```python
   folder_path = "/content/drive/My Drive/Datasets/ROBIN/Dataset_3rooms"
   save_path = "/content/drive/My Drive/Result/ROBIN Augmented/Dataset_3rooms Augmented"
   ```

**5.** **Run the notebook.** The script will augment each image and save the results in the target folder on Drive.

> ⚠️ Make sure your Google Drive has at least **5 GB of free space** before running the notebook.