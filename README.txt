# To run python3:
source av1_python_env/bin/activate

# To support arithmetic coding:
I did this in my av1_python_env/lib/python3.11/site-packages/:
git clone https://github.com/nayuki/Reference-arithmetic-coding.git

And then copied *.py directly into av1_python_env/lib/python3.11/site-packages/:
adaptive-arithmetic-compress.py
adaptive-arithmetic-decompress.py
arithmetic-compress.py
arithmetic-decompress.py
arithmeticcoding.py
ppm-compress.py
ppm-decompress.py
ppmmodel.py
