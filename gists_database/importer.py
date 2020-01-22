import requests


def import_gists_to_database(db, username, commit=True):
    keys = ["id","html_url","git_pull_url","git_push_url",
            "commits_url","forks_url","public","created_at",
           "updated_at","comments","comments_url"]
    
    url = "https://api.github.com/users/"+username+"/gists"
    response = requests.get(url)
    response.raise_for_status()
    data_list = []
    for item in response.json():
        data_dict = {key: val for key,val in item.items() if key in keys}
        data_list.append(data_dict)
    cur = db.cursor()
    for item in data_list:
        query = """ INSERT INTO gists (forks_url,commits_url,github_id,git_pull_url,git_push_url,html_url,
        public,created_at,updated_at,comments,comments_url)
        VALUES (?,?,?,?,?,?,?,?,?,?,?); """
        vals = tuple(item.values())
        cur.execute(query,(vals[0],vals[1],vals[2],vals[3],vals[4],vals[5],vals[6],vals[7],
                           vals[8],vals[9],vals[10]))
        
    if commit:
        db.commit()
    else:
        return None
