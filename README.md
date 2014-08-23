Very Simple Introductions to APIs using Twitter and Python.
===================

You will need to sign up for a developer account. If you have difficulty manuevering through the site, I have a set of visual instructions: [here](http://strangedata.ghost.io/2014/08/14/getting-started-with-twitter-api/)

These files use the *tweepy* module.
```language-python
pip install tweepy
```

You will need your own codes like these (in the Settings Tab on the developer's website) to access the API from python:
![](http://strangedata.ghost.io/content/images/2014/Aug/Screenshot-2014-08-13-11-37-45.png)
Make sure to generate your own application codes as these will not work for you.


* **01_search_twitter.py**  
  Uses the search() method.  
  You can find an example here: [Using Python to Find Happy People Around You](http://strangedata.ghost.io/2014/08/14/twitter-python-happy-people/)
  
* **02_user_timeline_twitter.py**  
  This also includes a *csv* module to save your results to a csv file.  
  Uses the user_timeline() method to check on another user's twitter feed.  
  
* **03_post_to_twitter.py**  
  Uses update_status() method.  
  Note: Make sure to change your application status on Twitter to Read-Write, otherwise you won't be able to post to your account.
