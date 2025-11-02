# Python-Kiwilytics-Project
Python function to calculate the sum of all integers in a list

# 🧮 sum_list Function

A simple Python program that reads a list of integers from input and returns their sum.

---

## 📘 Description
This function demonstrates basic Python skills including:
- Reading input  
- Validating data constraints  
- Summing list elements  

---

## 🧩 Function Definition

```python
def sum_list(numbers):
    if 1<= len(numbers) <=1000:
        for i in numbers:
            try:
                i = int(i)
            except:
                return
            if not -1000 <= i <= 1000:
                return
        return sum(numbers)
