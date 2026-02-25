import logging

## logging settings
logging.basicConfig(
    filename="app1.log",
    filemode='w',
    level=logging.DEBUG,
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
    datefmt='%Y - %m - %d %H:%M:%S',
    force= True
    )

    # handlers=[logging.FileHandler("app1.log"),
    #     logging.StreamHandler()])

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a + b
    logger.debug(f"adding {a} and {b} = {result}")
    return result

add(10,15)