# Notes
* ORB-SLAM requires an initial location where it can easily pick up details in order to initialize
* A good initial location should have a lot of detail
  * Complex Structure
  * Complex Texture
  * Variety of Color
* Faster motion could be detected although a slower pace usually yielded better results
* ORB-SLAM had a large amount of difficulty with extremely dark or extremely bright settings although it was able to still function about 40 to 50 percent of hte time in these conditions.
* There was also a large amount of difficulty with mono-colored, flat surfaces such as boxes, walls, etc, since these objects had little detail
  * Moving around such objects or zooming out often allowd these objects to be picked up as it often allowed ORB-SLAM to detect the structure
* Any motion of objects or people would cause ORB-SLAM to think that it was moving which made it more difficult to localize its postition
* With videos, if ORB-SLAM suddenly was unable to localize, a fairly detailed and recognizeable location was required to reinitialize and even then, this only happened about 25-50 percent of time with most videos and some videos did not allow it to reinitialize at all. 
* With the webcam, if ORB-SLAM was unable to relocalize suddenly, simly back up to a previous location it just saw that had a fair amount of detail
* On the webcam, ORB-SLAM tended to favor remaining stationary and rotating despite the camera moving if it wasn't sure if two objects were different
* On the webcam, ORB-SLAM also tended to favor the idea that it was making a circle even if the camera was moving in a straightline when brought really close to objects or a surface
