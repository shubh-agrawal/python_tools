# K-means-Color-in-Movie-Posters-
The related blog: https://yujingma.com/2016/02/26/using-web-scraper-and-k-means-to-find-the-colors-in-movie-posters/


Using web scrapping and k-means to extract colors in movie posters; And some related analyses with R
Each movie has their own posters. Even in today’s always-online climate, the movie poster remains a powerful form of advertising. 
Every movie poster has its own color scheme, based on the movie’s type, content, and tone. 
Best movie posters should catch people’s eyes. So what kinds of colors are more likely used in different types of movies?

To answer this question, we need analysis movie posters of different movies. 
First of all, we need to build a training dataset of movie posters. 
So, I used the Bing Image search engine for this. 
By using python to scrape all the movie posters from the website, 
I finally got 112 photos for 4 types of movies (horror, comedy, animation and action movies)

Then I used k-means clustering to do image segmentation, separate the pixels into different clusters based on their colors. 
Here is an example for image segmentation and compression from Bishop’s book Pattern Recognition and Machine Learning
