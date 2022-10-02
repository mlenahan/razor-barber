# Testing

## User Stories 

* As a site user I can browse through products so that I can decide what I may be interested in buying
![image](media/readme_screenshots/products.png)

* As a site user I can look at product details so that I can decide whether I would like to buy it
![image](media/readme_screenshots/product_detail.png)

* As a site user I can search for products so that I have another way of looking for items
![image](media/readme_screenshots/header.png)

* As a site user I can sort products on criteria such as price so that I have a method of ordering the products as I prefer
![image](media/readme_screenshots/sort_price.png)

* As a site user I can add products I want to purchase to a basket so that I may then decide whether to purchase them or not
![image](media/readme_screenshots/added_to_bag.png)

* As a site user I can view the contents of my shopping basket so that I can make any adjustments to it
![image](media/readme_screenshots/shopping_bag.png)

* As a site user I can perform a checkout on my shopping basket so that I can create an order
![image](media/readme_screenshots/checkout.png)

* As a site user I can register an account so that I can make use of features reserved for registered users
![image](media/readme_screenshots/signup.png)

* As a site user I can log in so that I can use features reserved for registered users
![image](media/readme_screenshots/signin.png)

* As a site user I can log out so that my account remains secure if I were to visit the site from a shared PC
![image](media/readme_screenshots/signout.png)

* As a site user I can view a profile for my user account so that I can see my order history and also make any adjustments to the details kept on record for me
![image](media/readme_screenshots/profile.png)

* As a site user I can submit a message to admin so that any feedback or issues can be raised to them
![image](media/readme_screenshots/contact_us.png)

* As a site user I can reply to blog posts so that I can express an opinion about them or add a comment
* As a site user I can edit my replies to the blog posts so that I may update them if needed
* As a site user I can delete any of my replies to the blog posts so that I can remove them if I feel they’re no longer needed
![image](media/readme_screenshots/blog_comment.png)

* As a site admin I can manage products so that I may add, update or delete them as needed
![image](media/readme_screenshots/admin_edit_products.png)

* As a site admin I can manage user accounts so that any required changes to them can be made
![image](media/readme_screenshots/user_accounts.png)

* As a site admin I can view created orders so that they may be fulfilled, or amended if needs be
![image](media/readme_screenshots/admin_orders.png)

* As a site admin I can view messages submitted via the contact us section so that I may act upon them
![image](media/readme_screenshots/admin_view_messages.png)

* As a site admin I can manage the content on the blog page so that it can be amended if needed
![image](media/readme_screenshots/admin_blog.png)

Testing for returning users is covered in the above user story tests.

## Responsiveness

My site is responsive accross all devices as far as I am aware.

- ### Desktop

![image](media/testing_screenshots/desktop_responsive.jpg)

- ### Tablet

![image](media/testing_screenshots/ipad_responsive.png)

- ### Mobile

![image](media/testing_screenshots/iphone_responsive.png)

## Bugs

There are no know bugs on this site.

## Validation

### Python

All files have been checked for flake8 standards. `autopep8 --in-place --aggressive --aggressive <file name>` has been run on all python files in order to ensure the files comply to flake8 rules. Any errors left are left because changing them would break the code.

### HTML

Some pages contain the warning "Self-closing tag syntax in text/html documents is widely discouraged; it’s unnecessary and interacts badly with other HTML features (e.g., unquoted attribute values). If you’re using a tool that injects self-closing tag syntax into all void elements, without any option to prevent it from doing so, then consider switching to a different tool.". The warning is saying that `<input>` tags shouldn't have a closing tag. I have searched my codebase for the lines of code they refer to but these lines aren't present so I am unsure on how to get rid of this warning.

* Home <br>
![image](media/testing_screenshots/home_html_val.png)

* Products <br>
![image](media/testing_screenshots/products_html_val.png)

* Product Detail <br>
![image](media/testing_screenshots/product_detail_html_val.png)

* Bag <br>
![image](media/testing_screenshots/bag_html_val.png)

* Checkout <br>
![image](media/testing_screenshots/checkout_html_val.png)

* Checkout Success <br>
![image](media/testing_screenshots/checkout_success_html_val.png)

* Blog <br>
![image](media/testing_screenshots/blog_html_val.png)

* Blog Detail <br>
![image](media/testing_screenshots/blog_detail_html_val.png)

* Blog Comment Edit <br>
![image](media/testing_screenshots/blog_edit_html_val.png)

* Blog Comment Delete <br>
![image](media/testing_screenshots/blog_comment_delete_html_val.png)

* Contact Us <br>
![image](media/testing_screenshots/contact_html_val.png)

* Product Add <br>
![image](media/testing_screenshots/product_add_html_val.png)

* Product Edit <br>
![image](media/testing_screenshots/product_edit_html_val.png)

### CSS

* base.css
![image](media/testing_screenshots/base_css_val.png)

* checkout.css
![image](media/testing_screenshots/checkout_css_val.png)

* profile.css
![image](media/testing_screenshots/profile_css_val.png)

### JavaScript

* Quantity input script <br>
![image](media/testing_screenshots/quantity_input_js_val.png)

* Sort selection script <br>
![image](media/testing_screenshots/)

* stripe-elements.js <br>
![image](media/testing_screenshots/stripe_element_js_val.png)

* update-remove.js <br>
![image](media/testing_screenshots/base_html_script.png)
