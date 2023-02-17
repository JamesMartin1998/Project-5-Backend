# Let's Pick API

Let's Vote is a voting app which allows users to make posts about two things and have people vote on which is best. The website aims to be a fun, social place to for people to light-heartedly share their interests with other people. Users are able to be creative and share their interests with other users in numerous ways. For example, users can interact through posting content for other uses to see, voting on other users' posts and also commenting on posts. 

The Let's Pick API is built using the Django Rest Framework. Its purpose is to provide data to the front end website and control authenticaion.

The project was built to store 'Posts', 'Votes', 'Comments', 'Favourites' and 'Profiles' data. Each resource was created as a Django app.

- Models were used define the core data fields for each resource.
- Serializers were used to define additional fields for each resource and convert between Python and JSON data.
- URLs were used to create 2 URLs for each resource - a list URL (where all instances of a resource can be accessed) and a details URL (where a specific instance could be accessed).
- Generic views were used to create 2 views for each resource. Firstly, a list view with a collection of all data instances for the specific resource. This allowed instances to be viewed and created. Secondly, a detail view with data for an individual instance for a specific resource. This allowed for additional CRUD functionality, such as updating and deleting an instance.

Examples of authentication include:
- Using permission classes to limit access to functionality in specific views.
    - IsAuthenticatedOrReadOnly restricts logged out users to view data, not manipulate it.
    - IsAuthorOrReadOnly allows only the author of a resource (post/comment) to manipulate the resource, other users can view the data.
    - Is OwnerOrReadOnly allows only the owner of a resource (vote/favourite/profile) to manipulate the resource, other users can view the data.

## Project Links

- [Deployed Front End Site](https://lets-pick-app.herokuapp.com/)
- [Repository for Front End Site](https://github.com/JamesMartin1998/lets-pick)
- [Deployed API Site](https://lets-pick.herokuapp.com/)
- [Repository for API Site](https://github.com/JamesMartin1998/Project-5-Backend)

## User Stories

The API was built to allow the user stories to be achieved on the front end website.

### Epic 1: Navigation

1. As a **user** I can **view a navbar on each page** so that **I can use the links to change my current page**.
2. As a **user** I can **navigate between pages quickly** so that **I am not delayed by unnecessary page refreshes**.
3. As a **user**, I can **see the log in and sign up links when logged out, compared to the log out link when logged in**, so that **I can access the appropriate actions accordingly**.

### Epic 2: Authentication

1. As a **user**, I can **sign up for an account** so that **I can have access to more functionality on the website**.
2. As a **user**, I can **sign in to my account** so that **I can access to additional functionality**.
3. As a **user**, I can **see my logged in status** so that **I know if am currently logged in or not**.
4. As a **user**, I can **see users’ avatars** so that **I can identify specify profiles easily**.

### Epic 3: Posts

1. As a **logged in user**, I can **create posts** so that **I can create content on the website**.
2. As a **user**, I can **click on a post to view it individually** so that **I can view more details such as its comments**.
3. : As a **post author**, I can **edit my post** so that **I can correct the post’s details**.
4. As a **post author** , I can **delete my own post** so that **it is removed from my profile**.
5. As a **user**, I can **view the most recent posts at the top of a continuous feed** so that **I see new content first**.
6. As a **user**, I can **search for specific posts by post title and author** so that **I can find posts that I am interested in**.
7. As a **user**, I can **filter posts by selecting a category** so that **I can see posts that I am interested in**.
8. As a **user**, I can **view a feed on posts by scrolling down continuously to load more posts** so that **I don’t have to reload new pages with more posts**.
9. As a **user**, I can **view a post’s page** so that **I can read comments about the post**.


### Epic 4: Votes

1. As a **logged in user**, I can **vote on a post** so that **I can share my preference**.
2. As a **logged in user**, I can **view posts that I have voted on previously** so that **I can revisit the results of the posts**.
3. As a **logged in user**, I can **remove my vote on a post** so that **I can vote again on the post to change my vote option**.


### Epic 5: Comments

1. As a **logged in user**, I can **create a comment on a post** so that **I can share my opinion**.
2. As a **user**, I can **see the date of a comment** so that **I know how old a comment is**.
3. As a **user**, I can **view comments on a post** so that **I can read other users’ opinions**.
4. As a **comment author**, I can **edit my comment** so that **I can correct its detail**.
5. As a **comment author**, I can **delete my comment** so that **I can remove it from the post**.

### Epic 6: Favourites

1. As a **logged in user**, I can **favourite a post** so that **I can save my favourite posts**.
2. As a **loggeed in user**, I can **view my favourite posts in a feed** so that **I can revisit my favourite posts**.
3. As a **logged in user**, I can **remove a favourite on a post** so that **it no longer appears in my favourites feed**.

### Epic 7: Profile

1. As a **user**, I can **view users’ profiles** so that **I can learn more about them**.
2. As a **user**, I can **view a user’s statistics** so that **I can see how many posts, votes received and votes made they have**.
3. As a **user**, I can **see all of a user’s posts on their profile page** so that **I can view more content by users I like**.
4. As a **profile owner**, **I can edit my profile** so that **I can change details such as my profile image and bio**.
5. As a **user**, I can **edit my username and password** so that **I can keep my account secure**.

## Models and Database

### Initial Models

![Image showing the initial models](/images/database-models.png)

### Database Models

- Serializer used to created more fields.

![Image showing the database models](/images/database-models-total.png)

## Testing 

### Manual Testing

Manual testing was carried out throughout the developement of the project using the Django Rest Framework 'Browsable API'. By creating multiple superusers, I was able to check all CRUD functionality at each valid endpoint.

### Root

| Test Case | User Status | CRUD operation | Test Description | Test Result |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 001 | Any | Read | All users can retrieve data. | Pass |

### /posts/

| Test Case | User Status | CRUD operation | Test Description | Test Result |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 002 | Any | Read | Logged out can retrieve posts data. | Pass |
| 003 | Logged in | Create | Logged in users are able to create posts. | Pass |
| 004 | Logged out | Create | Logged out users are unable to create posts. | Pass |

### /posts/\<id>/

| Test Case | User Status | CRUD operation | Test Description | Test Result |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 005 | Any | Read | All users can retrieve data for a single post. | Pass |
| 006 | Not post author | Update | Users that are not the author of a post are unable to update it. | Pass |
| 007 | Post author | Update | User that is the post author can update the post. | Pass |
| 008 | Not post author | Delete | Users that are not the author of a post are unable to delete it. | Pass |
| 009 | Post author | Delete | User that is the post author can delete the post. | Pass |

### /profiles/

| Test Case | User Status | CRUD operation | Test Description | Test Result |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 010 | Any | Read | All users can retrieve data for profiles. | Pass |
(No create functionality as profiles are created automatically upon user instance creation)

### /profiles/\<id>/
| Test Case | User Status | CRUD operation | Test Description | Test Result |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 011 | Any | Read | All users can retrieve data for a single profile. | Pass |
| 012 | Not Profile owner | Update | Users that are not the owner of a profile are unable to update it. | Pass |
| 013 | Profile owner | Update | Users that are the owner of a profile are able to update it. | Pass |
(No delete functionality, users are unable to delete their profiles)

### /votes/
| Test Case | User Status | CRUD operation | Test Description | Test Result |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 014 | Any | Read | All users can retrieve data for votes. | Pass |
| 015 | Logged in | Create | Logged in users can create votes. | Pass |
| 015 | Logged out | Create | Logged in users cannot create votes. | Pass |

### /votes/\<id>/

|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
