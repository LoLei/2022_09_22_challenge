# 2022_09_22_challenge - Problem 2

## How to Run

### Locally via pyenv

```
pyenv install 3.9.2
pyenv virtualenv 3.9.2 2022_09_22_challenge
pyenv local 2022_09_22_challenge
./entrypoint.sh
```

### Docker

```
# Build
docker build -f Dockerfile -t ghcr.io/lolei/2022_09_22_challenge:0.2.0 .
# Or pull
docker pull ghcr.io/lolei/2022_09_22_challenge:0.2.0
# Run
docker run ghcr.io/lolei/2022_09_22_challenge:0.2.0
```

## Assumptions

- Input lines start with `> `
- No numbers in talk names
- Input lines generally conform to format, although some cleaning is performed
- There can be an infinite number of tracks, not only two
