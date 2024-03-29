# Razor Barber

## Overview

Razor Barber is a website selling top of the range hair products as well as allowing users to book haircuts. Users are able to browse the selection of hair cproducts and purchase them. Users will be able to look at previous orders and update their delivery details if they register an account. Admin users can add, edit and delete products. Non-admin users are also able to add, edit and delete replies to the blog posts they have made.

[Link to deployed site](https://barber-django-ml.herokuapp.com/)

### Making Payments

The website uses [Stripe](https://stripe.com/gb) to process payments. The Stripe account associated with this project is in 'test' mode, so to make payments on the site, one of Stripe's test cards will need to be used, 2 of which are as follows.

4242 4242 4242 4242 - to simulate standard payments

4000 0025 0000 3155 - to simulate 3D Secure authentication payments

Then use any future date and any 3-digit CVC code.

## Business Model

The business model for this e-commerce website is a 'B2C – Business to customer' model. None of the products sold are made or developed by Razor Barber, so everything is bought at wholesale prices to sell to customers at a profit. With this in mind, the site has been designed to make everything as easy as possible for customers visiting the site. Everything is designed to be easily found and understood and to produce a positive response from the site's users.

### Marketing Strategy

The marketing strategy for this site uses a combination of Email Marketing, Social Media Marketing and Search Engine Optimisation.

Users can subscribe to the site's mailing list by submitting their email addresses via a simple MailChimp form in the site's footer.

#### Search Engine Optimisation

To optimise how search engines will view this site, a number of short-tail and long-tail keywords are needed. After some research using Google's 'People always ask' and 'Related Searches' features, a list of 10-20 short-tail and long-tail keywords were discovered and have been placed in the keywords meta tag within the head of the main HTML document.

### Facebook Business Page

You can find a link to the business page [here.](https://www.facebook.com/Razor-Barber-108482478691688). There is also a link to tit in the footer of the site.

![Facebook](media/readme_screenshots/facebook.jpg)


## UX

### User Stories

* New users

    * As a site user I can browse through products so that I can decide what I may be interested in buying
    * As a site user I can look at product details so that I can decide whether I would like to buy it
    * As a site user I can search for products so that I have another way of looking for items
    * As a site user I can sort products on criteria such as price so that I have a method of ordering the products as I prefer
    * As a site user I can add products I want to purchase to a basket so that I may then decide whether to purchase them or not
    * As a site user I can view the contents of my shopping basket so that I can make any adjustments to it
    * As a site user I can perform a checkout on my shopping basket so that I can create an order
    * As a site user I can register an account so that I can make use of features reserved for registered users
    * As a site user I can log in so that I can use features reserved for registered users
    * As a site user I can log out so that my account remains secure if I were to visit the site from a shared PC
    * As a site user I can view a profile for my user account so that I can see my order history and also make any adjustments to the details kept on record for me
    * As a site user I can submit a message to admin so that any feedback or issues can be raised to them
    * As a site user I can reply to blog posts so that I can express an opinion about them or add a comment 
    * As a site user I can edit my replies to the blog posts so that I may update them if needed
    * As a site user I can delete any of my replies to the blog posts so that I can remove them if I feel they’re no longer needed
    * As a site admin I can manage products so that I may add, update or delete them as needed
    * As a site admin I can manage user accounts so that any required changes to them can be made
    * As a site admin I can view created orders so that they may be fulfilled, or amended if needs be
    * As a site admin I can view messages submitted via the contact us section so that I may act upon them
    * As a site admin I can manage the content on the blog page so that it can be amended if needed

* Returning users

    * As a returning site user I can check to see if any new products have been added so that I can decide if I want to buy any
    * As a returning site user I can view my user profile (if I registered an account) so that I can edit my details and also view previous orders
    * As a returning site user I can see whether any new blog posts and associated replies have been added
    * As a returning site admin I can see whether any new messages have been submitted so that I can action them accordingly
    * As a returning site admin I can look at whether any new orders have been placed so that I can fulfill or amend them as required
    * As a returning site admin I can update the blog page content so that any required changes to it are reflected

User stories have also been recorded using GitHub issues and have been placed in the milsetone section under a 'Product Backlog' title. They can be seen [here.](https://github.com/mlenahan/razor-barber/milestone/1)

I also used an Iteration Board to help with the planning of this project. That can be seen [here.](https://github.com/users/mlenahan/projects/4)


### Design

* Imagery

    * This website features a simple background image showing some texture on the homepage. The other images present are those for the products. I also make use of Font Awesome icons.

* Typography

    * The font used in my application is Lato. 

* Colour scheme

    * I have used a monochromatic colour scheme to align with my preference for clean, minimalistic approach to styling
 
 ### Schema

Details of the database scheme and it's relationships can be viewed in the image above.

![Image of schema overview](media/db_schema.png)<br>

The relationships are as follows:

* Order has a one-to-many relationship with OrderLineItem
* Product has a one-to-many relationship with OrderLineItem
* UserProfile  has a one-to-many relationship with Order
* UserProfile has a one-to-one relationship with django's default User model
* BlogPost has a one-to-many relationship with the Reply
* Reply has a one-to-many relationship with the User
* I have included the non functional Reservation model for potential future use

### Wireframes

Wireframes were created on Balsamiq.

* [Mobile](media/wireframes/mobile-wireframe.pdf)
* [Tablet](media/wireframes/tablet-wireframe.pdf)
* [Desktop](media/wireframes/desktop-wireframe.pdf)

Some final design choices aren't reflected in wireframes.

## Features

### Existing Features

Details of all site features are listed below.

Header contains a logo, nav items, a search bar, account icon and basket icon.

![Image of header](media/readme_screenshots/header.png)<br>

Homepage:

![Image of homepage](media/readme_screenshots/homepage.jpg)<br>

The footer contains an about us, link to socials, and a sign up to newletter.

![Image of footer](media/readme_screenshots/footer.png)<br>

Log in.

![Image of login page](media/readme_screenshots/signin.png)<br>

Logout.

![Image of logout page](media/readme_screenshots/signout.png)<br>

Account registration.

![Image of sign up page](media/readme_screenshots/signup.png)<br>

Product overview.

![Image of products page](media/readme_screenshots/products.png)<br>

Product detail

![Image of product detail page](media/readme_screenshots/product_detail.png)<br>

Added to basket.

![Image of notification](media/readme_screenshots/added_to_bag.png)<br>

Basket view.

![Image of basket page](media/readme_screenshots/shopping_bag.png)<br>

Checkout.

![Image of checkout page 1](media/readme_screenshots/checkout.png)<br>

Checkout success

![Image of checkout complete page](media/readme_screenshots/order_success.png)<br>

Profile view.

![Image of profile page](media/readme_screenshots/profile.png)<br>

Order details.

![Image of order history page](media/readme_screenshots/order_history.png)<br>

Blog.

![Image of blog overview page](media/readme_screenshots/blog.png)<br>

Blog post detail.

![Image of blog detail page](media/readme_screenshots/blog_post_detail.png)<br>

Blog commenting. Comments can be edited and deleted.

![Image of blog detail page](media/readme_screenshots/blog_comment.png)<br>

Contact Us

![Image of contact us page](media/readme_screenshots/contact_us.png)<br>

Product management for admins.

![Image of add product page](media/readme_screenshots/product_management.png)<br>


Admin users can also edit and delete products:

![Image of edit product page](media/readme_screenshots/product_edit_delete.png)<br>

## Features left to implemement

I attempted to add a booking system to this site but I couldn't find a solution to create a reservation. i have still included some of the booking flow in the site but have added an error page which lets the user know the system is down.

Book now button on homepage.

![Image of edit product page](media/readme_screenshots/book_now.png)<br>

Service selection.

![Image of edit product page](media/readme_screenshots/services.png)<br>

Barber selection.

![Image of edit product page](media/readme_screenshots/barbers.png)<br>

Custom error page.

![Image of edit product page](media/readme_screenshots/error_page.png)<br>

# Technologies

## Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs Used

1. [Google Fonts](https://fonts.google.com/)
2. [Font Awesome](https://fontawesome.com/)
3. [Git](https://git-scm.com/)
4. [GitHub](https://github.com/)
5. [Gitpod](https://www.gitpod.io/)
6. [Chrome devtools](https://developer.chrome.com/docs/devtools/)
7. [Heroku](https://dashboard.heroku.com/apps)
8. [Postgres](https://www.postgresql.org/)
9. [Django](https://www.djangoproject.com/)
10. [Autopep8](https://pypi.org/project/autopep8/)
11. [Django Summernote](https://github.com/summernote/django-summernote)
12. [Stripe](https://stripe.com/)
13. [Mailchimp](https://mailchimp.com/)
14. [Django Summernote](https://github.com/summernote/django-summernote)
15. [AWS](https://aws.amazon.com/)

# Testing

Testing and results can be found [here](TESTING.md)

## Deployment

### Amazon Web Services (AWS)

An [Amazon Web Services](https://aws.amazon.com/) S3 bucket has been used to host all static and media files for this website. A user, user group and bucket were created with appropriate names and with public access set to enabled. The ACCESS and SECRET keys provided were then used as environment variables within the project.

### Stripe

[Stripe](https://stripe.com/gb) was used for processing payments on the site, including the use of Stripe webhooks. After setting up an account and an appropriate webhook endpoint, the PUBLIC, SECRET and webhook SECRET keys provided were then used as environment variables within the project.

### Initial deployment

- Gitpod
    - Create new repository from CI template
    - Install Django and required dependencies into Gitpod workspace
    - Create new Django project
    - Create procfile as required
    - Run "pip3 freeze --local > requirements.txt" to update requirements file
- Heroku
    - Log into Heroku 
    - Create new app 
    - Add a PostgreSQL "hobby" database as resource
    - Configure "DISABLE_COLLECTSTATIC = 1" in Config Vars
    - Configure "SECRET_KEY" variable in Config Vars
- Gitpod
    - Create env.py file and add database path from Heroku
    - Add secret key to env.py
    - Configure database path and secret key in settings.py to be read from environment variables
    - Perform commit and push to GitHub
- Heroku
    - Perform deployment on portal, await completion 

### Final deployment

- Gitpod
    - Ensure all required files up-to-date and that application is working
    - Run "pip3 freeze > requirements.txt" to update requirements file
    - Ensure "DEBUG = False" set in settings.py
    - Perform commit and push to GitHub
- Heroku
    - Under settings, go to Config Vars
    - Remove the value "DISABLE_COLLECTSTATIC = 1" from Config Vars
    - Add new Config Vars entries for the following with appropriate values:
        - AWS_ACCESS_KEY_ID
        - AWS_SECRET_ACCESS_KEY
        - EMAIL_HOST_PASS
        - EMAIL_HOST_USER
        - STRIPE_PUBLIC_KEY
        - STRIPE_SECRET_KEY
        - STRIPE_WH_SECRET
        - USE_AWS 
    - Browse to Deploy and run deployment
    - Wait for confirmation that app has deployed

## Fork

- To fork this project, go to my [repository](https://github.com/mlenahan/razor-barber).

- Click the fork option displayed on the top right side of the page.

- The fork should now be in your repositories.

## Clone

- If someone wishes to clone the [repository](https://github.com/mlenahan/razor-barber), they can do so by using this command in their terminal/command line `git clone https://github.com/mlenahan/razor-barber.git`

- To install requirements, the user can use this command in their terminal/command line `pip3 install -r requirements.txt`

## Media

- All media for product images belong to [Ruger Barber](https://www.rugerbarber.com/)
- Homepage image and images used in Blog are taken from a Google Image Search

# Credits

- Code Institute for walk through project 'Boutique Ado' and their GitPod template.

- StackOverflow for helping me troubleshoot issues I encountered and providing code snippets I could modify to use in my project.

- A lot of the blog logic was taken from a pervious project I have worked on [Johnpooch.dog.](https://github.com/mlenahan/Johnpooch.dog)