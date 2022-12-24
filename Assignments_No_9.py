#!/usr/bin/env python
# coding: utf-8

# 1. To what does a relative path refer?

# In[ ]:


Ans: A relative path points to a location relative to a current directory. 
Relative paths use two special symbols, a dot (.) and a double-dot (..), which translate into the current and parent directories.


# 2. What does an absolute path start with your operating system?

# In[ ]:


Ans: An absolute path is a path that contains the entire path to the file or directory that you need to access.
This path will begin at the home directory of your computer and will end with the file or directory that you wish to access.
Absolute paths ensure that Python can find the exact file on your computer.


# 3. What do the functions os.getcwd() and os.chdir() do?

# In[ ]:


Ans: os.chdir() method in Python used to change the current working directory to specified path.
It takes only a single argument as new directory path.

To know the current working directory of the file, getcwd() method can be used.
After changing the path, one can verify the path of current working directory using this method.


# 4. What are the . and .. folders?

# In[ ]:


Ans:The . folder is the current folder, and .. is the parent folder.


# 6. What are the three “mode” arguments that can be passed to the open() function?

# In[ ]:


Ans:The string 'r' for read mode, 'w' for write mode, and 'a' for append mode


# 7. What happens if an existing file is opened in write mode?

# In[ ]:


Ans: An existing file opened in write mode is erased and completely overwritten.


# 8. How do you tell the difference between read() and readlines()?

# In[ ]:


Ans:The read() method returns the file's entire contents as a single string value.
The readlines() method returns a list of strings, where each string is a line from the file's contents.


# 9. What data structure does a shelf value resemble?

# In[ ]:


A shelf value resembles a dictionary value;
it has keys and values, along with keys() and values() methods that work similarly to the dictionary methods of the same names.

