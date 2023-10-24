# fast-api-db-template wxo

This project has as its main objective to be a template for FastAPI with Cloudant DB. After that, upload to IBM Cloud.

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python ^3.9](https://www.python.org/downloads/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

* Create a .env file to run the cloudant-rest-db branch
```sh
CLOUDANT_USER=""
CLOUDANT_PWD=""
CLOUDANT_HOST=""
CLOUDANT_DATABASE=""
```

* Create a vcap-local.json file to run the deploy-to-ibm-cloud branch
```sh
{
    "services": {
      "cloudantNoSQLDB": [
        {
          "credentials": {
            "username":"",
            "password":"",
            "host":""
          },
          "label": "cloudantNoSQLDB"
        }
      ]
    }
  }
```

* Install Python3, pip3

### Installation

Once with all prerequisites done, you need install the dependencies:
```sh
pip3 install -r requirements.txt
```
Run the server with:
```sh
uvicorn main:app --reload
```
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Now go to http://127.0.0.1:8000/docs to verify all the routes.
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Matheus Bitencourt - [@matbiit](https://www.linkedin.com/in/matbiit/)

Project Link: [https://github.com/matbiit/fast-api-db-template](https://github.com/matbiit/fast-api-db-template)

<p align="right">(<a href="#top">back to top</a>)</p>

