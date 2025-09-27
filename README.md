# LeafSense
# 🌱 Soybean Leaf Disease Detection using CNN + GradCAM

Automated detection of **soybean leaf diseases** using a **custom CNN** trained on a background-removed dataset with **4 classes**. Includes **data augmentation** for robust learning and **GradCAM/GradCAM++** for explainable predictions.

---

## ⚡ Features
- Preprocessing: resizing + background removal  
- Custom CNN (3 Conv layers + Dense classifier)  
- Data augmentation: flip, rotate, zoom, brightness/contrast  
- GradCAM & GradCAM++ for explainability  
- Evaluation: accuracy, precision, recall, F1-score  

---

## 📊 Dataset
- 4 Classes: Healthy, Bacterial Blight, Rust, Mosaic  
- Oversampled and background-removed images  

---

## 📈 Results
- **Test Accuracy:** XX%  
- **Precision / Recall / F1:** XX%  
- Confusion matrix and GradCAM visualizations included

---

## 🚀 Usage
```bash
python src/train.py       # Train model
python src/evaluate.py    # Evaluate model
python src/gradcam.py     # Generate GradCAM heatmaps
