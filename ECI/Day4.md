This page collects instructions, links and materials for the Day 4

# Day 4: Key Topics

- What is Deep Learning?
- What is BiaPy?
- How can you use BiaPy?
- Quality control in deep learning: From dataset validation to model performance monitoring.
- Tools available in ZerocostDL4Mic for segmentation, denoising, and super-resolution.
- Example of deep learning in microscopy: Analyzing cancer cell behavior in microfluidics.
- By the end of the lecture, you’ll have a basic understanding of deep learning and how to train an instance segmentation model using BiaPy.

**Instructor** 

Joanna Pylvänäinen, Åbo Akademi University. Turku, Finland, joanna.pylvanainen@abo.fi

## Session 1: Lecture: Leveraging Deep Learning for Microscopy Image Analysis and BiaPy

In this lecture, we will explore BiaPy, a powerful and accessible toolbox designed to help researchers and students train deep learning models for microscopy image analysis. We will start with an introduction to deep learning and its applications in microscopy, followed by a detailed discussion of how BiaPy simplifies the process of building and applying neural networks, even for those with limited computational resources.

> Lecture [here]()

## Session 2: Hands-on: Preparing, Training, and Evaluating a Deep Learning Model for Instance Segmentation in Microscopy

In this comprehensive hands-on session, you will gain practical experience with the full workflow of training a deep learning model for instance segmentation tasks in microscopy, using the BiaPy platform. This session integrates two crucial stages of deep learning workflows: 1) data preparation and training and 2) model evaluation and deployment.

> **[Lecture here]()** <br />
> **[BiaPy plarform](https://biapyx.github.io/)** <br />
> **[Download image for annotation]()** <br />
> **[Download T cell dataset]()** <br />

**Part1: Preparing Data and Training an Instance Segmentation Model**

You will begin by learning how to prepare your data for deep learning, which includes annotating microscopy images and setting up a training dataset suitable for instance segmentation. Through guided practice, you will learn to:

- Annotate images effectively for segmentation tasks.

- Organize and format your dataset for model training.

- Train a deep learning model to segment cells in microscopy images.

By the end of this segment, you will have hands-on experience in developing a deep learning model from scratch and applying it to microscopy data.

**Part 2: Evaluating Model Quality and Applying It to New Data**

Once your model is trained, you will move on to the next phase: Quality Control (QC). Ensuring that your model is robust and generalizes well to new data is essential in any deep learning project. This part of the session will cover:

- The importance of QC in DL-based segmentation.

- Techniques to evaluate the model’s performance using training history and validation results.

- Visualization and inspection of model outputs for quality assessment.

- Deployment of the trained model to segment new, unseen datasets.

By the end of this segment, you’ll be equipped with the knowledge and tools to conduct thorough QC and confidently apply your model to real-world microscopy data.


> **Link to Quality conrol notebook**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Image-Analysis-Hub/Pasteur-BioImage-Analysis-Course-2025/blob/BiaPy_joanna/ECI/Day_4_materials/Quality_control_notebook.ipynb)







