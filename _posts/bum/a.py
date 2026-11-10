import requests
import os

BASE_URL = "https://sumtext.domain2026.online/"

files = [
    "assets/StudioPage-Bij8WYQZ.js",
    "assets/AdminRepositoryHttp-CYovMZ-t.js",
    "assets/idempotency-TqwnZ0a7.js",
    "assets/index-CkVLxZsN.js",
    "assets/index-B6BPjShS.js",
    "assets/CloseCircleOutlined-D-yZiQ65.js",
    "assets/index-DI4Yi-En.js",
    "assets/index-B1FxZL3t.js",
    "assets/index-CgyO6-08.js",
    "assets/JobDetailModal-D_G3WwJW.js",
    "assets/LinkOutlined-CbBExy88.js",
    "assets/PaperClipOutlined-CDW-bSQC.js",
    "assets/index-DqFPdWuE.js",
    "assets/index-VebvI7Lb.js",
    "assets/DeleteOutlined-BxsaYP_R.js",
    "assets/index-fPl0pKRM.js",
    "assets/index-CG3UKVVX.js",
    "assets/ThunderboltOutlined-Yepo-k4Q.js",
    "assets/JobStageChips-XI4on617.js",
    "assets/HistoryPage-BEQg87tx.js",
    "assets/index-BOsV-2db.js",
    "assets/SummaryRatingModal-BLfReRJo.js",
    "assets/Table-D__wE9AZ.js",
    "assets/StarOutlined-BQFllg99.js",
    "assets/JobsPage-tidXTAeo.js",
    "assets/index-DTdAgami.js",
    "assets/SyncOutlined-DZHE0h-5.js",
    "assets/AdminPage-LsQtPFx2.js",
    "assets/AppstoreOutlined-C8xmm_jn.js",
    "assets/StatisticsPage-BNukEsHu.js",
    "assets/ProfilePage-B9Y2J6uB.js",
    "assets/MailOutlined-t0F_Dj3s.js",
    "assets/ComponentDemoAntd-BwJ0FcBF.js",
]

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0"
})

for path in files:
    url = BASE_URL.rstrip("/") + "/" + path

    try:
        response = session.get(url, timeout=20)
        response.raise_for_status()

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "wb") as f:
            f.write(response.content)

        print(f"[+] Downloaded: {path} ({len(response.content)} bytes)")

    except requests.RequestException as e:
        print(f"[-] Failed: {url} - {e}")

print("\nDone!")