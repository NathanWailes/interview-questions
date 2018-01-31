### Install scripts

Intercom is integrated using a small JS snippet placed into the customer’s own
application or site. Along with basic fields we can also store any custom data
that is entered in the intercomSettings object (like `number_of_photos` for a
photo sharing app). We can store strings, numbers, dates (in unix timestamp
format), and boolean values.  There is a multitude of ways that users do this
incorrectly or sub-optimally.

Please identify the error(s) or improvement(s) in the following snippets and
**craft a response as if you were responding to a customer.**

_Hi John,_

_Thanks for reaching out to us! I took a look at your JS snippet and I think I’ve found the issue:_

_<explain issue>_

_Thank you again for reaching out to us!_

_Nathan_

---
```
window.intercomSettings = {
    email: 'joeomally@example.com',
    name: 'Joe O'Mally',
    app_id: 'abc1234',
    created_at: 1234567890
}
```
_It looks like the name “Joe O’Malley” has a single apostrophe in it, which can
confuse the computer because single-apostrophes are used to indicate the
beginning and the end of the name. Try changing the single-apostrophes
surrounding the name to double-apostrophes._

---
```
window.intercomSettings = {
    email: 'bob@example.com',
    name: 'Bob Sagget',
    app_id: 'abc1234'
    created_at: 1234567890
}
```
_It looks like there’s a comma missing after the app_id value ‘abc1234’, which
can confuse the computer because commas are used to indicate where one
key-value pair ends and a new one begins. Try adding a comma after the ‘abc1234’._

---
```
window.intercomSettings = {
    email: 'bob@example.com',
    name: 'Bob Sagget',
    app_id: 'abc1234'
}
```
_It looks like the snippet is missing a ‘created_at’ key-value pair, which is
necessary for the snippet to work properly. Try adding that in, such as the
following: created_at: 1234567890. Note that the date will need to be a [Unix
timestamp](https://en.wikipedia.org/wiki/Unix_time). You can find the current
date and time as a Unix timestamp at [this link](http://www.epochconverter.com/).
You can also use that link to generate the Unix timestamp for any other
date and time you might want to specify instead._

---
```
window.intercomSettings = {
    email: 'bob@example.com',
    name: 'Bob Sagget',
    app_id: 'abc1234',
    created_at: 1234567890,
    profile_completed_at: 1234567890,
    paid_account: "true"
}
```
_It looks like the value for the ‘paid_account’ setting has quotes around it when
it shouldn’t; ‘paid_account’ take a true/false option, and computers prefer to
have the values ‘true’ and ‘false’ specified without quotes so that they know to
treat them differently from the plain words “true” and “false”._

_Try changing the line to read like this:_
```
paid_account: true
```

---
```
window.intercomSettings = {
    eamil: 'bob@example.com',
    name: 'Bob Sagget',
    app_id: 'abc1234',
    created_at: 1234567890,
    profile_completed_at: 1234567890,
}
```
_It looks like the ‘email’ setting may have been accidentally misspelled: it reads
‘eamil’ instead of ‘email’. Try switching it to read ‘email’ and see if that fixes
the issue._

---
```
window.intercomSettings = {
    email: 'bob@example.com',
    name: 'Bob Sagget',
    app_id: 'abc1234',
    created_at: 1234567890,
    number_of_photos: "3",
    profile_completed_at: 1234567890,
    paid_account: true
}
```
_It looks like the ‘number_of_photos’ setting has a value with quotes around it
when it shouldn’t (“3”). Computers treat numbers differently depending on whether
 they have quotes around them or not; in this case, it looks like you probably
 want the number without quotes. Try having the line read like below and see if
 that fixes the issue:_
```
number_of_photos: 3,
```

---
```
window.intercomSettings = {
    app_id: 'abc1234'
}
```
_It looks like the snippet is missing a number of settings that are necessary for
its proper use; at a minimum, the settings snippet needs to specify the app_id
(which you’ve already done), an ‘email’, a ‘name’, and a ‘created_at’ (in the Unix
timestamp format). Below is an example of the minimum fields being filled out:_
```
window.intercomSettings = {
    email: 'bob@example.com',
    name: 'Bob Sagget',
    app_id: 'abc1234',
    created_at: 1234567890
}
```
_See if filling out those other fields fixes the issue; please let me know if it
doesn’t!_

### Programming
**Write some code in either Ruby or JavaScript that prints out, in reverse order,
every multiple of 3 between 1 and 200.**
```
current_value_to_print = 198
while current_value_to_print >= 3 do
    puts current_value_to_print
    current_value_to_print -= 3
end
```
---

**Write some code in either Ruby or JavaScript that will flatten an array of
 arbitrarily nested arrays of integers into a flat array of integers. e.g.
 [[1,2,[3]],4] -> [1,2,3,4]. Please don't use any built-in flatten functions
 in either language.**
```
def flatten_array (array_to_flatten)
    array_to_return = []
    array_to_flatten.each { |element|
        if element.kind_of?(Array) then
            array_to_return += flatten_array(element)
        else
            array_to_return += [element]
        end
    }
    return array_to_return
end
```
---

**Write some code in either Ruby or JavaScript that will determine if a given
number is prime.**

Using existing libraries:
```
require 'prime'
Prime.prime?(number_to_check)

Coding a simple solution from scratch:
def is_prime (number_to_check)
    if number_to_check % 2 == 0 then
        return FALSE
    end

    largest_potential_factor_we_need_to_check = Math.sqrt(number_to_check)
    current_potential_factor = 3
    while current_potential_factor <= largest_potential_factor_we_need_to_check do
        if number_to_check % current_potential_factor == 0 then
            return FALSE
        end
        current_potential_factor += 2
    end
    return TRUE
end
```

### Code comprehension
**Please describe, in plain English, what this method does.**
```
def optimize(hsh)
    hsh.reduce({}) do |new_hsh, (k,v)|
        new_hsh[k.to_sym] = v.kind_of?(Hash) ? optimize(v) : v
        new_hsh
    end
end
```
- From the perspective of the caller, it doesn’t seem to do anything. As far as I 
can tell, it takes a hash object as input and returns the same hash object as output.
- Within the function, it just seems to recursively step through any hash objects 
in the original hash object. Presumably you could add more code to take some kind 
of action as you’re stepping through all of the hash objects.

**How would you describe the pros and cons of both strongly-typed and weakly-typed 
languages to someone just starting to learn programming?**

One of the major sources of problems when programming is keeping track of what 
type of data a given variable represents. Strongly-typed languages require that 
when you write a function, you must specify the type of data that function will 
accept as input and what type of data it will output. This strictness makes it 
easier to avoid errors in the future caused by confusion over the type of data 
that a function takes as input or returns as output. On the other hand, weak typing
 makes it possible to make the functions more flexible: you can accept multiple 
 types of input and return multiple types of output.


**What does a good RESTful design look like to you?**

I haven’t done as much web programming as offline programming, but from the projects
 I have worked on and from the studying I’ve done, I’ve picked up a few guidelines:
 
- It has versioning (eg ‘www.website.com/api/v1/users’) (this has caused me some headaches).
- It paginates results when it makes sense to do so.
- It makes use of the HTTP status codes.
- It has plural endpoints (eg ‘/users/’ instead of ‘/user/’).
- It has good documentation (this has been a pain point on some projects).
- It returns JSON.
- It’s stateless.
- It returns useful error messages (going beyond the HTTP status codes).