# Ascii art

Simple, but amazing to play with.

Sample WebCam feed as seen by ascii-art lens

![Input Image](ascii-art.gif)


### Input image
![Input Image](input.jpg)

### Output image
##### Algorithm used for brightness - Average
brightness = (R + G + B) / 3

![Avg output](output_avg.jpg)

##### Algorithm used for brightness - Min Max
brightness = (Max(R, G, B) + Min(R, G, B)) / 2
![Avg output](output_min_max.jpg)


##### Algorithm used for brightness - Luminosity
brightness = 0.21 * R + 0.72 * G + 0.07 * B
![Avg output](output_luminosity.jpg)
