<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h1 align="center">Daily Leetcode</h1>

  <p align="center">
    A slack bot that automatically sends Leetcode questions.  Users can change the difficulty level and category of the Leetcode question.  Users can also manually request a Leetcode question.
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
 In preparation for technical interviews, my friends and I were discussing ways to reduce friction in doing one technical programming question a day.  As a result, we created a bot that automatically sends a Leetcode question to our Slack channel.  Users can change the difficulty level and category of the Leetcode question.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [Python](https://www.python.org/)
* [Slack API](https://api.slack.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/christietsang/DailyLeetcode.git
   ```
2. Create a new App on Slack API's [website](https://api.slack.com/apps) 

3. Generate your configuration token and sign-in secret on Slack API's website.

4. Create a `.env` file in the folder `daily-leetcode` with the information:
    ```html
    SLACK_TOKEN = <your_configuration_token_here>
    SIGNIN_SECRET = <your_secret_here>
    ```
5. Install dependencies.

6. Change the value returned from `generate_channel_id` to the channel id where you would like to interact with this bot.

7. Host the bot.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

<!-- CONTACT -->
## Contact

Christie Tsang - [LinkedIn](https://www.linkedin.com/in/christietsang/)

Belal Kourkmas - [LinkedIn](https://www.linkedin.com/in/belal-kourkmas/)

Bosco Chan - [LinkedIn](https://www.linkedin.com/in/boscochw/)

Project Link: [https://github.com/christietsang/DailyLeetcode.git](https://github.com/christietsang/DailyLeetcode.git)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/christietsang/DailyLeetcode.svg?style=for-the-badge
[contributors-url]: https://github.com/christietsang/DailyLeetcode/graphs/contributors
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/christietsang/

