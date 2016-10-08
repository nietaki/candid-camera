def take_picture(filename, delay=1, resolution="1280x720")
    command_string = "fswebcam -r {0} --jpeg 95 -D {1} {2}".format(resolution, delay, filename)
    os.system(command_string)
