This page collects instructions, links and materials for the Day 2

# Topic 1: Ilastik for machine learning in image analysis

[Ilastik](https://www.ilastik.org/) is a machine learning software for bioimage analysis. This course shows you how to use Ilastik to segment cells in 2D & 3D images. 

**Instructor**: Minh-Son Phan, IAH Institut Pasteur, minh-son.phan@pasteur.fr

**Outline**
- Introduction of how machine learning is used in practice for image analysis
- Hands-on
  - 2D nuclei segmentation
  - 3D nuclei segmentation

**Preparation**
- Ilastik: download the latest version (1.4.1rc2) [here](https://www.ilastik.org/download). For Apple PC, use the version compatible with the chipset (Apple intel or Apple silicon). Please install Ilastik before the course since the installation is a bit long.
- Fiji: http://fiji.sc/
- Download the [dataset](https://drive.google.com/file/d/1y-shYx_DuZfwHG0aGRI7c1BK_W8Ko0IX/view?usp=sharing)

**Remark**: please bring your mouse since we will draw a lot! Using the trackpad of your laptop will make you cry!


# Topic 2: Icy for Bioimage Analysis

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

For Mac : Download the DMG file (x64 for Intel Mac, ARM64 for Apple Silicon M1, M2, M3 and M4) 
For Windows : Download th MSI file
For Linux : Download the DEB file and run this command from where it has been downloaded on your computer : ```sudo dpkg -i ./jdk-21_linux-x64_bin.deb```

Ask the helpers if you have doubt about what version to install.

### VTK

VTK (Vizualization ToolKit) is the 3D framework for Icy.

If you are using a Mac (Intel or Apple Silicon) you should be able to run it without issue if you are minimum on MacOS 13 Ventura.

If you are using a Windows 11 and 10, there is actually an issue with VTK and you may not be able to run VTK.

If you are using a Linux Ubuntu 24, you may need to download and install two packages with ```sudo apt install``` :
- libopengl-dev
- libvtk9-dev

If you are using a Linux Ubuntu 22, or an older version of MacOS 13 Ventura, you may not able to run VTK properly.

If you are not able to run VTK in Icy, it's not a huge problem, you just have to skip the 3D part of the training course.

### Installing Icy

**On Windows and Linux : If you have tried to open Icy with the old TAR.GZ file, you need to erase the old instance of Icy. Ask the helpers if it's the case.**

You can dowload the alpha of Icy from here:

[MEGA](https://mega.nz/folder/O8tTmZCC#d4Q8IGyDT38g-owsldJxMw)

[Google Drive](https://drive.google.com/drive/folders/1HzOoC6JLYcDfQQrrZC7QXRBmXHhgqYGa?usp=share_link)

[OneDrive](https://1drv.ms/f/s!AjYcCRMJw3HvsF3ysVnK9jdvuPRn?e=vMv5XO)

- If you are on a Mac :
  - Download the DMG file then open it by double-clicking it
  - Move the Icy 3 app on your Applications folder
  - Double click on the newly copied Icy 3 application
  - If your not able to launch it because of Apple security, go to : System Settings > Privacy and Security > click on Open Anyway
- If you are on a Windows :
  - Download the ZIP file and unzip it
  - Open the unzipped folder then double click on Icy.exe
- If you are on Linux :
  - Download the TAR file and unzip it
  - Open the unzipped folder in the terminal
  - Execute ‘icy’ file with sh in your terminal with : ```./icy```

 
If Java was properly installed, you should see a window like this one:
<img width="1452" alt="Screenshot 2025-05-06 at 10 01 58" src="https://github.com/user-attachments/assets/dac20284-1028-4851-a441-b5b7523da2fa" />

In the first run, Icy will copy libraries to an adequate (.icy/) folder in your home directory.

### Downloading the training materials

You can find the training materials inside the "documents" and "images" folders in the link above.


