# eCommerce Application

This is an eCommerce application built using Django web framework and hosted on AWS. The application includes features such as product listings, shopping cart functionality, and checkout functionality. It uses various AWS services for database storage, file storage, and deployment.

## Functional Requirements
- Users can browse product listings
- Users can add products to their shopping cart
- Users can remove products from their shopping cart
- Users can filter and search for products
- Users can checkout and complete their purchase

## Non-functional Requirements
- The application should be scalable to handle increasing traffic and demand
- The application should be secure to protect user data and prevent unauthorized access
- The application should be performant to provide a smooth user experience

## Architecture
The application uses the following AWS services:
- Amazon RDS for PostgreSQL: for database storage
- Amazon S3: for file storage
- Amazon Elastic Beanstalk: for application deployment
- Amazon CodePipeline: for continuous integration and deployment

The application is built using the Django web framework and follows a typical Django application structure. The `settings.py` file contains the settings for the project, and various application folders such as `accounts`, `cart`, and `products` contain the application code.

## Getting Started
To run the application locally, follow these steps:

1. Clone the repository
2. Install the required dependencies using `pip install -r requirements.txt`
3. Set up the database by running `python manage.py migrate`
4. Create a superuser account by running `python manage.py createsuperuser`
5. Start the development server by running `python manage.py runserver`

## Deployment
Please note that the servers used for this project were part of a college AWS learners lab and are no longer available. Therefore, the application cannot be accessed or deployed.

The application was originally deployed on AWS Elastic Beanstalk using CodePipeline. Any changes pushed to the master branch of the repository would have triggered a new deployment.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
