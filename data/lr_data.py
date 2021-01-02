import cv2 
import os

hr_dir = 'training_hr_images'
lr_dir = 'training_lr_images'
if not os.path.isdir(lr_dir):
	os.makedirs(lr_dir)
hr_imgs = os.listdir(hr_dir)
for imgname in hr_imgs:
	img = cv2.imread(os.path.join(hr_dir, imgname))
	h, w, c = img.shape
	resimg = cv2.resize(img, (w//3, h//3), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(os.path.join(lr_dir, imgname), resimg)
