# ✅ update.py — This script fetches LeetCode stats for user `user3012lg`

import requests
from datetime import datetime

USERNAME = "user3012lg"
README_FILE = "README.md"

query = """
{
  matchedUser(username: \"%s\") {
    submitStats {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
""" % USERNAME

url = "https://leetcode.com/graphql"
response = requests.post(url, json={"query": query})
data = response.json()

# Extract counts
easy = data['data']['matchedUser']['submitStats']['acSubmissionNum'][1]['count']
medium = data['data']['matchedUser']['submitStats']['acSubmissionNum'][2]['count']
hard = data['data']['matchedUser']['submitStats']['acSubmissionNum'][3]['count']
total = easy + medium + hard

date = datetime.now().strftime("%Y-%m-%d")

# Update README.md
with open(README_FILE, "w") as f:
    f.write(f"""
# 📊 LeetCode Progress Tracker

Tracking LeetCode stats for user: **{USERNAME}**

| Difficulty | Problems Solved |
|------------|------------------|
| Easy       | {easy} ✅        |
| Medium     | {medium} 🔁      |
| Hard       | {hard} 🔥        |
| **Total**  | **{total}** 💯    |

_Last updated: {date}_
""")

print("README updated successfully!")
