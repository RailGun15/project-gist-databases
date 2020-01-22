import requests


def import_gists_to_database(db, username, commit=True):
    
    url = "https://api.github.com/users/"+username+"/gists"
    response = requests.get(url)
    response.raise_for_status()
    cur = db.cursor()
    for item in response.json():
        parameters = {
            "github_id": item['id'],
            "html_url": item['html_url'],
            "git_pull_url": item['git_pull_url'],
            "git_push_url": item['git_push_url'],
            "commits_url": item['commits_url'],
            "forks_url": item['forks_url'],
            "public": item['public'],
            "created_at": item['created_at'],
            "updated_at": item['updated_at'],
            "comments": item['comments'],
            "comments_url": item['comments_url'],
        }
        query = 
        """ INSERT INTO gists (github_id, html_url, git_pull_url, git_push_url, commits_url,
                forks_url, public, created_at,updated_at, comments, comments_url)
            VALUES (:github_id, :html_url, :git_pull_url, :git_push_url, :commits_url, :forks_url,
                :public, :created_at, :updated_at,:comments, :comments_url); """
        cur.execute(query,parameters)
        
    if commit:
        db.commit()
    else:
        return None
