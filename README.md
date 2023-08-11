# highlight
Colorize text in your terminal :rainbow:

---

### Install via [pipx](https://pypa.github.io/pipx/):
```bash
  pipx install git+https://github.com/tspotts/highlight
```

### Usage:
```bash
  cat /tmp/rgb.log | highlight --red='foo' --green='bar' --blue='baz' 
```

### Help:
```bash
  highlight --help
```

---

### Dev Guide:
```
$ cd ~/development
$ git clone git@github.com:tspotts/highlight.git
$ cd ~/development/highlight

$ pyenv virtualenv 3.10.12 highlight
$ pyenv local highlight

$ pip3 install --editable .
  
```