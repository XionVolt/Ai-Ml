# Semi-Supervised Learning

[Watch this video](https://youtu.be/81ymPYEtFOw?si=MQTeDhP3fGw-0CNy&t=1261)

## What is it?
Semi-supervised learning is a middle ground between supervised and unsupervised learning. It trains a model using **a small set of labeled data** and **a large set of unlabeled data**, improving accuracy while reducing labeling costs.

## Why Use It?
✅ **Cost-Effective** – Less labeled data needed(***because labeling a data requires human effort and thus need money***).  
✅ **Better Accuracy** – Uses unlabeled data for better learning.  
✅ **Real-World Fit** – Many datasets are partially labeled.  

## How It Works?
1. **Self-Training** – Model labels unlabeled data & retrains.  
2. **Co-Training** – Two models teach each other.  
3. **Graph-Based** – Labels spread through data similarity.  
4. **Generative Models** – VAEs & GANs generate missing labels.  

## Where is it Used?
🔹 **NLP** – Sentiment analysis, text classification.  
🔹 **Computer Vision** – Image classification, object detection.  
🔹 **Healthcare** – Disease diagnosis, medical records analysis.  
🔹 **Speech Recognition** – Training models with limited transcribed data.  

## Example
Imagine a dataset of 10,000 cat and dog images:
- 1,000 images are labeled "cat" or "dog."
- 9,000 images are unlabeled.
- The model learns from labeled data and improves by analyzing unlabeled images.

Semi-supervised learning is a **powerful approach** when labeled data is scarce but unlabeled data is abundant.