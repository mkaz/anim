import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("Anim")

framenum = 0
print("Press <Space> to take Frame")
print("Press <Esc> to when done")
while True:

    ret, frame = cam.read()
    cv2.imshow("Anim", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

    elif k % 256 == 32:
        # SPACE pressed
        img_name = "anim_frame_{:0>4d}.png".format(framenum)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        framenum += 1

cam.release()
cv2.destroyAllWindows()

