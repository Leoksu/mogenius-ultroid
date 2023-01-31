
<b><h3>An Script to deploy ultroid on mogenius.com</h3></b>

# Tutorial

1. Go to [GithubToken](https://github.com/settings/tokens) and create new access token (give all permission)
2. Clone this repo and set it private
<details>
<summary><h3>How to clone?</h3></summary>

- Fork this that you wanna clone first and do the steps below
- **if you in mobile, turn on desktop site** 
  - click plus sign besides your profile icon and select import repository
  - then fill the old repository column with your forked repo link
  - **SET YOUR CLONE REPO TO PRIVATE**
<img src="./resources/extras/screencap.jpg" alt="details">
</details>

---
3. Open the clone of this repo and edit `.env` file with your variables
4. And then open [mogenius](https://mogenius.com/) create new accounts and add cloudspace
5. Then add service and select docker file
6. Connect your GitHub account, select repository, add your clone repository 
7. Slide cpu, ram, disk to maximum
<details>
<summary>Detail pic</summary>
<img src="./resources/extras/slidecpu.jpg" alt="details">
</details>

---
8. Add port `8080` and run it, wait till the deployment complete
- Congratulations, you are done!

# Need help?
- Feel free to ask me when you get problem  [![Contact me](https://img.shields.io/badge/My%20Telegram-blue)](https://t.me/aethersghoul)

### Credits
- This is a modified script for deploy ultroid
- There is [Original](https://github.com/ITZ-ZAID/mogenius) code
- if u use this script, please give both a star ;)
