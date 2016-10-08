import camera
import sys
import image

if __name__ == "__main__":
    print(sys.argv)
    camera.take_picture("foo.jpg")
    camera.take_picture("bar.jpg")
    print(image.similarity_f("pictures/foo.jpg", "pictures/bar.jpg"))
