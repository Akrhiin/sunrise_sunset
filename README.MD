## Sunrise & Sunset Image Recognition

### Project Goals
My goal with this project was to get a better grasp of machine learning principles and implementation.  I have little experience with the topic, so I'd like to improve while also working toward a finished project.  

### Status
I currently have a pair of files 'read_sunrise_pictures.py' and 'read_sunset_pictures.py' that convert all images in the 'sunrise' and 'sunset' directories, respectively, into a 2d array to be stored in '.txt' files in the 'sunrises_data' and 'sunsets_data' directories.  These files act as a way to store data for later, and as the main way of formatting data for the 'the_machine.py' script.

The machine learning components will be implemented in the 'the_machine.py' file; I've written code to pull data from all files in the 'sunrises_data' and 'sunsets_data' directories and store them in 2d arrays 'sunrise_colors' and 'sunset_colors', and intend to feed said \[float32\] data to an undecided algorithm.  I'd like to get it accurate enough to differentiate sunrises and sunsets with at least 50% accuracy, with a long term goal of 70-80%.
