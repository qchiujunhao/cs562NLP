#Part 1

1. Program
   deserialize.py
   run "python deserialize.py data/*.xml.gz > deserialized.txt"

2. Sample terminal output
   deserialized_100.txt
   from "head -n 100 derserialized.txt > deserialized_100.txt" on linux

3. I used "wget -c -r -nd -k -L -p https://cslu.ohsu.edu/~bedricks/courses/cs662/resources/GW-cna_eng/" to download the data. And then I wrote the program to read the data. As your tips, in the script, I used gzip and lxml.tree, and I dealt with the blank paragraphs using "etree.XMLParser(remove_blank_text=True)".

Fortunately, I did not meet trouble.

#Part 2