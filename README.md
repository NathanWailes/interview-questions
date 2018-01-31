## Misc

- I am using a `main` branch but not a `master` branch. According to [this Stack Overflow answer](https://stackoverflow.com/a/15987482/4115031)
(and as you can verify  yourself by visiting [GitHub's robot.txt page](https://github.com/robots.txt)), if you
don't have a `master` branch,  Google will not index your GitHub repo, and so there's no way that someone
searching for the answer to a particular company's test question would be able to find my solution by searching
on Google.


## Steps to take when adding a new interview

- When naming the company folder, use only lowercase.
  - Thought: Why? Because it's easier at the command line? Is that relevant here?
- Add the question / prompt.
  - If the prompt is in PDF form, convert it to Markdown.
    - Thought: is it really necessary to do that? I think the reason people
    say you shouldn't commit binary files is because *when you update
    them* they take up a lot of space. But if you know you'll never be
    updating them, it should be OK to commit them, right? Or would even
    just moving the file take up more space?