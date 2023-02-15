# PyAgg
Python News Aggregator
---
![Screenshot 2022-09-04 142859](https://user-images.githubusercontent.com/105527191/188334305-73c9c1e9-f3d0-4a65-988c-fcb0a8849bee.jpg)

the image above shows the FOX News was updated timely
---
**What is the purpose of this project?**

It will automatically update the news from designated website by designated rate

---
**How to run this project**

input ```python manage.py runserver``` in the command prompt

---
**Where is my news resource and how should I update it?**

The news resource feed website is inside ```news/management/commands/startjobs.py```. If you want to change the website, please update it with **feed**

Run ```python manage.py startjobs``` to update the news
