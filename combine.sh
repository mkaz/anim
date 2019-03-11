#!/bin/bash

ffmpeg -framerate 6 -i anim_frame_%04d.png anim.mp4
