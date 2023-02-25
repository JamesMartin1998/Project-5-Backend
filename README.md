# Let's Pick API

Let's Vote is a voting app which allows users to make posts about two things and have people vote on which is best. The website aims to be a fun, social place for people to light-heartedly share their interests with other people. Users are able to be creative and share their interests with other users in numerous ways. For example, users can interact through posting content for other uses to see, voting on other users' posts and also commenting on posts. 

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

1. As a **user**, I can **view a navbar on each page** so that **I can use the links to change my current page**.
2. As a **user**, I can **navigate between pages quickly** so that **I am not delayed by unnecessary page refreshes**.
3. As a **user**, I can **see the log in and sign up links when logged out, compared to the log out link when logged in**, so that **I can access the appropriate actions accordingly**.

### Epic 2: Authentication

1. As a **user**, I can **sign up for an account** so that **I can have access to more functionality on the website**.
2. As a **user**, I can **sign in to my account** so that **I can access to additional functionality**.
3. As a **user**, I can **see my logged in status** so that **I know if am currently logged in or not**.
4. As a **user**, I can **see users’ avatars** so that **I can identify specific profiles easily**.

### Epic 3: Posts

1. As a **logged in user**, I can **create posts** so that **I can create content on the website**.
2. As a **user**, I can **click on a post to view it individually** so that **I can view more details such as its comments**.
3. As a **post author**, I can **edit my post** so that **I can correct the post’s details**.
4. As a **post author** , I can **delete my own post** so that **it is removed from my profile**.
5. As a **user**, I can **view the most recent posts at the top of a continuous feed** so that **I see new content first**.
6. As a **user**, I can **search for specific posts by post title and author** so that **I can find posts that I am interested in**.
7. As a **user**, I can **filter posts by selecting a category** so that **I can see posts that I am interested in**.
8. As a **user**, I can **view a feed of posts by scrolling down continuously to load more posts** so that **I don’t have to reload new pages with more posts**.
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

## Validation testing

All python files (excluding settings.py, env.py and migrations) were passed into the "CI Python Linter" to check that the code conforms to PEP8 guidelines. No validation errors were found.

## Manual Testing

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
| 016 | Logged out | Create | Logged in users cannot create votes. | Pass |

### /votes/\<id>/
| Test Case | User Status | CRUD operation | Test Description | Test Result |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 017 | Any | Read | All users can retrieve data for a single vote. | Pass |
| 018 | Not Vote owner | Delete | Users that are not the owner of a vote are unable to delete it. | Pass |
| 019 | Vote owner | Delete | Users that are the owner of a vote are able to delete it. | Pass |

(No update functionality, users cannot edit their vote and instead have to delete their vote and vote again with other option)

### /comments/

| Test Case | User Status | CRUD operation | Test Description | Test Result |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 020 | Any | Read | All users can retrieve data for comments. | Pass |
| 021 | Logged in | Create | Logged in users can create comments. | Pass |
| 022 | Logged out | Create | Logged out users cannot create comments. | Pass |

### /comments/\<id>/

| Test Case | User Status | CRUD operation | Test Description | Test Result |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 023 | Any | Read | All users can retrieve data for a single comment. | Pass |
| 024 | Not comment author | Update | Users that are not the author of a comment cannot update it. | Pass |
| 025 | Comment author | Update | Users that are the author of a comment can update it. | Pass |
| 026 | Not comment author | Delete | Users that are not the author of a comment cannot delete it. | Pass |
| 027 | Comment author | Delete | Users that are the author of a comment can delete it. | Pass |

### /favourites/

| Test Case | User Status | CRUD operation | Test Description | Test Result |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 028 | Any | Read | All users can retrieve data for favourites. | Pass |
| 029 | Logged in | Create | Logged in users can create favourites. | Pass |
| 030 | Logged out | Create | Logged out users cannot create favourites. | Pass |

### /favourites/\<id>/

| Test Case | User Status | CRUD operation | Test Description | Test Result |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 031 | Any | Read | All users can retrieve data for a single favourite. | Pass |
| 032 | Not favourite owner | Delete | Users that are not the owner of a favourite cannot delete it. | Pass |
| 032 | Favourite owner | Delete | Users that are the owner of a favourite can delete it. | Pass |

(No update functionality, users cannot edit their favourite)

## Automated Testing

Automated tests were also constructed to test the API. Results for each resource are linked below:
- [Posts Automated Tests](https://github.com/JamesMartin1998/Project-5-Backend/blob/main/posts/tests.py)
- [Profiles Automated Tests](https://github.com/JamesMartin1998/Project-5-Backend/blob/main/profiles/tests.py)
- [Votes Automated Tests](https://github.com/JamesMartin1998/Project-5-Backend/blob/main/votes/tests.py)
- [Comments Automated Tests](https://github.com/JamesMartin1998/Project-5-Backend/blob/main/comments/tests.py)
- [Favourites Automated Tests](https://github.com/JamesMartin1998/Project-5-Backend/blob/main/favourites/tests.py)

## Technologies Used

### Main Languages Used

- Python

### Dependencies and Programs Used
- Django
- djangorestframework
- Cloudinary
- django-clouinary-storage
- dj-rest-auth
- django-allauth 
- django-cors-headers 
- django-filters
- djangorestframework-simplejwt
- gunicorn
- Pillow
- psycopg2 
- oauthlib
- PyJWT
- python3-openid
- pytz
- requests-oauthlib
- sqlparse
- PostgreSQL
- ElephantSQL 
- Gitpod
- GitHub
- Heroku

## Deployment

### Run Locally

- Manually Downloading the Repository:

    - Opening the project repository at: https://github.com/JamesMartin1998/Project-5-Backend.
    - Opening the dropdown on the 'code' button.
    - Downloading the zip file.
    - Extracting the files from the zip file into a new folder on your computer.
    - Opening the folder in an IDE of your choice.
    - Type "pip install requirements.txt" in the terminal and press "Enter"
    - creating an env.py file, importing os and creating the following variables:
        - os.environ['DATABASE_URL'] = *enter a database url*
        - os.environ['SECRET_KEY'] = *enter any secret key*
        - os.environ['CLOUDINARY_URL'] = *enter your cloudinary url*
    - Type "python manage.py makemigrations" and press "Enter".
    - Type "python manage.py migrate" and press "Enter".

- Cloning the Repository:

    - Opening the project repository at: https://github.com/JamesMartin1998/Project-5-Backend.
    - Opening the dropdown on the 'code' button.
    - Copying the link under the HTTPS heading (https://github.com/JamesMartin1998/Project-5-Backend.git).
    - Opening an IDE of your choice (must have Git support or relevant git extension).
    - Open the terminal and create a directory to store the repository.
    - Type "git clone https://github.com/JamesMartin1998/Project-5-Backend.git" and press enter in the terminal.
    - Type "pip install requirements.txt" and press "Enter".
    - creating an env.py file, importing os and creating the following variables:
        - os.environ['DATABASE_URL'] = *enter a database url*
        - os.environ['SECRET_KEY'] = *enter any secret key*
        - os.environ['CLOUDINARY_URL'] = *enter your cloudinary url*
    - Type "python manage.py makemigrations" and press "Enter".
    - Type "python manage.py migrate" and press "Enter".

### Deploying to Heroku
During the development of the project, version control was used by committing and pushing the code to GitHub. The GitHub repository can be found here: https://github.com/JamesMartin1998/Project-5-Backend

This project was deployed to Heroku by:
- Within Gitpod, adding the dependencies to the requirements file by typing 'pip3 freeze > requirements.txt' in the terminal.
- Committing and pushing the code to GitHub.
- On the Heroku website, clicking 'Create New App'.
- Setting the name and region and pressing 'Create App'.
- Clicking the 'Settings' tab.
- Setting config vars for the keys: CLOUDINARY_URL, DATABASE_URL, ALLOWED_HOST, CLIENT_ORIGIN, CLIENT_ORIGIN_DEV and SECRET_KEY.
- Clicking 'Add Buildpack', 'Python', 'Save Changes'.
- Clicking the 'Deploy' tab.
- Clicking 'Connect to GitHub', search for repository, click 'Connect'.
- Enabling Manual Deploy. Check for successful message.
- Enabling Automatic Deploys.
- The live site can be found here: https://lets-pick.herokuapp.com/

## Credits

- Code Institute's Django Rest Framework Project was used to lay the foundations of this project and was adapted on to create a unique project. (https://github.com/Code-Institute-Solutions/drf-api/tree/ed54af9450e64d71bc4ecf16af0c35d00829a106)
- Cloudinary was used to store images.
- Default Profile image and Post image used from Code Institute's Django Rest Framework project.
- Django Rest Framework Documentation was used to code with:
    - Django Filter Backend (https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend)
    - Filterting on annotations (https://docs.djangoproject.com/en/4.1/topics/db/aggregation/#filtering-on-annotations)
- PostgreSQL database provided by ElephantSQL.com
- Python code was validated using the "CI Python Linter" (https://pep8ci.herokuapp.com/)
- Thanks to my mentor, Spencer, for his guidance throughout the project.
