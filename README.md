# MediaCloud Python API Client for API testing

This [Media Cloud API client's](https://github.com/c4fcm/MediaCloud-API-Client) fork is being used for testing [Media Cloud's](https://github.com/berkmancenter/mediacloud) API.


## Merging from upstream

To integrate changes from Media Cloud API client's upstream, execute:

    # (Run once) add upstream to remotes
    git remote add upstream https://github.com/c4fcm/MediaCloud-API-Client.git
    
    # Fetch changes from upstream
    git fetch upstream
    
    # Merge in upstream changes
    git checkout master
    git merge upstream/master
    
    # Tag and push changes
    git tag v<latest_version_from_upstream>-api-testing
    git push origin --tags
    
Lastly, update the Media Cloud API client's testing version tag being checked out in Media Cloud's [`.travis.yml`](https://github.com/berkmancenter/mediacloud/blob/master/.travis.yml#L87)
