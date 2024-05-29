# Distinct Elements in Streams

I was intrigued by how simple the Quanta article [Computer Scientists Invent an Efficient New Way to Count](https://www.quantamagazine.org/computer-scientists-invent-an-efficient-new-way-to-count-20240516/) seemed so I tried to implement it myself. Turns out the article had a few errors within the description (check the comments), but I was eventually able to get something working.

I made it into a simple script so that you can pass it a file and it will provide an estimate of the number of distinct elements within that file. 

## Usage

```
$ wget https://raw.githubusercontent.com/samedhi/unicount/main/unicount.py
$ wget https://raw.githubusercontent.com/samedhi/unicount/main/hamlet.txt
$ python uniqcount.py hamlet.txt
```

## Reference

* [Computer Scientists Invent an Efficient New Way to Count](https://www.quantamagazine.org/computer-scientists-invent-an-efficient-new-way-to-count-20240516/)
* [Notes by Knuth](https://cs.stanford.edu/~knuth/papers/cvm-note.pdf)
* [Presentation Slides](https://www.cs.toronto.edu/~meel/Slides/meel-distinct.pdf)
* [arxis Paper](https://arxiv.org/pdf/2301.10191)
