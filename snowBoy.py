import snowboydecoder


def listen(event):

    detector = snowboydecoder.HotwordDetector('resources/gangdan.pmdl', sensitivity=0.5)
    detector.start(detected_callback=event.set)
