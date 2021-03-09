# Caesar-Cypher-Container

This container uses allows a user to input text to be encoded by a user defined key. This is a caesar cypher, which works by shifting letters by a key value. For example, if we had the text input of "a" and a key input of "2", the encrypted output would be "c."

### Load Docker Image

To load the Docker image, run the following:
*Key must be an int.*
```
docker pull nathan2warren/caesar_cipher:latest
```

### List docker images
You should see the docker image you have pulled.
```
docker image ls
```

### Run this container
Text is what you wish to encrypt. Key must be an integer.

```
docker run -it nathan2warren/caesar_cypher:latest python app.py --text "text" --key "key"
```

### Exmaple

```
docker run -it nathan2warren/caesar_cypher:latest python app.py --text "abbccc" --key "2"  
> Original: abbccc
> Shift: 2
> Encrypted: cddeee
```


