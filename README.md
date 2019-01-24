# Hublog (WIP)

It is a small project that I extracted from my personal blog that I'm building. I put this small project online because I think that it can be helpful for someone else. It is an example of how use Python, Flask, Markdown and Github for basic blogging system. Although I like static blog engines, I would like to extend some features and I write by myself some behaviors. This is why I started this project.


## Requirements
 - You need Python 3.x
 - A Github Account
 - All libraries you can find in [requirements.txt](requirements.txt)

## Installation
Start cloning this repository and installing the [requirements.txt](requirements.txt) properly inside your environment. I recommend to use a virtual env.

```
$ git clone git@github.com:klassmann/hublog.git
```

## Settings
You have to modify the `settings.py` inside `/app`. Add your account information and follow the comments.

## Running

If you want to run locally and use the `/local` folder for testing purpouses. You must run `./run-local` script.

```
$ ./run-local
```

## TODO
- [ ] Add more information in README
- [ ] Add a small cache system
- [ ] Heroku deployment as an example
- [ ] Add tests
- [ ] Improve the quality of code

## License
Apache 2.0
