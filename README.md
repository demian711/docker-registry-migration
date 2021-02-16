Docker Registry migration tool
=========

Purpose if this script is to perform a migration from a given Docker Registry to another one.
Steps that script will perform are:

* Collect all images from source Registry
* Iterate over all images and for each one:
    * Retrieve all tags and for each one:
        * docker pull
        * docker tag with new Registry url
        * docker push to new registry
        * delete local images for source and dest

Two Docker API endpoints are being used for such purpose:

* "/v2/_catalog"
* "/v2/%7B%7Bnamespace/image%7D%7D/tags/list"

---
**NOTE**

Parameter "?n=1000" was added to each endpoint to avoid pagination. Manually increase value if required.

---

### Requirements

This script was thought to be executed with Python3

Required packages can be installed with 

```
$ pip3 install -r requirements.txt

```
You also need pull access to the origin Docker Registry, and push access to destination


### Usage 

Script needs 2 extra arguments to work:

 * `registry_source`: Docker Registry where actual images are allocated
 * `registry_dest`: Docker Registry where images will be pushed to


### Run Example

```
$ python3 'my.old.registry' 'my.new.registry'

```

Author Information
------------------

[Demian Ignacio Sciessere (demian711@hotmail.com)](mailto:demian711@hotmail.com)