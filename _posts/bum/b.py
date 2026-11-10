for i in range(1,10):
    with open("./urls.txt", "a") as f:
        b = f"\"http://127.0.0.1:{i}/\",\n"
        f.write(b)