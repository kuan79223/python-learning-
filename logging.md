# Log檔
![image](https://user-images.githubusercontent.com/112489587/204212454-e3a400e8-dab8-4507-93e8-41a396cc4c62.png)


    import logging

    loger = logging.getLogger('Log模組')

    loger.setLevel(level=logging.INFO)

    format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler = logging.FileHandler('log.txt')

    handler.setLevel(logging.INFO)

    handler.setFormatter(format)

    console = logging.StreamHandler()

    console.setLevel(logging.INFO)

    console.setFormatter(format)

    loger.addHandler(handler)

    loger.addHandler(console)


