import cv2
from skimage.metrics import structural_similarity as ssim


def match(path1, path2):
#Normalisation des images pour comparaison    
    # Lecture des images
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    # transformer images en grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # redimensionner images pour comparison
    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))
    # afficher les deux images
    cv2.imshow("One", img1)
    cv2.imshow("Two", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    similarity_value = "{:.2f}".format(ssim(img1, img2)*100)

    return float(similarity_value)

