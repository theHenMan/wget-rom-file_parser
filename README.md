# wget Filename parser
### Clean ROM names generated from wget

#### Should work on most file types; but it doesn't dive into directories

##### This works:
![Correct:](/images/Sample_Type.PNG)

##### This doesn't:
![Incorrect:](/images/Incorrect_Format.PNG)

----------

I used **wget** to get information from a site.
The file generated contained a bunch of extra data.  I only want the file name and file size.

Example files attached to try out that was generated by **wget**.

I created a python script to prettify the names/output and show total files and size

----------

#### USAGE:
Run the file, either double click or from command line, select file to parse and then where to save
