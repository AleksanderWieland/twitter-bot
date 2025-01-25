**Project developed as part of the "Operating Systems" course in the Computer Science program at Cardinal Stefan Wyszyński University in Warsaw.**

The program allows for automatic posting of "tweets" when a specific team scores a goal, concedes a goal, or when another "event" occurs during the team's match. API keys must be stored in a `.env` file.

**API used:** [https://www.api-football.com/](https://www.api-football.com/)

The script initially checks if the team with a given ID is playing a match on the day the script is executed. If a match is scheduled, the script pauses until the match's start time. During the match, it sends periodic GET requests to check for new "events." Currently, the frequency is set in the code to ensure the number of requests during the match does not exceed the free API limits of api-football.

**Recommended usage:** Create a container and set up a Linux cron job to run the script daily after midnight.
