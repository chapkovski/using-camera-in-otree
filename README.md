# Photo camera in otree
Based on [WebcamJS 1.0](https://github.com/jhuckaby/webcamjs) by [Joseph Huckaby](https://github.com/jhuckaby).

Docs for camera [are available here](https://github.com/jhuckaby/webcamjs/blob/master/DOCS.md).


An alternative concise and even nicer solution in jQuery  can [be found here](https://jsfiddle.net/dannymarkov/cuumwch5/). See more in Danny Markov's [tutorial](http://tutorialzine.com/2016/07/take-a-selfie-with-js/).


On oTree side, the solution is a bit primitive: we put the camera data into a TextField, and then process it decoding from Base64 back to image, and save it in a static folder with the name [photo]+[participant's code].

At the next page the player can delete or keep the photo on server.
