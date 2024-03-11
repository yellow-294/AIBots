# Task 1

Name: Wee Xin Yang, Markus

## Setup

Clone the repository to your local machine

Locate the root directory of the repository on your machine

Install all the requirements using the command below

```bash
$ pip install -r requirements.txt
```

## Running

Run the command below to compile the bash script

```bash
chmod +x run.sh
```

Run the bash script

```
./run.sh
```

You can now view the app at http://0.0.0.0/docs on your browser

##Summary of functions

Prompts can be added using the final function /prompts/{prompt}
Prompts are to be inputted as strings

When prompts are inputted, a Message object with a unique id is created. Another Message object is formed when the response is given

You can view the id, roles and content of all these messages using /conversations/read_all

The contents can also be updated with the PUT functions. They can also be deleted with the DELETE function.
