# highlight
Colorize text in your terminal :rainbow:

---

### Install via [pipx](https://pypa.github.io/pipx/):
```console
  $ pipx install git+https://github.com/tspotts/highlight
```

### Usage:
```console
  $ cat /tmp/rgb.log | highlight --red='foo' --green='bar' --blue='baz' 
```

### Help:
```console
  $ highlight --help
```

---

### Dev Guide (using [pyenv](https://github.com/pyenv/pyenv)):
```console
$ cd ~/development
$ git clone git@github.com:tspotts/highlight.git
$ cd ~/development/highlight

$ pyenv virtualenv 3.10.12 highlight
$ pyenv local highlight

$ pip3 install --editable .
  
```
