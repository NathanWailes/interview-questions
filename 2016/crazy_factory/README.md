# Hello future colleague!

The Crazy Factory IT Department is currently looking for promising new candidates to join our ranks
within the ever growing online business of Crazy Factory Trading Ltd. We’re offering excellent work
opportunities, including but not limited to: Working with modern technologies, be a part of a young
and motivated team, flat hierarchies, awesome lunches, a relaxed and fun work atmosphere, modern
hardware, challenging tasks and many other perks!

This test serves two equally important goals. We want to get to know you! And we want to check out
your various abilities and experiences. We want to know what you achieved so far in your
professional career, your English communicative skills and your approach at problem solving. We’re
looking for “fresh to market” candidates as well as “long time experienced” developers, so just answer
honestly and to your best abilities.

We realize many questions can be answered quickly by using Google. We don’t mind if you use your
favorite tools to help you because this is perfectly acceptable in the office anyway. During the test
though we value honesty and would be happy if you let us know when and why you had to look up
certain points. If you can’t answer a question you may skip it entirely.

Create a new file for answering the test’s questions. You may use any tools to aid you, just make sure
you’re sending in a single PDF file for us to read in the end!

Good luck and enjoy the test,

_The CF Developer Team_


# 1. The web!

## 1.1. Optimize SQL for performance.

The following code is used to create two entries in ​stock_ledger​ for each found entry in
quality_control_articles ​– one with positive quantity and one with negative quantity.
```
$result​ = ​mysql_query​(​'SELECT article_id, quantity FROM quality_control_articles
WHERE qc_id = 720'​);
​
while​(​$row​ = ​mysql_fetch_array​(​$result​))
{
    ​mysql_query​(​'
        ​INSERT INTO stock_ledger SET
        ​article_id = "'​.​addslashes​(​$row​[​'article_id'​]).​'"
        ​bin = "quality_control",
        ​quantity ="'​.​addslashes​(​$row​[​'quantity'​]).​'"
    ​'​);
    ​mysql_query​(​'
        ​INSERT INTO stock_ledger SET
        ​article_id = "'​.​addslashes​(​$row​[​'article_id'​]).​'"
        ​bin = "main_bin",
        ​quantity = "'​.​addslashes​(­​$row​[​'quantity'​]).​'"
    ​'​);
}
```
If the SELECT returns 100 entries, this makes 201 queries.

Can you do this come up with a way to do this with only 2 queries or even with a single query? What
are the benefits and drawbacks of each approach.

## 1.2. Analyzing SQL functionality

Imagine the following code is used to regularly check orders to have at least 1 line. Orders without
any lines should be marked as empty and a notification be sent to a team member.
```
$result​ = ​mysql_query​(​'SELECT order_id, COUNT(*) AS number_of_lines FROM orders
LEFT JOIN order_lines USING (order_id) WHERE !checked GROUP BY order_id'​);
​
while​ (​$row​ = ​mysql_fetch_array​(​$result​))
{
    ​mysql_query​(​'UPDATE orders SET checked = 1, is_empty = '
        .(​$row​[​'number_of_lines'​] == ​ 0 ​ ? ​ 1 ​ : ​ 0 ​).​' WHERE order_id = "'
        .​addslashes​(​$row​[​'order_id'​]).​'"'​);
    ​if​ (​$row​[​'number_of_lines'​] == ​0)
        send_email(
            ​'sales@example.com​'​,
            ​'Empty order found'​,
            ​'Order ID '​.​$row​[​'order_id'​].​' has no lines!'​);
}
```
Does the code pose any problems? Can it be improved in general?

## 1.3. Write an SQL statement

Given the following data structure:

```
Table: posts
- post_id
- content

Table: comments
- comment_id
- post_id
- create_datetime
- content
```

Write an SQL query that returns each post (sorted alphabetically by content) and its last comment, in
a way that it can be used to show a list like:

| Post                | Most recent comment                                         |
|---------------------|-------------------------------------------------------------|
| More cat videos     | I disagree, these are hilarious! (created 2013­06­21 14:52) |
| My cutest cat video | Great! (created 2013­06­21 14:53)                           |

## 1.4. What do you need to do to avoid this dialog?

```
Confirm (dialog)
To display this page, Firefox must send information that will repeat any action (such
as a search of order confirmation) that was performed earlier.

<Resend>    <Cancel>
```

## 1.5. Migrating CSS to SCSS.

You are given a CSS file like the following:
```
.grid​ {
    ​display: ​block​;
    border: 1px solid #F0F;
    ​margin: ​ 0 ​ ​auto​;
}
​
@media​ (min­width: ​640px​) {
    .grid > .tile​ {
        ​float: ​left​;
        ​width: ​50%​;
    }​
    .grid > .tile.width­2​ {
        ​width: ​100%​;
    ​}
}​
@media​ (min­width: ​1024px​) {
    .grid​ {
        ​max­width: ​80%​;
    ​}
    .grid > .tile​ {
        ​width: ​33%​;
    ​}
    .grid > .tile.width­2​ {
        ​width: ​66%​;
    ​}
    .grid > .tile.width­3​ {
        ​width: ​100%​;
    ​}
}
@media​ (min­width: ​1440px​) {
    .grid​ {
        ​max­width: ​65%​;
    ​}
    .grid > .tile​ {
        ​width: ​25%​;
    ​}
    .grid > .tile.width­2​ {
        ​width: ​50%​;
    ​}
    .grid > .tile.width­3​ {
        ​width: ​75%​;
    ​}
    .grid > .tile.width­4​ {
        ​width: ​100%​;
    ​}
}
​
.grid > .tile​ ​.title​ {
    color: #F0F;
    ​display: ​none​;
}
​
@media​ (min­width: ​1024px​) {
    .grid > .tile​ ​.title​ {
        ​display: ​block​;
    ​}
}
```
Write a short SCSS file as a replacement. Use variables, mixins and loops for recurring use­cases.

# 2. Code Review

In this section we ask you to do reviews for short code snippets.
Imagine each piece is the work of a fellow coworker and you have to provide him with notes to
improve stability, quality and performance of his code.

## 2.1. Review the following ​PHP/HTML ​snippet.

```
if​ ((​isset​(​$_COOKIE​[​'area'​]) ? ​$_COOKIE​[​'area'​] : ​'p'​) == ​'f'​)
    ​$html​ = ​'<h2>Fashion</h2>'​;
else
    ​$html​ = ​'<h2>Piercings</h2>'​;
​
$html​ = ​'<table>'​;
​
foreach​ (​$_POST​ ​as​ ​$field​ => ​$value​)
{
    ​if​ (​$_POST​[​$field​] == ​'special1'​)
        ​$_POST​[​$field​] = ​'Block'​;
​
    ​$html​ .= ​'
      ​<tr>
      <td>'​.
       ​$field
      .​'</td>
      ​<td>'​.
      $value
      .​'</td>
      ​</tr>
​      '​;
}
​
$html​ .= ​'</table>'​;
```

## 2.2. Review the following ​PHP ​snippet.

```
$mapping​ = ​array​(
   'carnivore'​ => ​array​(
       ​'cat'​ => ​ 3 ​,
       ​'dog'​ => ​ 6
   ),
   ​'herbivore'​ => ​array​(
       ​'horse'​ => ​ 7
   )
);
​
foreach​ (​$mapping​ ​as​ ​$type​ => ​$animal​)
{
   ​foreach​ (​$animal​ ​as​ ​$species​ => ​$id​)
   {
       ​$data​ = ​trim​(​$raw_data​);
       ​if​ (​$data​ == ​''​) {​return​ ​'Error: no data'​;}
       ​if​ (!function_exists(​'base64_encode'​)){
           ​return​ ​'Error: func base64_encode n/a'​;
       }
   }
​   $data​ = ​json_decode​(​base64_decode​(​$data​));

​   $found_info​[​$species​] = ​$data​[​$id​];
}

return​ ​$found_info​;
```

## 2.3. Review the following ​JavaScript ​snippet.
```
class​ ​Entity​ {
    constructor(​/*private*/​ validateFn) {
        ​this​.validateFn = validateFn;
    }
}
​
class​ ​Person​ ​extends​ Entity {
    constructor(​/*public*/​ lastName = ​"Doe"​, ​/*public*/​ firstName = ​'John'​) {
​        super​(() => firstName && lastName)
    }
    get isValid() => ​this​.validateFn;
}
​
let​ ​person​ = ​new​ Person();
​
if​ (person.isValid) {
    personApi.create(person);
}
```
(You can assume ​`personApi` is instantiated correctly)

# 3. Experiences, preferences and random topics

These questions can help us to get to know you quickly and are also a great place
to brag about your
opinions and preferences!

## 3.1. SPA Technology stacks

If you had to develop a large Single Page Application by yourself, which technology
stack would you
choose? Would it be different for a large team of developers and why?

## 3.2. Search Engine optimization

What are important factors for a website, when going for a high ranking in major
search engines?

## 3.3. Testing

Have you ever used some kind of testing during a project? What’s your opinion on
TDD/BDD?

## 3.4. Language Portfolio

Which programming languages are you familiar with? Tell us about your experiences
and favorites!

## 3.5. IDE and Toolchain

What IDEs do you use and why? Have your worked with code repository systems? How
about Grunt, Gulp, Webpack, Jenkins, Jira, Slack, Trello and others? Are there tools
you would like to keep on using? Or tools you’d be happy to get rid of?

## 3.6. Professional career

What motivated you to become a software developer? What is your current/last
position and what are/were your responsibilities?

## 3.7. Code samples

Can you show or describe some projects you were working on? Do you contribute to
any Open Source projects we might take a look at? You may brag about some private
projects as well! :)

## 3.8. Mobile Apps

What is your experience with mobile app development and related frameworks?

## 3.9. What other related skills do you possess that might be of use?

Skilled Sysadmin? Cloud Hosting Guru? Unity3d Modder? Skilled Pixel pusher?
First­class chef?

## All done?

Wrap up your answers in a PDF and send them to
[dev@crazy­factory.com](dev@crazy­factory.com). We’ll get back to you shortly! :)


