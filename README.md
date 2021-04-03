# BytesToNES

BytesToNES is a little python script that converts bytes from the standard input to NES controller input string. It supports [NES native coding](https://wiki.nesdev.com/w/index.php/Controller_reading_code) format and the input movie format for [BizHawk](https://github.com/TASVideos/BizHawk) and [FCEUX](http://fceux.com/).

## Installation

Just clone the github repository and have a working python 3 installation
```bash
git clone https://github.com/mtardy/bytesToNES
```

## Usage

For usage information, please see `./bytesToNES.py -h`
```
usage: bytesToNES.py [-h] [-d] [-f {bk2,fm2}] [-v] [-b BYTE]

Converts bytes to NES controller strings, see '-d' for information on the format.

optional arguments:
  -h, --help            show this help message and exit
  -d, --doc             display documentation on the NES controller string format and exit
  -f {bk2,fm2}, --format {bk2,fm2}
                        change the format of output
  -v, --verbose         verbose human readable output, line is red if the controller combinaison is impossible a priori
  -b BYTE, --byte BYTE  input one byte to convert
```

## About

We worked on arbitrary code injection in video games based on [Lord Tom's NES Super Mario Bros. 3 "Total Control" in 08:16.23](http://tasvideos.org/4961S.html) exploit.
We injected bytes in the game using the controller input so we needed a tool to convert our assembled binary code from regular bytes to controller input strings.

In our project, we injected stuff in Super Mario Bros 3 and we noticed that the controller driver filters "illegal" inputs such as pressing up and down or left and right simultaneously.
Using the `--verbose` (or just `-v`) option, you can spot "illegal" inputs displayed in red.
Typically, you can write your assembly and pipe the output of the assembler to the converter then by trial and error, fix the illegal entries.
A good idea, in that specific situation, is to begin by writing a new driver that accept any input to be more relaxed!

## Contributing

You can extend the supported format by modifying the `formatter` function, you just have to provide a template, the buttons order to respect and the separator character.

## License

[MIT](https://choosealicense.com/licenses/mit/)
