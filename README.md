# Get Info about a Github Release

This action fetches information about the latest Release for a repo and returns a Download Url for Assets or the Release Tag

## Inputs

## `url`

**Required** Url to Repo
## `mode`

**Required**  asset_url || release_tag
## `download_url_pattern`

Pattern to look for 
## Example usage
```
uses: actions/schmiddim-action-gh-release-info@v1
with:
  url: https://github.com/hpool-dev/chia-miner/
  mode: download_url_pattern
  download_url_pattern: .*linux
```

Output will be stored in **release_info**
