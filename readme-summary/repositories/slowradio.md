# slowradio

Summary:

Slow Radio is a software implementation of the Paul Stretch algorithm, designed to create a constant stream of stretched audio. It operates as a slow radio station, accepting Ogg Vorbis input and broadcasting via Icecast. The project is written in C and utilizes several third-party libraries (libshout, libconfig, libvorbis, libvorbisfile, libvorbisenc, libogg) along with two of the author's own libraries (bclib, libpstretch). A configuration file (radio.cfg) is required to set up the audio reader, stretcher, encoder, and broadcaster. Docker images are available for easy deployment, though they are currently large due to limited optimization efforts. The software is licensed under the BSD License.

KEYWORDS:
Slow Radio, Paul Stretch algorithm, stretched audio, Creative Commons Attribution License, Ogg Vorbis, Icecast, C programming language, CMake, libshout, libconfig, libvorbis, libvorbisfile, libvorbisenc, libogg, bclib, libpstretch, BSD License
