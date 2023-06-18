The web service is powered by Django and Django Rest Framework.
The data is aggregated in the databse and manipulated via ORM.
The models content is serialized to APIs and can be distributed
across multiple frontends.
The API endpoints are divided into several categories, each one 
contains both collection and object endpoints; all of them are still under
version 1.

There is also a user API endpoint hub contains a token authentication
flow.
Besides raw APIs, the web servise itself has got several templates
where there are several kinds of products rendered on.