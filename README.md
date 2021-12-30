[![codecov](https://codecov.io/gh/schmiddim/action-gh-release-info/branch/master/graph/badge.svg?token=LN3DTGWBJN)](https://codecov.io/gh/schmiddim/action-gh-release-info)
[![Python application](https://github.com/schmiddim/action-gh-release-info/actions/workflows/python-app.yaml/badge.svg)](https://github.com/schmiddim/action-gh-release-info/actions/workflows/python-app.yaml)
[![.github/workflows/action.yaml](https://github.com/schmiddim/action-gh-release-info/actions/workflows/action.yaml/badge.svg)](https://github.com/schmiddim/action-gh-release-info/actions/workflows/action.yaml)

# Get Info about a Github Release

This action fetches information about the latest Release for a repo and returns a Download Url for Assets or the Release Tag

## Inputs

## `url`

**Required** Url to Repo

## `download_url_pattern`

**Optional** Pattern to look for 
## Example usage
```
  - name: Get Asset Url for an linux release
    uses: schmiddim/action-gh-release-info@master
    id: hello
    with:
      url: https://github.com/hpool-dev/chia-miner/
      download_url_pattern: .*linux
```
Consume the outputs with
```
${{ steps.hello.outputs.release_url }}
${{ steps.hello.outputs.release_tag }}
```




## Dev 
Run tests
```
PYTHONPATH=. pytest tests/
```
