# Topic 1: Icy for Bioimage Analysis

We will be using the alpha of the new version of Icy 3, that we have been brewing in the past 2 years. 
This new version will be release after the course and will ship new means to interact with the Python scientific ecosystem. 
In this tutorial we will learn and discover how to use Icy for Bioimage Analysis, using the alpha version.

## Preparing for the tutorial

### Java

Like Fiji and QuPath, Icy is a Java software, so we need to dowload Java. 
And for the new and future version of these software, we will be using Java version 21.
If you want to know what version of Java you have, open a terminal (or CMD, Powershell on Windows) and type

```sh
java -version
```

If you see something like
```
java version "21.x.y" 2025-04-15 LTS
Java(TM) SE Runtime Environment (build 21.0.7+8-LTS-245)
Java HotSpot(TM) 64-Bit Server VM (build 21.0.7+8-LTS-245, mixed mode, sharing)
```
you are good.

Otherwise, download and install Java 21 from there:

Download and install Java 21 : [Oracle JDK 21](https://www.oracle.com/java/technologies/downloads/#java21)

Ask the helpers if you have doubt about what version to install.

### VTK

VTK (Vizualization ToolKit) is the 3D framework for Icy.

If you are using a Mac (Intel or Apple Silicon) you should be able to run it without issue if you are minimum on MacOS 13 Ventura.

If you are using a Windows 11, you should be able to run it without issue if your graphics driver is up-to-date.

If you are using a Linux Ubuntu 24, you may need to download and install two packages with ```sudo apt install``` :
- libopengl-dev
- libvtk9-dev

If you are using a Windows 10, a Linux Ubuntu 22, or an older version of MacOS 13 Ventura, you may not able to run VTK properly.


### Installing Icy

You can dowload the alpha of Icy from here:

[https://mega.nz/folder/O8tTmZCC#d4Q8IGyDT38g-owsldJxMw](https://mega.nz/folder/O8tTmZCC#d4Q8IGyDT38g-owsldJxMw)

Download and unzip icy_v3.0.0-a.4.tar.gz
- If you are on a Mac :
  - Rename the folder then add .app at the end of icy-app-v3 folder name
  - Double click on the newly created icy-app-v3.app
  - If your not able to launch it because of Apple security, go to : System Settings > Privacy and Security > click on Open Anyway
- If you are on a Windows :
  - Double click on Icy.exe
- If you are on Linux :
  - Execute ‘icy’ file with sh in your terminal with : ./icy
 
If Java was properly installed, you should see a window like this one:
<img width="1452" alt="Screenshot 2025-05-06 at 10 01 58" src="https://github.com/user-attachments/assets/dac20284-1028-4851-a441-b5b7523da2fa" />

In the first run, Icy will copy libraries to an adequate (.icy/) folder in your home directory.

### Downloading the training materials

You can find the training materials inside the "documents" and "images" folders in the link above.






