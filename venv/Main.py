import cv2
im=cv2.imread('circuit.tif');
s=strel('disk',1);
out=imerode(im,s);
imshow(out);