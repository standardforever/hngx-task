from flask import Flask, request
from datetime import date, datetime, timezone


app = Flask(__name__)


@app.route('/')
def home():
    return ("this is our home page, please navigate to /user to get the requirement you need")


@app.route('/user')
def user():
    """ It returns the user information
    """

    # Get the user slack name and track from query params
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    print(slack_name, track)

    # Get the current day
    today = date.today().weekday()
    days_of_the_week = ['Monday', "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday", "Sunday"]

    response = {
        "status_code": 200,
        "track": track,
        "slack_name": slack_name,
        "current_day": days_of_the_week[today],
        "github_file_url": None,
        "github_repo_url": None,
        "utc_time": datetime.utcnow().replace(tzinfo=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    }


    return (response)


if __name__ == "__main__":
    app.run(debug=True)
