# 2022_09_22_challenge - Problem 2

This is my solution to Problem 2 of the proposed challenges.  
I chose Python as a language because it is simple to get a development environment going and I know
the most of the syntax and standard library methods by heart, out of all languages I know.

## How to Run

### Locally via pyenv

```sh
pyenv install 3.9.2
pyenv virtualenv 3.9.2 2022_09_22_challenge
pyenv local 2022_09_22_challenge
./entrypoint.sh
```

### Docker

```sh
# Build
docker build -f Dockerfile -t ghcr.io/lolei/2022_09_22_challenge:0.2.1 .
# Or pull
docker pull ghcr.io/lolei/2022_09_22_challenge:0.2.1
# Run
docker run ghcr.io/lolei/2022_09_22_challenge:0.2.1
```

### Tests

```sh
pip install -r requirements-dev.txt # There are no production dependencies, only dev
python -m pytest .
```

See also [`pipelines.sh`](./pipeline.sh) or the [GitHub Actions Workflow](.github/workflows/preliminary.yml).

## Assumptions

- Input lines start with `> `
- No numbers in talk names
- Input lines generally conform to format, although some cleaning is performed
- There can be an infinite number of tracks, not only two
