# exam-calendar
This project was created with [DjangoRestFramework](https://www.django-rest-framework.org/).
It is deployed [here](https://www.django-rest-framework.org/)

### What it is all about?

This app is created to observe the situation with university exams. Users can add professors from universtities listed. 
Then they can provide them with rate (0-100). 
Each professor has its own average rate which is used to count possibility of passing his exam.

Apart from that users can also add exams to their schedule, where they can add literature lists or any other useful sources.
If date, time and professor are the same, it will automatically merge into one another. 
Users can also add main points, which are keys for succesfully passing an exam.

The main idea of that app that users can vote for and against everything. For example if professor's name isn't true they can downvote this instance. 
Another example comes with useful sources: if they are really useful users will upvote them. 
If an instance has too many downvotes it is being deleted and never showed again. User will get special rate...

### Routes

Although, project also has a documentation inside itself, here are the main endpoints:

1. `api/universities [GET]` - get all universities supported
2. `api/professors/ [POST]` - create new professor
3. `api/professors/<int> [GET/POST/PUT/PATCH/DELETE]` - CRUD with professor
4. `api/professors/<int>/rate [POST]` - rate professot with `id=<int>`
5. `api/professors/<slug> [GET]` - get all professors from current university
