## Test scenarios for ITS/2019L course
Author: Tibor Kubik(xkubik34@stud.fit.vutbr.cz)
This test plan contains 4 different test suites, each focusing on different element of OpenCart e-shop. I have decided to focus on wider range of elements rather then just one. That is also the goal of my test plan - to test more parts in a superficial way.

Test plan contains following features:
- registration.feature
- shopping_list.feature
- wishlist.feature
- admin_products.feature

### User registration feature
User registration feature contains scenarios testing the process of registration of a **new** user. Most of the scenarios are trying to detect whether system does not allow to register a new user, when he/she does not follow registration instructions.

### Shopping Cart feature
This feature tests actions with shopping cart. As shopping cart is a crucial in the process of product order, feature tests actions like:
- Adding a new item to Shopping Cart
- Changing the quantity of an item
- Deleting one item or all items

### Wish List feature
Wish List is a non-essential part of an e-shop. That means, that even during implementation, plenty of bugs might have been created due to the idea that this module is unimportant. That is the reason why I have decided to test this part. Especially adding new item to a Wish List, redirecting from Wish List to a product, removing an item from a Wish list and remove everything from a Wish List.

### Admin Product Catalog feature
This feature tests actions within product catalog that is modifiable by an administrator. As the product list is being changed constantly in an e-shop, I have decided to test these operations that admin can do:
- Filtration of products within list by number of filters
- Removing a product
- Removing all products
- Editing a product
