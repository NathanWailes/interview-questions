
# Answers to GitLab Questions

#### Question 1 -  If you are going to install something on Linux, what are the different ways that could be done?

Preface: I have to admit that Linux is something that I'm not extremely familiar with yet. I worked with it at Infer when I needed to interact with our company's internal server, and at Service Fusion when deploying to their development and production servers, and when creating my own projects on PythonAnywhere.com, but I've been using Windows laptops rather than Apple's Unix-based laptops, and so I can't remember ever needing to install something on Linux.

That said, without looking it up on Google (which is how I would normally deal with a question like this), I would guess that the two major ways to do it would be by 1) downloading a binary and 2) installing from the source code (I think by running "make" on it?). I've never run into a situation where I've needed to install from source code, but my understanding is that it's useful for installing the bleeding-edge version of software.

#### Question 2 - What are the advantages and disadvantages of using a Web framework such as Rails?

Advantages

- It can save you a lot of time that you might otherwise need to spend implementing the functionality the framwork offers.

Disadvantages

- Depending on your situation, no web framework may offer the particular features that you need.
- Using a web framework may require an additional upfront investment of time to learn how to use it.
- A web framework is an additional dependency, which can somewhat tie your fate to that of the web framework. For example, the web framework is abandoned by its developers, or if there's any issue with the license down-the-road (as seems to have happened briefly with React), you could end up with a problem.

#### Question 3 - What would you do if you found a bug in your software and wanted to use git to help identify when this problem started?

- I use PyCharm (JetBrains) when working on projects, and they make it very easy to see the history of each line in a file.
- If I'm the only person working with the file, and the bug popped up recently, I would select the portion of code I want to see the history of, then right-click, select "Local History", and then "Show History for Selection".
- If I have been working with other people, and I suspect the problem was caused by someone else making a change to one of the lines of code, I would right-click in the file, select "Git", and then "Annotate", and it'll open a new left-hand-side column that shows the date that each line was last modified, and who modified it.
- I am also aware of the "git blame" command, but because I use PyCharm I've never run into a situation where I've needed to use it directly.
- I've been using SourceTree to do my local git work, and I remember it also has the ability to do a git blame on a file.

#### Question 4 - Describe the resources or steps you may use to resolve a customer’s problem when you don’t know the answer. (Make assumptions wherever you need to about how the GitLab team works).

- If it's an important customer or an urgent problem, I would be inclined to notify my supervisor immediately of the situation and continue with the steps below while waiting for any additional instructions.
- I would check the company's internal wiki for any relevant information that might help me resolve the issue.
- I would ping coworkers on our internal chat to see if they had any experience with the issue.
- If checking the wiki and asking coworkers didn't resolve the issue, I would notify my supervisor that I had an issue I couldn't resolve, explain what steps I had already taken, and would ask for their help to resolve it.


#### Question 5 - If you have them, please provide links to what you consider some of your best answers on forums such as Stack Overflow, Reddit, or in projects on GitLab, GitHub, etc.

- [How to create a new Python project using PythonAnywhere, Bitbucket, SourceTree, and PyCharm](https://nathanwailes.atlassian.net/wiki/spaces/MTOVT/pages/25788541/How+to+create+a+new+Python+project+using+PythonAnywhere+Bitbucket+SourceTree+and+PyCharm)
  - This is on my personal wiki. I'm pretty proud of it, it took a lot of work to explain every step in-depth, including pictures. I think this gives a good idea of the level of quality I aim for with very important / highly-trafficked wiki pages.
- [Stack Overflow - How can I combine Vue.js with Flask?](https://stackoverflow.com/questions/46214132/how-can-i-combine-vue-js-with-flask)
  - This isn't as in-depth as the one above, but it's probably the longest and most-helpful (to me) answer I've given on Stack Overflow.
- [GitHub - flask-dance - How does twitter.authorized know it's me?](https://github.com/singingwolfboy/flask-dance/issues/88)
  - This shows some back-and-forth I had recently with the maintainer of flask-dance, which makes it easy to add Oauth login to a Flask website. I'm not sure if it qualifies as an answer as you would define it, but it shows me working with another person to try to resolve a problem.