The openface library offer fantastic, state-of-the-art,
functionality for identifying and working with facial
features with a corpus of images. However, the dependencies
required for the library can be fairly daunting to install,
particularly if your application only needs the given
functionality as part of a longer pipeline. This repository
provides a simpler solution: we construct a docker container
that can spin up and deliver a restful API with a single
command. We then supply a client-side request module, written
in python, that queries the API for a given image. Both can
run on the same machine for single-user applications, or
the master can be deployed as a separate instance as part of
a larger analytic pipeline. The server side is a lightweight
Flask app, and should be able to handle reasonably sized
loads.

Once you have docker installed locally and the docker daemon
running, simply clone the repository and start the server:
```
./master/start_server.sh
```
By default it will listen on port `5000`. An example of
querying the API with python is given in the file
`client/test-api.py`. It uses the `OpenFaceClient` class
to query the server. This script can be easily modified
depending on your needs and specific server set up, including
querying from other programing languages.

### API resources

By default, the master node exposes four resources:
* `api/health`: indicates whether the server is up and running
* `api/bbox`: given an image, a list of the bounding boxes for
all detected faces is returned
* `api/features`: given an image, the set of landmarks for each
detected face are returned
* `api/align`: given an image, an aligned representation of each
face is returned
Other resources can be added easily by adding them in the script
`app.py`.

### Image data type



