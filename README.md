# mandelbrot

## Introduction

This is a tool dedicated to generating pictures of the [Mandelbrot Set](http://en.wikipedia.org/wiki/Mandelbrot_set), a set of complex numbers found by mathematian Benoit Mandelbrot.

The Mandelbrot Set is entirely [self-similar](http://en.wikipedia.org/wiki/Self-similarity), and shows some amazing features at differnt levels of zoom.

## Usage

This repository contains a the Alpha version of a command line tool for generating grayscale pictures of the Mandelbrot set. The user can set options like the number of iterations the program processes, and number of pixels of the height of the image. So far the program only accepts a single form of coordinates, (x,y,r) where x,y represent the centre of the rectangle and r represents the rectangle's vertical "radius" (and half the horizontal radius). 

The user should remember to add "--" before specifying the coordinates when including negative numbers.

You'll need to follow the link in dependencies in order to download the packages required for image handling.

### Examples

```
./generate -i 500 -d 4000 -c -- -0.235125 0.827215 0.00004
```

```
Usage with centered coordinates: ./generate -i 128 -d 5000 -c -- x y r
Options
   -i Set number of iterations [default -i 128]
   -d Set number of y pixels [default -d 5000]
   -c Use centered coordinates x y r
```

## Comments

* The program logs each command and saves the calculated array to disk, to save you from repeatedly generating the same image
* The program currently only accepts centered coordinates and generates landscape images at a ratio of 2:1
* The program currently gives the images timestamped names. Custom names will be available soon.

Interesting coordinates can be found at http://www.cuug.ab.ca/dewara/mandelbrot/images.html
