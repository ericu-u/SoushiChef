# SwampHacks 2022 Submission
This project was created as a submission to [SwampHacks 2022](https://swamphacks.notion.site/SwampHacks-VIII-Hacker-Guide-1d4a8b027b9647cd88f29764b6d87a9a).
**Team Members**:  *Jonathan Lo and Eric Wang*

## SoushiChef
SoushiChef is a WebApp and voice assistant designed to be your personal Sous Chef in the kitchen. SoushiChef offers a wide variety of meals and will help guide you to make the perfect dish using voice commands, precise and understandable quantities, time keeping, and much more!

## Running SoushiChef
In order to run SoushiChef locally, you will need its dependencies and an Assembly AI Key.
### Set Up
 1. Clone the repository.
 2. Install pipenv and Django.
 3. Create a `config.txt` and input the Assembly AI Key according to `config.text.example`
 4. Configure database in `settings.py` to local settings (We use MySQL)
 5. Start local server using: 
  ```
  python3 manage.py runserver
  ```


## Tech Stack
The backend is entirely written in Python using the [Django](https://www.djangoproject.com/) framework. The frontend is written in HTML and CSS with some JS. SoushiChef utilizes [Assembley AI's](https://www.assemblyai.com/) API for real time voice commands and NLP. Database
