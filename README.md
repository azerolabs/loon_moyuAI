# loon_moyuAI

Converts [ddgksf2013's AI rules](https://ddgksf2013.top/filter/Ai.yaml) into a Loon `.list` rule set. `AI-Loon.list` contains routing rules, not proxy nodes.

Loon remote rule subscription:

```ini
[Remote Rule]
https://raw.githubusercontent.com/azerolabs/loon_moyuAI/main/AI-Loon.list, policy=PROXY, tag=AI, enabled=true
```

Replace `PROXY` with your Loon policy group name.

GitHub Actions checks upstream daily at 08:17 Asia/Shanghai and commits only when the output changes. It can also be run manually with **Actions → Update Loon AI rules → Run workflow**.
