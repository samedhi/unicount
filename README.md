# Distinct Elements in Streams

I was intrigued by how simple the Quanta article [Computer Scientists Invent an Efficient New Way to Count](https://www.quantamagazine.org/computer-scientists-invent-an-efficient-new-way-to-count-20240516/) seemed so I tried to implement it myself. Turns out the article had a few errors within the description (check the comments), but I was eventually able to get something working.

I made it into a simple script so that you can pass it a file and it will provide an estimate of the number of distinct elements within that file. 

## Usage

```
$ wget something
$ python uniqcount.py hamlet.txt
```

