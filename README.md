[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

# Magma Bot

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>

## About The Project

An open-source bot made for  [lavalaph's discord server](https://discord.gg/MeYDgpHGZQ)!

Interested in knowing how the bot works? Wanna try to add some features? Go crazy! Feel free to add any features or fix bugs by <a href="#contributing">creating a pull request</a>. The bot is coded in python using [discord.py](https://github.com/Rapptz/discord.py), you can read their docs [here](https://discordpy.readthedocs.io/en/stable/).

Before starting, keep in mind the bot is ran under a containerized instance, so most windows-like commands or modules will not function, Instead, you may work on the bot using [wsl](https://docs.microsoft.com/en-us/windows/wsl/install-win10#manual-installation-steps).

# Getting Started

## Prerequisites

* Python
  ```sh
  apt install python3
  pip3 install -r requirements.txt
  ```
* MongoDB
  ```sh
  Read the instructions at https://docs.mongodb.com/manual/administration/install-community/ to install MongoDB.
  ```
* A Discord Bot token
  ```
  Read the instructions at https://discordpy.readthedocs.io/en/latest/discord.html#creating-a-bot-account to get a token from discord for a dev bot.
  ```
<i>yes im lazy to type them all out</i>

## Installation

### Using The source code

1. Clone the repo
   ```sh
   git clone https://github.com/Abaan404/MagmaBot
   ```
2. Open your editor of choice and insert your bot token at the end of the file like so
   ```python
   bot.run("PASTEBOTTOKENHERE")
   ```
3. Make sure MongoDB is up and running then run the command in the `./src` directory
   ```sh
   cd ./src
   python3 main.py
   ```

### Using a Docker Container

1. Install Docker using the instructions [here](https://docs.docker.com/get-docker/)
2. Open `docker-compose.yml` and change the BOT_TOKEN env variable to your personal bot token
   ```yml
   environment:
    - BOT_TOKEN=PASTEBOTTOKENHERE
   ```
3. Run the following command to start up the bot. Running the command for the first time will take a while, subsequent runs will be faster.
   ```sh
   docker-compose up -d
   ```
* To stop the bot run `docker-compose down`
* To restart the bot (i.e. to apply changes) run `docker-compose restart`
* To learn more about Docker I recommend [this video](https://youtu.be/zJ6WbK9zFpI?t=160)

# Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch `git checkout -b new-feature-branch`
3. Commit your Changes `git commit -m 'Add some epic new stuff lulz 😎'` 
4. Push to the Branch `git push origin new-feature-branch`
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements
* Used a README Template by [othneildrew](https://github.com/othneildrew/Best-README-Template)

[contributors-shield]: https://img.shields.io/github/contributors/Abaan404/MagmaBot.svg?style=for-the-badge
[contributors-url]: https://github.com/Abaan404/MagmaBot/graphs/contributors
[issues-shield]: https://img.shields.io/github/issues/Abaan404/MagmaBot.svg?style=for-the-badge
[issues-url]: https://github.com/Abaan404/MagmaBot/issues
[license-shield]: https://img.shields.io/github/license/Abaan404/MagmaBot.svg?style=for-the-badge
[license-url]: https://github.com/Abaan404/MagmaBot/blob/master/LICENSE.txt