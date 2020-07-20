# danblog_public
The public code for my blog, which can be found at www.danielpdwalker.com.

Its a very simple django blog, hosted on digital ocean, with a postgresql database and making use of the built in admin area to add and maintain my blog posts.

Other than just Django there is obviously a little HTML, a tiny bit of CSS. I make use of the templating system in django, and also ended up adding some pagination.
   
The most recent addition is the ability to search by tags. Including a tag_search page where you can see a list of all the tags I've used on my posts, and see all posts related to them. (Ordered by most recently posted).
