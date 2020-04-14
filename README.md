# Responsive-img-gen

This is a simple python script that creates 5 different images of different sizes for responsive web development.

Usage "web-img-gen -R &lt;Recursive mode, this enables the -i flag to use a directory&gt; -i &lt;File / Directory to be converted&gt; -o &lt;Directory to output the images to&gt;"

The -o uses the folder structure of the -i flag, so:

    Let's say we have a input directory of a structure of:
    InputFolder/ -
                 |
                 V
                 img.jpg
                 another_folder/ -
                                 |
                                 V
                                 img2.png
    
    Then the output folder looks like this:

    OutputFolder/ -
                  |
                  V
                  img_xxs.jpg
                  img_xs.jpg
                  img_s.jpg
                  img_m.jpg
                  another_folder/ -
                                  |
                                  V
                                  img2_xxs.png
                                  img2_xs.png
                                  img2_s.png
                                  img2_m.png