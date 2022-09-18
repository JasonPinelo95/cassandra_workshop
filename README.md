# CASSANDRA WORKSHOP

## Learn the basics of cassandra

This workshop is a hands-on introduction to cassandra. It is designed to be run on a single machine, but can be run on multiple machines as well.

## You will learn

* How to install cassandra
* How to start cassandra
* How to create a keyspace
* How to create a table
* How to insert data
* How to query data
* How to update data
* How to delete data

## Prerequisites

* Docker
* Docker Compose
* Python 
* Python virtualenv
* Google Cloud Platform account
* Basic knowledge of Linux
* Bash shell
* Network knowledge

## Running the workshop

### Setup
In order to run the workshop, you need to have a Google Cloud Platform account. You can create one for free [here](https://cloud.google.com/free/).

You also need to have a Google Cloud Platform project. You can create one [here](https://console.cloud.google.com/projectcreate).

Create a new VM instance on Google Cloud Platform. You can do this [here](https://console.cloud.google.com/compute/instancesAdd).

Select the following options:
* Name: cassandra-workshop
* Region: us-central1
* Zone: us-central1-c
* Machine type: e2-standard-2 (2 vCPUs, 8 GB memory)
* Boot disk: Ubuntu 18.04 LTS (x86_64)
* Click on "Create"

SSH into the VM instance. You can do this by clicking on the SSH button in the Google Cloud Platform console.

Optional: For Mac OS X and Linux users, you can also do this by SSHing into the VM in your terminal. You can do this by running the following command:

```$ ssh -i ~/.ssh/<PATH_TO_PUBLIC_KEY> <USERNAME>@<EXTERNAL_IP> ```

Once you are SSHed into the VM, run the following commands one by one:

```$ sudo apt-get update```

```$ sudo apt-get install -y git```

```$ git clone https://github.com/JasonPinelo95/cassandra_workshop.git```

```$ cd cassandra_workshop```

```$ chmod +x givePermissions.sh```

```$ ./givePermissions.sh```

```$ ./installDocker.sh```

```$ ./installPy.sh```

```$ source ~/.bashrc```

```$ pyenv local cassandra```

```$ ./installDependencies.sh```


### Running the workshop

```$ docker-compose up -d```



