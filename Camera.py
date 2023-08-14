import cv2

vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, img = vid.read()

    cv2.imshow('frame', img)
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()


