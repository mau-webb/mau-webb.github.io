# MAU Webb

Public platform for Open Educational Resources (OER) from Malmö University (MaU). Published at:

> https://mau-webb.github.io

## Getting started

This site is made with [Jekyll](http://jekyllrb.com) and published with [GitHub Pages](https://pages.github.com/). Be sure to read up on both [Jekyll](http://jekyllrb.com) and [Using Jekyll with Pages](https://help.github.com/articles/using-jekyll-with-pages) before contributing.

To get started:

1. Clone this repository

```bash
git clone https://github.com/mau-webb/mau-webb.github.io.git
cd mau-webb.github.io
```

2. Install dependencies

```bash
gem install bundle -v 2.4.22 # ignore if bundle is already installed
bundle install
```

3. Build and preview the site locally at `http://localhost:4000`

```bash
bundle exec jekyll serve
```
or with automatic rebuilds
```bash
bundle exec jekyll serve --incremental
```

You should now be up and running locally!

## Structure

### The `_data` directory

In the `_data` directory you will find a `resources` folder containing a lot of YAML files that contain data connected to a specific course. This is where you can add and remove courses from being displayed on the site. This is also where sidebar navigation is defined for each course.

### The `resurser` directory

In the `resurser` directory you will find a folder for each course. Each course folder contains a `index.md` file that is the main page for that course. This is also where all the course material is stored such as exercises, lectures, and other resources.

## Contributing

If you want to contribute to this project, please do so by forking the repository and submitting a pull request. If you have any questions, feel free to open an issue.

## License

Everything is published under [The MIT License](https://mit-license.org).
