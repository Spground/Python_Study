#...the FIle I/O ....
import os

#read the user input
stdIn = input("Please input the content you want to be wrote into file:");
fd = open("foo.txt", "w+");
fd.write(stdIn);
fd.close();

#write something into a file
fd = open("foo.txt", "r");
content = fd.read();
print("The content of the file is :", content);
print("The current file pointer is :", fd.tell());
fd.seek(3, 0);
print("The third char is :", fd.read(1));
fd.close();

#rename a file
os.rename("foo.txt", "fool_.txt");

#delete a existed file
os.remove("fool_.txt");

#show current work dir
print("The currrent work dir is :", os.getcwd());

#make a new dir "Tom"
os.mkdir("Tom");

#change current work dir to Tom
os.chdir("Tom")
print("The current new work dir is :", os.getcwd());

#remove the Tome dir
os.chdir("../");
os.rmdir("Tom");

