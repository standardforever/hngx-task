from flask import Flask, request
from datetime import date, datetime, timezone


app = Flask(__name__)



@app.route('/')
def user():
    """ It returns the user information
    """

    # Get the user slack name and track from query params
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day
    today = date.today().weekday()
    days_of_the_week = ['Monday', "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday", "Sunday"]

    response = {
        "status_code": 200,
        "track": track,
        "slack_name": slack_name,
        "current_day": days_of_the_week[today],
        "github_file_url": "https://github.com/standardforever/hngx-task/blob/main/task.py",
        "github_repo_url": "https://github.com/standardforever/hngx-task",
        "utc_time": datetime.utcnow().replace(tzinfo=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    }


    return (response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

