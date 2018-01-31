

# Answers to the Crazy Factory Developer Test

_During the test though we value honesty and would be happy if you let us know when
and why you had to look up certain points. If you can’t answer a question you may
skip it entirely. Create a new file for answering the test’s questions. You may
use any tools to aid you, just make sure you’re sending in a single PDF file for
us to read in the end!_

# 1. The Web

#### 1.1 Optimize SQL for performance

I looked at the query and saw two major parts: getting a list of things, and then
setting a bunch of things. I notice that the “setting” part depends on the
“getting” part for some of the values its setting. From the hint that it could
be done with one query, and from working with SQL at my current job, I guessed
that I might be able to do things with a single query that used an inner select
statement to get the necessary info for the “setting” part.

At my job I don’t do any modification of SQL tables, only “select” queries, so
I’m not as familiar with that part of the challenge. So I decide to do an
experiment online. I google “SQL simulator” and go to http://sqlfiddle.com/.
```
insert into stock_ledger
```
There’s no comma after the ‘article_id’ line when doing the ‘insert’ statement.

Googled for “SQL simulator”.

#### 1.2. Analyzing SQL functionality

Hmm…

- I’m not sure I understand what “order lines” are. I’m guessing an “order” is like
Amazon’s concept of a “basket”, and an “order line” is like an individual item in
the basket.
- I don’t understand what the “!checked” clause means in the “$result” query.
  “checked” seems to be a Boolean column but I’m not sure what it signifies…
  Update: after looking at the ‘UPDATE’ query, I see that it indicates whether
  a row has been checked or not. I guess I’m supposed to assume that the value
  is initialized properly to ‘0’ when the order is created?
- Can order items be removed from an order? If an order is checked, and then an
 order item is removed, does the code there also set ‘checked’ back to ‘0’?
- I’m not sure what “mysql_fetch_array” does. I have an idea, but I’m not totally
 sure, so I’m going to Google it…and from
 [this link](http://php.net/manual/en/function.mysql-fetch-array.php), the
 combination of a ‘while’ loop with that function seems to be something like
 Python’s “generator” functions, where it keeps providing you with a new value
 until there aren’t any left.
- Ok, well now that I’m looking at the inner logic of the ‘while’ loop, it seems
 to be updating the value of ‘number_of_lines’ before the ‘if’ statement, so that
 the ‘if’ statement will never return ‘true’…but on the other hand, ‘$row’ is
 probably a copy of the data in the SQL table, and so updating the SQL table
 shouldn’t affect the values in $row.
- Personally I like having SQL code formatted the way I would have it in a SQL
 editor, like this:
```
$result = mysql_query ( 'SELECT order_id, '
                        'COUNT(*) AS number_of_lines '
                        'FROM orders '
                        'LEFT JOIN order_lines '
                        'USING (order_id) '
                        'WHERE !checked '
                        'GROUP BY order_id' );

while ( $row = mysql_fetch_array ( $result )) {
    mysql_query ( 'UPDATE orders '
                  'SET checked = 1, '
                  '    is_empty = ' .( $row [ 'number_of_lines' ] == 0 ? 1 : 0 ). ' '
                  'WHERE order_id = "' . addslashes ( $row [ 'order_id' ]). '"' );

    if ( $row [ 'number_of_lines' ] == 0)
        send_email('sales@example.com ' , 'Empty order found' ,
                   'Order ID ' . $row [ 'order_id' ]. ' has no lines!');
}
```

#### 1.3. Write an SQL statement
I do a lot of SQL queries at my job.
Off the top of my head, I think I’d try something like this:
```
select posts.content,
       comments.content,
       comments.create_datetime
from posts
left join comments
on posts.post_id = comments.post_id
order by posts.content
```
Just for fun, I’ll test it using sqlfiddle…and it seems to work:
http://sqlfiddle.com/#!15/849c6/1/0

#### 1.4. What do you need to do to avoid this dialog?
I don’t know, so I’ll just Google the error message…

…and I see the following links (among others):

- http://stackoverflow.com/questions/12622019/preventing-firefox-reload-confirmation
- http://stackoverflow.com/questions/9871705/to-display-this-page-firefox-must-send-information-that-will-repeat-any-action

[This answer](http://stackoverflow.com/a/9871738/1513115) in particular seems easy
to understand and plausible:

> This happens when you refresh a page that is the result of a POST request (as
opposed to a GET request). To avoid it, you can use the POST/redirect/GET pattern.

#### 1.5. Migrating CSS to SCSS.

I haven’t used CSS in a while, and never professionally, so I’m not as familiar with
the various tricks available. I need to refresh my memory of what mixins are, so I’m
going to Google it…
- I came across [this Stack Overflow
question](http://stackoverflow.com/questions/12049108/), which showed how to nest
immediate-child selectors in Sass.

# 2. Code Review

#### 2.1. Review the following PHP/HTML snippet.

I haven’t worked with PHP in a while, and when I did it was on my own and not part of
a team, so I’m not sure how much I’ll be able to notice, but I’ll give it a shot:

- I’m not sure where the $html variable is first created and when it is finally used
to render the page, but I do see that the dot-equals operator is present later on in
the snippet, presumably to gradually build the HTML that’s going to be rendered, but
earlier in the snippet the dot-equals operator is not used, which means that the
variable is getting overwritten each time with the new value without retaining the
old values. That seems unintentional.
- I find the first ‘if’ condition very hard to read. I generally like to create a
variable that explains what the Boolean value is representing. It looks like it’s
also possible to rearrange the logic to make it simpler:
```
$user_is_in_the_piercings_area = !isset($_COOKIE['area']) || $_COOKIE['area'] != 'f';

if ($user_is_in_the_piercings_area)
```
- I prefer not having opening braces on their own line.
- I don’t understand why the `<td>` / `<tr>` tags are so broken up, I would change it to something like this:
```
$html .= ‘<tr>
              <td>’ . $field . ‘</td>
              <td>’ . $value . ‘</td>
          </tr>’ ;
```
- ‘special1’ isn’t a very helpful key name.
- There’s no explanation of what the “Block” field value does.
- There are a lot of hard-coded values here…things like “Piercings” and “Fashion”
seem like things that would be likely to change over time. This code doesn’t look
like it will be easy to change in the future. I’ve done a little work with Flask
(Python), and things are done very differently there.

Here’s what I ended up with:
```
$user_is_in_the_piercings_area = !isset($_COOKIE['area']) || $_COOKIE['area'] != 'f';

if ($user_is_in_the_piercings_area)
    $html .= '<h2>Piercings</h2>';
else
    $html .= '<h2>Fashion</h2>';

$html .= '<table>';
foreach ($_POST as $field => $value ) {
    if ($_POST [ $field ] == 'special1')
        $_POST [ $field ] = 'Block';

    $html .= '<tr>
                  <td>' . $field . '</td>
                  <td>' . $value . '</td>
              </tr>';
}
$html .= '</table>';
```

# 2.2. Review the following PHP snippet.

- I would rename $mapping to something like $consumption_class_to_animals.
- I would rename $type to $consumption_class.
- I would rename $animal to something like $animal_name_to_id.
- I wouldn’t have opening braces on their own lines.
- It isn’t clear to me where $raw_data is defined; I generally like to initialize a
variable as closely as possible to where I’m going to use it.
- I might rename the first occurrence of $data to $trimmed_data.
- When $data is reassigned to the result of json_decode(), I might rename that to
something like $json_data, or something else that better reflects the contents of
the variable.
- I don’t understand what the inner for-loop is trying to accomplish.
- The error messages aren’t very helpful.
  - ‘no data’ is vague
  - ‘func n/a’ is vague
- I’m not familiar enough with PHP to know whether the ‘json_decode()’ and
‘base64_decode()’ functions are potential sources of problems, but encoding and
decoding is a frequent source of problems in my projects and at my job, so that
might be worth looking into.
- The $found_info[$species] = $data[$id]; line seems to be referencing variables
that are not in that loop’s scope ($species and $id). Unless I’m missing something,
those variables should only be used in the inner for-loop.
- It isn’t clear where $found_info is initialized, and whether it should still
exist by the final ‘return’ statement (return $found_info;).
- In short, I can’t tell what this code is trying to do.

# 2.3. Review the following JavaScript snippet.

- I don’t work with JavaScript as part of my job, so I could end up missing a lot.
- I’m not familiar with the syntax for constructors in JavaScript, so I’m Googling it.
- I’m not immediately sure what “Fn” stands for, but after looking at the code for
a minute I see that it seems to be an abbreviation for “function”.
- “() =>” looks strange to me, so I’m Googling it. Given that it’s being passed to
the Entity constructor—that seems to take a function as its only argument—I suspect
I know what it’s doing, but I want to be sure.
  - And as I suspected, it seems to be similar to (the same as?) what in Python are
  referred to as “lambda expressions”.
- The ‘super()’ line in the Person constructor doesn’t end with a semicolon…I think
semicolons are mandatory in JavaScript…I’m going to Google it…and it looks like
they’re not always mandatory, and there’s some debate about whether you should
always include them or not.
let person = new Person(); looks strange to me because I vaguely remember that new
objects in JavaScript are instantiated with the ‘var’ keyword. I’m going to Google
it…
  - I came across these articles:
    - http://stackoverflow.com/questions/762011/let-keyword-vs-var-keyword
    - http://programmers.stackexchange.com/questions/274342/is-there-any-reason-to-use-the-var-keyword-in-es6
  - From this comment (combined with my previous experience) it seems ‘let’ is
  preferable to ‘var’, but that ‘const’ is preferable to ‘let’, so it may be
  preferable to switch ‘let’ to ‘const’.
- The ‘person.isValid’ call in the bottom ‘if’ statement doesn’t have trailing
parentheses. In Python I believe an if statement will return ‘True’ if you give
it a reference to a function by mistake instead of calling the function. I’m not
sure if that happens in JavaScript, so I’m going to try it…and yes, it’s the same.

# 3. Experiences, preferences, and random topics

#### 3.1. SPA technology stacks

#### If you had to develop a large Single Page Application by yourself, which technology stack would you choose?

Honestly this question may be beyond my experience with web development.

At Infer I believe the original vision was to have a single-page experience, and we
sort-of have that; they use Flask to route and a custom technology they created on
top of Coffeescript called “Reactive Coffee” to dynamically refresh certain parts
of the webpage.

My understanding is that the key to a single-page experience is using JavaScript
to only change certain parts of the page when users click buttons instead of
refreshing the entire webpage. I might go with Flask or Django and whatever the
most-dominant JavaScript framework is (Angular?).

On the other hand, I’ve heard Pieter Levels (of levels.io) say that PHP is a
much better tool for working on projects by yourself, so I might be inclined to
use that instead. Or maybe just WordPress, depending on what I needed.

#### Would it be different for a large team of developers? Why?

I don’t think I’m experienced enough with web development to know what tools are
better for solo developers vs. large teams. But if I think about actual
construction projects (constructing buildings), there are certainly differences
between how people construct smaller buildings and how they construct skyscrapers,
and so it seems plausible to me that the same pattern would show up in software
development.

So, like I said above, I might be inclined to use WordPress or PHP for a project
I’d be working on by myself, and something like Flask or Django for a project
involving a large team.

#### 3.2. Search engine optimization

#### What are important factors for a website, when going for a high ranking in major search engines?

I’m not an expert on this, so I can only rely on my vague memory of what I’ve read,
and I’m probably only going to be mentioning obvious things.

- I vaguely remember someone saying that the age of your website is a large factor
in its ranking.
- I also vaguely remember hearing that the similarity of your domain name to the
search query can have a big impact.
- Make sure your website doesn’t have some kind of gap in its page structure that
makes it impossible for bots to reach all of the pages on your website that you
want crawled.
- My understanding is that Google punishes people who engage in certain kinds of
spamming (like having bots posting comments on WordPress blogs).
- On the other hand, from having read about RapGenius gaming the system to increase
its ranking on Google, it seems like some kind of link sharing / link exchanging
can help you boost your ranking.
- At a very basic level, I vaguely remember hearing that it’s important to have
your website follow standard HTML conventions, with descriptors of the page
content in one of the tags (I can’t remember the name of it…Update: I just Googled
it, I was thinking of the ‘meta’ description).

# 3.3. Testing

#### Have you ever used some kind of testing during a project?

Yes, we use Doctest and unittest at Infer, and I’ve used them when putting code in
the Data Analyst code repository.

#### What’s your opinion on TDD/BDD?

I think it’s a very interesting idea, and I’d be open to trying it; I don’t have a
strong opinion one way or the other about whether it should be done or not. I’m a
big fan of the website PythonAnywhere.com, and the developers there use TDD, and
one of the cofounders wrote a book on TDD with Django.

I do suspect that over time software development may move closer to the kind of
structured approach we see when people are designing and constructing buildings,
and TDD would seem to be in-line with that trend.

On the other hand, one of the things that has occurred to me is that testing can
be thought of making your code “stronger” / more resilient, and that that is
analogous to using stronger materials when constructing a building. But when
constructing a building, there are parts of the building that are more important
to have reinforced, and there are other parts that may not need to be reinforced
much at all (like many of the internal walls). And I thought that could be a good
analogy for a codebase: there are sections of code that may be tangential and
one-off, and future code is not going to build on top of that code, and so it
isn’t necessary to reinforce that code with thorough tests. But other sections of
the codebase may have lots of other code “built on top of it”, and thus it may be
much more important to have those sections thoroughly tested.

# 3.4. Language portfolio

At this point I’m most familiar with Python, and it’s also my favorite.

Before Python I was mainly working with Processing, a data visualization library
for Java, so basically I was working with Java, but I was using Processing’s
stripped-down editor instead of Eclipse, so larger projects were harder to manage.

I’ve also worked with PHP and thought it was much easier to get-up-and-going with
than the frameworks out there (Rails, Django). I’ve done some reading and it seems
like my experience is a pretty common one.

I’ve read through Michael Hartl’s Ruby on Rails tutorial twice, but ended up
preferring to study Python because it is used for both web development and in
finance (which is another interest of mine). But I would be open to working with
Ruby.

# 3.5. IDE and toolchain

#### What IDEs do you use and why?

At the moment the only IDE I’m using is PyCharm. Why: I do basically all of my
personal projects and work-related stuff with Python, PyCharm was recommended to
me by several of the engineers at my current company, and it seems to be a
dominant (if not the dominant) IDE for Python. It’s really a pleasure to work
with. But, again, I haven’t worked with many other IDEs, so I’m open to the
possibility that there’s some other IDE I could benefit from using instead.

#### Have you worked with code repository systems?

Yes. I use Bitbucket to store my code and often pull code from GitHub. I also used
Subversion a little bit when I was helping to work on a PC game mod back in high
school.

#### Have you worked with Grunt, Gulp, Webpack, Jenkins, Jira, Slack, Trello and others?

We use JIRA, Slack, and Jenkins at Infer, and I’ve had some brief exposure to
Trello, but I haven’t used Grunt, Gulp, or Webpack. I haven’t had enough exposure
to Jenkins to say that I’m very familiar with it.

#### Are there tools you would like to keep on using?

I don’t think I’m very tied to particular tools. I’m a big fan of the Atlassian
products I’ve used (JIRA, Confluence, Bitbucket, and SourceTree), but I haven’t
had much exposure to competing products and so I can’t say that I would prefer
Atlassian to their competitors.

I’m also a big fan of Python and PyCharm, but not so much that I would turn down
a chance at a junior developer position in some other language.

#### Are there tools you’d be happy to get rid of?

The only one I can think of off the top of my head is pgAdmin, which I use to do
SQL queries. There are a bunch of better tools available online, but for security
reasons we can’t use them at Infer.

# 3.6. Professional career

#### What motivated you to become a software developer?

I have several friends who knew from at least middle school what they were
interested in and what they wanted to do professionally. I was not like that
at all. I majored in psychology and philosophy in college because I didn’t
know what profession I wanted to go into, but I knew I wanted to understand
how to make myself happy. After college I was thinking about becoming a lawyer,
but after spending several years reading and thinking I concluded that law was
not the best possible skillset to learn. Instead, I concluded that the four
skillsets I should focus on were: entrepreneurship, programming, finance, and
mathematics.

There were a bunch of reasons I concluded that programming was a valuable skillset:

- Computers are like the modern-day equivalent of the cannons of the 18th-century:
they’re extremely powerful, and if you know how to use them well you can become
extremely powerful, but to be used properly the technology needs to be studied
(just as Napoleon studied artillery while at the École Militaire).
- Programming is a younger profession than law and is more progressive in many
of its social norms. As a lawyer I would have been expected to wear a suit, and
remote work would be much more difficult to get than as a software developer.

#### What is your current/last position?

I’m currently a Data Analyst. At my last job (two years ago) I was basically an
Account Manager.

#### What are/were your responsibilities?

- Use our internal web app to build machine-learning models.
- Use SQL / Python to investigate our customers’ Salesforce data to deal with
problems that pop up.
- Document how we’re doing things.
- File bugs when the web app doesn’t work properly.
- Automate our work as much as possible.
- Research various miscellaneous questions that pop up in the course of doing
business.

# 3.7. Code samples

[Obfuscated screenshots of my code for Infer](https://www.dropbox.com/sh/72peo3dd1uwgv9y/AACip5HjY3rHHRmVbRThtHCga?dl=0)

- This is the 'analyst repository', where I kept my code that helped me to
automate my job.
- I pushed for its creation and at the moment I'm the only Data Analyst who has
used it. It has 3000+ lines so far.
- The first screenshot shows my nested folder structure, which allowed me to
'slot in' new code easily.
  - I wanted to automate a very large responsibility that had many smaller
  aspects, which I knew would require a lot of code that I couldn't write all
  at once.
  - I spent a good amount of time thinking about how I wanted my code organized
  because I've run into problems in the past when I rushed things at the beginning.
- The second screenshot shows a typical example of the source code.
  - I spent time adding doctests (which show up as the highlighted lines) because
  I was interfacing with our existing codebase via an API, and the behavior of
  that API was subject to frequent changes.
  - PyCharm makes it easy to add some basic docstrings to indicate the type of
  the arguments and return value, so I spent some time filling those in.
  - I did not fill in the docstrings as much as I should have with explanations
  of the functions. I know I should have. However I think the descriptive
  function names partially make up for it.
  - You can see that I like to keep my functions short, with the code at one
  level of abstraction as much as possible.
  - I like using longer, more-descriptive names because I've had many problems
  in the past remembering how my code worked when I used shorter names. But I'm
  open to using shorter names as well.
  - The code reads top-to-bottom, with the top-most function the one meant to
  be accessed from outside the file and the lower functions (with leading
  underscores in their names) meant to be used only internally to that file.

https://bitbucket.org/NathanWailes/ill-metric/src

- This is a small weekend project that works with the EchoNest API.
- I was working with Martin Connor of rapanalysis.com to try to come up with a
rap-equivalent of basketball's "Player Efficiency Rating": a metric for ranking
rappers by the characteristics of their songs.
- As part of a first-stab, Martin wanted to have numbers measuring various
musical characteristics of a large body of rap songs that he had (eg tempo, BPM).
- My job was to take his list of songs and get the necessary stats from EchoNest.
- Various complications made the project take an entire weekend.
- This was one-time-use code, so I didn't put much effort into making it elegant
(for example, the functions are longer than I normally like to have them and
there are no docstrings / tests).
- However you can see how I like to structure my files and folders so that when
you run an import statement, the import statement reads as much as possible
like a sentence: 'get / scrape / azlyrics / artist / url_names.py'

# 3.8. Mobile apps
I don’t have much experience but I’m very interested in learning. Two years ago
I watched a bunch of videos on Android development, started going through an
“Android development for Dummies” book, and briefly messed around with some demo
apps in Android Studio, so I have a basic familiarity with Android development,
but I ended up focusing on other projects.

I’ve also spent some time going through Ionic tutorials, but haven’t yet had a
project idea that has made me want to dedicate more time to mobile development.

# 3.9. What other related skills do you possess that might be of use?

I’m very well-read about entrepreneurship, and I’m often able to describe what
other entrepreneurs have done when facing a particular problem. You can see an
example of this here:

http://www.nathanwailes.com/blog/an-email-to-a-friend-with-some-ideas-for-creating-a-repeatable-salesgrowth-process/