# EXA-JS-Fragmentation
(EXA, Example)

Contains a working example of the JS fragmentation method

![](https://github.com/creativecommons/cc-assets/blob/main/license_badges/small/by.svg)

---
**WARNING**

The code in this example uses the `.innerHTML` property of the DOM to set the HTML of the page. 
This is a potential security risk if you do not use the correct sanitization methods.

Any input data that the user submits that will then be used to generate a fragmented template
should be sanitized server side.

If you do not sanitize the input data, you are opening yourself up to XSS attacks!

---


### Attribution

[CheeseCake87 (David Carmichael)](https://github.com/CheeseCake87)

### Setup

(This assumes you have Python installed)

1. Download or Clone this repository.
2. Open terminal (Linux) / powershell (Windows) and cd to the directory of the project.

```text
# Linux
cd /path/to/EXA-JS-Fragmentation

# Windows
cd C:\path\to\EXA-JS-Fragmentation
```

---

### Linux

**Create a virtual environment and activate it.**

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

**Install the requirements.**

```bash
pip install -r requirements.txt
```

**run**

```bash
flask run
```
or
```bash
python3 run.py
```

---

### Windows


**Create a virtual environment and activate it.**

```bash
python -m venv venv
```

```bash
.\venv\Scripts\activate
```

**Install the requirements.**

```bash
pip install -r requirements.txt
```

**run**

```bash
flask run
```
or
```bash
python run.py
```
